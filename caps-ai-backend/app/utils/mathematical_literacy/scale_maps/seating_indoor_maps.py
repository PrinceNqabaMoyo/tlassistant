"""Cluster 6: Seating Plans & Indoor Layout Maps (Subskills 45 to 52).

Covers:
45. Cinema & theatre seating plans: row letter and seat number coordinate grids
46. Sports stadium seating plans: stands (North/South/East/West), gates, and ticket tiers
47. School classroom & exam hall seating grid layout and desk spacing
48. Commercial aeroplane passenger cabin seating (Window, Middle, and Aisle seats)
49. Event banquet hall seating: round table capacity and floor clearance
50. Shopping mall indoor directory floor plans & retail shop navigation
51. Emergency fire evacuation route planning (shortest exit path and stairs rule)
52. Universal accessibility & wheelchair ramp routes on public building maps
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _build_question_payload,
)


def _gen_map_seat_cinema_theatre_grid_row_seat_number(r: random.Random) -> Dict[str, Any]:
    rows = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K"]
    seats_per_row = r.choice([16, 18, 20])
    row_count = len(rows)
    total_seats = row_count * seats_per_row

    chosen_row = r.choice(["D", "E", "F", "G"])
    chosen_seat = r.randint(4, seats_per_row - 2)

    prompt = (
        f"Study the seating plan diagram below for a community theatre:\n\n"
        f"• The auditorium has {row_count} rows labelled from Row A (front row) to Row K (back row).\n"
        f"• Each row contains exactly {seats_per_row} seats numbered consecutively from Seat 1 on the left to Seat {seats_per_row} on the right.\n\n"
        f"1. What is the total seating capacity of the auditorium?\n"
        f"2. A patron's ticket reads: **Row {chosen_row}, Seat {chosen_seat}**. How many seats are to the right of this patron in the same row?"
    )
    seats_to_right = seats_per_row - chosen_seat
    ans = f"Capacity = {total_seats} seats; {seats_to_right} seats to the right"

    s1 = f"Multiply number of rows ({row_count}) by seats per row ({seats_per_row}) = {total_seats}. Subtract patron's seat number ({chosen_seat}) from row total ({seats_per_row}) to find seats to the right: {seats_per_row} − {chosen_seat} = {seats_to_right}."
    s2 = f"✓ [1 Mark: Method – Capacity multiplication and row subtraction]\nTotal capacity = {row_count} rows × {seats_per_row} seats = {total_seats}.\nSeats to right = {seats_per_row} − {chosen_seat} = {seats_to_right}."
    s3 = f"✓ [1 Mark: Accuracy – Total capacity and seats to the right]\n{ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "seating_plan",
        "title": "Auditorium Seating Plan",
        "rows": rows[:5],
        "seats_per_row": seats_per_row,
        "target_seat": f"Row {chosen_row}, Seat {chosen_seat}",
    }

    return _build_question_payload(
        "map_seat_cinema_theatre_grid_row_seat_number",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Total capacity = {row_count} × {seats_per_row}.",
        tier_2_hint=f"Subtract seat {chosen_seat} from total row width {seats_per_row}.",
        tier_3_hint=f"{ans}.",
        diagram_spec=diagram_spec,
    )


def _gen_map_seat_stadium_stands_turnstiles_gate(r: random.Random) -> Dict[str, Any]:
    stand = r.choice(["North Stand (behind goalposts)", "South Stand", "East Stand (Grandstand)", "West Stand"])
    block = r.randint(101, 125)
    gate = r.choice(["Gate 4", "Gate 7", "Gate 12", "Gate 15"])

    prompt = (
        f"Refer to the stadium perimeter gate and seating plan map below.\n\n"
        f"A soccer spectator holds an admission ticket for an international match at FNB Stadium:\n"
        f"**[ Admission: Gate {gate} | Stand: {stand} | Block: {block} | Seat: 42 ]**\n\n"
        f"According to the stadium perimeter map, why must the spectator enter strictly through **{gate}**?"
    )
    ans = f"Gate {gate} is the designated perimeter turnstile providing direct, unblocked access to {stand} Block {block}, preventing overcrowding and security bottlenecks in other stadium quadrants."
    opts = [
        f"Gate {gate} is the designated perimeter turnstile providing direct, unblocked access to {stand} Block {block}, preventing overcrowding and security bottlenecks in other stadium quadrants.",
        "Spectators can enter through any gate if they arrive before kickoff.",
        "Gate numbers correspond to the spectator's home street address.",
        "Tickets are only scanned at gates that sell cold drinks.",
    ]

    s1 = f"Understand crowd control logistics and zonal ingress routing in large sporting venues."
    s2 = f"✓ [1 Mark: Method – Explaining perimeter turnstile routing and crowd safety]\nDesignated gates guide patrons directly to their assigned block, minimizing pedestrian congestion around the outer concourse."
    s3 = f"✓ [1 Mark: Accuracy – Correct crowd management rationale]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": "FNB Stadium Perimeter Turnstile Map",
        "rooms": [stand, "North Stand", "South Stand", "Concourse", f"Entrance {gate}"],
        "scale": f"Turnstile {gate}",
    }

    return _build_question_payload(
        "map_seat_stadium_stands_turnstiles_gate",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Why do large stadiums have multiple lettered/numbered gates around the outside?",
        tier_2_hint="Specific gates provide direct access to specific stands to manage crowd flow and safety.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_seat_classroom_exam_hall_spacing(r: random.Random) -> Dict[str, Any]:
    rows = r.choice([5, 6, 7, 8])
    desks_per_row = r.choice([4, 5, 6])
    total_desks = rows * desks_per_row
    spacing_m = 1.2

    prompt = (
        f"Refer to the examination hall seating plan layout diagram below.\n\n"
        f"• The hall has {rows} rows of single examination desks.\n"
        f"• Each row contains {desks_per_row} individual desks.\n"
        f"• All desks are spaced exactly {_fmt(spacing_m)} m apart from each other in all directions.\n\n"
        f"1. Calculate the total number of candidates that can write an examination simultaneously in this hall.\n"
        f"2. Why do examination regulations mandate a minimum spacing of {_fmt(spacing_m)} m between desks?"
    )
    ans = f"{total_desks} candidates — To prevent candidates from reading each other's answer scripts and to allow invigilators to walk freely between rows"
    opts = [
        f"{total_desks} candidates — To prevent candidates from reading each other's answer scripts and to allow invigilators to walk freely between rows",
        f"{total_desks + 10} candidates — Extra desks are kept for invigilators to sit at.",
        f"{total_desks} candidates — Desks must be spaced apart to prevent sound echoing.",
        f"{total_desks - 5} candidates — Five desks are always reserved for latecomers.",
    ]

    s1 = f"Multiply rows ({rows}) by desks per row ({desks_per_row}) = {total_desks}. Explain exam integrity spacing and invigilator circulation."
    s2 = f"✓ [1 Mark: Method – Grid desk multiplication and exam integrity rationale]\nTotal = {rows} × {desks_per_row} = {total_desks}.\nSpacing prevents copying and provides inspection aisles."
    s3 = f"✓ [1 Mark: Accuracy – Total candidate capacity and regulation rationale]\n{ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Examination Hall Grid Layout ({total_desks} Desks)",
        "rooms": [f"Row {i + 1} ({desks_per_row} Desks)" for i in range(min(rows, 5))],
        "scale": f"{_fmt(spacing_m)} m Spacing",
    }

    return _build_question_payload(
        "map_seat_classroom_exam_hall_spacing",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Multiply {rows} rows by {desks_per_row} desks.",
        tier_2_hint=f"Total capacity = {rows} × {desks_per_row} = {total_desks}.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_seat_aeroplane_cabin_window_aisle(r: random.Random) -> Dict[str, Any]:
    row_num = r.randint(10, 28)
    seat_letter = r.choice(["A", "B", "C", "D", "E", "F"])

    if seat_letter in ["A", "F"]:
        seat_type = "Window seat"
        explanation = "Seats A (port/left) and F (starboard/right) are situated directly against the outer cabin fuselage with a window."
    elif seat_letter in ["C", "D"]:
        seat_type = "Aisle seat"
        explanation = "Seats C and D flank the central passenger walking aisle, offering direct access without disturbing other passengers."
    else:
        seat_type = "Middle seat"
        explanation = "Seats B and E are positioned in the middle between the window passenger and aisle passenger."

    prompt = (
        f"Refer to the aircraft passenger cabin seating plan below for a Boeing 737 with a standard 3–3 layout:\n\n"
        f"**[ Window | Seat A | Seat B | Seat C | AISLE | Seat D | Seat E | Seat F | Window ]**\n\n"
        f"A passenger is assigned seat **'{row_num}{seat_letter}'**.\n\n"
        f"Identify whether this is a **Window seat, Middle seat, or Aisle seat**, and describe its position in the cabin."
    )
    ans = f"{seat_type} — {explanation}"
    opts = [
        f"{seat_type} — {explanation}",
        "Cockpit jump seat — Reserved for trainee pilots only.",
        "Cargo hold seat — Situating the passenger under the cabin floor.",
        "Emergency exit row with no seating.",
    ]

    s1 = f"Identify standard commercial aircraft seating layout: A/F = Window, B/E = Middle, C/D = Aisle."
    s2 = f"✓ [1 Mark: Method – Identifying letter position relative to cabin layout]\nSeat letter {seat_letter} corresponds to {seat_type}."
    s3 = f"✓ [1 Mark: Accuracy – Correct seat classification and cabin position]\n{ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "seating_plan",
        "title": "Boeing 737 Passenger Cabin Layout",
        "rows": [f"Row {row_num}"],
        "seats_per_row": 6,
        "target_seat": f"Seat {row_num}{seat_letter}",
    }

    return _build_question_payload(
        "map_seat_aeroplane_cabin_window_aisle",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Look at where Seat {seat_letter} sits in the diagram above.",
        tier_2_hint=f"A and F are at the windows; C and D are next to the aisle; B and E are in the middle.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_seat_event_banquet_round_tables(r: random.Random) -> Dict[str, Any]:
    tables = r.choice([12, 15, 18, 20])
    chairs_per_table = r.choice([8, 10])
    head_table_guests = r.choice([10, 12])
    total_guests = (tables * chairs_per_table) + head_table_guests

    prompt = (
        f"Refer to the banquet hall seating layout plan below set up for a matric farewell celebration:\n\n"
        f"• The room layout features {tables} identical round guest tables, each seating {chairs_per_table} guests.\n"
        f"• A raised rectangular Head Table seats exactly {head_table_guests} dignitaries.\n\n"
        f"Calculate the total maximum seating capacity of the banquet hall."
    )
    ans = f"{total_guests} guests"

    s1 = f"Multiply the number of round tables ({tables}) by chairs per table ({chairs_per_table}) = {tables * chairs_per_table}, then add the head table guests ({head_table_guests})."
    s2 = f"✓ [1 Mark: Method – Multiplying round table capacity and adding head table]\nRound tables = {tables} × {chairs_per_table} = {tables * chairs_per_table} guests.\nTotal capacity = {tables * chairs_per_table} + {head_table_guests}."
    s3 = f"✓ [1 Mark: Accuracy – Total hall capacity]\nTotal = {total_guests} guests."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Matric Farewell Banquet Layout ({total_guests} Guests)",
        "rooms": [
            {"name": f"Guest Tables ({tables})", "dimensions": f"{chairs_per_table} per table"},
            {"name": f"Head Table", "dimensions": f"{head_table_guests} guests"},
            {"name": "Dance Floor", "dimensions": "8 m x 6 m"},
            {"name": "Buffet Area", "dimensions": "10 m x 4 m"},
        ],
        "scale": "1 : 100",
    }

    return _build_question_payload(
        "map_seat_event_banquet_round_tables",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Find the total at round tables: {tables} × {chairs_per_table} = {tables * chairs_per_table}.",
        tier_2_hint=f"Add the {head_table_guests} head table guests: {tables * chairs_per_table} + {head_table_guests}.",
        tier_3_hint=f"Total capacity = {total_guests} guests.",
        diagram_spec=diagram_spec,
    )


def _gen_map_indoor_shopping_mall_directory_navigation(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    mall = r.choice(["Gateway Theatre of Shopping", "Mall of Africa", "Canal Walk", "Menlyn Park", "Sandton City"])
    store_code = r.choice(["Shop B14", "Shop C22", "Shop A05", "Shop D12"])
    grid_col = r.choice(["B", "C", "D"])
    grid_row = r.choice([1, 2, 3, 4])

    prompt = (
        f"{name} is visiting {mall} and uses the indoor directory map to locate {store_code}.\n"
        f"The directory index lists the store's map grid coordinates as **{grid_col}{grid_row}**.\n\n"
        f"Refer to the indoor mall grid layout below.\n\n"
        f"Explain how {name} uses the grid coordinate {grid_col}{grid_row} to locate the store on the map."
    )
    ans = f"Find column {grid_col} on the horizontal grid axis, find row {grid_row} on the vertical axis, and locate the square where column {grid_col} and row {grid_row} intersect."
    opts = [
        f"Find column {grid_col} on the horizontal grid axis, find row {grid_row} on the vertical axis, and locate the square where column {grid_col} and row {grid_row} intersect.",
        f"Walk {grid_row} kilometres in the direction of letter {grid_col}.",
        f"Count {grid_row} shops starting from entrance {grid_col}.",
        f"Take elevator {grid_col} up to floor {grid_row}.",
    ]

    s1 = f"Understand alphanumeric grid referencing on indoor floor plans: Column letter on one axis intersects row number on the other axis."
    s2 = f"✓ [1 Mark: Method – Describing Cartesian-style grid intersection lookup]\nIdentify horizontal column {grid_col} and vertical row {grid_row} and locate their intersection square."
    s3 = f"✓ [1 Mark: Accuracy – Correct grid lookup procedure]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "grid_map",
        "title": f"Mall Floor Grid ({mall}: {grid_col}{grid_row})",
        "columns": 5,
        "rows": 4,
        "landmarks": [{"name": store_code, "row": grid_row, "col": grid_col}],
    }

    return _build_question_payload(
        "map_indoor_shopping_mall_directory_navigation",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"What do the letter {grid_col} and number {grid_row} represent on a map grid?",
        tier_2_hint=f"Locate column {grid_col} and row {grid_row} and find where they meet.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    s1 = f"Extract sequential waypoints and directions from an indoor commercial floor plan directory."
    s2 = f"✓ [1 Mark: Method – Sequential navigation path synthesis from directory text]\nFollow straight path past fountain → turn right at landmark elevator → reach target destination."
    s3 = f"✓ [1 Mark: Accuracy – Clear correct navigation route]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": "Ground Floor Directory Navigation Plan",
        "rooms": [
            {"name": "Entrance Gate 3", "dimensions": "North Atrium"},
            {"name": "Pharmacy G12", "dimensions": "Left of Entrance"},
            {"name": "Central Elevator", "dimensions": "80 m Straight"},
            {"name": "Supermarket G45", "dimensions": "50 m Right Turn"},
        ],
        "scale": "1 : 200",
    }

    return _build_question_payload(
        "map_indoor_shopping_mall_directory_navigation",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Read the exact directions provided on the directory board.",
        tier_2_hint="The path involves walking straight past the fountain, then turning right at the elevator.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_indoor_evacuation_shortest_emergency_exit(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    room = r.choice(["Computer Lab 3", "Science Lab 2", "Library Mezzanine", "Main Auditorium"])
    d_exit1_m = r.choice([15, 18, 22])
    d_exit2_m = d_exit1_m + r.choice([12, 16, 20])

    prompt = (
        f"{name} is in {room} when the school emergency evacuation alarm sounds.\n"
        f"The emergency evacuation floor plan indicates two designated escape routes:\n"
        f"• Exit Door A: {_fmt(d_exit1_m)} metres away along the South corridor\n"
        f"• Exit Door B: {_fmt(d_exit2_m)} metres away through the North stairwell\n\n"
        f"Refer to the emergency evacuation layout below.\n\n"
        f"According to South African occupational health and safety regulations, which exit door should {name} use, and why?"
    )
    ans = f"Exit Door A — It is the shortest, most direct emergency escape path ({_fmt(d_exit1_m)} m vs {_fmt(d_exit2_m)} m), minimizing evacuation time and smoke exposure risk."
    opts = [
        f"Exit Door A — It is the shortest, most direct emergency escape path ({_fmt(d_exit1_m)} m vs {_fmt(d_exit2_m)} m), minimizing evacuation time and smoke exposure risk.",
        f"Exit Door B — Because longer escape routes provide more exercise during an emergency.",
        "Neither exit — Occupants should remain seated inside the room until the fire is put out.",
        "Exit Door B — Because stairwells are always safe from smoke and flames.",
    ]

    s1 = f"Apply emergency safety principles (SANS 10400-T): Always take the shortest unobstructed route to the nearest clear exterior fire assembly point."
    s2 = f"✓ [1 Mark: Method – Comparing escape route distances and identifying safety principle]\nExit A ({_fmt(d_exit1_m)} m) is shorter than Exit B ({_fmt(d_exit2_m)} m)."
    s3 = f"✓ [1 Mark: Accuracy – Selection of Exit A with safety rationale]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "grid_map",
        "title": f"Evacuation Plan ({room})",
        "columns": 6,
        "rows": 4,
        "landmarks": [{"name": f"Exit A ({d_exit1_m}m)", "row": 1, "col": 1}, {"name": f"Exit B ({d_exit2_m}m)", "row": 4, "col": 6}],
    }

    return _build_question_payload(
        "map_indoor_evacuation_shortest_emergency_exit",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint=f"Compare the two distances: {_fmt(d_exit1_m)} m vs {_fmt(d_exit2_m)} m.",
        tier_2_hint="In a fire emergency, always use the closest available exit route.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    s1 = f"Understand building fire safety codes and evacuation diagram protocols (SANS 10400-T regulations)."
    s2 = f"✓ [1 Mark: Method – Technical rationale for prohibiting elevators during fire evacuation]\nElevators present lethal failure hazards during structural fires due to power cuts, sensor activation, and smoke accumulation in elevator shafts."
    s3 = f"✓ [1 Mark: Accuracy – Correct evacuation rule and motivation]\n{ans}"

    diagram_spec = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": "Corridor Emergency Fire Evacuation Plan",
        "rooms": [
            {"name": "Office Corridor", "dimensions": "Active Zone"},
            {"name": "Fire Stairwell 1", "dimensions": "Emergency Exit"},
            {"name": "Fire Stairwell 2", "dimensions": "Emergency Exit"},
            {"name": "Elevator Lobby", "dimensions": "DO NOT USE"},
        ],
        "scale": "SANS 10400-T Standard",
    }

    return _build_question_payload(
        "map_indoor_evacuation_shortest_emergency_exit",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="What happens to electric elevators if a building's power cuts during a fire?",
        tier_2_hint="Elevators can trap passengers or fill with smoke; stairwells are protected fire escapes.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )


def _gen_map_indoor_universal_wheelchair_accessibility(r: random.Random) -> Dict[str, Any]:
    facility = r.choice(["municipal library", "community clinic", "civic centre", "provincial museum"])
    ramp_m = r.choice([12, 15, 18])
    prompt = (
        f"Refer to the {facility} universal accessibility floor plan below (featuring a {ramp_m} m access ramp).\n\n"
        f"Which architectural feature on the plan allows a wheelchair user to access a raised reading terrace "
        f"located 1,5 metres above the main entrance level without encountering stairs?"
    )
    ans = "A gently sloped access ramp (with a maximum gradient of 1 : 12 and safety handrails) or an accessible passenger platform lift"
    opts = [
        "A gently sloped access ramp (with a maximum gradient of 1 : 12 and safety handrails) or an accessible passenger platform lift",
        "A steep flight of concrete stairs with non-slip nosing",
        "An overhead rope ladder with climbing harnesses",
        "An outdoor fire escape spiral metal staircase",
    ]

    s1 = f"Identify universal accessibility standards (SANS 10400-S) on public building architectural plans: ramps with gradient ≤ 1:12, elevators, and wide doorways."
    s2 = f"✓ [1 Mark: Method – Identifying step-free architectural access elements]\nRamps and platform lifts provide barrier-free vertical transit for wheeled mobility devices."
    s3 = f"✓ [1 Mark: Accuracy – Correct accessibility feature identification]\nFeature: {ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Universal Accessibility Plan ({facility.title()})",
        "rooms": [
            {"name": "Ground Level", "dims": "0,0 m Level", "length_m": 10.0, "width_m": 6.0},
            {"name": f"Access Ramp ({ramp_m}m)", "dims": "1 : 12 Gradient", "length_m": float(ramp_m), "width_m": 2.0},
            {"name": "Raised Terrace", "dims": "+1,5 m Level", "length_m": 8.0, "width_m": 6.0},
        ],
        "length_m": 20.0,
        "width_m": 12.0,
        "scale": "SANS 10400-S",
    }

    return _build_question_payload(
        "map_indoor_universal_wheelchair_accessibility",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="How can a person in a wheelchair move between different floor levels?",
        tier_2_hint="Ramps with gentle slopes and platform lifts allow step-free access.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )

    s1 = f"Identify universal accessibility standards (SANS 10400-S) on public building architectural plans: ramps with gradient ≤ 1:12, elevators, and wide doorways."
    s2 = f"✓ [1 Mark: Method – Identifying step-free architectural access elements]\nRamps and platform lifts provide barrier-free vertical transit for wheeled mobility devices."
    s3 = f"✓ [1 Mark: Accuracy – Correct accessibility feature identification]\nFeature: {ans}."

    diagram_spec = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": "Municipal Library Universal Accessibility Plan",
        "rooms": [
            {"name": "Ground Floor Entrance", "dimensions": "0,0 m Level"},
            {"name": "Access Ramp", "dimensions": "1 : 12 Gradient"},
            {"name": "Reading Terrace", "dimensions": "+1,5 m Level"},
            {"name": "Main Staircase", "dimensions": "Flight of Stairs"},
        ],
        "scale": "SANS 10400-S Standard",
    }

    return _build_question_payload(
        "map_indoor_universal_wheelchair_accessibility",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="How can a person in a wheelchair move between different floor levels?",
        tier_2_hint="Ramps with gentle slopes and platform lifts allow step-free access.",
        tier_3_hint=f"{ans}",
        diagram_spec=diagram_spec,
    )
