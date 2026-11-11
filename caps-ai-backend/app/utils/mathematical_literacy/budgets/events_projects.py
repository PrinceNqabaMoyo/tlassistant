"""Cluster 4: Event, Project & Travel Budgeting (8 Subskills)."""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional
from .common import SA_NAMES, _fmt, _fmt_curr, _make_q

def _gen_budg_event_birthday_party_catering(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    hall_hire = round(r.choice([1200.00, 1500.00, 1800.00]), 2)
    dj_sound = round(r.choice([800.00, 1000.00, 1200.00]), 2)
    decorations = round(r.choice([450.00, 600.00, 750.00]), 2)
    catering_per_guest = round(r.choice([65.00, 75.00, 85.00, 95.00]), 2)
    num_guests = r.choice([30, 40, 50, 60])
    total_catering = round(catering_per_guest * num_guests, 2)
    total_event_cost = round(hall_hire + dj_sound + decorations + total_catering, 2)
    ans_str = _fmt_curr(total_event_cost)

    prompt = (
        f"{name}'s family is planning a 21st birthday celebration for **{num_guests} guests**.\n\n"
        f"The itemised event budget includes:\n"
        f"• Community hall hire: **{_fmt_curr(hall_hire)}**\n"
        f"• DJ and sound equipment hire: **{_fmt_curr(dj_sound)}**\n"
        f"• Balloon garlands and table decorations: **{_fmt_curr(decorations)}**\n"
        f"• Finger food catering platter cost: **{_fmt_curr(catering_per_guest)} per guest**\n\n"
        f"Calculate the **Total Budgeted Cost** for the birthday event."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Total event budget combines fixed venue/sound costs and variable catering costs based on guest attendance:\n"
        f"  $$\\text{{Total Cost}} = \\text{{Hall}} + \\text{{DJ}} + \\text{{Decor}} + (\\text{{Catering per guest}} \\times \\text{{Number of guests}})$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Total Catering}} = \\text{{{_fmt_curr(catering_per_guest)}}} \\times {num_guests} = \\text{{{_fmt_curr(total_catering)}}}$.\n"
        f"• $\\text{{Total Event Cost}} = \\text{{{_fmt_curr(hall_hire)}}} + \\text{{{_fmt_curr(dj_sound)}}} + \\text{{{_fmt_curr(decorations)}}} + \\text{{{_fmt_curr(total_catering)}}} = \\text{{{_fmt_curr(total_event_cost)}}}$.\n"
        f"✓ **[1 Mark: Method – multiplying catering rate by guest count and adding fixed costs]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total party budget in Rands]**"
    )
    return _make_q(
        subskill="budg_event_birthday_party_catering",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (catering × guests) + hall + dj + decor", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"First find total catering: {_fmt_curr(catering_per_guest)} × {num_guests} = {_fmt_curr(total_catering)}.",
            "tier_2": f"Add the hall ({_fmt_curr(hall_hire)}), DJ ({_fmt_curr(dj_sound)}), decorations ({_fmt_curr(decorations)}), and catering ({_fmt_curr(total_catering)}).",
            "tier_3": f"Total event cost = {_fmt_curr(total_event_cost)}."
        },
        r=r
    )

def _gen_budg_event_ticket_cover_charge_break_even(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    venue_cost = round(r.choice([2500.00, 3000.00, 3600.00]), 2)
    sound_lights = round(r.choice([1500.00, 2000.00]), 2)
    security_guards = round(r.choice([800.00, 1000.00, 1200.00]), 2)
    total_fixed_cost = round(venue_cost + sound_lights + security_guards, 2)
    ticket_price = r.choice([50, 60, 80, 100])
    break_even_tickets = math.ceil(total_fixed_cost / ticket_price)
    ans_str = f"{break_even_tickets} tickets"

    prompt = (
        f"The Representative Council of Learners (RCL) at {name}'s high school is organizing a fundraising talent show:\n\n"
        f"• School hall lighting & sound technician hire: **{_fmt_curr(sound_lights)}**\n"
        f"• Private security officers: **{_fmt_curr(security_guards)}**\n"
        f"• Venue sanitization & cleanup deposit: **{_fmt_curr(venue_cost)}**\n"
        f"• Admission ticket price: **{_fmt_curr(ticket_price)} per ticket**\n\n"
        f"Calculate the **minimum number of tickets** that must be sold to **break even** (cover all fixed expenses exactly)."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• The break-even point occurs when total ticket revenue equals total fixed costs:\n"
        f"  $$\\text{{Break-even Tickets}} = \\frac{{\\text{{Total Fixed Costs}}}}{{\\text{{Price per Ticket}}}}$$\n"
        f"• If the division produces a fraction, always round up to the next whole ticket, as you cannot sell a partial ticket.\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Total Fixed Costs}} = \\text{{{_fmt_curr(sound_lights)}}} + \\text{{{_fmt_curr(security_guards)}}} + \\text{{{_fmt_curr(venue_cost)}}} = \\text{{{_fmt_curr(total_fixed_cost)}}}$.\n"
        f"• $\\text{{Break-even}} = \\frac{{{_fmt(total_fixed_cost)}}}{{{ticket_price}}} = {total_fixed_cost / ticket_price:.2f} \\implies {break_even_tickets}\\text{{ tickets}}$.\n"
        f"✓ **[1 Mark: Method – dividing total fixed costs by ticket price and rounding up]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct whole number of tickets]**"
    )
    custom_opts = [
        f"{break_even_tickets} tickets",
        f"{break_even_tickets - 1} tickets",
        f"{break_even_tickets + 10} tickets",
        f"{break_even_tickets - 10} tickets"
    ]
    return _make_q(
        subskill="budg_event_ticket_cover_charge_break_even",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – total costs ÷ ticket price (rounded up)", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Sum fixed expenses: {_fmt_curr(sound_lights)} + {_fmt_curr(security_guards)} + {_fmt_curr(venue_cost)} = {_fmt_curr(total_fixed_cost)}.",
            "tier_2": f"Divide {_fmt_curr(total_fixed_cost)} by {_fmt_curr(ticket_price)} per ticket.",
            "tier_3": f"Minimum tickets needed = {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_budg_event_attendance_sensitivity_surplus(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_costs = round(r.choice([8000.00, 9500.00, 11000.00]), 2)
    ticket_price = round(r.choice([80.00, 100.00, 120.00]), 2)
    attendees = r.choice([120, 140, 150, 180])
    total_revenue = round(ticket_price * attendees, 2)
    net_surplus = round(total_revenue - total_costs, 2)
    ans_str = _fmt_curr(net_surplus)

    prompt = (
        f"{name}'s community choir hosts an annual fundraising concert:\n\n"
        f"• Total staging and catering expenses: **{_fmt_curr(total_costs)}**\n"
        f"• Ticket price per attendee: **{_fmt_curr(ticket_price)}**\n"
        f"• Actual confirmed attendance: **{attendees} people**\n\n"
        f"Calculate the **net fundraising profit (surplus)** generated by the concert."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Net Profit (Surplus) is calculated as:\n"
        f"  $$\\text{{Net Surplus}} = \\text{{Total Revenue}} - \\text{{Total Expenses}}$$\n"
        f"  $$\\text{{Total Revenue}} = \\text{{Ticket Price}} \\times \\text{{Number of Attendees}}$$\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Total Revenue}} = \\text{{{_fmt_curr(ticket_price)}}} \\times {attendees} = \\text{{{_fmt_curr(total_revenue)}}}$.\n"
        f"• $\\text{{Net Surplus}} = \\text{{{_fmt_curr(total_revenue)}}} - \\text{{{_fmt_curr(total_costs)}}} = \\text{{{_fmt_curr(net_surplus)}}}$.\n"
        f"✓ **[1 Mark: Method – multiplying ticket price by attendees and subtracting total expenses]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct fundraising surplus in Rands]**"
    )
    return _make_q(
        subskill="budg_event_attendance_sensitivity_surplus",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (ticket_price × attendees) - expenses", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Calculate ticket revenue: {_fmt_curr(ticket_price)} × {attendees} = {_fmt_curr(total_revenue)}.",
            "tier_2": f"Subtract total expenses ({_fmt_curr(total_costs)}) from revenue ({_fmt_curr(total_revenue)}).",
            "tier_3": f"Net surplus = {_fmt_curr(net_surplus)}."
        },
        r=r
    )

def _gen_budg_proj_travel_bus_trip_comparison(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    team_members = 18
    # Option A: Private minibus charter: R 6 500 flat fee + R 850 toll gates
    charter_fee = round(r.choice([5800.00, 6200.00, 6500.00]), 2)
    toll_gates = round(r.choice([650.00, 780.00, 850.00]), 2)
    option_a_total = round(charter_fee + toll_gates, 2)
    option_a_per_person = round(option_a_total / team_members, 2)

    # Option B: Individual commercial bus tickets
    bus_ticket_return = round(r.choice([380.00, 420.00, 450.00]), 2)
    option_b_total = round(bus_ticket_return * team_members, 2)

    diff = round(abs(option_a_total - option_b_total), 2)
    cheaper_option = "Private charter" if option_a_total < option_b_total else "Commercial bus"
    cheaper_total = min(option_a_total, option_b_total)
    ans_str = f"{cheaper_option} by {_fmt_curr(diff)}"

    prompt = (
        f"{name} is tasked with budgeting travel for a soccer team of **{team_members} players** travelling from Polokwane to Johannesburg for a tournament:\n\n"
        f"• **Option 1 (Private 22-seater minibus charter)**: Flat rental fee of **{_fmt_curr(charter_fee)}** plus **{_fmt_curr(toll_gates)}** in total toll fees.\n"
        f"• **Option 2 (Commercial scheduled bus)**: Return ticket cost of **{_fmt_curr(bus_ticket_return)} per player**.\n\n"
        f"1. Calculate the total cost for both options.\n"
        f"2. Determine which travel option is **cheaper** and by **how much**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Compare total expenditure for both travel alternatives:\n"
        f"  $$\\text{{Option 1 Total}} = \\text{{Charter Fee}} + \\text{{Toll Gates}}$$\n"
        f"  $$\\text{{Option 2 Total}} = \\text{{Ticket Price}} \\times \\text{{Number of Players}}$$\n"
        f"• Calculate the difference: $|\\text{{Option 1}} - \\text{{Option 2}}|$.\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Option 1}} = \\text{{{_fmt_curr(charter_fee)}}} + \\text{{{_fmt_curr(toll_gates)}}} = \\text{{{_fmt_curr(option_a_total)}}}$.\n"
        f"• $\\text{{Option 2}} = \\text{{{_fmt_curr(bus_ticket_return)}}} \\times {team_members} = \\text{{{_fmt_curr(option_b_total)}}}$.\n"
        f"• $\\text{{Difference}} = |\\text{{{_fmt_curr(option_a_total)}}} - \\text{{{_fmt_curr(option_b_total)}}}| = \\text{{{_fmt_curr(diff)}}}$.\n"
        f"• Therefore, **{cheaper_option}** is cheaper by **{_fmt_curr(diff)}**.\n"
        f"✓ **[1 Mark: Method – calculating both totals and determining cost difference]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct travel option choice and monetary savings]**"
    )
    custom_opts = [
        f"Private charter by {_fmt_curr(diff)}",
        f"Commercial bus by {_fmt_curr(diff)}",
        f"Private charter by {_fmt_curr(round(diff * 1.15, 2))}",
        f"Commercial bus by {_fmt_curr(round(diff * 1.15, 2))}"
    ]
    return _make_q(
        subskill="budg_proj_travel_bus_trip_comparison",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – comparing Option 1 and Option 2 totals", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Option 1 = {_fmt_curr(charter_fee)} + {_fmt_curr(toll_gates)} = {_fmt_curr(option_a_total)}. Option 2 = {_fmt_curr(bus_ticket_return)} × {team_members} = {_fmt_curr(option_b_total)}.",
            "tier_2": f"Subtract the smaller total from the larger total.",
            "tier_3": f"Result: {ans_str}."
        },
        options=custom_opts,
        r=r
    )

def _gen_budg_proj_holiday_drakensberg_hike(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    people = 4
    nights = 3
    chalet_per_night = round(r.choice([850.00, 950.00, 1100.00]), 2)  # for the chalet
    conservation_per_person_per_day = round(r.choice([55.00, 65.00, 75.00]), 2)
    fuel_total = round(r.choice([1200.00, 1400.00]), 2)
    groceries_shared = round(r.choice([1600.00, 1800.00]), 2)

    total_chalet = round(chalet_per_night * nights, 2)
    total_conservation = round(conservation_per_person_per_day * people * nights, 2)
    grand_total = round(total_chalet + total_conservation + fuel_total + groceries_shared, 2)
    cost_per_person = round(grand_total / people, 2)
    ans_str = _fmt_curr(cost_per_person)

    prompt = (
        f"{name} and **3 friends** (a group of **{people} people** in total) plan a **{nights}-night hiking getaway** in the Drakensberg mountains:\n\n"
        f"• Self-catering chalet accommodation: **{_fmt_curr(chalet_per_night)} per night** (total for the whole unit)\n"
        f"• Ezemvelo KZN Wildlife conservation levy: **{_fmt_curr(conservation_per_person_per_day)} per person per day** (for {nights} days)\n"
        f"• Shared petrol and toll gate costs: **{_fmt_curr(fuel_total)}**\n"
        f"• Shared group food & braai supplies: **{_fmt_curr(groceries_shared)}**\n\n"
        f"1. Calculate the grand total expenditure for the trip.\n"
        f"2. Calculate the **budgeted cost per person** if all expenses are shared equally."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Calculate each component of the holiday budget:\n"
        f"  $$\\text{{Chalet}} = \\text{{Chalet Rate}} \\times \\text{{Nights}}$$\n"
        f"  $$\\text{{Conservation}} = \\text{{Daily Levy}} \\times \\text{{People}} \\times \\text{{Days}}$$\n"
        f"  $$\\text{{Grand Total}} = \\text{{Chalet}} + \\text{{Conservation}} + \\text{{Fuel}} + \\text{{Food}}$$\n"
        f"• Divide grand total equally among {people} friends: $\\frac{{\\text{{Grand Total}}}}{{{people}}}$.\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Chalet}} = \\text{{{_fmt_curr(chalet_per_night)}}} \\times {nights} = \\text{{{_fmt_curr(total_chalet)}}}$.\n"
        f"• $\\text{{Conservation}} = \\text{{{_fmt_curr(conservation_per_person_per_day)}}} \\times {people} \\times {nights} = \\text{{{_fmt_curr(total_conservation)}}}$.\n"
        f"• $\\text{{Grand Total}} = \\text{{{_fmt_curr(total_chalet)}}} + \\text{{{_fmt_curr(total_conservation)}}} + \\text{{{_fmt_curr(fuel_total)}}} + \\text{{{_fmt_curr(groceries_shared)}}} = \\text{{{_fmt_curr(grand_total)}}}$.\n"
        f"• $\\text{{Cost per Person}} = \\frac{{\\text{{{_fmt_curr(grand_total)}}}}}{{{people}}} = \\text{{{_fmt_curr(cost_per_person)}}}$.\n"
        f"✓ **[1 Mark: Method – summing all components and dividing by {people} people]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct cost per person in Rands]**"
    )
    return _make_q(
        subskill="budg_proj_holiday_drakensberg_hike",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – grand total ÷ 4 people", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Chalet = {_fmt_curr(chalet_per_night)} × {nights} = {_fmt_curr(total_chalet)}. Conservation = {_fmt_curr(conservation_per_person_per_day)} × {people} × {nights} = {_fmt_curr(total_conservation)}.",
            "tier_2": f"Sum all costs ({_fmt_curr(grand_total)}) and divide by {people} people.",
            "tier_3": f"Cost per person = {_fmt_curr(cost_per_person)}."
        },
        r=r
    )

def _gen_budg_proj_matric_dance_total_cost(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    ticket = round(r.choice([450.00, 500.00, 550.00, 600.00]), 2)
    attire_hire = round(r.choice([1200.00, 1500.00, 1800.00]), 2)
    shoes_accessories = round(r.choice([450.00, 550.00, 650.00]), 2)
    hair_styling = round(r.choice([350.00, 450.00, 550.00]), 2)
    photography = round(r.choice([300.00, 400.00]), 2)
    car_hire_share = round(r.choice([250.00, 350.00]), 2)
    total_cost = round(ticket + attire_hire + shoes_accessories + hair_styling + photography + car_hire_share, 2)
    ans_str = _fmt_curr(total_cost)

    prompt = (
        f"{name} prepares an itemised personal budget for attending the Grade 12 Matric Dance farewell:\n\n"
        f"• Admission ticket (includes three-course dinner): **{_fmt_curr(ticket)}**\n"
        f"• Evening dress / tailored suit hire: **{_fmt_curr(attire_hire)}**\n"
        f"• Formal shoes and accessories: **{_fmt_curr(shoes_accessories)}**\n"
        f"• Professional hair styling and grooming: **{_fmt_curr(hair_styling)}**\n"
        f"• Professional photo package: **{_fmt_curr(photography)}**\n"
        f"• Shared vintage car hire contribution: **{_fmt_curr(car_hire_share)}**\n\n"
        f"Calculate {name}'s **Total Matric Dance Budget**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• The total project budget is found by summing all individual preparation and event costs:\n"
        f"  $$\\text{{Total Budget}} = \\sum \\text{{All Itemised Matric Dance Expenses}}$$\n\n"
        f"**Step 2: Method Setup & Summation**\n"
        f"• $\\text{{Total Cost}} = \\text{{{_fmt_curr(ticket)}}} + \\text{{{_fmt_curr(attire_hire)}}} + \\text{{{_fmt_curr(shoes_accessories)}}} + \\text{{{_fmt_curr(hair_styling)}}} + \\text{{{_fmt_curr(photography)}}} + \\text{{{_fmt_curr(car_hire_share)}}} = \\text{{{_fmt_curr(total_cost)}}}$.\n"
        f"✓ **[1 Mark: Method – correctly summing all 6 itemised expenses]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct total budget in Rands]**"
    )
    return _make_q(
        subskill="budg_proj_matric_dance_total_cost",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – sum of all 6 dance expenses", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": "Add up all 6 expenses in the list.",
            "tier_2": f"{_fmt_curr(ticket)} + {_fmt_curr(attire_hire)} + {_fmt_curr(shoes_accessories)} + {_fmt_curr(hair_styling)} + {_fmt_curr(photography)} + {_fmt_curr(car_hire_share)}.",
            "tier_3": f"Total budget = {_fmt_curr(total_cost)}."
        },
        r=r
    )

def _gen_budg_proj_home_improvement_painting(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    wall_area_m2 = r.choice([80, 100, 120, 140])
    coverage_per_litre = 8  # 8 m^2 per litre
    coats = 2
    total_paint_litres = math.ceil((wall_area_m2 * coats) / coverage_per_litre)
    # 5L tins
    tins_5l = math.ceil(total_paint_litres / 5)
    cost_per_tin = round(r.choice([420.00, 480.00, 540.00]), 2)
    total_paint_cost = round(tins_5l * cost_per_tin, 2)
    accessories = round(r.choice([250.00, 320.00]), 2)  # rollers, brushes, masking tape
    labour_cost = round(r.choice([800.00, 1000.00, 1200.00]), 2)
    total_project_cost = round(total_paint_cost + accessories + labour_cost, 2)
    ans_str = _fmt_curr(total_project_cost)

    prompt = (
        f"{name} prepares a renovation budget to repaint the exterior walls of the family home:\n\n"
        f"• Total wall surface area: **{wall_area_m2} m²** (requiring **{coats} coats of paint**)\n"
        f"• Paint coverage specification: **{coverage_per_litre} m² per litre**\n"
        f"• The paint is sold only in **5-litre tins** at **{_fmt_curr(cost_per_tin)} per tin**\n"
        f"• Paint rollers, brushes, and drop cloths: **{_fmt_curr(accessories)}**\n"
        f"• Painter labour fee: **{_fmt_curr(labour_cost)}**\n\n"
        f"1. Determine the number of 5 L tins of paint required (rounding up to the nearest whole tin).\n"
        f"2. Calculate the **Total Renovation Budget**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Total area to cover = $\\text{{Wall Area}} \\times \\text{{Number of Coats}}$.\n"
        f"• Litres of paint required = $\\frac{{\\text{{Total Area}}}}{{\\text{{Coverage per Litre}}}}$.\n"
        f"• Number of 5 L tins = $\\lceil \\frac{{\\text{{Total Litres}}}}{{5}} \\rceil$.\n"
        f"• Total Project Budget = $(\\text{{Tins}} \\times \\text{{Cost per tin}}) + \\text{{Accessories}} + \\text{{Labour}}$.\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Total Paint Area}} = {wall_area_m2} \\times {coats} = {wall_area_m2 * coats}\\text{{ m}}^2$.\n"
        f"• $\\text{{Litres Needed}} = \\frac{{{wall_area_m2 * coats}}}{{{coverage_per_litre}}} = {total_paint_litres}\\text{{ litres}}$.\n"
        f"• $\\text{{5 L Tins}} = \\lceil \\frac{{{total_paint_litres}}}{{5}} \\rceil = {tins_5l}\\text{{ tins}}$.\n"
        f"• $\\text{{Paint Cost}} = {tins_5l} \\times \\text{{{_fmt_curr(cost_per_tin)}}} = \\text{{{_fmt_curr(total_paint_cost)}}}$.\n"
        f"• $\\text{{Total Budget}} = \\text{{{_fmt_curr(total_paint_cost)}}} + \\text{{{_fmt_curr(accessories)}}} + \\text{{{_fmt_curr(labour_cost)}}} = \\text{{{_fmt_curr(total_project_cost)}}}$.\n"
        f"✓ **[1 Mark: Method – finding number of tins, multiplying by tin price, and adding labour and accessories]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct home improvement project budget in Rands]**"
    )
    return _make_q(
        subskill="budg_proj_home_improvement_painting",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (tins × price) + accessories + labour", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Total area = {wall_area_m2} × {coats} = {wall_area_m2 * coats} m². Litres needed = {total_paint_litres} L. 5 L tins = {tins_5l} tins.",
            "tier_2": f"Paint cost = {tins_5l} × {_fmt_curr(cost_per_tin)} = {_fmt_curr(total_paint_cost)}. Add {_fmt_curr(accessories)} + {_fmt_curr(labour_cost)}.",
            "tier_3": f"Total budget = {_fmt_curr(total_project_cost)}."
        },
        r=r
    )

def _gen_budg_proj_school_sports_tour_fundraiser(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    total_tour_cost = round(r.choice([3600.00, 4200.00, 4800.00]), 2)
    sponsorship = round(r.choice([800.00, 1000.00, 1200.00]), 2)
    bake_sale = round(r.choice([400.00, 500.00, 600.00]), 2)
    total_raised = round(sponsorship + bake_sale, 2)
    shortfall = round(total_tour_cost - total_raised, 2)
    months = r.choice([4, 5, 6])
    monthly_payment = round(shortfall / months, 2)
    ans_str = _fmt_curr(monthly_payment)

    prompt = (
        f"{name} has been selected for the provincial netball tour, which costs **{_fmt_curr(total_tour_cost)}** in total.\n\n"
        f"To finance the tour, {name} secures:\n"
        f"• Local business corporate sponsorship: **{_fmt_curr(sponsorship)}**\n"
        f"• Saturday morning cake sale proceeds: **{_fmt_curr(bake_sale)}**\n\n"
        f"The remaining balance must be paid in **{months} equal monthly contributions** by {name}'s family.\n\n"
        f"Calculate the **required monthly payment**."
    )
    sol = (
        f"**Step 1: Financial Concept & Thought Process**\n"
        f"• Total funds raised reduces the outstanding financial obligation:\n"
        f"  $$\\text{{Remaining Balance}} = \\text{{Total Tour Cost}} - (\\text{{Sponsorship}} + \\text{{Cake Sale}})$$\n"
        f"• Monthly instalment = $\\frac{{\\text{{Remaining Balance}}}}{{\\text{{Number of Months}}}}$.\n\n"
        f"**Step 2: Method Setup & Calculations**\n"
        f"• $\\text{{Total Raised}} = \\text{{{_fmt_curr(sponsorship)}}} + \\text{{{_fmt_curr(bake_sale)}}} = \\text{{{_fmt_curr(total_raised)}}}$.\n"
        f"• $\\text{{Shortfall}} = \\text{{{_fmt_curr(total_tour_cost)}}} - \\text{{{_fmt_curr(total_raised)}}} = \\text{{{_fmt_curr(shortfall)}}}$.\n"
        f"• $\\text{{Monthly Payment}} = \\frac{{\\text{{{_fmt_curr(shortfall)}}}}}{{{months}}} = \\text{{{_fmt_curr(monthly_payment)}}}$.\n"
        f"✓ **[1 Mark: Method – subtracting funds raised from tour cost and dividing by {months} months]**\n\n"
        f"**Step 3: Final Answer**\n"
        f"$$\\mathbf{{{ans_str}}}$$\n"
        f"✓ **[1 Mark: Accuracy – correct monthly payment in Rands]**"
    )
    return _make_q(
        subskill="budg_proj_school_sports_tour_fundraiser",
        prompt=prompt,
        answer=ans_str,
        sol=sol,
        rubric=["1 Mark: Method – (tour cost - funds raised) ÷ months", f"1 Mark: Accuracy – {ans_str}"],
        hints={
            "tier_1": f"Funds raised = {_fmt_curr(sponsorship)} + {_fmt_curr(bake_sale)} = {_fmt_curr(total_raised)}.",
            "tier_2": f"Remaining balance = {_fmt_curr(total_tour_cost)} - {_fmt_curr(total_raised)} = {_fmt_curr(shortfall)}. Divide by {months}.",
            "tier_3": f"Monthly payment = {_fmt_curr(monthly_payment)}."
        },
        r=r
    )
