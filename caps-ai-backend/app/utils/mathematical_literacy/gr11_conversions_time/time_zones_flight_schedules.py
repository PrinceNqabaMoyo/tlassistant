"""Time zones, flight schedules, and timetable analysis (Subskills 45-52) for Grade 11 Mathematical Literacy."""
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


def generate_subskill_45(r: random.Random) -> Dict[str, Any]:
    """SAST (UTC+2) to London (GMT / UTC+0, 2 hours behind)."""
    name = r.choice(SA_NAMES)
    sast_h = r.randint(8, 22)
    sast_m = r.choice([0, 15, 30, 45])
    london_h = (sast_h - 2) % 24
    ans_str = f"{london_h:02d}:{sast_m:02d}"

    prompt = (
        f"{name} in Johannesburg needs to arrange a teleconference with a business colleague in London.\n"
        f"If the meeting is scheduled for {sast_h:02d}:{sast_m:02d} South African Standard Time (SAST, UTC+2),\n"
        f"what time will it be in London (GMT, UTC+0)?\n"
        f"*(Note: London is 2 hours behind South African Standard Time.)*"
    )
    explanation = (
        f"Step 1: Identify the time difference between SAST and London:\n"
        f"London is 2 hours behind SAST (subtract 2 hours). [1 mark]\n"
        f"Step 2: Subtract 2 hours from the South African time:\n"
        f"{sast_h:02d}:{sast_m:02d} - 2\\text{{ hours}} = {london_h:02d}:{sast_m:02d}. [1 mark]\n"
        f"Step 3: State the local London time:\n"
        f"\\text{{London time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{(sast_h + 2) % 24:02d}:{sast_m:02d}",
        f"{(london_h - 1) % 24:02d}:{sast_m:02d}",
        f"{sast_h:02d}:{sast_m:02d}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_45",
        prompt,
        ans_str,
        options,
        explanation,
        "London is 2 hours behind South Africa, so subtract 2 hours from SAST.",
        f"Calculate {sast_h:02d}:{sast_m:02d} - 2 hours.",
        f"Time in London = {ans_str}.",
        r,
    )


def generate_subskill_46(r: random.Random) -> Dict[str, Any]:
    """SAST (UTC+2) to New York (UTC-5, 7 hours behind)."""
    name = r.choice(SA_NAMES)
    sast_h = r.randint(14, 23)
    sast_m = r.choice([0, 15, 30, 45])
    ny_h = (sast_h - 7) % 24
    ans_str = f"{ny_h:02d}:{sast_m:02d}"

    prompt = (
        f"A live sports broadcast starts in South Africa at {sast_h:02d}:{sast_m:02d} SAST.\n"
        f"{name}'s cousin living in New York (Eastern Standard Time, UTC-5) wants to watch the broadcast.\n"
        f"What local time in New York should the cousin tune in?\n"
        f"*(Note: New York is 7 hours behind South Africa.)*"
    )
    explanation = (
        f"Step 1: Identify the time offset between South Africa and New York:\n"
        f"New York is 7 hours behind SAST (UTC-5 vs UTC+2). [1 mark]\n"
        f"Step 2: Subtract 7 hours from {sast_h:02d}:{sast_m:02d}:\n"
        f"{sast_h:02d}:{sast_m:02d} - 7\\text{{ hours}} = {ny_h:02d}:{sast_m:02d}. [1 mark]\n"
        f"Step 3: State the New York local time:\n"
        f"\\text{{New York time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{(sast_h + 7) % 24:02d}:{sast_m:02d}",
        f"{(ny_h + 1) % 24:02d}:{sast_m:02d}",
        f"{(ny_h - 2) % 24:02d}:{sast_m:02d}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_46",
        prompt,
        ans_str,
        options,
        explanation,
        "Subtract 7 hours from the South African time.",
        f"Calculate {sast_h:02d}:{sast_m:02d} - 7 hours.",
        f"New York time = {ans_str}.",
        r,
    )


def generate_subskill_47(r: random.Random) -> Dict[str, Any]:
    """SAST (UTC+2) to Sydney (UTC+10, 8 hours ahead)."""
    name = r.choice(SA_NAMES)
    sast_h = r.randint(6, 14)
    sast_m = r.choice([0, 15, 30, 45])
    syd_h = (sast_h + 8) % 24
    ans_str = f"{syd_h:02d}:{sast_m:02d}"

    prompt = (
        f"{name} wants to phone family in Sydney, Australia. If {name} places the call at "
        f"{sast_h:02d}:{sast_m:02d} South African Standard Time,\n"
        f"what local time will it be in Sydney?\n"
        f"*(Note: Sydney (UTC+10) is 8 hours ahead of South African Standard Time (UTC+2).)*"
    )
    explanation = (
        f"Step 1: Identify the time offset:\n"
        f"Sydney is 8 hours ahead of SAST. [1 mark]\n"
        f"Step 2: Add 8 hours to the South African time:\n"
        f"{sast_h:02d}:{sast_m:02d} + 8\\text{{ hours}} = {syd_h:02d}:{sast_m:02d}. [1 mark]\n"
        f"Step 3: State the local Sydney time:\n"
        f"\\text{{Sydney time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{(sast_h - 8) % 24:02d}:{sast_m:02d}",
        f"{(syd_h + 1) % 24:02d}:{sast_m:02d}",
        f"{(syd_h - 2) % 24:02d}:{sast_m:02d}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_47",
        prompt,
        ans_str,
        options,
        explanation,
        "Sydney is 8 hours ahead of South Africa, so add 8 hours to SAST.",
        f"Calculate {sast_h:02d}:{sast_m:02d} + 8 hours.",
        f"Sydney time = {ans_str}.",
        r,
    )


def generate_subskill_48(r: random.Random) -> Dict[str, Any]:
    """International flight arrival time accounting for duration and time zone difference."""
    name = r.choice(SA_NAMES)
    dep_h = r.randint(18, 21)
    dep_m = r.choice([15, 30, 45])
    dur_h = 11
    dur_m = 30
    tz_diff = -2  # London is 2 hours behind SAST

    # Step: departure in SAST + duration = arrival in SAST
    total_mins = (dep_h * 60) + dep_m + (dur_h * 60) + dur_m
    sast_arr_h = (total_mins // 60) % 24
    sast_arr_m = total_mins % 60
    # Step: convert arrival SAST to London time (subtract 2 hours)
    london_arr_h = (sast_arr_h + tz_diff) % 24
    london_arr_m = sast_arr_m
    ans_str = f"{london_arr_h:02d}:{london_arr_m:02d}"

    prompt = (
        f"A direct flight from Johannesburg to London Heathrow departs at {dep_h:02d}:{dep_m:02d} SAST. "
        f"The flight duration is {dur_h} hours and {dur_m} minutes.\n"
        f"At what local time in London will {name}'s flight land on the following day?\n"
        f"*(Given: London is 2 hours behind South Africa.)*"
    )
    explanation = (
        f"Step 1: Calculate arrival time in South African time (SAST):\n"
        f"{dep_h:02d}:{dep_m:02d} + {dur_h}\\text{{ h }} {dur_m}\\text{{ min}} = {sast_arr_h:02d}:{sast_arr_m:02d}\\text{{ SAST (next day)}}. [1 mark]\n"
        f"Step 2: Adjust for London's time zone by subtracting 2 hours:\n"
        f"{sast_arr_h:02d}:{sast_arr_m:02d} - 2\\text{{ hours}} = {london_arr_h:02d}:{london_arr_m:02d}. [1 mark]\n"
        f"Step 3: State the local London arrival time:\n"
        f"\\text{{Local arrival time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{sast_arr_h:02d}:{sast_arr_m:02d}",
        f"{(london_arr_h + 2) % 24:02d}:{london_arr_m:02d}",
        f"{(london_arr_h - 1) % 24:02d}:{london_arr_m:02d}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_48",
        prompt,
        ans_str,
        options,
        explanation,
        "Add the flight duration to the departure time, then subtract 2 hours for London time.",
        f"Arrival SAST = {sast_arr_h:02d}:{sast_arr_m:02d}. London time = {sast_arr_h:02d}:{sast_arr_m:02d} - 2 hours.",
        f"Arrival time = {ans_str}.",
        r,
    )


def generate_subskill_49(r: random.Random) -> Dict[str, Any]:
    """International flight departure time calculation from arrival time, flight duration, and time zone."""
    name = r.choice(SA_NAMES)
    arr_h = r.randint(6, 11)
    arr_m = r.choice([0, 15, 30, 45])
    dur_h = 8
    dur_m = 30
    tz_diff = 2  # Dubai is 2 hours ahead of SAST

    # Arrival in Dubai time -> Convert to SAST (Dubai - 2 hours)
    arr_sast_h = (arr_h - tz_diff) % 24
    # Subtract duration from arrival SAST
    total_arr_mins = (arr_sast_h * 60) + arr_m
    dep_sast_mins = total_arr_mins - ((dur_h * 60) + dur_m)
    if dep_sast_mins < 0:
        dep_sast_mins += 24 * 60
    dep_h = dep_sast_mins // 60
    dep_m = dep_sast_mins % 60
    ans_str = f"{dep_h:02d}:{dep_m:02d}"

    prompt = (
        f"{name} landed in Dubai at {arr_h:02d}:{arr_m:02d} local time after a flight from Johannesburg. "
        f"The flying time was {dur_h} hours and {dur_m} minutes.\n"
        f"Determine the departure time from Johannesburg in South African Standard Time (SAST).\n"
        f"*(Given: Dubai is 2 hours ahead of South African Standard Time.)*"
    )
    explanation = (
        f"Step 1: Convert the Dubai arrival time to South African time:\n"
        f"{arr_h:02d}:{arr_m:02d} - 2\\text{{ hours}} = {arr_sast_h:02d}:{arr_m:02d}\\text{{ SAST}}. [1 mark]\n"
        f"Step 2: Subtract the flight duration ({dur_h} h {dur_m} min) from the SAST arrival time:\n"
        f"{arr_sast_h:02d}:{arr_m:02d} - {dur_h}\\text{{ h }} {dur_m}\\text{{ min}} = {ans_str}\\text{{ SAST (previous day)}}. [1 mark]\n"
        f"Step 3: State the departure time:\n"
        f"\\text{{Departure time}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{(dep_h + 2) % 24:02d}:{dep_m:02d}",
        f"{(dep_h - 2) % 24:02d}:{dep_m:02d}",
        f"{dep_h:02d}:{(dep_m + 30) % 60:02d}",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_49",
        prompt,
        ans_str,
        options,
        explanation,
        "First convert Dubai arrival time to SAST (subtract 2 hours), then subtract the flight duration.",
        f"Dubai arrival in SAST = {arr_sast_h:02d}:{arr_m:02d}. Subtract {dur_h} h {dur_m} min.",
        f"Departure time = {ans_str}.",
        r,
    )


def generate_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Multi-leg flight itinerary with layovers and total journey duration."""
    name = r.choice(SA_NAMES)
    leg1_h = r.randint(7, 9)
    leg1_m = r.choice([15, 30, 45])
    layover_h = r.randint(2, 4)
    layover_m = r.choice([15, 30, 45])
    leg2_h = r.randint(6, 8)
    leg2_m = r.choice([0, 15, 30])

    total_mins = (leg1_h * 60 + leg1_m) + (layover_h * 60 + layover_m) + (leg2_h * 60 + leg2_m)
    tot_h = total_mins // 60
    tot_m = total_mins % 60
    ans_str = f"{tot_h} h {tot_m} min"

    prompt = (
        f"{name}'s flight itinerary from Cape Town to New York consists of two flights and a layover:\n"
        f"• Flight Leg 1 (Cape Town to Amsterdam): {leg1_h} hours and {leg1_m} minutes\n"
        f"• Airport layover in Amsterdam: {layover_h} hours and {layover_m} minutes\n"
        f"• Flight Leg 2 (Amsterdam to New York): {leg2_h} hours and {leg2_m} minutes\n\n"
        f"Calculate the total journey time from departure in Cape Town to arrival in New York."
    )
    explanation = (
        f"Step 1: Set up the sum of all itinerary components:\n"
        f"\\text{{Total}} = \\text{{Leg 1}} + \\text{{Layover}} + \\text{{Leg 2}}. [1 mark]\n"
        f"Step 2: Add hours and minutes:\n"
        f"\\text{{Hours}} = {leg1_h} + {layover_h} + {leg2_h} = {leg1_h + layover_h + leg2_h}\\text{{ h}}\n"
        f"\\text{{Minutes}} = {leg1_m} + {layover_m} + {leg2_m} = {leg1_m + layover_m + leg2_m}\\text{{ min}} [1 mark]\n"
        f"Step 3: Convert excess minutes to hours:\n"
        f"\\text{{Total journey duration}} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{tot_h + 1} h {tot_m} min",
        f"{tot_h - 1} h {tot_m} min",
        f"{tot_h} h {(tot_m + 30) % 60} min",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_50",
        prompt,
        ans_str,
        options,
        explanation,
        "Add Leg 1 duration + layover duration + Leg 2 duration.",
        f"Sum: ({leg1_h} h {leg1_m} min) + ({layover_h} h {layover_m} min) + ({leg2_h} h {leg2_m} min).",
        f"Total duration = {ans_str}.",
        r,
    )


def generate_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Long-distance bus timetable interpretation and layover analysis."""
    name = r.choice(SA_NAMES)
    timetable = [
        ("Johannesburg (Park Station)", "08:00", "08:30"),
        ("Kroonstad", "10:45", "11:00"),
        ("Bloemfontein", "13:15", "14:00"),
        ("Colesberg", "16:45", "17:00"),
        ("Beaufort West", "20:30", "21:00"),
        ("Cape Town", "04:30", "Terminus"),
    ]
    # Pick Bloemfontein stop layover: arrival 13:15, departure 14:00 -> 45 minutes
    stop_name = "Bloemfontein"
    arr = "13:15"
    dep = "14:00"
    ans_str = "45 minutes"

    table_text = (
        "| Station | Scheduled Arrival | Scheduled Departure |\n"
        "| :--- | :--- | :--- |\n"
        "| Johannesburg (Park Station) | --- | 08:30 |\n"
        "| Kroonstad | 10:45 | 11:00 |\n"
        "| Bloemfontein | 13:15 | 14:00 |\n"
        "| Colesberg | 16:45 | 17:00 |\n"
        "| Beaufort West | 20:30 | 21:00 |\n"
        "| Cape Town | 04:30 (next day) | Terminus |\n"
    )

    prompt = (
        f"{name} is travelling on a long-distance intercity bus from Johannesburg to Cape Town.\n"
        f"Refer to the timetable below:\n\n"
        f"{table_text}\n"
        f"Calculate the scheduled rest/layover duration at {stop_name} station."
    )
    explanation = (
        f"Step 1: Locate {stop_name} on the timetable:\n"
        f"Arrival time = {arr}; Departure time = {dep}. [1 mark]\n"
        f"Step 2: Subtract arrival time from departure time:\n"
        f"14:00 - 13:15 = 45\\text{{ minutes}}. [1 mark]\n"
        f"Step 3: State the layover duration:\n"
        f"\\text{{Duration}} = {ans_str}. [1 mark]"
    )
    distractors = [
        "30 minutes",
        "1 hour",
        "15 minutes",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_51",
        prompt,
        ans_str,
        options,
        explanation,
        f"Subtract the arrival time ({arr}) from the departure time ({dep}) at {stop_name}.",
        f"14:00 - 13:15 = 45 minutes.",
        f"Layover = {ans_str}.",
        r,
    )


def generate_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Industrial shift schedule, factory production cycle, and cumulative working hours."""
    name = r.choice(SA_NAMES)
    shifts_per_week = 5
    shift_start_h = 7
    shift_start_m = 30
    shift_end_h = 16
    shift_end_m = 30
    # Total span = 9 hours
    lunch_break_m = 60
    daily_work_h = (shift_end_h - shift_start_h) - (lunch_break_m / 60.0)
    weekly_hours = round(daily_work_h * shifts_per_week, 1)
    ans_str = f"{_fmt(weekly_hours)} hours"

    prompt = (
        f"{name} works at an automotive manufacturing assembly plant in Rosslyn, Pretoria.\n"
        f"The regular daily shift runs from {shift_start_h:02d}:{shift_start_m:02d} to {shift_end_h:02d}:{shift_end_m:02d}, "
        f"with an unpaid 60-minute lunch break.\n"
        f"If {name} works {shifts_per_week} days a week, calculate the total productive working hours per week."
    )
    explanation = (
        f"Step 1: Calculate the total shift duration per day:\n"
        f"{shift_end_h:02d}:{shift_end_m:02d} - {shift_start_h:02d}:{shift_start_m:02d} = 9\\text{{ hours}}. [1 mark]\n"
        f"Step 2: Subtract the unpaid lunch break to find daily working hours:\n"
        f"9\\text{{ hours}} - 1\\text{{ hour break}} = {daily_work_h:.0f}\\text{{ working hours/day}}. [1 mark]\n"
        f"Step 3: Multiply daily hours by {shifts_per_week} shifts:\n"
        f"\\text{{Weekly hours}} = {daily_work_h:.0f} \\times {shifts_per_week} = {ans_str}. [1 mark]"
    )
    distractors = [
        f"{_fmt(9 * shifts_per_week)} hours",
        f"{_fmt(weekly_hours - 5)} hours",
        f"{_fmt(weekly_hours + 4)} hours",
    ]
    options, _ = _build_options(ans_str, r, [ans_str] + distractors)
    return _build_question_payload(
        "subskill_52",
        prompt,
        ans_str,
        options,
        explanation,
        "Find the daily hours excluding lunch, then multiply by 5 days.",
        f"Daily hours = 9 h - 1 h = 8 h. Weekly hours = 8 h × 5 = {ans_str}.",
        f"Total hours = {ans_str}.",
        r,
    )
