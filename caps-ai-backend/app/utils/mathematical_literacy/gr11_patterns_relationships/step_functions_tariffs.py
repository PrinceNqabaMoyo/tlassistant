"""Step-function relationships and discrete tariff systems (Subskills 28-36) for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
)


def generate_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Parking garage fee table and step-function graph interpretation (hourly tiers)."""
    name = r.choice(SA_NAMES)
    t1 = r.choice([10.0, 15.0])
    t2 = t1 * 2
    t3 = t1 * 3 + r.choice([5.0, 10.0])
    t4 = t3 + r.choice([15.0, 20.0])

    case = r.choice([
        ("1 hour and 30 minutes", t2, "1 to 2 hours"),
        ("2 hours and 45 minutes", t3, "2 to 4 hours"),
        ("4 hours and 30 minutes", t4, "4 to 6 hours"),
    ])
    duration, fee, interval = case
    ans_str = _fmt_curr(fee)

    prompt = (
        f"{name} parked a car in an urban shopping mall parking garage for {duration}.\n"
        f"The parking tariff board displays:\n"
        f"• 0 to 1 hour: {_fmt_curr(t1)}\n"
        f"• 1 to 2 hours: {_fmt_curr(t2)}\n"
        f"• 2 to 4 hours: {_fmt_curr(t3)}\n"
        f"• 4 to 6 hours: {_fmt_curr(t4)}\n\n"
        f"Determine the parking fee that {name} must pay."
    )
    explanation = (
        f"Step 1: Check interval: {duration} falls in the '{interval}' interval. [1 mark]\n"
        f"Step 2: Read the corresponding tariff for this interval: {_fmt_curr(fee)}. [1 mark]\n"
        f"Step 3: State the parking fee:\n"
        f"\\text{{Parking fee}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(t1),
        _fmt_curr(t2 if fee != t2 else t3),
        _fmt_curr(t4 if fee != t4 else t3 + 10),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    diagram_spec = {
        "diagram_role": "context",
        "kind": "step_tariff",
        "diagram_type": "step_tariff",
        "title": f"Shopping Mall Parking Garage Step Tariff ({name})",
        "x_label": "Duration (hours)",
        "y_label": "Fee (R)",
        "steps": [
            {"label": "0 to 1 hr", "min": 0, "max": 1, "rate": t1},
            {"label": "1 to 2 hr", "min": 1, "max": 2, "rate": t2},
            {"label": "2 to 4 hr", "min": 2, "max": 4, "rate": t3},
            {"label": "4 to 6 hr", "min": 4, "max": 6, "rate": t4},
        ],
    }
    return _build_question_payload(
        "subskill_28",
        prompt,
        ans_str,
        options,
        explanation,
        f"Locate the interval containing {duration} (between {interval}).",
        f"The fee for {interval} is {_fmt_curr(fee)}.",
        f"Fee = {ans_str}.",
        r,
        diagram_spec=diagram_spec,
        difficulty="easy",
    )


def generate_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Reading values from a step-function graph with open and closed interval dots."""
    prompt = (
        "On a step-function graph representing postal courier tariffs, a solid (closed) dot appears at (2; 45) "
        "and a hollow (open) circle appears at (2; 25).\n\n"
        "What is the exact tariff charged for a parcel weighing exactly 2,0 kg?"
    )
    correct = "R 45,00 (the solid dot indicates the value included at exactly 2,0 kg)"
    distractors = [
        "R 25,00 (the hollow circle indicates the value included at exactly 2,0 kg)",
        "R 35,00 (the average of the two endpoints)",
        "R 70,00 (the sum of both tariff bands)",
    ]
    options, _ = _build_options(correct, r, [correct] + distractors)
    explanation = (
        "Step 1: Understand mathematical conventions for step functions:\n"
        "A solid (filled) dot indicates that the endpoint value IS included in that tier. [1 mark]\n"
        "A hollow (open) circle indicates that the point is NOT included in that tier. [1 mark]\n"
        "Step 2: Apply to 2,0 kg: the solid dot is at R 45,00. [1 mark]\n"
        f"\\text{{Conclusion}} = {correct}."
    )
    return _build_question_payload(
        "subskill_29",
        prompt,
        correct,
        options,
        explanation,
        "Solid dot means included; hollow circle means excluded.",
        "The solid dot at R 45,00 is the included value for 2,0 kg.",
        f"Answer = {correct}.",
        r,
        difficulty="medium",
    )


def generate_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Explaining why a step-function graph consists of disconnected horizontal segments."""
    prompt = (
        "In a Mathematical Literacy assessment, why are the horizontal line segments of a step-function graph "
        "drawn disconnected from one another rather than joined by vertical or diagonal lines?\n"
    )
    correct = (
        "Because moving across a boundary immediately triggers a completely new fixed charge, and vertical connections would falsely suggest multiple costs for the same input."
    )
    distractors = [
        "Because the printer ran out of ink while rendering the Cartesian axes.",
        "Because the rate of change is infinite and undefined everywhere.",
        "Because the government only allows graphs to be drawn with disconnected dashes.",
    ]
    options, _ = _build_options(correct, r, [correct] + distractors)
    explanation = (
        "Step 1: Analyse the physical reality of stepped billing: as soon as you exceed 1 hour by even 1 second, "
        "the cost jumps instantaneously to the next bracket. [1 mark]\n"
        "Step 2: Mathematical validity: joining them with vertical lines would imply that for one specific time, "
        "multiple different prices exist simultaneously. [1 mark]\n"
        "Step 3: State the correct reason:\n"
        f"\\text{{Conclusion}} = {correct}. [1 mark]"
    )
    return _build_question_payload(
        "subskill_30",
        prompt,
        correct,
        options,
        explanation,
        "A tariff jump means the cost changes instantly to a new bracket.",
        "Vertical lines would mean a single time has multiple costs, which is impossible.",
        f"Answer = {correct}.",
        r,
        difficulty="medium",
    )


def generate_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Postal / courier parcel mass step tariffs."""
    name = r.choice(SA_NAMES)
    parcel_mass = 3.4  # kg -> falls in 3 to 5 kg tier
    # Tiers: 0-1 kg = R 65; 1-3 kg = R 95; 3-5 kg = R 135; 5-10 kg = R 195
    cost = 135.0
    ans_str = _fmt_curr(cost)

    prompt = (
        f"{name} sends a parcel weighing 3,4 kg via a domestic express courier.\n"
        f"The courier applies the following mass-band pricing table:\n"
        f"• Up to 1 kg: R 65,00\n"
        f"• Exceeding 1 kg up to 3 kg: R 95,00\n"
        f"• Exceeding 3 kg up to 5 kg: R 135,00\n"
        f"• Exceeding 5 kg up to 10 kg: R 195,00\n\n"
        f"Determine the delivery cost for {name}'s 3,4 kg parcel."
    )
    explanation = (
        f"Step 1: Locate 3,4 kg in the table intervals: 3,4 kg is 'Exceeding 3 kg up to 5 kg'. [1 mark]\n"
        f"Step 2: Read across to the fee column: R 135,00. [1 mark]\n"
        f"Step 3: State the delivery cost:\n"
        f"\\text{{Delivery cost}} = {ans_str}. [1 mark]"
    )
    distractors = [
        "R 95,00",
        "R 195,00",
        "R 115,00",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_31",
        prompt,
        ans_str,
        options,
        explanation,
        "3,4 kg is greater than 3 kg and less than 5 kg, so it falls in the R 135 bracket.",
        "Fee = R 135,00.",
        f"Cost = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Minibus taxi fare stages along a commuter route."""
    name = r.choice(SA_NAMES)
    distance_km = 14.0  # km -> Stage 2 (10 to 20 km)
    # Stage 1 (0-10 km) = R 15,00
    # Stage 2 (10-20 km) = R 22,00
    # Stage 3 (20-35 km) = R 32,00
    fare = 22.0
    ans_str = _fmt_curr(fare)

    prompt = (
        f"{name} commutes 14 km to work every morning using a local minibus taxi service.\n"
        f"The taxi association charges according to route stages:\n"
        f"• Stage 1 (0 to 10 km): R 15,00\n"
        f"• Stage 2 (Exceeding 10 km up to 20 km): R 22,00\n"
        f"• Stage 3 (Exceeding 20 km up to 35 km): R 32,00\n\n"
        f"What is the single-trip taxi fare for {name}'s 14 km journey?"
    )
    explanation = (
        f"Step 1: Identify that 14 km is greater than 10 km and less than or equal to 20 km. [1 mark]\n"
        f"Step 2: Look up Stage 2 on the fare schedule: R 22,00. [1 mark]\n"
        f"Step 3: State the single-trip fare:\n"
        f"\\text{{Fare}} = {ans_str}. [1 mark]"
    )
    distractors = [
        "R 15,00",
        "R 32,00",
        "R 18,50",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_32",
        prompt,
        ans_str,
        options,
        explanation,
        "14 km falls into Stage 2 (10 to 20 km).",
        "Stage 2 fare = R 22,00.",
        f"Fare = {ans_str}.",
        r,
        difficulty="easy",
    )


def generate_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Cellular airtime billing: per-minute billing step function vs per-second billing."""
    name = r.choice(SA_NAMES)
    duration_seconds = 75  # 1 minute 15 seconds
    # Per-minute billing: 75 seconds rounds up to 2 whole minutes at R 1,50/min -> R 3,00
    # Per-second billing: 75 seconds * (R 1,50 / 60) = 75 * R 0,025 = R 1,875 -> R 1,88
    per_minute_cost = 3.00
    per_second_cost = round(duration_seconds * (1.50 / 60.0), 2)
    diff = round(per_minute_cost - per_second_cost, 2)
    ans_str = _fmt_curr(diff)

    prompt = (
        f"{name} makes a cellphone call lasting 1 minute and 15 seconds (75 seconds).\n"
        f"The advertised call rate is R 1,50 per minute.\n"
        f"• Plan A uses per-minute billing (any fraction of a minute is charged as a full minute).\n"
        f"• Plan B uses pure per-second billing (R 1,50 ÷ 60 = R 0,025 per second).\n\n"
        f"Calculate how much more {name} pays under Plan A compared to Plan B."
    )
    explanation = (
        f"Step 1: Calculate Plan A cost (75 seconds rounds up to 2 full minutes):\n"
        f"\\text{{Plan A}} = 2 \\times 1,50 = {_fmt_curr(per_minute_cost)}. [1 mark]\n"
        f"Step 2: Calculate Plan B cost (75 seconds at R 0,025/sec):\n"
        f"\\text{{Plan B}} = 75 \\times 0,025 = {_fmt_curr(per_second_cost)}. [1 mark]\n"
        f"Step 3: Subtract to find the difference:\n"
        f"3,00 - {per_second_cost:.2f} = {diff:.2f}.\n"
        f"\\text{{Difference}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(per_minute_cost),
        _fmt_curr(per_second_cost),
        _fmt_curr(round(diff * 1.5, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_33",
        prompt,
        ans_str,
        options,
        explanation,
        "Plan A charges for 2 full minutes (R 3,00). Plan B charges for 75 seconds (R 1,88). Subtract the two.",
        f"A = R 3,00. B = 75 × 0,025 = {_fmt_curr(per_second_cost)}. Difference = {_fmt_curr(diff)}.",
        f"Extra cost = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Municipal water stepped tariff calculation (Free basic water + tiered blocks)."""
    name = r.choice(SA_NAMES)
    consumption_kl = 18.0  # kL
    # Block 1 (0 to 6 kL): Free (R 0,00)
    # Block 2 (6 to 15 kL): R 14,50 per kL -> 9 kL * 14,50 = R 130,50
    # Block 3 (15 to 30 kL): R 22,00 per kL -> (18 - 15) = 3 kL * 22,00 = R 66,00
    b1_cost = 0.0
    b2_cost = 9.0 * 14.50  # 130.50
    b3_cost = 3.0 * 22.00  # 66.00
    total_water = round(b1_cost + b2_cost + b3_cost, 2)
    ans_str = _fmt_curr(total_water)

    prompt = (
        f"A municipality bills domestic households using a stepped water block tariff:\n"
        f"• Block 1 (0 to 6 kL): Free Basic Water (R 0,00 / kL)\n"
        f"• Block 2 (> 6 up to 15 kL): R 14,50 per kL\n"
        f"• Block 3 (> 15 up to 30 kL): R 22,00 per kL\n\n"
        f"If {name}'s household consumes 18 kL of water in a month,\n"
        f"calculate the total water consumption charge (excluding VAT)."
    )
    explanation = (
        f"Step 1: Break down the 18 kL into blocks:\n"
        f"- Block 1: First 6 kL at R 0,00 = R 0,00\n"
        f"- Block 2: Next 9 kL (from 6 to 15 kL) at R 14,50 = {_fmt_curr(b2_cost)}\n"
        f"- Block 3: Remaining 3 kL (from 15 to 18 kL) at R 22,00 = {_fmt_curr(b3_cost)}. [1 mark]\n"
        f"Step 2: Sum the charges for all blocks:\n"
        f"\\text{{Total}} = 0,00 + 130,50 + 66,00 = {total_water:.2f} [1 mark]\n"
        f"Step 3: State the total bill:\n"
        f"\\text{{Total water charge}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(round(consumption_kl * 22.00, 2)),  # Charged all at block 3 rate
        _fmt_curr(round(consumption_kl * 14.50, 2)),
        _fmt_curr(round(total_water + 35, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_34",
        prompt,
        ans_str,
        options,
        explanation,
        "First 6 kL is free. Next 9 kL at R 14,50. Remaining 3 kL at R 22,00. Add them together.",
        f"Block 2 = 9 × 14,50 = {_fmt_curr(b2_cost)}. Block 3 = 3 × 22 = {_fmt_curr(b3_cost)}. Total = {_fmt_curr(total_water)}.",
        f"Total charge = {ans_str}.",
        r,
        difficulty="hard",
    )


def generate_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Combined tariff: Base connection fee + stepped excess charges."""
    base_charge = 150.0  # Network charge
    consumption = 25.0   # kL
    # Block 1 (0-10 kL): R 12,00/kL -> 10 * 12 = R 120
    # Block 2 (>10 kL): R 20,00/kL -> 15 * 20 = R 300
    water_cost = (10.0 * 12.0) + (15.0 * 20.0)  # 420
    grand_total = round(base_charge + water_cost, 2)
    ans_str = _fmt_curr(grand_total)

    prompt = (
        f"A commercial water account has a fixed infrastructure service charge of {_fmt_curr(base_charge)} per month, "
        f"plus stepped consumption charges:\n"
        f"• First 10 kL: R 12,00 per kL\n"
        f"• Excess over 10 kL: R 20,00 per kL\n\n"
        f"Calculate the total bill for consuming 25 kL of water."
    )
    explanation = (
        f"Step 1: Calculate the stepped consumption charges:\n"
        f"- First 10 kL = 10 \\times 12,00 = R 120,00\n"
        f"- Excess (25 - 10 = 15 kL) = 15 \\times 20,00 = R 300,00\n"
        f"\\text{{Total water charge}} = 120 + 300 = {_fmt_curr(water_cost)}. [1 mark]\n"
        f"Step 2: Add the fixed service charge of R 150,00:\n"
        f"\\text{{Grand Total}} = 150 + 420 = {grand_total:.2f} [1 mark]\n"
        f"Step 3: State the final total bill:\n"
        f"\\text{{Total bill}} = {ans_str}. [1 mark]"
    )
    distractors = [
        _fmt_curr(water_cost),
        _fmt_curr(round(base_charge + (consumption * 20.0), 2)),
        _fmt_curr(round(grand_total + 80, 2)),
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_35",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate consumption charges in two blocks (10 × 12 and 15 × 20) and add the R 150 base fee.",
        f"Water = 120 + 300 = 420. Grand total = 150 + 420 = {_fmt_curr(grand_total)}.",
        f"Total bill = {ans_str}.",
        r,
        difficulty="medium",
    )


def generate_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Compare continuous linear billing vs stepped discrete billing for water consumption."""
    consumption = 20.0  # kL
    # Plan 1 (Flat linear rate): R 18,00 per kL -> 20 * 18 = R 360
    # Plan 2 (Stepped tariff): 0-6 kL free; 6-15 kL (9 kL) @ R 15; >15 kL (5 kL) @ R 25 -> 0 + 135 + 125 = R 260
    cost_linear = consumption * 18.0  # 360
    cost_stepped = (9.0 * 15.0) + (5.0 * 25.0)  # 260
    diff = round(cost_linear - cost_stepped, 2)
    ans_str = f"Stepped tariff is cheaper by {_fmt_curr(diff)}"

    prompt = (
        f"A resident compares two municipal water billing plans for an expected monthly consumption of 20 kL:\n"
        f"• Plan A (Flat linear rate): R 18,00 per kL for all water consumed\n"
        f"• Plan B (Stepped block tariff): 0 to 6 kL Free; next 9 kL at R 15,00/kL; remaining 5 kL at R 25,00/kL\n\n"
        f"Calculate the cost under both plans for 20 kL and determine which plan is cheaper, and by how much."
    )
    explanation = (
        f"Step 1: Calculate Plan A cost: 20 \\times 18,00 = {_fmt_curr(cost_linear)}. [1 mark]\n"
        f"Step 2: Calculate Plan B cost: (9 \\times 15,00) + (5 \\times 25,00) = 135 + 125 = {_fmt_curr(cost_stepped)}. [1 mark]\n"
        f"Step 3: Subtract to compare: 360 - 260 = {diff:.2f}.\n"
        f"\\text{{Conclusion}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"Flat linear rate is cheaper by {_fmt_curr(diff)}",
        f"Stepped tariff is cheaper by {_fmt_curr(round(diff * 1.5, 2))}",
        "Both plans cost the exact same amount",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_36",
        prompt,
        ans_str,
        options,
        explanation,
        "Calculate Plan A (20 × 18 = R 360) and Plan B (135 + 125 = R 260), then compare.",
        f"Plan A = {_fmt_curr(cost_linear)}. Plan B = {_fmt_curr(cost_stepped)}. Difference = {_fmt_curr(diff)}.",
        f"Outcome = {ans_str}.",
        r,
        difficulty="hard",
    )
