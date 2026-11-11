"""Subskills 1 to 8: Municipal Water & Sanitation Tariffs.
Covers stepped water blocks, multi-tier calculations, sanitation percentage billing,
leak surge analysis, municipal comparisons, reverse volume derivation, and drought tariffs.
"""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    SA_MUNICIPALITIES,
    VAT_RATE,
    _fmt,
    _fmt_curr,
    _build_options,
    _build_question_payload,
)


def gen_subskill_01(r: random.Random) -> Dict[str, Any]:
    """Subskill 01: Interpreting municipal residential water sliding scale blocks."""
    muni = r.choice(SA_MUNICIPALITIES)
    vol = r.randint(18, 28)

    prompt = (
        f"A domestic water tariff schedule for {muni} displays the following monthly stepped tariff structure (excl. VAT):\n\n"
        f"• Block 1: 0 to 6 kL @ Free (R 0,00/kL)\n"
        f"• Block 2: > 6 to 15 kL @ R 18,50/kL\n"
        f"• Block 3: > 15 to 30 kL @ R 27,20/kL\n"
        f"• Block 4: > 30 kL @ R 38,40/kL\n\n"
        f"If a household consumes {vol} kL of water during a billing cycle, how many kilolitres (kL) "
        f"will be billed specifically at the Block 3 rate of R 27,20/kL?"
    )

    kL_in_block_3 = vol - 15
    correct_ans = f"{kL_in_block_3} kL"
    explanation = (
        f"1. In a stepped sliding scale tariff, water usage is divided into intervals.\n"
        f"2. Block 1 covers the first 6 kL (0 to 6 kL = 6 kL).\n"
        f"3. Block 2 covers the next 9 kL (6 to 15 kL = 9 kL).\n"
        f"4. Block 3 applies to all usage between 15 kL and 30 kL. Here, total volume is {vol} kL.\n"
        f"5. Volume billed in Block 3 = {vol} - 15 = {kL_in_block_3} kL."
    )
    t1 = "Subtract the maximum threshold of Block 2 (15 kL) from the total water consumed."
    t2 = f"Block 1 covers 6 kL, Block 2 covers 9 kL (total 15 kL). The rest ({vol} - 15) falls in Block 3."
    t3 = f"Calculate: {vol} - 15 = {kL_in_block_3} kL."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_01",
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
    """Subskill 02: Calculating monthly water cost within Block 2."""
    name = r.choice(SA_NAMES)
    muni = r.choice(SA_MUNICIPALITIES)
    vol = r.randint(8, 14)
    rate_b2 = r.choice([16.50, 18.20, 20.40, 22.10])

    # Block 1 (0-6 kL) is free; Block 2 (>6 to 15 kL) is charged at rate_b2
    charge_excl_vat = round((vol - 6) * rate_b2, 2)
    charge_incl_vat = round(charge_excl_vat * (1 + VAT_RATE), 2)

    prompt = (
        f"{name}'s household in {muni} used {vol} kL of water in June.\n"
        f"The municipal tariff table states:\n"
        f"• Block 1 (0 to 6 kL): R 0,00 per kL\n"
        f"• Block 2 (> 6 to 15 kL): {_fmt_curr(rate_b2)} per kL (excl. VAT)\n\n"
        f"Calculate the total water charge including 15% VAT."
    )

    correct_ans = _fmt_curr(charge_incl_vat)
    explanation = (
        f"1. Volume in Block 1 (0 to 6 kL) = 6 kL @ R 0,00 = R 0,00.\n"
        f"2. Volume in Block 2 = {vol} - 6 = {vol - 6} kL.\n"
        f"3. Cost excl. VAT = {vol - 6} kL × {_fmt_curr(rate_b2)} = {_fmt_curr(charge_excl_vat)}.\n"
        f"4. Add 15% VAT: {_fmt_curr(charge_excl_vat)} × 1,15 = {_fmt_curr(charge_incl_vat)}."
    )
    t1 = "Calculate the number of kL in Block 2 by subtracting the free 6 kL."
    t2 = f"Multiply {vol - 6} kL by {_fmt_curr(rate_b2)}, then add 15% VAT."
    t3 = f"Cost = ({vol - 6} × {rate_b2}) × 1,15 = {_fmt_curr(charge_incl_vat)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_02",
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


def gen_subskill_03(r: random.Random) -> Dict[str, Any]:
    """Subskill 03: Calculating multi-tier water charges across 3 blocks with VAT."""
    name = r.choice(SA_NAMES)
    muni = r.choice(SA_MUNICIPALITIES)
    vol = r.randint(19, 27)

    r1 = 0.0
    r2 = r.choice([17.50, 19.80, 21.00])
    r3 = r.choice([28.40, 31.50, 34.00])

    cost_b1 = 6 * r1
    cost_b2 = 9 * r2
    cost_b3 = (vol - 15) * r3
    total_excl = round(cost_b1 + cost_b2 + cost_b3, 2)
    total_incl = round(total_excl * (1 + VAT_RATE), 2)

    prompt = (
        f"{name}'s family in {muni} used {vol} kL of water last month.\n"
        f"The municipal domestic stepped tariff rates (excl. VAT) are:\n"
        f"• Step 1 (0 to 6 kL): R 0,00/kL\n"
        f"• Step 2 (> 6 to 15 kL): {_fmt_curr(r2)}/kL\n"
        f"• Step 3 (> 15 to 30 kL): {_fmt_curr(r3)}/kL\n\n"
        f"Calculate the total water charge payable including 15% VAT."
    )

    correct_ans = _fmt_curr(total_incl)
    explanation = (
        f"1. Step 1 (0 to 6 kL): 6 kL × R 0,00 = R 0,00.\n"
        f"2. Step 2 (6 to 15 kL): 9 kL × {_fmt_curr(r2)} = {_fmt_curr(cost_b2)}.\n"
        f"3. Step 3 (15 to {vol} kL): {vol - 15} kL × {_fmt_curr(r3)} = {_fmt_curr(cost_b3)}.\n"
        f"4. Total excl. VAT = {_fmt_curr(cost_b2)} + {_fmt_curr(cost_b3)} = {_fmt_curr(total_excl)}.\n"
        f"5. Total incl. 15% VAT = {_fmt_curr(total_excl)} × 1,15 = {_fmt_curr(total_incl)}."
    )
    t1 = "Break the usage into three steps: first 6 kL, next 9 kL, and remaining usage above 15 kL."
    t2 = "Sum the cost of each step to find total cost excl. VAT, then multiply by 1,15."
    t3 = f"Total = ({cost_b2} + {cost_b3}) × 1,15 = {_fmt_curr(total_incl)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_03",
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


def gen_subskill_04(r: random.Random) -> Dict[str, Any]:
    """Subskill 04: Sanitation / Sewerage charge calculated as percentage of water consumption."""
    name = r.choice(SA_NAMES)
    muni = r.choice(SA_MUNICIPALITIES)
    water_vol = r.randint(18, 30)
    pct = r.choice([70, 75, 80])
    sanitation_rate = r.choice([14.50, 16.20, 18.00])

    sewer_vol = round(water_vol * (pct / 100.0), 2)
    sewer_cost_excl = round(sewer_vol * sanitation_rate, 2)
    sewer_cost_incl = round(sewer_cost_excl * (1 + VAT_RATE), 2)

    prompt = (
        f"{muni} calculates domestic sanitation (sewerage) charges based on {pct}% of the monthly water consumption.\n"
        f"{name}'s household consumed {water_vol} kL of water during the month.\n"
        f"The sanitation tariff is {_fmt_curr(sanitation_rate)} per kL (excl. VAT).\n\n"
        f"Calculate the total sanitation charge including 15% VAT."
    )

    correct_ans = _fmt_curr(sewer_cost_incl)
    explanation = (
        f"1. Volume billed for sanitation = {pct}% of {water_vol} kL = {_fmt(sewer_vol)} kL.\n"
        f"2. Sanitation cost excl. VAT = {_fmt(sewer_vol)} kL × {_fmt_curr(sanitation_rate)} = {_fmt_curr(sewer_cost_excl)}.\n"
        f"3. Sanitation cost incl. 15% VAT = {_fmt_curr(sewer_cost_excl)} × 1,15 = {_fmt_curr(sewer_cost_incl)}."
    )
    t1 = f"Calculate {pct}% of {water_vol} kL to determine billable sanitation volume."
    t2 = f"Multiply billable volume by {_fmt_curr(sanitation_rate)} and add 15% VAT."
    t3 = f"Charge = ({sewer_vol} × {sanitation_rate}) × 1,15 = {_fmt_curr(sewer_cost_incl)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_04",
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


def gen_subskill_05(r: random.Random) -> Dict[str, Any]:
    """Subskill 05: Water leak detection via meter readings and financial penalty across high blocks."""
    name = r.choice(SA_NAMES)
    normal_vol = r.randint(14, 18)
    leak_vol = normal_vol + r.randint(22, 35)

    r_normal = 19.50
    r_high = 48.00  # punitive top tier for > 30 kL

    extra_kL = leak_vol - normal_vol
    added_cost_excl = round(extra_kL * r_high, 2)
    added_cost_incl = round(added_cost_excl * (1 + VAT_RATE), 2)

    prompt = (
        f"{name}'s municipal water bill showed an undetected underground pipe leak:\n"
        f"• Previous meter reading: 1 420 kL\n"
        f"• Current meter reading: {1420 + leak_vol} kL (Total used: {leak_vol} kL)\n"
        f"Under normal conditions, the household consumes {normal_vol} kL per month.\n"
        f"All water consumed above 30 kL is billed at the punitive top tier of {_fmt_curr(r_high)} per kL (excl. VAT).\n\n"
        f"Assuming the entire excess volume of {extra_kL} kL was billed at this top tier rate,\n"
        f"calculate the additional cost added to the bill by the leak (including 15% VAT)."
    )

    correct_ans = _fmt_curr(added_cost_incl)
    explanation = (
        f"1. Excess water volume caused by leak = {leak_vol} kL - {normal_vol} kL = {extra_kL} kL.\n"
        f"2. Additional cost excl. VAT = {extra_kL} kL × {_fmt_curr(r_high)} = {_fmt_curr(added_cost_excl)}.\n"
        f"3. Additional cost incl. 15% VAT = {_fmt_curr(added_cost_excl)} × 1,15 = {_fmt_curr(added_cost_incl)}."
    )
    t1 = "Find the excess water volume by subtracting normal volume from total volume."
    t2 = f"Multiply the excess volume ({extra_kL} kL) by the top tier rate ({_fmt_curr(r_high)})."
    t3 = f"Calculate: ({extra_kL} × {r_high}) × 1,15 = {_fmt_curr(added_cost_incl)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_05",
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


def gen_subskill_06(r: random.Random) -> Dict[str, Any]:
    """Subskill 06: Water tariff comparison between two South African metropolitan municipalities."""
    vol = 25  # 25 kL consumed

    # Metro A: 0-6 free, 6-15 @ R18, 15-30 @ R28
    cost_a = (9 * 18.00) + (10 * 28.00)  # excl VAT = 162 + 280 = 442
    cost_a_incl = round(cost_a * 1.15, 2)

    # Metro B: 0-6 @ R10, 6-15 @ R16, 15-30 @ R25
    cost_b = (6 * 10.00) + (9 * 16.00) + (10 * 25.00)  # excl VAT = 60 + 144 + 250 = 454
    cost_b_incl = round(cost_b * 1.15, 2)

    diff = round(abs(cost_a_incl - cost_b_incl), 2)
    cheaper = "City A" if cost_a_incl < cost_b_incl else "City B"

    prompt = (
        f"A comparative municipal study evaluates domestic water charges for a household using 25 kL/month:\n\n"
        f"City A Tariff (excl. VAT):\n"
        f"• 0 to 6 kL: Free\n"
        f"• > 6 to 15 kL: R 18,00/kL\n"
        f"• > 15 to 30 kL: R 28,00/kL\n\n"
        f"City B Tariff (excl. VAT):\n"
        f"• 0 to 6 kL: R 10,00/kL\n"
        f"• > 6 to 15 kL: R 16,00/kL\n"
        f"• > 15 to 30 kL: R 25,00/kL\n\n"
        f"Calculate the difference in total monthly water charges (incl. 15% VAT) between the two cities."
    )

    correct_ans = _fmt_curr(diff)
    explanation = (
        f"1. City A total: (9 kL × R 18,00) + (10 kL × R 28,00) = R 162,00 + R 280,00 = R 442,00 excl. VAT.\n"
        f"   Incl. 15% VAT = R 442,00 × 1,15 = {_fmt_curr(cost_a_incl)}.\n"
        f"2. City B total: (6 kL × R 10,00) + (9 kL × R 16,00) + (10 kL × R 25,00) = R 60 + R 144 + R 250 = R 454,00 excl. VAT.\n"
        f"   Incl. 15% VAT = R 454,00 × 1,15 = {_fmt_curr(cost_b_incl)}.\n"
        f"3. Difference = |{_fmt_curr(cost_a_incl)} - {_fmt_curr(cost_b_incl)}| = {_fmt_curr(diff)}."
    )
    t1 = "Calculate total cost incl. VAT for City A and City B separately for 25 kL."
    t2 = "City A has free first 6 kL; City B charges for all kL. Compute both totals."
    t3 = f"Difference = |{_fmt_curr(cost_a_incl)} - {_fmt_curr(cost_b_incl)}| = {_fmt_curr(diff)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_06",
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
    """Subskill 07: Reverse tariff problem: finding total volume consumed given total charge."""
    name = r.choice(SA_NAMES)
    muni = r.choice(SA_MUNICIPALITIES)
    # Block 1: 0-6 kL @ R0
    # Block 2: 6-15 kL @ R20/kL
    # Block 3: >15 kL @ R30/kL
    # Suppose volume in Block 3 is kL_b3 (between 3 and 10 kL)
    kL_b3 = r.randint(3, 10)
    vol_actual = 15 + kL_b3
    cost_excl = (9 * 20.00) + (kL_b3 * 30.00)
    cost_incl = round(cost_excl * 1.15, 2)

    prompt = (
        f"{name}'s municipal water bill from {muni} for the month of October is {_fmt_curr(cost_incl)} (incl. 15% VAT).\n"
        f"The tariff schedule (excl. VAT) is:\n"
        f"• Block 1 (0 to 6 kL): Free (R 0,00)\n"
        f"• Block 2 (> 6 to 15 kL): R 20,00 per kL\n"
        f"• Block 3 (> 15 to 30 kL): R 30,00 per kL\n\n"
        f"Determine the total volume of water in kilolitres (kL) consumed by {name}."
    )

    correct_ans = f"{vol_actual} kL"
    explanation = (
        f"1. Remove 15% VAT: {_fmt_curr(cost_incl)} ÷ 1,15 = {_fmt_curr(cost_excl)} excl. VAT.\n"
        f"2. Block 1 (0 to 6 kL) cost = R 0,00.\n"
        f"3. Block 2 (6 to 15 kL = 9 kL) cost = 9 × R 20,00 = R 180,00.\n"
        f"4. Remaining amount in Block 3 = {_fmt_curr(cost_excl)} - R 180,00 = {_fmt_curr(kL_b3 * 30.00)}.\n"
        f"5. Volume in Block 3 = R {kL_b3 * 30.00:.2f} ÷ R 30,00/kL = {kL_b3} kL.\n"
        f"6. Total volume = 15 kL + {kL_b3} kL = {vol_actual} kL."
    )
    t1 = "First divide the bill by 1,15 to find cost before VAT."
    t2 = "Subtract the cost of Block 2 (9 kL × R 20,00 = R 180,00), then divide remainder by R 30,00/kL."
    t3 = f"Total volume = 15 + {kL_b3} = {vol_actual} kL."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_07",
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
    """Subskill 08: Drought restriction penalty tariff on high-volume consumption."""
    name = r.choice(SA_NAMES)
    vol = r.randint(22, 28)

    # Standard vs Drought tariff for >15 to 30 kL
    # 0-6: R0, 6-15: R18
    # Standard 15-30: R26/kL; Drought 15-30: R42/kL
    std_b3_rate = 26.00
    drought_b3_rate = 42.00

    vol_b3 = vol - 15
    cost_diff_excl = vol_b3 * (drought_b3_rate - std_b3_rate)
    cost_diff_incl = round(cost_diff_excl * 1.15, 2)

    prompt = (
        f"During a municipal drought emergency, Level 3 water restrictions were enacted in {name}'s town.\n"
        f"The tariff for Block 3 (> 15 to 30 kL) increased from the standard {_fmt_curr(std_b3_rate)}/kL "
        f"to {_fmt_curr(drought_b3_rate)}/kL (both excl. VAT).\n"
        f"Blocks 1 and 2 rates remained unchanged.\n\n"
        f"If {name}'s household consumed {vol} kL during the month,\n"
        f"calculate how much extra the household paid due to the drought restriction tariff (incl. 15% VAT)."
    )

    correct_ans = _fmt_curr(cost_diff_incl)
    explanation = (
        f"1. Volume affected by Block 3 increase = {vol} kL - 15 kL = {vol_b3} kL.\n"
        f"2. Rate difference = {_fmt_curr(drought_b3_rate)} - {_fmt_curr(std_b3_rate)} = {_fmt_curr(drought_b3_rate - std_b3_rate)} per kL excl. VAT.\n"
        f"3. Extra cost excl. VAT = {vol_b3} kL × {_fmt_curr(drought_b3_rate - std_b3_rate)} = {_fmt_curr(cost_diff_excl)}.\n"
        f"4. Extra cost incl. 15% VAT = {_fmt_curr(cost_diff_excl)} × 1,15 = {_fmt_curr(cost_diff_incl)}."
    )
    t1 = "Find the volume falling in Block 3 by subtracting 15 kL from total usage."
    t2 = f"Multiply the Block 3 volume ({vol_b3} kL) by the tariff difference ({_fmt_curr(drought_b3_rate - std_b3_rate)})."
    t3 = f"Add 15% VAT: ({vol_b3} × {drought_b3_rate - std_b3_rate}) × 1,15 = {_fmt_curr(cost_diff_incl)}."

    opts, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        "gr12_tariffs_subskill_08",
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
