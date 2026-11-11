"""Grade 8 Natural Sciences: Term 3 - Energy Transfer in Electrical Systems Archetypes (01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/01. Energy transfer in electrical systems.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List


def arch_01_definition_of_electric_current_and_amperes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In physics and natural sciences, current electricity powers homes and industries.\n\n"
        f"Which statement provides the precise scientific definition of an **electric current** and its SI unit of measurement?"
    )
    correct_opt = "The rate of flow of electrical charge (delocalised electrons) through a closed conducting circuit, measured in Amperes (A)."
    options = [
        correct_opt,
        "The total electrical energy stored inside a chemical battery, measured in Volts (V).",
        "The speed at which copper atoms travel along a wire, measured in metres per second.",
        "The frictional resistance of plastic insulation, measured in Ohms."
    ]
    rng.shuffle(options)
    sol = (
        f"**Definition of Electric Current:**\n"
        f"- Electric current ($I$) is defined as the rate at which charge ($Q$) passes a given cross-section of a conductor:\n"
        f"  $$I = \\frac{{Q}}{{t}}$$\n"
        f"- Charge is measured in Coulombs ($C$), time in seconds ($s$), and current in **Amperes** ($A$), where $1\\text{{ A}} = 1\\text{{ Coulomb per second}}$.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_01_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "01_definition_of_electric_current_and_amperes",
        "question_family_id": "01_definition_of_electric_current_and_amperes",
        "hints": {
            "tier_1": "What is electric current the flow of, and what unit measures it?",
            "tier_2": "Current is the rate of flow of charge, measured in Amperes.",
            "tier_3": "Rate of flow of electrical charge, measured in Amperes (A)."
        },
        "misconception_tags": ["confusing_current_and_voltage"]
    }


def arch_02_role_of_delocalised_electrons_in_metals(rng: random.Random) -> Dict[str, Any]:
    metals = ["copper", "aluminium", "silver", "brass"]
    m = rng.choice(metals)
    prompt = (
        f"Solid conductors such as **{m}** wire are outstanding conductors of electric current.\n\n"
        f"What atomic structure feature of metals enables electric current to flow through them?"
    )
    correct_opt = "Metals have metallic bonding with a lattice of positive ions surrounded by a 'sea' of delocalised valence electrons that are free to drift through the material."
    options = [
        correct_opt,
        "Positive atomic nuclei detach and swim freely through the wire from one end to the other.",
        "Metals contain hollow microscopic tunnels that suck in atmospheric lightning.",
        "Metal atoms dissolve into liquid electrons whenever a switch is closed."
    ]
    rng.shuffle(options)
    sol = (
        f"**Delocalised Electrons in Metallic Conduction:**\n"
        f"1. In metallic bonding, outer valence electrons are not bound to individual atoms.\n"
        f"2. Instead, they form a shared **sea of delocalised electrons** moving between fixed positive metal ions.\n"
        f"3. When a potential difference (voltage) is applied across the conductor, these delocalised electrons drift in a coordinated direction, constituting an **electric current**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_02_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "02_role_of_delocalised_electrons_in_metals",
        "question_family_id": "02_role_of_delocalised_electrons_in_metals",
        "hints": {
            "tier_1": "What particles are free to move inside a metal wire?",
            "tier_2": "Delocalised (free) valence electrons are free to move.",
            "tier_3": "A lattice of positive ions with a sea of delocalised valence electrons free to drift."
        },
        "misconception_tags": ["protons_drift_in_metals"]
    }


def arch_03_conventional_current_versus_electron_flow(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In electrical circuit theory, scientists distinguish between **conventional current** and actual **electron flow**.\n\n"
        f"Which statement correctly contrasts the directions of conventional current and electron flow in an external circuit?"
    )
    correct_opt = "Conventional current flows from positive (+) to negative (-), while actual electron flow is from negative (-) to positive (+)."
    options = [
        correct_opt,
        "Conventional current flows from negative (-) to positive (+), while electron flow is from positive (+) to negative (-).",
        "Both conventional current and electron flow travel from positive (+) to positive (+).",
        "Conventional current moves in a circle clockwise while electrons move counter-clockwise in all circuits."
    ]
    rng.shuffle(options)
    sol = (
        f"**Conventional Current vs Real Electron Flow:**\n"
        f"1. **Historical convention (Benjamin Franklin):** Current was assumed to be the flow of positive fluid from the **positive (+) terminal to the negative (-) terminal**.\n"
        f"2. **Physical reality:** Electrons are negative particles and are repelled by the negative terminal and attracted to the positive terminal: **negative (-) to positive (+)**.\n"
        f"3. Science and engineering still use **conventional current** (+ to -) for circuit analysis diagrams.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_03_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "03_conventional_current_versus_electron_flow",
        "question_family_id": "03_conventional_current_versus_electron_flow",
        "hints": {
            "tier_1": "Which way do negative electrons naturally flow: towards positive or negative?",
            "tier_2": "Electrons flow from - to +; conventional current is defined from + to -.",
            "tier_3": "Conventional current is (+) to (-); electron flow is (-) to (+)."
        },
        "misconception_tags": ["electrons_flow_positive_to_negative"]
    }


def arch_04_requirements_for_a_complete_closed_circuit(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A student builds an electrical circuit consisting of a cell, copper connecting wires, a switch, and a light bulb. "
        f"For the light bulb to light up continuously, two fundamental conditions must be satisfied.\n\n"
        f"What are these two mandatory requirements?"
    )
    correct_opt = "There must be an unbroken closed conducting loop, and there must be an energy source (cell/battery) providing potential difference."
    options = [
        correct_opt,
        "The circuit must be open to the air so electrons can absorb oxygen, and all wires must be made of plastic.",
        "The switch must be open at all times, and the wires must be kept in ice water.",
        "A light bulb requires zero electrical energy and only glows when exposed to direct sunlight."
    ]
    rng.shuffle(options)
    sol = (
        f"**Two Conditions for Electric Current:**\n"
        f"1. **A complete, closed conducting path (closed circuit):** Any break, gap, or open switch halts electron flow immediately.\n"
        f"2. **A source of electrical energy (cell, battery, generator):** Provides the electromotive force (potential difference) that pushes charges through resistance.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_04_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "04_requirements_for_a_complete_closed_circuit",
        "question_family_id": "04_requirements_for_a_complete_closed_circuit",
        "hints": {
            "tier_1": "Does current flow if the loop is broken or if there is no battery?",
            "tier_2": "Need an unbroken loop and an energy source (cell/battery).",
            "tier_3": "Unbroken closed conducting loop and an energy source providing potential difference."
        },
        "misconception_tags": ["open_circuit_conducts_current"]
    }


def arch_05_identifying_circuit_symbols_cell_battery_switch(rng: random.Random) -> Dict[str, Any]:
    components = [
        ("an electric cell", "a long thin line (representing positive terminal) parallel to a shorter thicker line (negative terminal)"),
        ("a multi-cell battery", "two or more pairs of long thin and short thick parallel lines connected in series with dashed or solid links"),
        ("an open switch", "a break in the conducting line with an angled line lifted away from a terminal dot"),
        ("a closed switch", "a straight conducting line bridging two terminal dots, completing the path")
    ]
    name, description = rng.choice(components)
    prompt = (
        f"Standard circuit diagrams use universal internationally recognised schematic symbols.\n\n"
        f"Which circuit component is represented symbolically by **{description}**?"
    )
    correct_opt = name.capitalize()
    wrong_opts = [c[0].capitalize() for c in components if c[0] != name]
    options = [correct_opt] + wrong_opts[:3]
    rng.shuffle(options)
    sol = (
        f"**Standard Circuit Symbols:**\n"
        f"- Cell: One long thin line (+) and one short thick line (-).\n"
        f"- Battery: Multiple cells in series.\n"
        f"- Open switch: Angled gap breaking connection.\n"
        f"- Closed switch: Closed bridge line.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_05_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "05_identifying_circuit_symbols_cell_battery_switch",
        "question_family_id": "05_identifying_circuit_symbols_cell_battery_switch",
        "hints": {
            "tier_1": "Recall the standard schematic representation for electrical components.",
            "tier_2": f"Description matches: {description}.",
            "tier_3": f"This symbol represents {correct_opt}."
        },
        "misconception_tags": ["confusing_circuit_symbols"]
    }


def arch_06_identifying_circuit_symbols_bulb_resistor_meters(rng: random.Random) -> Dict[str, Any]:
    symbols = [
        ("a light bulb (lamp)", "a circle with a cross (X) inside it"),
        ("a fixed resistor", "a plain open rectangle (or a continuous zigzag line)"),
        ("an ammeter", "a circle containing a capital letter 'A'"),
        ("a voltmeter", "a circle containing a capital letter 'V'")
    ]
    name, sym_desc = rng.choice(symbols)
    prompt = (
        f"In an engineering schematic, a component is represented by **{sym_desc}**.\n\n"
        f"Which electrical component does this symbol denote?"
    )
    correct_opt = name.capitalize()
    wrong_opts = [s[0].capitalize() for s in symbols if s[0] != name]
    options = [correct_opt] + wrong_opts[:3]
    rng.shuffle(options)
    sol = (
        f"**Component Schematic Symbols:**\n"
        f"- Circle with cross (X) = Light bulb / lamp\n"
        f"- Rectangle (or zigzag) = Resistor\n"
        f"- Circle with 'A' = Ammeter (measures current)\n"
        f"- Circle with 'V' = Voltmeter (measures potential difference)\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_06_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "06_identifying_circuit_symbols_bulb_resistor_meters",
        "question_family_id": "06_identifying_circuit_symbols_bulb_resistor_meters",
        "hints": {
            "tier_1": "Look at the symbol description.",
            "tier_2": f"Circle with {sym_desc[-5:] if 'circle' in sym_desc else sym_desc}.",
            "tier_3": f"This symbol denotes {correct_opt}."
        },
        "misconception_tags": ["confusing_meter_symbols"]
    }


def arch_07_distinguishing_single_cell_from_multi_cell_battery(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([2, 3, 4])
    v_cell = 1.5
    v_total = n_cells * v_cell
    v_str = f"{v_total}".replace(".", "{,}")
    prompt = (
        f"In everyday English, people often refer to a single AA cylinder as a 'battery'. "
        f"What is the precise distinction in physical science between an **electric cell** and a **battery**?"
    )
    correct_opt = f"A cell is a single individual electrochemical unit (typically 1,5 V), while a battery consists of two or more cells connected together in combination (e.g. {n_cells} cells in series giving {v_str} V)."
    options = [
        correct_opt,
        "A cell operates on alternating current (AC) while a battery operates on nuclear power.",
        "Cells are only found in living biological tissues, while batteries are found in rocks.",
        "There is zero scientific distinction; the two words are exact synonyms with identical technical definitions."
    ]
    rng.shuffle(options)
    sol = (
        f"**Scientific Distinction: Cell vs Battery:**\n"
        f"- **Cell:** A single unit that converts chemical energy into electrical energy (e.g. one AA, AAA, or D unit of $1{{,}}5\\text{{ V}}$).\n"
        f"- **Battery:** A collection or 'battery' of two or more cells linked together (e.g. a $9\\text{{ V}}$ smoke alarm battery contains 6 internal $1{{,}}5\\text{{ V}}$ cells in series; a car battery contains 6 lead-acid cells of $2\\text{{ V}}$ each to give $12\\text{{ V}}$).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_07_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "07_distinguishing_single_cell_from_multi_cell_battery",
        "question_family_id": "07_distinguishing_single_cell_from_multi_cell_battery",
        "hints": {
            "tier_1": "Is a battery one cell or a group of cells?",
            "tier_2": "A cell is a single unit; a battery is two or more cells connected together.",
            "tier_3": "A cell is a single unit; a battery consists of two or more cells connected together."
        },
        "misconception_tags": ["cell_and_battery_are_identical"]
    }


def arch_08_chemical_energy_conversion_inside_cells(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"An electrochemical cell (such as an alkaline torch cell or zinc-carbon dry cell) powers an electric circuit.\n\n"
        f"What energy conversion takes place inside the cell to maintain the flow of electric current?"
    )
    correct_opt = "Chemical potential energy stored within the electrolyte and electrodes is converted into electrical energy."
    options = [
        correct_opt,
        "Nuclear energy is converted directly into magnetic gravitational waves.",
        "Thermal energy from the room is absorbed and converted into physical electrons.",
        "Light energy inside the sealed metal casing is converted into sound."
    ]
    rng.shuffle(options)
    sol = (
        f"**Energy Transformation in Electrochemical Cells:**\n"
        f"1. Spontaneous redox chemical reactions occur between the metal electrodes and the electrolyte paste inside the cell.\n"
        f"2. These chemical reactions release electrons at the negative terminal (anode) and accept electrons at the positive terminal (cathode).\n"
        f"3. Thus, **chemical potential energy** is converted into **electrical potential energy** that drives current through the external circuit.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_08_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "08_chemical_energy_conversion_inside_cells",
        "question_family_id": "08_chemical_energy_conversion_inside_cells",
        "hints": {
            "tier_1": "What type of energy is stored in the chemicals inside a battery?",
            "tier_2": "Chemical potential energy transforms into electrical energy.",
            "tier_3": "Chemical potential energy is converted into electrical energy."
        },
        "misconception_tags": ["batteries_store_pure_electricity"]
    }


def arch_09_environmental_dangers_of_disposing_batteries(rng: random.Random) -> Dict[str, Any]:
    toxins = [
        ("lead and sulfuric acid", "lead-acid car batteries", "brain damage, nervous system disorders, and heavy soil contamination"),
        ("cadmium and nickel", "NiCd rechargeable power tool batteries", "kidney failure, lung disease, and bioaccumulation in aquatic food chains"),
        ("mercury and lithium", "button cell watch batteries and lithium-ion phone batteries", "severe environmental toxicity and potential explosive landfill fires")
    ]
    pollutants, source, harm = rng.choice(toxins)
    prompt = (
        f"Discarding exhausted batteries in municipal household trash heaps and open landfills poses serious environmental and health hazards. "
        f"For example, **{source}** contain toxic chemicals like **{pollutants}**.\n\n"
        f"What ecological harm occurs when these batteries corrode in unlined landfills?"
    )
    correct_opt = f"The heavy metals and corrosive chemicals leak out into soil and groundwater, causing {harm}."
    options = [
        correct_opt,
        "The dead batteries release millions of volts that shock earthworms into extinction.",
        "The batteries produce nuclear radiation that creates radioactive thunderstorms.",
        "Corroding batteries absorb all carbon dioxide from the air and cause freezing."
    ]
    rng.shuffle(options)
    sol = (
        f"**Battery Recycling and Environmental Toxicology:**\n"
        f"- Batteries contain toxic heavy metals ({pollutants}) and corrosive chemicals.\n"
        f"- When dumped in standard municipal landfills, moisture and acids cause the metal casings to corrode.\n"
        f"- Toxic heavy metals leach into subterranean aquifers and municipal water supplies, causing {harm}.\n"
        f"- Batteries must be separated and taken to specialized hazardous e-waste recycling depots.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_09_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "09_environmental_dangers_of_disposing_batteries",
        "question_family_id": "09_environmental_dangers_of_disposing_batteries",
        "hints": {
            "tier_1": "What leaches into soil and groundwater from corroding batteries?",
            "tier_2": "Toxic heavy metals leach into groundwater, causing severe health hazards.",
            "tier_3": f"Heavy metals and corrosive chemicals leak into soil and groundwater, causing {harm}."
        },
        "misconception_tags": ["batteries_are_harmless_organic_waste"]
    }


def arch_10_definition_and_nature_of_electrical_resistance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In an electric circuit, every component possesses a property called **electrical resistance** ($R$), measured in Ohms ($\\Omega$).\n\n"
        f"What is the physical cause and definition of electrical resistance at the particle level?"
    )
    correct_opt = "The opposition to the flow of electric current caused by moving delocalised electrons colliding with vibrating positive metal ions in the conductor lattice."
    options = [
        correct_opt,
        "The speed at which current travels through empty space without any collisions.",
        "The chemical attraction between the battery's plastic cover and atmospheric nitrogen.",
        "The magnetic force that pulls electrons backward towards the wall plug."
    ]
    rng.shuffle(options)
    sol = (
        f"**Mechanism of Electrical Resistance:**\n"
        f"1. When an electric field drives delocalised electrons through a conductor, they do not travel in a straight frictionless path.\n"
        f"2. Electrons constantly collide with the vibrating positive ions in the metallic crystal lattice.\n"
        f"3. Each collision transfers kinetic energy from the electrons to the ions (increasing ionic vibration -> generating heat).\n"
        f"4. This opposition to the free movement of charge is **electrical resistance** ($R = \\frac{{V}}{{I}}$).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_10_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "10_definition_and_nature_of_electrical_resistance",
        "question_family_id": "10_definition_and_nature_of_electrical_resistance",
        "hints": {
            "tier_1": "What collides with what inside the metal wire?",
            "tier_2": "Drifting electrons collide with vibrating lattice ions, opposing current.",
            "tier_3": "Opposition to current flow caused by electrons colliding with lattice ions."
        },
        "misconception_tags": ["resistance_is_a_friction_of_air"]
    }


def arch_11_four_factors_affecting_wire_resistance_overview(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A laboratory experiment investigates the electrical resistance of various conducting wires.\n\n"
        f"Which list correctly identifies the **four physical factors** that govern the resistance of a metal conducting wire?"
    )
    correct_opt = "Length of the wire, thickness (cross-sectional area), type of material, and temperature of the wire."
    options = [
        correct_opt,
        "Colour of the insulation plastic, brand of the battery, volume of the room, and air humidity.",
        "Weight of the switch, shape of the plug pins, ceiling height, and daylight intensity.",
        "Number of protons in the battery, price of the wire, age of the electrician, and magnetic north."
    ]
    rng.shuffle(options)
    sol = (
        f"**Four Factors Influencing Resistance:**\n"
        f"1. **Length ($L$):** Longer wire = more resistance ($R \\propto L$).\n"
        f"2. **Thickness / Cross-sectional Area ($A$):** Thicker wire = less resistance ($R \\propto \\frac{{1}}{{A}}$).\n"
        f"3. **Material:** Different metals have different atomic lattices and electron densities (resistivity $\\rho$).\n"
        f"4. **Temperature ($T$):** Higher temperature = greater ionic vibration = higher resistance.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_11_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "11_four_factors_affecting_wire_resistance_overview",
        "question_family_id": "11_four_factors_affecting_wire_resistance_overview",
        "hints": {
            "tier_1": "Think about wire dimensions, what it's made of, and how hot it is.",
            "tier_2": "Length, thickness, material, and temperature.",
            "tier_3": "Length, thickness (cross-sectional area), material, and temperature."
        },
        "misconception_tags": ["insulation_colour_affects_resistance"]
    }


def arch_12_effect_of_wire_length_on_resistance(rng: random.Random) -> Dict[str, Any]:
    l1 = rng.choice([10, 20])
    l2 = l1 * rng.choice([2, 3, 4])
    factor = l2 // l1
    prompt = (
        f"Two nichrome wires have identical thickness and temperature. Wire A is {l1} cm long, while Wire B is {l2} cm long ({factor} times longer).\n\n"
        f"How does the electrical resistance of Wire B compare to Wire A, and why?"
    )
    correct_opt = f"Wire B has {factor} times more resistance, because electrons must travel through a longer lattice of ions, suffering proportionally more collisions."
    options = [
        correct_opt,
        f"Wire B has {factor} times less resistance, because long wires allow electrons to build up supersonic speed.",
        "Both wires have identical resistance because length has zero effect on electrical flow.",
        f"Wire B has {factor * factor} times less resistance because longer wires are colder."
    ]
    rng.shuffle(options)
    sol = (
        f"**Resistance Proportionality to Length:**\n"
        f"- Resistance is directly proportional to conductor length: $R \\propto L$.\n"
        f"- As length increases by a factor of {factor} (from {l1} cm to {l2} cm), drifting electrons encounter {factor} times as many metal ions in their path.\n"
        f"- Therefore, resistance increases by {factor} times.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_12_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "12_effect_of_wire_length_on_resistance",
        "question_family_id": "12_effect_of_wire_length_on_resistance",
        "hints": {
            "tier_1": "Does a longer wire have more or less resistance?",
            "tier_2": f"Resistance is directly proportional to length: {factor} times longer = {factor} times more resistance.",
            "tier_3": f"Wire B has {factor} times more resistance because electrons encounter more collisions."
        },
        "misconception_tags": ["longer_wires_have_less_resistance"]
    }


def arch_13_effect_of_wire_thickness_cross_section_on_resistance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Consider two copper wires of equal length: Wire 1 is a very thin filament ($0{{,}}2\\text{{ mm}}$ diameter), while Wire 2 is a thick cable ($2{{,}}0\\text{{ mm}}$ diameter).\n\n"
        f"Which wire has the **lower resistance**, and what is the scientific analogy that explains this?"
    )
    correct_opt = "Wire 2 (thick cable) has much lower resistance, just as a wide multi-lane highway allows far more cars to flow easily with less congestion than a narrow single-lane alley."
    options = [
        correct_opt,
        "Wire 1 (thin filament) has lower resistance because electrons can easily squeeze past each other.",
        "Both wires have identical resistance because copper is copper regardless of thickness.",
        "Wire 2 has zero resistance because thick copper is an absolute superconductor at room temperature."
    ]
    rng.shuffle(options)
    sol = (
        f"**Cross-Sectional Area and Resistance:**\n"
        f"- Resistance is inversely proportional to cross-sectional area: $R \\propto \\frac{{1}}{{A}}$.\n"
        f"- A thicker conductor has a larger cross-sectional area, providing vastly more parallel paths for delocalised electrons to drift through simultaneously.\n"
        f"- More pathways = less congestion = lower overall electrical resistance.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_13_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "13_effect_of_wire_thickness_cross_section_on_resistance",
        "question_family_id": "13_effect_of_wire_thickness_cross_section_on_resistance",
        "hints": {
            "tier_1": "Do thick wires have higher or lower resistance than thin wires?",
            "tier_2": "Thicker wires have more space for electrons to flow, so lower resistance.",
            "tier_3": "Wire 2 (thick cable) has much lower resistance, like a wide highway."
        },
        "misconception_tags": ["thicker_wires_have_more_resistance"]
    }


def arch_14_effect_of_wire_material_copper_versus_nichrome(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In circuit construction, connecting leads are made of thick **copper** wire, while the heating elements of toasters and kettles are made of **nichrome** (nickel-chromium alloy) wire.\n\n"
        f"Why are these two specific metals chosen for their respective roles?"
    )
    correct_opt = "Copper has very low resistance so it transports current with negligible energy loss; nichrome has very high resistance so it converts electrical energy efficiently into intense thermal heat."
    options = [
        correct_opt,
        "Copper produces intense heat while nichrome remains at freezing temperatures.",
        "Nichrome is a non-metal that blocks current completely, while copper is a radioactive fuel.",
        "Both metals have identical resistance, but nichrome is silver-coloured for appearance."
    ]
    rng.shuffle(options)
    sol = (
        f"**Material Resistivity Comparison:**\n"
        f"- **Copper:** Excellent electrical conductor with very low resistivity ($\\rho \\approx 1{{,}}7 \\times 10^{{-8}}\\ \\Omega\\cdot\\text{{m}}$). Minimal voltage drop and almost no heat lost in connecting wires.\n"
        f"- **Nichrome:** High-resistance alloy ($\\rho \\approx 1{{,}}1 \\times 10^{{-6}}\\ \\Omega\\cdot\\text{{m}}$, ~60 times higher than copper). When current passes through, frequent electron-ion collisions generate intense Joule heating without melting or oxidizing.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_14_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "14_effect_of_wire_material_copper_versus_nichrome",
        "question_family_id": "14_effect_of_wire_material_copper_versus_nichrome",
        "hints": {
            "tier_1": "Which metal has low resistance for leads, and which has high resistance for heating?",
            "tier_2": "Copper has low resistance (connecting wires); nichrome has high resistance (heating elements).",
            "tier_3": "Copper has low resistance for minimal loss; nichrome has high resistance to produce heat."
        },
        "misconception_tags": ["all_metals_have_equal_resistance"]
    }


def arch_15_effect_of_temperature_on_metallic_resistance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A length of iron or copper wire is connected into a circuit with a cell and an ammeter. "
        f"When the wire is gently heated with a spirit burner flame, the reading on the ammeter steadily decreases.\n\n"
        f"Why does increasing the temperature of a metal conductor cause its resistance to increase?"
    )
    correct_opt = "Heating gives the metal lattice ions more thermal kinetic energy, causing them to vibrate more violently and collide more frequently with drifting electrons, obstructing current flow."
    options = [
        correct_opt,
        "Heat destroys electrons inside the wire, reducing the quantity of charge available.",
        "Heat causes the wire to shrink in diameter, blocking the electrons physically.",
        "The flame produces magnetic waves that repel electric current back into the battery."
    ]
    rng.shuffle(options)
    sol = (
        f"**Temperature Effect on Conductor Resistance:**\n"
        f"1. In a metallic conductor, positive ions vibrate around fixed positions.\n"
        f"2. When heated, the ions absorb thermal energy and vibrate with **larger amplitude**.\n"
        f"3. Drifting electrons suffer far more frequent collisions with these violently vibrating ions.\n"
        f"4. This increased collision rate impedes current flow, causing resistance ($R$) to increase and current ($I$) to decrease ($I = \\frac{{V}}{{R}}$).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_15_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "15_effect_of_temperature_on_metallic_resistance",
        "question_family_id": "15_effect_of_temperature_on_metallic_resistance",
        "hints": {
            "tier_1": "What happens to the vibration of metal lattice ions when heated?",
            "tier_2": "Vibrating ions collide more often with drifting electrons, increasing resistance.",
            "tier_3": "Lattice ions vibrate more violently, causing more collisions and increasing resistance."
        },
        "misconception_tags": ["heating_metals_decreases_resistance"]
    }


def arch_16_anatomy_and_operation_of_incandescent_bulb(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In an incandescent light bulb, a microscopically thin coiled wire of **tungsten** metal is connected between two thicker lead-in copper support wires.\n\n"
        f"Why does the thin tungsten filament glow brightly white-hot, while the copper connecting leads remain cool?"
    )
    correct_opt = "The tungsten filament is extremely thin and has high resistance, producing intense localized heat that reaches incandescence (~2500 °C), while copper wires are thick with low resistance."
    options = [
        correct_opt,
        "Copper wires are hollow tubes filled with cold water to quench heat.",
        "Tungsten contains radioactive isotopes that glow in the dark.",
        "Electric current only enters the filament and bypasses copper wires completely."
    ]
    rng.shuffle(options)
    sol = (
        f"**Incandescent Bulb Physics:**\n"
        f"- The tungsten filament is drawn to microscopic thinness ($0{{,}}02\\text{{ mm}}$) and tightly coiled, giving it very high electrical resistance ($R$).\n"
        f"- Power dissipated as heat: $P = I^2 R$.\n"
        f"- Because the same current ($I$) flows through the entire series circuit, the vast majority of heat is generated in the high-resistance filament, raising it to white-hot incandescence (~$2500^\\circ\\text{{C}}$).\n"
        f"- The copper support wires have negligible resistance and stay cool.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_16_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "16_anatomy_and_operation_of_incandescent_bulb",
        "question_family_id": "16_anatomy_and_operation_of_incandescent_bulb",
        "hints": {
            "tier_1": "Which part has the highest resistance: thin tungsten filament or thick copper wire?",
            "tier_2": "The thin tungsten filament has high resistance and glows white-hot.",
            "tier_3": "High resistance in the thin tungsten filament produces intense heat and glowing light."
        },
        "misconception_tags": ["all_parts_of_circuit_glow_equally"]
    }


def arch_17_function_of_argon_gas_inside_light_bulb(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The glass bulb of an incandescent lamp is evacuated of oxygen and filled with an inert gas like **argon** or nitrogen at low pressure.\n\n"
        f"What would happen to the tungsten filament if the glass envelope contained ordinary atmospheric air instead of inert argon gas?"
    )
    correct_opt = "The tungsten filament would react immediately with atmospheric oxygen at 2500 °C, burning out (oxidizing) in a fraction of a second."
    options = [
        correct_opt,
        "The light bulb would glow twice as bright because oxygen fuels electrical current.",
        "The filament would freeze solid into ice from nitrogen condensation.",
        "Nothing would happen; inert gas is purely a decorative feature."
    ]
    rng.shuffle(options)
    sol = (
        f"**Role of Inert Gas in Light Bulbs:**\n"
        f"- The tungsten filament operates at $\\approx 2500^\\circ\\text{{C}}$.\n"
        f"- At this extreme temperature in the presence of oxygen ($O_2$), tungsten vigorously combusts: $2\\text{{W}} + 3\\text{{O}}_2 \\to 2\\text{{WO}}_3$.\n"
        f"- The filament would burn through and snap within milliseconds.\n"
        f"- Inert gases like argon do not react chemically with hot tungsten, protecting the filament from oxidation while reducing tungsten vaporization.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_17_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "17_function_of_argon_gas_inside_light_bulb",
        "question_family_id": "17_function_of_argon_gas_inside_light_bulb",
        "hints": {
            "tier_1": "What happens when hot metal meets oxygen in the air?",
            "tier_2": "It burns/oxidizes rapidly. Inert argon gas prevents combustion.",
            "tier_3": "Tungsten would oxidize and burn out instantly in atmospheric oxygen."
        },
        "misconception_tags": ["argon_is_flammable"]
    }


def arch_18_nichrome_heating_element_in_appliances_kettle_toaster(rng: random.Random) -> Dict[str, Any]:
    appliances = [
        ("an electric kettle boiling water", "spiral element submerged in the water"),
        ("a pop-up toaster toasting bread slices", "flat ribbons of nichrome wrapped around mica sheets"),
        ("a bathroom wall heater radiating warmth", "coiled nichrome wire inside a silica quartz glass tube")
    ]
    app, element_desc = rng.choice(appliances)
    prompt = (
        f"In **{app}**, the heating element consists of **{element_desc}**.\n\n"
        f"Which two physical properties make **nichrome** the ideal alloy for electrical heating elements?"
    )
    correct_opt = "High electrical resistance (to generate intense thermal energy) and a high melting point with strong resistance to oxidation when glowing hot."
    options = [
        correct_opt,
        "Zero electrical resistance and a melting point below room temperature.",
        "High transparency to visible light and high solubility in warm water.",
        "Radioactive decay properties that produce heat without electric current."
    ]
    rng.shuffle(options)
    sol = (
        f"**Properties of Nichrome Heating Elements:**\n"
        f"1. **High resistivity:** Converts electrical energy rapidly to thermal energy ($P = I^2 R$).\n"
        f"2. **High melting point (~1400 °C):** Can operate at red-hot temperatures ($>800^\\circ\\text{{C}}$) without softening or melting.\n"
        f"3. **Oxidation resistance:** When heated, nichrome forms a tough, adherent surface layer of chromium oxide ($Cr_2O_3$) that prevents further atmospheric corrosion.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_18_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "18_nichrome_heating_element_in_appliances_kettle_toaster",
        "question_family_id": "18_nichrome_heating_element_in_appliances_kettle_toaster",
        "hints": {
            "tier_1": "What two properties must a heating element wire have?",
            "tier_2": "High resistance to create heat, and high melting point so it doesn't melt.",
            "tier_3": "High resistance and high melting point with oxidation resistance."
        },
        "misconception_tags": ["heating_elements_have_zero_resistance"]
    }


def arch_19_heating_effect_of_electric_current_joule_heating(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Whenever an electric current flows through a conductor with electrical resistance, thermal energy is inevitably produced (**Joule heating**).\n\n"
        f"According to Joule's law of heating ($P = I^2 R$), what happens to the rate of heat generation if the electric current ($I$) flowing through a fixed resistor is **doubled**?"
    )
    correct_opt = "The rate of heat generation increases by four times (quadruples), because heating power is proportional to the square of the current."
    options = [
        correct_opt,
        "The rate of heat generation is cut in half.",
        "The rate of heat generation simply doubles.",
        "The heat generation drops to zero because current flows faster."
    ]
    rng.shuffle(options)
    sol = (
        f"**Joule's Law of Heating:**\n"
        f"$$\\text{{Power (Heat Rate)}} = I^2 R\n$$\n"
        f"- If current $I$ is multiplied by $2$:\n"
        f"  $$P_\\text{{new}} = (2I)^2 R = 4I^2 R = 4 P_\\text{{original}}\n$$\n"
        f"- Doubling the current **quadruples** the rate of thermal energy release.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_19_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "19_heating_effect_of_electric_current_joule_heating",
        "question_family_id": "19_heating_effect_of_electric_current_joule_heating",
        "hints": {
            "tier_1": "Look at the formula: P = I^2 * R. Notice the square on I.",
            "tier_2": "2 squared is 4.",
            "tier_3": "Heat generation quadruples (increases by 4 times) because P is proportional to I^2."
        },
        "misconception_tags": ["heating_is_linear_with_current"]
    }


def arch_20_function_and_operation_of_an_electric_fuse(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"An electric fuse is a critical safety device connected in series on the live wire of an electrical circuit.\n\n"
        f"How does a fuse protect an electrical circuit from damage and fire hazard?"
    )
    correct_opt = "It contains a thin wire with a low melting point; if the current exceeds safe levels, the wire overheats, melts ('blows'), and breaks the circuit, stopping all current flow."
    options = [
        correct_opt,
        "It generates cold liquid nitrogen to cool down overheated wires.",
        "It increases the battery's voltage to push through the electrical blockage.",
        "It absorbs excess electrons and stores them as chemical fuel."
    ]
    rng.shuffle(options)
    sol = (
        f"**Function of an Electric Fuse:**\n"
        f"1. A fuse wire has a specific current rating (e.g. 3 A, 5 A, 13 A).\n"
        f"2. Under normal safe currents, Joule heating is low and the wire remains solid.\n"
        f"3. If a fault or overload occurs, the excessive current produces intense heat ($P = I^2 R$).\n"
        f"4. The fuse wire melts, creating an open circuit that immediately interrupts the current before cables inside walls can catch fire.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_20_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "20_function_and_operation_of_an_electric_fuse",
        "question_family_id": "20_function_and_operation_of_an_electric_fuse",
        "hints": {
            "tier_1": "What happens to the fuse wire when current gets too high?",
            "tier_2": "The wire melts and breaks the circuit to prevent a fire.",
            "tier_3": "The thin wire melts and breaks the circuit when current exceeds safe limits."
        },
        "misconception_tags": ["fuse_generates_cooling_power"]
    }


def arch_21_selecting_correct_fuse_rating_for_appliance(rng: random.Random) -> Dict[str, Any]:
    normal_i = rng.choice([2.5, 4.0, 7.5, 10.0])
    fuse_options = [3, 5, 10, 13, 15]
    valid_fuse = next(f for f in fuse_options if f > normal_i)
    i_str = f"{normal_i}".replace(".", "{,}")
    prompt = (
        f"An electrical household appliance draws a steady normal operating current of {i_str} A from a 230 V mains supply.\n\n"
        f"Available fuse ratings are 3 A, 5 A, 10 A, 13 A, and 15 A. Which fuse rating is the **safest and most appropriate** choice?"
    )
    correct_opt = f"The {valid_fuse} A fuse, because it is just slightly above the normal operating current ({i_str} A), allowing normal operation while quickly blowing if an abnormal surge occurs."
    options = [
        correct_opt,
        f"The 15 A fuse, because the highest possible rating is always the safest option for any appliance.",
        f"A 1 A fuse, so that the circuit is always disconnected for maximum safety.",
        "Replacing the fuse with a solid iron nail so it never blows under any circumstances."
    ]
    rng.shuffle(options)
    sol = (
        f"**Fuse Selection Rule:**\n"
        f"- The fuse rating must be **just above** the normal operating current of the appliance.\n"
        f"- For an appliance drawing {i_str} A, a {valid_fuse} A fuse allows regular operation without nuisance tripping.\n"
        f"- If an electrical fault occurs (current rising above {valid_fuse} A), the fuse melts promptly.\n"
        f"- Choosing an oversized fuse (e.g. 15 A) would allow dangerous overcurrents to heat cables and start fires.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_21_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "21_selecting_correct_fuse_rating_for_appliance",
        "question_family_id": "21_selecting_correct_fuse_rating_for_appliance",
        "hints": {
            "tier_1": f"Choose the rating that is just slightly higher than {i_str} A.",
            "tier_2": f"Next standard rating above {i_str} A is {valid_fuse} A.",
            "tier_3": f"The {valid_fuse} A fuse is just above the operating current of {i_str} A."
        },
        "misconception_tags": ["higher_fuse_rating_always_safer"]
    }


def arch_22_circuit_breakers_versus_disposable_fuses(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Modern domestic electrical distribution boards (DB boards) use **circuit breakers** rather than traditional wire fuses.\n\n"
        f"What is the major operational advantage of an electromagnetic or bimetallic circuit breaker over a traditional wire fuse?"
    )
    correct_opt = "A circuit breaker can be easily reset by flipping a switch after tripping, whereas a blown fuse wire is permanently destroyed and must be physically replaced."
    options = [
        correct_opt,
        "Circuit breakers eliminate the need for an electricity meter by generating free power.",
        "Circuit breakers allow unlimited electrical current to flow without ever turning off.",
        "Fuses are illegal worldwide because they emit poisonous mercury gas."
    ]
    rng.shuffle(options)
    sol = (
        f"**Circuit Breakers vs Fuses:**\n"
        f"- **Fuse:** Sacrificial wire. When it blows, it melts and must be thrown away and replaced with a new cartridge or wire.\n"
        f"- **Circuit breaker:** Uses an electromagnet or bimetallic strip to trip a mechanical latch. Once the fault is cleared, it is easily **reset** by flipping the toggle switch back on.\n"
        f"- Breakers also respond much faster to overcurrents, enhancing safety.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_22_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "22_circuit_breakers_versus_disposable_fuses",
        "question_family_id": "22_circuit_breakers_versus_disposable_fuses",
        "hints": {
            "tier_1": "Can you reset a circuit breaker or do you throw it away?",
            "tier_2": "A circuit breaker can simply be reset by flipping a switch.",
            "tier_3": "A circuit breaker can be reset after tripping, while a blown fuse must be replaced."
        },
        "misconception_tags": ["circuit_breakers_must_be_replaced_after_trip"]
    }


def arch_23_definition_and_dangers_of_a_short_circuit(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"If the plastic insulation around two conducting wires in a household appliance wears away and the bare copper wires touch each other, a **short circuit** occurs.\n\n"
        f"What happens to the electrical resistance and current flow during a short circuit, and why is it dangerous?"
    )
    correct_opt = "The current bypasses the appliance through an accidental path of near-zero resistance; this causes current to surge to dangerous levels, producing intense heat that can ignite a fire."
    options = [
        correct_opt,
        "The resistance increases to infinity and the current stops flowing completely.",
        "The voltage drops to zero and the appliance freezes into solid ice.",
        "The battery gains double chemical energy and charges all phones in the house."
    ]
    rng.shuffle(options)
    sol = (
        f"**Short Circuit Dynamics:**\n"
        f"1. Normally, current flows through a load (appliance) with resistance $R$.\n"
        f"2. A short circuit provides an unintended alternate path with **almost zero resistance** ($R \\approx 0$).\n"
        f"3. By Ohm's law: $I = \\frac{{V}}{{R}} \\to \\text{{massive surge in current}}$.\n"
        f"4. Joule heating ($P = I^2 R$) generates intense heat in the wiring within milliseconds, melting insulation and igniting surrounding materials.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_23_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "23_definition_and_dangers_of_a_short_circuit",
        "question_family_id": "23_definition_and_dangers_of_a_short_circuit",
        "hints": {
            "tier_1": "What happens to resistance when wires bypass the load?",
            "tier_2": "Resistance drops to near zero, causing current to surge dangerously.",
            "tier_3": "Current bypasses the load through near-zero resistance, surging and causing fire danger."
        },
        "misconception_tags": ["short_circuit_means_wire_is_too_short"]
    }


def arch_24_three_pin_plug_wiring_colour_codes_south_africa(rng: random.Random) -> Dict[str, Any]:
    wires = [
        ("Live wire (L)", "Brown", "carries high-voltage alternating current from the power station into the appliance"),
        ("Neutral wire (N)", "Blue", "completes the circuit by returning current safely at near-zero voltage"),
        ("Earth wire (E)", "Green and Yellow stripes", "a safety wire connected to the metal casing of the appliance leading to the ground")
    ]
    name, colour, function = rng.choice(wires)
    prompt = (
        f"In South African national electrical standards (SANS 164), domestic appliances are wired using a standard 3-core insulated cable.\n\n"
        f"Which insulation colour and function corresponds to the **{name}**?"
    )
    correct_opt = f"Insulation colour: {colour} | Function: {function}."
    wrong_wires = [w for w in wires if w[0] != name]
    options = [
        correct_opt,
        f"Insulation colour: {wrong_wires[0][1]} | Function: {wrong_wires[0][2]}.",
        f"Insulation colour: Red | Function: {function}.",
        f"Insulation colour: Black | Function: {wrong_wires[1][2]}."
    ]
    rng.shuffle(options)
    sol = (
        f"**Standard 3-Pin Plug Wiring Colours (SANS Code):**\n"
        f"- **Live (L):** **Brown** (carries 230 V power from source).\n"
        f"- **Neutral (N):** **Blue** (completes the circuit at ~0 V).\n"
        f"- **Earth (E):** **Green and Yellow stripes** (safety grounding wire).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_24_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "24_three_pin_plug_wiring_colour_codes_south_africa",
        "question_family_id": "24_three_pin_plug_wiring_colour_codes_south_africa",
        "hints": {
            "tier_1": "Brown = Live, Blue = Neutral, Green/Yellow = Earth.",
            "tier_2": f"{name} is coded with {colour} insulation.",
            "tier_3": f"Colour: {colour} | Function: {function}."
        },
        "misconception_tags": ["confusing_plug_wire_colours"]
    }


def arch_25_function_of_the_earth_wire_for_metal_appliances(rng: random.Random) -> Dict[str, Any]:
    appliances = ["an electric iron with a metal soleplate", "a metal-bodied electric kettle", "a metal-cased washing machine"]
    app = rng.choice(appliances)
    prompt = (
        f"In **{app}**, an earth wire is bolted directly to the metal casing.\n\n"
        f"How does the earth wire protect a person from fatal electric shock if the live wire becomes loose and touches the metal casing?"
    )
    correct_opt = "It provides a very low-resistance path to ground; a massive current surges safely through the earth wire, instantly blowing the fuse or tripping the circuit breaker before anyone can be shocked."
    options = [
        correct_opt,
        "The earth wire converts the 230 V mains voltage into harmless radio waves.",
        "The earth wire produces a forcefield that pushes human hands away from the appliance.",
        "The earth wire absorbs water from the floor to insulate the metal casing."
    ]
    rng.shuffle(options)
    sol = (
        f"**Protection Mechanism of the Earth Wire:**\n"
        f"1. If a loose live wire touches the metal casing, the casing becomes live at $230\\text{{ V}}$.\n"
        f"2. Without an earth wire, touching the metal casing would send current through the human body to ground -> lethal shock.\n"
        f"3. With an earth wire attached to the casing, a path of **almost zero resistance** leads straight to the ground.\n"
        f"4. A huge surge current flows down the earth wire, immediately melting the fuse or tripping the circuit breaker in the DB board.\n"
        f"5. Power is cut in milliseconds, rendering the appliance safe.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_25_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "25_function_of_the_earth_wire_for_metal_appliances",
        "question_family_id": "25_function_of_the_earth_wire_for_metal_appliances",
        "hints": {
            "tier_1": "Where does fault current go if the casing is earthed?",
            "tier_2": "It surges safely down the earth wire, blowing the fuse and cutting power.",
            "tier_3": "Low-resistance path to ground draws a huge current that immediately blows the fuse."
        },
        "misconception_tags": ["earth_wire_is_for_powering_appliance"]
    }
