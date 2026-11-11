"""Grade 8 Natural Sciences: Term 3 - Series and Parallel Circuits Archetypes (26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/03. Series and parallel circuits.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List


def arch_26_why_copper_is_used_for_electrical_connecting_wires(rng: random.Random) -> Dict[str, Any]:
    application = rng.choice([
        "domestic household plug cables and wall sockets",
        "laboratory circuit connecting leads and jumper cables",
        "commercial electrical distribution harnesses",
    ])
    prompt = (
        f"In South African engineering and everyday appliances, {application} are manufactured using copper wire.\n\n"
        f"Which combination of scientific properties explains why **copper** is the standard metal chosen for electrical connecting wires?"
    )
    correct_opt = "Copper has exceptionally low electrical resistance, excellent ductility to bend into flexible wires, and high corrosion resistance."
    options = [
        correct_opt,
        "Copper has exceptionally high electrical resistance that forces voltage to increase along the line.",
        "Copper is an electrical insulator that prevents charges from escaping into the air.",
        "Copper is the only metal known to science that possesses positive protons in its outer electron shells.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Why Copper is Chosen for Connecting Wires:**\n"
        f"1. **Extremely Low Resistance:** Copper has a very low resistivity, ensuring minimal energy is wasted as heat during electrical transmission ($P_\\text{{loss}} = I^2 R$).\n"
        f"2. **High Ductility:** It can be easily drawn into fine, flexible wires without breaking.\n"
        f"3. **Affordability and Durability:** It resists oxidation and provides a durable, cost-effective conductor compared to silver or gold.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_26_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "26_why_copper_is_used_for_electrical_connecting_wires",
        "question_family_id": "26_why_copper_is_used_for_electrical_connecting_wires",
        "hints": {
            "tier_1": "Do connecting wires need low resistance or high resistance to avoid wasting energy?",
            "tier_2": "Copper has very low resistance and bends easily (ductile).",
            "tier_3": "Exceptionally low resistance and high ductility.",
        },
        "misconception_tags": ["connecting_wire_resistance_misunderstanding"],
    }


def arch_27_why_nichrome_is_used_in_electric_heaters_and_toasters(rng: random.Random) -> Dict[str, Any]:
    appliance = rng.choice(["electric toasters and hair dryers", "electric kettles and bar heaters", "oven bake elements and soldering irons"])
    prompt = (
        f"Heating appliances such as {appliance} utilize heating elements constructed from **nichrome wire** "
        f"(an alloy of nickel and chromium).\n\n"
        f"Why is nichrome selected for heating elements instead of copper?"
    )
    correct_opt = "Nichrome has high electrical resistance and a very high melting point, allowing it to glow red-hot and transfer large amounts of thermal energy without melting or oxidising."
    options = [
        correct_opt,
        "Nichrome has zero electrical resistance, allowing current to accelerate to infinite speeds.",
        "Nichrome acts as an insulator at low temperatures and converts into pure copper at high temperatures.",
        "Nichrome produces cold air currents when electric charge passes through it.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Properties of Nichrome Heating Elements:**\n"
        f"- **High Resistance:** As electrons collide with the dense alloy lattice, substantial electrical energy is converted into thermal energy ($E = I^2 R t$).\n"
        f"- **High Melting Point (~1400 °C):** Nichrome can operate red-hot without melting.\n"
        f"- **Oxidation Resistance:** Forms a protective chromium oxide layer that prevents it from burning or corroding in air.\n"
        f"- By contrast, copper has too low a resistance to produce significant heating without dangerous current levels.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_27_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "27_why_nichrome_is_used_in_electric_heaters_and_toasters",
        "question_family_id": "27_why_nichrome_is_used_in_electric_heaters_and_toasters",
        "hints": {
            "tier_1": "Does a heating element need high resistance or low resistance to generate heat?",
            "tier_2": "Nichrome has high resistance and a high melting point, making it ideal for heating elements.",
            "tier_3": "High resistance and high melting point allowing it to glow red-hot safely.",
        },
        "misconception_tags": ["heating_element_resistance_confusion"],
    }


def arch_28_definition_and_examples_of_circuit_output_devices(rng: random.Random) -> Dict[str, Any]:
    examples = rng.choice([
        ("an electric buzzer, a light bulb, and a direct-current motor", "sound, light, and kinetic energy"),
        ("a light-emitting diode (LED), an electric bell, and a heating element", "light, sound, and thermal energy"),
        ("an electric fan motor, a siren, and an indicator lamp", "kinetic, sound, and light energy"),
    ])
    prompt = (
        f"In an electric circuit, components such as {examples[0]} are classified as **output devices**.\n\n"
        f"Which statement precisely defines an output device in an electrical system?"
    )
    correct_opt = f"A device that converts electrical energy into useful non-electrical output forms such as {examples[1]}."
    options = [
        correct_opt,
        "A device that manufactures new electric charges from pure chemical reactions inside wires.",
        "A device used exclusively to measure the potential difference across a power supply.",
        "A safety device designed only to disconnect the circuit during lightning strikes.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Definition of Output Devices:**\n"
        f"- An output device is any component that receives electrical energy and converts it into another useful form of energy:\n"
        f"  - Light bulbs / LEDs $\\rightarrow$ Light energy\n"
        f"  - Electric motors $\\rightarrow$ Kinetic (mechanical) energy\n"
        f"  - Buzzers / Bells $\\rightarrow$ Sound energy\n"
        f"  - Heating elements $\\rightarrow$ Thermal energy\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_28_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "28_definition_and_examples_of_circuit_output_devices",
        "question_family_id": "28_definition_and_examples_of_circuit_output_devices",
        "hints": {
            "tier_1": "What does an output device do with electrical energy?",
            "tier_2": "Output devices convert electrical energy into useful forms like light, sound, or motion.",
            "tier_3": f"Converts electrical energy into {examples[1]}.",
        },
        "misconception_tags": ["output_device_classification_error"],
    }


def arch_29_structure_and_operating_principle_of_led_diodes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Light-Emitting Diodes (LEDs) are rapidly replacing traditional incandescent filament bulbs in modern technology.\n\n"
        f"Which statement correctly describes the internal structure and operational characteristics of an **LED**?"
    )
    correct_opt = "An LED is a solid-state semiconductor diode that emits light directly when current flows in the forward direction; it contains no fragile filament to burn out."
    options = [
        correct_opt,
        "An LED contains an ultra-thin tungsten wire coiled inside a vacuum tube that must heat up to 2500 °C to produce glow.",
        "An LED generates light by burning small amounts of pressurized kerosene oil inside a sealed glass envelope.",
        "An LED allows electric current to flow equally well in both forward and reverse directions without polarity.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Structure and Principles of LEDs:**\n"
        f"- An LED (Light-Emitting Diode) is made of semiconductor materials (e.g. gallium arsenide).\n"
        f"- It has **no wire filament**, so there is nothing to burn out or break when shaken.\n"
        f"- Light is produced directly when electrons recombine with electron holes in the semiconductor junction.\n"
        f"- It is a **diode**, meaning it is polar and allows current to pass in only one direction (forward bias).\n"
        f"- It produces very little waste heat compared to filament bulbs.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_29_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "29_structure_and_operating_principle_of_led_diodes",
        "question_family_id": "29_structure_and_operating_principle_of_led_diodes",
        "hints": {
            "tier_1": "Does an LED have a glowing metal filament like an old light bulb?",
            "tier_2": "LEDs are solid-state semiconductors with no filament, so they cannot burn out.",
            "tier_3": "Solid-state semiconductor with no fragile filament to burn out.",
        },
        "misconception_tags": ["led_filament_misconception"],
    }


def arch_30_comparing_led_efficiency_versus_filament_incandescent_bulbs(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A homeowner is deciding whether to illuminate a room with traditional incandescent filament bulbs or modern LED bulbs.\n\n"
        f"Why is an LED bulb considered dramatically more energy efficient than an incandescent filament bulb?"
    )
    correct_opt = "An LED converts most of its input electrical energy into useful light with minimal waste heat, whereas an incandescent bulb wastes up to 80% to 90% of its energy as heat."
    options = [
        correct_opt,
        "An incandescent bulb produces no heat whatsoever, making it cooler but more expensive.",
        "An LED creates extra electrical energy spontaneously, violating the law of conservation of energy.",
        "An incandescent bulb converts 100% of input energy into useful light, while an LED only converts 10%.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Energy Efficiency Comparison (LED vs Incandescent):**\n"
        f"- **Incandescent Bulb:** Relies on heating a tungsten filament red-hot. Approximately $80\\% - 90\\%$ of input energy is wasted as heat; only $10\\% - 20\\%$ becomes light.\n"
        f"- **LED Bulb:** Produces light via semiconductor electroluminescence. Around $70\\% - 85\\%$ of electrical energy is converted into useful light, with only $15\\% - 30\\%$ lost as heat.\n"
        f"- This superior efficiency means LEDs use far less electrical power for the same illumination and last up to 25 times longer.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_30_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "30_comparing_led_efficiency_versus_filament_incandescent_bulbs",
        "question_family_id": "30_comparing_led_efficiency_versus_filament_incandescent_bulbs",
        "hints": {
            "tier_1": "Which bulb produces less wasted heat: LED or incandescent?",
            "tier_2": "Incandescent bulbs waste 80-90% as heat. LEDs convert most energy into light.",
            "tier_3": "LED converts most input energy into light with minimal waste heat.",
        },
        "misconception_tags": ["incandescent_efficiency_overestimation"],
    }


def arch_31_interpreting_sankey_diagram_for_incandescent_filament_bulb(rng: random.Random) -> Dict[str, Any]:
    input_j = 100
    waste_j = rng.choice([80, 85, 90])
    useful_j = input_j - waste_j
    prompt = (
        f"A Sankey proportional energy flow model represents the energy transformation in an incandescent filament bulb.\n"
        f"For every ${input_j}\\text{{ J}}$ of electrical input energy, ${useful_j}\\text{{ J}}$ is transferred as useful light energy.\n\n"
        f"How much energy is wasted as thermal energy (heat), and how is this depicted in a proportional energy flow model?"
    )
    correct_opt = f"${waste_j}\\text{{ J}}$ is wasted as heat; in the model, this is represented by a broad downward arrow whose width is proportional to ${waste_j}\\text{{ J}}$."
    wrong_narrow = f"${waste_j}\\text{{ J}}$ is wasted as heat, represented by an arrow ten times narrower than the light arrow."
    options = [
        correct_opt,
        wrong_narrow,
        f"${useful_j}\\text{{ J}}$ is wasted as heat, because energy cannot be lost in filament bulbs.",
        f"0 J is wasted as heat, because electrical energy turns completely into luminous photons.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Interpreting Proportional Energy Flow Models:**\n"
        f"- In a Sankey model, the width of each arrow is directly proportional to the amount of energy.\n"
        f"- Conservation of energy states:\n"
        f"  $$\\text{{Input Energy}} = \\text{{Useful Output}} + \\text{{Wasted Energy}}$$\n"
        f"  $${input_j}\\text{{ J}} = {useful_j}\\text{{ J (light)}} + \\text{{Wasted Heat}}$$\n"
        f"  $$\\text{{Wasted Heat}} = {input_j}\\text{{ J}} - {useful_j}\\text{{ J}} = {waste_j}\\text{{ J}}$$\n"
        f"- The broad downward arrow represents the large ${waste_j}\\text{{ J}}$ wasted heat energy.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_31_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "31_interpreting_sankey_diagram_for_incandescent_filament_bulb",
        "question_family_id": "31_interpreting_sankey_diagram_for_incandescent_filament_bulb",
        "hints": {
            "tier_1": f"Subtract the useful light ({useful_j} J) from total input ({input_j} J).",
            "tier_2": f"Wasted heat = {input_j} - {useful_j} = {waste_j} J, represented by proportional arrow width.",
            "tier_3": f"{waste_j} J wasted as heat, shown by a proportional broad arrow.",
        },
        "misconception_tags": ["sankey_arrow_width_misinterpretation"],
    }


def arch_32_interpreting_sankey_diagram_for_high_efficiency_led_bulb(rng: random.Random) -> Dict[str, Any]:
    input_j = 100
    useful_j = rng.choice([70, 75, 80])
    waste_j = input_j - useful_j
    prompt = (
        f"A Sankey proportional energy flow model represents a high-efficiency domestic LED bulb.\n"
        f"For every ${input_j}\\text{{ J}}$ of electrical energy supplied, ${useful_j}\\text{{ J}}$ is emitted as useful light energy and ${waste_j}\\text{{ J}}$ is transferred as heat.\n\n"
        f"How does the visual proportion of arrows for this LED model compare to that of an incandescent filament bulb?"
    )
    correct_opt = f"The straight useful light arrow is significantly wider (${useful_j}\\text{{ J}}$), while the downward wasted heat arrow is narrow (${waste_j}\\text{{ J}}$), the reverse of an incandescent bulb."
    options = [
        correct_opt,
        "The downward wasted heat arrow is five times wider than the input arrow.",
        "Both the light arrow and heat arrow have zero width because LEDs consume no energy.",
        "The LED model has no light arrow because solid-state lamps omit visual radiation.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Sankey Model for an LED:**\n"
        f"- In a Sankey model, arrow width equals energy quantity:\n"
        f"  - Input trunk = ${input_j}\\text{{ J}}$ width.\n"
        f"  - Useful light branch = ${useful_j}\\text{{ J}}$ width (broad, dominant path).\n"
        f"  - Wasted heat branch = ${waste_j}\\text{{ J}}$ width (narrow secondary branch).\n"
        f"- This visually contrasts with a filament bulb, where the waste heat arrow is very broad and the light arrow is very narrow.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_32_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "32_interpreting_sankey_diagram_for_high_efficiency_led_bulb",
        "question_family_id": "32_interpreting_sankey_diagram_for_high_efficiency_led_bulb",
        "hints": {
            "tier_1": "Which arrow is wider on an LED model: light or heat?",
            "tier_2": f"Useful light ({useful_j} J) is wide, while wasted heat ({waste_j} J) is narrow.",
            "tier_3": "Light arrow is significantly wider than the narrow wasted heat arrow.",
        },
        "misconception_tags": ["sankey_proportionality_confusion"],
    }


def arch_33_calculating_electrical_device_percentage_efficiency_from_sankey(rng: random.Random) -> Dict[str, Any]:
    input_energy = rng.choice([200, 400, 500, 1000])
    eff_pct = rng.choice([60, 70, 75, 80])
    useful_energy = int(input_energy * (eff_pct / 100))
    waste_energy = input_energy - useful_energy
    prompt = (
        f"An electric motor draws ${input_energy}\\text{{ J}}$ of electrical input energy from a power source. "
        f"It produces ${useful_energy}\\text{{ J}}$ of useful kinetic energy, while ${waste_energy}\\text{{ J}}$ is transferred as wasted heat and sound.\n\n"
        f"What is the percentage energy efficiency of this electric motor?"
    )
    correct_opt = f"${eff_pct}\\%$, calculated as $\\left(\\frac{{{useful_energy}\\text{{ J}}}}{{{input_energy}\\text{{ J}}}}\\right) \\times 100\\%$."
    wrong_waste = f"{100 - eff_pct}%"
    options = [
        correct_opt,
        f"{wrong_waste}%, calculated as waste energy divided by total energy.",
        f"{useful_energy}%, directly taking the joule quantity as a percentage.",
        "100%, because energy is always conserved in every system.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Calculating Percentage Efficiency:**\n"
        f"- The formula for percentage efficiency is:\n"
        f"  $$\\text{{Efficiency}} = \\left(\\frac{{\\text{{Useful Energy Output}}}}{{\\text{{Total Energy Input}}}}\\right) \\times 100\\%$$\n"
        f"- Substituting the values:\n"
        f"  $$\\text{{Efficiency}} = \\left(\\frac{{{useful_energy}\\text{{ J}}}}{{{input_energy}\\text{{ J}}}}\\right) \\times 100\\% = {eff_pct}\\%$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_33_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "33_calculating_electrical_device_percentage_efficiency_from_sankey",
        "question_family_id": "33_calculating_electrical_device_percentage_efficiency_from_sankey",
        "hints": {
            "tier_1": "What is the formula for percentage efficiency?",
            "tier_2": f"Efficiency = (Useful output / Input) x 100% = ({useful_energy} / {input_energy}) x 100%.",
            "tier_3": f"Efficiency is {eff_pct}%.",
        },
        "misconception_tags": ["efficiency_formula_inversion"],
    }


def arch_34_calculating_wasted_heat_energy_from_input_and_useful_light(rng: random.Random) -> Dict[str, Any]:
    input_j = rng.choice([1500, 2000, 2400, 3000])
    useful_j = rng.choice([1200, 1400, 1800, 2100])
    if useful_j >= input_j:
        useful_j = int(input_j * 0.7)
    wasted_j = input_j - useful_j
    prompt = (
        f"An electric kettle uses ${input_j}\\text{{ J}}$ of electrical input energy to boil water. "
        f"Measurements show that ${useful_j}\\text{{ J}}$ is transferred as useful thermal energy into the water.\n\n"
        f"According to the Law of Conservation of Energy, how much energy was wasted (as sound and heat lost to surrounding air)?"
    )
    correct_opt = f"${wasted_j}\\text{{ J}}$, because $\\text{{Wasted Energy}} = \\text{{Input}} - \\text{{Useful Output}} = {input_j}\\text{{ J}} - {useful_j}\\text{{ J}}$."
    wrong_sum = f"{input_j + useful_j} J"
    options = [
        correct_opt,
        f"{wrong_sum}, because total wasted energy equals the sum of input and output.",
        "0 J, because electric kettles are perfectly 100% efficient closed thermal systems.",
        f"{round(input_j / useful_j, 1)} J, calculated by dividing input by output.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Conservation of Energy Calculation:**\n"
        f"- Energy cannot be created or destroyed, only transformed:\n"
        f"  $$\\text{{Total Input Energy}} = \\text{{Useful Energy Output}} + \\text{{Wasted Energy}}$$\n"
        f"- Rearranging for wasted energy:\n"
        f"  $$\\text{{Wasted Energy}} = {input_j}\\text{{ J}} - {useful_j}\\text{{ J}} = {wasted_j}\\text{{ J}}$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_34_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "34_calculating_wasted_heat_energy_from_input_and_useful_light",
        "question_family_id": "34_calculating_wasted_heat_energy_from_input_and_useful_light",
        "hints": {
            "tier_1": "How do you find wasted energy when total input and useful output are known?",
            "tier_2": f"Subtract useful output from input: {input_j} - {useful_j}.",
            "tier_3": f"Wasted energy is {wasted_j} J.",
        },
        "misconception_tags": ["energy_destruction_misconception"],
    }


def arch_35_history_electricity_amber_triboelectric_to_william_gilbert(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The scientific understanding of electricity developed through centuries of investigation.\n"
        f"Around 600 BC, ancient Greeks noticed that rubbing amber with animal fur allowed it to attract dry feathers. "
        f"In 1600 AD, English scientist William Gilbert published his landmark treatise *De Magnete*.\n\n"
        f"What major contribution did **William Gilbert** make to electrical science?"
    )
    correct_opt = "He coined the term 'electricity' (from the Greek word 'elektron' for amber) and established the fundamental distinction between electrostatic attraction and magnetism."
    options = [
        correct_opt,
        "He invented the first nuclear power reactor and alternating current induction motor.",
        "He constructed the first modern silicon solar panel and lithium-ion cell.",
        "He discovered the electron subatomic particle using a high-voltage cathode ray tube.",
    ]
    rng.shuffle(options)
    sol = (
        f"**William Gilbert (1600 AD):**\n"
        f"- Investigated static electrification produced by rubbing various materials.\n"
        f"- Coined the Latin term *electricus* ('like amber'), which gave rise to the English word **electricity**.\n"
        f"- Proved that electrostatic attraction is distinct from magnetic attraction.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_35_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "35_history_electricity_amber_triboelectric_to_william_gilbert",
        "question_family_id": "35_history_electricity_amber_triboelectric_to_william_gilbert",
        "hints": {
            "tier_1": "Who coined the term 'electricity' from the Greek word for amber?",
            "tier_2": "William Gilbert coined the term and distinguished electricity from magnetism in 1600.",
            "tier_3": "Coined 'electricity' from 'elektron' (amber) and distinguished it from magnetism.",
        },
        "misconception_tags": ["historical_milestone_misattribution"],
    }


def arch_36_history_electricity_benjamin_franklin_lightning_kite_discovery(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In 1752, Benjamin Franklin performed his famous experiment flying a kite during a thunderstorm in Philadelphia.\n\n"
        f"What fundamental scientific fact did Franklin's experiment prove, and what life-saving technology did he invent as a result?"
    )
    correct_opt = "He proved that thunderstorm lightning is a colossal form of static electricity, and he invented the lightning conductor rod to protect structures."
    options = [
        correct_opt,
        "He proved that clouds are made of solid magnetized iron plates, and invented the magnetic compass.",
        "He proved that electricity is a fluid that can be drunk to cure illnesses, and invented bottled electrolyte water.",
        "He proved that thunder travels faster than the speed of light, and invented the supersonic aircraft.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Benjamin Franklin's 1752 Discovery:**\n"
        f"- Extracted electrical charge from storm clouds using a silk kite with a metal wire and key.\n"
        f"- Demonstrated that storm clouds produce identical electrical sparks and shocks to Leyden jars, proving lightning is an electrostatic discharge.\n"
        f"- Invented the **lightning conductor rod**, providing a low-resistance path to safely divert strikes into the earth.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_36_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "36_history_electricity_benjamin_franklin_lightning_kite_discovery",
        "question_family_id": "36_history_electricity_benjamin_franklin_lightning_kite_discovery",
        "hints": {
            "tier_1": "What did Benjamin Franklin's kite experiment demonstrate about lightning?",
            "tier_2": "Franklin proved lightning is static electricity and invented lightning rods.",
            "tier_3": "Proved lightning is static electricity and invented lightning rods.",
        },
        "misconception_tags": ["lightning_nature_misconception"],
    }


def arch_37_history_electricity_volta_first_chemical_cell_and_galvani(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In 1800, Italian physicist Alessandro Volta invented the **voltaic pile**, marking a revolutionary breakthrough in science.\n\n"
        f"Why was Volta's invention such a pivotal milestone in the history of electrical science?"
    )
    correct_opt = "It was the first device capable of producing a continuous, steady direct electric current from chemical reactions, moving science beyond brief static sparks."
    options = [
        correct_opt,
        "It was the first telescope capable of photographing distant galaxies in space.",
        "It was the first steam engine used to power locomotives across Europe.",
        "It was the first mathematical calculator capable of performing binary digital logic.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Alessandro Volta (1800):**\n"
        f"- Built the 'voltaic pile' by alternating discs of zinc and copper separated by cardboard soaked in brine (salt water).\n"
        f"- Before Volta, scientists could only generate brief electrostatic sparks with frictional machines.\n"
        f"- Volta's cell produced the world's first **continuous direct electric current**.\n"
        f"- In honor of his breakthrough, the SI unit of potential difference is named the **Volt** ($V$).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_37_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "37_history_electricity_volta_first_chemical_cell_and_galvani",
        "question_family_id": "37_history_electricity_volta_first_chemical_cell_and_galvani",
        "hints": {
            "tier_1": "What did Alessandro Volta invent, and what kind of current did it produce?",
            "tier_2": "Volta built the first chemical battery (voltaic pile) providing continuous electric current.",
            "tier_3": "First device capable of producing continuous, steady electric current from chemical reactions.",
        },
        "misconception_tags": ["voltaic_pile_historical_error"],
    }


def arch_38_history_electricity_andre_marie_ampere_electrodynamics(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Following Oersted's 1820 discovery that electric currents deflect magnetic compass needles, "
        f"French mathematician and physicist André-Marie Ampère conducted groundbreaking research.\n\n"
        f"What was **André-Marie Ampère's** principal contribution to the foundation of electrical science?"
    )
    correct_opt = "He formulated the mathematical laws of electrodynamics, demonstrating that parallel currents exert magnetic forces on one another, and had the SI unit of electric current named after him."
    options = [
        correct_opt,
        "He discovered the radioactive decay of uranium salts into lead.",
        "He invented the incandescent filament light bulb and commercial phonograph.",
        "He formulated the law of universal gravitation and the three laws of motion.",
    ]
    rng.shuffle(options)
    sol = (
        f"**André-Marie Ampère (1775–1836):**\n"
        f"- Regarded as the father of electrodynamics.\n"
        f"- Showed that two parallel wires carrying currents attract each other if currents flow in the same direction, and repel if in opposite directions.\n"
        f"- Mathematically unified electric current and magnetic fields.\n"
        f"- The SI unit of electric current, the **Ampere** ($A$), was named in his honor.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_38_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "38_history_electricity_andre_marie_ampere_electrodynamics",
        "question_family_id": "38_history_electricity_andre_marie_ampere_electrodynamics",
        "hints": {
            "tier_1": "What unit of electric current is named after André-Marie Ampère?",
            "tier_2": "Ampère developed the laws of electrodynamics and gave his name to the Ampere (A).",
            "tier_3": "Formulated laws of electrodynamics and has the SI unit of current named after him.",
        },
        "misconception_tags": ["historical_scientist_identity_confusion"],
    }


def arch_39_history_electricity_georg_ohm_relationship_voltage_current(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In 1827, German schoolteacher and physicist Georg Simon Ohm published his experimental findings on electrical circuits.\n\n"
        f"What fundamental relationship did **Georg Ohm** establish in electrical physics?"
    )
    correct_opt = "He established that the electric current through a conductor is directly proportional to the potential difference across it and inversely proportional to its resistance ($V = I \\cdot R$)."
    options = [
        correct_opt,
        "He proved that electric charges are destroyed when they pass through high-resistance wires.",
        "He showed that electrical resistance decreases to zero when a conductor is heated to boiling temperatures.",
        "He proved that electric current flows at different speeds depending on the colour of the plastic insulation.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Georg Simon Ohm (1827) and Ohm's Law:**\n"
        f"- Experimented systematically with wires of varying lengths and materials connected to voltaic cells.\n"
        f"- Formulated **Ohm's Law**:\n"
        f"  $$I = \\frac{{V}}{{R}} \\quad \\Longleftrightarrow \\quad V = I \\cdot R$$\n"
        f"- Proved that resistance ($R$) is a measurable property of conductors.\n"
        f"- The SI unit of electrical resistance, the **Ohm** ($\\Omega$), is named after him.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_39_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "39_history_electricity_georg_ohm_relationship_voltage_current",
        "question_family_id": "39_history_electricity_georg_ohm_relationship_voltage_current",
        "hints": {
            "tier_1": "What law relates voltage, current, and resistance?",
            "tier_2": "Georg Ohm formulated Ohm's Law: current is proportional to voltage and inversely proportional to resistance.",
            "tier_3": "Current is directly proportional to voltage and inversely proportional to resistance (V = I * R).",
        },
        "misconception_tags": ["ohms_law_proportionality_error"],
    }


def arch_40_history_electricity_michael_faraday_electromagnetic_induction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In 1831, British scientist Michael Faraday made one of the most momentous discoveries in technological history.\n\n"
        f"What was Faraday's discovery of **electromagnetic induction**, and why is it essential to modern electricity generation?"
    )
    correct_opt = "He discovered that moving a magnet relative to a coil of wire induces an electric current, enabling the creation of mechanical electric generators and power stations."
    options = [
        correct_opt,
        "He discovered that rubbing silk on glass creates static electricity that can power city lights indefinitely.",
        "He proved that chemical cells generate energy by destroying atomic mass completely.",
        "He invented the first semiconductor transistor microchip used in computers.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Michael Faraday's Electromagnetic Induction (1831):**\n"
        f"- Demonstrated that a changing magnetic field induces an electromotive force (voltage) in a closed conductor.\n"
        f"- Moving a magnet inside a wire coil generates a continuous electric current without chemical cells.\n"
        f"- This principle forms the operational basis of all modern electrical generators (coal, nuclear, wind, hydro).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_40_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "40_history_electricity_michael_faraday_electromagnetic_induction",
        "question_family_id": "40_history_electricity_michael_faraday_electromagnetic_induction",
        "hints": {
            "tier_1": "What happens when a magnet moves inside a coil of copper wire?",
            "tier_2": "Faraday discovered electromagnetic induction: moving magnets induce current in coils, enabling generators.",
            "tier_3": "Moving a magnet relative to a coil induces an electric current, enabling electric generators.",
        },
        "misconception_tags": ["electromagnetic_induction_misunderstanding"],
    }


def arch_41_history_electricity_edison_dc_versus_tesla_ac_generators(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"During the late 19th-century 'War of the Currents', Thomas Edison championed Direct Current (DC) "
        f"while Nikola Tesla and George Westinghouse championed Alternating Current (AC).\n\n"
        f"Why did **Tesla's Alternating Current (AC)** system ultimately become the global standard for national power grids?"
    )
    correct_opt = "AC voltage can be easily stepped up to very high voltages using transformers for efficient low-loss transmission over long distances, then stepped down safely for homes."
    options = [
        correct_opt,
        "DC electricity can travel infinitely without requiring any conducting wires or power poles.",
        "AC electricity requires no power stations and is generated directly inside home appliances.",
        "Edison's DC system was banned worldwide because direct current cannot illuminate light bulbs.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Tesla's AC vs Edison's DC:**\n"
        f"- Edison's DC power could only travel approximately $1 - 2\\text{{ km}}$ before line resistance caused severe voltage drops, requiring power plants on every corner.\n"
        f"- Tesla proved that AC voltage can be stepped up to hundreds of thousands of volts using transformers.\n"
        f"- High voltage reduces current ($P = V \\cdot I$), which drastically cuts energy loss to heat in power lines ($P_\\text{{loss}} = I^2 R$).\n"
        f"- Near homes, transformers step the voltage down to safe levels ($230\\text{{ V}}$).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_41_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "41_history_electricity_edison_dc_versus_tesla_ac_generators",
        "question_family_id": "41_history_electricity_edison_dc_versus_tesla_ac_generators",
        "hints": {
            "tier_1": "Can DC or AC be easily transformed to high voltages for long-distance travel?",
            "tier_2": "AC can be stepped up with transformers, reducing power loss over long distances.",
            "tier_3": "AC voltage can be easily stepped up using transformers for low-loss long-distance transmission.",
        },
        "misconception_tags": ["ac_dc_transmission_confusion"],
    }


def arch_42_short_circuits_mechanism_and_extreme_current_overheating_danger(rng: random.Random) -> Dict[str, Any]:
    hazard = rng.choice([
        ("frayed appliance cord", "the bare live and neutral wires touch directly together"),
        ("faulty electrical kettle", "water leaks across the internal terminals creating an unresisted bridge"),
        ("classroom experiment error", "a thick copper wire is accidentally connected directly across both battery terminals"),
    ])
    prompt = (
        f"Consider a hazard scenario involving a {hazard[0]}, where {hazard[1]}.\n\n"
        f"What is a **short circuit**, and why does it represent an extreme fire hazard?"
    )
    correct_opt = "A connection providing an unintended path of near-zero resistance, causing current to spike to dangerously high levels and generating extreme overheating in wires."
    options = [
        correct_opt,
        "A connection that completely stops all current from moving, freezing the wires into ice.",
        "A connection that makes the conducting wire shorter in physical length without affecting current.",
        "A connection where voltage drops to zero while current remains perfectly unchanged.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Mechanism of a Short Circuit:**\n"
        f"- In a normal circuit, electrical components (bulbs, appliances) provide resistance, limiting current flow.\n"
        f"- A short circuit bypasses the load, connecting terminals through a near-zero resistance pathway ($R \\approx 0\\ \\Omega$).\n"
        f"- By Ohm's law ($I = V / R$), dividing by near-zero resistance causes an enormous surge in current ($I \\rightarrow \\infty$).\n"
        f"- Heating power is proportional to the square of current ($P = I^2 R$); this massive surge melts wire insulation, igniting electrical fires.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_42_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "42_short_circuits_mechanism_and_extreme_current_overheating_danger",
        "question_family_id": "42_short_circuits_mechanism_and_extreme_current_overheating_danger",
        "hints": {
            "tier_1": "What happens to the current when resistance drops to almost zero in a short circuit?",
            "tier_2": "Zero resistance = huge current spike = extreme heat and fire risk.",
            "tier_3": "Unintended near-zero resistance path causing massive current spike and extreme overheating.",
        },
        "misconception_tags": ["short_circuit_concept_missing"],
    }


def arch_43_fuses_and_circuit_breakers_overcurrent_protection_mechanism(rng: random.Random) -> Dict[str, Any]:
    device = rng.choice(["a cartridge fuse with a thin alloy wire", "an electro-mechanical circuit breaker switch in a distribution board"])
    prompt = (
        f"To prevent domestic electrical fires caused by overloads or short circuits, circuits are fitted with {device}.\n\n"
        f"How does this safety device operate to protect the electrical installation?"
    )
    correct_opt = "It is connected in series in the live path; when excessive current flows, it melts or automatically trips open, breaking the circuit before wires overheat."
    options = [
        correct_opt,
        "It is connected in parallel with appliances to absorb excess electricity and convert it into water.",
        "It stores unlimited excess current in an internal vacuum container to be reused later.",
        "It reduces the mains voltage to 0 V permanently for the entire city.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Operation of Fuses and Circuit Breakers:**\n"
        f"- Connected in **series** in the live conducting path.\n"
        f"- **Fuse:** Contains a short piece of wire with a specific low melting point. If current exceeds rated capacity, resistive heat melts the wire, opening the circuit.\n"
        f"- **Circuit Breaker:** Uses an electromagnet or bimetallic strip that mechanically flips a switch open during overcurrent. It can be reset after clearing the fault.\n"
        f"- Both prevent conductors from overheating and igniting fires.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_43_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "43_fuses_and_circuit_breakers_overcurrent_protection_mechanism",
        "question_family_id": "43_fuses_and_circuit_breakers_overcurrent_protection_mechanism",
        "hints": {
            "tier_1": "What happens to a fuse wire when too much current passes through it?",
            "tier_2": "A fuse melts (or breaker trips) when current is excessive, breaking the circuit safely.",
            "tier_3": "Connected in series; melts or trips open during overcurrent to break the circuit.",
        },
        "misconception_tags": ["fuse_connected_in_parallel_misconception"],
    }


def arch_44_misconception_electric_current_gets_used_up_by_bulbs(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A common misconception among beginner science learners is that 'electric current gets used up by light bulbs as it travels around a circuit.'\n\n"
        f"Which scientific counter-evidence refutes this misconception?"
    )
    correct_opt = "Ammeters placed before and after a glowing light bulb measure identical current values, proving electric charge is conserved and only electrical energy is transferred."
    options = [
        correct_opt,
        "Light bulbs do not need any electric current to glow because they run on battery sound.",
        "Current leaves the battery as electrons and returns to the battery as protons.",
        "Ammeter readings always double after passing through a light bulb.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Refuting the 'Current is Used Up' Misconception:**\n"
        f"- Electric current is the rate of flow of charges (electrons).\n"
        f"- Charges cannot be destroyed or consumed inside a component (Conservation of Charge).\n"
        f"- An ammeter connected immediately before a bulb and an ammeter connected immediately after read the exact same current ($I_\\text{{before}} = I_\\text{{after}}$).\n"
        f"- What IS transferred and converted is **electrical potential energy**, which transforms into light and thermal energy.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_44_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "44_misconception_electric_current_gets_used_up_by_bulbs",
        "question_family_id": "44_misconception_electric_current_gets_used_up_by_bulbs",
        "hints": {
            "tier_1": "What do ammeters placed before and after a bulb show?",
            "tier_2": "Current before equals current after; charge is conserved, only energy is transferred.",
            "tier_3": "Ammeters before and after measure identical current values; charge is conserved.",
        },
        "misconception_tags": ["current_consumption_misconception"],
    }


def arch_45_misconception_current_is_greater_before_a_bulb_than_after(rng: random.Random) -> Dict[str, Any]:
    current_val = rng.choice([0.3, 0.45, 0.6])
    c_str = f"{current_val}".replace(".", ",")
    prompt = (
        f"A learner connects an ammeter upstream of a bulb and records ${c_str}\\text{{ A}}$. "
        f"The learner predicts: 'The ammeter downstream after the bulb will read less than ${c_str}\\text{{ A}}$ because the bulb consumed current to produce light.'\n\n"
        f"Is the learner's prediction correct or incorrect, and why?"
    )
    correct_opt = f"Incorrect; the downstream ammeter will read exactly ${c_str}\\text{{ A}}$, because electrons cannot accumulate or disappear within the bulb."
    options = [
        correct_opt,
        f"Correct; the downstream ammeter will read half of ${c_str}\\text{{ A}}$ because bulbs use 50% of the charge.",
        f"Correct; the downstream ammeter will read 0 A because all current is converted into light.",
        f"Incorrect; the downstream ammeter will read twice as much because bulbs produce extra electrons.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Conservation of Charge in a Light Bulb:**\n"
        f"- Electrons flow in a continuous closed loop without accumulating anywhere.\n"
        f"- Every electron that enters the filament must exit the filament.\n"
        f"- Therefore, the current entering the bulb equals the current exiting the bulb:\n"
        f"  $$I_\\text{{in}} = I_\\text{{out}} = {c_str}\\text{{ A}}$$\n"
        f"- The bulb transfers energy, not charge.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_45_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "45_misconception_current_is_greater_before_a_bulb_than_after",
        "question_family_id": "45_misconception_current_is_greater_before_a_bulb_than_after",
        "hints": {
            "tier_1": "Can electrons pile up or vanish inside a bulb filament?",
            "tier_2": f"No; current in equals current out, so it reads exactly {c_str} A.",
            "tier_3": f"Incorrect; downstream ammeter reads exactly {c_str} A.",
        },
        "misconception_tags": ["unidirectional_attenuation_model"],
    }


def arch_46_misconception_adding_resistors_in_parallel_increases_resistance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A student argues: 'If you have one resistor and you add a second resistor in parallel, the total resistance must increase because you have two resistors instead of one.'\n\n"
        f"Why is this student's argument scientifically false?"
    )
    correct_opt = "Adding a parallel resistor provides an additional alternate pathway for charge, which decreases overall obstruction and lowers the total equivalent resistance."
    options = [
        correct_opt,
        "The student is actually correct; adding resistors in any configuration always increases total resistance.",
        "The argument is false because parallel resistors turn into zero-resistance superconductors instantly.",
        "The argument is false because second resistors always cancel out the voltage of the battery.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Why Parallel Resistance Decreases:**\n"
        f"- While adding resistors in *series* increases resistance, adding them in *parallel* provides parallel alternative paths.\n"
        f"- More pathways mean more total current can leave the battery for the same voltage.\n"
        f"- By Ohm's law ($R_\\text{{total}} = V / I_\\text{{total}}$), a higher total current for the same voltage means total resistance has **decreased**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_46_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "46_misconception_adding_resistors_in_parallel_increases_resistance",
        "question_family_id": "46_misconception_adding_resistors_in_parallel_increases_resistance",
        "hints": {
            "tier_1": "Does adding an alternate door make exiting easier or harder?",
            "tier_2": "Adding parallel pathways decreases total resistance.",
            "tier_3": "An alternate pathway decreases overall obstruction, lowering total resistance.",
        },
        "misconception_tags": ["parallel_resistance_additive_misconception"],
    }


def arch_47_misconception_connecting_cells_in_parallel_multiplies_voltage(rng: random.Random) -> Dict[str, Any]:
    n_cells = rng.choice([2, 3, 4])
    prompt = (
        f"A learner connects {n_cells} identical $1{{,}}5\\text{{ V}}$ cells in **parallel** and expects a voltmeter across the combination to read ${n_cells * 1.5}\\text{{ V}}$.\n\n"
        f"Why is the learner's expectation mistaken, and what will the voltmeter actually read?"
    )
    correct_opt = f"The voltmeter will read only $1{{,}}5\\text{{ V}}$; parallel cells do not add their voltages, they only share current delivery at the same potential difference."
    options = [
        correct_opt,
        f"The voltmeter will read 0 V, because parallel cells destroy each other's voltage completely.",
        f"The voltmeter will read {n_cells * 3} V, because parallel connections double each cell's voltage.",
        f"The voltmeter will read only {round(1.5 / n_cells, 2)} V, because voltage is divided among the cells.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Voltage of Cells in Parallel:**\n"
        f"- Connecting cells in parallel connects all positive terminals together and all negative terminals together.\n"
        f"- The potential difference between the terminals is simply the potential difference of a single cell: $V_\\text{{total}} = 1{{,}}5\\text{{ V}}$.\n"
        f"- To achieve ${n_cells * 1.5}\\text{{ V}}$, the cells would need to be connected in **series**, not parallel.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_47_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "47_misconception_connecting_cells_in_parallel_multiplies_voltage",
        "question_family_id": "47_misconception_connecting_cells_in_parallel_multiplies_voltage",
        "hints": {
            "tier_1": "Do cell voltages add together in parallel or in series?",
            "tier_2": "Voltages add in series, but remain unchanged (1.5 V) in parallel.",
            "tier_3": "Voltmeter will read only 1.5 V; parallel cells do not add voltage.",
        },
        "misconception_tags": ["parallel_cells_multiply_voltage_misconception"],
    }


def arch_48_misconception_electrons_originate_only_from_the_battery_chemical(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Some learners picture a battery as an 'electron tank' that sprays electrons out into empty wires like water from a hose.\n\n"
        f"What is the scientifically accurate description of the origin of moving electrons in an electric circuit?"
    )
    correct_opt = "Conductors are already packed with delocalised electrons throughout their entire structure; the battery simply provides the potential difference (energy push) that causes existing electrons to drift."
    options = [
        correct_opt,
        "All electrons in a circuit originate inside the battery chemicals and empty out completely into the bulb.",
        "Electrons are created out of empty space by the closing of the mechanical switch.",
        "Electrons enter the circuit from surrounding air molecules when the circuit switch clicks.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Origin of Moving Electrons in a Circuit:**\n"
        f"- Conducting metals (such as copper wires and tungsten filaments) contain a vast sea of delocalised valence electrons at all times.\n"
        f"- The battery does not 'create' or 'supply all' the electrons; rather, it acts as an **energy pump**.\n"
        f"- The chemical reactions inside the battery create a potential difference that pushes the electrons already present inside the wire.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_48_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "48_misconception_electrons_originate_only_from_the_battery_chemical",
        "question_family_id": "48_misconception_electrons_originate_only_from_the_battery_chemical",
        "hints": {
            "tier_1": "Are wires empty tubes or do they already contain electrons?",
            "tier_2": "Metals already contain delocalised electrons; the battery provides the push.",
            "tier_3": "Conductors already contain delocalised electrons; battery provides the energy push.",
        },
        "misconception_tags": ["battery_as_electron_reservoir_misconception"],
    }


def arch_49_experimental_design_variables_in_series_parallel_investigations(rng: random.Random) -> Dict[str, Any]:
    investigation = rng.choice([
        ("investigating how adding light bulbs in series affects the electric current strength",
         "Number of bulbs connected in series",
         "Electric current reading on the ammeter (A)",
         "Battery voltage, wire length, and bulb rating/type"),
        ("investigating how increasing the number of cells in series affects electric current",
         "Number of cells connected in series",
         "Electric current reading on the ammeter (A)",
         "Type and number of bulbs, wire type, and switch"),
        ("investigating how adding resistors in parallel affects total circuit current",
         "Number of parallel branches/resistors",
         "Total current measured in the main trunk (A)",
         "Supply voltage, wire resistance, and resistor values"),
    ])
    prompt = (
        f"A Grade 8 Natural Sciences class conducts a practical investigation: '{investigation[0]}'.\n\n"
        f"Which row correctly identifies the **Independent Variable**, **Dependent Variable**, and a **Controlled Variable** for this experiment?"
    )
    correct_opt = f"Independent: {investigation[1]} | Dependent: {investigation[2]} | Controlled: {investigation[3]}"
    wrong_swap = f"Independent: {investigation[2]} | Dependent: {investigation[1]} | Controlled: {investigation[3]}"
    options = [
        correct_opt,
        wrong_swap,
        f"Independent: {investigation[3]} | Dependent: {investigation[1]} | Controlled: {investigation[2]}",
        f"Independent: Room temperature | Dependent: Atmospheric pressure | Controlled: {investigation[1]}",
    ]
    rng.shuffle(options)
    sol = (
        f"**Variables in the Circuit Investigation:**\n"
        f"- **Independent Variable (what the experimenter deliberately changes):** {investigation[1]}.\n"
        f"- **Dependent Variable (what is measured in response):** {investigation[2]}.\n"
        f"- **Controlled Variables (kept constant to ensure a fair test):** {investigation[3]}.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_49_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "49_experimental_design_variables_in_series_parallel_investigations",
        "question_family_id": "49_experimental_design_variables_in_series_parallel_investigations",
        "hints": {
            "tier_1": "What is deliberately changed (independent), and what responds and is measured (dependent)?",
            "tier_2": f"Independent: {investigation[1]}; Dependent: {investigation[2]}.",
            "tier_3": f"Independent: {investigation[1]} | Dependent: {investigation[2]} | Controlled: {investigation[3]}.",
        },
        "misconception_tags": ["variable_identification_error"],
    }


def arch_50_electric_circuits_comprehensive_diagnostic_evaluation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Evaluate the following summary statements comparing **series** and **parallel** electrical circuits:\n\n"
        f"Which statement is entirely **scientifically correct** in every respect?"
    )
    correct_opt = (
        "In a series circuit, current is identical everywhere and adding resistors increases total resistance; "
        "in a parallel circuit, current divides among branches and adding resistors decreases total resistance."
    )
    options = [
        correct_opt,
        (
            "In a series circuit, voltage is identical across all components; "
            "in a parallel circuit, current never splits and total resistance doubles with every added branch."
        ),
        (
            "In a series circuit, if one bulb blows all other bulbs stay lit; "
            "in a parallel circuit, if one bulb blows all other branches shut down immediately."
        ),
        (
            "In a series circuit, adding cells in parallel triples the current; "
            "in a parallel circuit, ammeters must be connected in parallel with high resistance."
        ),
    ]
    rng.shuffle(options)
    sol = (
        f"**Comprehensive Synthesis of Circuit Rules:**\n"
        f"- **Series Circuits:**\n"
        f"  - Single pathway: $I_\\text{{total}} = I_1 = I_2$.\n"
        f"  - Voltage divides: $V_\\text{{total}} = V_1 + V_2$.\n"
        f"  - Total resistance increases with more components: $R_\\text{{total}} = R_1 + R_2$.\n"
        f"  - A break in one component halts current everywhere.\n"
        f"- **Parallel Circuits:**\n"
        f"  - Multiple pathways: $I_\\text{{total}} = I_1 + I_2$.\n"
        f"  - Voltage is identical across each branch: $V_\\text{{total}} = V_1 = V_2$.\n"
        f"  - Total resistance decreases with more branches.\n"
        f"  - Branches operate independently.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_circ_50_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "50_electric_circuits_comprehensive_diagnostic_evaluation",
        "question_family_id": "50_electric_circuits_comprehensive_diagnostic_evaluation",
        "hints": {
            "tier_1": "Recall: In series, current is constant; in parallel, current splits and resistance decreases.",
            "tier_2": "Series = constant current, increasing resistance. Parallel = dividing current, decreasing resistance.",
            "tier_3": "In series, current is identical everywhere; in parallel, current divides and resistance decreases.",
        },
        "misconception_tags": ["series_parallel_rule_confusion"],
    }
