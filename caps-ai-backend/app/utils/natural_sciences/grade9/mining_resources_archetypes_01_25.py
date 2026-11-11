"""Grade 9 Natural Sciences - Mining of Mineral Resources: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr9/Term 4/03. Mining of mineral resources.md
Focus:
Definitions (mineral vs ore, gangue, native metals, PGMs), Exploration methods (remote sensing, geophysics, geochemistry, core drilling),
Mining methods (open-cast, underground deep shaft, alluvial), Mineral processing & separation (crushing/milling, screens/cyclones,
gravity panning, magnetic separation, froth flotation), Chemical refining & smelting (reduction of oxides, blast furnace iron,
flux/slag chemistry, gold cyanidation, copper leaching, electrolytic refining, aluminium Hall-Heroult, Mapungubwe gold craft).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_mineral_vs_ore_economic_concentration_criteria(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In economic geology, all ores contain minerals, but not all mineral-bearing rocks are classified as **ores**.\n\n"
        "What essential economic condition qualifies a naturally occurring rock as an **ore**?"
    )
    correct = "It contains a high enough concentration of valuable minerals that it can be extracted, processed, and sold at a financial profit."
    options = [
        correct,
        "It must glow in the dark under ordinary atmospheric air.",
        "It must be completely liquid at room temperature.",
        "It must be composed exclusively of synthetic laboratory chemicals."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Definition of ore:\n"
        "A rock or mineral deposit containing valuable metals or commodities.\n"
        "Step 2: Economic viability:\n"
        "Mining requires massive capital expenditure. A rock body is only an ore if the grade and tonnage allow profitable extraction after covering exploration, mining, processing, and environmental costs."
    )
    return {
        "id": f"ns9_mine_01_{rng.randint(100000, 999999)}",
        "subskill": "01_mineral_vs_ore_economic_concentration_criteria",
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
        "hints": {
            "tier_1": "What financial factor determines whether rock is an ore?",
            "tier_2": "It must be profitable to extract and sell.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ore_definition_economic_viability"]
    }


def arch_02_native_elements_vs_mineral_compound_ores(rng: random.Random) -> Dict[str, Any]:
    metal_pair = rng.choice([
        ("Gold (Au) and Platinum (Pt)", "native uncombined elemental form because of their exceptionally low chemical reactivity", "Hematite (Fe2O3) and Galena (PbS)", "chemical compound ores requiring reduction to release the metal"),
        ("Copper (Cu) in malachite (Cu2CO3(OH)2)", "chemical carbonate compound requiring smelting", "Gold (Au)", "native pure metal occurring uncombined in quartz veins")
    ])
    m1, d1, m2, d2 = metal_pair
    prompt = (
        f"Some valuable metals are mined as uncombined **native elements**, while others occur only as **mineral compounds**.\n\n"
        f"Why does **{m1}** occur in {d1}, whereas **{m2}** occurs in {d2}?"
    )
    correct = "Unreactive (noble) metals resist oxidation and bond formation, remaining in native metallic states, while reactive metals chemically bond with oxygen or sulfur to form stable mineral compounds."
    options = [
        correct,
        "Reactive metals are manufactured in human factories, while noble metals fall from shooting stars.",
        "All metals are naturally native until rainwater turns them into radioactive gases.",
        "Compound ores only form when underground lightning strikes ocean water."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Reactivity series of metals:\n"
        "Gold and platinum have very low chemical affinity for oxygen/sulfur (noble metals), allowing them to exist as native elements in nature.\n"
        "Step 2: Reactive metals:\n"
        "Iron, lead, zinc, and aluminium readily oxidize, occurring naturally as oxides, sulfides, or carbonates that require chemical extraction."
    )
    return {
        "id": f"ns9_mine_02_{rng.randint(100000, 999999)}",
        "subskill": "02_native_elements_vs_mineral_compound_ores",
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
        "hints": {
            "tier_1": "How does chemical reactivity explain why gold is native while iron is an oxide?",
            "tier_2": "Unreactive noble metals remain pure; reactive metals form mineral compounds.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["native_metals_vs_compound_ores"]
    }


def arch_03_gangue_minerals_vs_valuable_target_ores(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In mineral processing, mined ore consists of two distinct components: the target ore mineral and the **gangue**.\n\n"
        "What is **gangue**, and why must it be separated from the valuable mineral?"
    )
    correct = "Gangue is the commercially worthless surrounding rock and waste minerals (such as quartz, calcite, or feldspar) that must be removed to concentrate the valuable ore before smelting."
    options = [
        correct,
        "Gangue is the pure refined metal ingot ready for export to international markets.",
        "Gangue is the chemical fuel used to power underground mining locomotives.",
        "Gangue is the high-voltage electrical cable used to operate mine ventilation fans."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Definition of gangue:\n"
        "The commercially valueless material in an ore deposit that surrounds or is closely mixed with desired minerals.\n"
        "Step 2: Processing purpose:\n"
        "Transporting and smelting gangue wastes vast amounts of energy and flux. Comminution and physical separation reject gangue into tailings, concentrating the ore mineral."
    )
    return {
        "id": f"ns9_mine_03_{rng.randint(100000, 999999)}",
        "subskill": "03_gangue_minerals_vs_valuable_target_ores",
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
        "hints": {
            "tier_1": "Is gangue the valuable metal or the worthless waste rock?",
            "tier_2": "Gangue is the commercially worthless rock that must be separated and discarded.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["gangue_waste_rock_definition"]
    }


def arch_04_platinum_group_metals_six_noble_elements(rng: random.Random) -> Dict[str, Any]:
    pgm_list = "platinum (Pt), palladium (Pd), rhodium (Rh), ruthenium (Ru), iridium (Ir), and osmium (Os)"
    elem = rng.choice(["Platinum (Pt)", "Palladium (Pd)", "Rhodium (Rh)"])
    prompt = (
        f"South Africa hosts the world's greatest reserves of **Platinum Group Metals (PGMs)**.\n\n"
        f"Which group of six transition metals comprises the PGMs, and what key property makes **{elem}** indispensable in vehicle catalytic converters?"
    )
    correct = f"The six PGMs are {pgm_list}; they exhibit exceptional catalytic efficiency and resistance to high-temperature chemical oxidation, catalysing toxic exhaust gases (CO, NOx, hydrocarbons) into harmless CO2, N2, and H2O."
    options = [
        correct,
        f"The six PGMs are copper, iron, lead, tin, zinc, and mercury; they dissolve completely in gasoline to make engines run faster.",
        f"The six PGMs are sodium, potassium, calcium, magnesium, lithium, and cesium; they explode in water to ignite spark plugs.",
        f"The six PGMs are silicon, oxygen, carbon, nitrogen, sulfur, and phosphorus; they freeze exhaust gases into solid ice."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: The six Platinum Group Metals:\n"
        f"{pgm_list}.\n"
        "Step 2: Industrial application:\n"
        "Their high melting points, chemical inertness, and ability to facilitate heterogeneous redox catalysis make them vital for automotive emissions control and hydrogen fuel cell technology."
    )
    return {
        "id": f"ns9_mine_04_{rng.randint(100000, 999999)}",
        "subskill": "04_platinum_group_metals_six_noble_elements",
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
        "hints": {
            "tier_1": "What are the six PGMs and why are they used in catalytic converters?",
            "tier_2": "Pt, Pd, Rh, Ru, Ir, Os; exceptional catalytic properties and chemical resistance.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["platinum_group_metals_catalytic_properties"]
    }


def arch_05_mineral_exploration_remote_sensing_satellite_radar(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Modern mining exploration begins from space using **remote sensing** technologies on satellites and survey aircraft.\n\n"
        "How do multispectral satellite sensors assist exploration geologists in identifying potential mineral deposits from orbit?"
    )
    correct = "They detect distinct spectral reflectance and absorption wavelengths of sunlight reflected from surface rocks and vegetation, revealing telltale alteration mineral zones (such as clays and iron oxides) associated with hidden ore bodies."
    options = [
        correct,
        "They shoot high-powered laser beams that instantly dig underground shafts from orbit.",
        "They use optical microscopes to count individual gold atoms on the surface.",
        "They beam television advertisements to miners working underground."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Principles of remote sensing in exploration:\n"
        "Different minerals reflect and absorb specific electromagnetic wavelengths (visible, near-infrared, shortwave infrared).\n"
        "Step 2: Ore signature:\n"
        "Hydrothermal alteration halos surrounding porphyry or vein deposits contain clays (kaolinite, illite) and iron oxides that exhibit characteristic diagnostic spectral absorption bands."
    )
    return {
        "id": f"ns9_mine_05_{rng.randint(100000, 999999)}",
        "subskill": "05_mineral_exploration_remote_sensing_satellite_radar",
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
        "hints": {
            "tier_1": "How does light reflection from space reveal minerals?",
            "tier_2": "Multispectral sensors detect distinct absorption wavelengths of alteration minerals.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["remote_sensing_multispectral_exploration"]
    }


def arch_06_geophysical_exploration_magnetometry_and_gravity_surveys(rng: random.Random) -> Dict[str, Any]:
    method, target = rng.choice([
        ("Airborne magnetometry (measuring variations in Earth's local magnetic field)", "detecting subsurface magnetic anomalies caused by magnetite iron ores, banded iron formations, or nickel-bearing ultramafic intrusions"),
        ("Ground gravity surveys (measuring minute fluctuations in gravitational acceleration)", "detecting subterranean density contrasts, identifying dense ore bodies like chromite and base metal sulfides versus lighter host rocks")
    ])
    prompt = (
        "Geophysical exploration tools measure physical fields to probe deep beneath the soil without digging.\n\n"
        f"What geological features are identified using **{method}**?"
    )
    correct = f"It is used for {target}."
    options = [
        correct,
        "It is used for detecting underground radio signals broadcast by prehistoric fossils.",
        "It is used for measuring the temperature of clouds to predict afternoon rain showers.",
        "It is used for calculating the speed of migrating bird flocks across the mine."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Physical basis of {method[:25]}:\n"
        "Rocks and ore bodies have physical properties (susceptibility, density) distinct from surrounding country rock.\n"
        f"Step 2: Practical target:\n"
        f"It is used for {target}."
    )
    return {
        "id": f"ns9_mine_06_{rng.randint(100000, 999999)}",
        "subskill": "06_geophysical_exploration_magnetometry_and_gravity_surveys",
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
        "hints": {
            "tier_1": f"What physical property does {method[:20]} measure?",
            "tier_2": f"It is used for {target[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["geophysical_exploration_methods"]
    }


def arch_07_geochemical_prospecting_soil_sampling_and_assays(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During **geochemical exploration**, teams collect grid-pattern soil and stream sediment samples for laboratory chemical assays.\n\n"
        "Why do geochemists analyze for trace **pathfinder elements** (such as arsenic, antimony, or bismuth) when searching for gold deposits?"
    )
    correct = "Pathfinder elements travel together with gold in hydrothermal fluids but form wider, more easily detectable geochemical dispersion halos around the deposit than the scarce gold atoms themselves."
    options = [
        correct,
        "Pathfinder elements are synthetic dyes injected into the ground by GPS satellites.",
        "Gold only forms when soil bacteria eat arsenic and turn it into solid nuggets.",
        "Pathfinder elements are magnetic magnets that pull gold nuggets to the surface."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Geochemical dispersion halos:\n"
        "Weathering and hydrothermal circulation disperse mobile elements outwards from the core mineralized deposit.\n"
        "Step 2: Pathfinder utility:\n"
        "Gold concentrations in unmineralized soil are parts-per-billion. Associated pathfinders (e.g. As with orpiment/arsenopyrite) have higher mobility and concentration, providing a wider geochemical footprint for discovery."
    )
    return {
        "id": f"ns9_mine_07_{rng.randint(100000, 999999)}",
        "subskill": "07_geochemical_prospecting_soil_sampling_and_assays",
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
        "hints": {
            "tier_1": "Why use pathfinder elements instead of searching only for gold?",
            "tier_2": "Pathfinders form broader, more easily detectable halos around the ore.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["geochemical_prospecting_pathfinder_elements"]
    }


def arch_08_diamond_core_drilling_stratigraphy_logging(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Before investing billions in developing a new mine, mining companies conduct extensive **diamond core drilling**.\n\n"
        "What crucial information does a cylindrical rock core provide that cannot be determined from surface surveys alone?"
    )
    correct = "It extracts intact continuous vertical rock cylinders showing exact depth, thickness, geological structure, dip angle, and precise laboratory assay grades of the underground ore body."
    options = [
        correct,
        "It proves whether the underground rock is inhabited by ancient subterranean animals.",
        "It pumps liquid diamond lubricant down to prevent underground earthquakes.",
        "It measures the atmospheric weather forecast for the next fifty years."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Diamond core drilling:\n"
        "Hollow industrial diamond-tipped drill bits core into the rock, retrieving solid cylindrical cores.\n"
        "Step 2: Geotechnical and grade logging:\n"
        "Geologists log lithology, fractures (RQD), alterations, and assay split core halves to calculate 3D ore reserves and grade distributions."
    )
    return {
        "id": f"ns9_mine_08_{rng.randint(100000, 999999)}",
        "subskill": "08_diamond_core_drilling_stratigraphy_logging",
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
        "hints": {
            "tier_1": "What does a solid core sample tell geologists about underground rocks?",
            "tier_2": "Continuous rock cylinders show depth, thickness, structure, and assay grade.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["diamond_core_drilling_resource_logging"]
    }


def arch_09_open_cast_surface_mining_benches_and_overburden(rng: random.Random) -> Dict[str, Any]:
    mine_ex = rng.choice(["Sishen iron ore mine in the Northern Cape", "Palabora copper pit in Limpopo", "Venetia diamond open pit in Limpopo"])
    prompt = (
        f"**Open-cast (open-pit) surface mining**, such as at the {mine_ex}, is used when mineral deposits lie close to Earth's surface.\n\n"
        "What engineering sequence characterizes open-pit mining, and what is the **strip ratio**?"
    )
    correct = "Topsoil and overlying waste rock (overburden) are stripped away, and the pit is excavated downward in stepped horizontal spiral ledges (benches); the strip ratio is the volume of waste rock that must be removed per tonne of valuable ore mined."
    options = [
        correct,
        "Vertical elevator shafts are drilled into the center of the Earth to boil magma into steam.",
        "A fleet of submarines dredges sand dunes from the bottom of deep ocean trenches.",
        "Underground explosions ignite coal seams to power surface turbines directly."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Open-pit bench architecture:\n"
        "Stepped benches ensure slope stability and provide haul roads for heavy trucks.\n"
        "Step 2: Strip ratio (waste-to-ore ratio):\n"
        "Strip ratio = (Volume of Overburden) / (Tonnage of Ore). If the strip ratio becomes too high as the pit deepens, surface mining becomes uneconomic, requiring a switch to underground methods."
    )
    return {
        "id": f"ns9_mine_09_{rng.randint(100000, 999999)}",
        "subskill": "09_open_cast_surface_mining_benches_and_overburden",
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
        "hints": {
            "tier_1": "What are the stepped ledges in an open-pit called and what is stripped away?",
            "tier_2": "Benches with overburden stripped; strip ratio is waste rock removed per tonne of ore.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["open_cast_mining_benches_strip_ratio"]
    }


def arch_10_underground_shaft_mining_hoists_and_stopes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When valuable mineral seams dip deeply beneath thick barren rock layers, mining companies develop **underground shaft mines**.\n\n"
        "What primary subterranean infrastructure allows miners and ore to move between the deep rock faces (**stopes**) and the surface?"
    )
    correct = "Vertical concrete-lined shafts equipped with high-speed hoists (headgear winders), horizontal tunnels (haulages/crosscuts) leading to working stopes, and giant ventilation/refrigeration shafts providing breathable, cooled air."
    options = [
        correct,
        "Water slides that flush miners down to the mantle using ocean waves.",
        "Giant trampolines that bounce ore rocks directly into surface cargo trains.",
        "Open spiral staircases carved into mountain cliffs without any mechanical hoists."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Deep underground mine components:\n"
        "• Vertical shaft: Main conduit for personnel, equipment, power, and ore hoisting.\n"
        "• Haulage levels: Horizontal drives with railway tracks or trackless loaders.\n"
        "• Stopes: The narrow production excavations where the ore reef is drilled, blasted, and scraped out.\n"
        "• Ventilation circuits: Exhaust and intake shafts circulating conditioned air."
    )
    return {
        "id": f"ns9_mine_10_{rng.randint(100000, 999999)}",
        "subskill": "10_underground_shaft_mining_hoists_and_stopes",
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
        "hints": {
            "tier_1": "What vertical and horizontal structures make up a deep underground mine?",
            "tier_2": "Vertical shafts with hoists, horizontal haulage tunnels, stopes, and ventilation.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["underground_mine_shaft_infrastructure"]
    }


def arch_11_ultra_deep_gold_mining_mponeng_thermal_limits(rng: random.Random) -> Dict[str, Any]:
    depth_m = rng.choice([3800, 3900, 4000])
    virgin_temp = rng.choice([60, 65, 66])
    prompt = (
        f"South Africa's **Mponeng Gold Mine** (near Carletonville) is the deepest mine on Earth, plunging nearly **{depth_m} meters** (4 km) beneath the surface.\n\n"
        f"At these extreme depths, virgin rock temperature reaches **{virgin_temp} °C** due to the geothermal gradient. How do engineers make human work possible?"
    )
    correct = "By pumping thousands of tonnes of ice slurry from surface refrigeration plants into massive underground air coolers to lower ambient stope temperatures to safe working conditions (~28 °C)."
    options = [
        correct,
        "By pumping boiling volcanic steam into the tunnels to equalize the pressure.",
        "By flooding all stopes with liquid nitrogen that freezes the entire mine solid.",
        "By requiring miners to wear battery-powered refrigerator suits while holding ice cubes."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Geothermal gradient in the Witwatersrand Basin:\n"
        f"Temperature rises ~9 to 11 °C per kilometer of depth, reaching ~{virgin_temp} °C at {depth_m} m.\n"
        "Step 2: Ventilation and cooling engineering:\n"
        "Immense surface refrigeration plants produce ice slurry. Cold air and chilled water are pumped down insulated shafts, absorbing heat from virgin rock and equipment."
    )
    return {
        "id": f"ns9_mine_11_{rng.randint(100000, 999999)}",
        "subskill": "11_ultra_deep_gold_mining_mponeng_thermal_limits",
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
        "hints": {
            "tier_1": "How is 60+ °C virgin rock cooled in ultra-deep gold mines?",
            "tier_2": "Massive ice-slurry refrigeration plants pump conditioned air to cool stopes.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ultra_deep_mining_geothermal_cooling"]
    }


def arch_12_alluvial_and_heavy_mineral_sand_dredging(rng: random.Random) -> Dict[str, Any]:
    min_ex = rng.choice(["alluvial diamonds along the Orange River and Namaqualand coast", "heavy mineral sands (ilmenite, rutile, zircon) at Richards Bay"])
    prompt = (
        f"**Alluvial mining and dredging**, such as for {min_ex}, extracts minerals that have weathered out of primary hard-rock deposits.\n\n"
        "Why do these valuable minerals accumulate in riverbeds, coastal gravels, and beach dunes?"
    )
    correct = "They possess high physical hardness, chemical resistance to weathering, and high density, allowing them to survive transport and settle into natural gravity traps when moving water slows down."
    options = [
        correct,
        "They are magnetic minerals that are attracted to fish swimming in the water.",
        "They are lightweight minerals that float on water like leaves and blow onto beaches.",
        "They are formed when ocean salt dissolves sand into solid gemstone crystals."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Placer deposit mechanics:\n"
        "Primary deposits weather and erode.\n"
        "Step 2: Physical concentration:\n"
        "Durable, dense minerals (diamonds ~3,5 g/cm³, zircon ~4,7 g/cm³, ilmenite ~4,7 g/cm³, gold ~19,3 g/cm³) resist attrition, while lighter quartz/feldspar (~2,6 g/cm³) is washed away, creating rich secondary placer deposits."
    )
    return {
        "id": f"ns9_mine_12_{rng.randint(100000, 999999)}",
        "subskill": "12_alluvial_and_heavy_mineral_sand_dredging",
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
        "hints": {
            "tier_1": "What properties allow minerals to concentrate in river gravels and beach sands?",
            "tier_2": "High density, hardness, and chemical resistance in natural gravity traps.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["alluvial_placer_mineral_concentration"]
    }


def arch_13_crushing_and_milling_comminution_grain_liberation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Once ore is blasted and hoisted to the surface, it enters the processing plant for **comminution** (crushing and milling).\n\n"
        "What is the physical objective of crushing large ore boulders into fine powder (slurry)?"
    )
    correct = "To liberate (free) individual valuable mineral grains from the enclosing waste rock (gangue) matrix so they can be separated physically or dissolved chemically."
    options = [
        correct,
        "To melt the rock into liquid glass before loading it onto export cargo ships.",
        "To turn all waste rock into synthetic gold through high-frequency acoustic friction.",
        "To evaporate all chemical elements into atmospheric gas clouds."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Comminution sequence:\n"
        "Jaw/gyratory crushers reduce run-of-mine ore (>1 m boulders down to <15 cm), followed by SAG and ball mills grinding to <75 micrometers.\n"
        "Step 2: Degree of liberation:\n"
        "Mineral grains are interlocked with gangue. Grinding until the particle size matches the mineral crystal size exposes clean mineral surfaces for flotation or leaching."
    )
    return {
        "id": f"ns9_mine_13_{rng.randint(100000, 999999)}",
        "subskill": "13_crushing_and_milling_comminution_grain_liberation",
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
        "hints": {
            "tier_1": "Why grind rock to fine dust in ball mills?",
            "tier_2": "To liberate valuable mineral grains from the surrounding gangue rock.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["comminution_milling_mineral_liberation"]
    }


def arch_14_particle_classification_vibrating_screens_cyclones(rng: random.Random) -> Dict[str, Any]:
    tool = rng.choice([
        ("Vibrating screens", "coarse particle sizing, separating oversized rocks that require further crushing from undersized particles"),
        ("Hydrocyclones", "wet centrifugal classification, using vortex fluid forces to separate fine particles (overflow) from heavy/coarse particles (underflow)")
    ])
    tool_name, function = tool
    prompt = (
        "Between crushing and milling stages, mineral processing plants use sizing and classification equipment.\n\n"
        f"What role is performed by **{tool_name}** in the processing circuit?"
    )
    correct = f"It is used for {function}."
    options = [
        correct,
        "It is used for burning coal to generate electricity for the plant.",
        "It is used for painting finished metal ingots with protective enamel paint.",
        "It is used for freezing waste water into giant blocks of ice."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Role of {tool_name}:\n"
        "Classification ensures efficient energy usage in grinding circuits.\n"
        f"Step 2: Mechanism:\n"
        f"It is used for {function}."
    )
    return {
        "id": f"ns9_mine_14_{rng.randint(100000, 999999)}",
        "subskill": "14_particle_classification_vibrating_screens_cyclones",
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
        "hints": {
            "tier_1": f"What is {tool_name} used for in mineral processing?",
            "tier_2": f"It is used for {function[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["particle_classification_screens_cyclones"]
    }


def arch_15_gravity_separation_density_panning_and_dms(rng: random.Random) -> Dict[str, Any]:
    method_pair = rng.choice([
        ("Dense Medium Separation (DMS)", "mixing crushed ore with a dense ferrosilicon slurry: heavy diamonds/ores sink while lighter waste rock floats"),
        ("Gold panning", "swirling water in a shallow pan: dense gold particles (density ~19,3 g/cm³) settle to the bottom ridges while lighter sand washes away")
    ])
    name, mechanism = method_pair
    prompt = (
        f"**Gravity separation** exploits differences in density between minerals and gangue.\n\n"
        f"How does **{name}** separate valuable materials from waste?"
    )
    correct = f"By {mechanism}."
    options = [
        correct,
        "By applying strong electrical shocks that vaporize non-metallic rock into steam.",
        "By using powerful suction vacuums that lift magnetic rock into the air.",
        "By soaking the rock in sulfuric acid until all minerals evaporate into clouds."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Principles of {name}:\n"
        "Density difference: Minerals with specific gravity significantly higher than gangue settle faster in a fluid medium.\n"
        f"Step 2: Operating mechanism:\n"
        f"By {mechanism}."
    )
    return {
        "id": f"ns9_mine_15_{rng.randint(100000, 999999)}",
        "subskill": "15_gravity_separation_density_panning_and_dms",
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
        "hints": {
            "tier_1": f"How does density help {name} separate minerals?",
            "tier_2": f"By {mechanism[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["gravity_separation_density_difference"]
    }


def arch_16_magnetic_separation_ferrous_ore_recovery(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In iron ore beneficiation plants (such as Sishen), **magnetic separation** is used to upgrade ore quality.\n\n"
        "How does magnetic separation isolate magnetic iron minerals from non-magnetic quartz and shale gangue?"
    )
    correct = "Crushed ore passes over rotating magnetic drums; magnetic iron particles adhere to the drum surface and drop into a concentrate chute, while non-magnetic waste rock is thrown off by centrifugal force into the tailings."
    options = [
        correct,
        "Magnets melt the iron ore into molten red metal while freezing the quartz rock into ice.",
        "Magnets reverse the Earth's gravity to make non-magnetic rocks float to the ceiling.",
        "Magnets dissolve iron into hydrochloric acid while leaving silica untouched."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Magnetic susceptibility:\n"
        "Magnetite (Fe3O4) is strongly ferromagnetic; hematite (Fe2O3) is weakly paramagnetic.\n"
        "Step 2: Drum separation:\n"
        "Permanent or electromagnets inside rotating drums hold magnetic grains against the shell until rotating out of the magnetic field, cleanly separating iron ore from non-magnetic silicate gangue."
    )
    return {
        "id": f"ns9_mine_16_{rng.randint(100000, 999999)}",
        "subskill": "16_magnetic_separation_ferrous_ore_recovery",
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
        "hints": {
            "tier_1": "How do magnetic drums pull iron ore away from waste rock?",
            "tier_2": "Magnetic particles stick to the drum while non-magnetic waste flies off.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["magnetic_separation_drum_mechanics"]
    }


def arch_17_froth_flotation_hydrophobic_bubbles_and_collectors(rng: random.Random) -> Dict[str, Any]:
    ore_app = rng.choice(["copper sulfide ore (chalcopyrite)", "platinum group metals (Bushveld PGM ore)"])
    prompt = (
        f"**Froth flotation** is the primary separation technique used worldwide for concentrating **{ore_app}**.\n\n"
        "How does chemical froth flotation separate finely ground mineral grains from waste rock in water tanks?"
    )
    correct = "Collector chemicals coat mineral grains to make them water-repellent (hydrophobic); air bubbles sparged through the tank attach to the hydrophobic minerals, floating them into an overflowing surface froth, while hydrophilic gangue sinks."
    options = [
        correct,
        "Soap dissolves the gangue rock completely into drinkable water, leaving behind dry metal blocks.",
        "High-voltage electricity electroplates all the minerals onto the walls of the flotation tank.",
        "The tank is boiled at 2000 °C until all minerals melt into a single puddle of molten brass."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Surface chemistry in flotation:\n"
        "Collector reagents (e.g. xanthates) selectively adsorb onto target sulfide/PGM surfaces, making them hydrophobic.\n"
        "Step 2: Froth collection:\n"
        "Frothers stabilize rising air bubbles. Hydrophobic mineral particles hitch a ride on bubble surfaces, forming a mineral-rich froth scraped off the top, while hydrophilic silicate gangue remains submerged and discharges as tailings."
    )
    return {
        "id": f"ns9_mine_17_{rng.randint(100000, 999999)}",
        "subskill": "17_froth_flotation_hydrophobic_bubbles_and_collectors",
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
        "hints": {
            "tier_1": "What makes minerals attach to rising air bubbles in flotation?",
            "tier_2": "Collector chemicals make minerals hydrophobic, allowing bubbles to float them into froth.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["froth_flotation_surface_hydrophobicity"]
    }


def arch_18_smelting_chemical_reduction_metal_oxides_carbon(rng: random.Random) -> Dict[str, Any]:
    metal_rxn = rng.choice([
        ("lead(II) oxide", "2PbO + C → 2Pb + CO2", "Lead (Pb)"),
        ("copper(II) oxide", "2CuO + C → 2Cu + CO2", "Copper (Cu)"),
        ("iron(III) oxide", "2Fe2O3 + 3C → 4Fe + 3CO2", "Iron (Fe)")
    ])
    oxide_name, eqn, metal_name = metal_rxn
    prompt = (
        f"In extractive metallurgy, **smelting** uses chemical reduction to extract metals from their oxide ores.\n\n"
        f"In the smelting reaction: $${eqn}$$, what chemical role does carbon (coke/charcoal) play?"
    )
    correct = f"Carbon acts as a reducing agent: it removes oxygen from {oxide_name} (reducing it to pure {metal_name}) while carbon itself is oxidized to carbon dioxide gas (CO2)."
    options = [
        correct,
        f"Carbon acts as an oxidizing agent: it adds oxygen to {metal_name} to turn it into an acid.",
        "Carbon acts only as a decorative black coloring dye with zero chemical participation.",
        "Carbon acts as an explosive detonator that destroys the furnace walls."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Redox definitions:\n"
        "Oxidation = loss of electrons / gain of oxygen.\n"
        "Reduction = gain of electrons / loss of oxygen.\n"
        f"Step 2: Smelting mechanism:\n"
        f"Carbon has higher affinity for oxygen at smelting temperatures than {metal_name}. Carbon strips oxygen from the metal oxide, reducing {oxide_name} to elemental {metal_name} while oxidizing C to CO2."
    )
    return {
        "id": f"ns9_mine_18_{rng.randint(100000, 999999)}",
        "subskill": "18_smelting_chemical_reduction_metal_oxides_carbon",
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
        "hints": {
            "tier_1": "Does carbon gain oxygen or lose oxygen during smelting?",
            "tier_2": "Carbon gains oxygen (is oxidized), acting as the reducing agent.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["smelting_chemical_reduction_carbon_agent"]
    }


def arch_19_iron_smelting_blast_furnace_coke_and_flux(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Industrial iron production occurs in a towering vertical **blast furnace** operating continuously for years.\n\n"
        "What three raw materials are continuously charged into the top of a blast furnace?"
    )
    correct = "Iron ore (e.g. hematite Fe2O3), coke (purified carbon fuel and reducing agent), and limestone (CaCO3 flux to remove silica impurities)."
    options = [
        correct,
        "Crude oil, water ice cubes, and volcanic pumice rock.",
        "Diamond crystals, gold dust, and liquid mercury metal.",
        "Plastic pellets, copper wire, and concentrated hydrochloric acid."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: The blast furnace charge (burden):\n"
        "1. Iron ore (source of iron atoms: Fe2O3).\n"
        "2. Coke (provides heat via combustion and generates CO reducing gas).\n"
        "3. Limestone flux (removes quartz/sand impurities by forming molten slag).\n"
        "Step 2: Hot air blast injected through tuyeres burns coke, driving reduction."
    )
    return {
        "id": f"ns9_mine_19_{rng.randint(100000, 999999)}",
        "subskill": "19_iron_smelting_blast_furnace_coke_and_flux",
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
        "hints": {
            "tier_1": "What three materials are fed into a blast furnace?",
            "tier_2": "Iron ore, coke, and limestone flux.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["blast_furnace_raw_materials_charge"]
    }


def arch_20_calcium_carbonate_flux_slag_formation_silicates(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During blast furnace iron smelting, **limestone (CaCO3)** is added specifically to react with sandy silica (SiO2) gangue.\n\n"
        "What chemical reaction sequence forms **slag**, and how is it separated from molten iron?"
    )
    correct = "Limestone thermally decomposes to calcium oxide (CaCO3 → CaO + CO2), which reacts with silica gangue to form molten calcium silicate slag (CaO + SiO2 → CaSiO3); because slag is less dense than molten iron, it floats on top and is tapped off separately."
    options = [
        correct,
        "Limestone dissolves iron into liquid gold, and slag sinks to the bottom because it is three times denser than iron.",
        "Limestone freezes the furnace so workers can shovel silica out with hand brooms.",
        "Limestone explodes into combustible gas that is burned to make plastic bottles."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Thermal decomposition of flux:\n"
        "CaCO3(s) → CaO(s) + CO2(g)↑.\n"
        "Step 2: Acid-base slag formation:\n"
        "Basic oxide CaO reacts with acidic silica: CaO + SiO2 → CaSiO3 (molten slag).\n"
        "Step 3: Density separation:\n"
        "Molten slag (density ~2,8 g/cm³) floats above molten iron (density ~7,0 g/cm³), protecting hot iron from re-oxidizing and allowing separate tapping."
    )
    return {
        "id": f"ns9_mine_20_{rng.randint(100000, 999999)}",
        "subskill": "20_calcium_carbonate_flux_slag_formation_silicates",
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
        "hints": {
            "tier_1": "What does limestone turn into and why does slag float on molten iron?",
            "tier_2": "CaO reacts with SiO2 to form molten CaSiO3 slag, which floats because it is less dense.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["flux_limestone_slag_formation_density"]
    }


def arch_21_gold_cyanidation_leaching_and_carbon_in_pulp(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In South African gold recovery plants, microscopic gold particles are extracted using **cyanidation** and **Carbon-in-Pulp (CIP)**.\n\n"
        "What chemical leaching mechanism dissolves gold, and how does activated carbon recover it from the pulp?"
    )
    correct = "A dilute sodium cyanide (NaCN) solution with dissolved oxygen leaches gold into soluble aurocyanide complex ions [Au(CN)2]⁻; porous activated coconut-shell carbon granules then adsorb the gold complex onto their surfaces."
    options = [
        correct,
        "Concentrated sulfuric acid dissolves all rock except gold, which melts into a puddle on the floor.",
        "Giant magnets attract gold atoms directly out of mud without using any liquid chemical solutions.",
        "Boiling salt water freezes gold into ice cubes that float to the surface."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Elsner's Equation for gold cyanidation:\n"
        "4Au + 8NaCN + O2 + 2H2O → 4Na[Au(CN)2] + 4NaOH.\n"
        "Step 2: Carbon adsorption:\n"
        "Activated carbon has enormous surface area (~1000 m²/g). It selectively adsorbs the [Au(CN)2]⁻ complex. The loaded carbon is screened out, eluted with hot caustic cyanide, and electro-won as gold cathode sludge."
    )
    return {
        "id": f"ns9_mine_21_{rng.randint(100000, 999999)}",
        "subskill": "21_gold_cyanidation_leaching_and_carbon_in_pulp",
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
        "hints": {
            "tier_1": "What chemical dissolves gold and what porous material adsorbs it?",
            "tier_2": "Dilute cyanide solution dissolves gold; activated carbon adsorbs the aurocyanide complex.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["gold_cyanidation_carbon_in_pulp_cip"]
    }


def arch_22_copper_heap_leaching_with_sulfuric_acid(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Low-grade copper oxide ores are often processed using **heap leaching**.\n\n"
        "What operational procedure constitutes heap leaching, and what solvent dissolves the copper?"
    )
    correct = "Crushed ore is piled into massive outdoor heaps lined with impermeable plastic membranes, and dilute sulfuric acid (H2SO4) is trickled over the top to dissolve copper into a pregnant leach solution (CuSO4)."
    options = [
        correct,
        "Ore is loaded into rocket boosters and launched into outer space to be baked by the Sun.",
        "Ore is submerged in liquid nitrogen ice until the rock fractures into diamond dust.",
        "Ore is burned in underground coal furnaces to vaporize copper into clouds."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Heap leaching layout:\n"
        "An engineered containment pad with an HDPE liner prevents environmental groundwater contamination.\n"
        "Step 2: Acid dissolution:\n"
        "CuO + H2SO4 → CuSO4(aq) + H2O.\n"
        "Percolating acid dissolves copper. The pregnant leach solution (PLS) is collected in drainage pipes for solvent extraction and electrowinning (SX-EW)."
    )
    return {
        "id": f"ns9_mine_22_{rng.randint(100000, 999999)}",
        "subskill": "22_copper_heap_leaching_with_sulfuric_acid",
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
        "hints": {
            "tier_1": "What acid trickles through ore heaps to dissolve copper?",
            "tier_2": "Dilute sulfuric acid (H2SO4) dissolves copper into copper sulfate solution.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["copper_heap_leaching_sulfuric_acid"]
    }


def arch_23_electrolytic_refining_high_purity_copper_cathodes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Blister copper produced from smelting is ~98% pure, but electrical wiring requires 99,99% purity. High purity is achieved via **electrolytic refining**.\n\n"
        "In the copper electrolysis cell, what happens at the **anode** and the **cathode**?"
    )
    correct = "Impure copper anodes dissolve (Cu → Cu²⁺ + 2e⁻), while copper ions migrate across the acidified copper sulfate electrolyte and plate onto pure copper cathode sheets (Cu²⁺ + 2e⁻ → Cu); noble metal impurities (Au, Ag) drop as anode slime."
    options = [
        correct,
        "Both electrodes dissolve completely into hydrogen gas bubbles with zero copper deposited.",
        "Cathodes dissolve into plastic while anodes turn into solid aluminum bars.",
        "Electrical current boils the electrolyte into poisonous steam, leaving solid gold on the walls."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Electrolytic cell setup:\n"
        "• Anode (+) = Impure copper slab.\n"
        "• Cathode (-) = Thin sheet of pure copper.\n"
        "• Electrolyte = CuSO4 + H2SO4.\n"
        "Step 2: Selective electroplating:\n"
        "Anode oxidation: Cu(s) → Cu²⁺(aq) + 2e⁻.\n"
        "Cathode reduction: Cu²⁺(aq) + 2e⁻ → Cu(s) (99,99% pure cathode).\n"
        "Precious metals (Au, Ag, Pt) do not oxidize at this voltage and settle as valuable anode slime."
    )
    return {
        "id": f"ns9_mine_23_{rng.randint(100000, 999999)}",
        "subskill": "23_electrolytic_refining_high_purity_copper_cathodes",
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
        "hints": {
            "tier_1": "Which electrode dissolves and which electrode plates out pure copper?",
            "tier_2": "Impure copper anode dissolves; pure copper plates onto cathode.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["electrolytic_refining_copper_electrodes"]
    }


def arch_24_aluminium_smelting_bauxite_bayer_hall_heroult(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Aluminium cannot be smelted with carbon in a blast furnace because aluminium has a greater affinity for oxygen than carbon.\n\n"
        "How is metallic aluminium commercially extracted from refined alumina (Al2O3) in the **Hall-Héroult process**?"
    )
    correct = "Alumina is dissolved in molten cryolite (Na3AlF6) at ~950 °C to lower its melting point, and colossal electrical currents pass through carbon anodes, reducing aluminium ions to molten aluminium metal at the cathode."
    options = [
        correct,
        "Alumina is boiled in tap water inside wooden barrels until aluminium floats to the surface.",
        "Alumina is placed in a freezer at -100 °C until oxygen spontaneously falls out as liquid air.",
        "Alumina is hammered with heavy steam presses until oxygen is squeezed out as water."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Why blast furnaces fail:\n"
        "Aluminium is too reactive; Al-O bond energy exceeds C-O affinity at accessible temperatures.\n"
        "Step 2: Hall-Héroult molten salt electrolysis:\n"
        "Pure Al2O3 melts at 2072 °C (impractically high). Dissolving it in molten cryolite lowers operating temperature to ~950 °C.\n"
        "Cathode: Al³⁺ + 3e⁻ → Al(l) (dense molten metal sinks to bottom).\n"
        "Anode: 2O²⁻ + C(anode) → CO2(g) + 4e⁻ (carbon anodes are consumed)."
    )
    return {
        "id": f"ns9_mine_24_{rng.randint(100000, 999999)}",
        "subskill": "24_aluminium_smelting_bauxite_bayer_hall_heroult",
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
        "hints": {
            "tier_1": "What molten mineral dissolves alumina to allow electrical reduction?",
            "tier_2": "Molten cryolite dissolves alumina at ~950 °C for molten salt electrolysis.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["hall_heroult_aluminium_electrolysis"]
    }


def arch_25_indigenous_african_metallurgy_mapungubwe_gold_craft(rng: random.Random) -> Dict[str, Any]:
    artifact = rng.choice(["the famous Golden Rhinoceros", "the golden scepter and bowl", "delicate gold foil beads"])
    prompt = (
        f"At the ancient Kingdom of **Mapungubwe** (c. 1220–1300 AD) in the Limpopo Valley, archaeologists unearthed {artifact}.\n\n"
        "What technological expertise was mastered by indigenous South African metallurgists at Mapungubwe centuries before European arrival?"
    )
    correct = "They mined alluvial and quartz gold, melted it in ceramic crucibles using charcoal bloomery fires, hammered the molten gold into ultra-thin foil sheets, and attached it with tiny gold tacks over carved wooden sculptures."
    options = [
        correct,
        "They imported all metals from 18th-century European factories via diesel steamships.",
        "They used nuclear particle accelerators to transmute river sand into pure gold.",
        "They bought plastic golden toys from modern commercial retail stores."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Archaeological evidence at Mapungubwe:\n"
        "Mapungubwe Hill graves yielded magnificent gold artifacts, including the iconic Golden Rhinoceros.\n"
        "Step 2: Indigenous metallurgical mastery:\n"
        "Pre-colonial African smiths possessed sophisticated pyrotechnology: melting gold in clay crucibles, casting ingots, hammering foil sheets with stone hammers, and tacking them onto wooden carvings, evidencing thriving indigenous science and regional trade."
    )
    return {
        "id": f"ns9_mine_25_{rng.randint(100000, 999999)}",
        "subskill": "25_indigenous_african_metallurgy_mapungubwe_gold_craft",
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
        "hints": {
            "tier_1": "How did Mapungubwe smiths craft the Golden Rhinoceros?",
            "tier_2": "Crucible melting and hammering gold foil attached over wooden carvings.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mapungubwe_indigenous_gold_metallurgy"]
    }


BUILDERS_01_25 = {
    "01_mineral_vs_ore_economic_concentration_criteria": arch_01_mineral_vs_ore_economic_concentration_criteria,
    "02_native_elements_vs_mineral_compound_ores": arch_02_native_elements_vs_mineral_compound_ores,
    "03_gangue_minerals_vs_valuable_target_ores": arch_03_gangue_minerals_vs_valuable_target_ores,
    "04_platinum_group_metals_six_noble_elements": arch_04_platinum_group_metals_six_noble_elements,
    "05_mineral_exploration_remote_sensing_satellite_radar": arch_05_mineral_exploration_remote_sensing_satellite_radar,
    "06_geophysical_exploration_magnetometry_and_gravity_surveys": arch_06_geophysical_exploration_magnetometry_and_gravity_surveys,
    "07_geochemical_prospecting_soil_sampling_and_assays": arch_07_geochemical_prospecting_soil_sampling_and_assays,
    "08_diamond_core_drilling_stratigraphy_logging": arch_08_diamond_core_drilling_stratigraphy_logging,
    "09_open_cast_surface_mining_benches_and_overburden": arch_09_open_cast_surface_mining_benches_and_overburden,
    "10_underground_shaft_mining_hoists_and_stopes": arch_10_underground_shaft_mining_hoists_and_stopes,
    "11_ultra_deep_gold_mining_mponeng_thermal_limits": arch_11_ultra_deep_gold_mining_mponeng_thermal_limits,
    "12_alluvial_and_heavy_mineral_sand_dredging": arch_12_alluvial_and_heavy_mineral_sand_dredging,
    "13_crushing_and_milling_comminution_grain_liberation": arch_13_crushing_and_milling_comminution_grain_liberation,
    "14_particle_classification_vibrating_screens_cyclones": arch_14_particle_classification_vibrating_screens_cyclones,
    "15_gravity_separation_density_panning_and_dms": arch_15_gravity_separation_density_panning_and_dms,
    "16_magnetic_separation_ferrous_ore_recovery": arch_16_magnetic_separation_ferrous_ore_recovery,
    "17_froth_flotation_hydrophobic_bubbles_and_collectors": arch_17_froth_flotation_hydrophobic_bubbles_and_collectors,
    "18_smelting_chemical_reduction_metal_oxides_carbon": arch_18_smelting_chemical_reduction_metal_oxides_carbon,
    "19_iron_smelting_blast_furnace_coke_and_flux": arch_19_iron_smelting_blast_furnace_coke_and_flux,
    "20_calcium_carbonate_flux_slag_formation_silicates": arch_20_calcium_carbonate_flux_slag_formation_silicates,
    "21_gold_cyanidation_leaching_and_carbon_in_pulp": arch_21_gold_cyanidation_leaching_and_carbon_in_pulp,
    "22_copper_heap_leaching_with_sulfuric_acid": arch_22_copper_heap_leaching_with_sulfuric_acid,
    "23_electrolytic_refining_high_purity_copper_cathodes": arch_23_electrolytic_refining_high_purity_copper_cathodes,
    "24_aluminium_smelting_bauxite_bayer_hall_heroult": arch_24_aluminium_smelting_bauxite_bayer_hall_heroult,
    "25_indigenous_african_metallurgy_mapungubwe_gold_craft": arch_25_indigenous_african_metallurgy_mapungubwe_gold_craft,
}
