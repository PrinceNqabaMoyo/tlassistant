"""Subskills 17 to 24: 3D Surface Area, Coating & Painting Calculations.
Covers closed rectangular boxes, open-top pools, closed and open cylindrical drums,
window/door deductions, spread rates with multiple coats, paint tin optimization, and corrugated roofing overlaps.
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


def gen_subskill_17(r: random.Random) -> Dict[str, Any]:
    """Subskill 17: Surface area of a closed rectangular cardboard carton."""
    l = r.choice([40, 50, 60])  # in cm
    w = r.choice([30, 40])
    h = r.choice([20, 25, 30])

    # SA = 2(lw + lh + wh)
    sa_cm2 = 2 * (l * w + l * h + w * h)
    sa_m2 = round(sa_cm2 / 10000.0, 4)

    prompt = (
        f"A packaging manufacturer produces a closed rectangular cardboard shipping box with dimensions:\n"
        f"• Length: {l} cm\n"
        f"• Width: {w} cm\n"
        f"• Height: {h} cm\n\n"
        f"Using the formula: Total Surface Area = 2 × (l × w + l × h + w × h),\n"
        f"calculate the total surface area of cardboard required for one closed carton in square centimetres (cm²)."
    )

    correct_ans = f"{_fmt(sa_cm2)} cm²"
    explanation = (
        f"1. Top & bottom faces: 2 × ({l} × {w}) = {2 * l * w} cm².\n"
        f"2. Front & back faces: 2 × ({l} × {h}) = {2 * l * h} cm².\n"
        f"3. Left & right faces: 2 × ({w} × {h}) = {2 * w * h} cm².\n"
        f"4. Total Surface Area = {2 * l * w} + {2 * l * h} + {2 * w * h} = {correct_ans}."
    )
    t1 = f"Calculate the three face pairs: ({l}×{w}), ({l}×{h}), and ({w}×{h})."
    t2 = f"Sum the three face areas: {l*w} + {l*h} + {w*h} = {l*w + l*h + w*h} cm²."
    t3 = f"Multiply by 2: 2 × {l*w + l*h + w*h} = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_17",
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


def gen_subskill_18(r: random.Random) -> Dict[str, Any]:
    """Subskill 18: Interior surface area of an open-top rectangular swimming pool."""
    l = r.choice([6.0, 8.0, 10.0])
    w = r.choice([3.0, 4.0, 5.0])
    d = r.choice([1.5, 1.8, 2.0])  # depth

    # Open top = Floor (lw) + 2 long walls (2 * l * d) + 2 short walls (2 * w * d)
    floor_area = l * w
    walls_area = 2 * (l * d) + 2 * (w * d)
    total_interior_sa = round(floor_area + walls_area, 2)

    prompt = (
        f"A contractor is lining the interior surface of a new rectangular swimming pool with spray-on marbelite cement.\n"
        f"The pool has the following interior dimensions:\n"
        f"• Length: {_fmt(l)} m\n"
        f"• Width: {_fmt(w)} m\n"
        f"• Uniform depth: {_fmt(d)} m\n\n"
        f"Notice that the pool is open at the top (it has 1 floor and 4 vertical walls).\n"
        f"Using the formula: Surface Area = (l × w) + 2 × (l × d) + 2 × (w × d),\n"
        f"calculate the total surface area to be coated in square metres (m²)."
    )

    correct_ans = f"{_fmt(total_interior_sa)} m²"
    explanation = (
        f"1. Floor area = {_fmt(l)} m × {_fmt(w)} m = {_fmt(floor_area)} m².\n"
        f"2. Long walls area (2 walls) = 2 × ({_fmt(l)} m × {_fmt(d)} m) = {_fmt(2 * l * d)} m².\n"
        f"3. Short walls area (2 walls) = 2 × ({_fmt(w)} m × {_fmt(d)} m) = {_fmt(2 * w * d)} m².\n"
        f"4. Total interior surface area = {_fmt(floor_area)} + {_fmt(2 * l * d)} + {_fmt(2 * w * d)} = {correct_ans}."
    )
    t1 = f"Calculate the floor: {l} × {w} = {floor_area} m²."
    t2 = f"Calculate the 4 walls: 2×({l}×{d}) + 2×({w}×{d}) = {walls_area} m²."
    t3 = f"Sum floor and walls: {floor_area} + {walls_area} = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_18",
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


def gen_subskill_19(r: random.Random) -> Dict[str, Any]:
    """Subskill 19: Total surface area of a closed cylindrical geyser / storage tank."""
    diameter = r.choice([0.6, 0.8, 1.0])  # in metres
    radius = diameter / 2.0
    height = r.choice([1.5, 1.8, 2.0])

    # TSA = 2*pi*r^2 + 2*pi*r*h
    circular_ends = 2 * PI * (radius ** 2)
    curved_surface = 2 * PI * radius * height
    tsa = round(circular_ends + curved_surface, 3)

    prompt = (
        f"An industrial cylindrical hot water storage geyser has a diameter of {_fmt(diameter)} m "
        f"(radius = {_fmt(radius)} m) and a height of {_fmt(height)} m.\n"
        f"The geyser is completely closed at both ends.\n\n"
        f"Using the formula: Total Surface Area = 2 × π × r² + 2 × π × r × h (where π = 3,142),\n"
        f"calculate the total exterior surface area in square metres (m²) rounded to 3 decimal places."
    )

    correct_ans = f"{_fmt(tsa, 3)} m²"
    explanation = (
        f"1. Area of 2 circular ends = 2 × 3,142 × ({_fmt(radius)})² = 2 × 3,142 × {radius**2:.4f} = {circular_ends:.4f} m².\n"
        f"2. Curved surface area = 2 × 3,142 × {_fmt(radius)} × {_fmt(height)} = {curved_surface:.4f} m².\n"
        f"3. Total Surface Area = {circular_ends:.4f} + {curved_surface:.4f} = {tsa:.3f} m² = {correct_ans}."
    )
    t1 = f"Calculate the 2 circular ends: 2 × 3,142 × ({radius})²."
    t2 = f"Calculate the curved wall: 2 × 3,142 × {radius} × {height}."
    t3 = f"Sum both components: {circular_ends:.3f} + {curved_surface:.3f} = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_19",
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


def gen_subskill_20(r: random.Random) -> Dict[str, Any]:
    """Subskill 20: Curved surface area of an open cylindrical storm water drainage pipe."""
    diameter = r.choice([0.5, 0.6, 0.8, 1.2])  # metres
    radius = diameter / 2.0
    length = r.choice([3.0, 4.0, 5.0, 6.0])    # length of pipe

    # Curved SA = 2 * pi * r * h = pi * d * h
    curved_sa = round(PI * diameter * length, 2)

    prompt = (
        f"A concrete storm water drainage pipe has an outer diameter of {_fmt(diameter)} m "
        f"and an axial length of {_fmt(length)} m.\n"
        f"Since water flows through both open ends, only the outer curved cylinder wall requires waterproof bitumen coating.\n\n"
        f"Using the formula: Curved Surface Area = π × diameter × length (where π = 3,142),\n"
        f"calculate the curved surface area to be coated (rounded to 2 decimal places)."
    )

    correct_ans = f"{_fmt(curved_sa)} m²"
    explanation = (
        f"1. Formula: Curved Area = π × d × L.\n"
        f"2. Substitution: Curved Area = 3,142 × {_fmt(diameter)} m × {_fmt(length)} m = {correct_ans}."
    )
    t1 = f"Multiply π (3,142) by diameter ({_fmt(diameter)} m) and length ({_fmt(length)} m)."
    t2 = f"Calculation: 3,142 × {diameter} × {length}."
    t3 = f"Curved area = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_20",
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


def gen_subskill_21(r: random.Random) -> Dict[str, Any]:
    """Subskill 21: Wall painting area calculation: subtracting window and door opening areas."""
    room_l = r.choice([4.5, 5.0, 5.5])
    room_w = r.choice([3.5, 4.0, 4.5])
    room_h = 2.8

    gross_walls = 2 * (room_l + room_w) * room_h
    door_area = 1.0 * 2.0
    window_area = 1.5 * 1.2
    openings_area = door_area + window_area
    net_paint_area = round(gross_walls - openings_area, 2)

    d_spec_21 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Bedroom Floor Plan ({_fmt(room_l)} m x {_fmt(room_w)} m)",
        "rooms": [{"name": "Bedroom", "length_m": room_l, "width_m": room_w, "height_m": room_h}],
    }

    prompt = (
        f"Refer to the bedroom floor plan measuring {_fmt(room_l)} m long, {_fmt(room_w)} m wide, and {_fmt(room_h)} m high.\n"
        f"The room contains:\n"
        f"• 1 door measuring 1,0 m wide by 2,0 m high (Area = 2,0 m²)\n"
        f"• 1 window measuring 1,5 m wide by 1,2 m high (Area = 1,8 m²)\n\n"
        f"Calculate the net wall surface area that will actually be painted in square metres (m²)."
    )

    correct_ans = f"{_fmt(net_paint_area)} m²"
    explanation = (
        f"1. Gross perimeter of walls = 2 × ({_fmt(room_l)} m + {_fmt(room_w)} m) = {2 * (room_l + room_w)} m.\n"
        f"2. Gross wall area = {2 * (room_l + room_w)} m × {_fmt(room_h)} m = {_fmt(gross_walls)} m².\n"
        f"3. Openings to deduct = Door (2,0 m²) + Window (1,8 m²) = {_fmt(openings_area)} m².\n"
        f"4. Net paint area = {_fmt(gross_walls)} m² - {_fmt(openings_area)} m² = {correct_ans}."
    )
    t1 = f"Calculate gross wall area: 2 × ({room_l} + {room_w}) × {room_h} = {_fmt(gross_walls)} m²."
    t2 = f"Subtract door (2,0 m²) and window (1,8 m²): {_fmt(gross_walls)} - 3,8."
    t3 = f"Net area = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_21",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_21,
    )


def gen_subskill_22(r: random.Random) -> Dict[str, Any]:
    """Subskill 22: Paint volume calculation based on spread rate and 2 coats of paint."""
    wall_area = r.choice([48.0, 60.0, 72.0, 84.0])
    spread_rate = 8.0  # 8 m² per litre
    coats = 2

    total_coverage = wall_area * coats
    litres_needed = round(total_coverage / spread_rate, 2)

    prompt = (
        f"A homeowner needs to paint a total wall area of {_fmt(wall_area)} m² with two (2) coats of acrylic PVA paint.\n"
        f"The manufacturer's paint tin label specifies a spread rate of 8 m² per litre per coat.\n\n"
        f"Calculate the total volume of paint required in litres (L)."
    )

    correct_ans = f"{_fmt(litres_needed)} L"
    explanation = (
        f"1. Total surface area for 2 coats = {_fmt(wall_area)} m² × 2 = {_fmt(total_coverage)} m².\n"
        f"2. Volume of paint required = Total coverage ÷ Spread rate\n"
        f"   = {_fmt(total_coverage)} m² ÷ 8 m²/L = {correct_ans}."
    )
    t1 = f"Multiply the wall area ({_fmt(wall_area)} m²) by 2 coats = {_fmt(total_coverage)} m²."
    t2 = f"Divide the total coverage ({_fmt(total_coverage)} m²) by the spread rate (8 m²/L)."
    t3 = f"Litres needed = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_22",
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


def gen_subskill_23(r: random.Random) -> Dict[str, Any]:
    """Subskill 23: Paint tin combination optimization: 5 L and 1 L tins."""
    litres_needed = r.choice([11.0, 12.0, 13.0, 14.0])
    # 5L tin costs R 320; 1L tin costs R 95
    price_5l = 320.00
    price_1l = 95.00

    # Option A: Two 5L tins (10L) + remaining 1L tins
    tins_5l = 2
    rem_litres = litres_needed - 10.0
    tins_1l = int(rem_litres)

    cost_optimized = (tins_5l * price_5l) + (tins_1l * price_1l)

    # Option B: Three 5L tins (15L) = 3 * 320 = 960
    cost_3_5l = 3 * price_5l

    final_cheapest = min(cost_optimized, cost_3_5l)

    prompt = (
        f"A decorating project requires exactly {int(litres_needed)} litres of interior paint.\n"
        f"Paint is sold in two tin sizes:\n"
        f"• 5-litre tin: {_fmt_curr(price_5l)}\n"
        f"• 1-litre tin: {_fmt_curr(price_1l)}\n\n"
        f"Determine the cheapest combination of tins to purchase at least {int(litres_needed)} litres, and calculate the total cost."
    )

    correct_ans = _fmt_curr(final_cheapest)
    explanation = (
        f"1. Evaluating combination 1: Two 5 L tins (10 L) + {tins_1l} × 1 L tins = {int(litres_needed)} L.\n"
        f"   Cost = (2 × {_fmt_curr(price_5l)}) + ({tins_1l} × {_fmt_curr(price_1l)}) = {_fmt_curr(cost_optimized)}.\n"
        f"2. Evaluating combination 2: Three 5 L tins (15 L).\n"
        f"   Cost = 3 × {_fmt_curr(price_5l)} = {_fmt_curr(cost_3_5l)}.\n"
        f"3. Cheapest option = {correct_ans}."
    )
    t1 = f"Compare buying two 5 L tins plus individual 1 L tins versus buying three 5 L tins."
    t2 = f"Calculate the total cost of each viable combination."
    t3 = f"Cheapest cost = {correct_ans}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_23",
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


def gen_subskill_24(r: random.Random) -> Dict[str, Any]:
    """Subskill 24: Roof sheeting surface area and corrugated iron sheets with overlap."""
    roof_length_m = 9.6  # 960 cm length of roof ridge
    sheet_width_cm = 85.0
    overlap_cm = 15.0  # side corrugation overlap
    effective_sheet_width_cm = sheet_width_cm - overlap_cm  # 70 cm = 0,7 m

    roof_length_cm = roof_length_m * 100  # 960 cm
    sheets_needed = int((roof_length_cm + effective_sheet_width_cm - 1) // effective_sheet_width_cm)

    prompt = (
        f"A shed roof has a ridge length of {_fmt(roof_length_m)} m ({int(roof_length_cm)} cm).\n"
        f"Corrugated iron roof sheets have a gross nominal width of 85 cm.\n"
        f"When installing adjacent sheets, a 15 cm side-overlap is required to prevent rainwater leakage.\n\n"
        f"Calculate the minimum number of sheets needed to cover this length of the roof (rounded up to the next whole sheet)."
    )

    correct_ans = f"{sheets_needed} sheets"
    explanation = (
        f"1. Effective coverage width per sheet = Gross Width ({sheet_width_cm} cm) - Overlap ({overlap_cm} cm) = {effective_sheet_width_cm} cm.\n"
        f"2. Number of sheets = Total roof length ÷ Effective width\n"
        f"   = {int(roof_length_cm)} cm ÷ {effective_sheet_width_cm} cm = {roof_length_cm / effective_sheet_width_cm:.2f} sheets.\n"
        f"3. Round up to whole sheets: {sheets_needed} sheets."
    )
    t1 = f"Subtract the 15 cm overlap from 85 cm to find the effective width ({effective_sheet_width_cm} cm)."
    t2 = f"Divide the roof length ({int(roof_length_cm)} cm) by the effective width ({effective_sheet_width_cm} cm)."
    t3 = f"Round up to the next whole sheet: {sheets_needed} sheets."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_meas_subskill_24",
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
