"""Grade 7 Natural Sciences: Term 3 - Energy Transfer to Surroundings (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/03. Energy transfer to surroundings.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _clean_options(correct: str, distractors: List[str], rng: random.Random) -> List[str]:
    opts = [correct] + [d for d in distractors if d != correct][:3]
    rng.shuffle(opts)
    return opts


# 26. Mechanical friction as cause of wasted heat
def arch_26_mechanical_friction_as_cause_of_wasted_heat(rng: random.Random) -> Dict[str, Any]:
    surfaces = [
        ("metal brake pads clamping against a spinning car wheel rotor", "kinetic energy of the moving vehicle is transformed into intense thermal heat in the brake pads and disc"),
        ("bicycle wheel bearings spinning without grease", "metal-on-metal contact generating friction that converts kinetic rotation into wasted heat"),
        ("rubbing two hands together vigorously on a cold morning", "friction between skin surfaces transforming muscular kinetic motion into thermal warmth"),
    ]
    scene, mechanism = rng.choice(surfaces)
    prompt = (
        f"Consider **{scene}**.\n\n"
        f"How does **mechanical friction** convert useful kinetic energy into wasted energy transferred to the surroundings?"
    )
    correct = f"Friction between rubbing surfaces opposes motion, converting kinetic energy into thermal heat ({mechanism})."
    distractors = [
        "Friction creates gravitational waves that pull the surfaces into Earth's mantle.",
        "Friction destroys atoms permanently, eliminating energy from the universe.",
        "Friction produces cold nuclear radiation that freezes the contact surfaces.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Friction as a Dissipative Mechanism:**\n"
        f"At a microscopic level, solid surfaces have rough ridges and valleys (asperities).\n"
        f"When surfaces slide past one another, collisions between surface atoms convert macroscopic motion into microscopic random vibrations (**thermal energy**).\n"
        f"Result: {mechanism}."
    )
    return {
        "id": f"ns7_et_26_{rng.randint(100000, 999999)}",
        "subskill": "26_mechanical_friction_as_cause_of_wasted_heat",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_26",
        "hints": {
            "tier_1": "What happens when you rub two surfaces together? They get warm.",
            "tier_2": "Friction transforms kinetic motion into thermal heat.",
            "tier_3": "Friction opposes motion, converting kinetic energy into thermal heat.",
        },
        "misconception_tags": ["friction_destroys_energy", "friction_produces_electricity_only"],
    }


# 27. Lubrication to reduce wasted thermal energy
def arch_27_lubrication_to_reduce_wasted_thermal_energy(rng: random.Random) -> Dict[str, Any]:
    lubricants = [
        ("applying specialized oil to a bicycle chain and gears", "creates a microscopic slippery barrier between metal teeth, reducing friction and heat waste"),
        ("adding motor oil to a car engine crankcase", "prevents metal-to-metal contact between pistons and cylinder walls, minimizing wasted thermal energy and mechanical wear"),
    ]
    practice, benefit = rng.choice(lubricants)
    prompt = (
        f"Mechanics and cyclists practice regular maintenance by **{practice}**.\n\n"
        f"From an energy efficiency standpoint, why is **lubrication** applied to moving mechanical parts?"
    )
    correct = f"It reduces friction between moving surfaces ({benefit}), allowing a higher percentage of input energy to perform useful kinetic work."
    distractors = [
        "It acts as a fuel that burns continuously to double the machine's speed.",
        "It eliminates Earth's gravitational pull on the vehicle.",
        "It turns mechanical gears into superconducting magnets.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Role of Lubrication in Energy Efficiency:**\n"
        f"- Unlubricated parts suffer severe friction, converting substantial kinetic energy into wasted thermal energy.\n"
        f"- Lubricants form a thin fluid film separating contact surfaces.\n"
        f"- {benefit.capitalize()}, reducing wasted heat and raising overall machine efficiency."
    )
    return {
        "id": f"ns7_et_27_{rng.randint(100000, 999999)}",
        "subskill": "27_lubrication_to_reduce_wasted_thermal_energy",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_27",
        "hints": {
            "tier_1": "What does oil do between two rubbing metals?",
            "tier_2": "Oil reduces friction, which reduces wasted heat and wear.",
            "tier_3": f"Reduces friction between moving surfaces ({benefit}).",
        },
        "misconception_tags": ["oil_is_used_only_for_cleaning", "lubricants_burn_as_fuel_in_chains"],
    }


# 28. Sound energy as wasted mechanical vibration
def arch_28_sound_energy_as_wasted_mechanical_vibration(rng: random.Random) -> Dict[str, Any]:
    machines = [
        ("a noisy industrial electric jackhammer tearing up asphalt", "violent impacts against pavement create shockwaves and loud acoustic noise that escapes to surroundings"),
        ("a roaring vacuum cleaner motor running in a living room", "high-speed motor spinning and air turbulence produce acoustic sound that does not clean carpets"),
    ]
    tool, acoustics = rng.choice(machines)
    prompt = (
        f"Consider **{tool}** ({acoustics}).\n\n"
        f"Why is the **sound energy** generated by this machine classified strictly as a **wasted output**?"
    )
    correct = (
        "Because acoustic sound waves consume a portion of the input electrical energy without contributing to the intended task, "
        "dissipating uselessly into the surrounding air."
    )
    distractors = [
        "Because sound waves are poisonous gases that suffocate the machine operator.",
        "Because sound destroys the electrical cords through magnetic vibration.",
        "Because sound cools down the machine until its internal motor freezes.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Sound as Wasted Energy in Machinery:**\n"
        f"- The intended task requires mechanical work (e.g. breaking asphalt or suctioning dirt).\n"
        f"- Rapid vibrations and turbulent airflow generate pressure waves in air (**sound energy**).\n"
        f"- Producing sound requires energy from the input source, yet sound performs no cleaning or drilling work; hence it is 100% wasted."
    )
    return {
        "id": f"ns7_et_28_{rng.randint(100000, 999999)}",
        "subskill": "28_sound_energy_as_wasted_mechanical_vibration",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_28",
        "hints": {
            "tier_1": "Does the noise from a vacuum cleaner or jackhammer do any actual work?",
            "tier_2": "Noise consumes energy without helping the machine do its job.",
            "tier_3": "Sound waves consume input energy without contributing to the intended task.",
        },
        "misconception_tags": ["louder_machines_are_always_doing_more_useful_work", "sound_costs_zero_energy"],
    }


# 29. Electrical resistance heating in conductors
def arch_29_electrical_resistance_heating_in_conductors(rng: random.Random) -> Dict[str, Any]:
    cables = [
        ("a thin extension cord carrying heavy electrical current to an electric heater", "the cord feels noticeably warm to the touch"),
        ("long-distance high-voltage power transmission cables stretching across the Karoo", "a small percentage of grid power is lost as thermal heat along the wires"),
    ]
    cable_type, symptom = rng.choice(cables)
    prompt = (
        f"When electric current flows through conductors, **{cable_type}** ({symptom}).\n\n"
        f"What physical phenomenon explains why electrical energy is converted into wasted thermal energy inside wires?"
    )
    correct = (
        "**Electrical resistance:** Moving electrons collide with stationary metal ions in the conductor's wire lattice, "
        "transferring kinetic energy into atomic vibrations that dissipate as heat (Joule heating)."
    )
    distractors = [
        "**Nuclear decay:** Copper wire atoms spontaneously split into hydrogen gas bubbles.",
        "**Gravitational friction:** Earth's magnetic core pulls the wires down into the soil.",
        "**Photonic refraction:** Sunlight entering the wires turns into solid carbon soot.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Electrical Resistance Heating (Joule Heating):**\n"
        f"- Metal conductors contain a lattice of positive metal ions.\n"
        f"- When an electric potential difference pushes electrons, they collide with lattice ions.\n"
        f"- Each collision transfers kinetic energy to lattice vibrations, observed macroscopically as **thermal heat** (\\(P = I^2R\\))."
    )
    return {
        "id": f"ns7_et_29_{rng.randint(100000, 999999)}",
        "subskill": "29_electrical_resistance_heating_in_conductors",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_29",
        "hints": {
            "tier_1": "What opposes the flow of electrons inside a metal wire?",
            "tier_2": "Electrical resistance causes moving electrons to collide with ions, creating heat.",
            "tier_3": "Electrical resistance: moving electrons collide with metal ions, dissipating heat.",
        },
        "misconception_tags": ["wires_have_zero_resistance", "current_disappears_inside_wires"],
    }


# 30. Improving car aerodynamics to reduce waste
def arch_30_improving_car_aerodynamics_to_reduce_waste(rng: random.Random) -> Dict[str, Any]:
    vehicles = [
        ("a streamlined passenger car with smooth, curved contours", "a boxy cargo delivery van with flat vertical surfaces", 100),
        ("a teardrop-shaped electric vehicle", "a flat-nosed transport truck", 120),
    ]
    streamlined, boxy, speed = rng.choice(vehicles)
    prompt = (
        f"Automotive engineers design **{streamlined}** rather than **{boxy}** for highway driving at **{speed} km/h**.\n\n"
        f"How does an **aerodynamic streamlined shape** reduce energy waste to the surroundings?"
    )
    correct = (
        "It allows air to flow smoothly around the vehicle body with minimal turbulence, "
        "drastically reducing air resistance (drag) and lowering the fuel energy wasted pushing air aside."
    )
    distractors = [
        "It eliminates Earth's gravitational pull on the vehicle, allowing it to glide weightlessly.",
        "It prevents the car engine from needing any coolant or radiator fluid.",
        "It generates free petrol inside the fuel tank through air compression.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Aerodynamic Efficiency in Transport:**\n"
        f"- At highway speeds ({speed} km/h), more than half of a car's engine power is spent overcoming **aerodynamic drag**.\n"
        f"- Boxy vehicles push large air masses, creating turbulent low-pressure wakes that pull backward on the vehicle.\n"
        f"- Streamlining smooths airflow, minimizing turbulent energy dissipation and conserving fuel."
    )
    return {
        "id": f"ns7_et_30_{rng.randint(100000, 999999)}",
        "subskill": "30_improving_car_aerodynamics_to_reduce_waste",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_30",
        "hints": {
            "tier_1": "Think about why airplanes and racing cars are sleek and curved.",
            "tier_2": "Curved shapes slice through air smoothly, reducing air drag (air resistance).",
            "tier_3": "Allows air to flow smoothly with minimal turbulence, reducing drag and fuel waste.",
        },
        "misconception_tags": ["air_resistance_has_zero_energy_cost", "aerodynamics_is_only_for_looks"],
    }


# 31. Household energy audit appliance waste
def arch_31_household_energy_audit_appliance_waste(rng: random.Random) -> Dict[str, Any]:
    appliances = [
        ("an uninsulated electric storage water heater (geyser) running continuously at 75 °C",
         "standing heat loss through the uninsulated metal tank wall wastes 30% to 40% of its electricity directly into the roof ceiling space"),
        ("an oven with a damaged rubber door seal",
         "hot air continuously escapes into the kitchen, forcing the heating element to draw far more electricity to maintain baking temperature"),
    ]
    device, waste_path = rng.choice(appliances)
    prompt = (
        f"During a home energy audit, a technician examines **{device}**.\n\n"
        f"Why does this appliance represent a major source of wasted household electrical energy?"
    )
    correct = f"Because {waste_path}."
    distractors = [
        "Because it transforms household water pipes into solid carbon rocks.",
        "Because it drains the magnetic field lines surrounding the neighborhood.",
        "Because it causes electricity to evaporate through open glass windows.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Household Thermal Energy Audit:**\n"
        f"- Heating devices consume the largest share of household electricity (up to 40-50%).\n"
        f"- In {device}, {waste_path}.\n"
        f"- Solutions: Fit a geyser blanket, lower thermostat to 55-60 °C, and replace worn oven door seals."
    )
    return {
        "id": f"ns7_et_31_{rng.randint(100000, 999999)}",
        "subskill": "31_household_energy_audit_appliance_waste",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_31",
        "hints": {
            "tier_1": "What happens to heat in a geyser or oven when insulation is poor?",
            "tier_2": "Heat escapes to the surroundings, wasting electricity.",
            "tier_3": f"Because {waste_path}.",
        },
        "misconception_tags": ["geysers_lose_zero_heat_when_unused", "damaged_seals_have_no_energy_cost"],
    }


# 32. Standby power vampire energy waste
def arch_32_standby_power_vampire_energy_waste(rng: random.Random) -> Dict[str, Any]:
    appliances = [
        ("televisions, microwave clock displays, and game consoles left plugged in on 'standby' mode",
         "internal power transformers and remote sensors continuously draw 5 W to 15 W of 'vampire' electrical power 24/7"),
        ("laptop and cell phone chargers left plugged into wall sockets without devices attached",
         "internal step-down transformers continue to consume a small continuous current that dissipates as warm idle heat"),
    ]
    app, description = rng.choice(appliances)
    prompt = (
        f"Many households leave **{app}**.\n\n"
        f"What is **standby power ('vampire power')**, and why is it considered an unnecessary waste of energy?"
    )
    correct = (
        f"It is electricity consumed by electronic devices while turned off or idle ({description}), "
        "generating wasted heat without providing active useful service."
    )
    distractors = [
        "It is electricity stolen by bats roosting in roof gutters.",
        "It is power that reverses into wall plugs and spins the municipal meter backwards.",
        "It is static electricity generated by walking across nylon carpets.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Vampire / Standby Power:**\n"
        f"- Electronic appliances with digital clocks, standby lights, and remote control receivers remain partially energized.\n"
        f"- {description.capitalize()}.\n"
        f"- Cumulatively, standby power can account for **5% to 10%** of an entire household's monthly electricity bill with zero useful output."
    )
    return {
        "id": f"ns7_et_32_{rng.randint(100000, 999999)}",
        "subskill": "32_standby_power_vampire_energy_waste",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_32",
        "hints": {
            "tier_1": "Do devices with clocks and standby lights draw power when you aren't using them?",
            "tier_2": "Standby devices draw idle power continuously, wasting energy as heat.",
            "tier_3": "Electricity consumed while turned off or idle, generating wasted heat without useful service.",
        },
        "misconception_tags": ["standby_mode_uses_zero_watts", "unplugging_appliances_has_no_effect"],
    }


# 33. Economic consequences of wasted energy
def arch_33_economic_consequences_of_wasted_energy(rng: random.Random) -> Dict[str, Any]:
    costs = [(2.50, 400, 1000), (3.00, 500, 1500)]
    rate_r, kwh_wasted, r_total = rng.choice(costs)
    prompt = (
        f"If a South African household wastes **{kwh_wasted} kWh** of electricity per month through inefficient appliances, "
        f"leaky geyser insulation, and incandescent bulbs, at a municipal tariff of **R{rate_r:.2f} per kWh**:\n\n"
        f"What is the direct economic cost to the family, and what does this illustrate?"
    )
    correct = (
        f"The family pays **R{r_total:.2f}** per month strictly for energy that escaped as wasted heat into the air, "
        "demonstrating that energy waste directly inflates household living expenses."
    )
    distractors = [
        "The municipality pays the family a bonus for heating the outdoor atmosphere.",
        "The electricity bill drops to zero because wasted energy is exempt from municipal billing.",
        "The family receives free solar panels automatically from the electricity meter.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Economic Impact of Energy Waste:**\n"
        f"$$\\text{{Financial Loss}} = {kwh_wasted}\\text{{ kWh}} \\times \\text{{R}}{rate_r:.2f}/\\text{{kWh}} = \\mathbf{{\\text{{R}}{r_total:.2f}}}$$\n"
        f"Every wasted kilowatt-hour is registered by the electricity meter and billed to the consumer. Energy efficiency directly saves money."
    )
    return {
        "id": f"ns7_et_33_{rng.randint(100000, 999999)}",
        "subskill": "33_economic_consequences_of_wasted_energy",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_33",
        "hints": {
            "tier_1": f"Multiply {kwh_wasted} kWh by R{rate_r:.2f}.",
            "tier_2": f"{kwh_wasted} x {rate_r:.2f} = R{r_total:.2f}.",
            "tier_3": f"The family pays R{r_total:.2f} per month for energy wasted to the air.",
        },
        "misconception_tags": ["wasted_energy_is_free", "meters_only_bill_useful_energy"],
    }


# 34. Environmental cost of power plant waste
def arch_34_environmental_cost_of_power_plant_waste(rng: random.Random) -> Dict[str, Any]:
    prompts = [
        ("coal-fired thermal power stations", "carbon dioxide (\\(\\text{{CO}}_2\\)), sulfur dioxide (\\(\\text{{SO}}_2\\)), and particulate fly ash")
    ]
    plant, emissions = rng.choice(prompts)
    prompt = (
        f"In South Africa, most grid electricity is produced by **{plant}**.\n\n"
        f"Why does wasting electrical energy in homes and businesses directly harm the natural environment?"
    )
    correct = (
        f"Because generating wasted electricity requires burning additional coal, releasing more {emissions}, "
        "intensifying global warming, air pollution, and acid rain."
    )
    distractors = [
        "Because wasted electricity travels into rivers and electrocutes freshwater fish.",
        "Because wasting electricity causes the Moon to pull away from Earth's orbit.",
        "Because electrical appliances suck natural rainfall out of rain clouds.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Environmental Connection:**\n"
        f"- To supply wasted electricity, power stations must combust additional tonnes of coal.\n"
        f"- Burning coal releases {emissions}.\n"
        f"- Therefore, conserving energy at the point of use directly reduces carbon emissions and fossil fuel mining at the source."
    )
    return {
        "id": f"ns7_et_34_{rng.randint(100000, 999999)}",
        "subskill": "34_environmental_cost_of_power_plant_waste",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_34",
        "hints": {
            "tier_1": "Where does the electricity come from? Burning coal at power stations.",
            "tier_2": "Wasting electricity means burning more coal and releasing more pollutants.",
            "tier_3": f"Generating wasted electricity burns more coal, releasing more {emissions}.",
        },
        "misconception_tags": ["electricity_waste_has_no_smokestack_impact", "power_stations_generate_only_on_demand_cleanly"],
    }


# 35. Sankey diagram for electric motor
def arch_35_sankey_diagram_for_electric_motor(rng: random.Random) -> Dict[str, Any]:
    motors = [(1000, 800, 150, 50, "Kinetic energy (spinning shaft)", "Thermal heat in windings", "Acoustic noise")]
    input_j, useful_j, heat_j, sound_j, useful_l, heat_l, sound_l = rng.choice(motors)
    prompt = (
        f"In an energy flow accounting for an industrial **electric motor**:\n"
        f"- Total Electrical Input: **{input_j} J**\n"
        f"- Output A: **{useful_j} J** ({useful_l})\n"
        f"- Output B: **{heat_j} J** ({heat_l})\n"
        f"- Output C: **{sound_j} J** ({sound_l})\n\n"
        f"What is the **efficiency percentage** of this motor, and which outputs are considered **wasted**?"
    )
    eff = int((useful_j / input_j) * 100)
    wasted_total = heat_j + sound_j
    correct = f"Efficiency: **{eff}%** | Wasted outputs: Outputs B and C combined ({wasted_total} J of heat and sound)."
    distractors = [
        f"Efficiency: **{100 - eff}%** | Wasted outputs: Output A only ({useful_j} J).",
        f"Efficiency: **100%** | Wasted outputs: Zero energy.",
        f"Efficiency: **{eff / 2}%** | Wasted outputs: Output B only.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Electric Motor Energy Accounting:**\n"
        f"- Useful Output = {useful_j} J ({useful_l}).\n"
        f"- Wasted Outputs = {heat_j} J + {sound_j} J = {wasted_total} J.\n"
        f"- Efficiency: \\(\\frac{{{useful_j}}}{{{input_j}}} \\times 100\\% = \\mathbf{{{eff}\\%}}\\).\n"
        f"- Both heat and sound do not perform useful shaft rotation and are wasted to surroundings."
    )
    return {
        "id": f"ns7_et_35_{rng.randint(100000, 999999)}",
        "subskill": "35_sankey_diagram_for_electric_motor",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_35",
        "hints": {
            "tier_1": f"Useful is {useful_j} J out of {input_j} J. What percentage is that?",
            "tier_2": f"{useful_j} / {input_j} = {eff}%. Heat and sound are wasted.",
            "tier_3": f"Efficiency: {eff}% | Wasted: Outputs B and C combined ({wasted_total} J).",
        },
        "misconception_tags": ["sound_is_useful_in_motors", "efficiency_includes_heat"],
    }


# 36. Sankey diagram for coal power station
def arch_36_sankey_diagram_for_coal_power_station(rng: random.Random) -> Dict[str, Any]:
    balances = [(100, 35, 65, "Kendal Power Station"), (1000, 340, 660, "Medupi Power Station")]
    chem_in, elec_out, waste_heat, stn = rng.choice(balances)
    prompt = (
        f"At **{stn}**, coal is burned to generate grid electricity.\n"
        f"For every **{chem_in} units** of chemical energy in coal:\n"
        f"- **{elec_out} units** leave as useful electrical energy on transmission lines.\n"
        f"- **{waste_heat} units** leave as thermal energy through cooling towers, flue gases, and ash.\n\n"
        f"What is the thermal efficiency of this power station, and what happens to the remaining energy?"
    )
    eff_pct = int((elec_out / chem_in) * 100)
    correct = f"Thermal efficiency is **{eff_pct}%**; the remaining {waste_heat} units are dissipated as wasted heat into cooling water and the atmosphere."
    distractors = [
        f"Thermal efficiency is **{100 - eff_pct}%**; electricity is the wasted output.",
        "Thermal efficiency is **100%** because power stations cannot lose heat.",
        "Thermal efficiency is **10%**; all energy turns into dark coal dust.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Thermal Power Station Efficiency:**\n"
        f"- Efficiency: \\(\\frac{{{elec_out}}}{{{chem_in}}} \\times 100\\% = \\mathbf{{{eff_pct}\\%}}\\).\n"
        f"- Due to fundamental thermodynamic limits of steam turbine cycles (Carnot limit), roughly two-thirds ({waste_heat} units) cannot be converted into work and is dissipated as warm water vapor in cooling towers and flue exhaust."
    )
    return {
        "id": f"ns7_et_36_{rng.randint(100000, 999999)}",
        "subskill": "36_sankey_diagram_for_coal_power_station",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_36",
        "hints": {
            "tier_1": f"Divide {elec_out} by {chem_in} to find efficiency.",
            "tier_2": f"Thermal efficiency is {eff_pct}%. The rest is lost as heat in cooling towers.",
            "tier_3": f"Thermal efficiency is {eff_pct}%; remaining {waste_heat} units are dissipated as wasted heat.",
        },
        "misconception_tags": ["power_stations_have_100_percent_efficiency", "cooling_towers_generate_electricity"],
    }


# 37. Thermal insulation to trap useful heat
def arch_37_thermal_insulation_to_trap_useful_heat(rng: random.Random) -> Dict[str, Any]:
    methods = [
        ("wrapping an electric geyser in a thick fiberglass insulation blanket", "drastically slows conductive heat loss from hot water through the metal tank to attic air"),
        ("installing double-pane glazed windows and thermal curtains", "reduces conductive and convective heat transfer from warm rooms to cold winter night air"),
    ]
    method, mechanism = rng.choice(methods)
    prompt = (
        f"Households implement energy-saving upgrades such as **{method}**.\n\n"
        f"How does **thermal insulation** improve energy efficiency?"
    )
    correct = f"It acts as a poor thermal conductor ({mechanism}), reducing the rate of wasted heat transfer to the surroundings."
    distractors = [
        "It generates fresh heat continuously without using any electrical power.",
        "It eliminates all atmospheric gravity around the hot water cylinder.",
        "It turns escaping heat into chemical fuel that flows back into the plug.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Insulation and Heat Transfer Reduction:**\n"
        f"- Insulators contain trapped pockets of air (which is a poor conductor of heat).\n"
        f"- By {mechanism}, useful thermal energy remains inside the intended system for longer.\n"
        f"- Consequently, less electrical energy is needed to keep the system at desired operating temperature."
    )
    return {
        "id": f"ns7_et_37_{rng.randint(100000, 999999)}",
        "subskill": "37_thermal_insulation_to_trap_useful_heat",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_37",
        "hints": {
            "tier_1": "What does a blanket do on a cold bed or hot water tank?",
            "tier_2": "Insulation slows down heat escaping to the cooler room.",
            "tier_3": f"Poor thermal conductor ({mechanism}), reducing wasted heat transfer.",
        },
        "misconception_tags": ["insulation_creates_heat", "insulators_are_100_percent_perfect_forever"],
    }


# 38. Comparison of cooling technologies
def arch_38_comparison_of_cooling_technologies(rng: random.Random) -> Dict[str, Any]:
    climates = [
        ("the hot, dry Northern Cape (Upington)", "Evaporative swamp cooler", "Refrigerant compressor air conditioner", "uses simple water evaporation with an 80% smaller electrical motor, avoiding heavy compressor energy waste"),
        ("a Karoo town in summer", "Evaporative cooler", "Refrigerant split-unit AC", "exploits low relative humidity to cool air by latent heat of evaporation, using far less grid electricity"),
    ]
    region, tech_a, tech_b, reason = rng.choice(climates)
    prompt = (
        f"In **{region}**, residents choose between a **{tech_a}** and a **{tech_b}**.\n\n"
        f"Why is the {tech_a} substantially more energy-efficient and less wasteful in this specific climate?"
    )
    correct = f"Because it {reason}."
    distractors = [
        "Because it freezes air using liquid uranium rods.",
        "Because it operates without consuming any water or electricity.",
        "Because it blows hot air into the ground to melt limestone.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Cooling Efficiency in Arid Climates:**\n"
        f"- In dry climates with low humidity, water absorbs heat as it evaporates (latent heat of vaporization).\n"
        f"- An evaporative cooler only needs to run a small water pump and a fan ({reason}).\n"
        f"- A compressor air conditioner must compress chemical refrigerants at high electrical power, expelling massive wasted heat outside."
    )
    return {
        "id": f"ns7_et_38_{rng.randint(100000, 999999)}",
        "subskill": "38_comparison_of_cooling_technologies",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_38",
        "hints": {
            "tier_1": "Think about evaporating water in dry desert heat.",
            "tier_2": "Evaporative coolers use water evaporation and a small fan, using much less power than a heavy compressor.",
            "tier_3": f"Because it {reason}.",
        },
        "misconception_tags": ["all_air_conditioners_are_identical", "evaporative_cooling_works_in_humid_durban"],
    }


# 39. Blender chopping food energy flow
def arch_39_blender_chopping_food_energy_flow(rng: random.Random) -> Dict[str, Any]:
    foods = [("chopping carrots and blending fruit into a smoothie", "kinetic cutting and shearing of food molecules")]
    task, useful_desc = rng.choice(foods)
    prompt = (
        f"A cook operates an electric kitchen blender for **{task}**.\n"
        f"After two minutes of blending, the glass jug feels warm and the kitchen is filled with loud whirring noise.\n\n"
        f"Which statement correctly accounts for the energy pathways in this system?"
    )
    correct = (
        f"Useful output: {useful_desc}.\n"
        "Wasted outputs: thermal energy (heat from electric motor resistance, blade friction, and fluid viscous friction) "
        "and sound energy (motor whining and blade impact noise)."
    )
    distractors = [
        "Useful output: sound energy to indicate blending.\nWasted output: all kinetic motion.",
        "Useful output: chemical energy in plastic lid.\nWasted output: pure light rays.",
        "Useful output: gravitational potential energy.\nWasted output: nuclear decay.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Blender Energy Accounting:**\n"
        f"- **Input:** Electrical energy.\n"
        f"- **Useful:** Kinetic energy ({useful_desc}).\n"
        f"- **Wasted:** Fluid shearing and motor bearings generate **thermal heat** (warming the soup/smoothie and motor housing); gear vibration produces **sound noise**."
    )
    return {
        "id": f"ns7_et_39_{rng.randint(100000, 999999)}",
        "subskill": "39_blender_chopping_food_energy_flow",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_39",
        "hints": {
            "tier_1": "What is the blender supposed to do? Cut and blend food.",
            "tier_2": "Kinetic chopping is useful; warmth in the soup and loud whining noise are wasted.",
            "tier_3": f"Useful: {useful_desc}; Wasted: thermal friction and sound.",
        },
        "misconception_tags": ["blenders_cool_down_food", "blender_noise_helps_puree_food"],
    }


# 40. Vacuum cleaner energy transfers
def arch_40_vacuum_cleaner_energy_transfers(rng: random.Random) -> Dict[str, Any]:
    ratings = [(1200, 400, 800, "an electric canister vacuum cleaner")]
    input_w, useful_w, wasted_w, device = rng.choice(ratings)
    prompt = (
        f"In **{device}** consuming **{input_w} W** of electrical power:\n"
        f"- **{useful_w} W** goes into kinetic air movement creating suction to lift dirt.\n"
        f"- **{wasted_w} W** is dissipated into the room.\n\n"
        f"In what forms does the {wasted_w} W of wasted energy escape into the surroundings?"
    )
    correct = "As high thermal energy (exhaust air and motor heating) and high-decibel acoustic sound noise."
    distractors = [
        "As radioactive alpha and beta particles.",
        "As gravitational waves that increase the weight of the carpet.",
        "As visible laser beams that disinfect the room.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Vacuum Cleaner Dissipation:**\n"
        f"- Useful power = {useful_w} W (fan creates low pressure / suction airflow).\n"
        f"- Wasted power = {wasted_w} W ({wasted_w/input_w*100:.0f}% of total power!).\n"
        f"- Air passing through the motor absorbs friction and electrical heat, exiting as warm exhaust; fan turbulence creates loud acoustic noise."
    )
    return {
        "id": f"ns7_et_40_{rng.randint(100000, 999999)}",
        "subskill": "40_vacuum_cleaner_energy_transfers",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_40",
        "hints": {
            "tier_1": "Feel the air blowing out of a vacuum cleaner: is it warm or cold?",
            "tier_2": "The air blowing out is hot, and the vacuum is loud (heat and sound).",
            "tier_3": "High thermal energy (warm exhaust air and motor heat) and sound noise.",
        },
        "misconception_tags": ["vacuums_destroy_dirt_atoms", "suction_requires_all_1200_w"],
    }


# 41. Smartphone battery drain and heating
def arch_41_smartphone_battery_drain_and_heating(rng: random.Random) -> Dict[str, Any]:
    apps = [("playing a high-intensity 3D video game on a smartphone", "processor chips draw high electrical current, causing electrical resistance heating")]
    activity, cause = rng.choice(apps)
    prompt = (
        f"While **{activity}**, the back of the phone becomes very hot and the battery level drops rapidly.\n\n"
        f"From an energy transfer perspective, why does the phone get hot?"
    )
    correct = f"Because {cause}; electrical energy is wasted as thermal heat dissipated to the user's hand and surrounding air."
    distractors = [
        "Because the battery is burning liquid fuel with open flames inside the phone.",
        "Because radio waves from the cell phone tower are turning into molten lava.",
        "Because the smartphone is absorbing gravitational weight from the earth.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Smartphone Energy Transfer:**\n"
        f"- **Input:** Chemical potential energy from lithium-ion battery -> Electrical current.\n"
        f"- **Useful:** Radiant light on display screen, sound from speakers, computation in silicon CPU/GPU.\n"
        f"- **Wasted:** Electrical resistance across billions of microscopic transistors converts current into **thermal heat** ({cause})."
    )
    return {
        "id": f"ns7_et_41_{rng.randint(100000, 999999)}",
        "subskill": "41_smartphone_battery_drain_and_heating",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_41",
        "hints": {
            "tier_1": "What happens when heavy current flows through microchips?",
            "tier_2": "Resistance converts electrical energy into wasted heat.",
            "tier_3": f"Because {cause}; electrical energy is wasted as thermal heat.",
        },
        "misconception_tags": ["smartphones_store_heat", "warm_phones_are_charging"],
    }


# 42. Washing machine spin cycle balance
def arch_42_washing_machine_spin_cycle_balance(rng: random.Random) -> Dict[str, Any]:
    cycles = [("an automatic washing machine during its high-speed 1 200 rpm spin cycle", "kinetic centrifugal rotation forcing water droplets out of wet clothing fibers")]
    cycle_desc, useful_desc = rng.choice(cycles)
    prompt = (
        f"Consider **{cycle_desc}**.\n\n"
        f"What is the **useful energy output**, and what are the **wasted energy outputs** during the spin cycle?"
    )
    correct = (
        f"Useful output: {useful_desc}.\n"
        "Wasted outputs: mechanical vibration noise (sound), motor heat, and friction between rotating drum bearings."
    )
    distractors = [
        "Useful output: violent rattling noise to alert the household.\nWasted output: drum rotation.",
        "Useful output: chemical energy in laundry detergent.\nWasted output: pure electricity.",
        "Useful output: gravitational potential energy.\nWasted output: cold air.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Washing Machine Spin Cycle:**\n"
        f"- **Input:** Electrical energy.\n"
        f"- **Useful:** Mechanical kinetic rotation ({useful_desc}).\n"
        f"- **Wasted:** Loud vibrations and hum (**sound energy**) and bearing/belt friction (**thermal energy**)."
    )
    return {
        "id": f"ns7_et_42_{rng.randint(100000, 999999)}",
        "subskill": "42_washing_machine_spin_cycle_balance",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_42",
        "hints": {
            "tier_1": "What is the purpose of the spin cycle? Spinning to extract water.",
            "tier_2": "Drum rotation is useful; shaking noise and motor heat are wasted.",
            "tier_3": f"Useful: {useful_desc}; Wasted: vibration sound, motor heat, and bearing friction.",
        },
        "misconception_tags": ["spin_cycle_dries_clothes_by_boiling", "vibrations_are_useful_energy"],
    }


# 43. Energy star rating labels interpretation
def arch_43_energy_star_rating_labels_interpretation(rng: random.Random) -> Dict[str, Any]:
    labels = [
        ("an appliance with an 'A+++' energy rating label vs an identical-capacity appliance with a 'D' energy rating label",
         "The 'A+++' appliance converts a much higher percentage of electricity into useful work and wastes far less energy as heat, saving substantial electricity costs over its lifespan.")
    ]
    scenario, explanation = rng.choice(labels)
    prompt = (
        f"In South African retail appliance stores, refrigerators and washing machines display standard **Energy Efficiency Rating Labels** (A+++ to G).\n\n"
        f"Consider **{scenario}**.\n"
        f"What does this rating comparison indicate to the consumer?"
    )
    correct = explanation
    distractors = [
        "The 'D' appliance is three times faster and produces free electricity for the home.",
        "Both appliances use identical amounts of electricity under all conditions.",
        "The rating refers only to the musical sound quality of the appliance chime.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Interpreting Energy Efficiency Labels:**\n"
        f"- Standard labels rank appliances by their specific energy consumption per unit of performance.\n"
        f"- 'A+++' is the highest efficiency class: modern insulation, efficient compressors, low wasted heat.\n"
        f"- 'D' or lower wastes significantly more electrical energy to surroundings as heat, increasing municipal electric bills."
    )
    return {
        "id": f"ns7_et_43_{rng.randint(100000, 999999)}",
        "subskill": "43_energy_star_rating_labels_interpretation",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_43",
        "hints": {
            "tier_1": "Is 'A+++' or 'D' better for saving electricity?",
            "tier_2": "A+++ is top-tier efficiency; it converts more electricity to useful work with minimal waste.",
            "tier_3": f"{explanation}",
        },
        "misconception_tags": ["energy_labels_are_for_safety_only", "d_rating_means_durable"],
    }


# 44. Misconception wasted energy is destroyed
def arch_44_misconception_wasted_energy_is_destroyed(rng: random.Random) -> Dict[str, Any]:
    claims = [
        ("When a light bulb shines, a learner thinks the wasted 90% heat energy disappears forever into nothing.",
         "The heat energy is not destroyed; it is transferred to the surrounding air molecules by conduction, convection, and infrared radiation, slightly warming the room.")
    ]
    myth, truth = rng.choice(claims)
    prompt = (
        f"Consider this student statement:\n*{myth}*\n\n"
        f"How does the Law of Conservation of Energy correct this misconception?"
    )
    correct = truth
    distractors = [
        "The statement is correct because wasted energy ceases to exist in the universe.",
        "The wasted heat turns into gold coins inside the electrical socket.",
        "The heat energy reverses time to become chemical fuel again automatically.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Conservation Law vs 'Disappearance' Myth:**\n"
        f"- Energy can never be created or destroyed (First Law of Thermodynamics).\n"
        f"- 'Wasted' does not mean annihilated.\n"
        f"- {truth}"
    )
    return {
        "id": f"ns7_et_44_{rng.randint(100000, 999999)}",
        "subskill": "44_misconception_wasted_energy_is_destroyed",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_44",
        "hints": {
            "tier_1": "Can energy ever be destroyed?",
            "tier_2": "No, energy is conserved. Wasted heat simply warms up the surrounding room air.",
            "tier_3": f"{truth}",
        },
        "misconception_tags": ["wasted_energy_is_destroyed", "heat_escapes_to_parallel_dimensions"],
    }


# 45. Misconception sound is useful in appliances
def arch_45_misconception_sound_is_useful_in_appliances(rng: random.Random) -> Dict[str, Any]:
    tools = [
        ("an electric lawnmower", "cutting grass blades cleanly"),
        ("an electric blender", "crushing and blending food ingredients"),
        ("a power drill", "boring holes through timber or masonry"),
    ]
    app, task = rng.choice(tools)
    prompt = (
        f"A student argues: *\"The loud noise made by {app} is useful because it lets me know that the machine is on and working.\"*\n\n"
        f"Why is this argument scientifically flawed when classifying energy outputs?"
    )
    correct = (
        f"The primary engineering purpose of the machine is to {task}; the acoustic sound waves do no work toward that task, "
        "and any electrical energy converted into sound reduces overall efficiency."
    )
    distractors = [
        "Because sound energy creates cold gravity that damages the lawn.",
        "Because sound destroys the electrical plug connections in the wall.",
        "Because the student is completely correct and sound is 100% of the useful work.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Classifying Useful vs Incidental Output:**\n"
        f"- The intended useful output of {app} is **kinetic energy** ({task}).\n"
        f"- While humans may hear the noise, sound is an **unavoidable byproduct of vibration and friction**.\n"
        f"- Every Joule of sound generated is a Joule stolen from doing the actual job."
    )
    return {
        "id": f"ns7_et_45_{rng.randint(100000, 999999)}",
        "subskill": "45_misconception_sound_is_useful_in_appliances",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_45",
        "hints": {
            "tier_1": "Does the noise from the motor cut grass or drill holes?",
            "tier_2": "Noise does not perform the machine's intended function; it is wasted vibration.",
            "tier_3": f"Sound does no work toward {task}, reducing overall efficiency.",
        },
        "misconception_tags": ["incidental_signals_are_useful_energy", "noise_performs_mechanical_work"],
    }


# 46. Misconception 100 percent efficient machine
def arch_46_misconception_100_percent_efficient_machine(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "An inventor claims to have built a mechanical machine that operates with **100% efficiency**, "
        "producing zero wasted heat or sound to the surroundings.\n\n"
        "Why does modern physics reject the possibility of a 100% efficient macroscopic mechanical machine?"
    )
    correct = (
        "In all real-world mechanical systems, friction between moving surfaces and air drag are unavoidable, "
        "always dissipating some portion of input energy as thermal heat and sound."
    )
    distractors = [
        "Because international patent laws forbid machines with even numbers.",
        "Because gravity naturally absorbs 50% of all machine power everywhere.",
        "Because 100% efficient machines require dark matter fuel from the Moon.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Impossibility of 100% Mechanical Efficiency:**\n"
        f"- Second Law of Thermodynamics: In any real physical process, some energy is inevitably degraded into dispersed thermal heat.\n"
        f"- Friction in bearings, gear meshing, air drag, and electrical resistance cannot be completely eliminated in macroscopic systems.\n"
        f"- Therefore, \\(\\text{{Efficiency}} < 100\\%\\) for all real mechanical machines."
    )
    return {
        "id": f"ns7_et_46_{rng.randint(100000, 999999)}",
        "subskill": "46_misconception_100_percent_efficient_machine",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_46",
        "hints": {
            "tier_1": "Can you ever eliminate friction and air resistance completely?",
            "tier_2": "Friction and resistance always convert some energy into wasted heat and sound.",
            "tier_3": "Friction and air drag are unavoidable, always dissipating some energy as heat and sound.",
        },
        "misconception_tags": ["perpetual_motion_machines_exist", "frictionless_ideal_machines_are_common"],
    }


# 47. Misconception heat is always wasted
def arch_47_misconception_heat_is_always_wasted(rng: random.Random) -> Dict[str, Any]:
    devices = [
        ("an electric geyser heating bathwater", "an electric iron pressing clothes", "thermal energy (heat) IS the primary intended useful output"),
        ("an electric toaster crisping bread", "a domestic room heater", "heat IS the desired useful output that fulfills the appliance's function"),
    ]
    dev1, dev2, role = rng.choice(devices)
    prompt = (
        f"A learner says: *\"Thermal energy (heat) is ALWAYS a wasted form of energy in every electrical system.\"*\n\n"
        f"How do **{dev1}** and **{dev2}** disprove this statement?"
    )
    correct = f"In these heating appliances, {role}; heat is only 'wasted' when it is an unwanted byproduct of devices meant for light or motion."
    distractors = [
        "They prove that hot water is actually a form of cold kinetic energy.",
        "They show that irons produce 100% visible light to flatten shirts.",
        "They confirm that geysers operate exclusively through nuclear sound waves.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Context-Dependent Classification of Energy:**\n"
        f"- Whether an energy form is 'useful' or 'wasted' depends entirely on the **intended function** of the system.\n"
        f"- In lamps and fans: heat is an unwanted byproduct (wasted).\n"
        f"- In {dev1} and {dev2}: **{role}**."
    )
    return {
        "id": f"ns7_et_47_{rng.randint(100000, 999999)}",
        "subskill": "47_misconception_heat_is_always_wasted",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_47",
        "hints": {
            "tier_1": "What is an iron or geyser supposed to produce? Heat!",
            "tier_2": "In heaters and geysers, heat is the useful output.",
            "tier_3": f"In heating appliances, {role}.",
        },
        "misconception_tags": ["heat_is_always_wasted", "useful_energy_can_only_be_kinetic"],
    }


# 48. Calculating efficiency from fuel joules
def arch_48_calculating_efficiency_from_fuel_joules(rng: random.Random) -> Dict[str, Any]:
    scenarios = [(2000, 400, 20), (5000, 1250, 25), (4000, 1200, 30), (3000, 900, 30)]
    input_kj, useful_kj, pct = rng.choice(scenarios)
    prompt = (
        f"A diesel generator consumes **{input_kj} kJ** of chemical potential energy from fuel.\n"
        f"It successfully outputs **{useful_kj} kJ** of useful electrical energy onto a building's power circuits.\n\n"
        f"Calculate the **energy efficiency percentage** of this generator."
    )
    correct = f"**{pct}%**, calculated as \\(\\frac{{{useful_kj}\\text{{ kJ}}}}{{{input_kj}\\text{{ kJ}}}} \\times 100\\%\\)."
    distractors = [
        f"**{pct * 2}%**, by doubling the useful output.",
        f"**{100 - pct}%**, by calculating the wasted heat percentage.",
        f"**{pct / 2}%**, by halving the efficiency.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Generator Efficiency Calculation:**\n"
        f"$$\\text{{Efficiency}} = \\left(\\frac{{\\text{{Useful Electrical Output}}}}{{\\text{{Total Chemical Input}}}}\\right) \\times 100\\%$$\n"
        f"$$\\text{{Efficiency}} = \\left(\\frac{{{useful_kj}\\text{{ kJ}}}}{{{input_kj}\\text{{ kJ}}}}\\right) \\times 100\\% = \\mathbf{{{pct}\\%}}$$\n"
        f"The remaining {input_kj - useful_kj} kJ ({100 - pct}%) is wasted as engine heat and exhaust to surroundings."
    )
    return {
        "id": f"ns7_et_48_{rng.randint(100000, 999999)}",
        "subskill": "48_calculating_efficiency_from_fuel_joules",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_48",
        "hints": {
            "tier_1": f"Divide {useful_kj} by {input_kj} and multiply by 100.",
            "tier_2": f"({useful_kj} / {input_kj}) x 100 = {pct}%.",
            "tier_3": f"{pct}%.",
        },
        "misconception_tags": ["efficiency_calculation_inverted", "subtracting_instead_of_dividing"],
    }


# 49. Designing a more efficient system challenge
def arch_49_designing_a_more_efficient_system_challenge(rng: random.Random) -> Dict[str, Any]:
    challenges = [
        ("A school wants to reduce electricity waste in its lighting system",
         "Replace existing incandescent filament bulbs with high-efficiency LED lighting",
         "LEDs convert up to 80% of electrical input into useful light compared to only 10% in filament bulbs, dramatically reducing wasted heat"),
        ("A factory wants to reduce energy waste in its conveyor belt transport motors",
         "Install low-friction roller bearings and apply high-grade synthetic lubrication regularly",
         "Reduces mechanical friction, allowing more electrical energy to convert to conveyor motion rather than wasted heat and sound"),
    ]
    goal, intervention, explanation = rng.choice(challenges)
    prompt = (
        f"**Engineering Design Challenge:**\n\n"
        f"Objective: **{goal}**.\n\n"
        f"Which engineering intervention will most effectively minimize energy transfer to the surroundings?"
    )
    correct = f"Intervention: **{intervention}**; Rationale: {explanation}."
    distractors = [
        "Intervention: Paint all electrical wires with black household paint; Rationale: Traps all electricity inside copper.",
        "Intervention: Run machines at triple speed without lubrication; Rationale: Overcomes friction by speed alone.",
        "Intervention: Switch off all safety breakers; Rationale: Allows electricity to bypass national grid standards.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Engineering Design Analysis:**\n"
        f"- Target Goal: {goal}.\n"
        f"- Optimal Solution: **{intervention}**.\n"
        f"- Scientific Rationale: **{explanation}**."
    )
    return {
        "id": f"ns7_et_49_{rng.randint(100000, 999999)}",
        "subskill": "49_designing_a_more_efficient_system_challenge",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "learning_objective_id": "ns7_et_49",
        "hints": {
            "tier_1": "Which intervention directly addresses the root cause of energy waste (friction or inefficient conversion)?",
            "tier_2": "Look for the evidence-based engineering solution.",
            "tier_3": f"Intervention: {intervention}.",
        },
        "misconception_tags": ["painting_wires_saves_energy", "higher_speed_eliminates_friction"],
    }


# 50. Energy transfer surroundings comprehensive diagnostic
def arch_50_energy_transfer_surroundings_comprehensive_diagnostic(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("A commercial bakery operates an industrial electric dough mixer (1 500 J input electrical energy -> 900 J useful rotational kinetic mixing, 450 J motor heat, 150 J acoustic noise)",
         60, 600,
         "Useful work accounts for 60% of input, while 40% (600 J) is wasted as heat and sound dissipated to the bakery air; total energy (1 500 J) is conserved"),
        ("A heavy delivery truck climbs a hill (10 000 J chemical fuel energy -> 3 000 J useful gravitational and kinetic gain, 4 500 J hot exhaust, 2 000 J radiator heat, 500 J sound)",
         30, 7000,
         "Useful work accounts for 30% of input, while 70% (7 000 J) is dissipated to surroundings as exhaust, radiator heat, and noise; total energy is conserved"),
    ]
    story, eff, wasted_sum, synthesis = rng.choice(scenarios)
    prompt = (
        f"**Comprehensive Energy Balance Diagnostic:**\n\n"
        f"Scenario: **{story}**.\n\n"
        f"Which statement provides the complete, scientifically accurate accounting of the system's energy efficiency, "
        f"wasted energy dissipation, and compliance with the Law of Conservation of Energy?"
    )
    correct = f"Efficiency is **{eff}%**; {synthesis}."
    distractors = [
        f"Efficiency is **100%** because all energy inputs were destroyed at the end of the process.",
        f"Efficiency is **{100 - eff}%** because wasted heat is the intended useful output.",
        "Conservation of energy failed because input energy was greater than useful output.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Comprehensive Diagnostic Solution:**\n"
        f"1. **Efficiency:** Useful Output / Total Input = **{eff}%**.\n"
        f"2. **Wasted Energy Accounting:** Total Input - Useful Output = **{wasted_sum} J**.\n"
        f"3. **Conservation Law:** {synthesis}."
    )
    return {
        "id": f"ns7_et_50_{rng.randint(100000, 999999)}",
        "subskill": "50_energy_transfer_surroundings_comprehensive_diagnostic",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 3,
        "learning_objective_id": "ns7_et_50",
        "hints": {
            "tier_1": "Calculate efficiency: Useful / Total Input x 100%.",
            "tier_2": "Account for all energy: input = useful + wasted.",
            "tier_3": f"Efficiency is {eff}%; {synthesis}.",
        },
        "misconception_tags": ["efficiency_below_100_violates_conservation", "wasted_energy_disappears"],
    }
