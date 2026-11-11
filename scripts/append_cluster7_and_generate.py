# -*- coding: utf-8 -*-
"""Appends Cluster 7 and the generate function to conversions_time_generator.py."""

from pathlib import Path

target = Path("caps-ai-backend/app/utils/mathematical_literacy/conversions_time_generator.py")

content = '''
# ==============================================================================
# CLUSTER 7: TIME CALCULATIONS, TIMETABLES & SPEED (17 Archetypes)
# ==============================================================================

def _gen_time_unit_seconds_minutes(r: random.Random) -> Dict[str, Any]:
    mins = r.choice([2.5, 3.0, 4.5, 5.0, 6.0])
    total_sec = int(mins * 60)
    prompt = f"A track athlete recorded a training split of **{total_sec} seconds**.\\n\\nConvert this time into minutes (**min**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from seconds to minutes moves from a smaller unit to a larger unit, requiring **division** by 60.\\n"
        f"• Base relationship: $1\\\\text{{ minute}} = 60\\\\text{{ seconds}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Time in minutes}} = \\\\frac{{{total_sec}\\\\text{{ s}}}}{{60}} = {_fmt(mins)}\\\\text{{ min}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 60]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(mins)}\\\\text{{ min}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value in minutes]**"
    )
    return _make_q(
        subskill="time_unit_seconds_minutes",
        prompt=prompt,
        answer=f"{_fmt(mins)} min",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 60", f"1 Mark: Accuracy – {_fmt(mins)} min"],
        hints={
            "tier_1": "There are 60 seconds in 1 minute. Divide by 60.",
            "tier_2": f"Divide {total_sec} by 60.",
            "tier_3": f"{total_sec} ÷ 60 = {_fmt(mins)} min."
        },
        r=r
    )

def _gen_time_unit_minutes_hours(r: random.Random) -> Dict[str, Any]:
    hrs = r.choice([1.5, 2.25, 2.5, 3.75, 4.5])
    total_mins = int(hrs * 60)
    prompt = f"A soccer tournament match day had a cumulative playing duration of **{total_mins} minutes**.\\n\\nConvert this time to hours (**hours**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from minutes to hours moves to a larger unit, requiring **division** by 60.\\n"
        f"• Base relationship: $1\\\\text{{ hour}} = 60\\\\text{{ minutes}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Time in hours}} = \\\\frac{{{total_mins}\\\\text{{ min}}}}{{60}} = {_fmt(hrs)}\\\\text{{ hours}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 60]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(hrs)}\\\\text{{ hours}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value in hours]**"
    )
    return _make_q(
        subskill="time_unit_minutes_hours",
        prompt=prompt,
        answer=f"{_fmt(hrs)} hours",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 60", f"1 Mark: Accuracy – {_fmt(hrs)} hours"],
        hints={
            "tier_1": "There are 60 minutes in 1 hour. Divide by 60.",
            "tier_2": f"Divide {total_mins} by 60.",
            "tier_3": f"{total_mins} ÷ 60 = {_fmt(hrs)} hours."
        },
        r=r
    )

def _gen_time_unit_hours_days(r: random.Random) -> Dict[str, Any]:
    days = r.choice([2.5, 3.0, 4.5, 5.0])
    total_hours = int(days * 24)
    prompt = f"A weather warning for heavy rain is issued for a continuous duration of **{total_hours} hours**.\\n\\nConvert this duration to days (**days**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from hours to days moves to a larger unit, requiring **division** by 24.\\n"
        f"• Base relationship: $1\\\\text{{ day}} = 24\\\\text{{ hours}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Duration in days}} = \\\\frac{{{total_hours}\\\\text{{ hours}}}}{{24}} = {_fmt(days)}\\\\text{{ days}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 24]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(days)}\\\\text{{ days}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value in days]**"
    )
    return _make_q(
        subskill="time_unit_hours_days",
        prompt=prompt,
        answer=f"{_fmt(days)} days",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 24", f"1 Mark: Accuracy – {_fmt(days)} days"],
        hints={
            "tier_1": "There are 24 hours in 1 day. Divide by 24.",
            "tier_2": f"Divide {total_hours} by 24.",
            "tier_3": f"{total_hours} ÷ 24 = {_fmt(days)} days."
        },
        r=r
    )

def _gen_time_unit_days_weeks_months(r: random.Random) -> Dict[str, Any]:
    weeks = r.randint(4, 12)
    days = weeks * 7
    prompt = f"A construction crew is scheduled to complete a school roofing project in **{days} days**.\\n\\nConvert this project timeline into weeks (**weeks**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from days to weeks moves to a larger unit, requiring **division** by 7.\\n"
        f"• Base relationship: $1\\\\text{{ week}} = 7\\\\text{{ days}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Duration in weeks}} = \\\\frac{{{days}\\\\text{{ days}}}}{{7}} = {weeks}\\\\text{{ weeks}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 7]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{weeks}\\\\text{{ weeks}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct number of weeks]**"
    )
    return _make_q(
        subskill="time_unit_days_weeks_months",
        prompt=prompt,
        answer=f"{weeks} weeks",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 7", f"1 Mark: Accuracy – {weeks} weeks"],
        hints={
            "tier_1": "There are 7 days in 1 week. Divide by 7.",
            "tier_2": f"Divide {days} by 7.",
            "tier_3": f"{days} ÷ 7 = {weeks} weeks."
        },
        r=r
    )

def _gen_time_format_12h_to_24h(r: random.Random) -> Dict[str, Any]:
    hh = r.randint(1, 11)
    mm = r.choice([5, 10, 15, 20, 30, 45, 50])
    merid = "p.m."
    h_24 = hh + 12
    ans_24 = f"{h_24:02d}:{mm:02d}"
    prompt = f"A concert notice advertises starting time as **{hh:02d}:{mm:02d} {merid}**.\\n\\nConvert this time to standard 24-hour time format."
    sol = (
        f"**Step 1: 24-Hour Time Conversion Principle**\\n"
        f"• For afternoon and evening times (p.m.), add 12 hours to the hour value (except 12 p.m. which remains 12:00).\\n"
        f"• The minute digits remain unchanged.\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Hours}} = {hh} + 12 = {h_24} \\\\implies \\\\mathbf{{{ans_24}}}$$\\n"
        f"✓ **[1 Mark: Method – adding 12 hours to {hh:02d}]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_24}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – four-digit 24-hour notation]**"
    )
    return _make_q(
        subskill="time_format_12h_to_24h",
        prompt=prompt,
        answer=ans_24,
        sol=sol,
        rubric=[f"1 Mark: Method – {hh} + 12 = {h_24}", f"1 Mark: Accuracy – {ans_24}"],
        hints={
            "tier_1": "For p.m. times, add 12 to the hours.",
            "tier_2": f"Add 12 to {hh:02d}.",
            "tier_3": f"{hh:02d}:{mm:02d} p.m. = {ans_24}."
        },
        r=r
    )

def _gen_time_format_24h_to_12h(r: random.Random) -> Dict[str, Any]:
    h_24 = r.randint(13, 23)
    mm = r.choice([10, 15, 25, 40, 45, 55])
    hh_12 = h_24 - 12
    ans_12 = f"{hh_12:02d}:{mm:02d} p.m."
    prompt = f"A bus arrival board displays the time **{h_24:02d}:{mm:02d}**.\\n\\nConvert this time into 12-hour format with a.m. or p.m."
    sol = (
        f"**Step 1: 12-Hour Conversion Principle**\\n"
        f"• Since the hour is greater than 12 ({h_24} > 12), subtract 12 to find the 12-hour clock value and attach **p.m.**\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Hours}} = {h_24} - 12 = {hh_12} \\\\implies \\\\mathbf{{{ans_12}}}$$\\n"
        f"✓ **[1 Mark: Method – subtracting 12 hours]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_12}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct time with p.m. notation]**"
    )
    return _make_q(
        subskill="time_format_24h_to_12h",
        prompt=prompt,
        answer=ans_12,
        sol=sol,
        rubric=[f"1 Mark: Method – {h_24} - 12 = {hh_12}", f"1 Mark: Accuracy – {ans_12}"],
        hints={
            "tier_1": "Times from 13:00 onwards are in the afternoon/evening. Subtract 12 hours and write p.m.",
            "tier_2": f"Subtract 12 from {h_24}.",
            "tier_3": f"{h_24:02d}:{mm:02d} = {ans_12}."
        },
        r=r
    )

def _gen_time_decimal_to_hours_minutes(r: random.Random) -> Dict[str, Any]:
    h = r.randint(2, 6)
    m_choice = r.choice([15, 30, 45])
    dec_frac = m_choice / 60.0
    dec_val = h + dec_frac
    ans_text = f"{h} hours and {m_choice} minutes"
    prompt = f"A worker logs **{_fmt(dec_val)} hours** on an electronic timesheet.\\n\\nConvert this decimal time into hours and minutes."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• The whole number part ({h}) represents the complete hours.\\n"
        f"• The decimal portion ({_fmt(dec_frac)}) represents a fraction of an hour. Multiply this fraction by 60 to convert it into minutes:\\n"
        f"  $$\\\\text{{Minutes}} = {_fmt(dec_frac)} \\\\times 60 = {m_choice}\\\\text{{ minutes}}$$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Total Time}} = {h}\\\\text{{ hours and }} ({_fmt(dec_frac)} \\\\times 60)\\\\text{{ minutes}} = \\\\mathbf{{{ans_text}}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying decimal fraction by 60]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_text}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – hours and minutes correctly stated]**"
    )
    return _make_q(
        subskill="time_decimal_to_hours_minutes",
        prompt=prompt,
        answer=ans_text,
        sol=sol,
        rubric=[f"1 Mark: Method – {_fmt(dec_frac)} × 60 = {m_choice} minutes", f"1 Mark: Accuracy – {ans_text}"],
        hints={
            "tier_1": "Keep the whole number as hours, and multiply the decimal part by 60 to find minutes.",
            "tier_2": f"Multiply {_fmt(dec_frac)} by 60.",
            "tier_3": f"{_fmt(dec_val)} hours = {ans_text}."
        },
        r=r
    )

def _gen_time_elapsed_same_day(r: random.Random) -> Dict[str, Any]:
    h1 = r.randint(8, 10)
    m1 = r.choice([15, 20, 30])
    h2 = r.randint(13, 16)
    m2 = r.choice([35, 45, 50])

    t1_mins = h1 * 60 + m1
    t2_mins = h2 * 60 + m2
    diff_mins = t2_mins - t1_mins
    el_h = diff_mins // 60
    el_m = diff_mins % 60
    ans_text = f"{el_h} hours and {el_m} minutes"

    prompt = (
        f"A workshop session begins at **{h1:02d}:{m1:02d}** and finishes at **{h2:02d}:{m2:02d}** on the same day.\\n\\n"
        f"Calculate the total elapsed time of the workshop session."
    )
    sol = (
        f"**Step 1: Method Strategy & Thought Process**\\n"
        f"• Calculate the time difference between start ({h1:02d}:{m1:02d}) and finish ({h2:02d}:{m2:02d}):\\n"
        f"  - Hours difference: ${h2} - {h1} = {h2 - h1}\\\\text{{ hours}}$\\n"
        f"  - Minutes difference: ${m2} - {m1} = {m2 - m1}\\\\text{{ minutes}}$\\n"
        f"  - Total elapsed: **{ans_text}**\\n\\n"
        f"**Step 2: Method Setup**\\n"
        f"$$\\\\text{{Elapsed Time}} = {h2:02d}:{m2:02d} - {h1:02d}:{m1:02d} = \\\\mathbf{{{ans_text}}}$$\\n"
        f"✓ **[1 Mark: Method – subtracting start time from end time]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_text}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct hours and minutes]**"
    )
    return _make_q(
        subskill="time_elapsed_same_day",
        prompt=prompt,
        answer=ans_text,
        sol=sol,
        rubric=["1 Mark: Method – subtracting times", f"1 Mark: Accuracy – {ans_text}"],
        hints={
            "tier_1": "Subtract start time from end time.",
            "tier_2": f"From {h1:02d}:{m1:02d} to {h2:02d}:{m2:02d}.",
            "tier_3": f"Elapsed time = {ans_text}."
        },
        r=r
    )

def _gen_time_elapsed_crossing_midnight(r: random.Random) -> Dict[str, Any]:
    h1 = r.choice([21, 22, 23])
    m1 = r.choice([15, 30, 45])
    h2 = r.choice([4, 5, 6])
    m2 = r.choice([10, 20, 30])

    mins_to_midnight = (24 * 60) - (h1 * 60 + m1)
    mins_after_midnight = h2 * 60 + m2
    total_mins = mins_to_midnight + mins_after_midnight
    el_h = total_mins // 60
    el_m = total_mins % 60
    ans_text = f"{el_h} hours and {el_m} minutes"

    prompt = (
        f"A security guard begins a night shift at **{h1:02d}:{m1:02d}** and concludes the shift at **{h2:02d}:{m2:02d}** the following morning.\\n\\n"
        f"Calculate the total duration of the guard's night shift."
    )
    sol = (
        f"**Step 1: Crossing Midnight Strategy & Thought Process**\\n"
        f"• When a time interval crosses midnight (24:00 / 00:00), split the calculation into two parts:\\n"
        f"  1. Time from start to midnight: $24:00 - {h1:02d}:{m1:02d} = {mins_to_midnight // 60}\\\\text{{ hours and }} {mins_to_midnight % 60}\\\\text{{ minutes}}$\\n"
        f"  2. Time from midnight to morning end: ${h2:02d}:{m2:02d} = {h2}\\\\text{{ hours and }} {m2}\\\\text{{ minutes}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Total Minutes}} = {mins_to_midnight} + {mins_after_midnight} = {total_mins}\\\\text{{ minutes}} = \\\\mathbf{{{ans_text}}}$$\\n"
        f"✓ **[1 Mark: Method – splitting at midnight and summing]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_text}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct total shift duration]**"
    )
    return _make_q(
        subskill="time_elapsed_crossing_midnight",
        prompt=prompt,
        answer=ans_text,
        sol=sol,
        rubric=["1 Mark: Method – calculation crossing midnight", f"1 Mark: Accuracy – {ans_text}"],
        hints={
            "tier_1": "Calculate time to midnight (24:00), then add the morning time.",
            "tier_2": f"From {h1:02d}:{m1:02d} to 24:00 is {mins_to_midnight} minutes. Then add {mins_after_midnight} minutes.",
            "tier_3": f"Total = {ans_text}."
        },
        r=r
    )

def _gen_time_elapsed_multi_day(r: random.Random) -> Dict[str, Any]:
    dep_day = "Friday"
    arr_day = "Sunday"
    dep_time = "14:00"
    arr_time = "18:30"
    total_hours = 52.5  # 24 + 24 + 4.5
    prompt = (
        f"A freight cargo train departs Polokwane on **{dep_day} at {dep_time}** and reaches Cape Town harbor on **{arr_day} at {arr_time}**.\\n\\n"
        f"Calculate the total travel duration in **hours**."
    )
    sol = (
        f"**Step 1: Multi-Day Time Breakdown & Thought Process**\\n"
        f"• Friday 14:00 to Saturday 14:00 = 24 hours\\n"
        f"• Saturday 14:00 to Sunday 14:00 = 24 hours\\n"
        f"• Sunday 14:00 to Sunday 18:30 = 4 hours 30 minutes (4,5 hours)\\n\\n"
        f"**Step 2: Method Setup & Summation**\\n"
        f"$$\\\\text{{Total Time}} = 24 + 24 + 4{{,}}5 = 52{{,}}5\\\\text{{ hours}}$$\\n"
        f"✓ **[1 Mark: Method – 48 hours for 2 full days plus 4,5 hours remaining]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{52{{,}}5\\\\text{{ hours (or 52 hours 30 minutes)}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – 52,5 hours]**"
    )
    options = [
        "52,5 hours (52 hrs 30 min)",
        "48,5 hours (48 hrs 30 min)",
        "56,5 hours (56 hrs 30 min)",
        "50,0 hours (50 hrs 00 min)",
    ]
    return _make_q(
        subskill="time_elapsed_multi_day",
        prompt=prompt,
        answer="52,5 hours (52 hrs 30 min)",
        sol=sol,
        rubric=["1 Mark: Method – 24 + 24 + 4,5 hours", "1 Mark: Accuracy – 52,5 hours (52 hrs 30 min)"],
        hints={
            "tier_1": "Count the full 24-hour days first: Friday 14:00 to Sunday 14:00 = 48 hours.",
            "tier_2": "Add the remaining time: Sunday 14:00 to 18:30 = 4,5 hours.",
            "tier_3": "48 + 4,5 = 52,5 hours."
        },
        options=options,
        r=r
    )

def _gen_time_schedule_bus_timetable(r: random.Random) -> Dict[str, Any]:
    timetable_md = (
        "| Bus Trip | Baragwanath (Dep) | Park Station | Sandton (Arr) |\\n"
        "| :---: | :---: | :---: | :---: |\\n"
        "| **Bus 1** | 06:15 | 06:55 | 07:35 |\\n"
        "| **Bus 2** | 06:45 | 07:25 | 08:05 |"
    )
    prompt = (
        f"Refer to the commuter bus timetable below:\\n\\n"
        f"{timetable_md}\\n\\n"
        f"**Required:**\\n"
        f"1. How long (in minutes) does Bus 1 take to travel from Baragwanath to Park Station?\\n"
        f"2. A commuter needs to arrive in Sandton before 07:50 for a job interview. Which bus must the commuter board?"
    )
    sol = (
        f"**Step 1: Reading & Travel Duration**\\n"
        f"• Bus 1 departs Baragwanath at 06:15 and arrives at Park Station at 06:55.\\n"
        f"  $$\\\\text{{Duration}} = 06:55 - 06:15 = 40\\\\text{{ minutes}}$$\\n"
        f"✓ **[1 Mark: Method – subtracting departure from arrival time]**\\n\\n"
        f"**Step 2: Timetable Analysis & Bus Selection**\\n"
        f"• Bus 1 reaches Sandton at 07:35 (which is before 07:50).\\n"
        f"• Bus 2 reaches Sandton at 08:05 (which is too late).\\n"
        f"• Therefore, the commuter must take **Bus 1**.\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"**1. 40 minutes | 2. Bus 1**\\n"
        f"✓ **[1 Mark: Accuracy – correct travel time and bus choice]**"
    )
    options = [
        "1. 40 minutes | 2. Bus 1",
        "1. 40 minutes | 2. Bus 2",
        "1. 30 minutes | 2. Bus 1",
        "1. 50 minutes | 2. Bus 2",
    ]
    return _make_q(
        subskill="time_schedule_bus_timetable",
        prompt=prompt,
        answer="1. 40 minutes | 2. Bus 1",
        sol=sol,
        rubric=["1 Mark: Method – 06:55 - 06:15 = 40 minutes", "1 Mark: Accuracy – Bus 1"],
        hints={
            "tier_1": "Subtract Bus 1 Baragwanath departure from Park Station arrival: 06:55 - 06:15.",
            "tier_2": "Check Sandton arrival times: Bus 1 arrives at 07:35, Bus 2 at 08:05.",
            "tier_3": "1. 40 minutes | 2. Bus 1."
        },
        options=options,
        r=r
    )

def _gen_time_schedule_train_flight(r: random.Random) -> Dict[str, Any]:
    dep_time = "09:40"
    prompt = (
        f"A domestic flight from Johannesburg (OR Tambo) to Cape Town is scheduled to depart at **{dep_time}**.\\n\\n"
        f"1. Passengers must check in **2 hours** prior to departure. Determine the latest check-in time.\\n"
        f"2. Boarding gates close **30 minutes** before departure. What time does the boarding gate close?"
    )
    sol = (
        f"**Step 1: Check-in Time Calculation**\\n"
        f"• Subtract 2 hours from departure time:\\n"
        f"  $$09:40 - 2\\\\text{{ hours}} = \\\\mathbf{{07:40}}$$\\n"
        f"✓ **[1 Mark: Method – subtracting 2 hours]**\\n\\n"
        f"**Step 2: Gate Closing Time Calculation**\\n"
        f"• Subtract 30 minutes from departure time:\\n"
        f"  $$09:40 - 30\\\\text{{ minutes}} = \\\\mathbf{{09:10}}$$\\n"
        f"✓ **[1 Mark: Method – subtracting 30 minutes]**\\n\\n"
        f"**Step 3: Final Combined Answer**\\n"
        f"**1. 07:40 | 2. 09:10**\\n"
        f"✓ **[1 Mark: Accuracy – both flight times correct]**"
    )
    options = [
        "1. 07:40 | 2. 09:10",
        "1. 07:40 | 2. 09:20",
        "1. 08:40 | 2. 09:10",
        "1. 06:40 | 2. 08:40",
    ]
    return _make_q(
        subskill="time_schedule_train_flight",
        prompt=prompt,
        answer="1. 07:40 | 2. 09:10",
        sol=sol,
        rubric=[
            "1 Mark: Method – 09:40 - 2 hours = 07:40",
            "1 Mark: Method – 09:40 - 30 min = 09:10",
            "1 Mark: Accuracy – 1. 07:40 | 2. 09:10"
        ],
        hints={
            "tier_1": "Subtract 2 hours from 09:40 for check-in; subtract 30 minutes from 09:40 for gate closing.",
            "tier_2": "09:40 - 2:00 = 07:40; 09:40 - 0:30 = 09:10.",
            "tier_3": "1. 07:40 | 2. 09:10."
        },
        options=options,
        total_marks=3,
        r=r
    )

def _gen_time_tide_table_reading(r: random.Random) -> Dict[str, Any]:
    ht1_time = "04:18"
    ht1_height = 2.15
    lt1_time = "10:32"
    lt1_height = 0.42

    tide_table_md = (
        "| Date | High Tide (Time / Height) | Low Tide (Time / Height) |\\n"
        "| :---: | :---: | :---: |\\n"
        f"| **14 Oct (Durban)** | {ht1_time} ({_fmt(ht1_height)} m) | {lt1_time} ({_fmt(lt1_height)} m) |"
    )
    prompt = (
        f"Refer to the coastal tide chart for Durban beach below:\\n\\n"
        f"{tide_table_md}\\n\\n"
        f"**Required:**\\n"
        f"1. Calculate the elapsed time between High Tide and Low Tide.\\n"
        f"2. Calculate the tidal range (difference in water height between high and low tide) in metres."
    )
    diff_h = 10 - 4
    diff_m = 32 - 18
    range_m = round(ht1_height - lt1_height, 2)
    ans_label = f"1. {diff_h} hrs {diff_m} min | 2. {_fmt(range_m)} m"

    sol = (
        f"**Step 1: Elapsed Time Calculation**\\n"
        f"$$10:32 - 04:18 = {diff_h}\\\\text{{ hours and }} {diff_m}\\\\text{{ minutes}}$$\\n"
        f"✓ **[1 Mark: Method – subtracting tide times]**\\n\\n"
        f"**Step 2: Tidal Range Calculation**\\n"
        f"$$\\\\text{{Tidal Range}} = {_fmt(ht1_height)}\\\\text{{ m}} - {_fmt(lt1_height)}\\\\text{{ m}} = {_fmt(range_m)}\\\\text{{ m}}$$\\n"
        f"✓ **[1 Mark: Method – subtracting water heights]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"**{ans_label}**\\n"
        f"✓ **[1 Mark: Accuracy – correct elapsed time and range]**"
    )
    options = [
        ans_label,
        f"1. {diff_h + 1} hrs {diff_m} min | 2. {_fmt(range_m)} m",
        f"1. {diff_h} hrs {diff_m} min | 2. {_fmt(round(range_m + 0.4, 2))} m",
        f"1. {diff_h - 1} hrs {diff_m + 10} min | 2. {_fmt(round(range_m - 0.3, 2))} m",
    ]
    return _make_q(
        subskill="time_tide_table_reading",
        prompt=prompt,
        answer=ans_label,
        sol=sol,
        rubric=[
            f"1 Mark: Method – 10:32 - 04:18 = {diff_h}h {diff_m}m",
            f"1 Mark: Method – {_fmt(ht1_height)} - {_fmt(lt1_height)} = {_fmt(range_m)} m",
            f"1 Mark: Accuracy – {ans_label}"
        ],
        hints={
            "tier_1": "1. Subtract High Tide time from Low Tide time. 2. Subtract Low Tide height from High Tide height.",
            "tier_2": f"10:32 - 04:18 = {diff_h}h {diff_m}m; {ht1_height} - {lt1_height} = {_fmt(range_m)} m.",
            "tier_3": f"{ans_label}."
        },
        options=options,
        total_marks=3,
        r=r
    )

def _gen_speed_distance_time_travel_duration(r: random.Random) -> Dict[str, Any]:
    speed_kmh = r.choice([80, 100, 120])
    hours = r.choice([2.5, 3.0, 3.5, 4.0])
    dist_km = int(speed_kmh * hours)
    h_int = int(hours)
    m_int = int((hours - h_int) * 60)
    ans_text = f"{h_int} hours and {m_int} minutes" if m_int else f"{h_int} hours"

    prompt = (
        f"A delivery vehicle travels between Johannesburg and Polokwane, covering a distance of **{dist_km} km** "
        f"at an average speed of **{speed_kmh} km/h**.\\n\\n"
        f"Calculate the total travel time."
    )
    sol = (
        f"**Step 1: Formula & Thought Process**\\n"
        f"• The relationship between Speed, Distance, and Time is:\\n"
        f"  $$\\\\text{{Time}} = \\\\frac{{\\\\text{{Distance}}}}{{\\\\text{{Speed}}}}$$\\n"
        f"• Divide total distance ({dist_km} km) by average speed ({speed_kmh} km/h).\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Time in hours}} = \\\\frac{{{dist_km}\\\\text{{ km}}}}{{{speed_kmh}\\\\text{{ km/h}}}} = {_fmt(hours)}\\\\text{{ hours}}$$\\n"
        f"✓ **[1 Mark: Method – dividing distance by speed]**\\n\\n"
        f"**Step 3: Conversion to Hours and Minutes**\\n"
        f"$$\\\\mathbf{{{ans_text}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – travel time stated correctly]**"
    )
    return _make_q(
        subskill="speed_distance_time_travel_duration",
        prompt=prompt,
        answer=ans_text,
        sol=sol,
        rubric=[f"1 Mark: Method – {dist_km} ÷ {speed_kmh} = {_fmt(hours)} hours", f"1 Mark: Accuracy – {ans_text}"],
        hints={
            "tier_1": "Formula: Time = Distance ÷ Speed.",
            "tier_2": f"Divide {dist_km} by {speed_kmh}.",
            "tier_3": f"{dist_km} ÷ {speed_kmh} = {_fmt(hours)} hours = {ans_text}."
        },
        r=r
    )

def _gen_speed_unit_conversion_kmh_to_ms(r: random.Random) -> Dict[str, Any]:
    kmh = r.choice([60, 90, 100, 120])
    ms = round(kmh / 3.6, 2)
    prompt = (
        f"A motor vehicle travels at a speed of **{kmh} km/h** on a national freeway.\\n\\n"
        f"Convert this speed into metres per second (**m/s**). Round your answer to two decimal places."
    )
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• To convert km/h to m/s:\\n"
        f"  $$1\\\\text{{ km/h}} = \\\\frac{{1\\\\ 000\\\\text{{ m}}}}{{3\\\\ 600\\\\text{{ s}}}} = \\\\frac{{1}}{{3{{,}}6}}\\\\text{{ m/s}}$$\\n"
        f"• Divide the speed in km/h by the standard factor 3,6.\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Speed in m/s}} = \\\\frac{{{kmh}}}{{3{{,}}6}} = {_fmt(ms)}\\\\text{{ m/s}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 3,6]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ms)}\\\\text{{ m/s}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct speed rounded to 2 decimal places]**"
    )
    return _make_q(
        subskill="speed_unit_conversion_kmh_to_ms",
        prompt=prompt,
        answer=f"{_fmt(ms)} m/s",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 3,6", f"1 Mark: Accuracy – {_fmt(ms)} m/s"],
        hints={
            "tier_1": "To convert from km/h to m/s, divide by 3,6.",
            "tier_2": f"Divide {kmh} by 3,6.",
            "tier_3": f"{kmh} ÷ 3,6 = {_fmt(ms)} m/s."
        },
        r=r
    )

def _gen_time_international_time_zones(r: random.Random) -> Dict[str, Any]:
    jhb_h = r.choice([14, 16, 18])
    jhb_m = 30
    diff = 2  # London UTC+0, JHB UTC+2 -> London is 2 hours behind
    lon_h = jhb_h - diff
    ans_text = f"{lon_h:02d}:{jhb_m:02d}"

    prompt = (
        f"South African Standard Time (Johannesburg) is **UTC+2**, while Greenwich Mean Time (London) is **UTC+0**.\\n\\n"
        f"If a live rugby match kicks off in Johannesburg at **{jhb_h:02d}:{jhb_m:02d}**, "
        f"what is the local broadcast time in London (24-hour format)?"
    )
    sol = (
        f"**Step 1: Time Zone Analysis & Thought Process**\\n"
        f"• Johannesburg is UTC+2 and London is UTC+0.\\n"
        f"• London is 2 hours behind Johannesburg (subtract 2 hours).\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{London Time}} = {jhb_h:02d}:{jhb_m:02d} - 2\\\\text{{ hours}} = \\\\mathbf{{{ans_text}}}$$\\n"
        f"✓ **[1 Mark: Method – subtracting 2 hours]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_text}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – 24-hour time notation]**"
    )
    return _make_q(
        subskill="time_international_time_zones",
        prompt=prompt,
        answer=ans_text,
        sol=sol,
        rubric=["1 Mark: Method – subtracting 2 hours for UTC+0", f"1 Mark: Accuracy – {ans_text}"],
        hints={
            "tier_1": "London is 2 hours behind Johannesburg. Subtract 2 hours.",
            "tier_2": f"Subtract 2 hours from {jhb_h:02d}:{jhb_m:02d}.",
            "tier_3": f"{jhb_h:02d}:{jhb_m:02d} - 2 hours = {ans_text}."
        },
        r=r
    )

def _gen_time_pace_speed_running(r: random.Random) -> Dict[str, Any]:
    dist_km = r.choice([5, 10, 15, 21])
    min_per_km = r.choice([4.5, 5.0, 5.5, 6.0])
    total_mins = int(dist_km * min_per_km)
    sec_rem = int((min_per_km - int(min_per_km)) * 60)
    ans_text = f"{int(min_per_km)} min {sec_rem:02d} s per km" if sec_rem else f"{int(min_per_km)} min per km"

    prompt = (
        f"A runner completes a **{dist_km} km** road race in exactly **{total_mins} minutes**.\\n\\n"
        f"Calculate the runner's average running pace in **minutes per kilometre (min/km)**."
    )
    sol = (
        f"**Step 1: Formula & Thought Process**\\n"
        f"• Running pace measures the time taken to complete 1 kilometre:\\n"
        f"  $$\\\\text{{Pace}} = \\\\frac{{\\\\text{{Total Time in Minutes}}}}{{\\\\text{{Distance in km}}}}$$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Pace}} = \\\\frac{{{total_mins}\\\\text{{ minutes}}}}{{{dist_km}\\\\text{{ km}}}} = {_fmt(min_per_km)}\\\\text{{ min/km}}$$\\n"
        f"✓ **[1 Mark: Method – dividing total minutes by distance]**\\n\\n"
        f"**Step 3: Conversion to Minutes and Seconds**\\n"
        f"• {_fmt(min_per_km)} min/km = **{ans_text}**\\n"
        f"✓ **[1 Mark: Accuracy – correct pace per km]**"
    )
    return _make_q(
        subskill="time_pace_speed_running",
        prompt=prompt,
        answer=ans_text,
        sol=sol,
        rubric=[f"1 Mark: Method – {total_mins} ÷ {dist_km} = {_fmt(min_per_km)} min/km", f"1 Mark: Accuracy – {ans_text}"],
        hints={
            "tier_1": "Formula: Pace = Total Minutes ÷ Total Kilometres.",
            "tier_2": f"Divide {total_mins} by {dist_km}.",
            "tier_3": f"{total_mins} ÷ {dist_km} = {_fmt(min_per_km)} min/km = {ans_text}."
        },
        r=r
    )


# ==============================================================================
# TOP-LEVEL GENERATE FUNCTION
# ==============================================================================

DISPATCH_TABLE = {
    "conv_len_mm_to_cm": _gen_conv_len_mm_to_cm,
    "conv_len_cm_to_mm": _gen_conv_len_cm_to_mm,
    "conv_len_cm_to_m": _gen_conv_len_cm_to_m,
    "conv_len_m_to_cm": _gen_conv_len_m_to_cm,
    "conv_len_mm_to_m": _gen_conv_len_mm_to_m,
    "conv_len_m_to_mm": _gen_conv_len_m_to_mm,
    "conv_len_m_to_km": _gen_conv_len_m_to_km,
    "conv_len_km_to_m": _gen_conv_len_km_to_m,

    "conv_mass_g_to_kg": _gen_conv_mass_g_to_kg,
    "conv_mass_kg_to_g": _gen_conv_mass_kg_to_g,
    "conv_mass_kg_to_tonne": _gen_conv_mass_kg_to_tonne,
    "conv_mass_tonne_to_kg": _gen_conv_mass_tonne_to_kg,
    "conv_mass_mg_to_g": _gen_conv_mass_mg_to_g,
    "conv_mass_g_to_mg": _gen_conv_mass_g_to_mg,
    "conv_mass_multi_step_tonne_to_g": _gen_conv_mass_multi_step_tonne_to_g,

    "conv_vol_ml_to_l": _gen_conv_vol_ml_to_l,
    "conv_vol_l_to_ml": _gen_conv_vol_l_to_ml,
    "conv_vol_l_to_kl": _gen_conv_vol_l_to_kl,
    "conv_vol_kl_to_l": _gen_conv_vol_kl_to_l,
    "conv_vol_cm3_to_ml": _gen_conv_vol_cm3_to_ml,
    "conv_vol_cm3_to_l": _gen_conv_vol_cm3_to_l,
    "conv_vol_m3_to_l": _gen_conv_vol_m3_to_l,

    "cook_tsp_to_ml": _gen_cook_tsp_to_ml,
    "cook_tbsp_to_ml": _gen_cook_tbsp_to_ml,
    "cook_tbsp_to_tsp": _gen_cook_tbsp_to_tsp,
    "cook_cups_to_ml": _gen_cook_cups_to_ml,
    "cook_recipe_scaling": _gen_cook_recipe_scaling,
    "cook_dry_cups_to_grams": _gen_cook_dry_cups_to_grams,

    "conv_imperial_inches_feet_to_cm_m": _gen_conv_imperial_inches_feet_to_cm_m,
    "conv_imperial_pounds_gallons_to_metric": _gen_conv_imperial_pounds_gallons_to_metric,

    "temp_celsius_to_fahrenheit": _gen_temp_celsius_to_fahrenheit,
    "temp_fahrenheit_to_celsius": _gen_temp_fahrenheit_to_celsius,
    "temp_baking_oven_setting": _gen_temp_baking_oven_setting,
    "temp_weather_comparison": _gen_temp_weather_comparison,
    "temp_negative_freezing_c_to_f": _gen_temp_negative_freezing_c_to_f,

    "time_unit_seconds_minutes": _gen_time_unit_seconds_minutes,
    "time_unit_minutes_hours": _gen_time_unit_minutes_hours,
    "time_unit_hours_days": _gen_time_unit_hours_days,
    "time_unit_days_weeks_months": _gen_time_unit_days_weeks_months,
    "time_format_12h_to_24h": _gen_time_format_12h_to_24h,
    "time_format_24h_to_12h": _gen_time_format_24h_to_12h,
    "time_decimal_to_hours_minutes": _gen_time_decimal_to_hours_minutes,
    "time_elapsed_same_day": _gen_time_elapsed_same_day,
    "time_elapsed_crossing_midnight": _gen_time_elapsed_crossing_midnight,
    "time_elapsed_multi_day": _gen_time_elapsed_multi_day,
    "time_schedule_bus_timetable": _gen_time_schedule_bus_timetable,
    "time_schedule_train_flight": _gen_time_schedule_train_flight,
    "time_tide_table_reading": _gen_time_tide_table_reading,
    "speed_distance_time_travel_duration": _gen_speed_distance_time_travel_duration,
    "speed_unit_conversion_kmh_to_ms": _gen_speed_unit_conversion_kmh_to_ms,
    "time_international_time_zones": _gen_time_international_time_zones,
    "time_pace_speed_running": _gen_time_pace_speed_running,
}

def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation function.
    Deterministic execution via seeded Random instance.
    """
    actual_seed = seed if seed is not None else random.randint(1, 1_000_000)
    r = random.Random(actual_seed)

    if archetype_index is not None and 0 <= archetype_index < len(SUBSKILLS):
        chosen_subskill = SUBSKILLS[archetype_index]
    elif subskill and subskill in DISPATCH_TABLE:
        chosen_subskill = subskill
    else:
        chosen_subskill = r.choice(SUBSKILLS)

    generator_fn = DISPATCH_TABLE[chosen_subskill]
    q = generator_fn(r)
    return [q]
'''

with open(target, "a", encoding="utf-8") as f:
    f.write(content)

print("Cluster 7 and generate appended successfully.")
