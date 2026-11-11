"""Time formats, decimal time conversions, and elapsed time (Subskills 37-44) for Grade 11 Mathematical Literacy."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_CITIES,
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def generate_subskill_37(r: random.Random) -> Dict[str, Any]:
    """Decimal hours to hours and minutes (e.g., 3,45 h = 3 h 27 min)."""
    name = r.choice(SA_NAMES)
    hours_int = r.randint(2, 6)
    mins_int = r.choice([12, 15, 18, 24, 30, 36, 42, 45, 48, 54])
    decimal_part = round(mins_int / 60.0, 2)
    dec_hours = hours_int + decimal_part
    ans_str = f"{hours_int} h {mins_int} min"

    prompt = (
        f"{name}'s digital timesheet recorded a total duration of {_fmt(dec_hours)} hours for a maintenance project.\n"
        f"Convert this duration to hours and minutes.\n"
        f"*(Note: Multiply the decimal fraction of an hour by 60 to find the minutes.)*"
    )
    explanation = (
        f"Step 1: Identify whole hours and decimal fraction:\n"
        f"\\text{{Whole hours}} = {hours_int}\\text{{ h}}; \\text{{Fraction}} = {_fmt(decimal_part)}\\text{{ h}}. [1 mark]\n"
        f"Step 2: Convert the decimal fraction to minutes by multiplying by 60:\n"
        f"\\text{{Minutes}} = {_fmt(decimal_part)} \\times 60 = {mins_int}\\text{{ min}}. [1 mark]\n"
        f"Step 3: Combine hours and minutes:\n"
        f"\\text{{Time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{hours_int} h {int(decimal_part * 100)} min",
        f"{hours_int} h {max(5, mins_int - 10)} min",
        f"{hours_int + 1} h {mins_int} min",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_37",
        prompt,
        ans_str,
        options,
        explanation,
        "Multiply the decimal part by 60 to find the minutes.",
        f"Calculate {_fmt(decimal_part)} × 60 = {mins_int} minutes.",
        f"Duration = {ans_str}.",
        r,
    )


def generate_subskill_38(r: random.Random) -> Dict[str, Any]:
    """Hours and minutes to decimal hours (e.g., 2 h 15 min = 2,25 h)."""
    name = r.choice(SA_NAMES)
    h = r.randint(1, 5)
    m = r.choice([15, 30, 45, 20, 40, 50])
    dec_val = round(h + (m / 60.0), 2)
    ans_str = f"{_fmt(dec_val)} h"

    prompt = (
        f"{name} worked for {h} hours and {m} minutes on a consulting assignment. "
        f"To calculate billable pay, the payroll system requires the duration in decimal hours.\n"
        f"Convert {h} hours and {m} minutes to decimal hours.\n"
        f"*(Round off to 2 decimal places if necessary.)*"
    )
    explanation = (
        f"Step 1: Convert minutes to a fraction of an hour by dividing by 60:\n"
        f"\\text{{Minutes as fraction}} = {m} \\div 60 = {m / 60.0:.4f}\\text{{ h}}. [1 mark]\n"
        f"Step 2: Add the decimal fraction to the whole hours:\n"
        f"\\text{{Total}} = {h} + {m / 60.0:.4f} = {dec_val:.4f}\\text{{ h}} [1 mark]\n"
        f"Step 3: Round off to 2 decimal places:\n"
        f"\\text{{Duration}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(h + (m / 100.0))} h",
        f"{_fmt(round(dec_val + 0.25, 2))} h",
        f"{_fmt(round(dec_val - 0.15, 2))} h",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_38",
        prompt,
        ans_str,
        options,
        explanation,
        "Divide the minutes by 60, then add to the whole hours.",
        f"Calculate {h} + ({m} ÷ 60).",
        f"Decimal hours = {ans_str}.",
        r,
    )


def generate_subskill_39(r: random.Random) -> Dict[str, Any]:
    """12-hour clock (am/pm) to 24-hour clock notation."""
    name = r.choice(SA_NAMES)
    is_pm = r.choice([True, False])
    hour_12 = r.randint(1, 11)
    minute = r.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
    ampm = "p.m." if is_pm else "a.m."

    if is_pm:
        hour_24 = hour_12 + 12
    else:
        hour_24 = hour_12

    ans_str = f"{hour_24:02d}:{minute:02d}"

    prompt = (
        f"A medical appointment for {name} is scheduled for {hour_12}:{minute:02d} {ampm}.\n"
        f"Write this appointment time in standard 24-hour clock format."
    )
    explanation = (
        f"Step 1: Check whether the time is a.m. or p.m.:\n"
        f"The time is {ampm}. [1 mark]\n"
        f"Step 2: Apply the 24-hour rule:\n"
        + (f"For p.m. times after 12:59, add 12 to the hour: {hour_12} + 12 = {hour_24}.\n" if is_pm else f"For a.m. times, the hour remains unchanged: {hour_24:02d}.\n")
        + f"[1 mark]\n"
        f"Step 3: Write in four-digit 24-hour format:\n"
        f"\\text{{24-hour time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{(hour_24 + 1) % 24:02d}:{minute:02d}",
        f"{(hour_12):02d}:{minute:02d}" if is_pm else f"{hour_12 + 12:02d}:{minute:02d}",
        f"{hour_24:02d}:{(minute + 15) % 60:02d}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_39",
        prompt,
        ans_str,
        options,
        explanation,
        "If p.m., add 12 to the hour (except 12 p.m.). If a.m., keep the hour as is with leading zeros.",
        f"Convert {hour_12}:{minute:02d} {ampm} to 24-hour format.",
        f"Time = {ans_str}.",
        r,
    )


def generate_subskill_40(r: random.Random) -> Dict[str, Any]:
    """24-hour clock notation to 12-hour clock (am/pm)."""
    name = r.choice(SA_NAMES)
    is_pm = r.choice([True, False])
    hour_12 = r.randint(1, 11)
    minute = r.choice([10, 15, 25, 30, 45, 50])
    hour_24 = hour_12 + 12 if is_pm else hour_12
    time_24 = f"{hour_24:02d}:{minute:02d}"
    ans_str = f"{hour_12}:{minute:02d} {'p.m.' if is_pm else 'a.m.'}"

    prompt = (
        f"A passenger train departs Johannesburg station at {time_24}.\n"
        f"Express this departure time in 12-hour clock format (using a.m. or p.m.)."
    )
    explanation = (
        f"Step 1: Check whether the 24-hour hour value is 12 or greater:\n"
        f"The hour is {hour_24:02d}. [1 mark]\n"
        f"Step 2: Determine 12-hour hour and period:\n"
        + (f"Since {hour_24} \\ge 12, subtract 12 from the hour: {hour_24} - 12 = {hour_12}, and designate p.m.\n" if is_pm else f"Since {hour_24} < 12, the hour is {hour_12} and designates a.m.\n")
        + f"[1 mark]\n"
        f"Step 3: State the final 12-hour time:\n"
        f"\\text{{Time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{hour_12}:{minute:02d} {'a.m.' if is_pm else 'p.m.'}",
        f"{(hour_12 + 1) % 12 or 12}:{minute:02d} {'p.m.' if is_pm else 'a.m.'}",
        f"{hour_24}:{minute:02d} {'p.m.' if is_pm else 'a.m.'}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_40",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract 12 if the hour is 13 or greater to get p.m., or keep it as a.m. if below 12.",
        f"Convert {time_24} to 12-hour notation.",
        f"Time = {ans_str}.",
        r,
    )


def generate_subskill_41(r: random.Random) -> Dict[str, Any]:
    """Elapsed time calculation within the same day."""
    name = r.choice(SA_NAMES)
    dep_h = r.randint(7, 10)
    dep_m = r.choice([15, 30, 45])
    dur_h = r.randint(3, 5)
    dur_m = r.choice([15, 30, 45])

    arr_m_total = dep_m + dur_m
    arr_h = dep_h + dur_h + (arr_m_total // 60)
    arr_m = arr_m_total % 60

    ans_str = f"{dur_h} h {dur_m} min"

    prompt = (
        f"{name} departed {SA_CITIES[0]} by car at {dep_h:02d}:{dep_m:02d} and arrived in "
        f"{SA_CITIES[1]} at {arr_h:02d}:{arr_m:02d} on the same day.\n"
        f"Calculate the total elapsed travel time in hours and minutes."
    )
    explanation = (
        f"Step 1: Set up the subtraction (Arrival time - Departure time):\n"
        f"{arr_h:02d}:{arr_m:02d} - {dep_h:02d}:{dep_m:02d}. [1 mark]\n"
        f"Step 2: Subtract minutes and hours:\n"
        f"\\text{{Hours difference}} = {arr_h} - {dep_h} = {arr_h - dep_h}\\text{{ h}}\n"
        f"Adjusting for minutes gives {dur_h}\\text{{ h and }} {dur_m}\\text{{ min}}. [1 mark]\n"
        f"Step 3: State the final elapsed time:\n"
        f"\\text{{Elapsed time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{dur_h + 1} h {dur_m} min",
        f"{dur_h} h {abs(dur_m - 15)} min",
        f"{dur_h - 1} h {dur_m + 30} min",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_41",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract departure time from arrival time, borrowing 60 minutes from hours if needed.",
        f"Calculate {arr_h:02d}:{arr_m:02d} - {dep_h:02d}:{dep_m:02d}.",
        f"Elapsed time = {ans_str}.",
        r,
    )


def generate_subskill_42(r: random.Random) -> Dict[str, Any]:
    """Elapsed time crossing midnight (overnight travel)."""
    name = r.choice(SA_NAMES)
    dep_h = r.randint(20, 22)
    dep_m = r.choice([15, 30, 45])
    dur_h = r.randint(6, 9)
    dur_m = r.choice([10, 20, 30, 40])

    # Time to midnight: (24:00 - dep)
    mins_to_midnight = ((24 - dep_h) * 60) - dep_m
    total_dur_mins = (dur_h * 60) + dur_m
    mins_after_midnight = total_dur_mins - mins_to_midnight
    arr_h = mins_after_midnight // 60
    arr_m = mins_after_midnight % 60

    ans_str = f"{dur_h} h {dur_m} min"

    prompt = (
        f"A long-distance coach carrying {name} left Pretoria at {dep_h:02d}:{dep_m:02d} at night and "
        f"arrived in Durban at {arr_h:02d}:{arr_m:02d} the following morning.\n"
        f"Calculate the total journey time in hours and minutes."
    )
    explanation = (
        f"Step 1: Calculate the time from departure to midnight (24:00):\n"
        f"24:00 - {dep_h:02d}:{dep_m:02d} = {mins_to_midnight // 60}\\text{{ h }} {mins_to_midnight % 60}\\text{{ min}}. [1 mark]\n"
        f"Step 2: Add the time travelled after midnight until arrival ({arr_h:02d}:{arr_m:02d}):\n"
        f"\\text{{Time after midnight}} = {arr_h}\\text{{ h }} {arr_m}\\text{{ min}}. [1 mark]\n"
        f"Step 3: Combine both durations:\n"
        f"({mins_to_midnight // 60}\\text{{ h }} {mins_to_midnight % 60}\\text{{ min}}) + "
        f"({arr_h}\\text{{ h }} {arr_m}\\text{{ min}}) = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{dur_h + 1} h {dur_m} min",
        f"{dur_h} h {(dur_m + 15) % 60} min",
        f"{dur_h - 1} h {dur_m} min",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_42",
        prompt,
        ans_str,
        options,
        explanation,
        "Split the calculation: calculate time until midnight (24:00), then add the time after midnight.",
        f"Time to midnight = 24:00 - {dep_h:02d}:{dep_m:02d}. Add {arr_h:02d}:{arr_m:02d}.",
        f"Journey duration = {ans_str}.",
        r,
    )


def generate_subskill_43(r: random.Random) -> Dict[str, Any]:
    """Determining arrival time given departure time and travel duration."""
    name = r.choice(SA_NAMES)
    dep_h = r.randint(6, 14)
    dep_m = r.choice([10, 20, 30, 45])
    dur_h = r.randint(2, 5)
    dur_m = r.choice([15, 25, 35, 45])

    total_m = dep_m + dur_m
    arr_h = (dep_h + dur_h + (total_m // 60)) % 24
    arr_m = total_m % 60
    ans_str = f"{arr_h:02d}:{arr_m:02d}"

    prompt = (
        f"{name} boarded a regional shuttle bus departing at {dep_h:02d}:{dep_m:02d}. "
        f"The travel duration according to the driver is {dur_h} hours and {dur_m} minutes.\n"
        f"Determine the scheduled arrival time in 24-hour clock format."
    )
    explanation = (
        f"Step 1: Add the journey duration to departure time:\n"
        f"{dep_h:02d}:{dep_m:02d} + {dur_h}\\text{{ h }} {dur_m}\\text{{ min}}. [1 mark]\n"
        f"Step 2: Add minutes: {dep_m} + {dur_m} = {total_m}\\text{{ min}} "
        f"(= {total_m // 60}\\text{{ h }} {arr_m}\\text{{ min}}). [1 mark]\n"
        f"Step 3: Add hours: {dep_h} + {dur_h} + {total_m // 60} = {arr_h:02d}.\n"
        f"\\text{{Arrival time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{(arr_h + 1) % 24:02d}:{arr_m:02d}",
        f"{arr_h:02d}:{(arr_m + 15) % 60:02d}",
        f"{(arr_h - 1) % 24:02d}:{arr_m:02d}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_43",
        prompt,
        ans_str,
        options,
        explanation,
        "Add hours and minutes of duration to the departure time.",
        f"Add {dur_h} h {dur_m} min to {dep_h:02d}:{dep_m:02d}.",
        f"Arrival time = {ans_str}.",
        r,
    )


def generate_subskill_44(r: random.Random) -> Dict[str, Any]:
    """Determining departure time given required arrival time and duration."""
    name = r.choice(SA_NAMES)
    arr_h = r.randint(14, 21)
    arr_m = r.choice([0, 15, 30, 45])
    dur_h = r.randint(1, 4)
    dur_m = r.choice([15, 30, 45])

    # Convert both to total minutes from start of day
    arr_total_m = (arr_h * 60) + arr_m
    dur_total_m = (dur_h * 60) + dur_m
    dep_total_m = arr_total_m - dur_total_m

    dep_h = dep_total_m // 60
    dep_m = dep_total_m % 60
    ans_str = f"{dep_h:02d}:{dep_m:02d}"

    prompt = (
        f"{name} must arrive at OR Tambo International Airport by {arr_h:02d}:{arr_m:02d} for flight check-in. "
        f"The driving time from {name}'s home is estimated at {dur_h} hours and {dur_m} minutes.\n"
        f"What is the latest time {name} should leave home?"
    )
    explanation = (
        f"Step 1: Set up the subtraction (Required arrival time - Travel duration):\n"
        f"{arr_h:02d}:{arr_m:02d} - {dur_h}\\text{{ h }} {dur_m}\\text{{ min}}. [1 mark]\n"
        f"Step 2: Subtract minutes and borrow 60 minutes from hours if needed:\n"
        f"Total minutes from midnight: {arr_total_m} - {dur_total_m} = {dep_total_m}\\text{{ min}}. [1 mark]\n"
        f"Step 3: Convert back to hours and minutes:\n"
        f"{dep_total_m} \\div 60 = {dep_h:02d}:{dep_m:02d}.\n"
        f"\\text{{Departure time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{(dep_h + 1) % 24:02d}:{dep_m:02d}",
        f"{dep_h:02d}:{(dep_m + 15) % 60:02d}",
        f"{(dep_h - 1) % 24:02d}:{dep_m:02d}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_44",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract the travel duration from the required arrival time.",
        f"Calculate {arr_h:02d}:{arr_m:02d} - {dur_h} h {dur_m} min.",
        f"Latest departure = {ans_str}.",
        r,
    )
