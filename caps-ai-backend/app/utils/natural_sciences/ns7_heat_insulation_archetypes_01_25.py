"""Grade 7 Natural Sciences: Term 3 - Heat Insulation and Energy Saving Archetypes (01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/04. Heat insulation and energy saving.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List


def arch_01_definition_of_thermal_insulator(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In natural sciences and thermal physics, materials are classified according to how easily heat transfers through them.\n\n"
        f"Which statement provides the precise scientific definition of a **thermal insulator**?"
    )
    correct_opt = "A material that resists, reduces, or significantly slows down the transfer of thermal energy (by conduction, convection, or radiation)."
    options = [
        correct_opt,
        "A material that produces its own electrical thermal energy when placed in the dark.",
        "A substance that completely destroys any heat energy that enters into it.",
        "A material that conducts thermal energy at the speed of light without resistance."
    ]
    rng.shuffle(options)
    sol = (
        f"**Definition of a Thermal Insulator:**\n"
        f"- A thermal insulator is a material through which thermal energy conducts or transfers very poorly.\n"
        f"- Insulators contain few or no free electrons and often trap pockets of air, drastically reducing heat dissipation.\n"
        f"- They are used to keep hot objects hot and cold objects cold.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_01_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "01_definition_of_thermal_insulator",
        "question_family_id": "01_definition_of_thermal_insulator",
        "hints": {
            "tier_1": "Does an insulator speed up or slow down heat transfer?",
            "tier_2": "Insulators resist the flow of thermal energy.",
            "tier_3": "A material that significantly slows down the transfer of thermal energy."
        },
        "misconception_tags": ["insulators_generate_heat"]
    }


def arch_02_distinguishing_thermal_conductors_from_insulators(rng: random.Random) -> Dict[str, Any]:
    groups = [
        (["Copper", "Aluminium", "Iron", "Silver"], ["Wood", "Plastic", "Glass wool", "Polystyrene"]),
        (["Brass", "Gold", "Steel", "Zinc"], ["Cork", "Dry straw", "Rubber", "Cardboard"])
    ]
    conductors, insulators = rng.choice(groups)
    prompt = (
        f"A laboratory technician separates a collection of materials into two groups: conductors and insulators.\n\n"
        f"Which classification correctly groups these materials?"
    )
    c_str = ", ".join(conductors)
    i_str = ", ".join(insulators)
    correct_opt = f"Conductors: {c_str} | Insulators: {i_str}"
    options = [
        correct_opt,
        f"Conductors: {i_str} | Insulators: {c_str}",
        f"Conductors: {conductors[0]}, {insulators[0]} | Insulators: {conductors[1]}, {insulators[1]}",
        "All solid substances conduct heat at the identical high speed"
    ]
    rng.shuffle(options)
    sol = (
        f"**Conductors vs Insulators:**\n"
        f"- **Good thermal conductors:** Metals ({c_str}) due to free electrons and close lattice packing.\n"
        f"- **Good thermal insulators:** Non-metals and porous materials ({i_str}) due to bound electrons and trapped air pockets.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_02_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "02_distinguishing_thermal_conductors_from_insulators",
        "question_family_id": "02_distinguishing_thermal_conductors_from_insulators",
        "hints": {
            "tier_1": "Which group contains metals vs non-metals?",
            "tier_2": "Metals are conductors; non-metallic porous materials are insulators.",
            "tier_3": f"Conductors: {c_str} | Insulators: {i_str}."
        },
        "misconception_tags": ["confusing_conductors_and_insulators"]
    }


def arch_03_role_of_trapped_air_in_insulating_materials(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Many of the most effective commercial and natural thermal insulators (such as fibreglass batts, polystyrene foam, sheep's wool, and down feathers) consist largely of **trapped still air**.\n\n"
        f"Why is trapped still air such an outstanding thermal barrier?"
    )
    correct_opt = "Air is a gas whose widely separated particles conduct heat extremely slowly, and trapping it in tiny microscopic pockets prevents convection currents from developing."
    options = [
        correct_opt,
        "Air particles absorb coldness and chemically turn it into warm nitrogen.",
        "Air in tiny pockets freezes solid at room temperature, blocking all thermal vibrations.",
        "Trapped air attracts magnetic waves that neutralise infrared rays."
    ]
    rng.shuffle(options)
    sol = (
        f"**Physical Basis of Air as an Insulator:**\n"
        f"1. **Poor conduction:** Air molecules are far apart; thermal conductivity of stationary air is extremely low ($k \\approx 0{{,}}026\\text{{ W/m·K}}$).\n"
        f"2. **Suppression of convection:** Free air can transfer heat easily by convection currents. When air is trapped in microscopic pores, pockets, or fibres, fluid circulation is physically blocked.\n"
        f"3. Thus, both conduction and convection are virtually eliminated.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_03_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "03_role_of_trapped_air_in_insulating_materials",
        "question_family_id": "03_role_of_trapped_air_in_insulating_materials",
        "hints": {
            "tier_1": "How do gas particles conduct heat, and what happens when air cannot circulate?",
            "tier_2": "Air has low conductivity, and trapping it stops convection currents.",
            "tier_3": "Air particles conduct poorly, and trapping them in tiny pockets stops convection."
        },
        "misconception_tags": ["air_is_a_good_conductor"]
    }


def arch_04_investigating_cup_insulation_materials_comparison(rng: random.Random) -> Dict[str, Any]:
    temp_init = rng.choice([75, 80, 85])
    prompt = (
        f"Four identical tin cans each containing $150\\text{{ cm}}^3$ of hot water at {temp_init} °C are wrapped in equal thicknesses of different materials: "
        f"Can 1: Newspaper | Can 2: Bubble wrap | Can 3: Bare metal (unwrapped control) | Can 4: Polystyrene foam.\n\n"
        f"After 20 minutes, which can will retain the **highest** temperature, and which will record the **lowest** temperature?"
    )
    correct_opt = "Highest temperature: Can 4 (Polystyrene foam) | Lowest temperature: Can 3 (Bare metal control)"
    options = [
        correct_opt,
        "Highest temperature: Can 3 (Bare metal) | Lowest temperature: Can 4 (Polystyrene foam)",
        "Highest temperature: Can 1 (Newspaper) | Lowest temperature: Can 2 (Bubble wrap)",
        "All four cans will drop to 0 °C in the exact same time"
    ]
    rng.shuffle(options)
    sol = (
        f"**Insulation Comparison Analysis:**\n"
        f"- Polystyrene foam has millions of closed trapped gas cells, giving it the lowest thermal conductivity -> retains heat best (highest final temperature).\n"
        f"- Bubble wrap and newspaper provide intermediate insulation.\n"
        f"- Bare metal is an unwrapped conductor with high heat loss via conduction, convection, and radiation -> cools fastest (lowest final temperature).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_04_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "04_investigating_cup_insulation_materials_comparison",
        "question_family_id": "04_investigating_cup_insulation_materials_comparison",
        "hints": {
            "tier_1": "Which material is the best insulator, and which is uninsulated?",
            "tier_2": "Polystyrene insulates best; bare unwrapped metal loses heat fastest.",
            "tier_3": "Can 4 (polystyrene) highest; Can 3 (bare metal) lowest."
        },
        "misconception_tags": ["bare_can_stays_warmest"]
    }


def arch_05_identifying_variables_in_insulation_investigation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Learners conduct a scientific investigation titled: *'Which wrapping material keeps coffee hot for the longest time?'*\n\n"
        f"Which selection correctly identifies the independent variable, dependent variable, and one essential controlled variable?"
    )
    correct_opt = "Independent: Type of wrapping material | Dependent: Temperature of water over time | Controlled: Initial volume and starting temperature of water"
    options = [
        correct_opt,
        "Independent: Starting temperature of water | Dependent: Type of wrapping material | Controlled: Room colour",
        "Independent: Temperature over time | Dependent: Brand of thermometer | Controlled: Type of wrapping material",
        "There are no controlled variables needed in thermal investigations"
    ]
    rng.shuffle(options)
    sol = (
        f"**Scientific Method Variables:**\n"
        f"- **Independent variable (manipulated):** The wrapping material being tested.\n"
        f"- **Dependent variable (measured response):** The temperature of the liquid recorded over time.\n"
        f"- **Controlled variables (kept constant):** Liquid volume, starting water temperature, container size, ambient room temperature.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_05_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "05_identifying_variables_in_insulation_investigation",
        "question_family_id": "05_identifying_variables_in_insulation_investigation",
        "hints": {
            "tier_1": "What is changed, what is measured, and what is kept the same?",
            "tier_2": "Independent = material; Dependent = temperature; Controlled = volume and starting temp.",
            "tier_3": "Independent: Type of wrapping material | Dependent: Temperature over time | Controlled: Initial volume and starting temperature."
        },
        "misconception_tags": ["variable_inversion_error"]
    }


def arch_06_polystyrene_cooler_box_thermal_mechanism(rng: random.Random) -> Dict[str, Any]:
    items = ["cold cold-drinks and ice packs", "fresh butchery meat for a braai", "vaccine vials transported to a rural clinic"]
    item = rng.choice(items)
    prompt = (
        f"Expanded polystyrene (Styrofoam) cooler boxes are widely used in South Africa to transport {item}.\n\n"
        f"How does the polystyrene cooler box keep its contents cold for hours?"
    )
    correct_opt = "It contains trapped air pockets that prevent outside warm air from conducting heat into the interior, while the lid stops warm convection currents from entering."
    options = [
        correct_opt,
        "The polystyrene produces active freezing rays that continually drop the temperature below 0 °C.",
        "The box absorbs heat from the outside and converts it into pure solid ice.",
        "Polystyrene draws coldness out of the atmosphere and pumps it inside."
    ]
    rng.shuffle(options)
    sol = (
        f"**Cooler Box Physics:**\n"
        f"1. A cooler box does not generate cold; it simply prevents heat from entering.\n"
        f"2. Heat naturally transfers from warmer ambient surroundings toward colder interior items.\n"
        f"3. Thick polystyrene walls have very low thermal conductivity due to millions of trapped gas bubbles, stopping conductive heat gain.\n"
        f"4. The sealed lid prevents outside warm air from circulating inside by convection.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_06_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "06_polystyrene_cooler_box_thermal_mechanism",
        "question_family_id": "06_polystyrene_cooler_box_thermal_mechanism",
        "hints": {
            "tier_1": "Does a cooler box make cold or stop heat from entering?",
            "tier_2": "It stops external heat from conducting and convecting inward.",
            "tier_3": "Trapped air prevents heat conduction into the interior, and the lid blocks convection."
        },
        "misconception_tags": ["cooler_boxes_generate_cold"]
    }


def arch_07_bubble_wrap_and_cardboard_packaging_insulation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Corrugated cardboard and plastic bubble wrap are widely used for protective packaging. When tested for thermal properties, both act as remarkably good thermal insulators.\n\n"
        f"What structural similarity explains why both materials resist heat transfer?"
    )
    correct_opt = "Both feature sealed dead-air spaces (air-filled plastic hemispheres in bubble wrap; fluted corrugation air channels in cardboard) that halt conduction and convection."
    options = [
        correct_opt,
        "Both materials are infused with metallic lead that absorbs gamma rays.",
        "Cardboard and plastic are superconducting conductors that redirect heat into light.",
        "Both contain magnetic fields that repel temperature molecules."
    ]
    rng.shuffle(options)
    sol = (
        f"**Structural Thermal Analysis:**\n"
        f"- Bubble wrap seals individual pockets of air inside flexible polymer film.\n"
        f"- Corrugated cardboard sandwiches fluted paper waves between linerboards, creating internal air channels.\n"
        f"- In both, heat cannot conduct easily across the dead-air gap, and air cannot circulate to create convection currents.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_07_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "07_bubble_wrap_and_cardboard_packaging_insulation",
        "question_family_id": "07_bubble_wrap_and_cardboard_packaging_insulation",
        "hints": {
            "tier_1": "What is inside the bubbles of bubble wrap and the flutes of cardboard?",
            "tier_2": "Both trap stationary air in pockets or channels.",
            "tier_3": "Sealed dead-air spaces in both materials halt conduction and convection."
        },
        "misconception_tags": ["cardboard_has_no_thermal_properties"]
    }


def arch_08_mineral_wool_and_fibreglass_ceiling_insulation(rng: random.Random) -> Dict[str, Any]:
    thickness = rng.choice([100, 135, 145])
    prompt = (
        f"In South African building standards (SANS 10400-XA), installing {thickness} mm fibreglass or mineral wool insulation rolls in roof ceilings is mandatory for energy efficiency.\n\n"
        f"How does ceiling insulation reduce home heating and cooling energy needs?"
    )
    correct_opt = "It prevents thermal energy from conducting through the roof into the home during hot summer days, and stops indoor heated air from escaping through the roof in winter."
    options = [
        correct_opt,
        "It acts as a battery that generates electrical current for household lighting.",
        "It pulls moisture from the sky to cool the shingles with cold rain.",
        "It eliminates gravity inside the ceiling to stop hot air from rising."
    ]
    rng.shuffle(options)
    sol = (
        f"**Dual Benefit of Ceiling Insulation:**\n"
        f"- In **summer**: The sun heats the roof tiles/sheeting to >$60^\\circ\\text{{C}}$. Ceiling batts prevent this massive heat load from conducting downward into living areas.\n"
        f"- In **winter**: Warm indoor air rises towards the ceiling. Insulation prevents heat from conducting through the ceiling boards into the cold roof cavity and outside.\n"
        f"- Result: Massive reduction in electricity used by heaters and air conditioners.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_08_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "08_mineral_wool_and_fibreglass_ceiling_insulation",
        "question_family_id": "08_mineral_wool_and_fibreglass_ceiling_insulation",
        "hints": {
            "tier_1": "Does ceiling insulation help in summer, winter, or both?",
            "tier_2": "It blocks summer heat coming down and stops winter warmth escaping up.",
            "tier_3": "Prevents roof heat entering in summer, and keeps indoor heat inside in winter."
        },
        "misconception_tags": ["insulation_only_needed_in_winter"]
    }


def arch_09_cellulose_and_recycled_paper_ceiling_batts(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Cellulose ceiling insulation is manufactured from recycled newspaper treated with non-toxic fire-retardant borate minerals.\n\n"
        f"From an environmental and thermal standpoint, why is treated recycled cellulose an effective sustainable choice?"
    )
    correct_opt = "It repurposes waste paper, traps air effectively between tangled paper fibres for high thermal resistance, and has low embodied energy compared to synthetic materials."
    options = [
        correct_opt,
        "It evaporates completely after installation to create a permanent vacuum in the ceiling.",
        "It converts into coal inside the ceiling to provide winter heating.",
        "It is 100% transparent and allows infrared light to pass freely."
    ]
    rng.shuffle(options)
    sol = (
        f"**Cellulose Insulation Advantages:**\n"
        f"1. **Environmental:** Diverts waste paper from landfills and requires far less manufacturing energy (embodied energy) than glass or rock wool.\n"
        f"2. **Thermal:** Tangled wood/paper fibres trap air efficiently, providing high thermal resistance (R-value).\n"
        f"3. **Safety:** Borate salts make it fire-retardant and resistant to insects and rodents.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_09_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "09_cellulose_and_recycled_paper_ceiling_batts",
        "question_family_id": "09_cellulose_and_recycled_paper_ceiling_batts",
        "hints": {
            "tier_1": "Consider recycling, air trapping, and low carbon footprint.",
            "tier_2": "Recycles paper, traps air efficiently, low embodied energy.",
            "tier_3": "Repurposes waste paper, traps air between fibres, low embodied energy."
        },
        "misconception_tags": ["recycled_materials_have_poor_insulation"]
    }


def arch_10_reflective_foil_radiant_barrier_in_roofs(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A multi-layer aluminium radiant foil barrier is installed directly beneath roof tiles or corrugated iron sheeting with an air gap facing downward.\n\n"
        f"Which mechanism of heat transfer does this shiny metallic foil primarily block?"
    )
    correct_opt = "Radiation: the shiny aluminium foil has high reflectivity and low emissivity, reflecting over 90% of radiant heat coming from the hot roof sheeting."
    options = [
        correct_opt,
        "Convection: the foil dissolves all air currents and creates liquid nitrogen.",
        "Conduction: aluminium is a non-metal that blocks all particle collisions.",
        "Gravity: the foil reverses gravitational acceleration in the attic."
    ]
    rng.shuffle(options)
    sol = (
        f"**Radiant Barriers & Heat Radiation:**\n"
        f"- In summer, roof tiles reach high temperatures and radiate intense infrared waves downward into the attic space.\n"
        f"- Aluminium foil is a **radiant barrier**.\n"
        f"- Its shiny mirror-like surface reflects incoming thermal radiation back towards the roof tiles.\n"
        f"- It also has very low emissivity, emitting minimal infrared radiation downward into the ceiling.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_10_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "10_reflective_foil_radiant_barrier_in_roofs",
        "question_family_id": "10_reflective_foil_radiant_barrier_in_roofs",
        "hints": {
            "tier_1": "What heat transfer mode is stopped by shiny reflective foil?",
            "tier_2": "Shiny foil reflects infrared thermal radiation.",
            "tier_3": "Radiation: shiny foil reflects over 90% of radiant heat from the roof."
        },
        "misconception_tags": ["foil_only_stops_conduction"]
    }


def arch_11_hot_box_wonderbag_thermal_cooking_concept(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A 'hot box' (or Wonderbag) is an insulated bag filled with polystyrene foam beads or dry fabric scraps. "
        f"A pot of stew is brought to a boil on a stove for 10 minutes, then placed inside the hot box and sealed tightly.\n\n"
        f"How does the hot box continue cooking the stew for several hours without any external heat source?"
    )
    correct_opt = "The thick insulation drastically reduces heat loss by conduction and convection, keeping the pot at near-boiling cooking temperatures using only its retained thermal energy."
    options = [
        correct_opt,
        "The polystyrene beads contain an internal chemical fuel that burns without smoke.",
        "The fabric generates electrical microwaves that vibrate food particles.",
        "The sealed box draws solar energy through the fabric fibers even in a dark cupboard."
    ]
    rng.shuffle(options)
    sol = (
        f"**Physics of Retained-Heat Cooking (Hot Box):**\n"
        f"1. Water and stew have a high specific heat capacity and hold large amounts of thermal energy at $100^\\circ\\text{{C}}$.\n"
        f"2. Normally on a counter, heat escapes rapidly via conduction, convection, and steam evaporation.\n"
        f"3. In a hot box, thick insulating material traps air and stops heat loss.\n"
        f"4. The temperature stays above $80^\\circ\\text{{C}}$ for 4-8 hours, continuing the gentle cooking process without burning extra electricity or wood.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_11_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "11_hot_box_wonderbag_thermal_cooking_concept",
        "question_family_id": "11_hot_box_wonderbag_thermal_cooking_concept",
        "hints": {
            "tier_1": "Does the hot box add new heat, or trap existing heat?",
            "tier_2": "It traps existing thermal energy, slowing cooling to a crawl.",
            "tier_3": "Thick insulation prevents heat loss, keeping food hot enough to cook on retained heat."
        },
        "misconception_tags": ["hot_boxes_add_energy"]
    }


def arch_12_hot_box_food_safety_and_fuel_saving_benefits(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In rural and informal communities in South Africa, using a hot box offers major social, economic, and safety benefits.\n\n"
        f"Which combination accurately lists these benefits?"
    )
    correct_opt = "Saves up to 70% of cooking fuel/electricity, reduces paraffin stove fires and burns, and frees up time because food cannot boil over or burn."
    options = [
        correct_opt,
        "Eliminates the need for any water or food ingredients during cooking.",
        "Causes food to become radioactive and stay preserved for 100 years.",
        "Generates excess electricity that can be fed into the national power grid."
    ]
    rng.shuffle(options)
    sol = (
        f"**Benefits of Retained-Heat Cooking in South Africa:**\n"
        f"- **Fuel & money savings:** Cuts electricity, gas, paraffin, or firewood usage by up to 60-70%.\n"
        f"- **Fire safety:** Less time with open paraffin flames or stoves reduces house fire risk.\n"
        f"- **Convenience:** Food cooks gently without scorching, boiling dry, or requiring constant supervision.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_12_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "12_hot_box_food_safety_and_fuel_saving_benefits",
        "question_family_id": "12_hot_box_food_safety_and_fuel_saving_benefits",
        "hints": {
            "tier_1": "Think about fuel costs, fire safety, and burning food.",
            "tier_2": "Saves fuel/electricity, reduces fire hazards, prevents burning.",
            "tier_3": "Saves up to 70% fuel/electricity, reduces paraffin stove fires, and frees up time."
        },
        "misconception_tags": ["cooking_always_requires_constant_flame"]
    }


def arch_13_solar_water_heater_storage_tank_insulation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A solar water heater collects solar energy during the day to heat water. "
        f"However, families need hot water early in the morning before the Sun rises.\n\n"
        f"What design feature ensures water heated during yesterday's afternoon stays hot overnight?"
    )
    correct_opt = "The storage tank is encased in a thick, seamless layer of rigid polyurethane foam insulation that minimizes conductive and convective heat loss through the tank walls."
    options = [
        correct_opt,
        "The tank is left uninsulated so night air can recharge the water particles.",
        "Water is pumped into deep underground caves every night and pumped back up in the morning.",
        "The tank contains glowing nuclear fuel rods that keep water boiling forever."
    ]
    rng.shuffle(options)
    sol = (
        f"**Solar Storage Tank Insulation:**\n"
        f"- The key challenge of solar heating is matching daytime heat collection with morning demand.\n"
        f"- Storage geyser cylinders are surrounded by a thick layer of high-density rigid polyurethane foam ($k \\approx 0{{,}}022\\text{{ W/m·K}}$).\n"
        f"- This prevents thermal energy from escaping overnight into cold ambient air.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_13_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "13_solar_water_heater_storage_tank_insulation",
        "question_family_id": "13_solar_water_heater_storage_tank_insulation",
        "hints": {
            "tier_1": "How do you keep hot water warm overnight without new sunlight?",
            "tier_2": "Heavy tank insulation retains yesterday's heat.",
            "tier_3": "A thick layer of rigid polyurethane foam insulation minimizes heat loss overnight."
        },
        "misconception_tags": ["solar_heaters_only_work_when_sun_is_shining"]
    }


def arch_14_evacuated_glass_tube_solar_collector_insulation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"High-efficiency solar water heating systems use **evacuated glass tubes**. "
        f"Each tube consists of two concentric glass cylinders with a vacuum sealed between them.\n\n"
        f"Why is an evacuated tube collector significantly more efficient in cold or windy weather than a simple flat glass plate collector?"
    )
    correct_opt = "The vacuum space eliminates all heat loss by conduction and convection from the absorber to the outside cold air and wind."
    options = [
        correct_opt,
        "The vacuum magnifies gravity so sunlight moves faster through the glass.",
        "The tube sucks in warm air from outer space directly into the copper pipe.",
        "The double glass creates sound waves that heat the water through friction."
    ]
    rng.shuffle(options)
    sol = (
        f"**Evacuated Tube Insulation Physics:**\n"
        f"1. In cold or windy weather, a flat-plate collector loses large amounts of collected heat through air convection and conduction.\n"
        f"2. Evacuated tubes work like a Thermos flask: the vacuum contains no particles.\n"
        f"3. Conduction and convection cannot occur across a vacuum.\n"
        f"4. Therefore, solar radiation passes into the absorber, but heat cannot escape back out to the cold wind.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_14_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "14_evacuated_glass_tube_solar_collector_insulation",
        "question_family_id": "14_evacuated_glass_tube_solar_collector_insulation",
        "hints": {
            "tier_1": "What can cross a vacuum and what cannot?",
            "tier_2": "Conduction and convection cannot cross a vacuum, eliminating heat loss to wind.",
            "tier_3": "The vacuum space eliminates heat loss by conduction and convection."
        },
        "misconception_tags": ["vacuum_tubes_lose_heat_to_wind"]
    }


def arch_15_insulating_hot_water_copper_pipes(rng: random.Random) -> Dict[str, Any]:
    dist = rng.choice([2, 3, 4, 5])
    prompt = (
        f"Plumbers insulate the first {dist} metres of copper hot-water pipes leaving an electric geyser using closed-cell polyethylene foam sleeves.\n\n"
        f"Why is pipe insulation necessary, especially with copper pipes?"
    )
    correct_opt = "Copper is an outstanding thermal conductor; bare copper pipes rapidly conduct and radiate heat from hot water into cold roof cavities even when no tap is running."
    options = [
        correct_opt,
        "Copper dissolves immediately if exposed to air at temperatures above 30 °C.",
        "Pipe insulation is required to prevent water from turning into steam and bursting the pipes.",
        "Uninsulated pipes cause electric shocks through bathroom water taps."
    ]
    rng.shuffle(options)
    sol = (
        f"**Pipe Insulation Physics:**\n"
        f"1. Copper has an extremely high thermal conductivity (~$400\\text{{ W/m·K}}$).\n"
        f"2. Bare hot copper pipe acts like a radiator, continuously dumping heat into the cold ceiling space via conduction and radiation (thermosiphon standing losses).\n"
        f"3. Slipping closed-cell foam sleeves over the pipe drastically cuts standing thermal losses, saving significant electricity.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_15_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "15_insulating_hot_water_copper_pipes",
        "question_family_id": "15_insulating_hot_water_copper_pipes",
        "hints": {
            "tier_1": "Is copper a good conductor or insulator?",
            "tier_2": "Copper conducts heat away rapidly. Foam sleeves stop heat loss.",
            "tier_3": "Copper conducts heat rapidly; bare pipes radiate heat away into cold ceiling spaces."
        },
        "misconception_tags": ["pipes_do_not_lose_heat_when_taps_are_closed"]
    }


def arch_16_geyser_blanket_energy_conservation_impact(rng: random.Random) -> Dict[str, Any]:
    savings = rng.choice(["10% to 20%", "15% to 25%"])
    prompt = (
        f"Fitting a specialised thermal **geyser blanket** (fibreglass or mineral wool wrapped in reflective foil) around an electric geyser in a home roof space can reduce water-heating electricity consumption by {savings}.\n\n"
        f"What is the thermodynamic mechanism by which a geyser blanket achieves these savings?"
    )
    correct_opt = "It significantly reduces standing heat loss from the metal tank into the cold ceiling, reducing the frequency and duration that the electric element must switch on to maintain temperature."
    options = [
        correct_opt,
        "It acts as a secondary heating element by generating electrical watts from room sound.",
        "It prevents cold water from entering the geyser tank from municipal pipes.",
        "It forces the water inside the tank to stop moving at the atomic level."
    ]
    rng.shuffle(options)
    sol = (
        f"**Geyser Blanket Thermodynamics:**\n"
        f"- Water heaters suffer from 'standing losses'—continuous heat dissipation to surroundings even when no hot water is used.\n"
        f"- A geyser blanket adds thermal resistance ($R$-value) around the tank, slowing heat loss.\n"
        f"- As the water stays hot longer, the thermostat does not trip the heating element on as frequently, directly cutting kilowatt-hour (kWh) electricity usage.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_16_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "16_geyser_blanket_energy_conservation_impact",
        "question_family_id": "16_geyser_blanket_energy_conservation_impact",
        "hints": {
            "tier_1": "How does keeping a tank warm reduce element run time?",
            "tier_2": "Less standing heat loss means the heating element turns on less often.",
            "tier_3": "Reduces standing heat loss into the cold ceiling, so the element runs less."
        },
        "misconception_tags": ["geyser_blanket_adds_heat"]
    }


def arch_17_setting_geyser_thermostat_temperature_efficiency(rng: random.Random) -> Dict[str, Any]:
    high_t = rng.choice([70, 75, 80])
    eff_t = rng.choice([55, 60])
    prompt = (
        f"Energy efficiency experts in South Africa advise homeowners to lower their geyser thermostat from {high_t} °C down to {eff_t} °C.\n\n"
        f"Why does lowering the geyser thermostat from {high_t} °C to {eff_t} °C save significant electrical energy?"
    )
    correct_opt = f"The rate of heat loss to surroundings is directly proportional to the temperature difference; water at {eff_t} °C loses heat much slower than water at {high_t} °C, requiring less electricity to maintain."
    options = [
        correct_opt,
        f"Water at {eff_t} °C creates its own electricity through hydrogen bonding.",
        f"The geyser heating element stops drawing power completely at {eff_t} °C.",
        f"Lowering temperature increases water density so that gravity heats the tank for free."
    ]
    rng.shuffle(options)
    sol = (
        f"**Rate of Heat Loss & Thermostat Setting:**\n"
        f"1. Rate of heat loss $\\propto (T_\\text{{geyser}} - T_\\text{{surroundings}})$.\n"
        f"2. A geyser kept at {high_t} °C in a 15 °C ceiling has $\\Delta T = {high_t - 15}^\\circ\\text{{C}}$, causing very rapid heat leakage.\n"
        f"3. Lowering to {eff_t} °C reduces $\\Delta T$ to ${eff_t - 15}^\\circ\\text{{C}}$, dramatically slowing standing heat loss.\n"
        f"4. Heating water from cold to {eff_t} °C also requires fewer Joules: $Q = mc\\Delta T$.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_17_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "17_setting_geyser_thermostat_temperature_efficiency",
        "question_family_id": "17_setting_geyser_thermostat_temperature_efficiency",
        "hints": {
            "tier_1": "Does hotter water lose heat faster or slower?",
            "tier_2": "A smaller temperature difference with surroundings means slower heat loss.",
            "tier_3": f"Water at {eff_t} °C loses heat much slower than water at {high_t} °C."
        },
        "misconception_tags": ["higher_temp_saves_energy"]
    }


def arch_18_thatch_grass_roof_versus_corrugated_iron_sheet(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A traditional rondavel with a thick dry-grass thatched roof and a modern informal dwelling with an uninsulated corrugated iron roof are built side by side in a hot rural village.\n\n"
        f"On a scorching $36^\\circ\\text{{C}}$ summer midday, how and why will the indoor temperatures differ?"
    )
    correct_opt = "The thatched rondavel remains noticeably cool because thatch traps millions of air pockets that block conduction, while corrugated iron conducts intense solar heat straight into the dwelling."
    options = [
        correct_opt,
        "The corrugated iron house remains cooler because iron reflects 100% of heat into outer space.",
        "Both houses have identical temperatures because roofs do not affect indoor climate.",
        "The thatched rondavel catches fire automatically at midday due to grass metabolism."
    ]
    rng.shuffle(options)
    sol = (
        f"**Thermal Performance: Thatch vs Corrugated Iron:**\n"
        f"- **Corrugated iron:** Metal has high thermal conductivity. It rapidly absorbs solar radiation and conducts it directly into the room, turning the shack into an oven ($>45^\\circ\\text{{C}}$).\n"
        f"- **Thatch:** Natural grass stems create thousands of tiny trapped air pockets. Stationary air is an outstanding insulator ($k \\approx 0{{,}}026\\text{{ W/m·K}}$), preventing solar heat from conducting downwards.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_18_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "18_thatch_grass_roof_versus_corrugated_iron_sheet",
        "question_family_id": "18_thatch_grass_roof_versus_corrugated_iron_sheet",
        "hints": {
            "tier_1": "Which conducts heat faster: metal iron sheets or thick dry grass thatch?",
            "tier_2": "Iron conducts heat quickly; thatch traps air and insulates well.",
            "tier_3": "Thatch traps air pockets keeping the rondavel cool; corrugated iron conducts heat inside."
        },
        "misconception_tags": ["metal_roofs_are_cooler"]
    }


def arch_19_mud_brick_thermal_mass_in_traditional_dwellings(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Traditional African dwellings constructed with thick mud bricks or clay plaster stay comfortably moderate inside, even in arid regions where day temperatures soar to $38^\\circ\\text{{C}}$ and night temperatures drop to $8^\\circ\\text{{C}}$.\n\n"
        f"What physical phenomenon explains this moderating effect of thick mud walls?"
    )
    correct_opt = "High thermal mass (thermal inertia): thick mud walls absorb heat slowly during the hot day without heating up rapidly, then slowly release that stored thermal energy into the interior during the cold night."
    options = [
        correct_opt,
        "Mud contains subterranean water currents that pump air conditioning through microscopic tubes.",
        "Clay chemically neutralises all temperature fluctuations by converting heat into gravity.",
        "Mud bricks reflect all daylight and absorb all darkness."
    ]
    rng.shuffle(options)
    sol = (
        f"**Thermal Mass in Architecture:**\n"
        f"1. Heavy, dense materials like mud brick, stone, and adobe have high **thermal mass**.\n"
        f"2. They have large heat capacity and low thermal diffusivity.\n"
        f"3. During daytime, the thick walls absorb solar heat, keeping the interior cool.\n"
        f"4. The heat takes 6-10 hours to conduct through the wall ('thermal lag').\n"
        f"5. By nightfall when outside temperature plummets, the stored heat reaches the interior, keeping the room warm.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_19_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "19_mud_brick_thermal_mass_in_traditional_dwellings",
        "question_family_id": "19_mud_brick_thermal_mass_in_traditional_dwellings",
        "hints": {
            "tier_1": "What happens when heavy walls absorb heat during the day and release it at night?",
            "tier_2": "This is known as thermal mass or thermal inertia.",
            "tier_3": "High thermal mass absorbs daytime heat and releases it into the interior during the cold night."
        },
        "misconception_tags": ["walls_have_zero_thermal_inertia"]
    }


def arch_20_corrugated_iron_shack_temperature_extremes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Residents of informal settlements often describe uninsulated corrugated iron shacks as *'ovens in summer and refrigerators in winter'*.\n\n"
        f"Which two thermal properties of thin corrugated iron explain these extreme temperature fluctuations?"
    )
    correct_opt = "High thermal conductivity and negligible thermal insulation: iron transfers external heat rapidly inward in summer, and allows internal heat to escape rapidly outward in winter."
    options = [
        correct_opt,
        "Iron produces heat when cold and produces cold when hot.",
        "Corrugated iron creates an airtight vacuum that amplifies sound into heat.",
        "Iron attracts radioactive rays that freeze room air in June."
    ]
    rng.shuffle(options)
    sol = (
        f"**Thermal Deficiencies of Uninsulated Iron Shacks:**\n"
        f"1. **High conductivity:** Iron is a metal ($k \\approx 50-80\\text{{ W/m·K}}$). It conducts thermal energy very rapidly.\n"
        f"2. **Very thin cross-section:** Typically $0{{,}}5\\text{{ mm}}$, providing almost zero thermal resistance ($R \\approx 0$).\n"
        f"3. In summer: intense solar radiation conducts straight down inside.\n"
        f"4. In winter: indoor heat conducts straight out into freezing night air.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_20_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "20_corrugated_iron_shack_temperature_extremes",
        "question_family_id": "20_corrugated_iron_shack_temperature_extremes",
        "hints": {
            "tier_1": "Does thin metal have high or low thermal conductivity?",
            "tier_2": "High conductivity and low insulation cause rapid heat transfer both ways.",
            "tier_3": "High thermal conductivity and negligible insulation allow rapid heat transfer in both seasons."
        },
        "misconception_tags": ["metal_maintains_constant_temp"]
    }


def arch_21_passive_solar_building_orientation_south_africa(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In South Africa (located in the Southern Hemisphere), passive solar building guidelines recommend that the main living rooms and major windows should face **true North**.\n\n"
        f"What is the solar and thermal scientific reason for this North-facing orientation?"
    )
    correct_opt = "The Sun arcs across the northern sky in the Southern Hemisphere; North-facing windows capture maximum low-angled warming sunlight in winter while avoiding excessive harsh heat."
    options = [
        correct_opt,
        "Magnetic north attracts infrared radiation waves directly from the Earth's molten core.",
        "The Sun rises in the North and sets in the South in Southern Africa.",
        "South-facing windows would cause room oxygen to freeze into liquid nitrogen."
    ]
    rng.shuffle(options)
    sol = (
        f"**Passive Solar Orientation in South Africa:**\n"
        f"- In the Southern Hemisphere, the midday Sun is always in the **Northern** portion of the sky.\n"
        f"- In **winter**, the Sun is at a low angle in the north, shining directly into North-facing windows to provide free natural space heating.\n"
        f"- In **summer**, the Sun is high overhead at midday, making North-facing windows easy to shade with properly sized roof overhangs.\n"
        f"- East/West windows catch low, blistering summer morning/afternoon sun and should be kept small.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_21_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "21_passive_solar_building_orientation_south_africa",
        "question_family_id": "21_passive_solar_building_orientation_south_africa",
        "hints": {
            "tier_1": "Where is the Sun at midday in the Southern Hemisphere?",
            "tier_2": "The midday Sun is in the northern sky in South Africa.",
            "tier_3": "North-facing windows capture maximum low-angled sunlight in winter."
        },
        "misconception_tags": ["sun_direction_same_in_both_hemispheres"]
    }


def arch_22_roof_overhangs_and_eaves_seasonal_sun_angles(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Passive solar homes in South Africa are designed with carefully calculated roof overhangs (eaves) above north-facing windows.\n\n"
        f"How do roof overhangs take advantage of seasonal changes in solar elevation to regulate indoor temperatures?"
    )
    correct_opt = "In summer, when the midday Sun is high overhead, the overhang blocks harsh direct solar radiation; in winter, when the Sun is at a lower angle, sunlight passes under the overhang directly into the window."
    options = [
        correct_opt,
        "The overhang folds down mechanically like a garage door every evening at sunset.",
        "The overhang reflects cold air into the sky and absorbs warm air into the gutters.",
        "Overhangs prevent the Sun's ultraviolet waves from reaching the grass in the garden."
    ]
    rng.shuffle(options)
    sol = (
        f"**Seasonal Solar Elevation Geometry:**\n"
        f"- In **summer**: The Sun reaches a high solar elevation angle at midday (~$80^\\circ$). A fixed roof overhang casts a shadow over the window, preventing overheating.\n"
        f"- In **winter**: The Sun stays at a much lower midday angle (~$35^\\circ$). Sunlight streams directly under the eaves, penetrating deep into the room to warm the floor and walls.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_22_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "22_roof_overhangs_and_eaves_seasonal_sun_angles",
        "question_family_id": "22_roof_overhangs_and_eaves_seasonal_sun_angles",
        "hints": {
            "tier_1": "Is the Sun higher in the sky in summer or in winter?",
            "tier_2": "High summer Sun is blocked by eaves; low winter Sun passes underneath.",
            "tier_3": "Summer high Sun is shaded by overhangs; low winter Sun shines under into the window."
        },
        "misconception_tags": ["sun_angle_constant_all_year"]
    }


def arch_23_window_placement_and_sizing_for_solar_gain(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When designing an energy-smart house in Johannesburg or Bloemfontein, an architect plans different window sizes for North, South, East, and West walls.\n\n"
        f"Which window design strategy minimizes summer overheating while maximizing winter warmth?"
    )
    correct_opt = "Large, shaded North-facing windows (for winter solar gain) and small East/West windows (to prevent intense low-angled summer morning and afternoon overheating)."
    options = [
        correct_opt,
        "Massive unshaded West-facing glass walls with zero North-facing windows.",
        "All four walls must have identical floor-to-ceiling glass without any shading.",
        "Zero windows anywhere in the building to maintain total darkness."
    ]
    rng.shuffle(options)
    sol = (
        f"**Window Placement Strategy in South Africa:**\n"
        f"1. **North:** Large windows bring in desirable low winter sun; easy to shade in summer.\n"
        f"2. **East & West:** Low morning/afternoon summer sun strikes at shallow horizontal angles that overhangs cannot shade, causing severe overheating. Keep these windows small.\n"
        f"3. **South:** Receives almost no direct sun in winter; keep small to minimize conductive winter heat loss.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_23_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "23_window_placement_and_sizing_for_solar_gain",
        "question_family_id": "23_window_placement_and_sizing_for_solar_gain",
        "hints": {
            "tier_1": "Where should the largest windows be placed in South Africa?",
            "tier_2": "Large north windows for winter sun; small east/west windows to avoid summer heat.",
            "tier_3": "Large, shaded North-facing windows and small East/West windows."
        },
        "misconception_tags": ["all_orientations_equal"]
    }


def arch_24_thermal_curtains_pelmets_and_double_glazing(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Single-pane glass windows are significant sources of heat loss in winter. "
        f"Homeowners can install heavy lined curtains with closed **pelmets** (valance boxes above the curtain rail) or double-glazed window units.\n\n"
        f"How does a pelmet-enclosed curtain or double-glazing reduce convective and conductive winter heat loss?"
    )
    correct_opt = "Double-glazing traps a stationary air/argon gap between panes, while pelmets prevent cold downward air convection currents from flowing behind the curtain into the room."
    options = [
        correct_opt,
        "Pelmets create magnetic charges that attract dust to absorb cold air.",
        "Curtains generate thermal watts through electrostatic friction with the carpet.",
        "Double glazing turns incoming cold air into pure hydrogen gas."
    ]
    rng.shuffle(options)
    sol = (
        f"**Window Heat Loss Prevention:**\n"
        f"1. **Double glazing:** Two sheets of glass separated by a sealed $12-16\\text{{ mm}}$ gap of still air or argon gas. The stationary gas is a poor conductor, cutting conductive heat loss by ~50%.\n"
        f"2. **Pelmets on curtains:** Without a pelmet, warm room air enters the top of the curtain, cools against the glass, and sinks out the bottom, creating a rapid chilling convection loop. A pelmet seals the top and stops this loop.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_24_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "24_thermal_curtains_pelmets_and_double_glazing",
        "question_family_id": "24_thermal_curtains_pelmets_and_double_glazing",
        "hints": {
            "tier_1": "What do pelmets stop at the top of the curtain?",
            "tier_2": "Pelmets stop the air convection loop behind curtains; double glazing traps still air.",
            "tier_3": "Double-glazing traps still air, and pelmets stop cold downward convection behind curtains."
        },
        "misconception_tags": ["curtains_only_for_privacy"]
    }


def arch_25_shading_with_deciduous_trees_seasonal_benefit(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In eco-friendly architectural landscape design, planting **deciduous trees** (trees that shed their leaves in autumn) on the North and West sides of a South African home is widely encouraged.\n\n"
        f"Why are deciduous trees superior to evergreen trees for natural seasonal thermal control?"
    )
    correct_opt = "Their full leafy canopy provides cooling shade against intense summer solar radiation, while their bare branches in winter allow warm sunshine to penetrate through windows."
    options = [
        correct_opt,
        "Deciduous trees pump hot water from their roots into the home's plumbing during July.",
        "Evergreen trees attract lightning bolts that destroy household electrical insulation.",
        "Deciduous leaves absorb all atmospheric carbon monoxide and turn it into hot steam."
    ]
    rng.shuffle(options)
    sol = (
        f"**Seasonal Shading with Deciduous Trees:**\n"
        f"- In **summer**: The tree has dense, full foliage that blocks direct radiant sunlight, keeping walls and windows cool and lowering air conditioning loads.\n"
        f"- In **winter**: The leaves fall off, leaving bare branches that allow ~70-80% of winter solar radiation to reach windows, providing free natural solar space heating.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_25_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "25_shading_with_deciduous_trees_seasonal_benefit",
        "question_family_id": "25_shading_with_deciduous_trees_seasonal_benefit",
        "hints": {
            "tier_1": "What do deciduous trees do in summer vs winter?",
            "tier_2": "Leaves shade in summer; bare branches let winter sun through.",
            "tier_3": "Leafy canopy shades in summer; bare branches let warm sun in during winter."
        },
        "misconception_tags": ["trees_block_light_equally_all_year"]
    }
