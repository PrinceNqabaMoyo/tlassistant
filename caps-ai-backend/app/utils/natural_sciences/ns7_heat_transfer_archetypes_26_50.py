"""Grade 7 Natural Sciences: Term 3 - Heat Energy Transfer Archetypes (26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/03. Heat Energy transfer.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List


def arch_26_matt_black_versus_shiny_white_absorbers_experiment(rng: random.Random) -> Dict[str, Any]:
    dist = rng.choice([15, 20, 25])
    temp_init = rng.choice([20, 22, 24])
    prompt = (
        f"Two identical tin cans, Can A painted matt (dull) black and Can B painted shiny silver/white, each contain $100\\text{{ cm}}^3$ of water at {temp_init} °C. "
        f"Both cans are placed at an equal distance of {dist} cm from an infrared heat lamp and exposed for 15 minutes.\n\n"
        f"Which can will record the higher water temperature after 15 minutes, and why?"
    )
    correct_opt = "Can A (matt black), because dark, dull surfaces are superior absorbers of thermal radiation compared to shiny, reflective surfaces."
    options = [
        correct_opt,
        "Can B (shiny silver), because shiny surfaces attract and magnify infrared rays like a magnifying glass.",
        "Both cans will reach the exact same temperature because colour has zero influence on radiation absorption.",
        "Can B, because white paint contains chemical heating crystals that activate under light."
    ]
    rng.shuffle(options)
    sol = (
        f"**Absorption of Thermal Radiation:**\n"
        f"1. Matt black surfaces absorb almost all incident thermal radiation and convert it to heat.\n"
        f"2. Shiny silver/white surfaces reflect most of the incident thermal radiation away.\n"
        f"3. Therefore, water in Can A absorbs much more radiant heat energy and reaches a significantly higher temperature.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_26_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "26_matt_black_versus_shiny_white_absorbers_experiment",
        "question_family_id": "26_matt_black_versus_shiny_white_absorbers_experiment",
        "hints": {
            "tier_1": "Which absorbs more heat: dull black or shiny silver?",
            "tier_2": "Black absorbs radiant heat; shiny surfaces reflect radiant heat.",
            "tier_3": "Can A (matt black) absorbs radiation best and reaches a higher temperature."
        },
        "misconception_tags": ["shiny_absorbs_more_radiation"]
    }


def arch_27_matt_black_versus_shiny_white_emitters_experiment(rng: random.Random) -> Dict[str, Any]:
    temp_hot = rng.choice([80, 85, 90])
    prompt = (
        f"Two identical metal teapots, one painted dull matt black and the other polished shiny silver, are filled with boiling water at {temp_hot} °C and left to cool on a kitchen counter in still air.\n\n"
        f"Which teapot will cool down to room temperature faster by emitting thermal radiation?"
    )
    correct_opt = "The dull matt black teapot, because good absorbers of thermal radiation are also the best emitters of thermal radiation."
    options = [
        correct_opt,
        "The polished shiny silver teapot, because shiny metals emit radiation ten times faster than black surfaces.",
        "Both teapots cool down at the exact same identical rate because emission is independent of surface finish.",
        "The black teapot stays hot forever because black surfaces trap all heat inside permanently."
    ]
    rng.shuffle(options)
    sol = (
        f"**Emission of Thermal Radiation:**\n"
        f"1. A fundamental law of thermal physics states that good absorbers of radiation are also **good emitters** of radiation.\n"
        f"2. Poor absorbers (shiny, light-coloured surfaces) are **poor emitters**.\n"
        f"3. The dull black teapot emits infrared radiation into the surrounding room much faster than the shiny silver teapot.\n"
        f"4. Consequently, the black teapot cools down faster.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_27_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "27_matt_black_versus_shiny_white_emitters_experiment",
        "question_family_id": "27_matt_black_versus_shiny_white_emitters_experiment",
        "hints": {
            "tier_1": "Are good absorbers also good emitters or poor emitters?",
            "tier_2": "Dull black surfaces are both the best absorbers and best emitters of heat.",
            "tier_3": "The matt black teapot radiates heat away faster and cools quicker."
        },
        "misconception_tags": ["absorbers_are_poor_emitters"]
    }


def arch_28_solar_collector_plates_black_surface_selection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Solar water heating panels installed on residential rooftops across South Africa feature copper pipes bonded to a metal absorber plate painted with specialised matt black paint.\n\n"
        f"Why is the solar absorber plate painted matt black rather than shiny chrome or white?"
    )
    correct_opt = "Matt black absorbs the maximum percentage of incoming solar radiation, converting radiant energy efficiently into thermal energy to heat the water."
    options = [
        correct_opt,
        "Matt black paint is waterproof, whereas white paint dissolves instantly in rainwater.",
        "Shiny chrome absorbs too much radiation and would cause the roof to catch fire.",
        "Black colour repels UV rays into outer space to prevent sunburn on the tiles."
    ]
    rng.shuffle(options)
    sol = (
        f"**Solar Thermal Engineering:**\n"
        f"- The primary goal of a solar collector is to harvest maximum radiant energy from the Sun.\n"
        f"- Dark, matt black finishes have an absorption coefficient of over 95%, meaning almost all incident solar radiation is absorbed rather than reflected.\n"
        f"- The absorbed energy is conducted into the copper pipes and heats the circulating water.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_28_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "28_solar_collector_plates_black_surface_selection",
        "question_family_id": "28_solar_collector_plates_black_surface_selection",
        "hints": {
            "tier_1": "What colour absorbs maximum sunlight?",
            "tier_2": "Matt black surfaces absorb maximum radiation and minimize reflection.",
            "tier_3": "Matt black absorbs the maximum percentage of incoming solar radiation."
        },
        "misconception_tags": ["reflective_heats_better"]
    }


def arch_29_silver_emergency_space_blanket_reflection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Paramedics and mountain rescue teams wrap hypothermia patients in lightweight, shiny, silver-coated plastic foil 'space blankets'.\n\n"
        f"How does the shiny silver surface of the emergency blanket help keep the patient warm?"
    )
    correct_opt = "The shiny silver inner surface reflects infrared thermal radiation emitted by the human body back toward the patient, minimizing radiant heat loss."
    options = [
        correct_opt,
        "The foil generates its own thermal energy through radioactive decay of aluminium atoms.",
        "The silver layer absorbs coldness from the patient's skin and stores it in the foil.",
        "The blanket is electrically charged and sends high-voltage warming currents into muscles."
    ]
    rng.shuffle(options)
    sol = (
        f"**Mechanism of Emergency Space Blankets:**\n"
        f"1. A living human body continually radiates thermal energy in the form of infrared waves.\n"
        f"2. The shiny, mirror-like aluminized surface has very low emissivity and high reflectivity (>90%).\n"
        f"3. It reflects the body's own emitted infrared radiation back toward the skin.\n"
        f"4. It also prevents wind from removing warm air by convection.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_29_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "29_silver_emergency_space_blanket_reflection",
        "question_family_id": "29_silver_emergency_space_blanket_reflection",
        "hints": {
            "tier_1": "What does a shiny mirror surface do to radiation waves?",
            "tier_2": "It reflects infrared radiation emitted by the human body back to the patient.",
            "tier_3": "The shiny silver surface reflects body heat radiation back inward."
        },
        "misconception_tags": ["blankets_generate_their_own_heat"]
    }


def arch_30_thermos_vacuum_flask_conduction_prevention(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A double-walled vacuum flask (Thermos) keeps hot soup hot for many hours. "
        f"Between the inner glass container and the outer container is a sealed space where all air has been removed (a vacuum).\n\n"
        f"How does this vacuum layer specifically prevent heat loss by **conduction**?"
    )
    correct_opt = "Conduction requires material particles to collide and pass on kinetic energy; in a vacuum, there are zero particles, making conduction completely impossible."
    options = [
        correct_opt,
        "The vacuum is extremely cold and freezes any heat trying to escape.",
        "The vacuum contains magnetic fields that deflect heat particles back into the soup.",
        "Air particles in the vacuum are packed so tightly that heat cannot squeeze between them."
    ]
    rng.shuffle(options)
    sol = (
        f"**Vacuum Flask & Conduction:**\n"
        f"- Conduction relies on particle-to-particle collisions.\n"
        f"- By evacuating all air from the space between the double walls, no particles remain to collide.\n"
        f"- Thus, thermal conduction across the gap is entirely eliminated.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_30_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "30_thermos_vacuum_flask_conduction_prevention",
        "question_family_id": "30_thermos_vacuum_flask_conduction_prevention",
        "hints": {
            "tier_1": "Can conduction occur without particles?",
            "tier_2": "No particles exist in a vacuum, so conduction cannot happen.",
            "tier_3": "Conduction requires particles to collide; a vacuum has no particles."
        },
        "misconception_tags": ["vacuum_can_conduct"]
    }


def arch_31_thermos_vacuum_flask_convection_prevention(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In addition to stopping conduction, how does the vacuum gap and the tight plastic or cork stopper in a Thermos flask prevent heat loss by **convection**?"
    )
    correct_opt = "The vacuum has no fluid particles to form convection currents across the gap, and the stopper seals the top to prevent hot air currents and evaporating steam from escaping."
    options = [
        correct_opt,
        "The stopper creates a vortex that spins cold air out into the atmosphere.",
        "The vacuum speeds up convection so much that heat returns before leaving.",
        "The cork stopper conducts cold from the kitchen table into the liquid."
    ]
    rng.shuffle(options)
    sol = (
        f"**Vacuum Flask & Convection:**\n"
        f"1. Convection requires fluid (gas or liquid) particles that can circulate in bulk.\n"
        f"2. The vacuum between the walls contains no fluid, preventing convection currents across the walls.\n"
        f"3. The insulated stopper at the top seals the opening, preventing hot air and warm vapour from rising out of the flask.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_31_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "31_thermos_vacuum_flask_convection_prevention",
        "question_family_id": "31_thermos_vacuum_flask_convection_prevention",
        "hints": {
            "tier_1": "What is needed for convection currents to form?",
            "tier_2": "A fluid is needed. No fluid in a vacuum, and stopper stops air escape.",
            "tier_3": "No fluid particles in the vacuum, and the stopper seals hot air/steam inside."
        },
        "misconception_tags": ["convection_in_a_vacuum"]
    }


def arch_32_thermos_vacuum_flask_radiation_prevention(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Even across a perfect vacuum, heat can still transfer in the form of infrared radiation. "
        f"How does the internal design of a vacuum flask prevent this radiative heat transfer?"
    )
    correct_opt = "The glass walls facing the vacuum are coated with a shiny silver mirror layer that reflects infrared radiation back into the hot liquid (and reflects outside radiation away from cold liquid)."
    options = [
        correct_opt,
        "The walls are painted pitch black so they can absorb all radiation and destroy it.",
        "A small magnetic coil absorbs infrared waves and transforms them into sound.",
        "The outer plastic shell filters out cosmic heat waves from outer space."
    ]
    rng.shuffle(options)
    sol = (
        f"**Vacuum Flask & Radiation:**\n"
        f"- Thermal radiation (infrared waves) can cross a vacuum.\n"
        f"- To block radiation, the inner glass walls facing the vacuum are silvered (mirror-coated).\n"
        f"- The shiny surface has very low emissivity and high reflectivity.\n"
        f"- It reflects escaping infrared radiation back into the hot liquid.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_32_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "32_thermos_vacuum_flask_radiation_prevention",
        "question_family_id": "32_thermos_vacuum_flask_radiation_prevention",
        "hints": {
            "tier_1": "What reflects infrared radiation waves?",
            "tier_2": "Silvered mirror surfaces reflect thermal radiation.",
            "tier_3": "Shiny silver coatings on the glass walls reflect infrared radiation back."
        },
        "misconception_tags": ["silver_absorbs_radiation"]
    }


def arch_33_identifying_heat_transfer_in_boiling_kettle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Consider an electric kettle boiling water on a kitchen counter:\n"
        f"I. Heat transfers from the submerged metal heating element through its metal surface into the adjacent water.\n"
        f"II. Hot water at the element expands, rises, and circulates throughout the kettle volume.\n"
        f"III. Your hand held 10 cm above the outside stainless steel kettle body feels warmth.\n\n"
        f"Which sequence correctly identifies heat transfer modes I, II, and III?"
    )
    correct_opt = "I: Conduction | II: Convection | III: Radiation (with some convection)"
    options = [
        correct_opt,
        "I: Radiation | II: Conduction | III: Convection",
        "I: Convection | II: Radiation | III: Conduction",
        "I: Conduction | II: Conduction | III: Conduction"
    ]
    rng.shuffle(options)
    sol = (
        f"**Analysis of Kettle Heat Transfers:**\n"
        f"- **I (Element to water):** Direct contact between metal solid and liquid boundary = **Conduction**.\n"
        f"- **II (Circulation of water):** Cyclic fluid movement caused by density differences = **Convection**.\n"
        f"- **III (Heat radiating outward):** Infrared waves emitted from the hot surface = **Radiation**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_33_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "33_identifying_heat_transfer_in_boiling_kettle",
        "question_family_id": "33_identifying_heat_transfer_in_boiling_kettle",
        "hints": {
            "tier_1": "What happens through solid contact, what happens by fluid motion, and what radiates?",
            "tier_2": "Through metal is conduction; circulating water is convection; emitted warmth is radiation.",
            "tier_3": "I is Conduction, II is Convection, III is Radiation."
        },
        "misconception_tags": ["single_transfer_mode_fallacy"]
    }


def arch_34_identifying_heat_transfer_around_a_campfire(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Around an open wood braai or campfire at night:\n"
        f"- Person A sits 2 metres to the side and feels warming heat on their face.\n"
        f"- Person B holds their hands directly above the smoke and flame and feels strong rising heat.\n"
        f"- Person C holds a metal braai tong whose tip has been resting in the glowing embers.\n\n"
        f"Which mechanism of heat transfer predominantly affects Person A, Person B, and Person C?"
    )
    correct_opt = "Person A: Radiation | Person B: Convection | Person C: Conduction"
    options = [
        correct_opt,
        "Person A: Conduction | Person B: Radiation | Person C: Convection",
        "Person A: Convection | Person B: Conduction | Person C: Radiation",
        "All three individuals experience heat exclusively by conduction"
    ]
    rng.shuffle(options)
    sol = (
        f"**Campfire Heat Transfer Analysis:**\n"
        f"1. **Person A (to the side):** Hot air rises upward, not sideways. The warmth felt on the face is infrared **Radiation**.\n"
        f"2. **Person B (above the flame):** Warm, less dense air and combustion gases rise directly upward by **Convection**.\n"
        f"3. **Person C (holding tongs in embers):** Heat travels through the solid metal tongs via particle vibrations by **Conduction**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_34_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "34_identifying_heat_transfer_around_a_campfire",
        "question_family_id": "34_identifying_heat_transfer_around_a_campfire",
        "hints": {
            "tier_1": "Remember warm air rises (convection), heat felt sideways is radiation, heat along metal is conduction.",
            "tier_2": "A = sideways (radiation), B = directly above (convection), C = through metal tongs (conduction).",
            "tier_3": "Person A: Radiation | Person B: Convection | Person C: Conduction."
        },
        "misconception_tags": ["convection_travels_sideways"]
    }


def arch_35_identifying_heat_transfer_in_domestic_oven(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a modern domestic convection oven, a fan circulates hot air past the baking trays. "
        f"A baking dish rests directly on a metal wire rack, while the top glowing element toasts the cheese topping.\n\n"
        f"Which heat transfer method corresponds to the fan circulating air, the rack touching the dish, and the glowing top element?"
    )
    correct_opt = "Circulating air: Convection | Metal rack touching dish: Conduction | Glowing element: Radiation"
    options = [
        correct_opt,
        "Circulating air: Conduction | Metal rack touching dish: Radiation | Glowing element: Convection",
        "Circulating air: Radiation | Metal rack touching dish: Convection | Glowing element: Conduction",
        "All three operations rely entirely on nuclear fission radiation"
    ]
    rng.shuffle(options)
    sol = (
        f"**Oven Heat Transfers:**\n"
        f"- Fan moving hot air = Forced **Convection**.\n"
        f"- Direct solid-to-solid contact between wire rack and baking dish = **Conduction**.\n"
        f"- Glowing element emitting infrared electromagnetic rays downward onto food = **Radiation**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_35_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "35_identifying_heat_transfer_in_domestic_oven",
        "question_family_id": "35_identifying_heat_transfer_in_domestic_oven",
        "hints": {
            "tier_1": "Air circulating = convection; touching solids = conduction; glowing element = radiation.",
            "tier_2": "Match fluid movement, contact, and electromagnetic emission.",
            "tier_3": "Convection for circulating air, conduction for rack-to-dish, radiation for glowing element."
        },
        "misconception_tags": ["oven_is_purely_radiant"]
    }


def arch_36_heat_transfer_in_refrigerator_cooling_coils(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"At the back of a domestic refrigerator, a network of black metal cooling coils (condenser) feels warm to the touch. "
        f"Why are these external coils painted black and designed with thin metal cooling fins?"
    )
    correct_opt = "The fins increase the surface area for conduction and convection to the surrounding air, while black paint enhances the emission of thermal radiation."
    options = [
        correct_opt,
        "Black paint hides dirt so the refrigerator requires less cleaning.",
        "The fins trap heat permanently behind the fridge so it never escapes.",
        "The black colour magnetises oxygen molecules to freeze them instantly."
    ]
    rng.shuffle(options)
    sol = (
        f"**Refrigerator Heat Dissipation:**\n"
        f"1. A refrigerator removes heat from inside the food compartment and must dump this heat into the kitchen air.\n"
        f"2. Thin metal fins drastically increase total **surface area**, speeding up **conduction** to air and promoting natural **convection currents**.\n"
        f"3. Matt black coating maximises **thermal radiation emission** into the surroundings.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_36_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "36_heat_transfer_in_refrigerator_cooling_coils",
        "question_family_id": "36_heat_transfer_in_refrigerator_cooling_coils",
        "hints": {
            "tier_1": "Why do heat sinks have fins and dark surfaces?",
            "tier_2": "Large surface area boosts convection/conduction; black colour boosts radiation emission.",
            "tier_3": "Fins increase surface area; black paint maximises radiation emission."
        },
        "misconception_tags": ["black_only_absorbs_never_emits"]
    }


def arch_37_car_radiator_cooling_system_heat_loss(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A car's engine generates intense thermal energy. Hot coolant liquid flows from the engine into the radiator at the front of the vehicle. "
        f"As the car drives forward, outside air passes through hundreds of tiny aluminium radiator fins.\n\n"
        f"What sequence of heat transfers takes place in the car radiator?"
    )
    correct_opt = "Heat is conducted from hot liquid through thin metal tube walls into the aluminium fins, then transferred to passing air by forced convection and conduction."
    options = [
        correct_opt,
        "Hot liquid turns into radiation beams that project through the front headlights into the street.",
        "The radiator uses nuclear cooling rods to destroy thermal energy completely.",
        "Heat is stored in the tyres and converted into rubber mass."
    ]
    rng.shuffle(options)
    sol = (
        f"**Radiator Heat Transfer Process:**\n"
        f"1. Coolant carries internal heat from the engine blocks.\n"
        f"2. Inside the radiator, heat is **conducted** through the thin copper/aluminium tube walls into the attached fins.\n"
        f"3. Air forced through the grille carries heat away via **convection** and **conduction**.\n"
        f"4. Cooled liquid is pumped back into the engine block to repeat the cycle.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_37_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "37_car_radiator_cooling_system_heat_loss",
        "question_family_id": "37_car_radiator_cooling_system_heat_loss",
        "hints": {
            "tier_1": "How does heat leave the hot liquid through the metal to the air?",
            "tier_2": "Conduction through the metal tubes and fins, then convection into moving air.",
            "tier_3": "Conduction through metal walls into fins, then forced convection into passing air."
        },
        "misconception_tags": ["radiators_cool_only_by_radiation"]
    }


def arch_38_greenhouse_effect_trapping_thermal_radiation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"On a bright sunny winter day, the interior of a car parked with windows closed or the inside of a glass agricultural greenhouse becomes significantly warmer than the outside air.\n\n"
        f"What thermal radiation mechanism explains this heating?"
    )
    correct_opt = "High-energy, short-wavelength solar radiation passes easily through transparent glass and warms internal objects; these objects re-radiate longer-wavelength infrared radiation, which cannot pass back through glass easily and remains trapped."
    options = [
        correct_opt,
        "Glass creates heat from nitrogen gas whenever exposed to daylight.",
        "Convection currents carry hot air from the upper atmosphere through microscopic pores in the glass.",
        "Glass prevents all heat from leaving because glass is an absolute superconductor of thermal vibrations."
    ]
    rng.shuffle(options)
    sol = (
        f"**The Greenhouse Mechanism:**\n"
        f"1. Short-wavelength solar radiation (visible and near-infrared) penetrates transparent glass.\n"
        f"2. Interior surfaces (seats, dashboard, soil, plants) absorb this radiation and heat up.\n"
        f"3. The warmed surfaces re-emit thermal energy as longer-wavelength infrared radiation.\n"
        f"4. Glass is mostly opaque to this longer-wavelength infrared radiation, trapping it inside.\n"
        f"5. The trapped air also cannot circulate out by convection, raising the interior temperature.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_38_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "38_greenhouse_effect_trapping_thermal_radiation",
        "question_family_id": "38_greenhouse_effect_trapping_thermal_radiation",
        "hints": {
            "tier_1": "Can short-wavelength sunlight enter glass easily?",
            "tier_2": "Short waves enter; objects warm up and emit long infrared waves which cannot escape through glass easily.",
            "tier_3": "Short-wavelength solar radiation enters, but longer-wavelength infrared re-emitted inside is trapped by the glass."
        },
        "misconception_tags": ["greenhouse_generates_heat"]
    }


def arch_39_hot_drink_cooling_rate_investigation_variables(rng: random.Random) -> Dict[str, Any]:
    containers = [
        ("ceramic mug, a polystyrene foam cup, and a thin metal camping tin", "material / insulation of the cup", "temperature of hot water over time", "volume of water and starting temperature"),
        ("a wide shallow bowl versus a tall narrow thermos flask", "surface area of liquid exposed to air", "rate of cooling", "initial liquid volume and liquid type")
    ]
    setup, indep, dep, controlled = rng.choice(containers)
    prompt = (
        f"A student designs an investigation using **{setup}** to compare how quickly hot water cools.\n\n"
        f"Which identification of variables is scientifically correct?"
    )
    correct_opt = f"Independent variable: {indep} | Dependent variable: {dep} | Controlled variable: {controlled}"
    options = [
        correct_opt,
        f"Independent variable: {dep} | Dependent variable: {indep} | Controlled variable: {controlled}",
        f"Independent variable: {controlled} | Dependent variable: {dep} | Controlled variable: {indep}",
        "There are no variables needed because all cups cool at the identical speed regardless of material"
    ]
    rng.shuffle(options)
    sol = (
        f"**Investigative Variables Analysis:**\n"
        f"- **Independent variable (what the experimenter changes):** {indep}.\n"
        f"- **Dependent variable (what is measured as the response):** {dep}.\n"
        f"- **Controlled variables (kept constant for a fair test):** {controlled}.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_39_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "39_hot_drink_cooling_rate_investigation_variables",
        "question_family_id": "39_hot_drink_cooling_rate_investigation_variables",
        "hints": {
            "tier_1": "What is changed by the student, what is measured, and what is kept constant?",
            "tier_2": "Independent = changed; Dependent = measured; Controlled = kept identical.",
            "tier_3": f"Independent: {indep} | Dependent: {dep} | Controlled: {controlled}."
        },
        "misconception_tags": ["swapping_independent_and_dependent_variables"]
    }


def arch_40_reading_cooling_curve_temperature_versus_time(rng: random.Random) -> Dict[str, Any]:
    t0 = 80
    t5 = rng.choice([62, 64, 66])
    t10 = rng.choice([50, 52, 54])
    t15 = rng.choice([42, 44, 46])
    t20 = rng.choice([36, 38, 40])
    prompt = (
        f"A laboratory experiment records the cooling of $200\\text{{ cm}}^3$ of hot water over time in a room at $22^\\circ\\text{{C}}$:\n\n"
        f"| Time (minutes) | Temperature ($^\\circ\\text{{C}}$) |\n"
        f"|---|---|\n"
        f"| 0 | {t0} |\n"
        f"| 5 | {t5} |\n"
        f"| 10 | {t10} |\n"
        f"| 15 | {t15} |\n"
        f"| 20 | {t20} |\n\n"
        f"Why does the temperature drop more steeply in the first 5 minutes (${t0 - t5}^\\circ\\text{{C}}$ drop) than in the last 5 minutes (${t15 - t20}^\\circ\\text{{C}}$ drop)?"
    )
    correct_opt = "The rate of heat transfer is proportional to the temperature difference between the hot liquid and the room; when the water is much hotter, heat transfers out much faster."
    options = [
        correct_opt,
        "Water particles evaporate completely in the first 5 minutes and stop moving.",
        "The thermometer runs out of degrees Celsius as time progresses.",
        "Cold from the room only enters during the first few minutes and then stops."
    ]
    rng.shuffle(options)
    sol = (
        f"**Rate of Cooling Analysis:**\n"
        f"1. Heat loss rate depends directly on the temperature gradient (difference between object and surroundings).\n"
        f"2. At $t = 0\\text{{ min}}$, $T = {t0}^\\circ\\text{{C}}$ while room is $22^\\circ\\text{{C}}$: $\\Delta T = {t0 - 22}^\\circ\\text{{C}}$ (large difference -> rapid heat loss -> ${t0 - t5}^\\circ\\text{{C}}$ drop).\n"
        f"3. At $t = 15\\text{{ min}}$, $T = {t15}^\\circ\\text{{C}}$: $\\Delta T = {t15 - 22}^\\circ\\text{{C}}$ (small difference -> slow heat loss -> only ${t15 - t20}^\\circ\\text{{C}}$ drop).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_40_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "40_reading_cooling_curve_temperature_versus_time",
        "question_family_id": "40_reading_cooling_curve_temperature_versus_time",
        "hints": {
            "tier_1": "Is the temperature difference between water and room larger at the start or end?",
            "tier_2": "A larger temperature difference produces a faster rate of heat transfer.",
            "tier_3": "Heat transfers out faster when the temperature difference between the object and room is largest."
        },
        "misconception_tags": ["linear_cooling_fallacy"]
    }


def arch_41_calculating_temperature_drop_over_time(rng: random.Random) -> Dict[str, Any]:
    t_start = rng.choice([85, 90, 95])
    t_end = rng.choice([45, 50, 55])
    mins = rng.choice([10, 15, 20])
    delta_t = t_start - t_end
    rate = round(delta_t / mins, 1)
    rate_str = f"{rate}".replace(".", "{,}")
    prompt = (
        f"A beaker of hot tea cools from ${t_start}^\\circ\\text{{C}}$ to ${t_end}^\\circ\\text{{C}}$ over a period of ${mins}\\text{{ minutes}}$.\n\n"
        f"What is the average rate of temperature drop in degrees Celsius per minute ($^\\circ\\text{{C/min}}$)?"
    )
    correct_opt = f"{rate_str} °C/min"
    options = [
        correct_opt,
        f"{round((t_start + t_end) / mins, 1)}".replace(".", "{,}") + " °C/min",
        f"{delta_t}" + " °C/min",
        f"{round(mins / delta_t, 2)}".replace(".", "{,}") + " °C/min"
    ]
    options = list(dict.fromkeys(options))
    while len(options) < 4:
        options.append(f"{rng.randint(1, 6)}" + " °C/min")
    rng.shuffle(options)
    sol = (
        f"**Step 1: Calculate total temperature change ($\\Delta T$):**\n"
        f"$$\\Delta T = T_\\text{{initial}} - T_\\text{{final}} = {t_start}^\\circ\\text{{C}} - {t_end}^\\circ\\text{{C}} = {delta_t}^\\circ\\text{{C}}$$\n\n"
        f"**Step 2: Calculate average cooling rate per minute:**\n"
        f"$$\\text{{Rate}} = \\frac{{\\Delta T}}{{\\text{{time}}}} = \\frac{{{delta_t}^\\circ\\text{{C}}}}{{{mins}\\text{{ min}}}} = {rate_str}^\\circ\\text{{C/min}}$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_41_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "41_calculating_temperature_drop_over_time",
        "question_family_id": "41_calculating_temperature_drop_over_time",
        "hints": {
            "tier_1": "Divide total change in temperature by time in minutes.",
            "tier_2": f"Change in temperature = {t_start} - {t_end} = {delta_t} °C.",
            "tier_3": f"{delta_t} / {mins} = {rate_str} °C/min."
        },
        "misconception_tags": ["inverting_rate_ratio"]
    }


def arch_42_calculating_thermal_energy_transfer_rate_concept(rng: random.Random) -> Dict[str, Any]:
    joules = rng.choice([1200, 2400, 3600, 4800])
    seconds = rng.choice([30, 60, 120])
    watts = joules // seconds
    prompt = (
        f"A small electric heating element transfers ${joules}\\text{{ Joules}}$ of thermal energy into a cup of water over a duration of ${seconds}\\text{{ seconds}}$.\n\n"
        f"At what rate is energy being transferred in **Watts** (Joules per second)?"
    )
    correct_opt = f"{watts} W"
    options = [
        correct_opt,
        f"{joules * seconds} W",
        f"{joules + seconds} W",
        f"{seconds // (joules // 1000) if joules // 1000 else 1} W"
    ]
    options = list(dict.fromkeys(options))
    while len(options) < 4:
        options.append(f"{rng.randint(10, 150)} W")
    rng.shuffle(options)
    sol = (
        f"**Step 1: Formula for power / energy transfer rate:**\n"
        f"$$\\text{{Power (Watts)}} = \\frac{{\\text{{Energy (Joules)}}}}{{\\text{{Time (seconds)}}}}$$\n\n"
        f"**Step 2: Substitute values:**\n"
        f"$$\\text{{Power}} = \\frac{{{joules}\\text{{ J}}}}{{{seconds}\\text{{ s}}}} = {watts}\\text{{ W}}$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_42_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "42_calculating_thermal_energy_transfer_rate_concept",
        "question_family_id": "42_calculating_thermal_energy_transfer_rate_concept",
        "hints": {
            "tier_1": "Power in Watts equals Joules divided by seconds.",
            "tier_2": f"Divide {joules} by {seconds}.",
            "tier_3": f"{joules} / {seconds} = {watts} W."
        },
        "misconception_tags": ["multiplying_energy_by_time"]
    }


def arch_43_identifying_conduction_convection_radiation_in_daily_life(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("A spoon getting hot in hot tea", "Conduction", "Warm air rising above a heater", "Convection", "Feeling the warmth of the Sun on your face", "Radiation"),
        ("An egg frying in a cast iron pan", "Conduction", "Water boiling and tumbling in a pot", "Convection", "Bread browning under a glowing toaster filament", "Radiation")
    ]
    ex1, m1, ex2, m2, ex3, m3 = rng.choice(examples)
    prompt = (
        f"Consider these three everyday phenomena:\n"
        f"1. **{ex1}**\n"
        f"2. **{ex2}**\n"
        f"3. **{ex3}**\n\n"
        f"Which option correctly classifies the predominant heat transfer mechanism for 1, 2, and 3?"
    )
    correct_opt = f"1: {m1} | 2: {m2} | 3: {m3}"
    options = [
        correct_opt,
        f"1: {m2} | 2: {m3} | 3: {m1}",
        f"1: {m3} | 2: {m1} | 3: {m2}",
        f"1: {m1} | 2: {m1} | 3: {m1}"
    ]
    rng.shuffle(options)
    sol = (
        f"**Phenomenon Analysis:**\n"
        f"- 1. {ex1} involves particle collisions through a solid/liquid contact: **{m1}**.\n"
        f"- 2. {ex2} involves bulk movement of heated fluid due to density differences: **{m2}**.\n"
        f"- 3. {ex3} involves infrared electromagnetic radiation traveling without a medium: **{m3}**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_43_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "43_identifying_conduction_convection_radiation_in_daily_life",
        "question_family_id": "43_identifying_conduction_convection_radiation_in_daily_life",
        "hints": {
            "tier_1": "Recall: solids/contact = conduction, moving fluids = convection, waves = radiation.",
            "tier_2": f"1 is {m1}, 2 is {m2}, 3 is {m3}.",
            "tier_3": f"1: {m1} | 2: {m2} | 3: {m3}."
        },
        "misconception_tags": ["conflating_heat_mechanisms"]
    }


def arch_44_traditional_african_thatch_roof_thermal_properties(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In traditional African architecture across Southern Africa (such as rondavels), roofs made of dry grass thatch keep the interior cool during hot summer days and warm during cold winter nights.\n\n"
        f"What physical property of thatch explains this excellent thermal performance?"
    )
    correct_opt = "Thatch traps millions of microscopic pockets of still air between dry grass stalks; trapped air is a poor conductor of heat and prevents convection currents from developing."
    options = [
        correct_opt,
        "Dry grass stalks generate electricity that powers an invisible refrigeration field.",
        "Thatch is made of pure lead which reflects all atmospheric heat away.",
        "The grass absorbs cold during the day and sprays it into the room at night."
    ]
    rng.shuffle(options)
    sol = (
        f"**Thermal Performance of Thatch:**\n"
        f"1. Thatch consists of thousands of hollow dry grass stems bound tightly in layers.\n"
        f"2. Most of the volume consists of **trapped still air**.\n"
        f"3. Air is one of the poorest thermal conductors in nature ($k \\approx 0{{,}}026\\text{{ W/m·K}}$).\n"
        f"4. Because the air is partitioned into tiny compartments, convection currents cannot form.\n"
        f"5. Hence, external heat cannot easily conduct inwards during summer, and internal heat cannot escape during winter.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_44_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "44_traditional_african_thatch_roof_thermal_properties",
        "question_family_id": "44_traditional_african_thatch_roof_thermal_properties",
        "hints": {
            "tier_1": "What substance is trapped inside dry grass thatch?",
            "tier_2": "Trapped still air is an outstanding thermal insulator.",
            "tier_3": "Trapped pockets of still air prevent conduction and stop convection currents."
        },
        "misconception_tags": ["natural_materials_have_no_insulation_value"]
    }


def arch_45_misconception_cold_is_transferred_not_heat(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner says: *'When I open the refrigerator door, the coldness rushes out into the kitchen.'*\n\n"
        f"How should a natural science teacher correct this scientific misconception?"
    )
    correct_opt = "'Cold' is not a physical entity or form of energy; heat (thermal energy) from the warmer kitchen transfers into the colder refrigerator."
    options = [
        correct_opt,
        "The statement is fully correct because cold is a substance with negative mass.",
        "Cold air has positive charge and is drawn by electrostatic attraction to the kitchen tiles.",
        "Both cold and heat are substances that push against each other with equal force."
    ]
    rng.shuffle(options)
    sol = (
        f"**Scientific Clarification:**\n"
        f"- In physics, 'cold' is simply the **absence of thermal energy**.\n"
        f"- There is no such physical substance or energetic quantity as 'coldness'.\n"
        f"- Thermal energy always transfers from **higher temperature to lower temperature**.\n"
        f"- When the door opens, warm kitchen air transfers thermal energy into the cooler fridge air.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_45_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "45_misconception_cold_is_transferred_not_heat",
        "question_family_id": "45_misconception_cold_is_transferred_not_heat",
        "hints": {
            "tier_1": "Is cold a form of energy?",
            "tier_2": "Cold is the absence of heat. Only thermal energy flows.",
            "tier_3": "Cold is not a physical substance; heat flows from the kitchen into the fridge."
        },
        "misconception_tags": ["cold_is_an_entity_fallacy"]
    }


def arch_46_misconception_temperature_and_heat_are_identical(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A sparked match flame reaches approximately $800^\\circ\\text{{C}}$, while a large bath filled with warm water is at $40^\\circ\\text{{C}}$.\n\n"
        f"Which contains more total **thermal energy**, and what does this demonstrate about the difference between temperature and heat?"
    )
    correct_opt = "The bath of warm water contains vastly more thermal energy because thermal energy depends on both temperature and total mass of particles, even though the match flame has a higher temperature."
    options = [
        correct_opt,
        "The match flame contains far more thermal energy because its temperature is higher.",
        "Both contain the exact same amount of thermal energy because heat and temperature are identical.",
        "Neither contains thermal energy because heat only exists when water boils at 100 °C."
    ]
    rng.shuffle(options)
    sol = (
        f"**Heat vs Temperature Demonstration:**\n"
        f"1. **Temperature:** Measures the *average* kinetic energy per particle ($800^\\circ\\text{{C}}$ vs $40^\\circ\\text{{C}}$).\n"
        f"2. **Thermal Energy:** Represents the *total* internal kinetic energy of all particles combined.\n"
        f"3. A bath contains roughly $150\\text{{ kg}}$ of water ($10^{{27}}$ particles), whereas a match flame contains only milligrams of gas.\n"
        f"4. The cumulative energy of the bath water far exceeds the energy of the tiny match flame.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_46_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "46_misconception_temperature_and_heat_are_identical",
        "question_family_id": "46_misconception_temperature_and_heat_are_identical",
        "hints": {
            "tier_1": "Does total thermal energy depend on how much substance there is?",
            "tier_2": "Thermal energy is total particle energy; temperature is average particle energy.",
            "tier_3": "The bath contains more total thermal energy due to its much larger mass."
        },
        "misconception_tags": ["temperature_equals_total_thermal_energy"]
    }


def arch_47_misconception_sweaters_and_blankets_generate_heat(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A student places a thermometer wrapped tightly inside a thick woollen winter jersey on an empty wooden table at $18^\\circ\\text{{C}}$. "
        f"After two hours, the thermometer still reads exactly $18^\\circ\\text{{C}}$.\n\n"
        f"What scientific truth does this result prove about winter clothing?"
    )
    correct_opt = "Woollen jerseys do NOT generate or produce heat; they are thermal insulators that merely trap air and slow down the rate of heat loss from a warm human body."
    options = [
        correct_opt,
        "The thermometer is broken because wool creates heat through friction with table wood.",
        "The jersey only generates heat when the room temperature is below 0 °C.",
        "Table wood absorbs all heat created by the wool fibres before the thermometer can measure it."
    ]
    rng.shuffle(options)
    sol = (
        f"**Function of Winter Clothing:**\n"
        f"1. A jersey or blanket is not an active heat source (it has no battery, combustion, or metabolism).\n"
        f"2. When worn by a human, the human body is the heat source ($37^\\circ\\text{{C}}$).\n"
        f"3. The wool traps pockets of air, acting as a **thermal insulator** that retards conductive and convective heat dissipation to cold surroundings.\n"
        f"4. Without a heat source inside it, a sweater will stay at room temperature ($18^\\circ\\text{{C}}$).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_47_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "47_misconception_sweaters_and_blankets_generate_heat",
        "question_family_id": "47_misconception_sweaters_and_blankets_generate_heat",
        "hints": {
            "tier_1": "Can a woollen jersey produce its own heat without a living body inside?",
            "tier_2": "Clothing insulates; it does not produce heat.",
            "tier_3": "Jerseys do not produce heat; they insulate and trap body heat."
        },
        "misconception_tags": ["clothing_creates_heat"]
    }


def arch_48_misconception_radiation_only_occurs_from_nuclear_sources(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner claims: *'Radiation only comes from nuclear power plants and radioactive uranium; ordinary warm objects do not radiate.'*\n\n"
        f"Which statement correctly refutes this misconception using thermal physics principles?"
    )
    correct_opt = "Every object with a temperature above absolute zero (-273,15 °C) continuously emits thermal radiation in the form of electromagnetic (infrared) waves."
    options = [
        correct_opt,
        "Only objects made of pure iron can radiate heat waves.",
        "Radiation only exists when something is on fire with visible yellow flames.",
        "Thermal radiation can only travel through dense liquid water."
    ]
    rng.shuffle(options)
    sol = (
        f"**Thermal Radiation Omnipresence:**\n"
        f"- In science, 'radiation' refers to any energy emitted as electromagnetic waves.\n"
        f"- While high-energy ionizing radiation comes from radioactive decay, **thermal radiation** (infrared) is emitted by **all matter** above absolute zero ($-273{{,}}15^\\circ\\text{{C}}$ or $0\\text{{ K}}$).\n"
        f"- A cup of tea, an ice cube, a human body, and a desk all continuously emit and absorb infrared radiation.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_48_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "48_misconception_radiation_only_occurs_from_nuclear_sources",
        "question_family_id": "48_misconception_radiation_only_occurs_from_nuclear_sources",
        "hints": {
            "tier_1": "Do everyday warm objects emit infrared radiation?",
            "tier_2": "All matter above absolute zero emits thermal radiation.",
            "tier_3": "Every object above absolute zero continuously emits infrared radiation."
        },
        "misconception_tags": ["radiation_only_nuclear"]
    }


def arch_49_improving_thermal_efficiency_of_home_appliance(rng: random.Random) -> Dict[str, Any]:
    appliances = [
        ("an electric hot water geyser", "fitting a specialised geyser insulation blanket and insulating hot water copper pipes", "conduction and radiation heat losses to roof space"),
        ("an electric baking oven", "installing multi-layer double-glazed oven door glass with airtight silicone seals", "convective air leaks and conductive heat loss through the door"),
        ("a home refrigerator", "checking and replacing worn flexible magnetic door gaskets", "warm room air entering by convection and conduction")
    ]
    app, mod, loss = rng.choice(appliances)
    prompt = (
        f"A homeowner seeks to reduce household electricity costs by improving the thermal efficiency of **{app}**.\n\n"
        f"Which practical engineering intervention and heat transfer rationale achieves this goal?"
    )
    correct_opt = f"By {mod}, thereby minimizing unwanted {loss}."
    options = [
        correct_opt,
        "By painting the entire appliance bright neon yellow to convert heat into visible light.",
        "By drilling ventilation holes in the sides so hot air can escape continuously.",
        "By replacing all metal parts with copper to maximize thermal dissipation."
    ]
    rng.shuffle(options)
    sol = (
        f"**Energy Efficiency Rationale:**\n"
        f"- For {app}, substantial electrical energy is wasted through {loss}.\n"
        f"- Implementing '{mod}' directly addresses this mechanism, slowing down heat transfer and retaining desired temperatures with lower electrical consumption.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_49_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "49_improving_thermal_efficiency_of_home_appliance",
        "question_family_id": "49_improving_thermal_efficiency_of_home_appliance",
        "hints": {
            "tier_1": "How do you minimize heat loss from thermal appliances?",
            "tier_2": "Insulation blankets and tight seals stop unwanted heat transfer.",
            "tier_3": f"By {mod}, minimizing unwanted {loss}."
        },
        "misconception_tags": ["insulation_not_cost_effective"]
    }


def arch_50_heat_energy_transfer_comprehensive_diagnostic(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A comprehensive examination question asks learners to analyze heat transfer across three distinct scenarios:\n"
        f"Case 1: A metal spoon left in boiling soup quickly burns your fingers.\n"
        f"Case 2: A hot air balloon ascends into the morning sky when the propane burner is fired.\n"
        f"Case 3: Solar energy warms the surface of rocks on Mars across the cold vacuum of space.\n\n"
        f"Which unified sequence correctly categorizes Case 1, Case 2, and Case 3?"
    )
    correct_opt = "Case 1: Conduction | Case 2: Convection | Case 3: Radiation"
    options = [
        correct_opt,
        "Case 1: Radiation | Case 2: Conduction | Case 3: Convection",
        "Case 1: Convection | Case 2: Radiation | Case 3: Conduction",
        "Case 1: Conduction | Case 2: Radiation | Case 3: Convection"
    ]
    rng.shuffle(options)
    sol = (
        f"**Unified Diagnostic Synthesis:**\n"
        f"- **Case 1 (Spoon in soup):** Particle-to-particle kinetic collisions through solid metal = **Conduction**.\n"
        f"- **Case 2 (Hot air balloon):** Heated air expands, decreases in density, and rises by buoyancy = **Convection**.\n"
        f"- **Case 3 (Solar energy to Mars):** Electromagnetic infrared waves travelling through the vacuum of space = **Radiation**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ht_50_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "50_heat_energy_transfer_comprehensive_diagnostic",
        "question_family_id": "50_heat_energy_transfer_comprehensive_diagnostic",
        "hints": {
            "tier_1": "Match each case to one of the 3 heat transfer modes.",
            "tier_2": "Case 1 is solid conduction; Case 2 is fluid convection; Case 3 is vacuum radiation.",
            "tier_3": "Case 1: Conduction | Case 2: Convection | Case 3: Radiation."
        },
        "misconception_tags": ["diagnostic_synthesis_error"]
    }
