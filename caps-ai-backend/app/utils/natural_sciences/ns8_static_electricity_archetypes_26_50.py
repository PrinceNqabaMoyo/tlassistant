"""Grade 8 Natural Sciences: Term 3 - Static Electricity Archetypes (26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/01. Static electricity.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List


def arch_26_charge_separation_in_thunderclouds(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"During massive summer thunderstorms across the South African Highveld (e.g. Gauteng, Mpumalanga), huge cumulonimbus thunderclouds become intensely electrified.\n\n"
        f"How does charge separation occur inside a towering storm cloud?"
    )
    correct_opt = "Violent updrafts and downdrafts cause collisions between rising ice crystals and falling graupel (soft hail); friction strips electrons, leaving lighter ice crystals positive at the cloud top and heavier graupel negative at the cloud base."
    options = [
        correct_opt,
        "The cloud absorbs static electricity emitted by ground radio towers.",
        "Protons evaporate from the ocean and float exclusively into the upper atmosphere.",
        "Lightning bolts travel from the Moon into the cloud to deposit electrical charge."
    ]
    rng.shuffle(options)
    sol = (
        f"**Thundercloud Electrification Mechanism:**\n"
        f"1. Violent convection currents circulate moisture and ice within the thundercloud.\n"
        f"2. Collisions between rising ice crystals and descending hail/graupel cause triboelectric electron transfer.\n"
        f"3. Lighter ice crystals lose electrons and carry positive charge to the top of the cloud ($+10\\text{{ km}}$).\n"
        f"4. Heavier hail gains electrons and accumulates a massive negative charge region at the base of the cloud ($2-4\\text{{ km}}$).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_26_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "26_charge_separation_in_thunderclouds",
        "question_family_id": "26_charge_separation_in_thunderclouds",
        "hints": {
            "tier_1": "What collides inside a storm cloud to create friction?",
            "tier_2": "Ice crystals and hail collide; positive at the top, negative at the base.",
            "tier_3": "Collisions between rising ice crystals and falling hail separate charges by friction."
        },
        "misconception_tags": ["clouds_charge_by_magnetism"]
    }


def arch_27_lightning_as_giant_electrostatic_discharge(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A cloud-to-ground lightning strike is a dramatic natural spectacle. "
        f"What is the physical nature of a lightning bolt in terms of electrostatics?"
    )
    correct_opt = "A gigantic electrostatic discharge spark: millions of volts overcome the insulating resistance of air, allowing billions of electrons to surge between the cloud and the Earth to neutralize charge."
    options = [
        correct_opt,
        "A stream of pure liquid fire falling from the upper atmosphere to the ground.",
        "A beam of radioactive gamma rays emitted by exploding nitrogen atoms.",
        "A permanent electric cord that connects the sky to municipal power generators."
    ]
    rng.shuffle(options)
    sol = (
        f"**Physical Nature of Lightning:**\n"
        f"1. The negative cloud base induces a massive positive charge on the ground surface below.\n"
        f"2. A gigantic electric potential difference (tens of millions of volts) builds up.\n"
        f"3. When the electric field exceeds the dielectric breakdown strength of air (~$3 \\times 10^6\\text{{ V/m}}$), air molecules are ionized into conductive plasma.\n"
        f"4. Electrons surge down in a stepped leader, meeting an upward streamer, resulting in a colossal electrostatic discharge spark: **lightning**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_27_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "27_lightning_as_giant_electrostatic_discharge",
        "question_family_id": "27_lightning_as_giant_electrostatic_discharge",
        "hints": {
            "tier_1": "What is lightning in terms of electric charge?",
            "tier_2": "It is a massive electrostatic discharge spark neutralizing high potential.",
            "tier_3": "A gigantic electrostatic discharge spark between cloud and Earth."
        },
        "misconception_tags": ["lightning_is_actual_fire"]
    }


def arch_28_thunder_as_acoustic_shockwave_of_heated_air(rng: random.Random) -> Dict[str, Any]:
    temp = rng.choice([25000, 30000, 33000])
    prompt = (
        f"During a lightning flash, the electrical discharge heats the narrow air channel to approximately {temp} °C (hotter than the surface of the Sun) in a fraction of a millisecond.\n\n"
        f"What causes the loud booming sound of **thunder** that follows the flash?"
    )
    correct_opt = "The superheated air expands violently and explosively, creating an acoustic shockwave that travels outward through the atmosphere as sound."
    options = [
        correct_opt,
        "Two solid clouds colliding with each other like massive rocks.",
        "Raindrops exploding into gas when striking the ground at supersonic speed.",
        "The sound of electrons crashing into protons and destroying them."
    ]
    rng.shuffle(options)
    sol = (
        f"**Genesis of Thunder:**\n"
        f"- The lightning plasma channel heats the air almost instantaneously to $\\approx {temp}^\\circ\\text{{C}}$.\n"
        f"- The intense heat causes rapid, violent thermal expansion of the air column.\n"
        f"- This explosive expansion generates a cylindrical acoustic shockwave that radiates outward at the speed of sound ($\\approx 340\\text{{ m/s}}$).\n"
        f"- We perceive this acoustic shockwave as **thunder**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_28_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "28_thunder_as_acoustic_shockwave_of_heated_air",
        "question_family_id": "28_thunder_as_acoustic_shockwave_of_heated_air",
        "hints": {
            "tier_1": "What happens when air is heated violently and expands in microseconds?",
            "tier_2": "Rapid explosive expansion of superheated air creates an acoustic shockwave.",
            "tier_3": "Superheated air expands explosively, creating an acoustic shockwave known as thunder."
        },
        "misconception_tags": ["clouds_colliding_create_thunder"]
    }


def arch_29_function_and_design_of_lightning_conductor_rods(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Tall buildings, thatched rondavels, and church steeples in South Africa are fitted with pointed metal **lightning conductors** (Franklin rods) mounted at the highest point and connected to a thick copper strip leading deep into moist soil.\n\n"
        f"How does a lightning conductor protect a building from fire and destruction?"
    )
    correct_opt = "It provides a low-resistance path that safely conducts the massive discharge current directly into the Earth, bypassing the building's combustible structure."
    options = [
        correct_opt,
        "It repels thunderclouds into outer space using electrostatic magnetic force.",
        "It turns lightning into household 12-volt DC electricity to power the lights.",
        "It absorbs all rain and moisture from the storm so lightning cannot ignite."
    ]
    rng.shuffle(options)
    sol = (
        f"**Function of Lightning Conductors:**\n"
        f"1. **Safe conduction path:** If a strike occurs, the pointed metal rod intercepts the strike.\n"
        f"2. The heavy copper conductor ($R \\approx 0$) provides a dedicated path of least resistance directly to ground electrodes.\n"
        f"3. The colossal current ($\\\\sim 30\\,000\\text{{ A}}$) flows safely into the Earth without dissipating dangerous heat or igniting thatch or brickwork.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_29_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "29_function_and_design_of_lightning_conductor_rods",
        "question_family_id": "29_function_and_design_of_lightning_conductor_rods",
        "hints": {
            "tier_1": "Does the rod prevent lightning, or guide it safely into the ground?",
            "tier_2": "It provides a low-resistance path to direct lightning safely into the Earth.",
            "tier_3": "Provides a low-resistance path conducting the discharge safely into the Earth."
        },
        "misconception_tags": ["lightning_rods_prevent_lightning_from_occurring"]
    }


def arch_30_lightning_safety_precautions_outdoors(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"You are caught in an open soccer field when a severe thunderstorm suddenly breaks overhead. "
        f"Which outdoor action represents the **safest** immediate response according to lightning safety science?"
    )
    correct_opt = "Crouch down low on the balls of your feet with feet pressed together, head tucked down, and never shelter under a tall isolated tree."
    options = [
        correct_opt,
        "Run under the tallest solitary oak tree on the field to stay completely dry.",
        "Lie completely flat on your stomach with arms and legs spread wide on the wet grass.",
        "Hold a metal golf club or metal umbrella pointed straight up toward the cloud."
    ]
    rng.shuffle(options)
    sol = (
        f"**Outdoor Lightning Safety Rules:**\n"
        f"1. **Never shelter under tall isolated trees:** Lightning strikes the highest pointed object. Ground currents and side flashes jump from the trunk to nearby people.\n"
        f"2. **Do not lie flat:** Ground currents spread radially through wet soil. Lying flat creates a large voltage difference across your body.\n"
        f"3. **Lightning crouch:** Crouch low (minimize height) on the balls of your feet touching together (minimize contact area and ground potential difference).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_30_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "30_lightning_safety_precautions_outdoors",
        "question_family_id": "30_lightning_safety_precautions_outdoors",
        "hints": {
            "tier_1": "Should you stand under a tall solitary tree in a storm?",
            "tier_2": "Never under a tall tree. Crouch low on the balls of your feet together.",
            "tier_3": "Crouch low on the balls of your feet with feet together; avoid tall isolated trees."
        },
        "misconception_tags": ["sheltering_under_tall_trees_is_safe"]
    }


def arch_31_lightning_safety_precautions_indoors(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Even inside a standard house during an intense thunderstorm, certain activities pose serious electrocution risks from lightning.\n\n"
        f"Which indoor activity should be strictly avoided during a severe electrical storm?"
    )
    correct_opt = "Taking a bath or shower, washing dishes, and using corded landline telephones, because lightning can conduct along metal plumbing pipes and electrical wiring."
    options = [
        correct_opt,
        "Reading a printed paper book while sitting on a wooden sofa.",
        "Wearing rubber-soled slippers on a carpeted floor.",
        "Sleeping in a bed placed in the centre of an enclosed room."
    ]
    rng.shuffle(options)
    sol = (
        f"**Indoor Lightning Hazards:**\n"
        f"- Metal plumbing pipes and copper electrical/telephone wires act as prime conductors for lightning strikes hitting a house or nearby ground.\n"
        f"- Water containing dissolved minerals is an electrical conductor.\n"
        f"- Showering or touching metal taps during a storm can transmit lethal surge currents.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_31_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "31_lightning_safety_precautions_indoors",
        "question_family_id": "31_lightning_safety_precautions_indoors",
        "hints": {
            "tier_1": "What can conduct lightning currents into a home?",
            "tier_2": "Plumbing pipes and corded wires conduct surge currents.",
            "tier_3": "Avoid baths/showers and corded phones as plumbing/wiring can conduct lightning."
        },
        "misconception_tags": ["indoors_is_100_percent_safe_doing_anything"]
    }


def arch_32_faraday_cage_effect_safety_inside_metal_car(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"If lightning strikes a modern motor car on a highway, the occupants inside are virtually always unharmed.\n\n"
        f"What is the actual scientific reason why people inside a metal car are protected from a lightning strike?"
    )
    correct_opt = "The car's enclosed steel body acts as a Faraday cage: electrostatic charges travel exclusively along the outer metal skin and discharge to the road, leaving zero electric field inside."
    options = [
        correct_opt,
        "Rubber tyres act as absolute insulators that completely prevent lightning from touching the car.",
        "The car battery absorbs all billions of Joules of lightning energy instantly.",
        "Automotive glass windows reflect all electrical currents into the atmosphere."
    ]
    rng.shuffle(options)
    sol = (
        f"**Faraday Cage Protection in Vehicles:**\n"
        f"1. **Common misconception debunked:** Rubber tyres do NOT protect the car; lightning has already jumped through kilometres of insulating air and jumps easily over rubber tyres.\n"
        f"2. **Scientific truth:** The continuous metal frame and body of the vehicle form a **Faraday cage**.\n"
        f"3. Electrical charge flows around the outer surface of the metal skin and arcs to the road surface, leaving the interior cavity completely free of electric fields.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_32_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "32_faraday_cage_effect_safety_inside_metal_car",
        "question_family_id": "32_faraday_cage_effect_safety_inside_metal_car",
        "hints": {
            "tier_1": "Is it the rubber tyres or the metal body that protects you?",
            "tier_2": "It is the metal body acting as a Faraday cage, NOT rubber tyres.",
            "tier_3": "The metal body acts as a Faraday cage, keeping charge on the exterior."
        },
        "misconception_tags": ["rubber_tyres_protect_car_from_lightning"]
    }


def arch_33_electrostatic_precipitators_in_smokestacks(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In coal-fired power stations (like Eskom stations in Mpumalanga) and cement factories, **electrostatic precipitators** are installed in giant industrial chimneys.\n\n"
        f"How do electrostatic precipitators remove up to 99% of fine soot and fly ash particles from smoke?"
    )
    correct_opt = "Smoke passes highly charged metal wires that give ash particles a strong negative charge; the particles are then attracted to and trapped on positively charged collecting plates."
    options = [
        correct_opt,
        "Giant magnets suck carbon atoms out of the hot exhaust gases.",
        "Chemical sprayers douse the smoke with liquid nitrogen to freeze soot into ice.",
        "Radioactive lasers burn all ash particles into non-existent matter."
    ]
    rng.shuffle(options)
    sol = (
        f"**Operation of Electrostatic Precipitators:**\n"
        f"1. Dirty flue gas passes high-voltage wire electrodes (negatively charged at ~$50\\,000\\text{{ V}}$).\n"
        f"2. A corona discharge ionizes the gas, transferring negative electrons onto passing ash and dust particles.\n"
        f"3. The negatively charged particles enter an electric field between grounded/positively charged collecting plates.\n"
        f"4. **Unlike charges attract**: the ash particles are pulled onto the positive plates where they stick.\n"
        f"5. The plates are periodically hammered (rapped) so clean dust falls into hoppers for disposal.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_33_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "33_electrostatic_precipitators_in_smokestacks",
        "question_family_id": "33_electrostatic_precipitators_in_smokestacks",
        "hints": {
            "tier_1": "How are particles charged and attracted to plates?",
            "tier_2": "Wires charge the particles negatively, positive plates attract and collect them.",
            "tier_3": "Wires give particles a negative charge, which are attracted to positive collecting plates."
        },
        "misconception_tags": ["precipitators_are_mechanical_sieves"]
    }


def arch_34_electrostatic_spray_painting_efficiency(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Car manufacturing plants use **electrostatic spray painting** to coat automobile metal bodies with paint.\n\n"
        f"Why is electrostatic spray painting vastly superior to ordinary pneumatic spray painting?"
    )
    correct_opt = "Paint droplets are given a positive charge as they leave the nozzle while the car body is earthed/negative; electrostatic attraction pulls paint uniformly onto all curves and corners with near-zero overspray waste."
    options = [
        correct_opt,
        "The electrostatic charge changes the colour of the paint automatically into metallic chrome.",
        "Electrostatic paint dries at 0 Kelvin without needing baking ovens.",
        "The car body becomes liquid during spraying so the paint absorbs into the steel."
    ]
    rng.shuffle(options)
    sol = (
        f"**Electrostatic Spray Painting Physics:**\n"
        f"1. Fine paint mist passes through an electrode that imparts a uniform positive charge to all droplets.\n"
        f"2. Because like charges repel, the droplets repel each other, producing a fine, uniform cloud without clumping.\n"
        f"3. The car body is grounded with an opposite (negative) potential.\n"
        f"4. **Opposites attract**: Electric field lines wrap around the car body, pulling paint droplets even onto the backs of curved edges ('wrap-around effect').\n"
        f"5. Overspray waste is reduced from 40% down to less than 5%.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_34_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "34_electrostatic_spray_painting_efficiency",
        "question_family_id": "34_electrostatic_spray_painting_efficiency",
        "hints": {
            "tier_1": "What happens when paint droplets and car body have opposite charges?",
            "tier_2": "Opposite charges attract, pulling paint evenly with minimal waste.",
            "tier_3": "Charged paint is attracted to the oppositely charged car body, eliminating waste."
        },
        "misconception_tags": ["electrostatic_painting_is_magnetic"]
    }


def arch_35_photocopier_laser_printer_toner_attraction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Modern office photocopiers and laser printers rely on **xerography**, a technology based on electrostatic charges and light-sensitive materials.\n\n"
        f"How does an electrostatic charge help transfer black toner powder onto paper in a photocopier?"
    )
    correct_opt = "A rotating drum is given a static charge that is erased by light where paper is white; oppositely charged black toner particles cling to the remaining charged regions and are transferred onto paper."
    options = [
        correct_opt,
        "Toner powder is mixed with boiling glue that sprays across the paper under high air pressure.",
        "The drum magnetises the paper fibres so that ink particles melt into liquid.",
        "Static electricity cuts tiny physical holes into the paper in the shape of letters."
    ]
    rng.shuffle(options)
    sol = (
        f"**Xerographic Process (Photocopier / Laser Printer):**\n"
        f"1. A photoconductive drum is uniformly charged with static electricity in the dark.\n"
        f"2. Light reflects from the original document onto the drum (or laser writes image). Where light hits, charge drains away.\n"
        f"3. A static latent image remains where dark letters exist.\n"
        f"4. Oppositely charged black toner powder is dusted over the drum, clinging only to the charged letters.\n"
        f"5. Paper given an even stronger charge pulls toner off the drum, which is then heat-fused.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_35_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "35_photocopier_laser_printer_toner_attraction",
        "question_family_id": "35_photocopier_laser_printer_toner_attraction",
        "hints": {
            "tier_1": "What holds the toner powder in the shape of letters on the drum?",
            "tier_2": "Opposite static electrical charges attract toner to the charged areas.",
            "tier_3": "Oppositely charged toner particles cling to the charged image on the drum."
        },
        "misconception_tags": ["photocopiers_use_chemical_printing_presses"]
    }


def arch_36_fuel_tanker_earthing_grounding_safety(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When a large road tanker delivers petrol to a filling station in South Africa, regulations require the driver to attach a heavy-duty copper **grounding cable** between the tanker and the depot earth stake BEFORE attaching the fuel hose.\n\n"
        f"What catastrophe is prevented by earthing the petrol tanker prior to fuel transfer?"
    )
    correct_opt = "Friction of flowing petrol and air turbulence generates static electricity; an ungrounded tanker could produce a static spark that would ignite explosive fuel vapours."
    options = [
        correct_opt,
        "Earthing prevents the petrol from turning into diesel fuel during pumping.",
        "Earthing stops the heavy tanker truck from floating away into the sky.",
        "The copper cable is used to charge the tanker's headlights using ground current."
    ]
    rng.shuffle(options)
    sol = (
        f"**Static Hazard in Fuel Delivery:**\n"
        f"1. Liquid fuels (petrol, aviation kerosene) are poor electrical conductors.\n"
        f"2. Pumping fuel through pipes generates massive static charge via internal fluid friction.\n"
        f"3. Without an earth cable, dangerous potentials ($>20\\,000\\text{{ V}}$) accumulate on the metal tank.\n"
        f"4. A spark jumping between the nozzle and tank would immediately ignite volatile petrol-air vapours, causing a catastrophic explosion.\n"
        f"5. Grounding bleeds off electrons continuously, preventing spark formation.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_36_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "36_fuel_tanker_earthing_grounding_safety",
        "question_family_id": "36_fuel_tanker_earthing_grounding_safety",
        "hints": {
            "tier_1": "What can static sparks do to petrol vapours?",
            "tier_2": "A static spark can ignite fuel vapours and cause an explosion.",
            "tier_3": "Friction creates static charge; earthing prevents sparks from igniting explosive vapours."
        },
        "misconception_tags": ["fuels_do_not_generate_static"]
    }


def arch_37_aircraft_refuelling_static_bonding_clamp(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"During aircraft refuelling at OR Tambo International Airport, a ground technician connects a bonding wire between the fuel truck and the aircraft wing before inserting the fuel nozzle.\n\n"
        f"Why do aeroplanes carry massive electrostatic charges upon landing?"
    )
    correct_opt = "High-speed friction between the aircraft's metallic skin and atmospheric air, ice crystals, and dust particles during flight transfers electrons, building up huge static potentials."
    options = [
        correct_opt,
        "Aeroplane jet engines burn nuclear fuel that releases positive electricity.",
        "Aeroplanes fly close to the Moon where cosmic batteries recharge the aluminium fuselage.",
        "Radio communication antennas absorb high-voltage DC current from satellites."
    ]
    rng.shuffle(options)
    sol = (
        f"**Aviation Electrostatic Charging:**\n"
        f"- An aircraft cruising at $800-900\\text{{ km/h}}$ experiences continuous high-speed friction with air molecules, aerosols, and ice crystals.\n"
        f"- This triboelectric effect charges the aircraft fuselage to thousands of volts.\n"
        f"- Rubber landing gear tyres insulate the aircraft upon landing.\n"
        f"- Bonding wires equalize potential between fuel truck and plane, avoiding catastrophic sparks during refuelling.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_37_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "37_aircraft_refuelling_static_bonding_clamp",
        "question_family_id": "37_aircraft_refuelling_static_bonding_clamp",
        "hints": {
            "tier_1": "How does an airplane flying at 800 km/h get charged?",
            "tier_2": "Friction between the metal skin and air/ice particles charges the plane.",
            "tier_3": "High-speed friction between the plane's skin and air/ice separates static charge."
        },
        "misconception_tags": ["planes_do_not_carry_static"]
    }


def arch_38_anti_static_wrist_straps_in_electronics_repair(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Computer technicians repairing motherboards and installing RAM chips wear an **electrostatic discharge (ESD) wrist strap** connected by a coiled wire to an earthed metal point.\n\n"
        f"Why is this anti-static wrist strap essential when handling sensitive microelectronic chips?"
    )
    correct_opt = "Microchip circuits have microscopic transistors that can be destroyed by tiny static discharges (even below 100 V) that are imperceptible to human touch."
    options = [
        correct_opt,
        "The wrist strap prevents the technician from being struck by indoor lightning bolts.",
        "The strap acts as a magnetic brace that prevents the technician's hand from trembling.",
        "Computer chips are radioactive and the wrist strap absorbs gamma radiation."
    ]
    rng.shuffle(options)
    sol = (
        f"**ESD Protection in Electronics:**\n"
        f"1. Humans rarely feel an electrostatic shock below $\\approx 3000\\text{{ V}}$.\n"
        f"2. Modern semiconductor chips (CPUs, RAM) operate at $1{{,}}2\\text{{ V}}$ with gate oxide barriers only nanometres thick.\n"
        f"3. A static discharge of just $50-100\\text{{ V}}$ will punch holes through transistor gates, permanently ruining the component.\n"
        f"4. The wrist strap constantly drains static charge safely to ground through a $1\\text{{ M}}\\Omega$ safety resistor.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_38_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "38_anti_static_wrist_straps_in_electronics_repair",
        "question_family_id": "38_anti_static_wrist_straps_in_electronics_repair",
        "hints": {
            "tier_1": "Can static sparks damage computer microchips?",
            "tier_2": "Microchips are destroyed by tiny static voltages humans cannot even feel.",
            "tier_3": "Microscopic transistors are destroyed by tiny static discharges below 100 V."
        },
        "misconception_tags": ["chips_require_thousands_of_volts_to_damage"]
    }


def arch_39_static_cling_in_clothes_dryers(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When removing laundry from a tumble dryer, synthetic garments often crackle and cling stubbornly to each other or to your body ('static cling').\n\n"
        f"What causes static cling in a tumble dryer, and how do dryer sheets prevent it?"
    )
    correct_opt = "Tumbling clothes rub together in dry hot air, transferring electrons and creating opposite charges that attract; dryer sheets deposit a thin conductive coating that dissipates static charge."
    options = [
        correct_opt,
        "Dryer heat melts synthetic fabrics so they chemically fuse together.",
        "Clothes dryers generate magnetic fields that align fabric iron atoms.",
        "Water in the clothes becomes radioactive from heating."
    ]
    rng.shuffle(options)
    sol = (
        f"**Static Cling in Tumble Dryers:**\n"
        f"1. As garments tumble, constant friction in warm dry air separates electrons between different materials (polyester, nylon, cotton).\n"
        f"2. Oppositely charged garments attract each other strongly (**static cling**).\n"
        f"3. Anti-static dryer sheets release positively charged lubricants that coat fibres, neutralizing surface charges and allowing charges to bleed off.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_39_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "39_static_cling_in_clothes_dryers",
        "question_family_id": "39_static_cling_in_clothes_dryers",
        "hints": {
            "tier_1": "What happens when synthetic clothes tumble together in dry air?",
            "tier_2": "Friction separates electrons, creating opposite charges that cling.",
            "tier_3": "Friction transfers electrons creating opposite charges; dryer sheets dissipate charge."
        },
        "misconception_tags": ["dryers_melt_fibres"]
    }


def arch_40_triboelectric_series_ranking_charge_tendency(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A reference **triboelectric series** lists materials in order of their tendency to lose or gain electrons when rubbed:\n\n"
        f"*(More likely to LOSE electrons / become positive)*\n"
        f"1. Dry human hair\n"
        f"2. Glass\n"
        f"3. Wool\n"
        f"4. Silk\n"
        f"5. Polythene plastic\n"
        f"*(More likely to GAIN electrons / become negative)*\n\n"
        f"If a glass rod is rubbed with a woollen cloth, what will be their resulting charges according to this series?"
    )
    correct_opt = "Glass loses electrons and becomes positively charged; wool gains electrons and becomes negatively charged."
    options = [
        correct_opt,
        "Glass gains electrons and becomes negatively charged; wool becomes positively charged.",
        "Both glass and wool become positively charged simultaneously.",
        "Neither material acquires any charge because both are insulators."
    ]
    rng.shuffle(options)
    sol = (
        f"**Interpreting the Triboelectric Series:**\n"
        f"- In the given ranking, Glass is higher (Item 2) than Wool (Item 3).\n"
        f"- The higher material in the series has a greater tendency to **lose electrons** and become **positive**.\n"
        f"- The lower material (Wool) has a greater affinity to **gain electrons** and become **negative**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_40_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "40_triboelectric_series_ranking_charge_tendency",
        "question_family_id": "40_triboelectric_series_ranking_charge_tendency",
        "hints": {
            "tier_1": "Which is higher on the list: glass or wool?",
            "tier_2": "Glass is higher (loses electrons -> positive); wool is lower (gains -> negative).",
            "tier_3": "Glass loses electrons (becomes positive); wool gains electrons (becomes negative)."
        },
        "misconception_tags": ["inverting_triboelectric_series"]
    }


def arch_41_calculating_net_charge_from_protons_and_electrons(rng: random.Random) -> Dict[str, Any]:
    n_p = rng.choice([50, 100, 250, 500])
    n_e = rng.choice([20, 40, 80, 120])
    while n_p == n_e:
        n_e += 10
    net = n_p - n_e
    sign = "+" if net > 0 else "-"
    type_str = "positive" if net > 0 else "negative"
    prompt = (
        f"A microscopic dust particle suspended in air contains ${n_p}$ positive protons and ${n_e}$ negative electrons.\n\n"
        f"What is the total elementary charge and electrical nature of the particle?"
    )
    correct_opt = f"Net charge of {sign}{abs(net)} (elementary charges); the particle is {type_str}."
    options = [
        correct_opt,
        f"Net charge of {n_p + n_e} (elementary charges); the particle is neutral.",
        f"Net charge of 0; particles always balance automatically.",
        f"Net charge of -{abs(net)} (elementary charges); the particle is {'negative' if net > 0 else 'positive'}."
    ]
    options = list(dict.fromkeys(options))
    while len(options) < 4:
        options.append(f"Net charge of +{rng.randint(10, 300)}")
    rng.shuffle(options)
    sol = (
        f"**Net Elementary Charge Calculation:**\n"
        f"$$\\text{{Total charge}} = (+{n_p}) + (-{n_e}) = {sign}{abs(net)}\\text{{ e}}\n$$\n"
        f"Because protons ({n_p}) {'exceed' if net > 0 else 'are less than'} electrons ({n_e}), the particle carries a **{type_str}** net charge of **{sign}{abs(net)}**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_41_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "41_calculating_net_charge_from_protons_and_electrons",
        "question_family_id": "41_calculating_net_charge_from_protons_and_electrons",
        "hints": {
            "tier_1": "Subtract the number of electrons from the number of protons.",
            "tier_2": f"Protons = {n_p}, Electrons = {n_e}. Net = {n_p} - {n_e} = {net}.",
            "tier_3": f"Net charge of {sign}{abs(net)} ({type_str})."
        },
        "misconception_tags": ["adding_charges_without_signs"]
    }


def arch_42_predicting_interaction_between_multiple_charged_spheres(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Three small light spheres (Sphere A, Sphere B, Sphere C) are suspended by insulating nylon threads:\n"
        f"- Sphere A is known to be **positively charged**.\n"
        f"- Sphere A repels Sphere B.\n"
        f"- Sphere B attracts Sphere C.\n\n"
        f"What are the definite or possible electrical states of Sphere B and Sphere C?"
    )
    correct_opt = "Sphere B is positively charged; Sphere C is either negatively charged or electrically neutral."
    options = [
        correct_opt,
        "Sphere B is negatively charged; Sphere C is positively charged.",
        "Sphere B is neutral; Sphere C is positively charged.",
        "All three spheres must be completely neutral."
    ]
    rng.shuffle(options)
    sol = (
        f"**Electrostatic Logic Deduction:**\n"
        f"1. **Sphere A repels Sphere B:** Only like charges repel! Since Sphere A is positive, Sphere B **must be positively charged**.\n"
        f"2. **Sphere B attracts Sphere C:** Attraction can occur between unlike charges (negative) OR between a charged object and a **neutral** object (by induction).\n"
        f"3. Therefore, Sphere C is **either negatively charged or neutral**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_42_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "42_predicting_interaction_between_multiple_charged_spheres",
        "question_family_id": "42_predicting_interaction_between_multiple_charged_spheres",
        "hints": {
            "tier_1": "Remember: only like charges repel, but attraction can involve neutral objects.",
            "tier_2": "A repels B -> B is positive. Positive attracts negative OR neutral.",
            "tier_3": "Sphere B is positive; Sphere C is either negative or neutral."
        },
        "misconception_tags": ["attraction_only_between_opposite_charges"]
    }


def arch_43_charging_by_contact_conduction_between_spheres(rng: random.Random) -> Dict[str, Any]:
    q_init = rng.choice([-8, -6, -4, -10])
    q_final = q_init // 2
    prompt = (
        f"Identical metal Sphere 1 carries a charge of ${q_init}\\text{{ nC}}$ (nanocoulombs). "
        f"Identical metal Sphere 2 is completely neutral ($0\\text{{ nC}}$). "
        f"Both spheres rest on insulating stands. "
        f"The two spheres are touched together momentarily and then separated.\n\n"
        f"What is the final charge on each sphere after separation?"
    )
    correct_opt = f"Each sphere carries {q_final} nC (identical negative charges)."
    options = [
        correct_opt,
        f"Sphere 1 has {q_init} nC and Sphere 2 has 0 nC (no charge transfers).",
        f"Each sphere carries {q_init} nC (charge doubles automatically).",
        f"Sphere 1 has 0 nC and Sphere 2 has {q_init} nC (all charge transferred)."
    ]
    rng.shuffle(options)
    sol = (
        f"**Conduction Between Identical Conductors:**\n"
        f"1. **Law of Conservation of Charge:** Total charge is conserved:\n"
        f"   $$Q_\\text{{total}} = Q_1 + Q_2 = {q_init}\\text{{ nC}} + 0\\text{{ nC}} = {q_init}\\text{{ nC}}\n$$\n"
        f"2. Because the spheres are identical in geometry, excess electrons redistribute equally due to mutual electrostatic repulsion:\n"
        f"   $$Q_\\text{{final}} = \\frac{{Q_\\text{{total}}}}{{2}} = \\frac{{{q_init}}}{{2}} = {q_final}\\text{{ nC}}\n$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_43_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "43_charging_by_contact_conduction_between_spheres",
        "question_family_id": "43_charging_by_contact_conduction_between_spheres",
        "hints": {
            "tier_1": "Divide total charge equally between the two identical spheres.",
            "tier_2": f"Total charge = {q_init} nC. Split between 2 spheres = {q_final} nC each.",
            "tier_3": f"Each sphere carries {q_final} nC."
        },
        "misconception_tags": ["charge_does_not_share_equally"]
    }


def arch_44_separating_two_neutral_spheres_in_presence_of_charged_rod(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Two uncharged metal spheres (Sphere P and Sphere Q) touch each other on insulating stands. "
        f"A negatively charged plastic rod is held near Sphere P without touching it. "
        f"While the rod is held in place, the two spheres are separated. The charged rod is then removed.\n\n"
        f"What are the final charges on Sphere P and Sphere Q?"
    )
    correct_opt = "Sphere P is positively charged, and Sphere Q is negatively charged."
    options = [
        correct_opt,
        "Sphere P is negatively charged, and Sphere Q is positively charged.",
        "Both spheres are negatively charged because the rod transferred its electrons.",
        "Both spheres remain completely neutral because the rod never touched them."
    ]
    rng.shuffle(options)
    sol = (
        f"**Two-Sphere Electrostatic Induction:**\n"
        f"1. Negative rod repels mobile electrons away from Sphere P into Sphere Q.\n"
        f"2. Sphere P now has a deficit of electrons (**positive**).\n"
        f"3. Sphere Q now has an excess of electrons (**negative**).\n"
        f"4. When separated with the rod still near, the electrons are trapped on Sphere Q.\n"
        f"5. Removing the rod leaves Sphere P positive and Sphere Q negative.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_44_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "44_separating_two_neutral_spheres_in_presence_of_charged_rod",
        "question_family_id": "44_separating_two_neutral_spheres_in_presence_of_charged_rod",
        "hints": {
            "tier_1": "Where do negative electrons go when repelled by a negative rod?",
            "tier_2": "Electrons are repelled into Sphere Q, leaving Sphere P positive.",
            "tier_3": "Sphere P is positive (electrons repelled away); Sphere Q is negative."
        },
        "misconception_tags": ["induction_leaves_both_spheres_neutral"]
    }


def arch_45_misconception_positive_protons_move_during_charging(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner writes in a test: *'When silk rubs a glass rod, positive protons flow from the silk into the glass.'*\n\n"
        f"Which statement best corrects this fundamental misconception?"
    )
    correct_opt = "Protons never move between objects during electrostatic charging; the glass rod becomes positively charged because it LOSES negative electrons to the silk."
    options = [
        correct_opt,
        "The statement is completely true because positive charge always consists of flowing protons.",
        "Protons only move when the ambient temperature is below 0 °C.",
        "Glass contains no electrons, only protons."
    ]
    rng.shuffle(options)
    sol = (
        f"**Core Truth of Electrostatics:**\n"
        f"- Protons are bound rigidly inside the atomic nucleus by the strong nuclear force.\n"
        f"- Only outer electrons are mobile and can be transferred by friction.\n"
        f"- Gaining a positive charge is strictly the result of **losing negative electrons**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_45_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "45_misconception_positive_protons_move_during_charging",
        "question_family_id": "45_misconception_positive_protons_move_during_charging",
        "hints": {
            "tier_1": "Can protons move between atoms during everyday friction?",
            "tier_2": "Protons are locked in the nucleus; only electrons move.",
            "tier_3": "Protons never move during charging; objects become positive by losing electrons."
        },
        "misconception_tags": ["proton_transfer_fallacy"]
    }


def arch_46_misconception_neutral_objects_have_no_charges_at_all(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner believes that an uncharged neutral plastic ruler contains 'no electricity and zero electrical charges whatsoever'.\n\n"
        f"Why is this belief incorrect?"
    )
    correct_opt = "A neutral object contains trillions of positive protons and trillions of negative electrons; it appears uncharged only because the equal positive and negative charges precisely balance to net zero."
    options = [
        correct_opt,
        "The learner is correct because neutral means an object is completely devoid of atoms.",
        "Neutral objects contain only neutrons and have lost all atomic structure.",
        "Charges only appear when an object is plugged into a wall power outlet."
    ]
    rng.shuffle(options)
    sol = (
        f"**Understanding Neutrality:**\n"
        f"- All matter is made of atoms consisting of protons, neutrons, and electrons.\n"
        f"- A $10\\text{{-gram}}$ ruler contains roughly $3 \\times 10^{{24}}$ protons and an equal $3 \\times 10^{{24}}$ electrons.\n"
        f"- Electrical neutrality is an exact balance, not an absence of charges.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_46_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "46_misconception_neutral_objects_have_no_charges_at_all",
        "question_family_id": "46_misconception_neutral_objects_have_no_charges_at_all",
        "hints": {
            "tier_1": "Are atoms made of charged particles?",
            "tier_2": "Yes, atoms contain protons and electrons. Neutral means they balance.",
            "tier_3": "Neutral objects contain trillions of protons and electrons that balance to net zero."
        },
        "misconception_tags": ["neutral_equals_empty_of_charge"]
    }


def arch_47_misconception_static_electricity_is_a_different_kind_of_energy(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner asks: *'Is static electricity a completely different kind of electricity from the current electricity flowing through wall sockets?'*\n\n"
        f"What is the true relationship between static electricity and current electricity?"
    )
    correct_opt = "Both involve the exact same fundamental electrical charges (electrons); 'static' electricity refers to charges at rest (accumulated), while 'current' electricity refers to charges in continuous motion."
    options = [
        correct_opt,
        "Static electricity is made of protons, while current electricity is made of magnetism.",
        "Static electricity only occurs in nature, while current electricity was invented in a factory.",
        "They are two completely incompatible physical forces that destroy each other on contact."
    ]
    rng.shuffle(options)
    sol = (
        f"**Static vs Current Electricity:**\n"
        f"- Both involve the **same negative electrons** and **positive protons**.\n"
        f"- **Static electricity:** Charges build up and remain largely stationary on an insulating surface until discharged.\n"
        f"- **Current electricity:** Charges flow continuously along a closed conductive path.\n"
        f"- When static electricity discharges (a spark), it momentarily becomes current electricity!\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_47_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "47_misconception_static_electricity_is_a_different_kind_of_energy",
        "question_family_id": "47_misconception_static_electricity_is_a_different_kind_of_energy",
        "hints": {
            "tier_1": "Do static and current electricity both use electrons?",
            "tier_2": "Yes. Static is charges at rest; current is charges moving.",
            "tier_3": "Both involve the exact same electrons; static is at rest, current is in motion."
        },
        "misconception_tags": ["static_is_different_entity"]
    }


def arch_48_misconception_lightning_never_strikes_the_same_place_twice(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A widespread folk myth claims: *'Lightning never strikes the same place twice.'*\n\n"
        f"How does scientific data from meteorological observatories and tall structures (like the Hillbrow Tower or Brixton Tower in Johannesburg) disprove this myth?"
    )
    correct_opt = "Tall, pointed conductive structures provide the shortest path of least resistance from cloud to ground and are struck repeatedly, often dozens of times every year."
    options = [
        correct_opt,
        "The myth is true because the ground becomes permanently immune to electricity after one strike.",
        "Lightning only strikes an object once because the object vaporizes immediately.",
        "Clouds remember where they struck and deliberately avoid those coordinates."
    ]
    rng.shuffle(options)
    sol = (
        f"**Refuting the Lightning Myth:**\n"
        f"- Lightning strikes the path of **least electrical resistance** to ground.\n"
        f"- Prominent tall buildings (e.g. Empire State Building, Hillbrow Tower) are struck 20 to 100 times every single year.\n"
        f"- The idea that lightning never strikes the same place twice is dangerous folklore with zero scientific basis.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_48_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "48_misconception_lightning_never_strikes_the_same_place_twice",
        "question_family_id": "48_misconception_lightning_never_strikes_the_same_place_twice",
        "hints": {
            "tier_1": "Do tall communication towers get struck by lightning more than once?",
            "tier_2": "Tall structures are struck dozens of times a year because they offer the path of least resistance.",
            "tier_3": "Tall structures provide the path of least resistance and are struck repeatedly."
        },
        "misconception_tags": ["lightning_never_strikes_twice"]
    }


def arch_49_investigating_factors_affecting_static_charge_strength(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Learners investigate factors affecting the amount of static charge generated by friction. "
        f"They test rubbing a plastic rod 5 times, 15 times, and 30 times with wool, measuring how many paper scraps are picked up.\n\n"
        f"What relationship between friction duration/strokes and static charge is demonstrated?"
    )
    correct_opt = "More rubbing strokes provide more kinetic energy and friction contact, transferring more electrons and generating a stronger electrostatic charge (up to a saturation limit)."
    options = [
        correct_opt,
        "More rubbing strokes destroys electrons, reducing the charge to zero.",
        "The number of strokes has zero effect because static charge is always a constant fixed number.",
        "Rubbing more than 10 times causes the rod to turn into molten liquid iron."
    ]
    rng.shuffle(options)
    sol = (
        f"**Investigating Charging by Friction:**\n"
        f"1. Each stroke brings fresh uncharged microscopic surface regions into direct contact.\n"
        f"2. Increased friction transfers more electrons across the contact interface.\n"
        f"3. Greater accumulated net charge produces a stronger electric field, attracting more paper scraps.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_49_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "49_investigating_factors_affecting_static_charge_strength",
        "question_family_id": "49_investigating_factors_affecting_static_charge_strength",
        "hints": {
            "tier_1": "Does more friction transfer more or fewer electrons?",
            "tier_2": "More rubbing strokes transfer more electrons, building up a stronger charge.",
            "tier_3": "More strokes transfer more electrons, building up a stronger electrostatic charge."
        },
        "misconception_tags": ["charge_independent_of_friction"]
    }


def arch_50_static_electricity_comprehensive_diagnostic_evaluation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A comprehensive examination question assesses three core principles of static electricity:\n"
        f"Principle 1: Friction transfers only negative electrons; positive protons remain fixed in nuclei.\n"
        f"Principle 2: Like charges repel each other, while unlike charges attract each other.\n"
        f"Principle 3: Earthing neutralizes a charged conductor by allowing electrons to flow to or from the Earth.\n\n"
        f"Which evaluation of these three principles is scientifically correct?"
    )
    correct_opt = "All three principles (1, 2, and 3) are foundational, scientifically proven laws of electrostatics."
    options = [
        correct_opt,
        "Only Principle 1 is correct; Principles 2 and 3 are scientific fallacies.",
        "Only Principle 2 is correct; Principles 1 and 3 violate atomic theory.",
        "All three principles are incorrect and superseded by quantum gravity."
    ]
    rng.shuffle(options)
    sol = (
        f"**Comprehensive Electrostatics Diagnostic:**\n"
        f"- **Principle 1 is TRUE:** Only electrons are transferred during electrostatic charging; protons stay bound in nuclei.\n"
        f"- **Principle 2 is TRUE:** The fundamental law of electrostatics states that like charges repel and opposite charges attract.\n"
        f"- **Principle 3 is TRUE:** Connecting a conductor to Earth allows electrons to flow until net charge is zero.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_50_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "50_static_electricity_comprehensive_diagnostic_evaluation",
        "question_family_id": "50_static_electricity_comprehensive_diagnostic_evaluation",
        "hints": {
            "tier_1": "Are all 3 statements foundational laws of electrostatics?",
            "tier_2": "Every one of the three principles is true.",
            "tier_3": "All three principles (1, 2, and 3) are foundational, scientifically proven laws."
        },
        "misconception_tags": ["diagnostic_synthesis_error"]
    }
