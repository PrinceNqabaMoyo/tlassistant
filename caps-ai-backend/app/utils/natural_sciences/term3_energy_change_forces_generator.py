"""Natural Sciences Senior Phase (Grades 7–9) — Term 3: Energy and Change & Forces Generator.
Deterministic 6-pillar CAPS question generator covering:
- Grade 7: Heat Energy Transfer (conduction, convection, radiation, thermal insulation).
- Grade 8: Static Electricity, Current Electricity (series and parallel circuits, current and potential difference).
- Grade 9: Forces (contact vs non-contact, gravitational weight calculations Fg = mg), Electrical Power and Cost of Electricity (kWh calculation).
Supports compound exam questions and atomic elementary sub-drills.
Zero-Meta-Curriculum Invariant strictly enforced.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.natural_sciences._science_common import (
    fmt_sa,
    make_science_question,
    rng,
)

TOPIC = "natural_sciences_energy_and_change"
LO = "ns_senior_energy_change_forces"

# ============================================================================
# ARCHETYPE 1: ELECTRICAL COST & POWER CALCULATIONS (Grade 9)
# ============================================================================

APPLIANCES_DB = [
    {"name": "Electric geyser", "power_w": 3000, "hours_day": 3, "tariff_cents": 285},
    {"name": "Electric stove oven", "power_w": 2400, "hours_day": 2, "tariff_cents": 285},
    {"name": "Kettle", "power_w": 2000, "hours_day": 0.5, "tariff_cents": 285},
    {"name": "Oil heater", "power_w": 1500, "hours_day": 6, "tariff_cents": 285},
    {"name": "Air conditioner", "power_w": 1800, "hours_day": 5, "tariff_cents": 285},
    {"name": "Incandescent lighting bank", "power_w": 600, "hours_day": 8, "tariff_cents": 285},
]


def _gen_cost_of_electricity_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    app = r.choice(APPLIANCES_DB)
    days = r.choice([30, 31, 28])
    power_kw = app["power_w"] / 1000.0
    total_hours = app["hours_day"] * days
    energy_kwh = power_kw * total_hours
    tariff_rand = app["tariff_cents"] / 100.0
    total_cost_rand = energy_kwh * tariff_rand
    
    cost_str = fmt_sa(total_cost_rand, 2)
    energy_str = fmt_sa(energy_kwh, 2)
    power_kw_str = fmt_sa(power_kw, 2)
    tariff_rand_str = fmt_sa(tariff_rand, 2)
    
    prompt = (
        f"A South African household operates a **{app['name']}** rated at **{app['power_w']} W** for an average of **{app['hours_day']} hours per day** "
        f"throughout a **{days}-day** billing month. The municipal electricity tariff is **{app['tariff_cents']} cents per kWh**.\n\n"
        f"1. Convert the appliance's power rating from watts (W) to kilowatts (kW).\n"
        f"2. Calculate the total electrical energy consumed in kilowatt-hours (kWh) over the {days}-day period.\n"
        f"3. Calculate the total cost (in Rands) of operating this appliance for the month.\n"
        f"4. State TWO practical energy-saving habits the household could implement to reduce their electricity bill."
    )
    prompt_latex = (
        rf"\textbf{{Household Electrical Energy Consumption & Cost Analysis}}" "\n\n"
        rf"\text{{Appliance: {app['name']}}} \quad P = {app['power_w']}\text{{ W}}, \quad t = {app['hours_day']}\text{{ h/day for }} {days}\text{{ days}}" "\n"
        rf"\text{{Municipal Tariff}} = {app['tariff_cents']}\text{{ c/kWh}} = \text{{R}}{tariff_rand_str}\text{{/kWh}}" "\n\n"
        r"\text{Formulae: } \quad E\text{ (kWh)} = P\text{ (kW)} \times t\text{ (hours)}, \quad \text{Cost} = E \times \text{Tariff}"
    )
    answer_latex = (
        rf"\text{{1. }} P = \frac{{{app['power_w']}}}{{1\,000}} = {power_kw_str}\text{{ kW}}" "\n"
        rf"\text{{2. }} t_\text{{total}} = {app['hours_day']} \times {days} = {fmt_sa(total_hours, 1)}\text{{ h}} \implies "
        rf"E = {power_kw_str}\text{{ kW}} \times {fmt_sa(total_hours, 1)}\text{{ h}} = {energy_str}\text{{ kWh}}" "\n"
        rf"\text{{3. Cost}} = {energy_str}\text{{ kWh}} \times \text{{R}}{tariff_rand_str} = \text{{R}}{cost_str}" "\n"
        r"\text{4. Fit a geyser timer / blanket, switch off when not in use, use solar / energy-efficient alternatives.}"
    )
    sample = (
        f"1. Power in kW = {app['power_w']} / 1000 = {power_kw_str} kW.\n"
        f"2. Total hours = {app['hours_day']} h/day x {days} days = {total_hours} hours.\n"
        f"   Energy consumed = {power_kw_str} kW x {total_hours} h = {energy_str} kWh.\n"
        f"3. Tariff in Rands = {app['tariff_cents']}c / 100 = R{tariff_rand_str} per kWh.\n"
        f"   Cost = {energy_str} kWh x R{tariff_rand_str} = R{cost_str}.\n"
        "4. Energy-saving measures: Install a geyser blanket/timer, replace with solar water heating, switch off at wall when idle."
    )
    schema = {
        "total_marks": 6,
        "marking_points": [
            {"id": "mp1", "desc": f"Convert W to kW ({power_kw_str} kW)", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Calculate monthly hours ({total_hours} h)", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Energy in kWh calculation ({energy_str} kWh)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Cost formula and accurate answer (R{cost_str})", "marks": 2, "editable": True},
            {"id": "mp5", "desc": "Practical energy-conservation recommendations", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Always divide watts by 1000 to get kilowatts before multiplying by hours.",
        "concept": "Electrical cost = Power in kW x Total time in hours x Tariff in Rands per kWh.",
        "breakdown": f"Step 1: {app['power_w']} W = {power_kw_str} kW. Step 2: {total_hours} hours total. Step 3: Energy = {energy_str} kWh. Step 4: Cost = R{cost_str}.",
    }
    return make_science_question(
        prefix="ns_elec_cost",
        topic=TOPIC,
        subskill="electrical_energy_and_cost_calculations",
        learning_objective_id=f"{LO}_cost_of_electricity",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["forgetting_watts_to_kilowatts_conversion", "cents_to_rands_currency_conversion_error"],
        keywords=["power", "kilowatt-hour", "electricity cost", "tariff", "energy conservation"],
        term=3,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode=mode,
        difficulty="medium",
        marks=6,
    )


# ============================================================================
# ARCHETYPE 2: FORCES & GRAVITATIONAL WEIGHT (Grade 9)
# ============================================================================

def _gen_forces_and_weight_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    mass_kg = r.choice([45, 60, 75, 80, 120, 250])
    g_earth = 9.8  # N/kg
    weight_earth = mass_kg * g_earth
    g_moon = 1.63  # N/kg
    weight_moon = mass_kg * g_moon
    
    w_earth_str = fmt_sa(weight_earth, 1)
    w_moon_str = fmt_sa(weight_moon, 1)
    
    prompt = (
        f"A piece of scientific equipment has a mass of **{mass_kg} kg**.\n\n"
        f"1. Distinguish clearly between the scientific concepts of **mass** and **weight**, stating the SI unit for each.\n"
        f"2. Calculate the weight of the equipment on Earth ($g_\\text{{Earth}} = 9,8\\text{{ N/kg}}$).\n"
        f"3. If the equipment is transported to the Moon, where gravitational acceleration is $1,63\\text{{ N/kg}}$, calculate:\n"
        f"   (a) Its mass on the Moon\n"
        f"   (b) Its weight on the Moon\n"
        f"4. Classify the gravitational force as either a **contact force** or a **non-contact (field) force**, and name ONE other force belonging to that same classification."
    )
    prompt_latex = (
        rf"\textbf{{Mechanics: Mass vs. Gravitational Weight}}" "\n\n"
        rf"\text{{Object mass }} m = {mass_kg}\text{{ kg}}, \quad g_\text{{Earth}} = 9,8\text{{ N/kg}}, \quad g_\text{{Moon}} = 1,63\text{{ N/kg}}" "\n\n"
        r"\text{Formula: } F_g = m \times g"
    )
    answer_latex = (
        r"\text{1. Mass: Amount of matter in an object (kg, constant). Weight: Gravitational attraction force on mass (Newtons, N, variable).}" "\n"
        rf"\text{{2. }} F_{{g,\text{{Earth}}}} = {mass_kg}\text{{ kg}} \times 9,8\text{{ N/kg}} = {w_earth_str}\text{{ N}}" "\n"
        rf"\text{{3. (a) Mass on Moon }} = {mass_kg}\text{{ kg (mass is invariant); (b) }} F_{{g,\text{{Moon}}}} = {mass_kg} \times 1,63 = {w_moon_str}\text{{ N}}" "\n"
        r"\text{4. Non-contact (field) force. Other examples: Magnetic force or Electrostatic force.}"
    )
    sample = (
        "1. Mass is the total quantity of matter in an object measured in kilograms (kg); it remains constant anywhere in the universe. "
        "Weight is the downward gravitational pull acting on that mass measured in Newtons (N); it changes with gravitational field strength.\n"
        f"2. F_g (Earth) = m x g = {mass_kg} kg x 9,8 N/kg = {w_earth_str} N.\n"
        f"3. (a) Mass on the Moon = {mass_kg} kg (mass does not change with location).\n"
        f"   (b) Weight on the Moon = m x g_Moon = {mass_kg} kg x 1,63 N/kg = {w_moon_str} N.\n"
        "4. Non-contact (field) force. Examples: Magnetic force or electrostatic force."
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Accurate distinction between mass (kg) and weight (N)", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Correct Earth weight calculation ({w_earth_str} N)", "marks": 2, "editable": True},
            {"id": "mp3", "desc": f"State invariant Moon mass ({mass_kg} kg)", "marks": 1, "editable": True},
            {"id": "mp4", "desc": f"Correct Moon weight calculation ({w_moon_str} N)", "marks": 1, "editable": True},
            {"id": "mp5", "desc": "Non-contact force classification with valid second example", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Remember that mass never changes regardless of which planet you travel to. Weight depends on local gravity.",
        "concept": "Formula: Fg = m x g. SI units: Mass in kg, Weight in Newtons (N).",
        "breakdown": f"Earth weight: {mass_kg} x 9,8 = {w_earth_str} N. Moon weight: {mass_kg} x 1,63 = {w_moon_str} N.",
    }
    return make_science_question(
        prefix="ns_weight_calc",
        topic=TOPIC,
        subskill="mass_weight_distinction_and_gravitational_force",
        learning_objective_id=f"{LO}_forces_and_weight",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["assuming_mass_changes_on_the_moon", "confusing_newtons_with_kilograms"],
        keywords=["mass", "weight", "gravity", "newton", "non-contact force"],
        term=3,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode=mode,
        difficulty="medium",
        marks=7,
    )


# ============================================================================
# ARCHETYPE 3: HEAT ENERGY TRANSFER (Grade 7)
# ============================================================================

HEAT_SCENARIOS = [
    {
        "process": "Conduction",
        "example": "A metal spoon becoming hot when left inside a bowl of boiling vegetable soup",
        "mechanism": "Direct transfer of thermal kinetic energy through particle collisions in a solid without movement of the material as a whole",
        "application": "Copper base on cooking pots; wooden or plastic handles as thermal insulators",
    },
    {
        "process": "Convection",
        "example": "Hot water rising to the top of an electric kettle while cold water sinks to the bottom",
        "mechanism": "Transfer of heat in fluids (liquids and gases) via density currents: heated fluid expands, becomes less dense, and rises",
        "application": "Domestic hot water geyser systems, oceanic convection currents, room convection heaters",
    },
    {
        "process": "Radiation",
        "example": "Feeling heat on your face when standing in bright sunlight or near an open braai fire",
        "mechanism": "Transfer of thermal energy via electromagnetic infrared waves that can travel through empty vacuum without requiring matter particles",
        "application": "Solar water heating panels painted matte black to absorb infrared rays; thermos flasks silvered to reflect radiation",
    },
]


def _gen_heat_transfer_question(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    item = r.choice(HEAT_SCENARIOS)
    
    prompt = (
        f"Thermal energy naturally transfers from regions of higher temperature to regions of lower temperature.\n\n"
        f"1. Name the THREE distinct mechanisms of thermal energy transfer.\n"
        f"2. Consider this real-world observation: *'{item['example']}'*.\n"
        f"   (a) Identify the primary mechanism of heat transfer responsible for this observation.\n"
        f"   (b) Explain the particle or physical mechanism that drives this process.\n"
        f"3. Explain why heat from the Sun can only reach the Earth via **radiation** and neither by conduction nor convection.\n"
        f"4. Why are domestic solar collector pipes painted matte black rather than shiny silver?"
    )
    prompt_latex = (
        rf"\textbf{{Thermal Physics: Heat Energy Transfer Mechanisms}}" "\n\n"
        rf"\text{{Observation: {item['example']}}}" "\n\n"
        r"\text{Analyse conduction, convection, and radiation. Explain vacuum heat propagation and selective absorption.}"
    )
    answer_latex = (
        r"\text{1. Conduction, Convection, Radiation.}" "\n"
        rf"\text{{2. (a) {item['process']}; (b) {item['mechanism']}.}}" "\n"
        r"\text{3. Space is an empty vacuum (no matter particles). Conduction and convection require physical particles to transfer energy, whereas infrared radiation travels through vacuum.}" "\n"
        r"\text{4. Dark matte black surfaces are superior absorbers of radiant infrared heat, whereas shiny surfaces reflect heat.}"
    )
    sample = (
        "1. Conduction, convection, and radiation.\n"
        f"2. (a) {item['process']}.\n"
        f"   (b) {item['mechanism']}.\n"
        "3. Outer space between the Sun and Earth is a vacuum containing no matter particles. Conduction and convection require particles to collide or circulate; only radiation travels as electromagnetic waves through a vacuum.\n"
        "4. Matte black surfaces are excellent absorbers of radiant heat energy, whereas shiny silver surfaces reflect radiant heat away."
    )
    schema = {
        "total_marks": 7,
        "marking_points": [
            {"id": "mp1", "desc": "Identify the 3 heat transfer methods", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correctly identify {item['process']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Accurate physical mechanism explanation", "marks": 2, "editable": True},
            {"id": "mp4", "desc": "Explain vacuum propagation (particles absent vs EM waves)", "marks": 2, "editable": True},
            {"id": "mp5", "desc": "Matte black as optimal thermal absorber", "marks": 1, "editable": True},
        ],
        "deductions": [],
        "carry_forward_rule": "consequential_accuracy",
    }
    hints = {
        "nudge": "Conduction takes place in solids; convection in fluids; radiation can pass through a vacuum.",
        "concept": "Dark matte colours absorb radiation; light shiny colours reflect radiation. Vacuum prevents conduction and convection.",
        "breakdown": f"Scenario is {item['process']}: {item['mechanism']}.",
    }
    return make_science_question(
        prefix="ns_heat_trans",
        topic=TOPIC,
        subskill="heat_transfer_mechanisms_and_thermal_physics",
        learning_objective_id=f"{LO}_heat_transfer",
        prompt=prompt,
        prompt_latex=prompt_latex,
        answer_latex=answer_latex,
        sample_answer=sample,
        marking_schema=schema,
        hints=hints,
        misconception_tags=["believing_convection_occurs_in_solids", "believing_heat_rises_instead_of_hot_fluid"],
        keywords=["conduction", "convection", "radiation", "insulation", "vacuum", "infrared"],
        term=3,
        caps_weight_percent=25,
        suggested_duration_mins=7,
        mode=mode,
        difficulty="medium",
        marks=7,
    )


# ============================================================================
# MAIN DISPATCH ENTRY POINT
# ============================================================================

def generate(seed: Optional[int] = None, grade: int = 8, mode: str = "compound", archetype: Optional[str] = None) -> Dict[str, Any]:
    """Generates a fully formed 6-pillar Natural Sciences Energy & Change question."""
    r = rng(seed)
    
    if archetype == "cost_electricity" or (archetype is None and grade == 9):
        return _gen_cost_of_electricity_question(r, mode=mode)
    elif archetype == "forces" or (archetype is None and grade == 8):
        return _gen_forces_and_weight_question(r, mode=mode)
    elif archetype == "heat_transfer" or (archetype is None and grade == 7):
        return _gen_heat_transfer_question(r, mode=mode)
    else:
        choice = r.choice(["cost_electricity", "forces", "heat_transfer"])
        if choice == "cost_electricity":
            return _gen_cost_of_electricity_question(r, mode=mode)
        elif choice == "forces":
            return _gen_forces_and_weight_question(r, mode=mode)
        else:
            return _gen_heat_transfer_question(r, mode=mode)
