"""Grade 8 Natural Sciences: Term 3 - Energy Transfer in Electrical Systems Archetypes (26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/01. Energy transfer in electrical systems.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List


def arch_26_magnetic_effect_of_an_electric_current_oersted(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In 1820, Danish scientist Hans Christian Oersted placed a small magnetic compass needle directly parallel beneath a copper conducting wire connected to a battery.\n\n"
        f"What happened to the compass needle when the switch was closed, and what fundamental discovery did this reveal?"
    )
    correct_opt = "The compass needle deflected perpendicularly away from North, discovering that an electric current flowing through a conductor creates an associated magnetic field."
    options = [
        correct_opt,
        "The compass needle permanently demagnetized and dissolved into liquid iron.",
        "The compass needle spun continuously at supersonic speed without stopping.",
        "Nothing happened because copper is completely non-magnetic and ignores electricity."
    ]
    rng.shuffle(options)
    sol = (
        f"**Oersted's Discovery (Electromagnetism):**\n"
        f"1. A compass needle responds exclusively to magnetic forces.\n"
        f"2. When current flows through the copper wire, moving electric charges generate a **magnetic field** in the space surrounding the wire.\n"
        f"3. The magnetic needle aligns with this circular magnetic field, deflecting sharply.\n"
        f"4. This established the foundational link between electricity and magnetism (**electromagnetism**).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_26_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "26_magnetic_effect_of_an_electric_current_oersted",
        "question_family_id": "26_magnetic_effect_of_an_electric_current_oersted",
        "hints": {
            "tier_1": "What does an electric current create around a wire that affects a compass?",
            "tier_2": "Current flowing through a wire creates a magnetic field.",
            "tier_3": "The needle deflected, proving current creates an associated magnetic field."
        },
        "misconception_tags": ["current_has_no_magnetic_effect"]
    }


def arch_27_shape_of_magnetic_field_around_straight_wire(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Iron filings are sprinkled onto a horizontal sheet of white cardboard. A thick vertical copper wire passes through a hole in the centre of the board. "
        f"When a strong direct current flows through the wire and the board is gently tapped, the iron filings align into a distinct geometric pattern.\n\n"
        f"What geometric shape does the magnetic field form around a long straight current-carrying wire?"
    )
    correct_opt = "Concentric circles centred on the wire, with circles spaced closer together near the wire where the magnetic field is strongest."
    options = [
        correct_opt,
        "Straight parallel lines pointing away from the wire like spokes on a bicycle wheel.",
        "Square boxes aligned with the four cardinal directions (North, South, East, West).",
        "Random criss-crossing spirals with zero geometric symmetry."
    ]
    rng.shuffle(options)
    sol = (
        f"**Magnetic Field Geometry of a Straight Conductor:**\n"
        f"- The magnetic field lines around a long straight current-carrying wire form a series of **concentric circular rings** centred on the wire.\n"
        f"- The field lines are in planes perpendicular to the wire.\n"
        f"- Field strength decreases with radial distance ($B \\propto \\frac{{1}}{{r}}$), so the circular lines are closest together near the wire surface.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_27_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "27_shape_of_magnetic_field_around_straight_wire",
        "question_family_id": "27_shape_of_magnetic_field_around_straight_wire",
        "hints": {
            "tier_1": "Do field lines around a wire form circles, squares, or straight lines?",
            "tier_2": "Field lines form concentric circles centred on the wire.",
            "tier_3": "Concentric circles centred on the wire, denser near the wire."
        },
        "misconception_tags": ["magnetic_fields_are_radial_spokes"]
    }


def arch_28_right_hand_grip_rule_for_wire_magnetic_field(rng: random.Random) -> Dict[str, Any]:
    current_dirs = [
        ("vertically upwards", "counter-clockwise (anticlockwise) when viewed from above"),
        ("vertically downwards", "clockwise when viewed from above")
    ]
    c_dir, field_dir = rng.choice(current_dirs)
    prompt = (
        f"A straight vertical wire carries conventional electric current flowing **{c_dir}**.\n\n"
        f"Using the **Right-Hand Grip Rule**, in which direction do the circular magnetic field lines circulate around the wire?"
    )
    correct_opt = f"The magnetic field lines circulate {field_dir}."
    opposite_dir = "clockwise when viewed from above" if "counter" in field_dir else "counter-clockwise (anticlockwise) when viewed from above"
    options = [
        correct_opt,
        f"The magnetic field lines circulate {opposite_dir}.",
        "The magnetic field points straight upwards parallel to the current.",
        "The magnetic field reverses direction every second automatically."
    ]
    rng.shuffle(options)
    sol = (
        f"**The Right-Hand Grip Rule:**\n"
        f"1. Imagine gripping the conducting wire with your **right hand**.\n"
        f"2. Point your extended thumb in the direction of conventional current ({c_dir}).\n"
        f"3. The direction in which your fingers curl around the wire indicates the direction of magnetic field lines.\n"
        f"4. For current {c_dir}, the curled fingers point **{field_dir}**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_28_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "28_right_hand_grip_rule_for_wire_magnetic_field",
        "question_family_id": "28_right_hand_grip_rule_for_wire_magnetic_field",
        "hints": {
            "tier_1": "Use your right hand: thumb points along current, fingers curl along field.",
            "tier_2": f"Current {c_dir} produces {field_dir} field lines.",
            "tier_3": f"The field lines circulate {field_dir}."
        },
        "misconception_tags": ["using_left_hand_rule"]
    }


def arch_29_magnetic_field_pattern_of_a_solenoid_coil(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When an insulated wire is wound into a long helical coil of many turns, it is called a **solenoid**.\n\n"
        f"What is the overall shape and structure of the magnetic field produced by a current-carrying solenoid?"
    )
    correct_opt = "It produces a magnetic field nearly identical to that of a permanent bar magnet, with strong uniform parallel field lines inside the coil and loops emerging from a North pole to enter a South pole."
    options = [
        correct_opt,
        "It cancels all magnetic fields inside the coil, leaving zero field anywhere.",
        "It generates a spherical field that attracts all non-metallic objects like wood and plastic.",
        "It creates an alternating electrical field that changes all nearby metals into liquid."
    ]
    rng.shuffle(options)
    sol = (
        f"**Magnetic Field of a Solenoid:**\n"
        f"1. Each loop of wire adds its own circular magnetic field to adjacent loops.\n"
        f"2. Inside the coil, the individual fields add together constructively, forming a **strong, uniform, parallel magnetic field**.\n"
        f"3. Outside the coil, the field lines emerge from one end (acting as a **North magnetic pole**) and curve around to re-enter the other end (acting as a **South magnetic pole**).\n"
        f"4. The field pattern is virtually indistinguishable from a standard **permanent bar magnet**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_29_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "29_magnetic_field_pattern_of_a_solenoid_coil",
        "question_family_id": "29_magnetic_field_pattern_of_a_solenoid_coil",
        "hints": {
            "tier_1": "What permanent magnetic object does a solenoid's field resemble?",
            "tier_2": "A solenoid produces a field almost identical to a bar magnet.",
            "tier_3": "Nearly identical to a bar magnet: uniform field inside, North and South poles at ends."
        },
        "misconception_tags": ["solenoid_field_is_purely_circular"]
    }


def arch_30_structure_and_definition_of_an_electromagnet(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In school science projects, students construct a simple **electromagnet** using an iron nail, insulated copper wire, and a D-cell.\n\n"
        f"Which statement precisely describes the construction and operational principle of an electromagnet?"
    )
    correct_opt = "A temporary magnet created by winding an insulated wire coil around a magnetic core (such as soft iron); it exhibits strong magnetic properties ONLY while electric current flows through the coil."
    options = [
        correct_opt,
        "A permanent magnet that stays magnetized for hundreds of years without requiring any battery or current.",
        "A piece of copper wire that absorbs magnetic radiation from thunderstorms.",
        "An electric battery made entirely of magnetic rock."
    ]
    rng.shuffle(options)
    sol = (
        f"**Definition and Structure of an Electromagnet:**\n"
        f"- An electromagnet is a **temporary magnet** consisting of a solenoid wrapped around a ferromagnetic core (like soft iron).\n"
        f"- When current flows: the coil creates a magnetic field that aligns domains in the iron core, multiplying magnetic strength hundreds of times.\n"
        f"- When current is switched off: the magnetic field collapses instantly, and the core loses its magnetism.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_30_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "30_structure_and_definition_of_an_electromagnet",
        "question_family_id": "30_structure_and_definition_of_an_electromagnet",
        "hints": {
            "tier_1": "Is an electromagnet permanent or temporary?",
            "tier_2": "It is a temporary magnet that works only when electric current is switched on.",
            "tier_3": "A temporary magnet consisting of a coil around a soft iron core, magnetic only while current flows."
        },
        "misconception_tags": ["electromagnets_are_permanent"]
    }


def arch_31_role_of_soft_iron_core_in_electromagnet(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When constructing an electromagnet, why is a **soft iron nail** or rod placed inside the coil, rather than a piece of hard steel, aluminium, or wood?"
    )
    correct_opt = "Soft iron is a ferromagnetic material that magnetizes easily to amplify the magnetic field hundreds of times, and demagnetizes instantly when the current is switched off."
    options = [
        correct_opt,
        "Soft iron acts as an electrical insulator that prevents the battery from draining.",
        "Hard steel and aluminium are transparent to magnetic fields and repel all magnetic flux.",
        "Iron produces its own electric current inside the coil through chemical reaction."
    ]
    rng.shuffle(options)
    sol = (
        f"**Why Soft Iron is Used for Electromagnet Cores:**\n"
        f"1. **High magnetic permeability:** Iron has magnetic domains that readily align with the coil's field, boosting field strength by up to 1000 times.\n"
        f"2. **Low retentivity (soft magnetic material):** As soon as the circuit is opened, the domains randomize immediately, losing virtually all residual magnetism.\n"
        f"3. (If hard steel were used, it would remain permanently magnetized, making it impossible to switch the electromagnet off).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_31_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "31_role_of_soft_iron_core_in_electromagnet",
        "question_family_id": "31_role_of_soft_iron_core_in_electromagnet",
        "hints": {
            "tier_1": "What happens when you turn off the current in an electromagnet?",
            "tier_2": "You want it to lose magnetism instantly. Soft iron magnetizes and demagnetizes easily.",
            "tier_3": "Soft iron amplifies the field and demagnetizes immediately when current is cut."
        },
        "misconception_tags": ["steel_is_identical_to_soft_iron"]
    }


def arch_32_factors_affecting_electromagnet_strength_turns(rng: random.Random) -> Dict[str, Any]:
    n1 = rng.choice([20, 30])
    n2 = n1 * rng.choice([2, 3])
    prompt = (
        f"A student builds two electromagnets using identical iron nails and identical 1,5 V cells. "
        f"Electromagnet 1 has {n1} turns of wire, while Electromagnet 2 has {n2} turns of wire.\n\n"
        f"When tested with steel paperclips, which electromagnet will pick up more paperclips, and why?"
    )
    correct_opt = f"Electromagnet 2 ({n2} turns), because increasing the number of turns increases the total magnetic field strength proportionally."
    options = [
        correct_opt,
        f"Electromagnet 1 ({n1} turns), because fewer turns allow current to move with less resistance.",
        "Both electromagnets will pick up the exact same number because turns have zero effect on magnetism.",
        "Neither electromagnet will pick up any paperclips because copper wire cancels magnetism."
    ]
    rng.shuffle(options)
    sol = (
        f"**Effect of Turns on Electromagnet Strength:**\n"
        f"- Magnetic field strength is directly proportional to the number of turns ($B \\propto N$).\n"
        f"- Each turn of wire contributes its own magnetic field to the core.\n"
        f"- Therefore, Electromagnet 2 with {n2} turns creates a significantly stronger magnetic field and picks up more paperclips.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_32_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "32_factors_affecting_electromagnet_strength_turns",
        "question_family_id": "32_factors_affecting_electromagnet_strength_turns",
        "hints": {
            "tier_1": "Does more turns of wire make an electromagnet stronger or weaker?",
            "tier_2": "More turns create a stronger magnetic field.",
            "tier_3": f"Electromagnet 2 ({n2} turns) is stronger because more turns increase field strength."
        },
        "misconception_tags": ["fewer_turns_make_stronger_magnet"]
    }


def arch_33_factors_affecting_electromagnet_strength_current(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"An electromagnet is connected first to a single 1,5 V cell, and then to three 1,5 V cells connected in series (4,5 V), increasing the electric current flowing through the coil threefold.\n\n"
        f"What happens to the magnetic strength of the electromagnet when the current is increased?"
    )
    correct_opt = "The magnetic field strength increases significantly, allowing the electromagnet to lift much heavier magnetic loads."
    options = [
        correct_opt,
        "The magnetic field strength drops to zero because higher current burns out magnetism.",
        "The electromagnet switches polarity from North to South every second.",
        "The electromagnet ceases to be magnetic and turns into a radio transmitter."
    ]
    rng.shuffle(options)
    sol = (
        f"**Current and Electromagnet Strength:**\n"
        f"- Magnetic field strength of a solenoid/electromagnet is directly proportional to current: $B \\propto I$.\n"
        f"- Higher current means more charge flows per second, producing a proportionally stronger magnetic flux in the core.\n"
        f"- Thus, running higher current triples the lifting force (until magnetic saturation of the iron core is reached).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_33_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "33_factors_affecting_electromagnet_strength_current",
        "question_family_id": "33_factors_affecting_electromagnet_strength_current",
        "hints": {
            "tier_1": "Does increasing current increase or decrease magnetic strength?",
            "tier_2": "Higher current creates a stronger magnetic field.",
            "tier_3": "Magnetic field strength increases significantly with greater current."
        },
        "misconception_tags": ["current_does_not_affect_magnet_strength"]
    }


def arch_34_comparing_permanent_magnets_and_electromagnets(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A technology student compares **permanent bar magnets** with **electromagnets** for use in an automated robotic sorting arm.\n\n"
        f"Which major advantage makes electromagnets uniquely suitable for picking up and dropping metal objects on demand?"
    )
    correct_opt = "An electromagnet's magnetic strength can be switched ON and OFF instantly with a switch and can be varied in strength by adjusting current, whereas permanent magnets are always on."
    options = [
        correct_opt,
        "Electromagnets are made of wood and are much lighter than permanent magnets.",
        "Permanent magnets require daily recharging from a 220 V wall outlet.",
        "Electromagnets attract non-magnetic materials like plastic and glass."
    ]
    rng.shuffle(options)
    sol = (
        f"**Electromagnet vs Permanent Magnet Comparison:**\n"
        f"1. **Switchable:** An electromagnet can be switched on to pick up scrap steel, and switched off to drop it. A permanent magnet cannot be switched off.\n"
        f"2. **Adjustable strength:** By varying current or turn count, the lifting power can be fine-tuned.\n"
        f"3. **Reversible poles:** Reversing current direction reverses the North and South magnetic poles.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_34_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "34_comparing_permanent_magnets_and_electromagnets",
        "question_family_id": "34_comparing_permanent_magnets_and_electromagnets",
        "hints": {
            "tier_1": "Can you turn a permanent magnet off? Can you turn an electromagnet off?",
            "tier_2": "Electromagnets can be turned on and off and adjusted.",
            "tier_3": "Electromagnets can be switched on and off instantly and adjusted by current."
        },
        "misconception_tags": ["permanent_magnets_can_be_switched_off"]
    }


def arch_35_application_of_electromagnet_in_scrap_metal_crane(rng: random.Random) -> Dict[str, Any]:
    mass = rng.choice([2, 5, 10])
    prompt = (
        f"In a metal recycling scrapyard in Durban, a giant industrial crane with an electromagnet disk lifts {mass} tonnes of scrap iron and car bodies into a shredder.\n\n"
        f"What sequence of actions does the crane operator perform to lift scrap iron from a pile and release it into the shredder?"
    )
    correct_opt = "Lower disk onto scrap -> switch current ON (magnetizing disk and picking up iron) -> swing crane over shredder -> switch current OFF (demagnetizing disk and dropping iron)."
    options = [
        correct_opt,
        "Keep current ON permanently and scrape the iron off with a wooden pole.",
        "Switch current OFF to pick up metal, and switch current ON to blow the metal off.",
        "Heat the crane disk with gas burners until it melts around the scrap iron."
    ]
    rng.shuffle(options)
    sol = (
        f"**Scrap Metal Crane Operation:**\n"
        f"1. Crane lowers the de-energized disk onto iron scrap.\n"
        f"2. Operator closes circuit switch -> massive current flows -> powerful magnetic field generated -> iron scrap jumps and clings to disk.\n"
        f"3. Crane moves load over the hopper/shredder.\n"
        f"4. Operator opens switch -> current cuts to zero -> magnetic field collapses instantly -> scrap metal drops by gravity.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_35_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "35_application_of_electromagnet_in_scrap_metal_crane",
        "question_family_id": "35_application_of_electromagnet_in_scrap_metal_crane",
        "hints": {
            "tier_1": "When do you want the magnet on, and when do you want it off?",
            "tier_2": "Current ON to pick up scrap; current OFF to drop scrap.",
            "tier_3": "Current ON to pick up, swing, current OFF to drop."
        },
        "misconception_tags": ["electromagnet_drops_metal_by_reversing_gravity"]
    }


def arch_36_operation_of_an_electric_bell_or_buzzer(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a traditional school electric bell, when someone presses the button, the hammer strikes the metal gong repeatedly in rapid succession ('brrrrring').\n\n"
        f"What cyclical mechanism makes the hammer strike the gong repeatedly rather than just once?"
    )
    correct_opt = "The electromagnet attracts a springy iron armature carrying the hammer; as the hammer strikes the gong, it pulls contact points apart, breaking the circuit; the magnet de-energizes, the spring pulls the armature back, re-making the circuit."
    options = [
        correct_opt,
        "The battery contains a tiny mechanical motor with spinning plastic gears.",
        "Electric current bounces like a rubber ball between the gong and the bell wire.",
        "The sound of the gong generates electricity that recharges the battery."
    ]
    rng.shuffle(options)
    sol = (
        f"**Electric Bell Make-and-Break Cycle:**\n"
        f"1. Push switch closes circuit -> current flows through electromagnet.\n"
        f"2. Electromagnet attracts soft iron armature, causing the attached striker (hammer) to hit the gong.\n"
        f"3. Moving forward pulls the contact screw apart from the contact spring, **breaking the circuit**.\n"
        f"4. Current stops -> electromagnet loses magnetism -> spring pulls armature back.\n"
        f"5. Returning to rest touches the contact screw again, **re-making the circuit**.\n"
        f"6. The cycle repeats rapidly (~20 times/sec) as long as the button is held down.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_36_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "36_operation_of_an_electric_bell_or_buzzer",
        "question_family_id": "36_operation_of_an_electric_bell_or_buzzer",
        "hints": {
            "tier_1": "What breaks and re-makes the circuit as the hammer moves?",
            "tier_2": "The moving armature opens the contact, breaking current, then springs back to re-make it.",
            "tier_3": "Electromagnet attracts hammer, breaking contacts; spring returns it, re-making circuit."
        },
        "misconception_tags": ["bells_use_continuous_magnets"]
    }


def arch_37_operation_of_an_electromagnetic_relay_switch(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In car starter circuits and industrial automation, an **electromagnetic relay** is used.\n\n"
        f"What is the functional purpose of a relay in an electrical system?"
    )
    correct_opt = "It uses a low-voltage, low-current safe circuit to activate an electromagnet that mechanically closes a separate high-voltage, high-current circuit."
    options = [
        correct_opt,
        "It amplifies 12 volts directly into 1 000 000 volts without consuming energy.",
        "It converts electrical current into radio signals that transmit through walls.",
        "It replaces fuses by absorbing electrical fires into an internal water chamber."
    ]
    rng.shuffle(options)
    sol = (
        f"**Function of an Electromagnetic Relay:**\n"
        f"1. A car ignition key switch operates at safe, low current ($\\approx 0{{,}}5\\text{{ A}}$).\n"
        f"2. The starter motor requires hundreds of Amperes ($>200\\text{{ A}}$), which would melt a dashboard key switch.\n"
        f"3. Turning the key energizes a small **relay electromagnet**.\n"
        f"4. The electromagnet pulls heavy copper contacts together in a separate, isolated high-current starter circuit.\n"
        f"5. A relay allows safe, remote control of dangerous or high-power circuits.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_37_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "37_operation_of_an_electromagnetic_relay_switch",
        "question_family_id": "37_operation_of_an_electromagnetic_relay_switch",
        "hints": {
            "tier_1": "How can a small safe switch control a massive motor current?",
            "tier_2": "A relay uses a small current to switch a separate high-current circuit.",
            "tier_3": "Uses a low-current circuit to electromagnetically close a high-current circuit."
        },
        "misconception_tags": ["relays_are_just_normal_switches"]
    }


def arch_38_chemical_effect_of_electric_current_definition(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Along with the heating effect and the magnetic effect, electric current can produce a **chemical effect**.\n\n"
        f"What is the chemical effect of an electric current, and what is this process called in physical chemistry?"
    )
    correct_opt = "Electrolysis: the chemical decomposition of an ionic compound (electrolyte) into simpler substances when an electric current passes through it."
    options = [
        correct_opt,
        "Combustion: burning fuel in an open flame to create heat.",
        "Photosynthesis: using green chlorophyll to make glucose from sunlight.",
        "Radioactive decay: spontaneous disintegration of atomic nuclei into lead."
    ]
    rng.shuffle(options)
    sol = (
        f"**Chemical Effect of Electric Current (Electrolysis):**\n"
        f"- When direct current passes through a conducting liquid containing mobile ions (**an electrolyte**), chemical redox reactions occur at the electrodes.\n"
        f"- Positive ions (cations) gain electrons at the cathode (reduction).\n"
        f"- Negative ions (anions) lose electrons at the anode (oxidation).\n"
        f"- This non-spontaneous chemical breakdown driven by electrical energy is called **electrolysis**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_38_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "38_chemical_effect_of_electric_current_definition",
        "question_family_id": "38_chemical_effect_of_electric_current_definition",
        "hints": {
            "tier_1": "What process uses electric current to break down chemical compounds?",
            "tier_2": "This process is called electrolysis.",
            "tier_3": "Electrolysis: chemical decomposition of an electrolyte by electric current."
        },
        "misconception_tags": ["electricity_cannot_cause_chemical_change"]
    }


def arch_39_electrolysis_of_water_into_hydrogen_and_oxygen(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a science laboratory, a Hoffman voltameter filled with acidified water has an electric current passed through it. "
        f"Gas bubbles collect above both the negative cathode and positive anode.\n\n"
        f"What chemical equation represents this decomposition, and what is the ratio of gas volumes collected?"
    )
    correct_opt = "2 H₂O (l) -> 2 H₂ (g) + O₂ (g); two volumes of hydrogen gas collect at the cathode for every one volume of oxygen gas at the anode (2:1 ratio)."
    options = [
        correct_opt,
        "H₂O (l) -> H₂ (g) + O₂ (g); equal volumes of hydrogen and oxygen collect at both electrodes (1:1 ratio).",
        "H₂O (l) -> CO₂ (g) + N₂ (g); carbon dioxide and nitrogen collect in a 3:1 ratio.",
        "Water decomposes into liquid gold and liquid silver with zero gas produced."
    ]
    rng.shuffle(options)
    sol = (
        f"**Electrolysis of Water:**\n"
        f"1. Balanced chemical reaction:\n"
        f"   $$2\\text{{H}}_2\\text{{O}} (l) \\xrightarrow{{\\text{{electricity}}}} 2\\text{{H}}_2 (g) + \\text{{O}}_2 (g)\n$$\n"
        f"2. **Cathode (- terminal):** $4\\text{{H}}^+ + 4e^- \\to 2\\text{{H}}_2 (g)$ -> **Hydrogen gas**.\n"
        f"3. **Anode (+ terminal):** $2\\text{{O}}^{{2-}} \\to \\text{{O}}_2 (g) + 4e^-$ -> **Oxygen gas**.\n"
        f"4. Because water molecules have two hydrogen atoms for every one oxygen atom ($H_2O$), exactly **twice as much hydrogen volume** is generated compared to oxygen (**2:1 volume ratio**).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_39_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "39_electrolysis_of_water_into_hydrogen_and_oxygen",
        "question_family_id": "39_electrolysis_of_water_into_hydrogen_and_oxygen",
        "hints": {
            "tier_1": "What is the formula of water, and what gas ratio does it give?",
            "tier_2": "H2O produces twice as much hydrogen as oxygen (2:1 ratio).",
            "tier_3": "2 H2O -> 2 H2 + O2; 2 volumes of hydrogen to 1 volume of oxygen."
        },
        "misconception_tags": ["water_electrolysis_produces_equal_volumes"]
    }


def arch_40_identifying_gases_produced_at_cathode_and_anode(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"During the electrolysis of acidified water, test tubes of gas collected over the two electrodes are tested with splints:\n\n"
        f"- Gas at Electrode X makes a loud 'pop' sound when tested with a burning wooden splint.\n"
        f"- Gas at Electrode Y relights a glowing wooden splint.\n\n"
        f"Which identification of Electrode X and Electrode Y is scientifically correct?"
    )
    correct_opt = "Electrode X is the Cathode (-) collecting Hydrogen gas; Electrode Y is the Anode (+) collecting Oxygen gas."
    options = [
        correct_opt,
        "Electrode X is the Anode (+) collecting Oxygen gas; Electrode Y is the Cathode (-) collecting Hydrogen gas.",
        "Electrode X is collecting Carbon dioxide; Electrode Y is collecting Nitrogen gas.",
        "Both electrodes are collecting Chlorine gas."
    ]
    rng.shuffle(options)
    sol = (
        f"**Standard Gas Identification Tests:**\n"
        f"1. **Pop test:** Characteristic test for **Hydrogen gas ($H_2$)** -> forms at the **Cathode** (negative electrode where $H^+$ cations gain electrons).\n"
        f"2. **Relighting glowing splint:** Characteristic test for **Oxygen gas ($O_2$)** -> forms at the **Anode** (positive electrode where oxidation occurs).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_40_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "40_identifying_gases_produced_at_cathode_and_anode",
        "question_family_id": "40_identifying_gases_produced_at_cathode_and_anode",
        "hints": {
            "tier_1": "Which gas makes a 'pop' sound, and which gas relights a glowing splint?",
            "tier_2": "Hydrogen pops (Cathode); Oxygen relights a splint (Anode).",
            "tier_3": "Electrode X is Cathode (Hydrogen); Electrode Y is Anode (Oxygen)."
        },
        "misconception_tags": ["swapping_cathode_and_anode_gases"]
    }


def arch_41_concept_and_purpose_of_electroplating(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In manufacturing and jewelry production, objects undergo **electroplating**.\n\n"
        f"What is the definition and primary engineering purpose of electroplating?"
    )
    correct_opt = "Using electrolysis to deposit a thin, protective or decorative layer of one metal onto the surface of another metal object to prevent corrosion, increase hardness, or enhance appearance."
    options = [
        correct_opt,
        "Melting plastic onto metal wires to create electrical insulation.",
        "Dipping metal into acid to dissolve rust and destroy the object.",
        "Heating metal until it glows white-hot to harden its crystalline lattice."
    ]
    rng.shuffle(options)
    sol = (
        f"**Definition of Electroplating:**\n"
        f"- Electroplating is the electrochemical deposition of a thin metal coating onto a conductive object using direct electric current.\n"
        f"- **Purposes:**\n"
        f"  1. **Corrosion resistance:** e.g. zinc-plating or chrome-plating steel car bumpers to stop rust.\n"
        f"  2. **Aesthetic/decorative value:** e.g. coating cheap brass cutlery or jewelry with thin layers of gold or silver.\n"
        f"  3. **Wear resistance:** chrome plating on hydraulic cylinders.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_41_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "41_concept_and_purpose_of_electroplating",
        "question_family_id": "41_concept_and_purpose_of_electroplating",
        "hints": {
            "tier_1": "What is electroplating used for in jewelry or car parts?",
            "tier_2": "Depositing a thin metal layer using electrolysis for protection or decoration.",
            "tier_3": "Depositing a thin metal layer onto an object to prevent corrosion or enhance appearance."
        },
        "misconception_tags": ["electroplating_is_painting"]
    }


def arch_42_anode_cathode_and_electrolyte_in_copper_plating(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A student sets up an electrolytic bath to coat an iron key with a shiny layer of pure copper.\n\n"
        f"Which arrangement of cathode, anode, and electrolyte solution is required for copper plating?"
    )
    correct_opt = "Cathode (-): Iron key | Anode (+): Pure copper strip | Electrolyte: Copper sulphate solution (CuSO₄)"
    options = [
        correct_opt,
        "Cathode (-): Pure copper strip | Anode (+): Iron key | Electrolyte: Distilled pure water",
        "Cathode (-): Iron key | Anode (+): Zinc strip | Electrolyte: Sodium chloride solution",
        "Cathode (-): Plastic ruler | Anode (+): Wooden spoon | Electrolyte: Mineral cooking oil"
    ]
    rng.shuffle(options)
    sol = (
        f"**Rules of Electroplating Setup:**\n"
        f"1. **Cathode (negative electrode):** MUST be the **object to be plated** (the iron key). Negative charge attracts positive metal cations ($Cu^{{2+}}$).\n"
        f"2. **Anode (positive electrode):** MUST be made of the **coating metal** (pure copper). It dissolves ($Cu \\to Cu^{{2+}} + 2e^-$) to replenish the solution.\n"
        f"3. **Electrolyte:** MUST be a soluble salt containing ions of the coating metal (**copper sulphate**, $CuSO_4$).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_42_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "42_anode_cathode_and_electrolyte_in_copper_plating",
        "question_family_id": "42_anode_cathode_and_electrolyte_in_copper_plating",
        "hints": {
            "tier_1": "Which electrode must the object to be plated be attached to: positive or negative?",
            "tier_2": "The object is the negative cathode. The plating metal is the positive anode.",
            "tier_3": "Cathode (-): Iron key | Anode (+): Pure copper strip | Electrolyte: Copper sulphate solution."
        },
        "misconception_tags": ["object_to_be_plated_is_anode"]
    }


def arch_43_electroplating_jewellery_gold_and_silver(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("silver", "silver cyanide or silver nitrate solution", "inexpensive brass spoons or teapots"),
        ("gold", "gold potassium cyanide solution", "costume jewelry earrings or watch cases")
    ]
    coating, electrolyte, items = rng.choice(metals)
    prompt = (
        f"In commercial jewelry finishing, **{items}** are electroplated with a thin layer of **{coating}** using **{electrolyte}**.\n\n"
        f"What chemical reaction occurs directly at the cathode surface to form the shiny metal coating?"
    )
    correct_opt = f"Positive {coating} metal ions in the solution gain electrons from the negative cathode and precipitate as solid {coating} metal atoms adhering to the object."
    options = [
        correct_opt,
        f"The {coating} atoms evaporate from the liquid and condense as gas onto the ceiling.",
        "The brass object dissolves completely and disappears into the electrolyte.",
        f"Electric current burns the {coating} ions into ash that sticks like paint."
    ]
    rng.shuffle(options)
    sol = (
        f"**Cathode Reduction Reaction in Electroplating:**\n"
        f"1. The item being plated is connected to the negative terminal (cathode), making its surface rich in excess electrons.\n"
        f"2. Positive {coating} metal ions in solution ($M^{{+}}$) migrate toward the cathode.\n"
        f"3. At the surface: $M^{{+}} + e^- \\to M (s)$ (Reduction).\n"
        f"4. The newly formed neutral metal atoms bond to the metal crystal lattice of the object, building a smooth, adherent microscopic plating layer.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_43_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "43_electroplating_jewellery_gold_and_silver",
        "question_family_id": "43_electroplating_jewellery_gold_and_silver",
        "hints": {
            "tier_1": "What happens when positive ions reach the negative cathode?",
            "tier_2": "They gain electrons and deposit as neutral solid metal atoms.",
            "tier_3": f"Positive {coating} ions gain electrons at the cathode and deposit as solid metal."
        },
        "misconception_tags": ["electroplating_is_evaporation"]
    }


def arch_44_industrial_electro_refining_of_blister_copper(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Smelted copper from mines (such as Palabora Mining Company in Limpopo) is approximately 98% pure ('blister copper'), which is inadequate for electrical wiring because impurities greatly increase resistance.\n\n"
        f"How is industrial **electro-refining** used to purify blister copper to 99,99% electrical-grade copper?"
    )
    correct_opt = "Impure blister copper is cast as the anode (+); during electrolysis, copper dissolves into the solution and plates out as 99,99% pure copper on cathode (-) starter sheets, leaving impurities behind."
    options = [
        correct_opt,
        "Blister copper is dissolved in acid and boiled until only radioactive steam remains.",
        "The copper is hammered by hand until all impurities bounce out mechanically.",
        "Electrolysis turns all non-copper impurities directly into pure gold."
    ]
    rng.shuffle(options)
    sol = (
        f"**Industrial Electro-refining of Copper:**\n"
        f"1. **Anode (+):** Giant slabs of impure blister copper (98% Cu).\n"
        f"2. **Cathode (-):** Thin starter sheets of pure copper.\n"
        f"3. **Electrolyte:** Copper sulphate ($CuSO_4$) acidified with sulfuric acid.\n"
        f"4. Under controlled voltage, copper atoms at the anode oxidize: $Cu (s) \\to Cu^{{2+}} + 2e^-$.\n"
        f"5. Only copper ions reduce onto the cathode: $Cu^{{2+}} + 2e^- \\to Cu (s)$ (99,99% pure).\n"
        f"6. Valuable impurities (silver, gold, platinum) fall to the tank floor as 'anode slime' and are recovered.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_44_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "44_industrial_electro_refining_of_blister_copper",
        "question_family_id": "44_industrial_electro_refining_of_blister_copper",
        "hints": {
            "tier_1": "Which electrode dissolves and which collects pure copper?",
            "tier_2": "Impure copper anode dissolves; pure copper deposits on the cathode.",
            "tier_3": "Impure copper anode dissolves; 99,99% pure copper plates onto the cathode."
        },
        "misconception_tags": ["electro_refining_is_melting"]
    }


def arch_45_ammeter_series_connection_and_low_internal_resistance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In circuit design, an **ammeter** measures the electric current flowing through a branch.\n\n"
        f"How must an ammeter be connected into a circuit, and why must an ammeter have an extremely **low internal resistance**?"
    )
    correct_opt = "Connected in SERIES, with near-zero internal resistance so that all current passes through it without reducing the circuit's total current."
    options = [
        correct_opt,
        "Connected in PARALLEL, with infinite internal resistance so it stops all current flow.",
        "Connected outside the circuit on the table without touching any wires.",
        "Connected across the battery terminals with massive resistance to generate heat."
    ]
    rng.shuffle(options)
    sol = (
        f"**Ammeter Connection Rules:**\n"
        f"1. **Series connection:** To count the Coulombs passing per second, the circuit path must be broken and the ammeter inserted directly into the line (**in series**).\n"
        f"2. **Very low internal resistance ($R \\approx 0$):** If an ammeter had significant resistance, inserting it would increase total circuit resistance and falsely decrease the current it is trying to measure.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_45_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "45_ammeter_series_connection_and_low_internal_resistance",
        "question_family_id": "45_ammeter_series_connection_and_low_internal_resistance",
        "hints": {
            "tier_1": "Is an ammeter connected in series or parallel?",
            "tier_2": "In series, with very low resistance so it doesn't reduce current.",
            "tier_3": "Connected in series with near-zero internal resistance."
        },
        "misconception_tags": ["ammeter_connected_in_parallel"]
    }


def arch_46_voltmeter_parallel_connection_and_high_internal_resistance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A **voltmeter** measures the potential difference (voltage) across a component (e.g. a resistor or bulb).\n\n"
        f"How must a voltmeter be connected into a circuit, and why must it possess an extremely **high internal resistance**?"
    )
    correct_opt = "Connected in PARALLEL across the component, with near-infinite internal resistance so that virtually zero current diverts through the voltmeter."
    options = [
        correct_opt,
        "Connected in SERIES directly in the main wire, with zero internal resistance.",
        "Wrapped around the battery in bubble wrap to protect the needle.",
        "Connected only when the circuit switch is turned completely off."
    ]
    rng.shuffle(options)
    sol = (
        f"**Voltmeter Connection Rules:**\n"
        f"1. **Parallel connection:** Potential difference is the work done per unit charge between *two separate points*. The voltmeter probes must touch across the component (**in parallel**).\n"
        f"2. **Very high internal resistance ($R \\to \\infty$):** If a voltmeter had low resistance, current would bypass the component through the meter (causing a short circuit). High resistance ensures virtually no current leaks through the voltmeter.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_46_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "46_voltmeter_parallel_connection_and_high_internal_resistance",
        "question_family_id": "46_voltmeter_parallel_connection_and_high_internal_resistance",
        "hints": {
            "tier_1": "Is a voltmeter connected in series or parallel?",
            "tier_2": "In parallel across the component, with very high internal resistance.",
            "tier_3": "Connected in parallel across the component, with near-infinite internal resistance."
        },
        "misconception_tags": ["voltmeter_connected_in_series"]
    }


def arch_47_misconception_electrons_are_consumed_in_circuit(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner says: *'The electric current leaving a light bulb is smaller than the current entering it because electrons are used up and consumed to make light.'*\n\n"
        f"How does the Principle of Conservation of Charge refute this statement?"
    )
    correct_opt = "Electrons are fundamental particles and are NEVER destroyed or consumed; only their electrical potential energy is converted into light and heat, while the exact same number of electrons exits the bulb as enters it."
    options = [
        correct_opt,
        "The learner is correct because light is made of converted, destroyed electrons.",
        "Electrons multiply inside the bulb, so more electrons exit than enter.",
        "All electrons are permanently absorbed by the glass envelope."
    ]
    rng.shuffle(options)
    sol = (
        f"**Conservation of Charge in Circuits:**\n"
        f"- Electrons are indestructible in an electric circuit.\n"
        f"- Current is the **rate of flow** of electrons ($I = \\frac{{Q}}{{t}}$).\n"
        f"- In a series circuit, current entering a component equals current leaving it ($I_\\text{{in}} = I_\\text{{out}}$).\n"
        f"- What is 'used up' is **energy** (joules), not the physical electrons themselves (coulombs)!\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_47_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "47_misconception_electrons_are_consumed_in_circuit",
        "question_family_id": "47_misconception_electrons_are_consumed_in_circuit",
        "hints": {
            "tier_1": "Are electrons consumed, or is energy converted?",
            "tier_2": "Electrons are not consumed; only electrical energy is converted into light/heat.",
            "tier_3": "Electrons are never destroyed; only energy is transformed into light and heat."
        },
        "misconception_tags": ["electrons_are_consumed"]
    }


def arch_48_misconception_current_slows_down_after_passing_resistor(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a simple series circuit with a battery, a single resistor, and two ammeters (Ammeter 1 placed before the resistor and Ammeter 2 placed after the resistor).\n\n"
        f"How will the readings on Ammeter 1 ($I_1$) and Ammeter 2 ($I_2$) compare?"
    )
    correct_opt = "I₁ = I₂ (both ammeters show identical readings), because electric current is constant everywhere throughout a single series loop."
    options = [
        correct_opt,
        "I₁ is much larger than I₂ because the resistor slows down and stores current.",
        "I₂ is twice as large as I₁ because resistors speed up electrons.",
        "I₂ drops to zero because all current is blocked inside the resistor."
    ]
    rng.shuffle(options)
    sol = (
        f"**Current Constancy in a Series Circuit:**\n"
        f"- A series circuit is like a closed pipe filled with water: water cannot pile up inside the pipe.\n"
        f"- The resistor limits the overall flow rate throughout the *entire* circuit.\n"
        f"- The rate at which electrons enter the resistor equals the rate at which they exit: $I_1 = I_2$.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_48_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "48_misconception_current_slows_down_after_passing_resistor",
        "question_family_id": "48_misconception_current_slows_down_after_passing_resistor",
        "hints": {
            "tier_1": "Is current the same everywhere in a series loop?",
            "tier_2": "Current is identical everywhere in a series circuit: I1 = I2.",
            "tier_3": "I1 = I2; both ammeters show identical readings."
        },
        "misconception_tags": ["current_attenuation_after_resistor"]
    }


def arch_49_misconception_battery_stores_actual_electrons(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner describes a torch battery as *'a bucket that stores billions of extra electrons waiting to pour out into empty wires.'*\n\n"
        f"Why is this description scientifically inaccurate?"
    )
    correct_opt = "Conducting wires are ALREADY packed with delocalised electrons; a battery stores chemical potential energy that acts like a pump to push existing electrons through the circuit."
    options = [
        correct_opt,
        "The learner is correct because empty wires have zero electrons until a battery is plugged in.",
        "Batteries store protons, not electrons.",
        "Batteries only work when connected to a running municipal water tap."
    ]
    rng.shuffle(options)
    sol = (
        f"**Battery Function Clarification:**\n"
        f"1. Copper wires are never 'empty' of charge; every copper atom contributes delocalised electrons.\n"
        f"2. A battery does NOT supply the electrons that flow through the wires.\n"
        f"3. A battery provides the **energy** (electromotive force / potential difference) that pushes and circulates the electrons that are already present throughout the entire conducting circuit.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_49_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "49_misconception_battery_stores_actual_electrons",
        "question_family_id": "49_misconception_battery_stores_actual_electrons",
        "hints": {
            "tier_1": "Are wires empty of electrons before connecting a battery?",
            "tier_2": "Wires already have delocalised electrons. The battery acts as a pump, providing energy.",
            "tier_3": "Wires already contain delocalised electrons; a battery provides energy to push them."
        },
        "misconception_tags": ["battery_stores_electrons"]
    }


def arch_50_energy_transfer_electrical_systems_comprehensive_diagnostic(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A comprehensive examination question evaluates three core effects of an electric current:\n"
        f"Effect 1: Heating effect (used in kettles, geysers, toasters, and safety fuses).\n"
        f"Effect 2: Magnetic effect (used in electromagnets, electric bells, scrap cranes, and relays).\n"
        f"Effect 3: Chemical effect (used in electrolysis of water, electroplating, and metal refining).\n\n"
        f"Which statement correctly assesses these three fundamental effects of current electricity?"
    )
    correct_opt = "All three statements (Effect 1, Effect 2, and Effect 3) represent authentic, foundational physical and chemical effects of an electric current."
    options = [
        correct_opt,
        "Only Effect 1 is scientifically real; electric current has zero magnetic or chemical capabilities.",
        "Only Effect 2 is real; heating is caused exclusively by friction with air outside the wire.",
        "All three effects are outdated 19th-century scientific myths."
    ]
    rng.shuffle(options)
    sol = (
        f"**The Three Foundational Effects of Electric Current:**\n"
        f"1. **Heating Effect:** $P = I^2 R$ produces thermal energy in resistors (kettles, irons, fuses).\n"
        f"2. **Magnetic Effect:** Oersted's discovery: current produces magnetic fields (electromagnets, bells, motors).\n"
        f"3. **Chemical Effect:** Electrolytic decomposition and ion deposition (electroplating, refining).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_el_50_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "50_energy_transfer_electrical_systems_comprehensive_diagnostic",
        "question_family_id": "50_energy_transfer_electrical_systems_comprehensive_diagnostic",
        "hints": {
            "tier_1": "Are heating, magnetic, and chemical effects all authentic effects of electric current?",
            "tier_2": "Every one of the three statements represents a major effect of an electric current.",
            "tier_3": "All three statements represent authentic, foundational effects of an electric current."
        },
        "misconception_tags": ["diagnostic_synthesis_error"]
    }
