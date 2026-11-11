"""Grade 8 Natural Sciences: Term 3 - Series and Parallel Circuits Archetypes (01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/03. Series and parallel circuits.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List


def arch_01_definition_and_structure_of_series_circuit(rng: random.Random) -> Dict[str, Any]:
    context = rng.choice([
        ("decorative holiday light string", "all miniature bulbs are connected sequentially end-to-end"),
        ("classroom demonstration circuit", "a cell, switch, and two torch bulbs form a single loop"),
        ("simple torch flashlight", "the battery cells, switch, and single bulb form an unbroken pathway"),
    ])
    prompt = (
        f"Consider a {context[0]} where {context[1]}.\n\n"
        f"Which statement best defines a **series circuit** and its structural pathway?"
    )
    correct_opt = "A circuit providing only one continuous pathway for electric current to flow through all connected components."
    options = [
        correct_opt,
        "A circuit that provides multiple alternative pathways branching at junctions for current to split.",
        "A circuit where each component receives an independent direct connection to both terminals of the power source.",
        "A circuit where electric current flows only from the positive terminal to the switch and stops.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Definition of a Series Circuit:**\n"
        f"- In a series circuit, components are connected one after another in a single, unbranching pathway.\n"
        f"- All electrons must travel sequentially through every component in the loop.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_01_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "01_definition_and_structure_of_series_circuit",
        "question_family_id": "01_definition_and_structure_of_series_circuit",
        "hints": {
            "tier_1": "How many pathways are available for electric current in a series circuit?",
            "tier_2": "In series, there is only one pathway connecting all components sequentially.",
            "tier_3": "A circuit providing only one continuous pathway for electric current.",
        },
        "misconception_tags": ["confusing_series_and_parallel_pathways"],
    }


def arch_02_current_constancy_at_all_points_in_series_circuit(rng: random.Random) -> Dict[str, Any]:
    current_val = rng.choice([0.15, 0.2, 0.25, 0.35, 0.5])
    curr_str = f"{current_val}".replace(".", ",")
    pos_tested = rng.choice([
        ("between the positive battery terminal and the first bulb", "between the two bulbs"),
        ("between the two bulbs", "between the last bulb and the negative battery terminal"),
        ("between the switch and the first bulb", "between the second bulb and the battery"),
    ])
    prompt = (
        f"A series circuit consists of two identical light bulbs and an ammeter connected to a power supply.\n"
        f"When the ammeter is placed {pos_tested[0]}, it reads ${curr_str}\\text{{ A}}$.\n\n"
        f"What will the ammeter read when it is moved to a new position {pos_tested[1]}?"
    )
    wrong_half = f"{round(current_val / 2, 2)}".replace(".", ",")
    wrong_double = f"{round(current_val * 2, 2)}".replace(".", ",")
    correct_opt = f"Exactly ${curr_str}\\text{{ A}}$, because electric current is identical at all points in a series circuit."
    options = [
        correct_opt,
        f"${wrong_half}\\text{{ A}}$, because half of the electric current is consumed by the first bulb.",
        f"${wrong_double}\\text{{ A}}$, because electric current increases as charges accelerate through the conductor.",
        "0 A, because electric charge cannot pass between two resistive bulbs in series.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Current Constancy in Series:**\n"
        f"- In a series circuit, there is only one single pathway for electrons to flow.\n"
        f"- Electrons are not 'used up' or lost; the rate of charge flow past any cross-section is constant.\n"
        f"- Therefore: $I_1 = I_2 = I_3 = {curr_str}\\text{{ A}}$ everywhere in the circuit.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_02_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "02_current_constancy_at_all_points_in_series_circuit",
        "question_family_id": "02_current_constancy_at_all_points_in_series_circuit",
        "hints": {
            "tier_1": "Is electric current consumed as it moves through components in a single loop?",
            "tier_2": "Current is never used up; in series, the rate of flow is identical everywhere.",
            "tier_3": f"It remains exactly {curr_str} A at all points in a series circuit.",
        },
        "misconception_tags": ["current_attenuation_along_circuit"],
    }


def arch_03_effect_of_adding_resistors_in_series_on_total_resistance(rng: random.Random) -> Dict[str, Any]:
    n_resistors = rng.choice([2, 3, 4])
    res_val = rng.choice([5, 10, 15, 20])
    total_val = n_resistors * res_val
    prompt = (
        f"An electrical circuit initially contains one resistor with a resistance of ${res_val}\\ \\Omega$.\n"
        f"A learner adds {n_resistors - 1} more identical ${res_val}\\ \\Omega$ resistors in series into the same circuit.\n\n"
        f"What happens to the total overall resistance of the circuit?"
    )
    correct_opt = f"The total resistance increases to ${total_val}\\ \\Omega$, because series resistors add up sequentially."
    wrong_div = f"{round(res_val / n_resistors, 1)}".replace(".", ",")
    options = [
        correct_opt,
        f"The total resistance decreases to ${wrong_div}\\ \\Omega$, because more resistors offer more paths.",
        f"The total resistance remains ${res_val}\\ \\Omega$, because identical resistors cancel each other out.",
        "The total resistance drops to zero Ohms, creating a superconductor.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Resistance in Series:**\n"
        f"- When resistors are connected in series, each additional resistor opposes the flow of charge further.\n"
        f"- Total series resistance: $R_\\text{{total}} = R_1 + R_2 + \\dots + R_n$.\n"
        f"- For {n_resistors} identical resistors of ${res_val}\\ \\Omega$:\n"
        f"  $$R_\\text{{total}} = {n_resistors} \\times {res_val}\\ \\Omega = {total_val}\\ \\Omega$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_03_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "03_effect_of_adding_resistors_in_series_on_total_resistance",
        "question_family_id": "03_effect_of_adding_resistors_in_series_on_total_resistance",
        "hints": {
            "tier_1": "What happens to the total obstacle to charge flow when you place resistors one after another?",
            "tier_2": "In series, each resistor adds to the total resistance: R_total = R1 + R2 + ...",
            "tier_3": f"Total resistance increases to {total_val} Ohms.",
        },
        "misconception_tags": ["series_resistance_decrease_confusion"],
    }


def arch_04_effect_of_adding_bulbs_in_series_on_brightness_and_current(rng: random.Random) -> Dict[str, Any]:
    n_bulbs = rng.choice([2, 3, 4])
    prompt = (
        f"A circuit contains a single torch bulb connected to a $3\\text{{ V}}$ battery, glowing brightly.\n"
        f"If {n_bulbs - 1} more identical light bulbs are added in series into the circuit loop, what happens "
        f"to the electric current in the circuit and the brightness of each bulb?"
    )
    correct_opt = "The total current decreases, and each bulb glows significantly dimmer than the original single bulb."
    options = [
        correct_opt,
        "The total current increases, and all bulbs glow brighter than the original single bulb.",
        "The first bulb stays very bright, while the added bulbs do not light up at all.",
        "The current stays the same, and all bulbs continue to shine with full original brightness.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Adding Bulbs in Series:**\n"
        f"- Adding bulbs in series increases the total resistance of the circuit.\n"
        f"- By Ohm's law ($I = V / R$), increasing resistance with constant voltage causes the electric current to decrease.\n"
        f"- The battery voltage is divided equally among the {n_bulbs} identical bulbs ($V_\\text{{bulb}} = 3\\text{{ V}} / {n_bulbs}$).\n"
        f"- As each bulb receives less voltage and less current, all bulbs glow dimmer.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_04_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "04_effect_of_adding_bulbs_in_series_on_brightness_and_current",
        "question_family_id": "04_effect_of_adding_bulbs_in_series_on_brightness_and_current",
        "hints": {
            "tier_1": "Does adding more bulbs in series increase or decrease the total circuit resistance?",
            "tier_2": "More bulbs in series = higher resistance = less current = dimmer bulbs.",
            "tier_3": "Total current decreases, and each bulb glows dimmer.",
        },
        "misconception_tags": ["series_bulb_brightness_constancy"],
    }


def arch_05_ammeter_connection_in_series_and_low_internal_resistance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"An ammeter is a sensitive instrument used by scientists to measure electric current.\n\n"
        f"How must an ammeter be connected in an electrical circuit, and what internal resistance property does it possess?"
    )
    correct_opt = "Connected in series; it possesses near-zero (very low) internal resistance so it does not reduce the circuit current."
    options = [
        correct_opt,
        "Connected in parallel; it possesses near-zero internal resistance so all current flows through it.",
        "Connected in series; it possesses extremely high internal resistance so it blocks dangerous currents.",
        "Connected in parallel; it possesses infinite resistance to divide potential difference across the circuit.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Ammeter Connection Rules:**\n"
        f"- An ammeter measures the rate of charge flow (current) passing through a conductor loop.\n"
        f"- To measure this flow accurately, it must be inserted directly into the loop in **series**.\n"
        f"- It is designed with **extremely low internal resistance** so that inserting it does not alter or impede the circuit current.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_05_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "05_ammeter_connection_in_series_and_low_internal_resistance",
        "question_family_id": "05_ammeter_connection_in_series_and_low_internal_resistance",
        "hints": {
            "tier_1": "Does current flow through an ammeter or across it?",
            "tier_2": "An ammeter is connected in series and has very low resistance so it does not alter current.",
            "tier_3": "Connected in series with near-zero internal resistance.",
        },
        "misconception_tags": ["ammeter_voltmeter_connection_inversion"],
    }


def arch_06_effect_of_adding_cells_in_series_on_current_and_voltage(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([2, 3, 4])
    cell_v = 1.5
    total_v = round(n_cells * cell_v, 1)
    tot_str = f"{total_v}".replace(".", ",")
    prompt = (
        f"A laboratory circuit with two light bulbs is initially powered by a single $1{{,}}5\\text{{ V}}$ cell.\n"
        f"The experimenter then adds {n_cells - 1} more identical $1{{,}}5\\text{{ V}}$ cells in series with the first cell.\n\n"
        f"What is the total potential difference supplied, and how does this affect the electric current and bulb brightness?"
    )
    correct_opt = f"Total voltage increases to ${tot_str}\\text{{ V}}$, which increases the electric current and causes the bulbs to glow brighter."
    options = [
        correct_opt,
        f"Total voltage remains $1{{,}}5\\text{{ V}}$, but the current decreases because cells add extra resistance.",
        f"Total voltage drops to $0{{,}}5\\text{{ V}}$, causing the bulbs to glow dimmer.",
        f"Total voltage increases to ${tot_str}\\text{{ V}}$, but current stays unchanged because bulbs have fixed resistance.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Cells Connected in Series:**\n"
        f"- When identical cells are connected in series (positive terminal to negative terminal), their potential differences add together:\n"
        f"  $$V_\\text{{total}} = {n_cells} \\times 1{{,}}5\\text{{ V}} = {tot_str}\\text{{ V}}$$\n"
        f"- A higher total voltage provides more electrical push per unit charge.\n"
        f"- Since the circuit resistance remains constant, the current increases ($I = V / R$), making the bulbs shine brighter.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_06_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "06_effect_of_adding_cells_in_series_on_current_and_voltage",
        "question_family_id": "06_effect_of_adding_cells_in_series_on_current_and_voltage",
        "hints": {
            "tier_1": "Do voltages of cells add together when connected in series?",
            "tier_2": "In series, cell voltages add: 1.5 V + 1.5 V ... higher voltage drives greater current.",
            "tier_3": f"Total voltage is {tot_str} V, current increases, and bulbs glow brighter.",
        },
        "misconception_tags": ["series_cells_voltage_constancy"],
    }


def arch_07_broken_component_or_open_switch_consequence_in_series(rng: random.Random) -> Dict[str, Any]:
    n_bulbs = rng.choice([3, 4, 5])
    failed_idx = rng.choice([1, 2, n_bulbs])
    prompt = (
        f"A decorative lighting string consists of {n_bulbs} miniature light bulbs wired together in series.\n"
        f"During operation, the filament in bulb {failed_idx} melts and burns out (creating a physical break).\n\n"
        f"What happens to the remaining bulbs in this series circuit?"
    )
    correct_opt = "All remaining bulbs go out immediately, because the single conducting loop is broken and current ceases everywhere."
    options = [
        correct_opt,
        "The remaining bulbs stay lit and shine even brighter because electrical energy is shared among fewer bulbs.",
        "Only the bulbs located after bulb " + str(failed_idx) + " turn off, while bulbs before it remain on.",
        "The remaining bulbs begin to flash rapidly as current alternates back and forth.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Break in a Series Circuit:**\n"
        f"- In a series circuit, there is only one pathway for current to travel.\n"
        f"- When any single component fails or opens, an open circuit is created.\n"
        f"- Electrons cannot jump across the broken filament gap; electric current drops to zero throughout the entire circuit.\n"
        f"- Consequently, every bulb in the series circuit turns off immediately.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_07_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "07_broken_component_or_open_switch_consequence_in_series",
        "question_family_id": "07_broken_component_or_open_switch_consequence_in_series",
        "hints": {
            "tier_1": "Can current flow if there is a gap anywhere in a single closed loop?",
            "tier_2": "A broken bulb in series creates an open circuit, stopping current completely.",
            "tier_3": "All remaining bulbs go out immediately because the loop is broken.",
        },
        "misconception_tags": ["unidirectional_current_blockage_before_gap"],
    }


def arch_08_delocalised_electrons_instantaneous_conduction_in_circuit(rng: random.Random) -> Dict[str, Any]:
    distance = rng.choice(["a 100-metre long copper cable", "a domestic household wiring circuit", "a long laboratory circuit"])
    prompt = (
        f"When a switch is closed in {distance}, a light bulb turns on virtually instantaneously, "
        f"even though individual electrons drift through metal at a slow speed of less than a millimetre per second.\n\n"
        f"Which explanation accounts for this instantaneous response?"
    )
    correct_opt = "Delocalised electrons are already present throughout all parts of the conductor, and closing the switch sets all of them into motion simultaneously."
    options = [
        correct_opt,
        "Electrons shoot out of the battery terminal at the speed of light to reach the light bulb.",
        "The battery emits pure light rays through the hollow core of copper wires.",
        "Positive protons travel along the outside of the wire to activate the bulb first.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Instantaneous Conduction in Circuits:**\n"
        f"- Conducting wires are filled with a sea of delocalised valence electrons everywhere along their length.\n"
        f"- When the circuit is closed, an electric field is established across the entire circuit almost instantaneously.\n"
        f"- All electrons throughout the circuit begin drifting in unison at the same moment.\n"
        f"- Electrons already inside the bulb filament begin transferring energy immediately upon closure.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_08_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "08_delocalised_electrons_instantaneous_conduction_in_circuit",
        "question_family_id": "08_delocalised_electrons_instantaneous_conduction_in_circuit",
        "hints": {
            "tier_1": "Are copper wires empty before the battery is connected, or are electrons already present?",
            "tier_2": "Delocalised electrons exist everywhere in the wire; they all start moving together when switch closes.",
            "tier_3": "Electrons are already present throughout the conductor and move simultaneously.",
        },
        "misconception_tags": ["electrons_travel_from_battery_to_bulb_at_lightspeed"],
    }


def arch_09_definition_and_branch_structure_of_parallel_circuit(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Electric circuits can be arranged in either series or parallel configurations.\n\n"
        f"Which statement precisely describes the structure and defining characteristic of a **parallel circuit**?"
    )
    correct_opt = "A circuit that contains two or more separate branches (alternative pathways) for electric current to flow through."
    options = [
        correct_opt,
        "A circuit where all components must be connected in a single straight line with no junctions.",
        "A circuit where current flows simultaneously in opposite directions through a single wire.",
        "A circuit containing only direct current batteries and no resistors or switches.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Definition of a Parallel Circuit:**\n"
        f"- A parallel circuit offers more than one pathway for electrons to follow.\n"
        f"- The circuit splits into two or more branches at electrical junctions.\n"
        f"- Each parallel branch connects across the same common voltage nodes.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_09_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "09_definition_and_branch_structure_of_parallel_circuit",
        "question_family_id": "09_definition_and_branch_structure_of_parallel_circuit",
        "hints": {
            "tier_1": "How does the number of pathways in parallel differ from series?",
            "tier_2": "Parallel circuits contain two or more separate pathways (branches) for current.",
            "tier_3": "A circuit containing two or more separate branches for current to flow.",
        },
        "misconception_tags": ["confusing_series_and_parallel_pathways"],
    }


def arch_10_current_division_across_branches_in_parallel_circuit(rng: random.Random) -> Dict[str, Any]:
    n_branches = rng.choice([2, 3])
    total_i = rng.choice([0.6, 0.9, 1.2, 1.5, 1.8])
    branch_i = round(total_i / n_branches, 2)
    tot_str = f"{total_i}".replace(".", ",")
    br_str = f"{branch_i}".replace(".", ",")
    prompt = (
        f"A parallel circuit powered by a battery supplies a total main current of ${tot_str}\\text{{ A}}$.\n"
        f"The circuit divides into {n_branches} parallel branches, each containing an **identical** torch light bulb.\n\n"
        f"What is the electric current flowing through each individual branch?"
    )
    correct_opt = f"${br_str}\\text{{ A}}$, because identical branches offer equal resistance and split the total current equally."
    options = [
        correct_opt,
        f"${tot_str}\\text{{ A}}$, because every branch receives the full total current from the battery.",
        f"{round(total_i * n_branches, 1)} A, because parallel branches multiply the current by {n_branches}.",
        "0 A, because electric current cannot divide across junctions.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Current Division in Parallel Branches:**\n"
        f"- In a parallel circuit, total current ($I_\\text{{total}}$) divides among the available branches.\n"
        f"- When all {n_branches} branches contain identical components, they offer identical resistance.\n"
        f"- Therefore, current divides equally:\n"
        f"  $$I_\\text{{branch}} = \\frac{{I_\\text{{total}}}}{{{n_branches}}} = \\frac{{{tot_str}\\text{{ A}}}}{{{n_branches}}} = {br_str}\\text{{ A}}$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_10_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "10_current_division_across_branches_in_parallel_circuit",
        "question_family_id": "10_current_division_across_branches_in_parallel_circuit",
        "hints": {
            "tier_1": f"How is a total current of {tot_str} A divided among {n_branches} identical branches?",
            "tier_2": f"Divide total current by number of branches: {tot_str} / {n_branches}.",
            "tier_3": f"Each branch carries {br_str} A.",
        },
        "misconception_tags": ["parallel_current_equality_misconception"],
    }


def arch_11_sum_of_branch_currents_equals_total_main_current(rng: random.Random) -> Dict[str, Any]:
    i1 = rng.choice([0.2, 0.3, 0.4, 0.5])
    i2 = rng.choice([0.1, 0.25, 0.35, 0.6])
    i_total = round(i1 + i2, 2)
    i1_str = f"{i1}".replace(".", ",")
    i2_str = f"{i2}".replace(".", ",")
    tot_str = f"{i_total}".replace(".", ",")
    prompt = (
        f"A parallel circuit splits into two branches at junction P and recombines at junction Q.\n"
        f"An ammeter in branch 1 measures ${i1_str}\\text{{ A}}$, and an ammeter in branch 2 measures ${i2_str}\\text{{ A}}$.\n\n"
        f"What is the reading on the main ammeter connected in the main trunk before junction P?"
    )
    correct_opt = f"${tot_str}\\text{{ A}}$, because the main current equals the sum of the individual branch currents ($I_\\text{{total}} = I_1 + I_2$)."
    wrong_sub = f"{abs(round(i1 - i2, 2))}".replace(".", ",")
    options = [
        correct_opt,
        f"${i1_str}\\text{{ A}}$, because the main trunk current is determined only by the larger branch.",
        f"${wrong_sub}\\text{{ A}}$, because the two branch currents subtract from one another at the junction.",
        f"{round(i1 * i2, 2)} A, because parallel branches multiply electrical currents.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Kirchhoff's Current Law / Conservation of Charge:**\n"
        f"- Electric charge cannot accumulate at a junction nor vanish into nothing.\n"
        f"- The total current entering a junction must equal the sum of currents leaving the junction:\n"
        f"  $$I_\\text{{main}} = I_1 + I_2 = {i1_str}\\text{{ A}} + {i2_str}\\text{{ A}} = {tot_str}\\text{{ A}}$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_11_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "11_sum_of_branch_currents_equals_total_main_current",
        "question_family_id": "11_sum_of_branch_currents_equals_total_main_current",
        "hints": {
            "tier_1": "What is the relationship between the total current and branch currents in parallel?",
            "tier_2": f"Add the branch currents together: {i1_str} + {i2_str}.",
            "tier_3": f"Main current is {tot_str} A.",
        },
        "misconception_tags": ["conservation_of_charge_violation_in_parallel"],
    }


def arch_12_effect_of_adding_resistors_in_parallel_on_total_resistance(rng: random.Random) -> Dict[str, Any]:
    n_resistors = rng.choice([2, 3, 4])
    prompt = (
        f"A circuit contains a single resistor connected across a battery.\n"
        f"If {n_resistors - 1} more resistors are connected in **parallel** with the first resistor, "
        f"what happens to the total equivalent resistance of the circuit?"
    )
    correct_opt = "The total resistance decreases, because additional parallel branches provide extra pathways for electric charge to flow."
    options = [
        correct_opt,
        "The total resistance increases, because more resistors always create more total obstruction to current.",
        "The total resistance stays exactly the same, because each resistor acts independently.",
        "The total resistance fluctuates unpredictably between positive and negative values.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Resistance in Parallel Circuits:**\n"
        f"- Adding resistors in parallel creates alternative pathways for electrons.\n"
        f"- Even if each individual branch has resistance, providing more pathways makes it easier overall for charge to leave and return to the battery.\n"
        f"- Therefore, adding resistors in parallel **decreases** the overall circuit resistance.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_12_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "12_effect_of_adding_resistors_in_parallel_on_total_resistance",
        "question_family_id": "12_effect_of_adding_resistors_in_parallel_on_total_resistance",
        "hints": {
            "tier_1": "Does opening more pathways make it easier or harder for electrons to flow overall?",
            "tier_2": "More parallel branches = easier flow = total resistance decreases.",
            "tier_3": "The total resistance decreases because extra pathways are provided.",
        },
        "misconception_tags": ["parallel_resistance_additive_misconception"],
    }


def arch_13_doorway_school_hall_analogy_for_parallel_resistance_decrease(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In natural sciences, physical analogies help explain electrical behavior.\n"
        f"Imagine learners leaving a crowded school assembly hall through a single door. "
        f"If a second identical door is opened on the opposite side of the hall, learners exit much faster.\n\n"
        f"How does this doorway analogy explain the electrical behavior of a parallel circuit?"
    )
    correct_opt = "Opening a second door provides an alternative pathway, reducing overall obstruction (resistance) and increasing the rate of flow (current)."
    options = [
        correct_opt,
        "Opening a second door doubles the speed of each individual person while keeping the total exit rate identical.",
        "Opening a second door blocks the first door, forcing everyone to turn around in reverse flow.",
        "Opening a second door increases congestion and doubles the total resistance of the school hall.",
    ]
    rng.shuffle(options)
    sol = (
        f"**School Hall Doorway Analogy:**\n"
        f"- Single door = Single pathway (series): High resistance, slow flow rate of learners (charges).\n"
        f"- Two doors = Parallel pathways: Learners divide between both doors.\n"
        f"- The overall resistance to learners leaving the hall is halved, and the total exit rate (current) doubles.\n"
        f"- This illustrates why adding parallel branches decreases total resistance and increases total current.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_13_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "13_doorway_school_hall_analogy_for_parallel_resistance_decrease",
        "question_family_id": "13_doorway_school_hall_analogy_for_parallel_resistance_decrease",
        "hints": {
            "tier_1": "What happens to the crowd flow when an extra exit door is opened?",
            "tier_2": "More doors = less bottleneck/resistance = greater total flow rate.",
            "tier_3": "An alternative pathway reduces overall resistance and increases total current.",
        },
        "misconception_tags": ["doorway_analogy_inversion"],
    }


def arch_14_brightness_of_identical_bulbs_in_parallel_branches(rng: random.Random) -> Dict[str, Any]:
    v_source = rng.choice([3, 6, 9])
    prompt = (
        f"A circuit contains one light bulb connected across a ${v_source}\\text{{ V}}$ battery, glowing brightly.\n"
        f"A second identical light bulb is connected in **parallel** across the same battery.\n\n"
        f"How does the brightness of the two bulbs compare to each other and to the original single bulb?"
    )
    correct_opt = f"Both bulbs glow with equal brightness, and each glows just as brightly as the original single bulb because each receives the full ${v_source}\\text{{ V}}$."
    options = [
        correct_opt,
        "Both bulbs glow with only half of their original brightness because the battery voltage is split in two.",
        "The first bulb stays fully bright, while the second bulb glows much dimmer.",
        "Both bulbs turn off completely because parallel connections short-circuit the power supply.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Bulb Brightness in Parallel:**\n"
        f"- In a parallel circuit, every branch connects directly across the full potential difference of the power source.\n"
        f"- Each bulb receives the full ${v_source}\\text{{ V}}$ supply voltage ($V_1 = V_2 = {v_source}\\text{{ V}}$).\n"
        f"- Since their resistance is identical, each branch draws its full rated current ($I = V / R$).\n"
        f"- Therefore, both bulbs shine equally bright, matching the brightness of the single original bulb.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_14_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "14_brightness_of_identical_bulbs_in_parallel_branches",
        "question_family_id": "14_brightness_of_identical_bulbs_in_parallel_branches",
        "hints": {
            "tier_1": "Does connecting a bulb in a new parallel branch reduce the voltage across the first branch?",
            "tier_2": "Each parallel branch receives the full battery voltage, so brightness remains unchanged.",
            "tier_3": f"Both bulbs glow equally bright, each receiving the full {v_source} V.",
        },
        "misconception_tags": ["parallel_voltage_division_error"],
    }


def arch_15_independent_operation_of_parallel_branches_when_one_fails(rng: random.Random) -> Dict[str, Any]:
    n_bulbs = rng.choice([3, 4])
    prompt = (
        f"A laboratory parallel circuit contains {n_bulbs} identical light bulbs, each situated on its own parallel branch.\n"
        f"If the filament of one bulb burns out (creating a break in that branch), what happens to the remaining bulbs?"
    )
    correct_opt = "The remaining bulbs stay lit and maintain their normal brightness, because their separate conducting pathways remain closed."
    options = [
        correct_opt,
        "All remaining bulbs immediately turn off, because a broken component stops current in the entire circuit.",
        "The remaining bulbs become dimmer because electricity is diverted into the damaged bulb.",
        "The remaining bulbs blow up due to an immediate voltage surge.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Independent Operation of Parallel Branches:**\n"
        f"- Each parallel branch forms its own independent, closed circuit loop with the power supply.\n"
        f"- If one branch is disconnected or its bulb blows, the physical conducting loops of the other branches remain complete and intact.\n"
        f"- They continue receiving the full supply voltage and normal branch current.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_15_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "15_independent_operation_of_parallel_branches_when_one_fails",
        "question_family_id": "15_independent_operation_of_parallel_branches_when_one_fails",
        "hints": {
            "tier_1": "Is the pathway for the other bulbs broken when one branch fails in parallel?",
            "tier_2": "In parallel, each branch is independent; other bulbs stay lit normally.",
            "tier_3": "Remaining bulbs stay lit with normal brightness.",
        },
        "misconception_tags": ["series_dependency_assumed_for_parallel"],
    }


def arch_16_effect_of_adding_cells_in_parallel_on_voltage_and_current(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([2, 3, 4])
    cell_v = 1.5
    prompt = (
        f"A single light bulb is connected to one $1{{,}}5\\text{{ V}}$ cell in a simple circuit.\n"
        f"A learner adds {n_cells - 1} more identical $1{{,}}5\\text{{ V}}$ cells connected in **parallel** with the first cell.\n\n"
        f"What is the total potential difference across the circuit, and what happens to the bulb's brightness?"
    )
    correct_opt = f"The potential difference remains $1{{,}}5\\text{{ V}}$, and the bulb brightness does not change."
    wrong_v = f"{round(n_cells * cell_v, 1)}".replace(".", ",")
    options = [
        correct_opt,
        f"The potential difference increases to ${wrong_v}\\text{{ V}}$, and the bulb shines much brighter.",
        f"The potential difference drops to {round(cell_v / n_cells, 2)} V, and the bulb becomes extremely dim.",
        "The potential difference drops to 0 V, and the bulb turns off completely.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Cells Connected in Parallel:**\n"
        f"- When identical cells are connected in parallel (all positive terminals together and all negative terminals together), "
        f"the total potential difference remains equal to the voltage of a single cell:\n"
        f"  $$V_\\text{{total}} = 1{{,}}5\\text{{ V}}$$\n"
        f"- Because the voltage and load resistance are unchanged, the current through the bulb remains the same ($I = V / R$).\n"
        f"- Consequently, the bulb shines with the exact same brightness as with one cell.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_16_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "16_effect_of_adding_cells_in_parallel_on_voltage_and_current",
        "question_family_id": "16_effect_of_adding_cells_in_parallel_on_voltage_and_current",
        "hints": {
            "tier_1": "Does connecting cells in parallel increase the total voltage?",
            "tier_2": "Cells in parallel do NOT increase voltage; total voltage remains 1.5 V.",
            "tier_3": "Potential difference remains 1.5 V, and brightness is unchanged.",
        },
        "misconception_tags": ["parallel_cells_multiply_voltage_misconception"],
    }


def arch_17_longevity_and_capacity_of_cells_connected_in_parallel(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([2, 3, 4])
    prompt = (
        f"If connecting {n_cells} identical cells in parallel does not increase the voltage or make a light bulb brighter, "
        f"what is the practical benefit of connecting cells in parallel?"
    )
    correct_opt = f"The cells share the delivery of current equally, allowing the battery system to power the circuit for approximately {n_cells} times longer before discharging."
    options = [
        correct_opt,
        "It converts direct current (DC) into alternating current (AC) automatically.",
        "It eliminates all electrical resistance from the copper wires in the circuit.",
        "It allows the cells to recharge themselves spontaneously without any external energy input.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Advantage of Parallel Cells:**\n"
        f"- While the terminal voltage remains constant ($1{{,}}5\\text{{ V}}$), the total current drawn by the bulb is shared equally among the {n_cells} cells.\n"
        f"- Each individual cell only supplies $\\frac{{1}}{{{n_cells}}}$ of the total current:\n"
        f"  $$I_\\text{{cell}} = \\frac{{I_\\text{{total}}}}{{{n_cells}}}$$\n"
        f"- Because chemical energy is depleted at a fraction of the single-cell rate, the battery pack lasts approximately {n_cells} times longer.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_17_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "17_longevity_and_capacity_of_cells_connected_in_parallel",
        "question_family_id": "17_longevity_and_capacity_of_cells_connected_in_parallel",
        "hints": {
            "tier_1": "How much current does each cell supply when several cells share the load in parallel?",
            "tier_2": "Each cell supplies a smaller share of current, so the battery lasts longer.",
            "tier_3": f"Cells share current delivery and last approximately {n_cells} times longer.",
        },
        "misconception_tags": ["parallel_cells_useless_misconception"],
    }


def arch_18_switch_placement_in_main_circuit_versus_parallel_branch(rng: random.Random) -> Dict[str, Any]:
    target_branch = rng.choice(["Branch A (top branch)", "Branch B (bottom branch)"])
    prompt = (
        f"A parallel circuit consists of a battery and two parallel branches (Branch A and Branch B), each containing a bulb.\n"
        f"A technician wants to install a switch so that it turns off ONLY the bulb in {target_branch}, "
        f"while allowing the bulb in the other branch to remain continuously lit.\n\n"
        f"Where must this switch be placed?"
    )
    correct_opt = f"Directly inside {target_branch}, in series with its bulb before the branches recombine."
    options = [
        correct_opt,
        "In the main conducting trunk next to the battery, before the junction where the branches split.",
        "Across both branches in parallel, connecting their positive terminals together.",
        "Outside the circuit entirely, touching the plastic insulation of the battery.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Switch Placement in Parallel Circuits:**\n"
        f"- A switch placed in the **main trunk** controls the total current and turns off ALL branches simultaneously.\n"
        f"- A switch placed **inside a specific branch** controls current only within that individual branch.\n"
        f"- To control only {target_branch}, the switch must be placed directly within that branch in series with its bulb.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_18_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "18_switch_placement_in_main_circuit_versus_parallel_branch",
        "question_family_id": "18_switch_placement_in_main_circuit_versus_parallel_branch",
        "hints": {
            "tier_1": "Where does a switch need to be placed to interrupt current in only one branch?",
            "tier_2": "Place the switch directly inside the branch you want to control.",
            "tier_3": f"Directly inside {target_branch}.",
        },
        "misconception_tags": ["main_switch_versus_branch_switch_confusion"],
    }


def arch_19_domestic_household_wiring_rationale_for_parallel_circuits(rng: random.Random) -> Dict[str, Any]:
    appliances = rng.choice([
        ("refrigerator, television, and living room lamp"),
        ("microwave oven, kettle, and kitchen ceiling lights"),
        ("geyser, washing machine, and computer"),
    ])
    prompt = (
        f"In South African homes, appliances such as the {appliances} are connected to the electrical supply.\n\n"
        f"Why are domestic household electrical circuits wired in **parallel** rather than in series?"
    )
    correct_opt = "Every appliance receives the full mains voltage (230 V) and can be operated independently without affecting other appliances."
    options = [
        correct_opt,
        "Parallel wiring causes all appliances to turn off simultaneously when any single appliance is switched off.",
        "Parallel wiring increases total circuit resistance so that less electricity bill is charged.",
        "Parallel wiring prevents electricity from flowing to neighboring rooms.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Why Homes Are Wired in Parallel:**\n"
        f"1. **Full Voltage:** Every parallel branch receives the full standard mains potential difference ($230\\text{{ V}}$).\n"
        f"2. **Independent Operation:** Each appliance has its own dedicated switch; turning off or unplugging one appliance does not disrupt power to others.\n"
        f"3. **Reliability:** If one light bulb burns out, all other lights and appliances continue functioning normally.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_19_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "19_domestic_household_wiring_rationale_for_parallel_circuits",
        "question_family_id": "19_domestic_household_wiring_rationale_for_parallel_circuits",
        "hints": {
            "tier_1": "What would happen in a home if all lights were connected in series and one bulb blew?",
            "tier_2": "In parallel, each device gets full 230 V and independent switch control.",
            "tier_3": "Each appliance receives full 230 V and operates independently.",
        },
        "misconception_tags": ["domestic_series_wiring_misconception"],
    }


def arch_20_comparing_battery_drain_rate_in_series_versus_parallel(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Two identical $9\\text{{ V}}$ batteries are used in an experiment:\n"
        f"- Battery A powers two identical light bulbs connected in **series**.\n"
        f"- Battery B powers two identical light bulbs connected in **parallel**.\n\n"
        f"Which battery will run down (deplete its stored chemical energy) faster, and why?"
    )
    correct_opt = "Battery B will deplete faster, because the parallel circuit has lower total resistance and draws a significantly larger total current."
    options = [
        correct_opt,
        "Battery A will deplete faster, because series circuits have higher resistance which consumes more electrical charge.",
        "Both batteries will deplete at the exact same rate, because they have the same initial chemical energy and identical bulbs.",
        "Neither battery will deplete, because closed circuits recycle electrical energy indefinitely.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Battery Drain in Series vs Parallel:**\n"
        f"- In series (Battery A), total resistance is high ($R_\\text{{total}} = 2R$), resulting in a small current ($I = V / 2R$).\n"
        f"- In parallel (Battery B), total resistance is low ($R_\\text{{total}} = R / 2$), resulting in a much larger total current ($I = 2V / R$).\n"
        f"- Because Battery B supplies four times the current of Battery A, it converts chemical potential energy into electrical energy four times faster.\n"
        f"- Therefore, Battery B runs down much more quickly.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_20_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "20_comparing_battery_drain_rate_in_series_versus_parallel",
        "question_family_id": "20_comparing_battery_drain_rate_in_series_versus_parallel",
        "hints": {
            "tier_1": "Which circuit draws more total current from the battery: series or parallel?",
            "tier_2": "Parallel has lower resistance, drawing higher total current and depleting the battery faster.",
            "tier_3": "Battery B depletes faster because lower resistance draws greater total current.",
        },
        "misconception_tags": ["higher_resistance_drains_battery_faster_misconception"],
    }


def arch_21_ranking_bulb_brightness_in_series_versus_parallel_configurations(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Consider three separate circuits powered by identical $6\\text{{ V}}$ batteries with identical bulbs:\n"
        f"- **Circuit 1:** A single bulb connected alone.\n"
        f"- **Circuit 2:** Two bulbs connected in **series**.\n"
        f"- **Circuit 3:** Two bulbs connected in **parallel**.\n\n"
        f"Which option correctly ranks the brightness of individual bulbs in these circuits?"
    )
    correct_opt = "Bulbs in Circuit 3 and Circuit 1 shine with equal maximum brightness, while bulbs in Circuit 2 shine significantly dimmer."
    options = [
        correct_opt,
        "Bulbs in Circuit 2 shine brightest, followed by Circuit 3, with Circuit 1 being dimmest.",
        "All bulbs in all three circuits shine with identical brightness.",
        "Circuit 1 is brightest, Circuit 2 is medium, and Circuit 3 bulbs do not light up at all.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Bulb Brightness Comparison:**\n"
        f"- **Circuit 1 (Single bulb):** Receives full $6\\text{{ V}}$ $\\rightarrow$ Maximum brightness.\n"
        f"- **Circuit 3 (Parallel):** Each branch receives full $6\\text{{ V}}$ $\\rightarrow$ Equal maximum brightness to Circuit 1.\n"
        f"- **Circuit 2 (Series):** Voltage is divided equally ($3\\text{{ V}}$ each), and higher resistance halves the current $\\rightarrow$ Each bulb glows much dimmer.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_21_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "21_ranking_bulb_brightness_in_series_versus_parallel_configurations",
        "question_family_id": "21_ranking_bulb_brightness_in_series_versus_parallel_configurations",
        "hints": {
            "tier_1": "What voltage does each bulb receive in each circuit?",
            "tier_2": "Circuit 1 and Circuit 3 get 6 V per bulb. Circuit 2 gets only 3 V per bulb.",
            "tier_3": "Circuit 3 and Circuit 1 are brightest; Circuit 2 is dimmer.",
        },
        "misconception_tags": ["single_bulb_brighter_than_parallel_misconception"],
    }


def arch_22_calculating_branch_currents_from_total_and_other_branches(rng: random.Random) -> Dict[str, Any]:
    i_total = rng.choice([0.8, 1.0, 1.2, 1.5, 2.0])
    i_branch1 = round(i_total * rng.choice([0.3, 0.4, 0.6]), 2)
    i_branch2 = round(i_total - i_branch1, 2)
    tot_str = f"{i_total}".replace(".", ",")
    b1_str = f"{i_branch1}".replace(".", ",")
    b2_str = f"{i_branch2}".replace(".", ",")
    prompt = (
        f"A parallel circuit has an ammeter in the main trunk reading ${tot_str}\\text{{ A}}$.\n"
        f"The circuit divides into two unequal branches:\n"
        f"- An ammeter in Branch 1 reads ${b1_str}\\text{{ A}}$.\n\n"
        f"What is the reading on the ammeter placed in Branch 2?"
    )
    correct_opt = f"${b2_str}\\text{{ A}}$, calculated from $I_2 = I_\\text{{total}} - I_1 = {tot_str}\\text{{ A}} - {b1_str}\\text{{ A}}$."
    wrong_add = f"{round(i_total + i_branch1, 2)}".replace(".", ",")
    options = [
        correct_opt,
        f"${tot_str}\\text{{ A}}$, because every branch carries the total current.",
        f"${wrong_add}\\text{{ A}}$, because currents add up at the branch entrance.",
        f"${b1_str}\\text{{ A}}$, because all branches in parallel must carry identical current regardless of resistance.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Calculating Branch Current:**\n"
        f"- Total current entering a junction equals the sum of branch currents:\n"
        f"  $$I_\\text{{total}} = I_1 + I_2$$\n"
        f"- Rearranging to solve for the unknown Branch 2 current:\n"
        f"  $$I_2 = I_\\text{{total}} - I_1 = {tot_str}\\text{{ A}} - {b1_str}\\text{{ A}} = {b2_str}\\text{{ A}}$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_22_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "22_calculating_branch_currents_from_total_and_other_branches",
        "question_family_id": "22_calculating_branch_currents_from_total_and_other_branches",
        "hints": {
            "tier_1": f"How do you find the missing branch current when total is {tot_str} A and Branch 1 is {b1_str} A?",
            "tier_2": f"Subtract Branch 1 from total: {tot_str} - {b1_str}.",
            "tier_3": f"Branch 2 current is {b2_str} A.",
        },
        "misconception_tags": ["branch_current_conservation_error"],
    }


def arch_23_calculating_total_current_from_identical_parallel_branches(rng: random.Random) -> Dict[str, Any]:
    n_branches = rng.choice([3, 4, 5])
    branch_curr = rng.choice([0.15, 0.25, 0.3, 0.4])
    total_curr = round(n_branches * branch_curr, 2)
    br_str = f"{branch_curr}".replace(".", ",")
    tot_str = f"{total_curr}".replace(".", ",")
    prompt = (
        f"A laboratory parallel circuit contains {n_branches} identical parallel branches.\n"
        f"An ammeter inside one of the branches reads a current of ${br_str}\\text{{ A}}$.\n\n"
        f"What is the total current flowing out of the battery in the main trunk of the circuit?"
    )
    correct_opt = f"${tot_str}\\text{{ A}}$, because total current is the sum of all {n_branches} identical branch currents (${n_branches} \\times {br_str}\\text{{ A}}$)."
    options = [
        correct_opt,
        f"${br_str}\\text{{ A}}$, because the battery only supplies the amount of current seen in any one branch.",
        f"{round(branch_curr / n_branches, 3)} A, because total current is divided by the number of branches.",
        "0 A, because parallel branches cancel each other out at the battery terminal.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Calculating Total Current from Identical Branches:**\n"
        f"- Since all {n_branches} branches are identical, each draws ${br_str}\\text{{ A}}$.\n"
        f"- Total current entering and leaving the power source is the sum of all branch currents:\n"
        f"  $$I_\\text{{total}} = {n_branches} \\times I_\\text{{branch}} = {n_branches} \\times {br_str}\\text{{ A}} = {tot_str}\\text{{ A}}$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_23_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "23_calculating_total_current_from_identical_parallel_branches",
        "question_family_id": "23_calculating_total_current_from_identical_parallel_branches",
        "hints": {
            "tier_1": f"If each of {n_branches} branches draws {br_str} A, what is the combined current drawn from the cell?",
            "tier_2": f"Multiply branch current by number of branches: {n_branches} x {br_str}.",
            "tier_3": f"Total current is {tot_str} A.",
        },
        "misconception_tags": ["total_current_equals_single_branch_misconception"],
    }


def arch_24_relative_resistance_of_copper_aluminium_zinc_nichrome_wires(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Four wires of identical length and cross-sectional thickness made of copper, aluminium, zinc, "
        f"and nichrome are tested in an electrical circuit.\n\n"
        f"Which list correctly arranges these metals in order of **increasing electrical resistance** (from lowest resistance to highest resistance)?"
    )
    correct_opt = "Copper < Aluminium < Zinc < Nichrome"
    options = [
        correct_opt,
        "Nichrome < Zinc < Aluminium < Copper",
        "Zinc < Nichrome < Copper < Aluminium",
        "Aluminium < Copper < Nichrome < Zinc",
    ]
    rng.shuffle(options)
    sol = (
        f"**Electrical Resistance of Common Metals:**\n"
        f"- **Copper:** Extremely low resistance; best common conductor, used for connecting wires.\n"
        f"- **Aluminium:** Very low resistance; slightly higher than copper, lightweight.\n"
        f"- **Zinc:** Moderate resistance; higher than copper and aluminium.\n"
        f"- **Nichrome (Nickel-Chromium alloy):** High resistance; heats up strongly when current flows, used in heating elements.\n"
        f"- Order of increasing resistance: **Copper < Aluminium < Zinc < Nichrome**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_24_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "24_relative_resistance_of_copper_aluminium_zinc_nichrome_wires",
        "question_family_id": "24_relative_resistance_of_copper_aluminium_zinc_nichrome_wires",
        "hints": {
            "tier_1": "Which metal is the best conductor (lowest resistance) and which is used in heaters (highest)?",
            "tier_2": "Copper has lowest resistance; nichrome has highest resistance.",
            "tier_3": "Copper < Aluminium < Zinc < Nichrome.",
        },
        "misconception_tags": ["metal_resistivity_order_confusion"],
    }


def arch_25_investigating_qualitative_resistance_using_bulb_brightness(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("copper wire", "nichrome wire", "copper produces a much brighter glow than nichrome"),
        ("thick copper wire", "thin zinc wire", "thick copper produces a much brighter glow than thin zinc"),
        ("aluminium wire", "nichrome wire", "aluminium produces a much brighter glow than nichrome"),
    ])
    prompt = (
        f"A learner constructs an open test circuit with a cell and a torch bulb. "
        f"When testing two wires of equal length and diameter, the learner observes that the {pair[2]}.\n\n"
        f"What valid scientific conclusion can the learner draw regarding the electrical resistance of the two wires?"
    )
    correct_opt = f"The wire producing the brighter glow has lower resistance, allowing a larger electric current to reach the bulb."
    options = [
        correct_opt,
        "The wire producing the brighter glow has higher resistance, which forces extra voltage into the bulb.",
        "Both wires have identical resistance, but the dimmer wire creates negative electric charges.",
        "Bulb brightness is completely unrelated to the electrical resistance of conducting wires.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Qualitative Resistance Investigation:**\n"
        f"- Resistance is the opposition to the flow of electric charge.\n"
        f"- In a circuit with constant voltage, a lower resistance material allows more current to flow ($I = V / R$).\n"
        f"- Higher current delivers more energy per second to the bulb filament, causing it to glow brighter.\n"
        f"- Therefore, a brighter bulb indicates that the inserted test wire offers lower electrical resistance.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_25_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "25_investigating_qualitative_resistance_using_bulb_brightness",
        "question_family_id": "25_investigating_qualitative_resistance_using_bulb_brightness",
        "hints": {
            "tier_1": "Does a brighter bulb mean more current or less current is flowing?",
            "tier_2": "More current = lower resistance of the test wire = brighter bulb.",
            "tier_3": "Brighter glow indicates lower electrical resistance.",
        },
        "misconception_tags": ["brightness_resistance_inversion"],
    }
