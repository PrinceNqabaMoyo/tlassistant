"""Grade 7 Natural Sciences: Term 3 - Energy Transfer to Surroundings (Archetypes 01 to 25).
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


# 01. Concept of useful vs wasted energy
def arch_01_concept_of_useful_vs_wasted_energy(rng: random.Random) -> Dict[str, Any]:
    appliances = [
        ("an electric desktop study lamp", "radiant light to illuminate reading material", "thermal heat warming the lamp shade and room air"),
        ("an electric hand mixer in a bakery", "mechanical kinetic motion of beaters to blend batter", "motor whirring sound and thermal heat"),
        ("an electric room space heater", "thermal heat to warm cold indoor air", "faint glowing red light and humming sound"),
    ]
    app, useful_role, wasted_role = rng.choice(appliances)
    prompt = (
        f"Every electrical machine or household tool is designed to achieve a specific purpose.\n\n"
        f"Consider **{app}**.\n"
        f"Which statement correctly identifies the **useful energy output** and the **wasted energy output** of this system?"
    )
    correct = f"Useful output: {useful_role} | Wasted output: {wasted_role}."
    distractors = [
        f"Useful output: {wasted_role} | Wasted output: {useful_role}.",
        "Useful output: pure nuclear radiation | Wasted output: zero energy.",
        "Both outputs are 100% useful because all energy forms achieve the same purpose.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Useful vs Wasted Energy in Systems:**\n"
        f"- **Useful Energy:** The specific output energy form intended to perform the system's job ({useful_role}).\n"
        f"- **Wasted Energy:** Energy transferred to the surroundings that does not contribute to the intended purpose ({wasted_role})."
    )
    return {
        "id": f"ns7_et_01_{rng.randint(100000, 999999)}",
        "subskill": "01_concept_of_useful_vs_wasted_energy",
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
        "learning_objective_id": "ns7_et_01",
        "hints": {
            "tier_1": "What is the primary reason someone switches on this appliance?",
            "tier_2": "The intended function is useful; unwanted heat or sound escaping is wasted.",
            "tier_3": f"Useful output: {useful_role} | Wasted output: {wasted_role}.",
        },
        "misconception_tags": ["all_outputs_are_equally_useful", "wasted_energy_does_not_exist"],
    }


# 02. Scientific meaning of wasted energy
def arch_02_scientific_meaning_of_wasted_energy(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("an electric food blender getting hot and loud while operating", "thermal energy and sound waves dissipated into the kitchen air"),
        ("a car gearbox warming up during a long journey", "heat radiated to the undercarriage and surrounding atmosphere"),
    ]
    app, dissipation = rng.choice(examples)
    prompt = (
        f"In Natural Sciences, we describe certain energy outputs as **'wasted'**.\n\n"
        f"Consider **{app}** ({dissipation}).\n"
        f"What is the precise scientific meaning of 'wasted energy'?"
    )
    correct = (
        "It is energy transferred or dissipated to the surroundings in forms (such as heat and sound) "
        "that cannot be used to perform the intended work of the system."
    )
    distractors = [
        "It is energy that was physically destroyed into empty void space.",
        "It is toxic radioactive waste that must be buried in concrete bunkers.",
        "It is energy that spontaneously turns into heavy metallic mass inside the machine.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Scientific Meaning of 'Wasted Energy':**\n"
        f"- Energy is **never destroyed** (Law of Conservation of Energy).\n"
        f"- 'Wasted' means energy has transferred to the environment as low-grade thermal energy or sound waves.\n"
        f"- It disperses into the surroundings, making it unavailable to do useful work."
    )
    return {
        "id": f"ns7_et_02_{rng.randint(100000, 999999)}",
        "subskill": "02_scientific_meaning_of_wasted_energy",
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
        "learning_objective_id": "ns7_et_02",
        "hints": {
            "tier_1": "Does wasted energy disappear from the universe?",
            "tier_2": "It still exists, but has spread out into the surroundings as unwanted heat or sound.",
            "tier_3": "Energy transferred to surroundings in forms that cannot perform the intended work.",
        },
        "misconception_tags": ["wasted_energy_is_destroyed", "wasted_energy_is_matter"],
    }


# 03. Origin and definition of Sankey diagram
def arch_03_origin_and_definition_of_sankey_diagram(rng: random.Random) -> Dict[str, Any]:
    years = [(1898, "Captain Matthew Sankey", "the thermal energy efficiency of steam engines")]
    yr, founder, topic = rng.choice(years)
    prompt = (
        f"Engineers and scientists utilize **Sankey energy flow representations** to model system efficiency.\n\n"
        f"Who first introduced this visual tool in {yr}, and what was its original historical engineering application?"
    )
    correct = f"Introduced by **{founder}** to visually analyze **{topic}**."
    distractors = [
        f"Invented by Isaac Newton to map the orbits of planetary moons in outer space.",
        f"Developed by Thomas Edison to measure the chemical voltage of batteries.",
        f"Created by Albert Einstein to calculate the speed of light in glass.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Historical Background of Sankey Representations:**\n"
        f"- Named after Irish engineer {founder}.\n"
        f"- First published in {yr} in a seminal engineering report analyzing {topic}.\n"
        f"- It pioneered the standard of using scaled arrow widths to illustrate energy inputs, useful conversions, and wasted losses."
    )
    return {
        "id": f"ns7_et_03_{rng.randint(100000, 999999)}",
        "subskill": "03_origin_and_definition_of_sankey_diagram",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "ns7_et_03",
        "hints": {
            "tier_1": "Recall the historical note in the textbook overview.",
            "tier_2": "Look for Captain Matthew Sankey and steam engine efficiency.",
            "tier_3": f"Introduced by {founder} to visually analyze {topic}.",
        },
        "misconception_tags": ["sankey_invented_electricity", "sankey_is_a_unit_of_heat"],
    }


# 04. Sankey diagram arrow width significance
def arch_04_sankey_diagram_arrow_width_significance(rng: random.Random) -> Dict[str, Any]:
    units = [("Joules (J)", "energy flow rate or total energy quantity"),
             ("kilojoules (kJ)", "the amount of energy passing through each branch")]
    unit_str, quantity = rng.choice(units)
    prompt = (
        f"In a properly constructed Sankey energy flow representation, arrows represent energy pathways.\n\n"
        f"What does the **width (thickness)** of each arrow represent?"
    )
    correct = f"The width of each arrow is drawn strictly to scale to represent the quantity of energy in {unit_str} ({quantity})."
    distractors = [
        "The width represents the physical length of the electrical cables in centimeters.",
        "The width represents the speed of sound through the machinery casing.",
        "The width represents the total mass of the machine in kilograms.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Scale Convention in Sankey Flows:**\n"
        f"- Arrow width is directly proportional to energy quantity (measured in {unit_str}).\n"
        f"- A wide arrow represents a large amount of energy; a narrow arrow represents a small amount of energy.\n"
        f"- Arrow length has no physical meaning; only **width** matters."
    )
    return {
        "id": f"ns7_et_04_{rng.randint(100000, 999999)}",
        "subskill": "04_sankey_diagram_arrow_width_significance",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 1,
        "learning_objective_id": "ns7_et_04",
        "hints": {
            "tier_1": "Does arrow length or arrow width show how much energy flows?",
            "tier_2": "The width is drawn to scale to show the amount of energy in Joules.",
            "tier_3": f"Width is drawn to scale to represent the quantity of energy in {unit_str}.",
        },
        "misconception_tags": ["arrow_length_represents_energy", "arrow_color_determines_quantity"],
    }


# 05. Sankey diagram conservation law principle
def arch_05_sankey_diagram_conservation_law_principle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In every valid Sankey energy flow representation, the input arrow divides into two or more output branches.\n\n"
        "How must the width of the input arrow relate to the widths of the output arrows to obey the Law of Conservation of Energy?"
    )
    correct = "The width of the input arrow must exactly equal the combined total sum of the widths of all useful and wasted output arrows."
    distractors = [
        "The input arrow width must always be smaller than the useful output arrow width.",
        "The output arrows must add up to double the width of the input arrow.",
        "There is no relationship because arrow widths are chosen purely for artistic decoration.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Conservation Principle in Sankey Representations:**\n"
        f"$$\\text{{Width}}_{{\\text{{input}}}} = \\text{{Width}}_{{\\text{{useful}}}} + \\text{{Width}}_{{\\text{{wasted}}}}$$\n"
        f"Because energy cannot be created from nothing or destroyed into nothing, the total width entering must match the total width exiting."
    )
    return {
        "id": f"ns7_et_05_{rng.randint(100000, 999999)}",
        "subskill": "05_sankey_diagram_conservation_law_principle",
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
        "learning_objective_id": "ns7_et_05",
        "hints": {
            "tier_1": "Think about conservation: does energy in equal energy out?",
            "tier_2": "The input width must equal the sum of all output branch widths.",
            "tier_3": "Input arrow width must equal the combined sum of all output arrows.",
        },
        "misconception_tags": ["outputs_can_exceed_inputs_without_source", "wasted_energy_need_not_be_drawn"],
    }


# 06. Incandescent light bulb energy flow
def arch_06_incandescent_light_bulb_energy_flow(rng: random.Random) -> Dict[str, Any]:
    ratings = [(100, 10, 90), (60, 6, 54)]
    input_j, light_j, heat_j = rng.choice(ratings)
    prompt = (
        f"An old-fashioned **incandescent light bulb** consumes **{input_j} J** of electrical energy every second.\n"
        f"It produces **{light_j} J** of useful light energy and **{heat_j} J** of thermal energy.\n\n"
        f"Why is the incandescent light bulb considered an extremely **inefficient** lighting system?"
    )
    correct = f"Because roughly 90% of the input energy ({heat_j} J) is wasted as thermal heat transferred to the surroundings, with only ~10% converted to light."
    distractors = [
        "Because it creates cold air that freezes the room.",
        "Because it produces sound waves that shatter glass windows.",
        "Because light energy is heavier than thermal energy.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Incandescent Bulb Inefficiency:**\n"
        f"- The tungsten wire filament must be heated to over 2 500 °C before it glows white-hot.\n"
        f"- Useful output (Light): \\(\\frac{{{light_j}}}{{{input_j}}} \\times 100\\% = 10\\%\\).\n"
        f"- Wasted output (Heat): \\(\\frac{{{heat_j}}}{{{input_j}}} \\times 100\\% = 90\\%\\).\n"
        f"- Most input electrical energy is wasted as heat escaping to surroundings."
    )
    return {
        "id": f"ns7_et_06_{rng.randint(100000, 999999)}",
        "subskill": "06_incandescent_light_bulb_energy_flow",
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
        "learning_objective_id": "ns7_et_06",
        "hints": {
            "tier_1": "Compare the 10 J of light with the 90 J of heat.",
            "tier_2": "Most of the energy is lost as unwanted heat from the hot filament.",
            "tier_3": f"Roughly 90% of energy ({heat_j} J) is wasted as heat; only ~10% is light.",
        },
        "misconception_tags": ["light_bulbs_produce_mostly_light", "heat_from_bulbs_is_useful_work"],
    }


# 07. Fluorescent CFL light bulb comparison
def arch_07_fluorescent_cfl_light_bulb_comparison(rng: random.Random) -> Dict[str, Any]:
    comparisons = [
        ("a 100 J input electrical test", 10, 25, "Compact Fluorescent Lamp (CFL)", "incandescent bulb"),
        ("standard household illumination", 5, 20, "fluorescent tube", "filament bulb"),
    ]
    test, inc_light, cfl_light, cfl_name, inc_name = rng.choice(comparisons)
    prompt = (
        f"In a comparative lighting test with 100 J of electrical energy input:\n"
        f"- The {inc_name} produces only {inc_light} J of light energy.\n"
        f"- The {cfl_name} produces {cfl_light} J of light energy.\n\n"
        f"Why is the {cfl_name} significantly more energy-efficient than the {inc_name}?"
    )
    correct = f"It converts a higher proportion of electrical energy into useful light ({cfl_light} J vs {inc_light} J) and wastes far less energy as heat."
    distractors = [
        "It consumes zero electrical current from the power grid.",
        "It absorbs dark matter from the room to glow without input energy.",
        "It creates new carbon atoms inside the glass tube every minute.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**CFL vs Incandescent Efficiency:**\n"
        f"- {inc_name.capitalize()}: {inc_light}% efficient (wastes {100 - inc_light}% as heat).\n"
        f"- {cfl_name.capitalize()}: {cfl_light}% efficient (wastes {100 - cfl_light}% as heat).\n"
        f"- Because CFLs excite mercury vapor gas rather than heating a metal wire to extreme temperatures, they waste substantially less thermal energy."
    )
    return {
        "id": f"ns7_et_07_{rng.randint(100000, 999999)}",
        "subskill": "07_fluorescent_cfl_light_bulb_comparison",
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
        "learning_objective_id": "ns7_et_07",
        "hints": {
            "tier_1": "Which bulb gives more light for the same 100 J of electricity?",
            "tier_2": "CFL produces more light and wastes less energy as heat.",
            "tier_3": f"Converts higher proportion into useful light ({cfl_light} J vs {inc_light} J) and wastes less heat.",
        },
        "misconception_tags": ["all_bulbs_have_equal_efficiency", "fluorescents_emit_zero_heat"],
    }


# 08. Modern LED lighting efficiency
def arch_08_modern_led_lighting_efficiency(rng: random.Random) -> Dict[str, Any]:
    powers = [(10, 60, "A 10 W LED bulb produces the same brightness (lumens) as a 60 W incandescent bulb.")]
    led_w, inc_w, statement = rng.choice(powers)
    prompt = (
        f"Energy efficiency experts advise South African households: *\"{statement}\"*\n\n"
        f"What enables a **Light Emitting Diode (LED)** to achieve such high efficiency compared to traditional bulbs?"
    )
    correct = (
        "LED semiconductors convert electron movement directly into light photons with minimal heat generation, "
        "wasting very little energy to the surroundings."
    )
    distractors = [
        "LED bulbs burn coal directly inside their plastic casings.",
        "LED bulbs use gravitational waves instead of electrical current.",
        "LED bulbs destroy 50% of the room's oxygen to create light.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Solid-State Lighting (LED) Physics:**\n"
        f"- Unlike incandescent bulbs (which must heat a wire to 2 500 °C) or CFLs, LEDs use semiconductor chips.\n"
        f"- Electrons recombine with electron holes, releasing energy directly as photons of light.\n"
        f"- Very little electrical input is wasted as thermal energy, using ~80% less power for the same light output."
    )
    return {
        "id": f"ns7_et_08_{rng.randint(100000, 999999)}",
        "subskill": "08_modern_led_lighting_efficiency",
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
        "learning_objective_id": "ns7_et_08",
        "hints": {
            "tier_1": "Do LED bulbs get burning hot like old incandescent bulbs?",
            "tier_2": "LEDs stay relatively cool because they convert electricity directly to light.",
            "tier_3": "Semiconductors convert electron movement directly into light with minimal heat waste.",
        },
        "misconception_tags": ["led_bulbs_produce_no_light", "watts_measure_brightness"],
    }


# 09. Electric drill useful and wasted outputs
def arch_09_electric_drill_useful_and_wasted_outputs(rng: random.Random) -> Dict[str, Any]:
    tasks = [
        ("drilling a hole in a metal aircraft wing component", "kinetic energy of the spinning drill bit doing mechanical work"),
        ("drilling a hole through a dense pine wooden plank", "rotational kinetic motion cutting through timber fibers"),
    ]
    task, useful_def = rng.choice(tasks)
    prompt = (
        f"A craftsperson operates an **electric drill** for **{task}**.\n"
        f"During operation, the drill motor whines loudly and the drill bit becomes hot to the touch.\n\n"
        f"What are the **useful** and **wasted** energy outputs in this system?"
    )
    correct = f"Useful output: {useful_def} | Wasted outputs: thermal energy (heat from friction) and sound energy (noise)."
    distractors = [
        f"Useful output: the loud motor noise to warn coworkers | Wasted output: {useful_def}.",
        "Useful output: gravitational potential energy | Wasted output: radiant light rays.",
        "Useful output: chemical potential energy in the cord | Wasted output: pure electricity.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Electric Drill Energy Analysis:**\n"
        f"- **Input:** Electrical energy from the wall socket.\n"
        f"- **Useful Output:** {useful_def}.\n"
        f"- **Wasted Outputs:** Friction between the bit and material generates **thermal heat**; motor gears and air turbulence generate **sound noise**."
    )
    return {
        "id": f"ns7_et_09_{rng.randint(100000, 999999)}",
        "subskill": "09_electric_drill_useful_and_wasted_outputs",
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
        "learning_objective_id": "ns7_et_09",
        "hints": {
            "tier_1": "What is the drill supposed to do? Spin and drill holes.",
            "tier_2": "The spinning motion is useful; heat and loud noise are wasted.",
            "tier_3": f"Useful: {useful_def} | Wasted: thermal heat and sound.",
        },
        "misconception_tags": ["drill_sound_is_useful_work", "friction_does_not_create_heat"],
    }


# 10. Electric kettle energy flow analysis
def arch_10_electric_kettle_energy_flow_analysis(rng: random.Random) -> Dict[str, Any]:
    energies = [(500, 420, 80), (1000, 850, 150)]
    input_kj, useful_kj, wasted_kj = rng.choice(energies)
    prompt = (
        f"An electric kettle uses **{input_kj} kJ** of electrical energy to boil water.\n"
        f"Of this energy, **{useful_kj} kJ** is transferred to heat the water to 100 °C.\n\n"
        f"What happens to the remaining **{wasted_kj} kJ** of energy?"
    )
    correct = f"It is wasted as thermal energy escaping through the kettle walls and lid into the surrounding air, plus sound energy (boiling noise)."
    distractors = [
        "It is permanently destroyed into nothingness by the thermostat.",
        "It turns into solid copper metal inside the heating element.",
        "It flows backward into the national grid as negative electricity.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Kettle Energy Accounting:**\n"
        f"- Total Input = {input_kj} kJ.\n"
        f"- Useful Output (water heating) = {useful_kj} kJ.\n"
        f"- Wasted Output = {input_kj} kJ - {useful_kj} kJ = **{wasted_kj} kJ**.\n"
        f"- This wasted energy is transferred to surroundings via conduction/convection through the kettle body and sound waves from bubbling water."
    )
    return {
        "id": f"ns7_et_10_{rng.randint(100000, 999999)}",
        "subskill": "10_electric_kettle_energy_flow_analysis",
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
        "learning_objective_id": "ns7_et_10",
        "hints": {
            "tier_1": "Does the kettle body get hot and make bubbling noise?",
            "tier_2": "Heat escapes through the walls and sound escapes to the kitchen air.",
            "tier_3": f"Wasted as thermal energy escaping to surrounding air plus sound energy.",
        },
        "misconception_tags": ["kettles_are_100_percent_efficient", "heat_cannot_escape_plastic_kettles"],
    }


# 11. Electric iron energy transfers
def arch_11_electric_iron_energy_transfers(rng: random.Random) -> Dict[str, Any]:
    fabrics = [("smoothing wrinkles in cotton school shirts", "soleplate conduction"),
               ("pressing a formal wool blazer", "thermal transfer from baseplate to fabric")]
    task, mechanism = rng.choice(fabrics)
    prompt = (
        f"An electric steam iron is used for **{task}** ({mechanism}).\n\n"
        f"Which statement correctly classifies the useful and wasted energy transfers of an electric iron?"
    )
    correct = (
        "Useful: thermal energy transferred by conduction from the hot metal soleplate directly to the clothing fabric.\n"
        "Wasted: thermal energy radiating and convecting into the surrounding room air, plus hissing steam sound."
    )
    distractors = [
        "Useful: the sound of steam hissing to signal completion.\nWasted: the heat of the soleplate.",
        "Useful: magnetic fields pressing down on clothes.\nWasted: pure chemical potential energy.",
        "Useful: light from the indicator bulb.\nWasted: all thermal energy.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Electric Iron Energy Balance:**\n"
        f"- **Input:** Electrical energy.\n"
        f"- **Useful Output:** Thermal energy transferred directly to fabric ({mechanism}) to relax polymer fibers and remove wrinkles.\n"
        f"- **Wasted Output:** Heat transferred to surrounding ambient air (which does not iron clothes) and steam hissing sound."
    )
    return {
        "id": f"ns7_et_11_{rng.randint(100000, 999999)}",
        "subskill": "11_electric_iron_energy_transfers",
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
        "learning_objective_id": "ns7_et_11",
        "hints": {
            "tier_1": "What heats the clothes? The soleplate.",
            "tier_2": "Heat to clothes is useful; heat escaping to room air is wasted.",
            "tier_3": "Useful: thermal energy to fabric; Wasted: thermal energy into room air and steam sound.",
        },
        "misconception_tags": ["all_heat_from_iron_is_useful", "steam_is_chemical_energy"],
    }


# 12. Electric fan energy analysis
def arch_12_electric_fan_energy_analysis(rng: random.Random) -> Dict[str, Any]:
    fans = [("a rotating ceiling fan in a warm classroom", "kinetic energy of moving air currents creating a cooling breeze"),
            ("an oscillating electric pedestal fan in an office", "kinetic air motion to increase sweat evaporation from skin")]
    fan_type, useful_desc = rng.choice(fans)
    prompt = (
        f"Consider **{fan_type}**.\n\n"
        f"What is the **useful energy output** of this system, and what are its **wasted energy outputs**?"
    )
    correct = f"Useful output: {useful_desc} | Wasted outputs: thermal energy (electric motor heating up) and sound energy (humming/whirring)."
    distractors = [
        f"Useful output: motor heat to warm the ceiling | Wasted output: {useful_desc}.",
        "Useful output: gravitational potential energy | Wasted output: chemical battery acid.",
        "Useful output: light from the spinning blades | Wasted output: nuclear radiation.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Electric Fan Energy Balance:**\n"
        f"- **Input:** Electrical energy.\n"
        f"- **Useful Output:** {useful_desc}.\n"
        f"- **Wasted Outputs:** Electrical resistance and bearing friction generate **heat** in the motor housing; air slicing generates **sound**."
    )
    return {
        "id": f"ns7_et_12_{rng.randint(100000, 999999)}",
        "subskill": "12_electric_fan_energy_analysis",
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
        "learning_objective_id": "ns7_et_12",
        "hints": {
            "tier_1": "What is the fan designed to do? Move air.",
            "tier_2": "Air movement (kinetic) is useful; motor warmth and humming are wasted.",
            "tier_3": f"Useful: {useful_desc} | Wasted: motor heat and sound.",
        },
        "misconception_tags": ["fans_create_cold_energy", "fan_motor_has_zero_heat"],
    }


# 13. Car petrol engine energy balance
def arch_13_car_petrol_engine_energy_balance(rng: random.Random) -> Dict[str, Any]:
    proportions = [(100, 25, 75, "25% useful kinetic motion and 75% wasted thermal and sound energy"),
                   (1000, 280, 720, "28% useful kinetic motion and 72% wasted heat and sound")]
    total_j, useful_j, wasted_j, summary = rng.choice(proportions)
    prompt = (
        f"In a typical passenger car with an internal combustion petrol engine:\n"
        f"For every {total_j} J of chemical energy in petrol, only {useful_j} J is converted into vehicle movement.\n\n"
        f"How is the remaining {wasted_j} J of energy transferred to the surroundings?"
    )
    correct = (
        "It is wasted as hot exhaust gases blown out the tailpipe, thermal heat dissipated by the radiator and cooling system, "
        "and mechanical noise/sound."
    )
    distractors = [
        "It is converted into brand new petrol stored in the spare tire.",
        "It is destroyed completely into nothingness by the catalytic converter.",
        "It turns into pure gravitational energy that lifts the car off the highway.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Automotive Internal Combustion Energy Balance:**\n"
        f"- Car engines are only ~20% to 30% efficient ({summary}).\n"
        f"- Roughly 35% leaves as hot exhaust gases.\n"
        f"- Roughly 35% is absorbed by coolant and dissipated by the radiator to surrounding air.\n"
        f"- Roughly 5% is friction and acoustic sound waves."
    )
    return {
        "id": f"ns7_et_13_{rng.randint(100000, 999999)}",
        "subskill": "13_car_petrol_engine_energy_balance",
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
        "learning_objective_id": "ns7_et_13",
        "hints": {
            "tier_1": "Think about why a car engine has a radiator and a hot exhaust pipe.",
            "tier_2": "Most fuel energy is lost as hot exhaust, radiator heat, and engine noise.",
            "tier_3": "Wasted as hot exhaust gases, radiator heat, and engine sound.",
        },
        "misconception_tags": ["cars_convert_100_percent_fuel_to_motion", "exhaust_gases_are_cold"],
    }


# 14. Television screen energy transfers
def arch_14_television_screen_energy_transfers(rng: random.Random) -> Dict[str, Any]:
    tvs = [("a modern LED television monitor", "radiant light from the display screen and acoustic sound waves from speakers", "thermal heat radiating from back circuit boards")]
    tv_type, useful_desc, wasted_desc = rng.choice(tvs)
    prompt = (
        f"Consider **{tv_type}** plugged into a wall power outlet.\n\n"
        f"What are the **useful** energy outputs and the **wasted** energy output of a television?"
    )
    correct = f"Useful outputs: {useful_desc} | Wasted output: {wasted_desc}."
    distractors = [
        f"Useful output: {wasted_desc} | Wasted outputs: {useful_desc}.",
        "Useful output: chemical potential energy | Wasted output: gravitational waves.",
        "Useful output: nuclear fission | Wasted output: magnetic ice.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Television Energy Balance:**\n"
        f"- **Input:** Electrical energy.\n"
        f"- **Useful Outputs:** We watch pictures (radiant light) and listen to audio ({useful_desc}).\n"
        f"- **Wasted Output:** Electronic components, power converters, and processors warm up ({wasted_desc}), which does not improve the picture or sound."
    )
    return {
        "id": f"ns7_et_14_{rng.randint(100000, 999999)}",
        "subskill": "14_television_screen_energy_transfers",
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
        "learning_objective_id": "ns7_et_14",
        "hints": {
            "tier_1": "What do your eyes see and your ears hear from a TV?",
            "tier_2": "Light and sound are useful; the warm back panel is wasted heat.",
            "tier_3": f"Useful: {useful_desc} | Wasted: {wasted_desc}.",
        },
        "misconception_tags": ["tv_heat_is_useful_work", "tvs_consume_zero_power_when_on"],
    }


# 15. Hairdryer dual useful outputs
def arch_15_hairdryer_dual_useful_outputs(rng: random.Random) -> Dict[str, Any]:
    prompts = [
        ("an electric hair dryer", "thermal energy (nichrome heating coils to evaporate water) AND kinetic energy (fan motor blowing air)", "loud sound noise and excess casing heat")
    ]
    device, useful_pair, wasted_pair = rng.choice(prompts)
    prompt = (
        f"A hair dryer is an appliance with **two distinct useful energy outputs** working simultaneously.\n\n"
        f"What are the two useful energy outputs, and what is the primary wasted output of **{device}**?"
    )
    correct = f"Useful outputs: {useful_pair} | Wasted outputs: {wasted_pair}."
    distractors = [
        f"Useful outputs: {wasted_pair} | Wasted outputs: {useful_pair}.",
        "Useful outputs: light and chemical fuel | Wasted outputs: gravitational potential.",
        "Useful outputs: nuclear radiation | Wasted outputs: pure cold air.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Dual Useful Outputs in a Hairdryer:**\n"
        f"1. **Thermal Energy:** Heating coils warm the incoming air stream (evaporates moisture).\n"
        f"2. **Kinetic Energy:** Electric fan blows the heated air outward across hair.\n"
        f"3. **Wasted Output:** High-decibel sound noise and heat radiating through the plastic handle."
    )
    return {
        "id": f"ns7_et_15_{rng.randint(100000, 999999)}",
        "subskill": "15_hairdryer_dual_useful_outputs",
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
        "learning_objective_id": "ns7_et_15",
        "hints": {
            "tier_1": "A hairdryer produces both heat AND moving air.",
            "tier_2": "Both thermal (heat) and kinetic (wind) are useful; loud noise is wasted.",
            "tier_3": f"Useful: {useful_pair} | Wasted: {wasted_pair}.",
        },
        "misconception_tags": ["appliances_can_only_have_one_useful_output", "hairdryer_noise_dries_hair"],
    }


# 16. Bicycle mechanical energy transfer
def arch_16_bicycle_mechanical_energy_transfer(rng: random.Random) -> Dict[str, Any]:
    cyclists = [("a commuter pedaling a bicycle along a tar road", "chemical potential energy in leg muscles")]
    context, energy_input = rng.choice(cyclists)
    prompt = (
        f"Consider **{context}** ({energy_input}).\n\n"
        f"What is the **useful energy output**, and how is energy **wasted** to the surroundings in this system?"
    )
    correct = (
        "Useful output: kinetic energy of forward motion of bicycle and rider.\n"
        "Wasted outputs: thermal energy (heat in tires, chain friction, and rider's body sweating) and sound (chain clicking and tire contact)."
    )
    distractors = [
        "Useful output: thermal heat melting the tar road.\nWasted output: forward movement.",
        "Useful output: electrical current powering streetlights.\nWasted output: pure gravity.",
        "Useful output: light from the pedals.\nWasted output: zero energy.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Bicycle Energy Dynamics:**\n"
        f"- **Input:** Chemical potential energy from digested food metabolized by muscles.\n"
        f"- **Useful:** Kinetic energy (forward translational motion).\n"
        f"- **Wasted:** Tire rolling resistance, chain/gear friction, and air resistance generate **thermal energy**; moving parts produce **sound**."
    )
    return {
        "id": f"ns7_et_16_{rng.randint(100000, 999999)}",
        "subskill": "16_bicycle_mechanical_energy_transfer",
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
        "learning_objective_id": "ns7_et_16",
        "hints": {
            "tier_1": "What is the goal of riding a bike? Moving forward.",
            "tier_2": "Forward kinetic motion is useful; tire friction, chain noise, and sweat heat are wasted.",
            "tier_3": "Useful: kinetic motion; Wasted: thermal friction and sound.",
        },
        "misconception_tags": ["bicycles_have_zero_friction", "human_muscles_are_100_percent_efficient"],
    }


# 17. Burning candle useful vs wasted
def arch_17_burning_candle_useful_vs_wasted(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("a wax candle lit during loadshedding to illuminate a dining table", "radiant light energy to illuminate the room", "thermal heat energy warming the ceiling and air"),
        ("a wax candle lit in an emergency power outage", "light energy to read school books", "convection heat escaping upward into the room"),
    ]
    context, useful_role, wasted_role = rng.choice(scenarios)
    prompt = (
        f"Consider **{context}**.\n\n"
        f"In this scenario, how are the energy outputs classified?"
    )
    correct = f"Useful output: {useful_role} | Wasted output: {wasted_role}."
    distractors = [
        f"Useful output: {wasted_role} | Wasted output: {useful_role}.",
        "Useful output: sound waves | Wasted output: electrical current.",
        "Useful output: nuclear fission | Wasted output: gravitational waves.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Candle Energy Analysis:**\n"
        f"- **Input:** Chemical potential energy stored in paraffin wax hydrocarbons.\n"
        f"- **Context:** When lit for illumination during power cuts, **light** is the intended useful output ({useful_role}).\n"
        f"- **Wasted:** Most combustion energy is released as **heat** ({wasted_role}), which is unwanted for simple table illumination."
    )
    return {
        "id": f"ns7_et_17_{rng.randint(100000, 999999)}",
        "subskill": "17_burning_candle_useful_vs_wasted",
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
        "learning_objective_id": "ns7_et_17",
        "hints": {
            "tier_1": "Why was the candle lit during loadshedding? To see.",
            "tier_2": "Light is the useful output; heat rising to the ceiling is wasted.",
            "tier_3": f"Useful: {useful_role} | Wasted: {wasted_role}.",
        },
        "misconception_tags": ["candle_wax_turns_into_electricity", "heat_from_candles_is_always_useful"],
    }


# 18. Electric toaster energy flow
def arch_18_electric_toaster_energy_flow(rng: random.Random) -> Dict[str, Any]:
    breads = [("slices of brown bread placed into an electric two-slot toaster", "thermal infrared heat to toast and crisp the bread slices")]
    context, useful_heat = rng.choice(breads)
    prompt = (
        f"Consider **{context}**.\n\n"
        f"What is the **useful energy output**, and what energy is **wasted** to the surroundings?"
    )
    correct = (
        f"Useful output: {useful_heat}.\n"
        "Wasted outputs: thermal heat escaping out the open top slots into the kitchen air, faint red glow (light), and pop-up sound."
    )
    distractors = [
        "Useful output: the loud pop-up click sound.\nWasted output: all thermal heat.",
        "Useful output: kinetic energy launching bread to the ceiling.\nWasted output: electrical current.",
        "Useful output: chemical energy in the plug.\nWasted output: pure gravity.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Toaster Energy Analysis:**\n"
        f"- **Input:** Electrical energy.\n"
        f"- **Useful Output:** {useful_heat}.\n"
        f"- **Wasted Output:** Heat that escapes out the top without touching the bread, visible glowing red light from nichrome ribbons, and the spring ejection sound."
    )
    return {
        "id": f"ns7_et_18_{rng.randint(100000, 999999)}",
        "subskill": "18_electric_toaster_energy_flow",
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
        "learning_objective_id": "ns7_et_18",
        "hints": {
            "tier_1": "What toasts the bread? Heat.",
            "tier_2": "Heat to bread is useful; heat escaping out the open top and the pop-up sound are wasted.",
            "tier_3": "Useful: thermal heat to toast bread; Wasted: heat escaping into kitchen air, faint light, and pop-up sound.",
        },
        "misconception_tags": ["all_toaster_heat_enters_bread", "glowing_ribbons_mean_100_percent_light"],
    }


# 19. Refrigerator cooling energy displacement
def arch_19_refrigerator_cooling_energy_displacement(rng: random.Random) -> Dict[str, Any]:
    prompts = [
        ("a kitchen domestic refrigerator", "extracting thermal energy from food inside the cabinet and expelling it out the back condenser coils into the kitchen")
    ]
    app, action = rng.choice(prompts)
    prompt = (
        f"A common misconception is that **{app}** 'creates cold'.\n\n"
        f"From a thermodynamic perspective, how does a refrigerator actually function to chill food?"
    )
    correct = (
        f"Electrical energy runs a compressor and refrigerant cycle that {action}; "
        "it transfers heat from a colder interior to a warmer exterior."
    )
    distractors = [
        "It generates cold particles called 'frigidrons' that destroy heat atoms permanently.",
        "It absorbs all light from the food and converts it into solid ice.",
        "It pumps liquid nitrogen directly from outer space through the door gasket.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Thermodynamics of Refrigeration:**\n"
        f"- 'Cold' is not a physical substance; cold is simply the **absence of thermal energy**.\n"
        f"- A refrigerator uses electrical energy to pump refrigerant through evaporator and condenser coils.\n"
        f"- It {action}. (Feel the back of a fridge: it is warm!)."
    )
    return {
        "id": f"ns7_et_19_{rng.randint(100000, 999999)}",
        "subskill": "19_refrigerator_cooling_energy_displacement",
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
        "learning_objective_id": "ns7_et_19",
        "hints": {
            "tier_1": "Can you create 'cold', or do you remove heat?",
            "tier_2": "A fridge removes heat from inside and pumps it out the back.",
            "tier_3": f"Electrical energy runs a compressor that {action}.",
        },
        "misconception_tags": ["refrigerators_create_cold", "leaving_fridge_open_cools_the_house"],
    }


# 20. Audio speaker energy transfers
def arch_20_audio_speaker_energy_transfers(rng: random.Random) -> Dict[str, Any]:
    speakers = [("a high-power classroom audio loudspeaker", "acoustic sound wave kinetic energy")]
    device, useful_form = rng.choice(speakers)
    prompt = (
        f"Consider **{device}**.\n\n"
        f"What is the **useful energy output**, and what is the **wasted energy output** of a loudspeaker system?"
    )
    correct = f"Useful output: {useful_form} (vibrating air particles) | Wasted output: thermal energy (heat dissipated in voice coil and amplifier)."
    distractors = [
        f"Useful output: thermal energy to heat the room | Wasted output: {useful_form}.",
        "Useful output: gravitational potential energy | Wasted output: chemical battery acid.",
        "Useful output: nuclear fission | Wasted output: light rays.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Loudspeaker Energy Balance:**\n"
        f"- **Input:** Electrical audio signal.\n"
        f"- **Useful Output:** {useful_form} vibrating the speaker cone and surrounding air.\n"
        f"- **Wasted Output:** Electrical resistance in the voice coil wire and amplifier circuitry converts some energy into **thermal heat**."
    )
    return {
        "id": f"ns7_et_20_{rng.randint(100000, 999999)}",
        "subskill": "20_audio_speaker_energy_transfers",
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
        "learning_objective_id": "ns7_et_20",
        "hints": {
            "tier_1": "What is the purpose of a speaker? To produce sound.",
            "tier_2": "Sound is useful; voice coil heat is wasted.",
            "tier_3": f"Useful: {useful_form} | Wasted: thermal energy in voice coil.",
        },
        "misconception_tags": ["speakers_are_100_percent_efficient", "sound_has_no_energy"],
    }


# 21. Calculating efficiency percentage basic
def arch_21_calculating_efficiency_percentage_basic(rng: random.Random) -> Dict[str, Any]:
    problems = [(200, 50, 25), (400, 100, 25), (500, 200, 40), (250, 50, 20)]
    input_j, useful_j, eff = rng.choice(problems)
    prompt = (
        f"An electric motor draws **{input_j} J** of electrical input energy.\n"
        f"It produces **{useful_j} J** of useful mechanical kinetic work, with the remainder lost as heat.\n\n"
        f"What is the **energy efficiency percentage** of this motor?"
    )
    correct = f"**{eff}%**, calculated as \\(\\frac{{{useful_j}}}{{{input_j}}} \\times 100\\%\\)."
    distractors = [
        f"**{eff * 2}%**, calculated as \\(\\frac{{{useful_j} \\times 2}}{{{input_j}}} \\times 100\\%\\).",
        f"**{100 - eff}%**, calculated by subtracting input from useful.",
        f"**{eff / 2}%**, calculated as half the input.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Efficiency Calculation Formula:**\n"
        f"$$\\text{{Efficiency}} = \\left(\\frac{{\\text{{Useful Output Energy}}}}{{\\text{{Total Input Energy}}}}\\right) \\times 100\\%$$\n"
        f"$$\\text{{Efficiency}} = \\left(\\frac{{{useful_j}\\text{{ J}}}}{{{input_j}\\text{{ J}}}}\\right) \\times 100\\% = \\mathbf{{{eff}\\%}}$$"
    )
    return {
        "id": f"ns7_et_21_{rng.randint(100000, 999999)}",
        "subskill": "21_calculating_efficiency_percentage_basic",
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
        "learning_objective_id": "ns7_et_21",
        "hints": {
            "tier_1": "Formula: (Useful Output / Total Input) x 100%.",
            "tier_2": f"Divide {useful_j} by {input_j} and multiply by 100.",
            "tier_3": f"{eff}%.",
        },
        "misconception_tags": ["efficiency_is_input_divided_by_useful", "forgetting_percentage_multiplier"],
    }


# 22. Calculating wasted energy from input useful
def arch_22_calculating_wasted_energy_from_input_useful(rng: random.Random) -> Dict[str, Any]:
    values = [(1200, 300, 900), (800, 200, 600), (1500, 450, 1050)]
    total_in, useful_out, wasted_out = rng.choice(values)
    prompt = (
        f"A lawnmower petrol engine receives **{total_in} J** of chemical energy from fuel.\n"
        f"It converts **{useful_out} J** into useful kinetic energy of the spinning cutting blades.\n\n"
        f"According to the Law of Conservation of Energy, how much energy is **wasted** as heat and noise to the surroundings?"
    )
    correct = f"**{wasted_out} J**, because Wasted Energy = Total Input ({total_in} J) - Useful Output ({useful_out} J)."
    distractors = [
        f"**{total_in + useful_out} J**, because energy multiplies during cutting.",
        f"**0 J**, because lawnmowers do not lose energy.",
        f"**{useful_out / 2} J**, because half of useful output is lost.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Energy Balance Formula:**\n"
        f"$$\\text{{Total Input}} = \\text{{Useful Output}} + \\text{{Wasted Output}}$$\n"
        f"$$\\text{{Wasted Output}} = \\text{{Total Input}} - \\text{{Useful Output}}$$\n"
        f"$$\\text{{Wasted Output}} = {total_in}\\text{{ J}} - {useful_out}\\text{{ J}} = \\mathbf{{{wasted_out}\\text{{ J}}}}$$"
    )
    return {
        "id": f"ns7_et_22_{rng.randint(100000, 999999)}",
        "subskill": "22_calculating_wasted_energy_from_input_useful",
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
        "learning_objective_id": "ns7_et_22",
        "hints": {
            "tier_1": "Subtract useful output from total input.",
            "tier_2": f"{total_in} - {useful_out} = {wasted_out}.",
            "tier_3": f"{wasted_out} J.",
        },
        "misconception_tags": ["adding_instead_of_subtracting", "energy_lost_without_trace"],
    }


# 23. Calculating input energy from outputs
def arch_23_calculating_input_energy_from_outputs(rng: random.Random) -> Dict[str, Any]:
    outputs = [(150, 350, 500), (240, 560, 800), (80, 320, 400)]
    useful_j, wasted_j, input_j = rng.choice(outputs)
    prompt = (
        f"An electrical appliance produces **{useful_j} J** of useful work while releasing **{wasted_j} J** of wasted heat to the surroundings.\n\n"
        f"What was the **total electrical input energy** supplied to the appliance?"
    )
    correct = f"**{input_j} J**, because Total Input = Useful Output ({useful_j} J) + Wasted Output ({wasted_j} J)."
    distractors = [
        f"**{wasted_j - useful_j} J**, obtained by subtracting useful from wasted.",
        f"**{wasted_j * 2} J**, because input must double the waste.",
        f"**0 J**, because the appliance powers itself.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Energy Conservation Addition:**\n"
        f"$$\\text{{Total Input Energy}} = \\text{{Useful Output}} + \\text{{Wasted Output}}$$\n"
        f"$$\\text{{Total Input Energy}} = {useful_j}\\text{{ J}} + {wasted_j}\\text{{ J}} = \\mathbf{{{input_j}\\text{{ J}}}}$$"
    )
    return {
        "id": f"ns7_et_23_{rng.randint(100000, 999999)}",
        "subskill": "23_calculating_input_energy_from_outputs",
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
        "learning_objective_id": "ns7_et_23",
        "hints": {
            "tier_1": "Add useful output and wasted output together.",
            "tier_2": f"{useful_j} + {wasted_j} = {input_j}.",
            "tier_3": f"{input_j} J.",
        },
        "misconception_tags": ["subtracting_outputs_for_input", "ignoring_wasted_output_in_total"],
    }


# 24. Interpreting Sankey proportions visually
def arch_24_interpreting_sankey_proportions_visually(rng: random.Random) -> Dict[str, Any]:
    proportions = [
        ("the downward wasted arrow is three times wider than the horizontal useful arrow", "75% wasted and 25% useful", "inefficient"),
        ("the horizontal useful arrow is four times wider than the downward wasted arrow", "80% useful and 20% wasted", "highly efficient"),
    ]
    visual_desc, breakdown, status = rng.choice(proportions)
    prompt = (
        f"In a Sankey energy flow representation for an industrial machine, **{visual_desc}**.\n\n"
        f"What does this visual proportion reveal about the performance of the machine?"
    )
    correct = f"It indicates approximately **{breakdown}**, meaning the machine is **{status}**."
    distractors = [
        "It indicates that energy was destroyed inside the machine.",
        "It indicates that the machine creates free electricity out of cold air.",
        "It indicates that arrow widths were drawn randomly without scientific meaning.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Visual Interpretation of Sankey Arrows:**\n"
        f"- Arrow width is proportional to energy volume.\n"
        f"- When {visual_desc}, it reflects {breakdown}.\n"
        f"- Therefore, the system is classified as **{status}**."
    )
    return {
        "id": f"ns7_et_24_{rng.randint(100000, 999999)}",
        "subskill": "24_interpreting_sankey_proportions_visually",
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
        "learning_objective_id": "ns7_et_24",
        "hints": {
            "tier_1": "Wider arrow means more energy flowing through that path.",
            "tier_2": "Compare the relative widths of useful vs wasted arrows.",
            "tier_3": f"Approximately {breakdown}, meaning the machine is {status}.",
        },
        "misconception_tags": ["narrow_arrows_represent_more_energy", "visual_width_is_meaningless"],
    }


# 25. Distinguishing efficient from inefficient systems
def arch_25_distinguishing_efficient_from_inefficient_systems(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Device A converts 80% of input into useful work and 20% into wasted heat. Device B converts 15% of input into useful work and 85% into wasted heat.",
         "Device A is far more energy-efficient because a much larger percentage of its input energy accomplishes the intended task with minimal waste.")
    ]
    comparison, verdict = rng.choice(pairs)
    prompt = (
        f"Consider two competing mechanical devices:\n*{comparison}*\n\n"
        f"Which device is more energy-efficient, and why?"
    )
    correct = verdict
    distractors = [
        "Device B is more efficient because it produces much more wasted heat for the room.",
        "Both devices have identical efficiency because both obey conservation of energy.",
        "Neither device is efficient because neither produces nuclear energy.",
    ]
    options = _clean_options(correct, distractors, rng)
    sol = (
        f"**Energy Efficiency Definition:**\n"
        f"$$\\text{{Efficiency}} = \\frac{{\\text{{Useful Output}}}}{{\\text{{Total Input}}}} \\times 100\\%$$\n"
        f"- Device A: 80% efficient.\n"
        f"- Device B: 15% efficient.\n"
        f"Conclusion: {verdict}"
    )
    return {
        "id": f"ns7_et_25_{rng.randint(100000, 999999)}",
        "subskill": "25_distinguishing_efficient_from_inefficient_systems",
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
        "learning_objective_id": "ns7_et_25",
        "hints": {
            "tier_1": "Higher percentage of useful work means higher efficiency.",
            "tier_2": "80% useful is far better than 15% useful.",
            "tier_3": f"{verdict}",
        },
        "misconception_tags": ["efficiency_equals_power", "more_heat_means_better_efficiency"],
    }
