"""Subskills 47 to 52: Tide tables, tidal ranges, coastal navigation, daylight duration, and international time zones."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
    _fmt_curr,
    _fmt_frac,
    _fmt_pct,
    _fmt_time,
)


def generate_47_reading_high_and_low_tide_times(r: random.Random) -> Dict[str, Any]:
    """Read morning and afternoon high and low tide times and water levels from a South African port tide table."""
    port = r.choice(["Durban Harbour", "Table Bay (Cape Town)", "Port Elizabeth (Gqeberha)", "Mossel Bay"])

    ht1_time, ht1_level = "04:18", 1.95
    lt1_time, lt1_level = "10:32", 0.38
    ht2_time, ht2_level = "16:45", 2.05
    lt2_time, lt2_level = "22:58", 0.42

    correct_ans = f"High Tides: {ht1_time} ({_fmt(ht1_level, 2)} m) & {ht2_time} ({_fmt(ht2_level, 2)} m); Low Tides: {lt1_time} ({_fmt(lt1_level, 2)} m) & {lt2_time} ({_fmt(lt2_level, 2)} m)"

    custom_options = [
        correct_ans,
        f"High Tides: {lt1_time} & {lt2_time}; Low Tides: {ht1_time} & {ht2_time}",
        f"High Tides: {ht1_time} ({_fmt(ht1_level, 2)} m); Low Tides: {ht2_time} ({_fmt(ht2_level, 2)} m)",
        f"High Tides: 06:00 (2,50 m); Low Tides: 12:00 (0,10 m)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"The following tide table extract shows predicted sea levels for {port} on a spring tide day:\n\n"
        f"| Event | Time | Predicted Water Level (m) |\n"
        f"| :--- | :--- | :--- |\n"
        f"| High Tide 1 | {ht1_time} | {_fmt(ht1_level, 2)} |\n"
        f"| Low Tide 1 | {lt1_time} | {_fmt(lt1_level, 2)} |\n"
        f"| High Tide 2 | {ht2_time} | {_fmt(ht2_level, 2)} |\n"
        f"| Low Tide 2 | {lt2_time} | {_fmt(lt2_level, 2)} |\n\n"
        f"Read the table and state all high tide and low tide times along with their predicted water levels."
    )
    explanation = (
        f"Step 1: Identify high tide entries: High Tide 1 occurs at {ht1_time} with level {_fmt(ht1_level, 2)} m; High Tide 2 occurs at {ht2_time} with level {_fmt(ht2_level, 2)} m [M].\n"
        f"Step 2: Identify low tide entries: Low Tide 1 occurs at {lt1_time} with level {_fmt(lt1_level, 2)} m; Low Tide 2 occurs at {lt2_time} with level {_fmt(lt2_level, 2)} m [M].\n"
        f"Step 3: State complete reading accurately [A]."
    )
    return _build_question_payload(
        subskill_id="47_reading_high_and_low_tide_times",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Read the times and water levels directly from the respective High and Low rows.",
        tier_2="High tides are at 04:18 (1,95 m) and 16:45 (2,05 m). Low tides are at 10:32 (0,38 m) and 22:58 (0,42 m).",
        tier_3="Correct times and levels identified.",
        r=r,
    )


def generate_48_calculating_tidal_range(r: random.Random) -> Dict[str, Any]:
    """Calculate the tidal range (difference between high tide and low tide water levels)."""
    ht_level = round(r.uniform(1.85, 2.15), 2)  # e.g. 2.05 m
    lt_level = round(r.uniform(0.30, 0.45), 2)  # e.g. 0.38 m
    tidal_range = round(ht_level - lt_level, 2)  # e.g. 1.67 m

    correct_ans = f"Tidal Range = {_fmt(ht_level, 2)} m - {_fmt(lt_level, 2)} m = {_fmt(tidal_range, 2)} m"

    custom_options = [
        correct_ans,
        f"Tidal Range = {_fmt(ht_level + lt_level, 2)} m",
        f"Tidal Range = {_fmt(ht_level / lt_level, 2)} m",
        f"Tidal Range = {_fmt(tidal_range * 10, 1)} m",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"At Durban Harbour, an afternoon High Tide measures {_fmt(ht_level, 2)} m, "
        f"followed by an evening Low Tide measuring {_fmt(lt_level, 2)} m.\n\n"
        f"Definition: Tidal Range = High Tide Level - Low Tide Level\n\n"
        f"Calculate the tidal range in metres (m)."
    )
    explanation = (
        f"Step 1: Identify high tide level ({_fmt(ht_level, 2)} m) and low tide level ({_fmt(lt_level, 2)} m) [M].\n"
        f"Step 2: Subtract: {_fmt(ht_level, 2)} - {_fmt(lt_level, 2)} [M].\n"
        f"Step 3: Tidal Range = {_fmt(tidal_range, 2)} m [A]."
    )
    return _build_question_payload(
        subskill_id="48_calculating_tidal_range",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Tidal range is the difference: subtract the low tide level from the high tide level.",
        tier_2=f"{_fmt(ht_level, 2)} - {_fmt(lt_level, 2)} = {_fmt(tidal_range, 2)} m.",
        tier_3=f"Tidal Range = {_fmt(tidal_range, 2)} m.",
        r=r,
    )


def generate_49_elapsed_time_between_tides(r: random.Random) -> Dict[str, Any]:
    """Calculate the exact time difference in hours and minutes between consecutive high and low tides."""
    ht_h, ht_m = 4, 18   # 04:18
    lt_h, lt_m = 10, 32  # 10:32

    ht_mins = ht_h * 60 + ht_m  # 258 mins
    lt_mins = lt_h * 60 + lt_m  # 632 mins
    diff_mins = lt_mins - ht_mins  # 374 mins = 6h 14m

    diff_h = diff_mins // 60
    diff_m = diff_mins % 60

    correct_ans = f"Elapsed time = {diff_h} hours {diff_m} minutes (10:32 - 04:18 = 374 minutes)"

    custom_options = [
        correct_ans,
        f"Elapsed time = 6 hours 00 minutes",
        f"Elapsed time = {diff_h + 1} hours {diff_m} minutes",
        f"Elapsed time = 5 hours {diff_m} minutes",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"According to a hydrographic chart for Table Bay:\n"
        f"• Morning High Tide occurs at 04:18\n"
        f"• The following Low Tide occurs at 10:32\n\n"
        f"Calculate the elapsed time duration between this high tide and low tide in **hours and minutes**."
    )
    explanation = (
        f"Step 1: Convert both times to total minutes since midnight:\n"
        f"04:18 = (4 × 60) + 18 = 258 min; 10:32 = (10 × 60) + 32 = 632 min [M].\n"
        f"Step 2: Difference = 632 - 258 = 374 minutes [M].\n"
        f"Step 3: Convert to hours and minutes: 374 ÷ 60 = {diff_h} hours and {diff_m} minutes [A]."
    )
    return _build_question_payload(
        subskill_id="49_elapsed_time_between_tides",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the high tide time from the low tide time: 10:32 - 04:18.",
        tier_2="Hours: 10 - 4 = 6. Minutes: 32 - 18 = 14. Total = 6 hours 14 minutes.",
        tier_3=f"Elapsed time = {diff_h} hours {diff_m} minutes.",
        r=r,
    )


def generate_50_safe_boating_water_depth_window(r: random.Random) -> Dict[str, Any]:
    """Evaluate whether sea water level meets minimum draft safety depth for launching a boat."""
    boat_draft_m = 1.20  # boat requires 1.2 m of water
    safety_margin_m = 0.50 # plus 0.5 m clearance = 1.70 m required depth
    required_depth = boat_draft_m + safety_margin_m  # 1.70 m

    # Given tide chart:
    # High Tide: 2.05 m
    # Low Tide: 0.38 m
    ht_level = 2.05
    lt_level = 0.38

    can_launch_ht = ht_level >= required_depth  # True: 2.05 >= 1.70
    can_launch_lt = lt_level >= required_depth  # False: 0.38 < 1.70

    correct_ans = f"Required depth = {_fmt(required_depth, 2)} m; Safe to launch at High Tide ({_fmt(ht_level, 2)} m); UNSAFE at Low Tide ({_fmt(lt_level, 2)} m)"

    custom_options = [
        correct_ans,
        f"Required depth = 1,20 m; Safe to launch at all tides",
        f"Required depth = 2,50 m; Unsafe at both High and Low Tide",
        f"Required depth = 0,50 m; Safe to launch only at Low Tide",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A commercial deep-sea fishing ski-boat requires a minimum water depth (draft) of {_fmt(boat_draft_m, 2)} m "
        f"plus a safety clearance margin of {_fmt(safety_margin_m, 2)} m above the harbor sandbank to launch safely.\n\n"
        f"The tide forecast shows:\n"
        f"• High Tide water level: {_fmt(ht_level, 2)} m\n"
        f"• Low Tide water level: {_fmt(lt_level, 2)} m\n\n"
        f"Calculate the total minimum water depth required, and determine whether the boat can be safely launched "
        f"at High Tide and at Low Tide."
    )
    explanation = (
        f"Step 1: Total required depth = {_fmt(boat_draft_m, 2)} m (draft) + {_fmt(safety_margin_m, 2)} m (clearance) = {_fmt(required_depth, 2)} m [M].\n"
        f"Step 2: At High Tide: {_fmt(ht_level, 2)} m ≥ {_fmt(required_depth, 2)} m, so launching is SAFE [M].\n"
        f"Step 3: At Low Tide: {_fmt(lt_level, 2)} m < {_fmt(required_depth, 2)} m, so launching is DANGEROUS/UNSAFE (risk of grounding) [A]."
    )
    return _build_question_payload(
        subskill_id="50_safe_boating_water_depth_window",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the boat's draft and the safety margin together, then compare with the high and low tide levels.",
        tier_2=f"Required depth = {boat_draft_m} + {safety_margin_m} = {_fmt(required_depth, 2)} m.",
        tier_3=f"Safe at High Tide; Unsafe at Low Tide.",
        r=r,
    )


def generate_51_sunrise_sunset_daylight_duration(r: random.Random) -> Dict[str, Any]:
    """Calculate total daylight duration from sunrise and sunset times."""
    # Summer vs Winter sunrise and sunset
    is_summer = r.choice([True, False])
    if is_summer:
        sr_h, sr_m = 5, 28
        ss_h, ss_m = 19, 5
        season = "mid-summer (December)"
    else:
        sr_h, sr_m = 6, 52
        ss_h, ss_m = 17, 34
        season = "mid-winter (June)"

    sr_mins = sr_h * 60 + sr_m
    ss_mins = ss_h * 60 + ss_m
    daylight_mins = ss_mins - sr_mins

    dl_h = daylight_mins // 60
    dl_m = daylight_mins % 60

    sr_str = f"{sr_h:02d}:{sr_m:02d}"
    ss_str = f"{ss_h:02d}:{ss_m:02d}"

    correct_ans = f"Daylight duration = {dl_h} hours {dl_m} minutes ({ss_str} - {sr_str})"

    custom_options = [
        correct_ans,
        f"Daylight duration = {dl_h + 1} hours {dl_m} minutes",
        f"Daylight duration = {dl_h} hours 0 minutes",
        f"Daylight duration = {dl_h - 1} hours {dl_m} minutes",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"In Cape Town during {season}, the astronomical almanac records:\n"
        f"• Sunrise: {sr_str}\n"
        f"• Sunset: {ss_str}\n\n"
        f"Calculate the total duration of daylight in **hours and minutes**."
    )
    explanation = (
        f"Step 1: Convert sunrise to minutes since midnight: ({sr_h} × 60) + {sr_m} = {sr_mins} min [M].\n"
        f"Step 2: Convert sunset to minutes since midnight: ({ss_h} × 60) + {ss_m} = {ss_mins} min [M].\n"
        f"Step 3: Daylight duration = {ss_mins} - {sr_mins} = {daylight_mins} minutes = {dl_h} hours {dl_m} minutes [A]."
    )
    return _build_question_payload(
        subskill_id="51_sunrise_sunset_daylight_duration",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the sunrise time from the sunset time.",
        tier_2=f"{ss_str} - {sr_str} = {dl_h} hours and {dl_m} minutes.",
        tier_3=f"Daylight = {dl_h} hours {dl_m} minutes.",
        r=r,
    )


def generate_52_international_time_zones_travel(r: random.Random) -> Dict[str, Any]:
    """Calculate the local destination arrival time for an international flight across time zones."""
    # Flying Johannesburg (SAST, UTC+2) to London (GMT/UTC+0 in winter)
    # Time difference: London is 2 hours behind Johannesburg (SAST - 2 hours)
    dep_h, dep_m = 19, 45  # departs JHB 19:45 SAST
    flight_duration_h = 11
    flight_duration_m = 30 # 11 hours 30 mins
    tz_diff_hours = -2 # London is 2 hours behind SAST

    # In SAST time, arrival would be: 19:45 + 11h 30m = 07:15 next day
    # In London local time: 07:15 - 2 hours = 05:15 next morning
    dep_mins = dep_h * 60 + dep_m
    flight_mins = flight_duration_h * 60 + flight_duration_m
    sast_arr_mins = dep_mins + flight_mins # 1185 + 690 = 1875 mins
    # London mins:
    london_arr_mins = sast_arr_mins + (tz_diff_hours * 60) # 1875 - 120 = 1755 mins

    # Next day calculation:
    next_day_mins = london_arr_mins - (24 * 60) # 1755 - 1440 = 315 mins = 05:15
    arr_h = next_day_mins // 60
    arr_m = next_day_mins % 60
    arr_str = f"{arr_h:02d}:{arr_m:02d}"

    correct_ans = f"Arrival = {arr_str} (local London time, next day); SAST arrival = 07:15"

    custom_options = [
        correct_ans,
        f"Arrival = 07:15 (local London time, next day)",
        f"Arrival = 09:15 (local London time, next day)",
        f"Arrival = 03:15 (local London time, next day)",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A direct flight departs from OR Tambo International Airport (Johannesburg) at 19:45 (SAST).\n"
        f"• The scheduled flight duration to London Heathrow is 11 hours and 30 minutes\n"
        f"• South African Standard Time (SAST) is UTC+2\n"
        f"• London is in the Greenwich Mean Time zone (UTC+0), which is 2 hours behind South Africa\n\n"
        f"Calculate:\n"
        f"1. The arrival time in South African time (SAST)\n"
        f"2. The scheduled local arrival time in London"
    )
    explanation = (
        f"Step 1: Calculate SAST arrival time: 19:45 + 11 hours 30 minutes = 07:15 the next morning (SAST) [M].\n"
        f"Step 2: Adjust for time zone (London is 2 hours behind SAST): 07:15 - 2 hours [M].\n"
        f"Step 3: Local London arrival time = {arr_str} the following morning [A]."
    )
    return _build_question_payload(
        subskill_id="52_international_time_zones_travel",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the flight duration to the departure time, then subtract 2 hours for London's time zone.",
        tier_2="19:45 + 11 h 30 min = 07:15 SAST. Subtract 2 hours = 05:15 London time.",
        tier_3=f"Local London arrival = {arr_str} (next day).",
        r=r,
    )
