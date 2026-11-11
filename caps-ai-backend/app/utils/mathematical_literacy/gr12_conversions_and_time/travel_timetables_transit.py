"""Subskills 33 to 40: Travel timetables, transit scheduling, arrival times, excursion feasibility, and layovers."""
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


def generate_33_reading_transit_timetable_departures(r: random.Random) -> Dict[str, Any]:
    """Read specific departure and arrival times from a passenger ferry/bus timetable."""
    dep_options = ["08:20", "14:45", "18:00"]
    ret_options = ["07:00", "09:45", "16:15", "19:15"]

    correct_ans = f"Monday departures from Kerkira (Corfu): 08:20, 14:45, 18:00; Monday departures from Paxoi: 07:00, 09:45, 16:15, 19:15"

    custom_options = [
        correct_ans,
        f"Monday departures from Kerkira: 06:45, 14:30; Monday departures from Paxoi: 08:00",
        f"Monday departures from Kerkira: 09:30; Monday departures from Paxoi: 17:30",
        f"Monday departures from Kerkira: 07:00, 09:45; Monday departures from Paxoi: 08:20, 14:45",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"The following is an excerpt from a passenger hydrofoil ferry timetable between Corfu and the island of Paxoi:\n\n"
        f"| Day | Kerkira (Corfu) → Paxoi | Paxoi → Kerkira (Corfu) |\n"
        f"| :--- | :--- | :--- |\n"
        f"| **Monday** | 08:20 - 14:45 - 18:00 | 07:00 - 09:45 - 16:15 - 19:15 |\n"
        f"| **Tuesday** | 06:45 - 14:30 | 08:00 |\n"
        f"| **Wednesday** | 09:30 | 08:00 - 17:30 |\n"
        f"| **Duration** | **55 minutes** | **55 minutes** |\n\n"
        f"Read the timetable and list all scheduled departure times from Kerkira (Corfu) and from Paxoi on a **Monday**."
    )
    explanation = (
        f"Step 1: Locate the Monday row on the timetable [M].\n"
        f"Step 2: Read Corfu departures: 08:20, 14:45, and 18:00 (3 scheduled trips) [M].\n"
        f"Step 3: Read Paxoi departures: 07:00, 09:45, 16:15, and 19:15 (4 scheduled trips) [A]."
    )
    return _build_question_payload(
        subskill_id="33_reading_transit_timetable_departures",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Read the times listed in the Monday row under both directions.",
        tier_2="Corfu departures: 08:20, 14:45, 18:00. Paxoi departures: 07:00, 09:45, 16:15, 19:15.",
        tier_3="Correct times identified for both directions.",
        r=r,
    )


def generate_34_calculating_arrival_time_given_duration(r: random.Random) -> Dict[str, Any]:
    """Calculate arrival time by adding travel duration to departure time."""
    dep_h = r.choice([8, 14, 18])
    dep_m = r.choice([20, 45])
    duration_mins = 55

    total_m = dep_m + duration_mins
    arr_h = dep_h + (total_m // 60)
    arr_m = total_m % 60

    dep_str = f"{dep_h:02d}:{dep_m:02d}"
    arr_str = f"{arr_h:02d}:{arr_m:02d}"

    correct_ans = f"Arrival Time = {arr_str} ({dep_str} + 55 min)"

    custom_options = [
        correct_ans,
        f"Arrival Time = {arr_h + 1:02d}:{arr_m:02d}",
        f"Arrival Time = {dep_h:02d}:{dep_m + 55:02d}" if (dep_m + 55) < 60 else f"Arrival Time = {dep_h:02d}:15",
        f"Arrival Time = {arr_h:02d}:{abs(arr_m - 15):02d}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A hydrofoil ferry departs from the port of Kerkira at {dep_str}.\n"
        f"The crossing to Paxoi has a scheduled duration of {duration_mins} minutes.\n\n"
        f"Calculate the scheduled arrival time of the ferry in Paxoi."
    )
    explanation = (
        f"Step 1: Add duration to departure minutes: {dep_m} min + {duration_mins} min = {total_m} minutes [M].\n"
        f"Step 2: Convert minutes: {total_m} minutes = {total_m // 60} hour and {arr_m} minutes [M].\n"
        f"Step 3: Add to departure hour: {dep_h} + {total_m // 60} = {arr_h:02d}:{arr_m:02d} [A]."
    )
    return _build_question_payload(
        subskill_id="34_calculating_arrival_time_given_duration",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add 55 minutes to the departure time. Remember that 60 minutes equals 1 hour.",
        tier_2=f"{dep_str} + 55 min = {arr_str}.",
        tier_3=f"Arrival Time = {arr_str}.",
        r=r,
    )


def generate_35_total_travel_fare_family_group(r: random.Random) -> Dict[str, Any]:
    """Calculate total one-way or return passenger fares for a family group."""
    adults = 2
    children = r.choice([2, 3, 4])
    fare_adult = 17.0  # € 17.00
    fare_child = 10.0  # € 10.00
    is_return = r.choice([False, True])

    mult = 2 if is_return else 1
    total_cost = ((adults * fare_adult) + (children * fare_child)) * mult
    trip_type = "return" if is_return else "one-way"

    correct_ans = f"Total {trip_type} cost = € {_fmt(total_cost, 2)} ({adults} adults @ € {_fmt(fare_adult * mult, 2)}, {children} children @ € {_fmt(fare_child * mult, 2)})"

    custom_options = [
        correct_ans,
        f"Total {trip_type} cost = € {_fmt(total_cost * 1.5, 2)}",
        f"Total {trip_type} cost = € {_fmt((adults + children) * fare_adult, 2)}",
        f"Total {trip_type} cost = € {_fmt(total_cost / 2, 2)}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A family of {adults + children} (2 adults and {children} children) books a {trip_type} hydrofoil trip to Paxoi.\n"
        f"• Adult single fare: € {_fmt(fare_adult, 2)}\n"
        f"• Child single fare (under 12): € {_fmt(fare_child, 2)}\n\n"
        f"Calculate the total {trip_type} ticket fare for the entire family."
    )
    explanation = (
        f"Step 1: Calculate adult fares: {adults} × € {_fmt(fare_adult * mult, 2)} = € {_fmt(adults * fare_adult * mult, 2)} [M].\n"
        f"Step 2: Calculate child fares: {children} × € {_fmt(fare_child * mult, 2)} = € {_fmt(children * fare_child * mult, 2)} [M].\n"
        f"Step 3: Total = € {_fmt(total_cost, 2)} [A]."
    )
    return _build_question_payload(
        subskill_id="35_total_travel_fare_family_group",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Multiply adults by adult fare and children by child fare, doubling if it is a return trip.",
        tier_2=f"Adults: 2 × {fare_adult * mult} = {2 * fare_adult * mult}. Children: {children} × {fare_child * mult} = {children * fare_child * mult}.",
        tier_3=f"Total cost = € {_fmt(total_cost, 2)}.",
        r=r,
    )


def generate_36_feasibility_of_day_trip_excursion(r: random.Random) -> Dict[str, Any]:
    """Assess whether a day trip excursion allows the minimum required leisure time before the return departure."""
    dep_time = "14:45"
    duration_mins = r.choice([45, 50, 55, 60])
    arr_h = 14 + (45 + duration_mins) // 60
    arr_m = (45 + duration_mins) % 60
    arr_time = f"{arr_h:02d}:{arr_m:02d}"
    latest_return = "19:15"
    required_hours = 4

    d_spec_36 = {
        "diagram_role": "context",
        "kind": "strip_map",
        "title": f"Day Trip Transit Timetable (Departure: {dep_time})",
        "stops": [
            {"name": f"Departure ({dep_time})", "km": 0},
            {"name": f"Arrival ({arr_time})", "km": 40},
            {"name": f"Return ({latest_return})", "km": 80},
        ],
    }

    mins_available = (19 * 60 + 15) - (arr_h * 60 + arr_m)
    avail_h = mins_available // 60
    avail_m = mins_available % 60

    is_feasible = mins_available >= (required_hours * 60)  # False: 3h 35m < 4h 00m

    correct_ans = f"Arrival = {arr_time}; Available time = {avail_h} hours {avail_m} minutes; NOT feasible (less than {required_hours} hours)"

    custom_options = [
        correct_ans,
        f"Arrival = {arr_time}; Available time = 4 hours 30 minutes; Feasible",
        f"Arrival = 15:00; Available time = {avail_h + 1} hours {avail_m} minutes; Feasible",
        f"Arrival = {arr_time}; Available time = 2 hours 15 minutes; NOT feasible",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A family wants to spend at least {required_hours} hours on the island of Paxoi before returning on the same day.\n"
        f"• They plan to catch the {dep_time} Monday ferry from Corfu (journey duration: {duration_mins} minutes)\n"
        f"• The last scheduled return ferry from Paxoi on Monday departs at {latest_return}\n\n"
        f"Calculate the arrival time in Paxoi, the total leisure time available on the island, "
        f"and state whether this excursion plan is feasible."
    )
    explanation = (
        f"Step 1: Arrival time = {dep_time} + {duration_mins} min = {arr_time} [M].\n"
        f"Step 2: Calculate time available between arrival ({arr_time}) and departure ({latest_return}):\n"
        f"19:15 - 15:40 = 3 hours 35 minutes [M].\n"
        f"Step 3: Since 3 h 35 min is less than the required {required_hours} hours, the excursion is NOT feasible on this departure [A]."
    )
    return _build_question_payload(
        subskill_id="36_feasibility_of_day_trip_excursion",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate arrival time in Paxoi, then subtract arrival time from 19:15 to find available hours.",
        tier_2=f"Arrival = 14:45 + 55 min = 15:40. Available = 19:15 - 15:40 = 3 hours 35 minutes.",
        tier_3=f"NOT feasible (only {avail_h} hours {avail_m} minutes available).",
        r=r,
        diagram_spec=d_spec_36,
    )


def generate_37_latest_departure_time_with_buffer(r: random.Random) -> Dict[str, Any]:
    """Calculate the latest departure time from hotel given travel time, speed, and airport/ferry check-in buffer."""
    distance_km = 48
    avg_speed_kmh = 40
    # Travel time = 48 / 40 = 1.2 hours = 1 hour 12 minutes
    travel_mins = int((distance_km / avg_speed_kmh) * 60)  # 72 mins
    buffer_mins = 30  # 30 min buffer before departure
    ferry_dep_h = 8
    ferry_dep_m = 20  # 08:20

    total_backtrack_mins = travel_mins + buffer_mins  # 72 + 30 = 102 mins (1h 42m)
    dep_total_mins = (ferry_dep_h * 60) + ferry_dep_m  # 500 mins
    latest_leave_mins = dep_total_mins - total_backtrack_mins  # 398 mins = 06:38
    leave_h = latest_leave_mins // 60
    leave_m = latest_leave_mins % 60

    leave_str = f"{leave_h:02d}:{leave_m:02d}"

    correct_ans = f"Travel time = 1 h 12 min; Buffer = 30 min; Latest hotel departure = {leave_str}"

    custom_options = [
        correct_ans,
        f"Travel time = 1 h 20 min; Buffer = 30 min; Latest hotel departure = 06:30",
        f"Travel time = 1 h 12 min; Buffer = 0 min; Latest hotel departure = 07:08",
        f"Travel time = 2 h 00 min; Buffer = 30 min; Latest hotel departure = 05:50",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A family staying at a resort in Kavos intends to catch the 08:20 morning ferry from the terminal in Kerkira.\n"
        f"• The road distance from their resort to the ferry terminal is {distance_km} km\n"
        f"• Expected average driving speed: {avg_speed_kmh} km/h\n"
        f"• They must arrive at least {buffer_mins} minutes before ferry departure to buy tickets and board\n\n"
        f"1. Calculate the driving time in hours and minutes.\n"
        f"2. Calculate the latest time the family must depart from their hotel to catch the ferry."
    )
    explanation = (
        f"Step 1: Driving time = {distance_km} km ÷ {avg_speed_kmh} km/h = 1,2 hours = 1 hour 12 minutes (72 min) [M].\n"
        f"Step 2: Total required time before departure = 72 min driving + {buffer_mins} min buffer = {total_backtrack_mins} minutes (1 hour 42 minutes) [M].\n"
        f"Step 3: Subtract from 08:20: 08:20 - 1 hour 42 minutes = {leave_str} [A]."
    )
    return _build_question_payload(
        subskill_id="37_latest_departure_time_with_buffer",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Time = Distance ÷ Speed. Convert decimal hours to minutes, add buffer time, then subtract from 08:20.",
        tier_2=f"48 ÷ 40 = 1,2 h = 1 h 12 min. 1 h 12 min + 30 min = 1 h 42 min. 08:20 - 1 h 42 min = {leave_str}.",
        tier_3=f"Latest hotel departure = {leave_str}.",
        r=r,
    )


def generate_38_elapsed_time_crossing_midnight(r: random.Random) -> Dict[str, Any]:
    """Calculate total elapsed journey time for an overnight long-distance trip crossing midnight."""
    dep_h = r.choice([20, 21, 22])
    dep_m = r.choice([15, 30, 45])
    arr_h = r.choice([5, 6, 7])
    arr_m = r.choice([15, 30, 45])

    # Minutes to midnight: (24 * 60) - (dep_h * 60 + dep_m)
    mins_to_midnight = (24 * 60) - (dep_h * 60 + dep_m)
    mins_from_midnight = (arr_h * 60) + arr_m
    total_journey_mins = mins_to_midnight + mins_from_midnight

    dur_h = total_journey_mins // 60
    dur_m = total_journey_mins % 60

    dep_str = f"{dep_h:02d}:{dep_m:02d}"
    arr_str = f"{arr_h:02d}:{arr_m:02d}"

    correct_ans = f"Duration = {dur_h} hours {dur_m} minutes ({mins_to_midnight // 60} h {mins_to_midnight % 60} min before midnight + {arr_h} h {arr_m} min after)"

    custom_options = [
        correct_ans,
        f"Duration = {dur_h + 1} hours {dur_m} minutes",
        f"Duration = {abs(arr_h - dep_h)} hours {abs(arr_m - dep_m)} minutes",
        f"Duration = {dur_h} hours 0 minutes",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"An Intercape long-distance coach departs from Park Station in Johannesburg at {dep_str} "
        f"and arrives at the Durban station the following morning at {arr_str}.\n\n"
        f"Calculate the total elapsed travel duration of the coach journey in **hours and minutes**."
    )
    explanation = (
        f"Step 1: Calculate time from departure to midnight (24:00): 24:00 - {dep_str} = {mins_to_midnight // 60} hours {mins_to_midnight % 60} minutes [M].\n"
        f"Step 2: Add time from midnight to morning arrival: {arr_h} hours {arr_m} minutes [M].\n"
        f"Step 3: Total duration = {mins_to_midnight} min + {mins_from_midnight} min = {dur_h} hours {dur_m} minutes [A]."
    )
    return _build_question_payload(
        subskill_id="38_elapsed_time_crossing_midnight",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Split calculation at midnight: calculate time until 24:00, then add morning arrival time.",
        tier_2=f"Until midnight: 24:00 - {dep_str} = {mins_to_midnight // 60} h {mins_to_midnight % 60} min. Add {arr_h} h {arr_m} min.",
        tier_3=f"Duration = {dur_h} hours {dur_m} minutes.",
        r=r,
    )


def generate_39_multi_leg_journey_layover_scheduling(r: random.Random) -> Dict[str, Any]:
    """Calculate layover waiting time between two legs of a journey and total transit duration."""
    leg1_arr = "11:25"
    leg2_dep = "13:10"
    leg1_arr_mins = 11 * 60 + 25
    leg2_dep_mins = 13 * 60 + 10
    layover_mins = leg2_dep_mins - leg1_arr_mins  # 105 mins = 1h 45m

    start_time = "08:15"
    final_arr = "16:45"
    total_transit_mins = (16 * 60 + 45) - (8 * 60 + 15)  # 510 mins = 8h 30m

    correct_ans = f"Layover time = 1 hour 45 minutes; Total transit duration = 8 hours 30 minutes"

    custom_options = [
        correct_ans,
        f"Layover time = 2 hours 15 minutes; Total transit duration = 8 hours 30 minutes",
        f"Layover time = 1 hour 45 minutes; Total transit duration = 6 hours 45 minutes",
        f"Layover time = 45 minutes; Total transit duration = 9 hours 00 minutes",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    prompt = (
        f"A traveler flies from Cape Town to Polokwane with a connecting flight in Johannesburg:\n"
        f"• Leg 1: Departs Cape Town at 08:15; Arrives Johannesburg at {leg1_arr}\n"
        f"• Leg 2: Departs Johannesburg at {leg2_dep}; Arrives Polokwane at {final_arr}\n\n"
        f"1. Calculate the layover (connecting transfer) time at Johannesburg airport.\n"
        f"2. Calculate the total elapsed transit duration from departure in Cape Town to arrival in Polokwane."
    )
    explanation = (
        f"Step 1: Layover = {leg2_dep} - {leg1_arr} = {layover_mins} minutes = 1 hour 45 minutes [M].\n"
        f"Step 2: Total elapsed transit = {final_arr} - {start_time} = {total_transit_mins} minutes [M].\n"
        f"Step 3: Total transit = 8 hours 30 minutes [A]."
    )
    return _build_question_payload(
        subskill_id="39_multi_leg_journey_layover_scheduling",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract arrival of Leg 1 from departure of Leg 2 for layover. Subtract initial departure from final arrival for total duration.",
        tier_2=f"Layover = 13:10 - 11:25 = 1 h 45 min. Total = 16:45 - 08:15 = 8 h 30 min.",
        tier_3=f"Layover = 1 h 45 min; Total = 8 h 30 min.",
        r=r,
    )


def generate_40_delay_impact_on_scheduled_itinerary(r: random.Random) -> Dict[str, Any]:
    """Calculate the knock-on impact of an unexpected transit departure delay on arrival time and appointments."""
    sched_dep = "09:30"
    delay_mins = r.choice([35, 45, 50, 60])
    sched_duration_mins = 130  # 2 hours 10 mins

    sched_arr_mins = (9 * 60 + 30) + sched_duration_mins  # 570 + 130 = 700 = 11:40
    actual_dep_mins = (9 * 60 + 30) + delay_mins
    actual_arr_mins = actual_dep_mins + sched_duration_mins

    actual_arr_h = actual_arr_mins // 60
    actual_arr_m = actual_arr_mins % 60
    actual_arr_str = f"{actual_arr_h:02d}:{actual_arr_m:02d}"

    correct_ans = f"Scheduled Arrival = 11:40; Actual Arrival = {actual_arr_str} (delayed by {delay_mins} minutes)"

    custom_options = [
        correct_ans,
        f"Scheduled Arrival = 11:40; Actual Arrival = 11:40 (no delay on arrival)",
        f"Scheduled Arrival = 12:00; Actual Arrival = {actual_arr_h + 1:02d}:{actual_arr_m:02d}",
        f"Scheduled Arrival = 11:40; Actual Arrival = {actual_arr_h:02d}:{abs(actual_arr_m - 30):02d}",
    ]
    options, _ = _build_options(correct_ans, r, custom_options)

    name = r.choice(SA_NAMES)
    prompt = (
        f"{name} is scheduled to take a regional flight from Bloemfontein to Johannesburg:\n"
        f"• Scheduled departure: {sched_dep} | Scheduled flight duration: 2 hours 10 minutes\n"
        f"• Due to technical checks, departure is delayed by {delay_mins} minutes\n\n"
        f"Calculate {name}'s scheduled arrival time and the new expected actual arrival time."
    )
    explanation = (
        f"Step 1: Scheduled arrival = 09:30 + 2 hours 10 min = 11:40 [M].\n"
        f"Step 2: Add the {delay_mins}-minute delay to scheduled arrival: 11:40 + {delay_mins} min [M].\n"
        f"Step 3: New actual arrival = {actual_arr_str} [A]."
    )
    return _build_question_payload(
        subskill_id="40_delay_impact_on_scheduled_itinerary",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add flight duration to scheduled departure, then add the delay time.",
        tier_2=f"Scheduled = 09:30 + 2 h 10 min = 11:40. Actual = 11:40 + {delay_mins} min = {actual_arr_str}.",
        tier_3=f"Actual Arrival = {actual_arr_str}.",
        r=r,
    )
