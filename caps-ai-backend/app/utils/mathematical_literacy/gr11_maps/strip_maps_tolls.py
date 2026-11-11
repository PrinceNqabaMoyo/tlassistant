"""Subskills 28 to 36: Distance Tables, Strip Maps, Toll Plazas & Route Analysis for Grade 11 Mathematical Literacy."""
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
    """Subskill 28: Distance table matrix lookup between major South African cities."""
    # Distance table sample
    # JHB, DBN, CPT, PE
    matrix = {
        ("Johannesburg", "Durban"): 568,
        ("Johannesburg", "Cape Town"): 1398,
        ("Johannesburg", "Gqeberha (PE)"): 1047,
        ("Durban", "Cape Town"): 1635,
        ("Durban", "Gqeberha (PE)"): 910,
        ("Cape Town", "Gqeberha (PE)"): 750,
    }
    pair, dist = r.choice(list(matrix.items()))
    c1, c2 = pair

    prompt = (
        f"A standard South African road distance chart lists distances between major cities in kilometres:\n\n"
        f"| City | Johannesburg | Durban | Cape Town | Gqeberha (PE) |\n"
        f"| :--- | :--- | :--- | :--- | :--- |\n"
        f"| Johannesburg | — | 568 km | 1 398 km | 1 047 km |\n"
        f"| Durban | 568 km | — | 1 635 km | 910 km |\n"
        f"| Cape Town | 1 398 km | 1 635 km | — | 750 km |\n"
        f"| Gqeberha (PE) | 1 047 km | 910 km | 750 km | — |\n\n"
        f"According to the distance table, what is the direct road distance between **{c1}** and **{c2}**?"
    )

    correct_ans = f"{_fmt(dist)} km"
    options, _ = _build_options(correct_ans, r, custom_options=[f"{_fmt(v)} km" for v in [dist, 568, 1398, 910, 750] if v != dist][:3] + [correct_ans])

    explanation = (
        f"Step 1: Locate {c1} on the row header [1 mark].\n"
        f"Step 2: Trace across to the column for {c2} [1 mark].\n"
        f"The intersection shows {_fmt(dist)} km.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="28",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Find the row for the first city and trace across to the column for the second city.",
        tier_2=f"The intersection of {c1} and {c2} gives the distance.",
        tier_3=f"Distance = {_fmt(dist)} km.",
        r=r,
    )


def generate_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Subskill 29: Multi-leg road trip calculation from distance table."""
    name = r.choice(SA_NAMES)
    c1 = "Johannesburg"
    c2 = "Durban"
    c3 = "Gqeberha (PE)"

    d1 = 568  # JHB to DBN
    d2 = 910  # DBN to PE
    total_d = d1 + d2

    prompt = (
        f"{name} is planning a multi-leg business trip by road starting in {c1}, "
        f"travelling to {c2} ({_fmt(d1)} km), and then proceeding from {c2} to {c3} ({_fmt(d2)} km).\n"
        f"Calculate the total distance in kilometres for this two-leg journey."
    )

    correct_ans = f"{_fmt(total_d)} km"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Identify distances for both legs [1 mark].\n"
        f"Leg 1 ({c1} to {c2}) = {_fmt(d1)} km; Leg 2 ({c2} to {c3}) = {_fmt(d2)} km.\n"
        f"Step 2: Sum the distances [1 mark].\n"
        f"Total Distance = {_fmt(d1)} km + {_fmt(d2)} km = {_fmt(total_d)} km.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="29",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the distance of Leg 1 to the distance of Leg 2.",
        tier_2=f"{_fmt(d1)} km + {_fmt(d2)} km = {_fmt(total_d)} km.",
        tier_3=f"Total distance = {_fmt(total_d)} km.",
        r=r,
    )


def generate_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Subskill 30: Reading intermediate town distances on a strip map."""
    route = "N1 North"
    t1 = "Pretoria"
    t2 = "Bela-Bela"
    t3 = "Mokopane"
    t4 = "Polokwane"

    d12 = 105
    d23 = 100
    d34 = 55
    total = d12 + d23 + d34  # 260 km

    prompt = (
        f"A strip map for the {route} indicates the following distances between consecutive towns:\n"
        f"• {t1} to {t2}: {_fmt(d12)} km\n"
        f"• {t2} to {t3}: {_fmt(d23)} km\n"
        f"• {t3} to {t4}: {_fmt(d34)} km\n\n"
        f"What is the total road distance between {t1} and {t4} along this route?"
    )

    correct_ans = f"{_fmt(total)} km"
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Sum the intermediate consecutive segment distances [1 mark].\n"
        f"Total = {_fmt(d12)} + {_fmt(d23)} + {_fmt(d34)} [1 mark].\n"
        f"Step 2: Add values [1 mark].\n"
        f"Total = {_fmt(total)} km.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="30",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add the distances between each of the intermediate towns along the strip map.",
        tier_2=f"{d12} + {d23} + {d34} = {total} km.",
        tier_3=f"Total distance = {_fmt(total)} km.",
        r=r,
    )


def generate_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Subskill 31: Cumulative strip map distance calculation between non-adjacent towns."""
    t1 = "Bloemfontein"
    t2 = "Colesberg"
    t3 = "Beaufort West"
    t4 = "Cape Town"

    # Cumulative milestones from Bloemfontein:
    # Colesberg = 220 km, Beaufort West = 540 km, Cape Town = 1000 km
    m_colesberg = 220
    m_beaufort = 540
    m_cpt = 1000

    # Distance between Colesberg and Beaufort West = 540 - 220 = 320 km
    dist_between = m_beaufort - m_colesberg

    prompt = (
        f"A highway strip map displays cumulative milestone distances along the N1 route measured from {t1} (0 km):\n"
        f"• {t1}: 0 km\n"
        f"• {t2}: {_fmt(m_colesberg)} km\n"
        f"• {t3}: {_fmt(m_beaufort)} km\n"
        f"• {t4}: {_fmt(m_cpt)} km\n\n"
        f"Using these cumulative milestones, calculate the direct road distance between **{t2}** and **{t3}**."
    )

    correct_ans = f"{_fmt(dist_between)} km"
    wrong_1 = f"{_fmt(m_beaufort)} km"
    wrong_2 = f"{_fmt(m_beaufort + m_colesberg)} km"
    wrong_3 = f"{_fmt(dist_between - 40)} km"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Identify the cumulative milestones for both towns [1 mark].\n"
        f"Milestone at {t3} = {_fmt(m_beaufort)} km; Milestone at {t2} = {_fmt(m_colesberg)} km.\n"
        f"Step 2: Subtract the smaller milestone from the larger [1 mark].\n"
        f"Distance = {_fmt(m_beaufort)} km - {_fmt(m_colesberg)} km = {_fmt(dist_between)} km.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="31",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Subtract the cumulative distance of the first town from the cumulative distance of the second town.",
        tier_2=f"{_fmt(m_beaufort)} km - {_fmt(m_colesberg)} km = {_fmt(dist_between)} km.",
        tier_3=f"Distance = {_fmt(dist_between)} km.",
        r=r,
    )


def generate_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Subskill 32: National route corridor identification."""
    route_data = r.choice([
        ("N1", "Connects Cape Town to Zimbabwe via Bloemfontein, Johannesburg, and Pretoria"),
        ("N2", "Coastal national route connecting Cape Town, Port Elizabeth, East London, and Durban"),
        ("N3", "Crucial freight corridor connecting Johannesburg directly to the Port of Durban"),
        ("N4", "Trans-Kalahari / Maputo corridor connecting Botswana through Rustenburg and Pretoria to Mozambique"),
    ])
    route_num, route_desc = route_data

    prompt = (
        f"Which major South African national route is described below?\n"
        f"\"{route_desc}\""
    )

    correct_ans = route_num
    custom_opts = ["N1", "N2", "N3", "N4"]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Analyze the key transit cities and termini [1 mark].\n"
        f"The route described is: \"{route_desc}\".\n"
        f"Step 2: Match to official SANRAL national route numbering [1 mark].\n"
        f"This corresponds to the {route_num}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="32",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Review South African national highway corridors (N1, N2, N3, N4).",
        tier_2=f"{route_desc} describes the {route_num}.",
        tier_3=f"Answer: {route_num}.",
        r=r,
    )


def generate_subskill_33(r: random.Random) -> Dict[str, Any]:
    """Subskill 33: Toll plaza tariff summation along a national route."""
    name = r.choice(SA_NAMES)
    plazas = [
        ("De Hoek Toll Plaza", 60.50),
        ("Wilge Toll Plaza", 83.00),
        ("Tugela Toll Plaza", 88.50),
        ("Mooi River Toll Plaza", 62.00),
    ]

    total_tolls = round(sum(p[1] for p in plazas), 2)
    plazas_text = "\n".join([f"• {p[0]}: {_fmt_curr(p[1])}" for p in plazas])

    prompt = (
        f"{name} drives a standard passenger car (Class 1 light vehicle) from Johannesburg to Durban along the N3. "
        f"The toll plazas and applicable Class 1 tariffs are listed below:\n"
        f"{plazas_text}\n\n"
        f"Calculate the total toll fees in Rands that {name} will pay for a ONE-WAY trip."
    )

    correct_ans = _fmt_curr(total_tolls)
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Sum the tariffs for all toll plazas [1 mark].\n"
        f"Total = {' + '.join(_fmt_curr(p[1]) for p in plazas)} [1 mark].\n"
        f"Step 2: Calculate sum [1 mark].\n"
        f"Total Tolls = {_fmt_curr(total_tolls)}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="33",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Add up the fees of all toll plazas passed along the route.",
        tier_2=f"Sum: {' + '.join(_fmt_curr(p[1]) for p in plazas)}.",
        tier_3=f"Total tolls = {_fmt_curr(total_tolls)}.",
        r=r,
    )


def generate_subskill_34(r: random.Random) -> Dict[str, Any]:
    """Subskill 34: Toll plaza vehicle class classification under SANRAL rules."""
    vehicle_info = r.choice([
        ("Standard passenger sedan car (with no trailer)", "Class 1 (Light vehicle, length < 5,0 m, 2 axles)"),
        ("Heavy 2-axle delivery truck", "Class 2 (Medium heavy vehicle with 2 axles)"),
        ("Large 3-axle bus or long-haul freight vehicle", "Class 3 (Large heavy vehicle with 3 or 4 axles)"),
        ("Multi-axle articulated freight superlink truck (5 or more axles)", "Class 4 (Heavy vehicle with 5 or more axles)"),
    ])
    veh_desc, veh_class = vehicle_info

    prompt = (
        f"Under South African National Roads Agency (SANRAL) toll classifications, which toll vehicle class "
        f"applies to a: **{veh_desc}**?"
    )

    correct_ans = veh_class
    all_classes = [
        "Class 1 (Light vehicle, length < 5,0 m, 2 axles)",
        "Class 2 (Medium heavy vehicle with 2 axles)",
        "Class 3 (Large heavy vehicle with 3 or 4 axles)",
        "Class 4 (Heavy vehicle with 5 or more axles)",
    ]
    distractors = [c for c in all_classes if c != veh_class][:3]
    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans] + distractors)

    explanation = (
        f"Step 1: Check axle count and vehicle type [1 mark].\n"
        f"Vehicle: {veh_desc}.\n"
        f"Step 2: Match to SANRAL definitions [1 mark].\n"
        f"This vehicle falls under {veh_class}.\n"
        f"Step 3: Stated answer [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="34",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Class 1 = light passenger cars; Class 2 = 2-axle trucks; Class 3 = 3/4-axle; Class 4 = 5+ axles.",
        tier_2=f"{veh_desc} corresponds to {veh_class}.",
        tier_3=f"Classification: {veh_class}.",
        r=r,
    )


def generate_subskill_35(r: random.Random) -> Dict[str, Any]:
    """Subskill 35: Alternative route comparison: toll highway vs non-toll provincial road."""
    name = r.choice(SA_NAMES)
    toll_fee = 294.00
    fuel_price = 24.00
    car_rate = 8.0  # L/100 km

    # Route A (Toll Highway): 560 km + R 294 tolls
    dist_a = 560
    litres_a = (dist_a / 100) * car_rate  # 44.8 L
    fuel_a = litres_a * fuel_price  # R 1 075,20
    total_a = round(fuel_a + toll_fee, 2)  # R 1 369,20

    # Route B (Non-toll Alternative): 680 km, zero tolls
    dist_b = 680
    litres_b = (dist_b / 100) * car_rate  # 54.4 L
    fuel_b = round(litres_b * fuel_price, 2)  # R 1 305,60
    total_b = fuel_b

    diff = round(abs(total_a - total_b), 2)
    cheaper = "Route B (Non-toll road)" if total_b < total_a else "Route A (Toll highway)"

    prompt = (
        f"{name} is comparing two driving routes from City X to City Y for a car consuming 8,0 L/100 km (petrol = R 24,00/L):\n"
        f"• Route A (Toll Highway): Distance = 560 km; Total toll fees = R 294,00\n"
        f"• Route B (Alternative non-toll road): Distance = 680 km; Total toll fees = R 0,00\n"
        f"Which route is cheaper in terms of combined fuel and toll costs, and by how much?"
    )

    correct_ans = f"{cheaper} is cheaper by {_fmt_curr(diff)}"
    other = "Route A (Toll highway)" if cheaper == "Route B (Non-toll road)" else "Route B (Non-toll road)"
    wrong_1 = f"{other} is cheaper by {_fmt_curr(diff)}"
    wrong_2 = f"{cheaper} is cheaper by {_fmt_curr(diff + 100.0)}"
    wrong_3 = f"Both routes cost the exact same amount"
    custom_opts = [correct_ans, wrong_1, wrong_2, wrong_3]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate total cost for Route A [1 mark].\n"
        f"Fuel A = (560 ÷ 100) × 8,0 L × R 24,00 = 44,8 L × R 24,00 = {_fmt_curr(fuel_a)}.\n"
        f"Total A = Fuel + Tolls = {_fmt_curr(fuel_a)} + {_fmt_curr(toll_fee)} = {_fmt_curr(total_a)}.\n"
        f"Step 2: Calculate total cost for Route B [1 mark].\n"
        f"Fuel B = (680 ÷ 100) × 8,0 L × R 24,00 = 54,4 L × R 24,00 = {_fmt_curr(fuel_b)} (no tolls).\n"
        f"Step 3: Compare costs and difference [1 mark].\n"
        f"Difference = |{_fmt_curr(total_a)} - {_fmt_curr(total_b)}| = {_fmt_curr(diff)}.\n"
        f"Conclusion: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="35",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate the combined fuel and toll cost for each route and compare the totals.",
        tier_2=f"Route A = {_fmt_curr(total_a)}; Route B = {_fmt_curr(total_b)}.",
        tier_3=f"Difference = {_fmt_curr(diff)}. {cheaper} is cheaper.",
        r=r,
    )


def generate_subskill_36(r: random.Random) -> Dict[str, Any]:
    """Subskill 36: Round-trip total logistics cost: fuel, tolls, and accommodation."""
    name = r.choice(SA_NAMES)
    dist_oneway = r.choice([450, 500, 600])
    total_dist = dist_oneway * 2  # round-trip

    fuel_rate = 7.5
    petrol_price = 24.00
    fuel_cost = round((total_dist / 100) * fuel_rate * petrol_price, 2)

    toll_oneway = 145.00
    toll_total = toll_oneway * 2  # return tolls

    hotel_nights = 2
    hotel_rate = 850.00
    hotel_total = hotel_nights * hotel_rate

    grand_total = round(fuel_cost + toll_total + hotel_total, 2)

    prompt = (
        f"{name} plans a business trip requiring a return journey of {_fmt(total_dist)} km in total. "
        f"The car uses 7,5 L/100 km of petrol at R 24,00 per litre. "
        f"Return toll fees total {_fmt_curr(toll_total)}, and {name} stays for 2 nights at a guesthouse costing "
        f"{_fmt_curr(hotel_rate)} per night.\n"
        f"Calculate the total combined trip budget (fuel + tolls + accommodation) in Rands."
    )

    correct_ans = _fmt_curr(grand_total)
    options, _ = _build_options(correct_ans, r)

    explanation = (
        f"Step 1: Calculate fuel cost for {_fmt(total_dist)} km [1 mark].\n"
        f"Fuel = ({total_dist} ÷ 100) × 7,5 L × R 24,00 = {_fmt_curr(fuel_cost)}.\n"
        f"Step 2: Calculate tolls and accommodation [1 mark].\n"
        f"Tolls = {_fmt_curr(toll_total)}; Hotel = 2 × {_fmt_curr(hotel_rate)} = {_fmt_curr(hotel_total)}.\n"
        f"Step 3: Sum all expenses [1 mark].\n"
        f"Grand Total = {_fmt_curr(fuel_cost)} + {_fmt_curr(toll_total)} + {_fmt_curr(hotel_total)} = {_fmt_curr(grand_total)} ({correct_ans})."
    )

    return _build_question_payload(
        subskill_id="36",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate fuel cost, then add return tolls and accommodation costs.",
        tier_2=f"Fuel = {_fmt_curr(fuel_cost)}, Tolls = {_fmt_curr(toll_total)}, Hotel = {_fmt_curr(hotel_total)}.",
        tier_3=f"Total = {_fmt_curr(grand_total)}.",
        r=r,
    )
