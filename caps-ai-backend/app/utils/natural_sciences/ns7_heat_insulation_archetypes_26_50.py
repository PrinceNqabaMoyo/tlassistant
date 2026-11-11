"""Grade 7 Natural Sciences: Term 3 - Heat Insulation and Energy Saving Archetypes (26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/04. Heat insulation and energy saving.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List


def arch_26_thermal_mass_of_concrete_and_stone_floors(rng: random.Random) -> Dict[str, Any]:
    flooring = rng.choice(["dark slate stone tiles", "polished concrete slab", "clay quarry tiles"])
    prompt = (
        f"In passive solar homes, north-facing living rooms often feature {flooring} directly exposed to winter sunlight.\n\n"
        f"How does high thermal mass in the floor help keep the home comfortable day and night?"
    )
    correct_opt = "The dense floor absorbs solar heat during sunny daytime hours without overheating the room, then slowly radiates this stored heat into the living space at night."
    options = [
        correct_opt,
        "The stone generates new electrical power when illuminated by light.",
        "The dense floor acts as a vacuum pump that draws cold air into the foundations.",
        "Concrete contains chemical batteries that dissolve in the summer."
    ]
    rng.shuffle(options)
    sol = (
        f"**Thermal Mass Operation in Floors:**\n"
        f"1. Dense materials like stone, concrete, or tile have high heat capacity.\n"
        f"2. During winter days, low-angle sunlight strikes the floor, which absorbs large amounts of heat slowly, preventing the room air from overheating.\n"
        f"3. At night, as room temperature drops, the warm floor radiates its stored thermal energy back into the room.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_26_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "26_thermal_mass_of_concrete_and_stone_floors",
        "question_family_id": "26_thermal_mass_of_concrete_and_stone_floors",
        "hints": {
            "tier_1": "What does a heavy floor do with daytime heat?",
            "tier_2": "It absorbs heat during the day and radiates it back at night.",
            "tier_3": "The dense floor absorbs heat during the day and radiates stored heat into the room at night."
        },
        "misconception_tags": ["thermal_mass_heats_instantly"]
    }


def arch_27_white_reflective_cool_roof_technology(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In hot climates (such as the Northern Cape and Limpopo), municipal energy programs promote painting roofs with specialised reflective white 'cool roof' coatings.\n\n"
        f"What is the thermal physics benefit of a white reflective roof compared to a dark grey or black roof?"
    )
    correct_opt = "A white roof reflects up to 80% of solar radiation rather than absorbing it, drastically lowering roof surface temperatures and reducing indoor cooling electricity usage."
    options = [
        correct_opt,
        "White paint conducts coldness from outer space directly through the ceiling.",
        "White roof paint turns raindrops into solid ice cubes during the day.",
        "Dark roofs reflect more light than white roofs because dark colours repel radiation."
    ]
    rng.shuffle(options)
    sol = (
        f"**Cool Roof Reflectivity:**\n"
        f"- Light-coloured and white surfaces have high solar reflectance (albedo).\n"
        f"- A dark roof absorbs over 90% of solar radiation, heating up to $>65^\\circ\\text{{C}}$, which conducts directly into the building.\n"
        f"- A cool white roof reflects 70-85% of solar radiation, staying close to ambient air temperature and reducing cooling electricity loads by up to 30%.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_27_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "27_white_reflective_cool_roof_technology",
        "question_family_id": "27_white_reflective_cool_roof_technology",
        "hints": {
            "tier_1": "Do light colours absorb or reflect solar radiation?",
            "tier_2": "White reflects solar radiation, keeping the roof much cooler.",
            "tier_3": "A white roof reflects up to 80% of solar radiation, lowering roof surface temperature."
        },
        "misconception_tags": ["dark_roofs_stay_cooler"]
    }


def arch_28_draught_proofing_doors_and_windows(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Installing rubber self-adhesive weather-strips around door frames and using fabric 'door snakes' along the bottom edge of external doors is an inexpensive energy-saving measure.\n\n"
        f"Which heat loss mechanism does draught-proofing directly target and prevent?"
    )
    correct_opt = "Convection: it blocks air infiltration and leaks, preventing cold outdoor air from blowing in and warm heated indoor air from escaping."
    options = [
        correct_opt,
        "Radiation: it reflects ultraviolet light back into the garden.",
        "Nuclear decay: it blocks radioactive particles from penetrating wooden doors.",
        "Conduction: it converts solid wood into an electrical superconductor."
    ]
    rng.shuffle(options)
    sol = (
        f"**Draught Proofing Physics:**\n"
        f"- Cold wind blowing through gaps under doors and around window frames is direct convective air exchange (**infiltration**).\n"
        f"- Draught-proofing seals physical gaps, halting unwanted convective air movement.\n"
        f"- This preserves warm air produced by indoor heating appliances without wasteful leakage.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_28_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "28_draught_proofing_doors_and_windows",
        "question_family_id": "28_draught_proofing_doors_and_windows",
        "hints": {
            "tier_1": "What kind of heat transfer is moving drafts of cold wind?",
            "tier_2": "Moving air currents are convection.",
            "tier_3": "Convection: it blocks air infiltration and leaks."
        },
        "misconception_tags": ["drafts_are_conductive_losses"]
    }


def arch_29_animal_insulation_fur_feathers_and_blubber(rng: random.Random) -> Dict[str, Any]:
    animals = [
        ("Arctic polar bears", "a thick layer of blubber under the skin and dense fur that traps a layer of warm air", "extremely cold ice and freezing water"),
        ("Southern right whales", "a thick layer of fat blubber up to 50 cm thick under their skin", "the frigid waters of the Southern Ocean"),
        ("African sheep", "a thick fleece of crimped wool fibres that trap vast amounts of dead air", "freezing winter nights on the Karoo highveld")
    ]
    animal, adaptation, habitat = rng.choice(animals)
    prompt = (
        f"In biology and natural sciences, animals surviving in harsh thermal environments have evolved specialised adaptations. "
        f"For example, **{animal}** survive in **{habitat}**.\n\n"
        f"How does their thermal adaptation ({adaptation}) protect their internal body temperature?"
    )
    correct_opt = "It acts as a powerful thermal insulator with low conductivity, drastically slowing the rate of conductive and convective heat transfer from their warm core to the cold environment."
    options = [
        correct_opt,
        "It generates infinite chemical energy without needing food or oxygen.",
        "It turns the animal's outer skin completely cold so that heat cannot exist.",
        "It converts freezing water into boiling steam on contact with the skin."
    ]
    rng.shuffle(options)
    sol = (
        f"**Biological Thermal Insulation:**\n"
        f"- Warm-blooded endotherms must maintain constant core temperature ($37-39^\\circ\\text{{C}}$).\n"
        f"- Subcutaneous blubber (fat) has very low thermal conductivity and poor blood circulation, acting as an internal barrier.\n"
        f"- Fur, wool, and feathers trap a boundary layer of motionless air against the skin, preventing cold winds from stripping heat away by convection.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_29_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "29_animal_insulation_fur_feathers_and_blubber",
        "question_family_id": "29_animal_insulation_fur_feathers_and_blubber",
        "hints": {
            "tier_1": "How do fur and blubber slow down heat loss?",
            "tier_2": "They have low thermal conductivity and trap air, slowing heat transfer.",
            "tier_3": "They act as thermal insulators with low conductivity, slowing heat loss to the cold surroundings."
        },
        "misconception_tags": ["animals_produce_unlimited_heat"]
    }


def arch_30_penguin_feather_density_and_down_layer(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"African penguins (in Simon's Town and Boulders Beach) and Antarctic penguins possess up to 30 to 40 short, stiff, overlapping feathers per square centimetre, underlain by a fluffy down layer.\n\n"
        f"What dual thermal function do these specialized feathers perform when swimming in cold ocean water?"
    )
    correct_opt = "The oily, overlapping outer feathers create a waterproof seal that locks out cold ocean water, while the fluffy down layer underneath traps an insulating layer of dry warm air against the skin."
    options = [
        correct_opt,
        "The feathers conduct cold seawater directly to the internal organs to keep the penguin cool.",
        "The feathers produce heat by vibrating at ultrasonic speeds under water.",
        "Feathers dissolve in cold water and regrow immediately upon exiting."
    ]
    rng.shuffle(options)
    sol = (
        f"**Penguin Feather Insulation Mechanics:**\n"
        f"1. Water conducts heat roughly 25 times faster than air; if cold water touches the skin, the bird rapidly suffers hypothermia.\n"
        f"2. Outer contour feathers overlap like roof shingles and are coated in preening oil, forming an impermeable, waterproof barrier.\n"
        f"3. Beneath the waterproof outer coat, fluffy down plumage traps a protective blanket of dry air directly against the body.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_30_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "30_penguin_feather_density_and_down_layer",
        "question_family_id": "30_penguin_feather_density_and_down_layer",
        "hints": {
            "tier_1": "Why is it vital that cold water never touches the penguin's skin?",
            "tier_2": "Water conducts heat rapidly; feathers seal out water and trap dry air.",
            "tier_3": "Outer feathers seal out cold water, while inner down traps an insulating layer of dry air."
        },
        "misconception_tags": ["wet_feathers_insulate_well"]
    }


def arch_31_human_goosebumps_piloerection_evolutionary_purpose(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When humans are exposed to sudden cold air, tiny arrector pili muscles in the skin contract involuntarily, causing hair follicles to stand upright ('goosebumps' or piloerection).\n\n"
        f"What is the evolutionary biological purpose of this reflex in mammals?"
    )
    correct_opt = "Erecting hairs or fur traps a thicker boundary layer of stationary air close to the skin, enhancing thermal insulation and reducing convective heat loss."
    options = [
        correct_opt,
        "Goosebumps act as radio antennas to transmit emergency SOS signals to other humans.",
        "Hair erection forces cold blood out of the body through the hair shafts.",
        "Goosebumps produce sparks of static electricity that warm the skin."
    ]
    rng.shuffle(options)
    sol = (
        f"**Biological Function of Piloerection:**\n"
        f"- In furry mammals, piloerection increases the depth of the fur coat, trapping a deeper, thicker layer of motionless air against the skin.\n"
        f"- This significantly boosts thermal resistance, cutting convective heat loss.\n"
        f"- In humans (who have evolved sparse body hair), goosebumps are a vestigial evolutionary reflex inherited from our fur-covered mammalian ancestors.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_31_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "31_human_goosebumps_piloerection_evolutionary_purpose",
        "question_family_id": "31_human_goosebumps_piloerection_evolutionary_purpose",
        "hints": {
            "tier_1": "What does standing hair trap in furry animals?",
            "tier_2": "It traps a thicker layer of still air next to the skin.",
            "tier_3": "Erecting hairs traps a thicker layer of stationary air, increasing insulation."
        },
        "misconception_tags": ["goosebumps_generate_heat"]
    }


def arch_32_thermos_flask_as_insulation_case_study(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A Thermos vacuum flask is the ultimate example of thermal insulation engineering because it addresses all three heat transfer pathways simultaneously.\n\n"
        f"Which matching correctly pairs each design feature with the primary heat transfer pathway it restricts?"
    )
    correct_opt = "Vacuum gap: Conduction & Convection | Silvered interior: Radiation | Plastic/cork stopper: Convection & Evaporation"
    options = [
        correct_opt,
        "Vacuum gap: Radiation only | Silvered interior: Conduction | Stopper: Sound waves",
        "Vacuum gap: Nuclear fission | Silvered interior: Convection | Stopper: Radiation",
        "All three parts restrict only conduction and have zero effect on radiation or convection"
    ]
    rng.shuffle(options)
    sol = (
        f"**Thermos Flask 3-Way Insulation Architecture:**\n"
        f"1. **Vacuum gap between double walls:** No particles -> prevents **Conduction** and **Convection** across the walls.\n"
        f"2. **Silvered mirror walls:** High reflectivity / low emissivity -> prevents **Radiation** heat transfer.\n"
        f"3. **Tightly fitted insulated stopper:** Blocks **Convection** of warm air and prevents heat loss through **evaporation**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_32_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "32_thermos_flask_as_insulation_case_study",
        "question_family_id": "32_thermos_flask_as_insulation_case_study",
        "hints": {
            "tier_1": "What does vacuum block? What do silver surfaces block? What does the stopper block?",
            "tier_2": "Vacuum blocks conduction/convection; silver blocks radiation; stopper blocks air/evaporation.",
            "tier_3": "Vacuum gap: Conduction & Convection | Silvered interior: Radiation | Stopper: Convection & Evaporation."
        },
        "misconception_tags": ["vacuum_stops_radiation"]
    }


def arch_33_comparing_energy_consumption_insulated_vs_uninsulated_home(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Two identical houses (House A with ceiling insulation, geyser blanket, and shaded windows; House B completely uninsulated) are monitored over a cold winter month in Gauteng.\n\n"
        f"What significant differences in energy consumption and indoor comfort will be measured?"
    )
    correct_opt = "House A consumes 40% to 60% less electrical heating energy while maintaining a stable, comfortable indoor temperature; House B experiences severe temperature swings and high electricity bills."
    options = [
        correct_opt,
        "House B consumes less energy because uninsulated roofs absorb electricity directly from thunderstorms.",
        "Both houses record identical electricity consumption because insulation does not affect thermal efficiency.",
        "House A becomes uninhabitably hot at -5 °C because insulation creates uncontrollable heat."
    ]
    rng.shuffle(options)
    sol = (
        f"**Comparative Energy Audit:**\n"
        f"- Up to 40% of heat loss in a typical home occurs through an uninsulated roof/ceiling.\n"
        f"- An insulated home (House A) retains internal warmth for many hours, requiring heaters to run only intermittently.\n"
        f"- An uninsulated home (House B) loses heat as fast as heaters can generate it, leading to continuous heater operation, massive electricity bills, and poor comfort.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_33_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "33_comparing_energy_consumption_insulated_vs_uninsulated_home",
        "question_family_id": "33_comparing_energy_consumption_insulated_vs_uninsulated_home",
        "hints": {
            "tier_1": "Which house uses much less electricity for heating?",
            "tier_2": "House A uses 40-60% less energy due to ceiling and geyser insulation.",
            "tier_3": "House A consumes 40% to 60% less electrical heating energy while staying comfortable."
        },
        "misconception_tags": ["insulation_has_no_financial_impact"]
    }


def arch_34_calculating_electricity_cost_savings_from_geyser_insulation(rng: random.Random) -> Dict[str, Any]:
    monthly_kwh_save = rng.choice([50, 60, 75, 100])
    cost_per_kwh = rng.choice([2, 3])
    monthly_rand_save = monthly_kwh_save * cost_per_kwh
    annual_rand_save = monthly_rand_save * 12
    blanket_cost = rng.choice([300, 350, 400])
    payback_months = round(blanket_cost / monthly_rand_save, 1)
    payback_str = f"{payback_months}".replace(".", "{,}")
    prompt = (
        f"A family installs a geyser blanket costing R{blanket_cost}. The blanket saves {monthly_kwh_save} kWh of electricity each month. "
        f"If electricity costs R{cost_per_kwh} per kWh, how much money does the family save per year, and roughly how long is the financial payback period?"
    )
    correct_opt = f"Annual savings: R{annual_rand_save} per year | Payback period: ~{payback_str} months"
    options = [
        correct_opt,
        f"Annual savings: R{monthly_rand_save} per year | Payback period: ~12 months",
        f"Annual savings: R{annual_rand_save * 2} per year | Payback period: ~24 months",
        f"Annual savings: R{monthly_kwh_save} per year | Payback period: ~100 months"
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1: Calculate monthly financial savings:**\n"
        f"$$\\text{{Monthly savings}} = {monthly_kwh_save}\\text{{ kWh}} \\times \\text{{R}}{cost_per_kwh}\\text{{/kWh}} = \\text{{R}}{monthly_rand_save}\\text{{/month}}$$\n\n"
        f"**Step 2: Calculate annual savings:**\n"
        f"$$\\text{{Annual savings}} = \\text{{R}}{monthly_rand_save} \\times 12 = \\text{{R}}{annual_rand_save}\\text{{/year}}$$\n\n"
        f"**Step 3: Calculate payback period:**\n"
        f"$$\\text{{Payback}} = \\frac{{\\text{{R}}{blanket_cost}}}{{\\text{{R}}{monthly_rand_save}\\text{{/month}}}} \\approx {payback_str}\\text{{ months}}$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_34_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "34_calculating_electricity_cost_savings_from_geyser_insulation",
        "question_family_id": "34_calculating_electricity_cost_savings_from_geyser_insulation",
        "hints": {
            "tier_1": "Multiply saved kWh by cost per kWh, then multiply by 12 for the year.",
            "tier_2": f"Monthly = R{monthly_rand_save}; Annual = R{annual_rand_save}.",
            "tier_3": f"Annual savings: R{annual_rand_save} | Payback: ~{payback_str} months."
        },
        "misconception_tags": ["arithmetic_payback_error"]
    }


def arch_35_calculating_temperature_retention_over_time(rng: random.Random) -> Dict[str, Any]:
    t_start = 90
    t_ins = rng.choice([76, 78, 80])
    t_unins = rng.choice([40, 44, 48])
    mins = 30
    drop_ins = t_start - t_ins
    drop_unins = t_start - t_unins
    prompt = (
        f"Two flasks are filled with boiling water at {t_start} °C. Flask 1 is well-insulated, while Flask 2 is uninsulated. "
        f"After {mins} minutes, Flask 1 is at {t_ins} °C, while Flask 2 has dropped to {t_unins} °C.\n\n"
        f"How much less temperature drop was experienced by the insulated flask compared to the uninsulated flask?"
    )
    diff = drop_unins - drop_ins
    correct_opt = f"{diff} °C less temperature drop"
    options = [
        correct_opt,
        f"{drop_ins} °C less temperature drop",
        f"{drop_unins} °C less temperature drop",
        f"{diff + 10} °C less temperature drop"
    ]
    options = list(dict.fromkeys(options))
    while len(options) < 4:
        options.append(f"{rng.randint(5, 45)} °C less temperature drop")
    rng.shuffle(options)
    sol = (
        f"**Step 1: Calculate drop in insulated Flask 1:**\n"
        f"$$\\Delta T_1 = {t_start}^\\circ\\text{{C}} - {t_ins}^\\circ\\text{{C}} = {drop_ins}^\\circ\\text{{C}}$$\n\n"
        f"**Step 2: Calculate drop in uninsulated Flask 2:**\n"
        f"$$\\Delta T_2 = {t_start}^\\circ\\text{{C}} - {t_unins}^\\circ\\text{{C}} = {drop_unins}^\\circ\\text{{C}}$$\n\n"
        f"**Step 3: Difference in drop:**\n"
        f"$$\\text{{Difference}} = {drop_unins}^\\circ\\text{{C}} - {drop_ins}^\\circ\\text{{C}} = {diff}^\\circ\\text{{C}}$$\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_35_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "35_calculating_temperature_retention_over_time",
        "question_family_id": "35_calculating_temperature_retention_over_time",
        "hints": {
            "tier_1": "Find the temperature drop for both flasks and subtract them.",
            "tier_2": f"Flask 1 drop = {drop_ins} °C; Flask 2 drop = {drop_unins} °C.",
            "tier_3": f"{drop_unins} - {drop_ins} = {diff} °C."
        },
        "misconception_tags": ["subtracting_wrong_temperatures"]
    }


def arch_36_environmental_benefit_reducing_coal_power_demand(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In South Africa, over 80% of national electricity is generated by burning low-grade coal in thermal power stations (such as Medupi and Kusile in Mpumalanga).\n\n"
        f"How does widespread installation of home thermal insulation (ceilings, geyser blankets) protect the environment?"
    )
    correct_opt = "By reducing domestic electricity demand for space heating and water heating, fewer tonnes of coal must be burned, directly reducing air pollution, water consumption, and ash waste."
    options = [
        correct_opt,
        "Ceiling insulation absorbs coal smoke directly from power station smokestacks through magnetic attraction.",
        "Insulating homes eliminates the need for power lines by generating solar electricity in the ceiling.",
        "Insulation chemically turns coal into renewable nuclear fuel."
    ]
    rng.shuffle(options)
    sol = (
        f"**Environmental Connection to Thermal Insulation:**\n"
        f"1. Coal combustion produces massive emissions of carbon dioxide ($CO_2$), sulphur dioxide ($SO_2$), nitrogen oxides ($NO_x$), and particulates.\n"
        f"2. Water heating and space heating account for over 50% of residential electricity consumption in South Africa.\n"
        f"3. Installing thermal insulation lowers peak and baseload electrical demand.\n"
        f"4. Less electricity demanded = less coal combusted = reduced air pollution and acid rain.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_36_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "36_environmental_benefit_reducing_coal_power_demand",
        "question_family_id": "36_environmental_benefit_reducing_coal_power_demand",
        "hints": {
            "tier_1": "Where does South African electricity come from?",
            "tier_2": "Coal power plants. Less power used = less coal burned.",
            "tier_3": "Reduces electricity demand for heating, meaning less coal burned at power stations."
        },
        "misconception_tags": ["insulation_unrelated_to_environment"]
    }


def arch_37_reducing_greenhouse_gas_emissions_via_insulation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A national energy audit reports that insulating 1 million homes in South Africa prevents the release of over 2 million tonnes of carbon dioxide ($CO_2$) greenhouse gas into the atmosphere each year.\n\n"
        f"What is the connection between home thermal insulation and global climate change mitigation?"
    )
    correct_opt = "Insulation reduces the need for fossil-fuel-generated heating electricity, cutting emissions of carbon dioxide which traps infrared radiation in the global atmosphere."
    options = [
        correct_opt,
        "Insulating blankets directly destroy atmospheric ozone molecules to cool the planet.",
        "Insulation creates an artificial magnetic field that repels the Sun's cosmic rays.",
        "Ceiling batts absorb greenhouse gases from the sky like a giant air filter."
    ]
    rng.shuffle(options)
    sol = (
        f"**Climate Change & Insulation:**\n"
        f"- Carbon dioxide ($CO_2$) is the primary greenhouse gas driving anthropogenic global climate change.\n"
        f"- Every kilowatt-hour (kWh) of electricity generated on the South African grid emits ~1 kg of $CO_2$.\n"
        f"- Thermal insulation provides permanent, passive energy conservation with zero operational emissions.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_37_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "37_reducing_greenhouse_gas_emissions_via_insulation",
        "question_family_id": "37_reducing_greenhouse_gas_emissions_via_insulation",
        "hints": {
            "tier_1": "How does using less coal power reduce carbon dioxide emissions?",
            "tier_2": "Less electricity used means less carbon dioxide emitted into the atmosphere.",
            "tier_3": "Insulation cuts fossil fuel electricity demand, lowering greenhouse gas emissions."
        },
        "misconception_tags": ["co2_absorbed_by_ceiling"]
    }


def arch_38_energy_star_and_appliance_efficiency_labels(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In South African retail appliance stores, new refrigerators and washing machines display mandatory energy efficiency rating labels with letter grades from **A+++** down to **D**.\n\n"
        f"What does an **A+++** energy rating label signify to a consumer comparing two refrigerators of identical physical size?"
    )
    correct_opt = "The A+++ model is engineered with superior thermal insulation and high-efficiency compressors, consuming significantly fewer kilowatt-hours (kWh) of electricity per year."
    options = [
        correct_opt,
        "The A+++ model freezes food instantly to absolute zero (-273,15 °C).",
        "The A+++ model generates its own electricity and can power other appliances in the kitchen.",
        "The A+++ label indicates the appliance is painted with radioactive fluorescent paint."
    ]
    rng.shuffle(options)
    sol = (
        f"**Energy Efficiency Labeling:**\n"
        f"- Appliance rating labels (A+++ to D) inform consumers about relative energy efficiency.\n"
        f"- An A+++ refrigerator has thicker, higher-grade cyclopentane insulation foam and an inverter compressor.\n"
        f"- It minimizes heat leakage from the kitchen into the cold compartment, using up to 50-70% less electricity than a D-rated unit.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_38_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "38_energy_star_and_appliance_efficiency_labels",
        "question_family_id": "38_energy_star_and_appliance_efficiency_labels",
        "hints": {
            "tier_1": "Does A+++ mean high energy waste or high energy efficiency?",
            "tier_2": "A+++ represents superior insulation and lower annual electricity consumption.",
            "tier_3": "The A+++ model has superior insulation and uses significantly fewer kWh of electricity."
        },
        "misconception_tags": ["all_appliances_use_same_power"]
    }


def arch_39_efficient_cooking_pot_lids_and_matching_plate_sizes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In household cooking efficiency guides, two simple rules are emphasized:\n"
        f"1. Always keep a tight-fitting lid on the cooking pot.\n"
        f"2. Match the diameter of the pot base to the diameter of the stove spiral or hotplate.\n\n"
        f"What thermal physics rationale justifies both practices?"
    )
    correct_opt = "A tight lid prevents heat loss from escaping steam and convection; matching plate size ensures direct conductive contact without radiant and convective heat escaping around the sides."
    options = [
        correct_opt,
        "The lid magnetises the stew while the plate size regulates municipal voltage.",
        "Leaving the lid off cools the room while a smaller pot absorbs microwaves from the air.",
        "Both rules are purely cosmetic traditions with zero effect on thermal energy."
    ]
    rng.shuffle(options)
    sol = (
        f"**Cooking Energy Efficiency Principles:**\n"
        f"1. **Putting a lid on the pot:** Evaporation of water takes massive latent heat ($2260\\text{{ J/g}}$). A lid stops steam and convective air currents from carrying away heat, cooking food faster with less power.\n"
        f"2. **Matching plate diameter:** If a small pot is placed on a large hotplate, the exposed heated ring wastes thermal energy directly into kitchen air via radiation and convection.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_39_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "39_efficient_cooking_pot_lids_and_matching_plate_sizes",
        "question_family_id": "39_efficient_cooking_pot_lids_and_matching_plate_sizes",
        "hints": {
            "tier_1": "What escapes when the lid is off, and what is wasted if the plate is too big?",
            "tier_2": "Lid blocks steam/convection loss; matching plate stops heat wasting around sides.",
            "tier_3": "Lid stops steam and convection; matching plate size avoids heat leaking around sides."
        },
        "misconception_tags": ["lid_does_not_save_energy"]
    }


def arch_40_efficient_electric_kettle_water_volume_usage(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner boils a full $1{{,}}7\\text{{ litre}}$ kettle of water just to make one single $250\\text{{ cm}}^3$ mug of instant coffee.\n\n"
        f"Why is this habit thermally inefficient and wasteful of electrical energy?"
    )
    correct_opt = "Thermal energy required is directly proportional to mass ($Q = mc\\Delta T$); heating 1,7 L takes almost seven times more electrical energy and time than heating only the 250 mL needed, wasting heat as the leftover water cools down unused."
    options = [
        correct_opt,
        "Kettles consume the exact same amount of electrical Joules regardless of how much water is inside.",
        "Boiling a full kettle generates harmful ozone gas that destroys the kitchen ceiling.",
        "Water boiled in large quantities loses all of its oxygen atoms permanently."
    ]
    rng.shuffle(options)
    sol = (
        f"**Energy Consumption in Water Heating:**\n"
        f"1. Energy required: $Q = mc\\Delta T$, where $m$ is the mass of water.\n"
        f"2. Heating $1{{,}}7\\text{{ kg}}$ of water requires $\\approx 7$ times more electrical energy than heating $0{{,}}25\\text{{ kg}}$.\n"
        f"3. The unused $1{{,}}45\\text{{ L}}$ of boiling water sits in the kettle and cools back down to room temperature, dissipating all that purchased electrical energy into the kitchen as wasted heat.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_40_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "40_efficient_electric_kettle_water_volume_usage",
        "question_family_id": "40_efficient_electric_kettle_water_volume_usage",
        "hints": {
            "tier_1": "Does boiling more water require more or less energy?",
            "tier_2": "Energy needed is proportional to water mass (Q = mcΔT).",
            "tier_3": "Heating 1,7 L takes ~7 times more energy than 250 mL, wasting heat as leftover water cools."
        },
        "misconception_tags": ["boiling_volume_does_not_matter"]
    }


def arch_41_refrigerator_door_seal_maintenance_and_efficiency(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A common home test for refrigerator efficiency is the 'banknote test': closing a paper banknote in the door seal. If the note pulls out easily without resistance, the magnetic gasket is worn out.\n\n"
        f"Why does a worn, leaking refrigerator door gasket cause electricity bills to rise?"
    )
    correct_opt = "Warm kitchen air enters continuously by convection and conduction, forcing the electric compressor motor to run much longer and more frequently to maintain cold temperatures."
    options = [
        correct_opt,
        "The loose seal allows refrigerator magnetism to drain out into the floor tiles.",
        "Cold air has negative charge that attracts dust which breaks the electrical plug.",
        "A leaking seal generates high-frequency radiation that spins the home electricity meter backwards."
    ]
    rng.shuffle(options)
    sol = (
        f"**Refrigerator Door Gasket Mechanics:**\n"
        f"- Refrigerator gaskets contain flexible magnetic strips that create an airtight thermal seal.\n"
        f"- When the seal perishes, gaps allow warm, humid room air to infiltrate by **convection**.\n"
        f"- Thermal energy transfers into the compartment, causing internal temperatures to rise.\n"
        f"- The internal thermostat triggers the compressor to run continually, consuming excessive electrical kilowatt-hours.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_41_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "41_refrigerator_door_seal_maintenance_and_efficiency",
        "question_family_id": "41_refrigerator_door_seal_maintenance_and_efficiency",
        "hints": {
            "tier_1": "What happens when warm kitchen air leaks into a cold fridge?",
            "tier_2": "The compressor has to run constantly to remove the invading heat.",
            "tier_3": "Warm room air enters by convection, forcing the compressor to run longer and more frequently."
        },
        "misconception_tags": ["fridge_seals_only_keep_door_closed"]
    }


def arch_42_insulation_in_clothing_layering_principle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Outdoor hikers and mountaineers in the Drakensberg mountains wear multiple thin layers of clothing rather than one single heavy, thick jacket in freezing conditions.\n\n"
        f"What thermal insulation advantage does wearing multiple thin layers provide?"
    )
    correct_opt = "Multiple layers trap multiple thin cushions of stationary air between each fabric layer, providing superior overall thermal resistance and preventing convective air circulation."
    options = [
        correct_opt,
        "Multiple layers generate chemical friction that produces nuclear heat between the garments.",
        "Wearing several shirts attracts cosmic solar rays through clothes.",
        "A single thick jacket destroys trapped air while thin layers produce oxygen."
    ]
    rng.shuffle(options)
    sol = (
        f"**Layering Principle in Thermal Insulation:**\n"
        f"1. Stationary air is one of the most effective thermal insulators known ($k \\approx 0{{,}}026\\text{{ W/m·K}}$).\n"
        f"2. Three thin garments trap two distinct layers of dead air between them in addition to the air trapped in the fabric weave.\n"
        f"3. This multi-barrier configuration drastically reduces conductive and convective heat dissipation.\n"
        f"4. It also allows flexible regulation (shedding a layer when sweating to avoid conductive heat loss from damp clothing).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_42_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "42_insulation_in_clothing_layering_principle",
        "question_family_id": "42_insulation_in_clothing_layering_principle",
        "hints": {
            "tier_1": "What gets trapped between multiple layers of fabric?",
            "tier_2": "Multiple layers trap multiple blankets of still air.",
            "tier_3": "Multiple layers trap multiple cushions of stationary air between fabric layers."
        },
        "misconception_tags": ["one_thick_coat_always_superior"]
    }


def arch_43_down_feather_jackets_versus_compacted_cotton(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A goose-down puffer jacket is extremely lightweight and puffy yet keeps the wearer warmer than a heavy, dense cotton canvas overcoat.\n\n"
        f"Why is lofty down feather filling thermally superior to dense, compacted cotton fabric?"
    )
    correct_opt = "Lofty down filaments have a high volume-to-weight ratio and trap massive amounts of dead air, whereas dense compacted cotton has few air spaces and conducts heat away faster."
    options = [
        correct_opt,
        "Goose feathers generate active metabolic heat because geese are warm-blooded birds.",
        "Cotton absorbs all heat from the body and converts it into water vapour.",
        "Down feathers are made of metallic gold fibres that reflect all radiation."
    ]
    rng.shuffle(options)
    sol = (
        f"**Down vs Compacted Fabric:**\n"
        f"- Thermal insulation depends on the volume of **trapped still air**, not the weight or density of the solid material.\n"
        f"- Down feathers have millions of microscopic criss-crossing plumules that expand (loft) to trap huge volumes of air with minimal solid mass.\n"
        f"- Dense cotton is heavy and tightly packed with few air pockets, allowing heat to conduct through solid cellulose fibres much more readily.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_43_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "43_down_feather_jackets_versus_compacted_cotton",
        "question_family_id": "43_down_feather_jackets_versus_compacted_cotton",
        "hints": {
            "tier_1": "Does insulation depend on weight or volume of trapped air?",
            "tier_2": "Insulation depends on trapped air, not the weight of the fabric.",
            "tier_3": "Lofty down traps massive amounts of dead air compared to dense cotton."
        },
        "misconception_tags": ["heavier_clothing_is_always_warmer"]
    }


def arch_44_fire_safety_considerations_with_thermal_insulators(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When choosing thermal ceiling insulation for homes, building regulators strictly assess **fire safety ratings** (such as non-combustibility and smoke emission).\n\n"
        f"Why is fire safety a critical consideration when installing ceiling insulation materials?"
    )
    correct_opt = "Ceiling spaces house electrical wiring, downlights, and potential fire hazards; flammable insulating materials can ignite and rapidly spread toxic flames and smoke throughout the entire building."
    options = [
        correct_opt,
        "All thermal insulators spontaneously explode if the outdoor temperature exceeds 25 °C.",
        "Building codes require all ceilings to be filled with gunpowder for pest control.",
        "Fire-retardant materials prevent coldness from entering through the roof tiles."
    ]
    rng.shuffle(options)
    sol = (
        f"**Fire Safety and Building Insulation Standards:**\n"
        f"1. Ceiling cavities contain heat sources: recessed halogen/LED downlights, electrical junction boxes, transformers, and wiring.\n"
        f"2. Highly flammable untreated materials (like plain expanded polystyrene or untreated sawdust/paper) pose severe fire propagation hazards.\n"
        f"3. Building codes (SANS 10400-T) require non-combustible materials (mineral glass wool, rock wool) or cellulose treated with fire-retardant borate salts to prevent rapid fire spread.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_44_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "44_fire_safety_considerations_with_thermal_insulators",
        "question_family_id": "44_fire_safety_considerations_with_thermal_insulators",
        "hints": {
            "tier_1": "What heat sources exist in ceiling spaces?",
            "tier_2": "Electrical wiring and downlights can ignite flammable insulation.",
            "tier_3": "Flammable insulation can ignite from electrical wiring/lights and rapidly spread fire."
        },
        "misconception_tags": ["thermal_insulators_are_all_fireproof"]
    }


def arch_45_misconception_insulators_only_keep_things_warm_not_cold(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner says: *'Insulators are only useful for keeping hot things warm, like tea or blankets; they cannot keep cold things cold.'*\n\n"
        f"How should a science educator scientifically refute this statement?"
    )
    correct_opt = "Thermal insulators simply slow down the transfer of heat in whichever direction heat naturally flows; they keep cold drinks cold by preventing outside thermal energy from transferring inward."
    options = [
        correct_opt,
        "The learner is correct because insulators only contain positive heat particles.",
        "Insulators can only keep cold things cold if they are plugged into a 220V wall socket.",
        "Cold is an active energy that dissolves thermal insulation fibres."
    ]
    rng.shuffle(options)
    sol = (
        f"**Symmetrical Function of Thermal Insulators:**\n"
        f"- Heat transfer always flows from **hotter regions to cooler regions**.\n"
        f"- An insulator does not 'know' whether an object is hot or cold; it merely offers high resistance to heat conduction and convection.\n"
        f"- With a hot drink ($80^\\circ\\text{{C}}$ in $20^\\circ\\text{{C}}$ room): Insulator slows heat transfer *outward*.\n"
        f"- With an ice lolly ($-5^\\circ\\text{{C}}$ in $25^\\circ\\text{{C}}$ room): Insulator slows heat transfer *inward*.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_45_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "45_misconception_insulators_only_keep_things_warm_not_cold",
        "question_family_id": "45_misconception_insulators_only_keep_things_warm_not_cold",
        "hints": {
            "tier_1": "Does a cooler box have insulation?",
            "tier_2": "Yes. Insulators slow heat transfer in either direction.",
            "tier_3": "Insulators slow heat transfer in either direction; they keep cold things cold by stopping heat entry."
        },
        "misconception_tags": ["insulators_only_keep_things_warm"]
    }


def arch_46_misconception_insulators_produce_thermal_energy(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner places a winter blanket around a cold bottle of soda at $4^\\circ\\text{{C}}$ and expects the blanket to 'warm the soda up to body temperature'.\n\n"
        f"Why will the blanket NOT warm the cold soda bottle?"
    )
    correct_opt = "A blanket is a passive thermal insulator that generates zero heat; without an internal heat source, it actually insulates the soda from the warmer room air and keeps it cold longer."
    options = [
        correct_opt,
        "The blanket is missing its chemical batteries which activate when wrapped around glass.",
        "The blanket cools the bottle down to freezing because fabric produces liquid nitrogen.",
        "Wool blankets only produce heat when placed on iron surfaces."
    ]
    rng.shuffle(options)
    sol = (
        f"**Clarification on Passive Insulation:**\n"
        f"1. A blanket is not a heater; it contains no chemical, electrical, or metabolic energy source.\n"
        f"2. When placed on a person, the person ($37^\\circ\\text{{C}}$) is the heat generator, and the blanket retards heat loss.\n"
        f"3. When wrapped around cold soda ($4^\\circ\\text{{C}}$), the blanket retards heat from the room entering the bottle, preserving its cold temperature.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_46_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "46_misconception_insulators_produce_thermal_energy",
        "question_family_id": "46_misconception_insulators_produce_thermal_energy",
        "hints": {
            "tier_1": "Does a blanket generate heat on its own?",
            "tier_2": "Blankets do not produce heat; they only trap existing heat.",
            "tier_3": "A blanket generates zero heat; it actually keeps the cold soda cold longer."
        },
        "misconception_tags": ["blankets_generate_heat"]
    }


def arch_47_misconception_metals_cannot_be_insulated(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A student believes: *'Because metal is a conductor, covering a metal tank or pipe with an insulator is useless because heat will still escape through the metal anyway.'*\n\n"
        f"Why is this belief scientifically flawed?"
    )
    correct_opt = "Heat escaping from the metal must still pass through the outer insulating layer to reach the surroundings; the insulator provides a high-resistance barrier that restricts the entire heat flow."
    options = [
        correct_opt,
        "Insulating foam chemically converts metal atoms into non-metallic wood.",
        "Metals cease being conductors when placed inside darkness.",
        "Heat cannot travel through metal if the metal is painted with any colour."
    ]
    rng.shuffle(options)
    sol = (
        f"**Series Thermal Resistance:**\n"
        f"- In a copper pipe or steel geyser tank wrapped in foam, heat must travel in series:\n"
        f"  $$\\text{{Hot Water}} \\to \\text{{Metal Wall}} \\to \\text{{Insulation Foam}} \\to \\text{{Air}}$$\n"
        f"- The total thermal resistance is the sum of all layers: $R_\\text{{total}} = R_\\text{{metal}} + R_\\text{{insulation}}$.\n"
        f"- Even though $R_\\text{{metal}}$ is tiny, $R_\\text{{insulation}}$ is very large, drastically throttling the overall rate of heat escape.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_47_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "47_misconception_metals_cannot_be_insulated",
        "question_family_id": "47_misconception_metals_cannot_be_insulated",
        "hints": {
            "tier_1": "Can heat leave the metal if an insulating jacket surrounds it?",
            "tier_2": "Heat must pass through the insulator to escape to the outside air.",
            "tier_3": "Heat must still pass through the outer insulating barrier to reach the surroundings."
        },
        "misconception_tags": ["metals_cannot_be_insulated"]
    }


def arch_48_misconception_thicker_material_is_always_better_than_trapped_air(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A builder suggests using a $50\\text{{ mm}}$ solid concrete wall instead of a $25\\text{{ mm}}$ polystyrene foam board, claiming *'solid concrete is heavier and thicker, so it must insulate better.'*\n\n"
        f"How does the thermal conductivity of concrete compare to polystyrene, and which is the better thermal insulator?"
    )
    correct_opt = "Polystyrene is a vastly superior insulator because its thermal conductivity (k ~ 0,03 W/m·K) is roughly 50 times lower than solid concrete (k ~ 1,5 W/m·K); density and weight do not equal insulation."
    options = [
        correct_opt,
        "Concrete is 100 times better as an insulator because heavy rocks block heat waves completely.",
        "Both materials insulate identically because thickness is the only variable that matters.",
        "Polystyrene is a conductor of heat while concrete is an insulator."
    ]
    rng.shuffle(options)
    sol = (
        f"**Thermal Conductivity Comparison:**\n"
        f"- Concrete is dense and conducts heat relatively easily ($k \\approx 1{{,}}5\\text{{ W/m·K}}$).\n"
        f"- Polystyrene consists of 98% trapped stationary air bubbles ($k \\approx 0{{,}}03\\text{{ W/m·K}}$).\n"
        f"- A $25\\text{{ mm}}$ sheet of polystyrene provides roughly the same thermal resistance ($R$-value) as a $1250\\text{{ mm}}$ (1,25 metre!) thick concrete wall.\n"
        f"- Solid weight and density do not make an effective insulator.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_48_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "48_misconception_thicker_material_is_always_better_than_trapped_air",
        "question_family_id": "48_misconception_thicker_material_is_always_better_than_trapped_air",
        "hints": {
            "tier_1": "Which conducts heat slower: solid concrete or foamed polystyrene?",
            "tier_2": "Polystyrene has ~50 times lower thermal conductivity than concrete.",
            "tier_3": "Polystyrene is vastly superior because its conductivity is ~50 times lower than concrete."
        },
        "misconception_tags": ["density_equals_insulation"]
    }


def arch_49_designing_an_energy_efficient_house_in_south_africa(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"An architecture student enters a sustainable housing competition in South Africa. "
        f"Which package of design interventions achieves the highest energy efficiency rating for thermal comfort?"
    )
    correct_opt = "North-facing orientation, roof overhangs sized for seasonal sun, ceiling insulation (R > 3,7), geyser blanket with insulated pipes, and draught-sealed doors/windows."
    options = [
        correct_opt,
        "West-facing unshaded floor-to-ceiling glass, uninsulated corrugated iron roof, and open gaps under all doors.",
        "South-facing living rooms with black roof sheeting and no ceiling boards whatsoever.",
        "Sealing the building in solid lead sheets with zero ventilation and zero windows."
    ]
    rng.shuffle(options)
    sol = (
        f"**Integrated Energy-Smart Home Design:**\n"
        f"1. **Orientation:** North-facing living areas capture winter sun.\n"
        f"2. **Solar shading:** Overhangs/eaves shade high summer sun while admitting low winter sun.\n"
        f"3. **Roof/Ceiling insulation:** Thick batts (mineral wool/cellulose) block up to 40% of seasonal heat exchange.\n"
        f"4. **Water heating:** Geyser blanket and pipe insulation minimize standing electricity loss.\n"
        f"5. **Air sealing:** Draught-proofing stops convective heat loss.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_49_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "49_designing_an_energy_efficient_house_in_south_africa",
        "question_family_id": "49_designing_an_energy_efficient_house_in_south_africa",
        "hints": {
            "tier_1": "Combine orientation, shading, ceiling insulation, geyser blanket, and sealing.",
            "tier_2": "Look for the comprehensive energy-smart package.",
            "tier_3": "North-facing orientation, roof overhangs, ceiling insulation, geyser blanket, and draught-sealing."
        },
        "misconception_tags": ["piecemeal_design_deficiency"]
    }


def arch_50_heat_insulation_and_energy_saving_comprehensive_diagnostic(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a final diagnostic evaluation on heat insulation and energy conservation:\n"
        f"Statement 1: Trapped still air is the primary insulating mechanism in foams, wool, and fibreglass.\n"
        f"Statement 2: Vacuum layers completely eliminate conduction and convection.\n"
        f"Statement 3: Thermal insulation works symmetrically, keeping hot systems warm and cold systems cool.\n\n"
        f"Which evaluation of these three statements is correct?"
    )
    correct_opt = "All three statements (1, 2, and 3) are scientifically true and represent foundational principles of thermal insulation."
    options = [
        correct_opt,
        "Only Statement 1 is true; Statements 2 and 3 are false.",
        "Only Statement 2 is true; Statements 1 and 3 are false.",
        "All three statements are completely false."
    ]
    rng.shuffle(options)
    sol = (
        f"**Comprehensive Diagnostic Synthesis:**\n"
        f"- **Statement 1 is True:** Tangled fibres and closed-cell foams work because trapped stationary air has extremely low thermal conductivity ($k \\approx 0{{,}}026\\text{{ W/m·K}}$) and suppressed convection.\n"
        f"- **Statement 2 is True:** Conduction and convection strictly require material particles. In a vacuum, there are zero particles, making both processes physically impossible.\n"
        f"- **Statement 3 is True:** Insulators retard the rate of thermal energy transfer along a temperature gradient regardless of direction (e.g. keeping soup hot or keeping ice cream frozen).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns7_ins_50_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "50_heat_insulation_and_energy_saving_comprehensive_diagnostic",
        "question_family_id": "50_heat_insulation_and_energy_saving_comprehensive_diagnostic",
        "hints": {
            "tier_1": "Are trapped air, vacuum, and two-way insulation true principles?",
            "tier_2": "Every one of the three statements represents a core truth in thermal physics.",
            "tier_3": "All three statements (1, 2, and 3) are scientifically true."
        },
        "misconception_tags": ["diagnostic_synthesis_error"]
    }
