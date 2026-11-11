"""Cluster 2: Metric to Imperial Length, Distance & Speed (Subskills 10 to 18)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def _gen_inches_to_centimetres_screen_size(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_inches_to_centimetres_screen_size"
    name = r.choice(SA_NAMES)
    inches = r.choice([32, 40, 43, 50, 55, 65, 75])
    cm_val = round(inches * 2.54, 1)
    correct_ans = f"{_fmt(cm_val)} cm"

    prompt = (
        f"{name} buys a smart television with a screen diagonal of **{inches} inches**.\n\n"
        f"**Given conversion factor**: $1\\text{{ inch}} = 2,54\\text{{ cm}}$\n\n"
        f"Calculate the diagonal screen size in **centimetres (cm)**, rounded to 1 decimal place."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Multiply the number of inches by 2,54 to convert to centimetres: "
        f"$$\\text{{Length in cm}} = \\text{{Length in inches}} \\times 2,54$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Screen Size}} = {inches} \\times 2,54$$ "
        f"✓ [1 Mark: Method – multiplying screen inches by 2,54 cm/inch]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Screen Size}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate centimetres]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply inches by 2,54.",
        tier_2=f"{inches} × 2,54 = {correct_ans}.",
        tier_3=f"Screen size = {correct_ans}.",
        r=r,
    )


def _gen_centimetres_to_inches_height(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_centimetres_to_inches_height"
    name = r.choice(SA_NAMES)
    cm_val = r.choice([160, 168, 175, 180, 185, 192])
    inches = round(cm_val / 2.54, 1)
    correct_ans = f"{_fmt(inches)} inches"

    prompt = (
        f"A passport application requires {name}'s height of **{cm_val} cm** to be converted into **inches**.\n\n"
        f"**Given conversion factor**: $1\\text{{ inch}} = 2,54\\text{{ cm}}$\n\n"
        f"Convert {cm_val} cm into inches, rounded to 1 decimal place."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To convert from centimetres to inches, divide by 2,54: "
        f"$$\\text{{Inches}} = \\frac{{\\text{{Centimetres}}}}{{2,54}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Inches}} = \\frac{{{cm_val}}}{{2,54}} = {_fmt(cm_val / 2.54, 3)}$$ "
        f"✓ [1 Mark: Method – dividing centimetres by 2,54]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Height}} \\approx {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate rounded inches]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide centimetres by 2,54.",
        tier_2=f"{cm_val} ÷ 2,54 = {_fmt(inches)} inches.",
        tier_3=f"Height = {correct_ans}.",
        r=r,
    )


def _gen_feet_and_inches_to_metres_person(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_feet_and_inches_to_metres_person"
    name = r.choice(SA_NAMES)
    feet = r.choice([5, 6])
    inches = r.randint(2, 11)
    total_inches = (feet * 12) + inches
    cm_val = total_inches * 2.54
    metres = round(cm_val / 100.0, 2)
    correct_ans = f"{_fmt(metres)} m"

    prompt = (
        f"{name}'s height is stated as **{feet} feet and {inches} inches (5' {inches}\")**.\n\n"
        f"**Given conversion factors**:\n"
        f"  • $1\\text{{ foot (ft)}} = 12\\text{{ inches}}$\n"
        f"  • $1\\text{{ inch}} = 2,54\\text{{ cm}}$\n"
        f"  • $1\\text{{ m}} = 100\\text{{ cm}}$\n\n"
        f"Convert {name}'s height into **metres (m)**, rounded to 2 decimal places."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"First convert feet into inches: $\\text{{Inches}} = ({feet} \\times 12) + {inches} = {total_inches}\\text{{ inches}}$.\n"
        f"Multiply by 2,54 to get centimetres, then divide by 100 to get metres.\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Total Inches}} = ({feet} \\times 12) + {inches} = {total_inches}\\text{{ in}}$$\n"
        f"$$\\text{{Height in cm}} = {total_inches} \\times 2,54 = {_fmt(cm_val)}\\text{{ cm}}$$\n"
        f"$$\\text{{Height in m}} = \\frac{{{_fmt(cm_val)}}}{{100}}$$ "
        f"✓ [1 Mark: Method – converting feet/inches to total inches and applying 2,54 cm/inch]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Height}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate height in metres]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1=f"Total inches = ({feet} × 12) + {inches}. Multiply by 2,54, then divide by 100.",
        tier_2=f"{total_inches} in × 2,54 = {_fmt(cm_val)} cm = {correct_ans}.",
        tier_3=f"Height = {correct_ans}.",
        r=r,
    )


def _gen_metres_to_yards_sports_field(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_metres_to_yards_sports_field"
    metres = r.choice([50, 80, 100, 120])
    # 1 yard = 0.9144 m  ==>  yards = metres / 0.9144
    factor = 0.9144
    yards = round(metres / factor, 1)
    correct_ans = f"{_fmt(yards)} yards"

    prompt = (
        f"A rugby sports field has a length of **{metres} m**.\n\n"
        f"**Given conversion factor**: $1\\text{{ yard}} = 0,9144\\text{{ m}}$\n\n"
        f"Convert {metres} m to **yards**, rounded to 1 decimal place."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Because 1 yard is 0,9144 metres, divide metres by 0,9144 to convert to yards: "
        f"$$\\text{{Yards}} = \\frac{{\\text{{Metres}}}}{{0,9144}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Yards}} = \\frac{{{metres}}}{{0,9144}} = {_fmt(metres / factor, 3)}$$ "
        f"✓ [1 Mark: Method – dividing distance in metres by 0,9144 m/yard]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Distance}} \\approx {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate rounded yards]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide metres by 0,9144.",
        tier_2=f"{metres} ÷ 0,9144 = {_fmt(yards)} yards.",
        tier_3=f"Yards = {correct_ans}.",
        r=r,
    )


def _gen_miles_to_kilometres_road_travel(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_miles_to_kilometres_road_travel"
    name = r.choice(SA_NAMES)
    miles = r.choice([45, 60, 75, 120, 150, 240])
    factor = 1.60934
    km_val = round(miles * factor, 1)
    correct_ans = f"{_fmt(km_val)} km"

    prompt = (
        f"{name} rents a vehicle in the United States and drives a route measuring **{miles} miles**.\n\n"
        f"**Given conversion factor**: $1\\text{{ mile}} \\approx 1,60934\\text{{ km}}$\n\n"
        f"Convert {miles} miles into **kilometres (km)**, rounded to 1 decimal place."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Multiply the distance in miles by 1,60934 to convert to kilometres: "
        f"$$\\text{{Kilometres}} = \\text{{Miles}} \\times 1,60934$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Kilometres}} = {miles} \\times 1,60934 = {_fmt(miles * factor, 3)}$$ "
        f"✓ [1 Mark: Method – multiplying miles by 1,60934 km/mile]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Distance}} \\approx {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate distance in km]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply miles by 1,60934.",
        tier_2=f"{miles} × 1,60934 = {_fmt(km_val)} km.",
        tier_3=f"Kilometres = {correct_ans}.",
        r=r,
    )


def _gen_kilometres_to_miles_marathon(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_kilometres_to_miles_marathon"
    name = r.choice(SA_NAMES)
    km_dist = r.choice([21.1, 42.2, 50.0, 90.0])  # Half marathon, full marathon, Comrades ultra
    miles = round(km_dist / 1.60934, 1)
    correct_ans = f"{_fmt(miles)} miles"

    race = "Comrades Ultra Marathon" if km_dist == 90.0 else "standard marathon race"
    prompt = (
        f"{name} completes a {race} with a measured course distance of **{_fmt(km_dist)} km**.\n\n"
        f"**Given conversion factor**: $1\\text{{ mile}} \\approx 1,60934\\text{{ km}}$\n\n"
        f"Convert this distance into **miles**, rounded off to 1 decimal place."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To convert from kilometres to miles, divide by 1,60934: "
        f"$$\\text{{Miles}} = \\frac{{\\text{{Kilometres}}}}{{1,60934}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Miles}} = \\frac{{{_fmt(km_dist)}}}{{1,60934}} = {_fmt(km_dist / 1.60934, 3)}$$ "
        f"✓ [1 Mark: Method – dividing kilometres by 1,60934]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Distance}} \\approx {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate rounded miles]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide kilometres by 1,60934.",
        tier_2=f"{_fmt(km_dist)} ÷ 1,60934 = {_fmt(miles)} miles.",
        tier_3=f"Miles = {correct_ans}.",
        r=r,
    )


def _gen_speed_kmh_to_mph(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_speed_kmh_to_mph"
    speed_kmh = r.choice([60, 80, 100, 120])
    speed_mph = round(speed_kmh / 1.60934, 1)
    correct_ans = f"{_fmt(speed_mph)} mph"

    prompt = (
        f"A South African national highway has a maximum speed limit of **{speed_kmh} km/h**.\n"
        f"An imported car's dashboard speedometer reads in **miles per hour (mph)**.\n\n"
        f"**Given conversion factor**: $1\\text{{ mph}} \\approx 1,60934\\text{{ km/h}}$\n\n"
        f"Calculate the speed limit equivalent in miles per hour (mph), rounded to 1 decimal place."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Divide the speed in km/h by 1,60934 to convert to miles per hour: "
        f"$$\\text{{Speed in mph}} = \\frac{{\\text{{Speed in km/h}}}}{{1,60934}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Speed}} = \\frac{{{speed_kmh}}}{{1,60934}} = {_fmt(speed_kmh / 1.60934, 3)}$$ "
        f"✓ [1 Mark: Method – dividing km/h by 1,60934]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Speed}} \\approx {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate speed in mph]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide speed in km/h by 1,60934.",
        tier_2=f"{speed_kmh} ÷ 1,60934 = {_fmt(speed_mph)} mph.",
        tier_3=f"Speed = {correct_ans}.",
        r=r,
    )


def _gen_speed_kmh_to_metres_per_second(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_speed_kmh_to_metres_per_second"
    speed_kmh = r.choice([36, 54, 72, 90, 108, 126])  # Multiples of 18 give clean decimals
    speed_ms = round(speed_kmh / 3.6, 2)
    correct_ans = f"{_fmt(speed_ms)} m/s"

    prompt = (
        f"A passenger car travels on a freeway at a speed of **{speed_kmh} km/h**.\n\n"
        f"**Conversion identity**: $1\\text{{ km/h}} = \\frac{{1\\,000\\text{{ m}}}}{{3\\,600\\text{{ s}}}} = \\frac{{1}}{{3,6}}\\text{{ m/s}}$\n\n"
        f"Convert {speed_kmh} km/h into **metres per second (m/s)**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"To convert from km/h to m/s, divide the speed by 3,6 (since 1 km = 1 000 m and 1 hour = 3 600 s): "
        f"$$\\text{{Speed in m/s}} = \\frac{{\\text{{Speed in km/h}}}}{{3,6}}$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Speed}} = \\frac{{{speed_kmh}}}{{3,6}}$$ "
        f"✓ [1 Mark: Method – dividing speed in km/h by 3,6]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Speed}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate speed in m/s]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Divide the speed by 3,6.",
        tier_2=f"{speed_kmh} ÷ 3,6 = {correct_ans}.",
        tier_3=f"Speed = {correct_ans}.",
        r=r,
    )


def _gen_speed_metres_per_second_to_kmh(r: random.Random) -> Dict[str, Any]:
    sub_id = "gr11_conv_speed_metres_per_second_to_kmh"
    speed_ms = r.choice([15.0, 20.0, 25.0, 30.0, 35.0])
    speed_kmh = round(speed_ms * 3.6, 1)
    correct_ans = f"{_fmt(speed_kmh)} km/h"

    prompt = (
        f"A coastal weather station in Cape Town records gale-force wind gusts of **{_fmt(speed_ms)} m/s**.\n\n"
        f"**Conversion rule**: To convert from m/s to km/h, multiply by **3,6**.\n\n"
        f"Convert this wind speed into **kilometres per hour (km/h)**."
    )

    explanation = (
        f"**Step 1: Conceptual Reasoning & Identification**\n"
        f"Multiply the speed in m/s by 3,6 to convert to kilometres per hour: "
        f"$$\\text{{Speed in km/h}} = \\text{{Speed in m/s}} \\times 3,6$$\n\n"
        f"**Step 2: Technical Method & Working Setup**\n"
        f"$$\\text{{Speed}} = {_fmt(speed_ms)} \\times 3,6$$ "
        f"✓ [1 Mark: Method – multiplying speed in m/s by 3,6]\n\n"
        f"**Step 3: Final Calculation & Answer**\n"
        f"$$\\text{{Speed}} = {correct_ans}$$ ✓ [1 Mark: Accuracy – accurate speed in km/h]"
    )

    options, _ = _build_options(correct_ans, r)
    return _build_question_payload(
        subskill_id=sub_id,
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply the speed in m/s by 3,6.",
        tier_2=f"{_fmt(speed_ms)} × 3,6 = {correct_ans}.",
        tier_3=f"Speed = {correct_ans}.",
        r=r,
    )
