"""Subskills 45 to 52: Seating Plans, Stadiums, Building Layouts & Complex Route Navigation for Grade 11 Mathematical Literacy."""
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


def generate_subskill_45(r: random.Random) -> Dict[str, Any]:
    """Subskill 45: Stadium block, row, and seat allocation & coordinate navigation."""
    stadium = r.choice(["FNB Stadium (Soccer City)", "Moses Mabhida Stadium", "DHL Stadium (Cape Town)", "Loftus Versfeld"])
    stand = r.choice(["West Stand (Grandstand)", "East Stand", "North Stand", "South Stand"])
    block = r.randint(101, 128)
    row_letter = r.choice(["A", "C", "F", "J", "M", "P"])
    seat_num = r.randint(1, 24)

    prompt = (
        f"A spectator attends a major football match at **{stadium}**.\n"
        f"Their digital match ticket displays the seating coordinates:\n\n"
        f"**{stand} | Block {block} | Row {row_letter} | Seat {seat_num}**\n\n"
        f"According to standard stadium seating plans, if Row A is closest to the field and Row Z is highest up in the upper tier, "
        f"where is this spectator seated relative to the pitch and the entrance gate?"
    )

    row_dist = "very close to the playing field" if row_letter in ["A", "C"] else "in the middle elevation of the stand" if row_letter in ["F", "J"] else "high up towards the back of the lower tier"

    correct_ans = f"In {stand}, inside Block {block}, at Row {row_letter} ({row_dist}), specifically in seat number {seat_num}."
    opt_b = f"On the opposite side of the pitch in the standing terrace."
    opt_c = f"Directly inside the players' dug-out bench on the touchline."
    opt_d = f"In the VIP hospitality suite on the roof level."

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Identify the main quadrant/stand [1 mark]: {stand}.\n"
        f"Step 2: Locate the specific section block [1 mark]: Block {block}.\n"
        f"Step 3: Interpret row depth and seat number [1 mark]: Row {row_letter} ({row_dist}), seat {seat_num}."
    )

    return _build_question_payload(
        subskill_id="subskill_45",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Read the four-tier hierarchy: Stand -> Block -> Row -> Seat.",
        tier_2=f"Stand: {stand}, Block: {block}, Row: {row_letter}, Seat: {seat_num}.",
        tier_3=f"Correct answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_46(r: random.Random) -> Dict[str, Any]:
    """Subskill 46: Stadium ticketing revenue calculation across seating tiers."""
    stadium = r.choice(["FNB Stadium", "Kings Park Stadium", "DHL Stadium"])
    
    tier1_seats = r.randint(5000, 10000)
    tier1_price = r.choice([350, 400, 450])
    
    tier2_seats = r.randint(15000, 25000)
    tier2_price = r.choice([180, 200, 220])
    
    tier3_seats = r.randint(20000, 35000)
    tier3_price = r.choice([80, 100, 120])

    prompt = (
        f"The event coordinators for a South African rugby derby at **{stadium}** structure their seating plan into three tiers:\n\n"
        f"| Seating Category | Total Available Seats | Ticket Price |\n"
        f"| :--- | :--- | :--- |\n"
        f"| Category 1 (Lower Midfield) | {_fmt(tier1_seats)} | {_fmt_curr(tier1_price)} |\n"
        f"| Category 2 (Upper Midfield & Corners) | {_fmt(tier2_seats)} | {_fmt_curr(tier2_price)} |\n"
        f"| Category 3 (Goal Ends) | {_fmt(tier3_seats)} | {_fmt_curr(tier3_price)} |\n\n"
        f"If the match sells out 100% of the **Category 1** and **Category 2** seats, but only **80%** of the **Category 3** seats, "
        f"calculate the **total ticket revenue** generated."
    )

    rev_1 = tier1_seats * tier1_price
    rev_2 = tier2_seats * tier2_price
    sold_tier3 = int(tier3_seats * 0.80)
    rev_3 = sold_tier3 * tier3_price
    total_rev = rev_1 + rev_2 + rev_3

    correct_ans = _fmt_curr(total_rev)

    # Distractor 1: 100% sellout of Category 3
    full_rev = rev_1 + rev_2 + (tier3_seats * tier3_price)
    # Distractor 2: 80% on everything
    eighty_rev = int((tier1_seats * tier1_price + tier2_seats * tier2_price + tier3_seats * tier3_price) * 0.8)

    custom_opts = [
        correct_ans,
        _fmt_curr(full_rev),
        _fmt_curr(eighty_rev),
        _fmt_curr(total_rev - rev_1),
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate revenue from Category 1 and 2 [1 mark]:\n"
        f"Cat 1: {_fmt(tier1_seats)} × {_fmt_curr(tier1_price)} = {_fmt_curr(rev_1)}.\n"
        f"Cat 2: {_fmt(tier2_seats)} × {_fmt_curr(tier2_price)} = {_fmt_curr(rev_2)}.\n\n"
        f"Step 2: Calculate Category 3 sales (80% of {_fmt(tier3_seats)} seats) [1 mark]:\n"
        f"Cat 3 seats sold: {_fmt(tier3_seats)} × 0,80 = {_fmt(sold_tier3)} seats.\n"
        f"Cat 3 revenue: {_fmt(sold_tier3)} × {_fmt_curr(tier3_price)} = {_fmt_curr(rev_3)}.\n\n"
        f"Step 3: Sum total ticketing revenue [1 mark]:\n"
        f"Total Revenue = {_fmt_curr(rev_1)} + {_fmt_curr(rev_2)} + {_fmt_curr(rev_3)} = {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_46",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Multiply seats sold by price for each tier, taking 80% of Category 3 seats.",
        tier_2=f"Cat 1: R {rev_1:,}. Cat 2: R {rev_2:,}. Cat 3: {sold_tier3} × R {tier3_price} = R {rev_3:,}.",
        tier_3=f"Total Revenue = {correct_ans}.",
        r=r,
    )


def generate_subskill_47(r: random.Random) -> Dict[str, Any]:
    """Subskill 47: Cinema / auditorium seating plan layout and wheelchair accessibility zones."""
    cinema_num = r.randint(1, 12)
    standard_rows = 14
    seats_per_row = 18
    total_standard = standard_rows * seats_per_row
    wheelchair_bays = r.choice([4, 6, 8])

    name = r.choice(SA_NAMES)

    prompt = (
        f"A cinema seating plan for Cinema {cinema_num} at Nu Metro / Ster-Kinekor consists of:\n"
        f"- **14 rows of standard seats**, with **18 seats in each row**.\n"
        f"- A dedicated flat-access row at the front containing **{wheelchair_bays} wheelchair bays** with accompanying companion seats.\n\n"
        f"What is the **maximum seating capacity** of standard cinema seats, and what percentage of the total audience capacity "
        f"is reserved for wheelchair patrons? (Round percentage to 1 decimal place)."
    )

    total_seats = total_standard + wheelchair_bays
    wheelchair_pct = round((wheelchair_bays / total_seats) * 100, 1)

    correct_ans = f"{_fmt(total_standard)} standard seats; {_fmt(wheelchair_pct)}% wheelchair bays"

    custom_opts = [
        correct_ans,
        f"{_fmt(total_seats)} standard seats; {_fmt(wheelchair_pct)}% wheelchair bays",
        f"{_fmt(total_standard)} standard seats; {_fmt(round(wheelchair_pct * 2, 1))}% wheelchair bays",
        f"{_fmt(total_standard + 20)} standard seats; 1,0% wheelchair bays",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate standard seating capacity [1 mark]:\n"
        f"Standard capacity = 14 rows × 18 seats = {_fmt(total_standard)} seats.\n\n"
        f"Step 2: Calculate total capacity including wheelchair bays [1 mark]:\n"
        f"Total capacity = {_fmt(total_standard)} + {wheelchair_bays} = {_fmt(total_seats)}.\n\n"
        f"Step 3: Calculate percentage reserved for wheelchair patrons [1 mark]:\n"
        f"Percentage = ({wheelchair_bays} ÷ {_fmt(total_seats)}) × 100 = {_fmt(wheelchair_pct)}%.\n"
        f"Final statement: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_47",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Standard capacity = rows × seats per row. Percentage = (wheelchair bays ÷ total capacity) × 100.",
        tier_2=f"Standard = 14 × 18 = {total_standard}. Total = {total_seats}. Pct = ({wheelchair_bays} ÷ {total_seats}) × 100.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: Airplane seating chart (layout, aisle vs window, exit row rules)."""
    seat_choice = r.choice(["12A", "14C", "15D", "22F"])
    
    row_num = int(seat_choice[:-1])
    seat_letter = seat_choice[-1]

    if seat_letter in ["A", "F"]:
        pos = "Window seat"
    elif seat_letter in ["C", "D"]:
        pos = "Aisle seat"
    else:
        pos = "Middle seat"

    prompt = (
        f"On a domestic flight from Johannesburg (O.R. Tambo) to Cape Town, the Boeing 737 aircraft has a **3-3 seating layout** "
        f"with seats labelled **A - B - C [Aisle] D - E - F** across rows 1 to 32.\n\n"
        f"A passenger is assigned seat **{seat_choice}**.\n\n"
        f"Identify the position of seat **{seat_choice}** (Window, Middle, or Aisle) and describe its location relative to the central aisle."
    )

    if pos == "Window seat":
        desc = f"Window seat on the {'left' if seat_letter == 'A' else 'right'} side of the aircraft cabin, next to the exterior fuselage wall."
    elif pos == "Aisle seat":
        desc = f"Aisle seat on the {'left' if seat_letter == 'C' else 'right'} side of the aircraft, offering direct, unblocked access to the central walkway."
    else:
        desc = f"Middle seat positioned between a window seat and an aisle seat."

    correct_ans = f"Row {row_num}: {pos} ({desc})"
    opt_b = f"Row {row_num}: Pilot cockpit control seat"
    opt_c = f"Row {row_num}: {'Middle seat' if pos != 'Middle seat' else 'Flight attendant jump seat'}"
    opt_d = f"Row {row_num}: Cargo hold container"

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Check row number [1 mark]: Row {row_num}.\n"
        f"Step 2: Check column seat letter in 3-3 layout [1 mark]:\n"
        f"A = Window (Left), B = Middle (Left), C = Aisle (Left).\n"
        f"D = Aisle (Right), E = Middle (Right), F = Window (Right).\n"
        f"Step 3: Conclude seating position [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_48",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="In a 3-3 configuration: A and F are window seats, B and E are middle seats, C and D are aisle seats.",
        tier_2=f"Letter is {seat_letter}. Matches {pos}.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_49(r: random.Random) -> Dict[str, Any]:
    """Subskill 49: Shopping mall multi-level floor plan directory navigation."""
    mall = r.choice(["Mall of Africa", "Gateway Theatre of Shopping", "Sandton City", "Menlyn Park"])
    start_shop = "Woolworths (Lower Level 0)"
    end_shop = "Ster-Kinekor Cinema (Upper Level 2)"

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} is at **{mall}** standing outside **{start_shop}**.\n"
        f"They need to meet a friend at **{end_shop}**.\n\n"
        f"According to the mall directory floor plans:\n"
        f"- To travel from Level 0 to Level 1, they must take the Central Atrium Escalator.\n"
        f"- On Level 1, they must walk 120 m East towards the Food Court.\n"
        f"- Next to the Food Court, they must take the North Escalator up to Level 2.\n\n"
        f"Which concise set of navigation instructions accurately guides {name} from the current position to the destination?"
    )

    correct_ans = (
        f"Take Central Escalator up to Level 1 -> walk 120 m East to Food Court -> take North Escalator up to Level 2 cinema entrance."
    )
    opt_b = f"Take lift down to the basement parking -> exit through the loading dock."
    opt_c = f"Stay on Level 0 and walk West towards the supermarket."
    opt_d = f"Take the external fire escape stairs down to the ring road."

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Ascend from Level 0 to Level 1 via the Central Atrium Escalator [1 mark].\n"
        f"Step 2: Traverse Level 1 walking 120 m East to the Food Court [1 mark].\n"
        f"Step 3: Ascend from Level 1 to Level 2 using the North Escalator to reach the cinema [1 mark]."
    )

    return _build_question_payload(
        subskill_id="subskill_49",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Trace the sequential steps across the floor levels from Level 0 to Level 1, then Level 1 to Level 2.",
        tier_2="Check escalator transitions and walking direction.",
        tier_3=f"Correct path: {correct_ans}.",
        r=r,
    )


def generate_subskill_50(r: random.Random) -> Dict[str, Any]:
    """Subskill 50: Building emergency evacuation route analysis."""
    office_room = f"Room {r.randint(301, 315)} (3rd Floor)"
    fire_exit_a_dist = r.choice([25, 30, 35])  # metres to Fire Stairs East
    fire_exit_b_dist = r.choice([65, 75, 80])  # metres to Fire Stairs West
    
    name = r.choice(SA_NAMES)

    prompt = (
        f"A fire evacuation plan mounted on the wall of **{office_room}** in a high-rise office park indicates:\n"
        f"- **Fire Exit Stairs East**: Turn left in the corridor, walk **{fire_exit_a_dist} m**.\n"
        f"- **Fire Exit Stairs West**: Turn right in the corridor, walk **{fire_exit_b_dist} m**.\n"
        f"- **Passenger Elevators / Lifts**: Located directly opposite ({r.randint(5, 10)} m away).\n"
        f"- **Assembly Point**: Parking Lot B.\n\n"
        f"In the event of a fire alarm, which evacuation procedure MUST {name} strictly follow according to workplace health & safety regulations?"
    )

    correct_ans = (
        f"Turn left and evacuate immediately via Fire Exit Stairs East ({fire_exit_a_dist} m away) to Assembly Point B; NEVER use the elevators/lifts."
    )
    opt_b = f"Use the passenger elevators immediately because they are only 5-10 m away and faster."
    opt_c = f"Turn right and walk {fire_exit_b_dist} m to the furthest exit while ignoring the closer exit."
    opt_d = f"Stay in the room and lock the door until the meeting is finished."

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Identify the primary rule of fire evacuation in multi-storey buildings [1 mark]: NEVER use elevators during a fire due to risk of power failure or shaft chimney effects.\n"
        f"Step 2: Compare distances to emergency stairwells [1 mark]: Stairs East is only {fire_exit_a_dist} m away (closer than Stairs West at {fire_exit_b_dist} m).\n"
        f"Step 3: Stated evacuation route [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_50",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Always select the nearest fire exit stairwell. Never use elevators during a fire evacuation.",
        tier_2=f"Stairs East is closer ({fire_exit_a_dist} m vs {fire_exit_b_dist} m) and elevators are forbidden.",
        tier_3=f"Procedure: {correct_ans}.",
        r=r,
    )


def generate_subskill_51(r: random.Random) -> Dict[str, Any]:
    """Subskill 51: Wheelchair ramp accessibility slope compliance vs stair access (SANS 10400)."""
    # SANS 10400: Maximum gradient for wheelchair ramp is 1:12 (approx 8.33% slope)
    step_height_cm = r.choice([60, 75, 90, 100])  # total vertical rise in cm
    rise_m = step_height_cm / 100
    
    # Required minimum ramp run for 1:12 slope: Run = Rise * 12
    req_run_m = round(rise_m * 12, 2)
    
    actual_run_m = r.choice([req_run_m, round(req_run_m - 2.0, 2), round(req_run_m + 3.0, 2)])
    compliant = actual_run_m >= req_run_m

    building = r.choice(["Community Clinic", "High School Entrance", "Public Library", "Municipal Offices"])

    prompt = (
        f"Under South African National Standard **SANS 10400-S (Accessibility)**, any pedestrian wheelchair ramp "
        f"must have a maximum gradient of **1 : 12** (for every 1 m of vertical rise, there must be at least 12 m of horizontal run).\n\n"
        f"A new {building} has an entrance landing with a vertical height (rise) of **{_fmt(step_height_cm)} cm** ({_fmt(rise_m)} m) above ground level.\n"
        f"The architect's blueprint specifies a ramp horizontal length (run) of **{_fmt(actual_run_m)} m**.\n\n"
        f"Calculate the **minimum required ramp run** for SANS compliance, and determine whether the proposed design meets the national building regulation."
    )

    if compliant:
        correct_ans = f"Required minimum run = {_fmt(req_run_m)} m; Design is COMPLIANT ({_fmt(actual_run_m)} m ≥ {_fmt(req_run_m)} m)."
        opt_b = f"Required minimum run = {_fmt(req_run_m)} m; Design is NON-COMPLIANT."
        opt_c = f"Required minimum run = {_fmt(req_run_m * 2)} m; Design is NON-COMPLIANT."
        opt_d = f"Required minimum run = {_fmt(round(req_run_m / 2, 2))} m; Design is COMPLIANT."
    else:
        correct_ans = f"Required minimum run = {_fmt(req_run_m)} m; Design is NON-COMPLIANT ({_fmt(actual_run_m)} m < {_fmt(req_run_m)} m; ramp is too steep)."
        opt_b = f"Required minimum run = {_fmt(req_run_m)} m; Design is COMPLIANT."
        opt_c = f"Required minimum run = {_fmt(round(req_run_m / 2, 2))} m; Design is COMPLIANT."
        opt_d = f"Required minimum run = {_fmt(req_run_m * 2)} m; Design is NON-COMPLIANT."

    options, _ = _build_options(correct_ans, r, custom_options=[correct_ans, opt_b, opt_c, opt_d])

    explanation = (
        f"Step 1: Express vertical rise in metres [1 mark]:\n"
        f"Rise = {_fmt(step_height_cm)} cm ÷ 100 = {_fmt(rise_m)} m.\n\n"
        f"Step 2: Calculate minimum horizontal run using 1 : 12 ratio [1 mark]:\n"
        f"Minimum Run = {_fmt(rise_m)} m × 12 = {_fmt(req_run_m)} m.\n\n"
        f"Step 3: Compare proposed run ({_fmt(actual_run_m)} m) to requirement [1 mark]:\n"
        f"{'Since ' + _fmt(actual_run_m) + ' m ≥ ' + _fmt(req_run_m) + ' m, the ramp is COMPLIANT.' if compliant else 'Since ' + _fmt(actual_run_m) + ' m < ' + _fmt(req_run_m) + ' m, the ramp is TOO STEEP and NON-COMPLIANT.'}"
    )

    return _build_question_payload(
        subskill_id="subskill_51",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Convert rise to metres, multiply by 12 to find minimum horizontal run, then compare with proposed run.",
        tier_2=f"Rise = {rise_m} m. Minimum run = {rise_m} × 12 = {req_run_m} m. Proposed = {actual_run_m} m.",
        tier_3=f"Answer: {correct_ans}.",
        r=r,
    )


def generate_subskill_52(r: random.Random) -> Dict[str, Any]:
    """Subskill 52: Multi-modal transport route & itinerary evaluation."""
    route_name = "Centurion to Rosebank"
    
    # Option A: Gautrain
    train_fare = r.choice([64.0, 72.0, 80.0])
    train_time = 22  # minutes
    walk_time = 8   # minutes
    total_time_a = train_time + walk_time
    total_cost_a = train_fare

    # Option B: Private car / e-hailing
    car_time = r.choice([45, 55, 60])  # minutes in peak traffic
    car_fuel = r.choice([48.0, 55.0, 62.0])
    car_toll = 18.50
    total_cost_b = car_fuel + car_toll
    total_time_b = car_time

    name = r.choice(SA_NAMES)

    prompt = (
        f"{name} commutes from Centurion to Rosebank for work during peak morning traffic.\n"
        f"They evaluate two travel options:\n\n"
        f"**Option 1: Gautrain Rapid Rail + Walking**\n"
        f"- Train ride time: {train_time} minutes | Walking to office: {walk_time} minutes.\n"
        f"- Gautrain single smart card fare: {_fmt_curr(total_cost_a)}.\n\n"
        f"**Option 2: Private Car on N1/M1 Highway**\n"
        f"- Driving time in peak traffic: {car_time} minutes.\n"
        f"- Estimated petrol cost: {_fmt_curr(car_fuel)} | E-toll cost: {_fmt_curr(car_toll)}.\n\n"
        f"Calculate the **time saved (in minutes)** and the **financial cost difference** if {name} chooses Option 1 instead of Option 2."
    )

    time_saved = total_time_b - total_time_a
    cost_diff = abs(total_cost_b - total_cost_a)
    cheaper_opt = "Option 1 is cheaper" if total_cost_a < total_cost_b else "Option 2 is cheaper"

    correct_ans = f"Saves {time_saved} minutes; {cheaper_opt} by {_fmt_curr(cost_diff)}"

    custom_opts = [
        correct_ans,
        f"Saves {time_saved + 10} minutes; {cheaper_opt} by {_fmt_curr(cost_diff)}",
        f"Saves {time_saved} minutes; {'Option 2 is cheaper' if total_cost_a < total_cost_b else 'Option 1 is cheaper'} by {_fmt_curr(cost_diff)}",
        f"Takes {time_saved} minutes longer; {_fmt_curr(cost_diff)} difference",
    ]
    options, _ = _build_options(correct_ans, r, custom_options=custom_opts)

    explanation = (
        f"Step 1: Calculate total travel time for each option [1 mark]:\n"
        f"- Option 1: {train_time} min + {walk_time} min = {total_time_a} minutes.\n"
        f"- Option 2: {total_time_b} minutes.\n"
        f"Time saved with Option 1: {total_time_b} min - {total_time_a} min = {time_saved} minutes.\n\n"
        f"Step 2: Calculate total cost for each option [1 mark]:\n"
        f"- Option 1: {_fmt_curr(total_cost_a)}.\n"
        f"- Option 2: {_fmt_curr(car_fuel)} + {_fmt_curr(car_toll)} = {_fmt_curr(total_cost_b)}.\n"
        f"Cost difference: |{_fmt_curr(total_cost_b)} - {_fmt_curr(total_cost_a)}| = {_fmt_curr(cost_diff)}.\n\n"
        f"Step 3: Stated evaluation [1 mark]: {correct_ans}."
    )

    return _build_question_payload(
        subskill_id="subskill_52",
        prompt=prompt,
        correct_ans=correct_ans,
        options=options,
        explanation=explanation,
        tier_1="Calculate total time and cost for both options, then subtract to find the differences.",
        tier_2=f"Time: {total_time_b} - {total_time_a} = {time_saved} min. Cost: Option 1 = R {total_cost_a:.2f}, Option 2 = R {total_cost_b:.2f}.",
        tier_3=f"Result: {correct_ans}.",
        r=r,
    )
