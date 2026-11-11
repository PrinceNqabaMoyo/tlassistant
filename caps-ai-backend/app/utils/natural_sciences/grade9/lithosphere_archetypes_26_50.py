"""Grade 9 Natural Sciences - The Lithosphere: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr9/Term 4/02. The lithosphere.md
Focus:
Metamorphic textures (foliated vs non-foliated, soapstone & talc), Rock cycle closed network,
Minerals vs Rocks (5 mineral criteria, quartz, feldspar, calcite acid test, hematite/magnetite iron ores),
Crustal composition (top 8 elements, silicon-oxygen silicates), Mineral identification (Mohs hardness scratch test,
cleavage planes vs conchoidal fracture), Plate tectonics (lithospheric plates, convection, convergent/divergent/transform),
South African geological heritage (East African Rift, Table Mountain sandstone, Karoo Supergroup fossils,
Drakensberg flood basalts, Bushveld Igneous Complex, Kimberlite diamond pipes, Deep time, Comprehensive Diagnostic Autopsy).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_26_foliated_vs_non_foliated_metamorphic_textures(rng: random.Random) -> Dict[str, Any]:
    tex = rng.choice(["foliated texture", "non-foliated texture"])
    if tex == "foliated texture":
        desc = "minerals align in parallel wavy layers or bands under directional differential pressure (e.g. slate, schist, gneiss)"
        distractor = "mineral grains show no preferred alignment, forming a uniform sugary or interlocking crystalline mosaic under uniform pressure (e.g. marble, quartzite)"
    else:
        desc = "mineral grains show no preferred alignment, forming a uniform sugary or interlocking crystalline mosaic under uniform pressure (e.g. marble, quartzite)"
        distractor = "minerals align in parallel wavy layers or bands under directional differential pressure (e.g. slate, schist, gneiss)"
    prompt = (
        f"Metamorphic rocks are divided into two major textural groups based on the orientation of their mineral grains.\n\n"
        f"What physical characteristics and pressure conditions produce a **{tex}**?"
    )
    correct = f"It occurs when {desc}."
    options = [
        correct,
        f"It occurs when {distractor}.",
        "It occurs when molten lava boils in open air without cooling.",
        "It occurs when rocks dissolve completely in concentrated ocean brine."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Define {tex}:\n"
        f"Texture in metamorphic rocks reflects differential stress vs confining pressure.\n"
        f"Step 2: Mechanism:\n"
        f"A {tex} occurs when {desc}."
    )
    return {
        "id": f"ns9_lith_26_{rng.randint(100000, 999999)}",
        "subskill": "26_foliated_vs_non_foliated_metamorphic_textures",
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
            "tier_1": f"Are mineral grains aligned or non-aligned in {tex}?",
            "tier_2": f"It occurs when {desc[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["metamorphic_foliated_vs_nonfoliated_textures"]
    }


def arch_27_soapstone_talc_softness_and_traditional_carving(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "**Soapstone** (steatite) is a soft metamorphic rock traditionally prized across Southern Africa for carving cooking pots, pipes, and ceremonial bird sculptures (such as the Great Zimbabwe soapstone birds).\n\n"
        "What primary mineral component gives soapstone its soapy, greasy feel and remarkable softness?"
    )
    correct = "Talc, the softest known mineral on Earth (Mohs hardness 1), which can be easily scratched and shaped with an ordinary fingernail."
    options = [
        correct,
        "Liquid diamond crystals that dissolve in human saliva.",
        "Pure metallic lead melted into volcanic ash.",
        "Frozen animal fat petrified into sedimentary limestone."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Mineral composition of soapstone:\n"
        "Composed largely of talc: Mg3Si4O10(OH)2.\n"
        "Step 2: Physical properties:\n"
        "Talc defines Mohs hardness 1. Weak van der Waals forces between its sheet silicate layers give it a greasy or soapy tactile feel and allow it to be effortlessly carved using simple metal or bone tools."
    )
    return {
        "id": f"ns9_lith_27_{rng.randint(100000, 999999)}",
        "subskill": "27_soapstone_talc_softness_and_traditional_carving",
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
            "tier_1": "What is the softest mineral on the Mohs hardness scale (hardness 1)?",
            "tier_2": "Talc, which gives soapstone its soft, greasy feel.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["soapstone_talc_mineral_properties"]
    }


def arch_28_rock_cycle_complete_closed_interconversion_network(rng: random.Random) -> Dict[str, Any]:
    pathway = rng.choice([
        ("an igneous rock directly into a sedimentary rock", "weathering and erosion break it down into sediments, which undergo deposition, compaction, and cementation"),
        ("a sedimentary rock directly into a metamorphic rock", "tectonic burial subjects the rock to intense heat and differential pressure without melting"),
        ("a metamorphic rock directly into an igneous rock", "subduction into the hot mantle causes complete melting into magma, which subsequently cools and solidifies")
    ])
    trans, steps = pathway
    prompt = (
        f"In the rock cycle, geological pathways connect all rock families.\n\n"
        f"What geological processes transform **{trans}**?"
    )
    correct = f"Through {steps}."
    options = [
        correct,
        "Through evaporation of rock atoms into the upper stratosphere.",
        "Through photosynthesis carried out by subterranean tree roots.",
        "Through sound waves vibrating inside underground caverns."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Target pathway: {trans}.\n"
        f"Step 2: Step-by-step mechanism:\n"
        f"This transition occurs when {steps}."
    )
    return {
        "id": f"ns9_lith_28_{rng.randint(100000, 999999)}",
        "subskill": "28_rock_cycle_complete_closed_interconversion_network",
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
            "tier_1": f"How does {trans} occur?",
            "tier_2": f"It happens when {steps[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["rock_cycle_pathways_interconversion"]
    }


def arch_29_mineral_definition_five_criteria_inorganic_crystal(rng: random.Random) -> Dict[str, Any]:
    crit = rng.choice([
        ("Naturally occurring", "formed by natural geological processes rather than manufactured synthetically in human laboratories"),
        ("Inorganic", "not composed of organic molecules originating from once-living plant or animal tissues"),
        ("Solid", "existing as a solid state of matter under normal Earth surface temperatures and pressures"),
        ("Definite chemical composition", "expressed by a specific chemical formula (e.g. SiO2 or CaCO3) with fixed atomic ratios"),
        ("Ordered internal crystalline structure", "atoms are arranged in an orderly, repeating 3D geometric lattice pattern")
    ])
    crit_name, defn = crit
    prompt = (
        "In Earth science, a substance must satisfy five strict criteria to be officially classified as a **mineral**.\n\n"
        f"Which statement accurately explains the mineral criterion: **'{crit_name}'**?"
    )
    correct = f"It means the substance is {defn}."
    options = [
        correct,
        "It means the substance can only be found on the surface of the Moon.",
        "It means the substance dissolves instantly in cold tap water.",
        "It means the substance was invented by human chemical engineers in a factory."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: The 5 criteria for a mineral:\n"
        "1. Naturally occurring, 2. Inorganic, 3. Solid, 4. Definite chemical composition, 5. Ordered crystalline structure.\n"
        f"Step 2: Specific criterion '{crit_name}':\n"
        f"It means {defn}."
    )
    return {
        "id": f"ns9_lith_29_{rng.randint(100000, 999999)}",
        "subskill": "29_mineral_definition_five_criteria_inorganic_crystal",
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
            "tier_1": f"What does '{crit_name}' require in a mineral?",
            "tier_2": f"It requires that the substance is {defn[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["five_mineral_criteria_definition"]
    }


def arch_30_rock_vs_mineral_aggregate_distinction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "People often use the words 'rock' and 'mineral' interchangeably, but geologically they have precise, distinct definitions.\n\n"
        "What is the fundamental scientific difference between a **mineral** and a **rock**?"
    )
    correct = "A mineral is a pure, single inorganic chemical compound with an orderly crystalline structure, whereas a rock is a solid aggregate mixture composed of one or more minerals."
    options = [
        correct,
        "A mineral is always a liquid, while a rock is always an atmospheric gas.",
        "A mineral is man-made in factories, while a rock falls from outer space.",
        "A mineral is alive and performs photosynthesis, while a rock is non-living."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Mineral vs Rock distinction:\n"
        "Analogy: Minerals are like individual cake ingredients (flour, sugar, cocoa); a rock is the baked cake.\n"
        "Step 2: Real-world example:\n"
        "Granite is a ROCK; it contains an aggregate mixture of distinct MINERALS (quartz, potassium feldspar, plagioclase, and biotite mica)."
    )
    return {
        "id": f"ns9_lith_30_{rng.randint(100000, 999999)}",
        "subskill": "30_rock_vs_mineral_aggregate_distinction",
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
            "tier_1": "Is a rock made of minerals, or are minerals made of rocks?",
            "tier_2": "A rock is an aggregate mixture of one or more pure minerals.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["rock_vs_mineral_distinction_aggregate"]
    }


def arch_31_quartz_silicon_dioxide_tetrahedral_crystal_network(rng: random.Random) -> Dict[str, Any]:
    formula = "SiO2 (Silicon Dioxide)"
    hardness = 7
    prompt = (
        f"**Quartz** ({formula}) is one of the most common and durable minerals in Earth's continental crust, with a Mohs hardness of {hardness}.\n\n"
        "What atomic structure gives quartz its high resistance to chemical and physical weathering?"
    )
    correct = "A 3D framework of silicon-oxygen tetrahedra (SiO4) where all four oxygen atoms are shared between adjacent tetrahedra, creating strong covalent bonds in all directions."
    options = [
        correct,
        "A soft layer of organic petroleum coating the outside of each crystal.",
        "Loose electrostatic bonds that break whenever rainwater touches the crystal.",
        "A hollow iron cage that absorbs magnetic currents from the core."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Framework silicate (tectosilicate):\n"
        "Quartz is built from [SiO4]⁴⁻ tetrahedra.\n"
        "Step 2: Complete corner sharing:\n"
        "Every oxygen atom is shared between two silicon atoms (Si:O ratio = 1:2). With no weak cleavage planes and strong covalent Si-O bonds throughout, quartz resists chemical acid attack and mechanical abrasion, dominating beach and desert sands."
    )
    return {
        "id": f"ns9_lith_31_{rng.randint(100000, 999999)}",
        "subskill": "31_quartz_silicon_dioxide_tetrahedral_crystal_network",
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
            "tier_1": "What 3D atomic network gives quartz its hardness?",
            "tier_2": "A framework of covalently bonded silicon-oxygen tetrahedra.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["quartz_silicate_tetrahedral_framework"]
    }


def arch_32_feldspar_group_most_abundant_crustal_mineral(rng: random.Random) -> Dict[str, Any]:
    pct = rng.choice(["nearly 60%", "approximately 50% to 60%"])
    prompt = (
        f"The **feldspar mineral group** (including orthoclase and plagioclase) constitutes {pct} of Earth's crust by weight.\n\n"
        "When feldspar minerals undergo chemical weathering by acidic rainwater (hydrolysis), what essential soil material do they break down into?"
    )
    correct = "Soft, fine-grained clay minerals (such as kaolinite) and dissolved silica and potassium/sodium ions."
    options = [
        correct,
        "Pure liquid gold and molten silver nuggets.",
        "Radioactive uranium fuel rods.",
        "Hard diamond crystals that form mountain peaks."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Abundance of feldspar:\n"
        "Feldspars are aluminosilicates containing K, Na, or Ca.\n"
        "Step 2: Hydrolysis weathering:\n"
        "2KAlSi3O8 (feldspar) + 2H2CO3 + 9H2O → Al2Si2O5(OH)4 (kaolinite clay) + 2K⁺ + 2HCO3⁻ + 4H4SiO4.\n"
        "Chemical weathering of crustal feldspar is the primary source of Earth's fertile clay soils."
    )
    return {
        "id": f"ns9_lith_32_{rng.randint(100000, 999999)}",
        "subskill": "32_feldspar_group_most_abundant_crustal_mineral",
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
            "tier_1": "What does feldspar weather into in soils?",
            "tier_2": "Fine-grained clay minerals (like kaolinite).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["feldspar_abundance_and_clay_weathering"]
    }


def arch_33_calcite_calcium_carbonate_effervescence_acid_test(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the field, geologists carry a small dropper bottle of dilute hydrochloric acid (HCl) to perform a definitive diagnostic test for the mineral **calcite (CaCO3)**.\n\n"
        "What observable reaction occurs when dilute acid is dropped onto a sample of calcite, and what gas is released?"
    )
    correct = "Vigorous effervescence (bubbling/fizzing) as the acid reacts with calcium carbonate to release carbon dioxide gas (CO2)."
    options = [
        correct,
        "The mineral catches fire and burns with a bright green flame, releasing sulfur gas.",
        "The mineral instantly turns into liquid gold with zero bubbles.",
        "The mineral freezes into solid ice cubes, releasing liquid nitrogen."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Chemical acid test:\n"
        "CaCO3(s) + 2HCl(aq) → CaCl2(aq) + H2O(l) + CO2(g)↑.\n"
        "Step 2: Diagnostic value:\n"
        "The vigorous effervescence (fizzing) of escaping CO2 gas definitively identifies carbonate minerals (calcite) and carbonate rocks (limestone, marble)."
    )
    return {
        "id": f"ns9_lith_33_{rng.randint(100000, 999999)}",
        "subskill": "33_calcite_calcium_carbonate_effervescence_acid_test",
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
            "tier_1": "What gas causes the fizzing when acid touches calcite?",
            "tier_2": "Carbon dioxide (CO2) gas bubbles (effervescence).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["calcite_acid_test_effervescence_co2"]
    }


def arch_34_hematite_and_magnetite_iron_ore_oxide_minerals(rng: random.Random) -> Dict[str, Any]:
    ore, formula, feat = rng.choice([
        ("Hematite", "Fe2O3", "characteristic reddish-brown streak when scratched against an unglazed porcelain plate"),
        ("Magnetite", "Fe3O4", "strong natural ferromagnetism that easily attracts steel compass needles and magnets")
    ])
    prompt = (
        f"South Africa mines millions of tonnes of iron ore at Sishen and Kolomela in the Northern Cape. The primary ore mineral is **{ore}** ({formula}).\n\n"
        f"What diagnostic physical property identifies **{ore}** in mineral hand samples?"
    )
    correct = f"Its {feat}."
    options = [
        correct,
        "Its ability to dissolve completely in ordinary tap water within ten seconds.",
        "Its bright neon pink color and soft rubbery texture.",
        "Its tendency to evaporate into a gas at room temperature."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Properties of {ore}:\n"
        f"{ore} ({formula}) is a major iron oxide ore.\n"
        f"Step 2: Diagnostic identification:\n"
        f"It is identified by its {feat}."
    )
    return {
        "id": f"ns9_lith_34_{rng.randint(100000, 999999)}",
        "subskill": "34_hematite_and_magnetite_iron_ore_oxide_minerals",
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
            "tier_1": f"What is the key diagnostic property of {ore}?",
            "tier_2": f"It is identified by its {feat[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["iron_ore_minerals_hematite_magnetite"]
    }


def arch_35_top_eight_abundant_elements_in_earths_crust(rng: random.Random) -> Dict[str, Any]:
    elem, pct, rank = rng.choice([
        ("Oxygen (O)", "~46,6%", "1st (most abundant element in the crust)"),
        ("Silicon (Si)", "~27,7%", "2nd most abundant element"),
        ("Aluminum (Al)", "~8,1%", "3rd most abundant (most abundant metal)"),
        ("Iron (Fe)", "~5,0%", "4th most abundant element")
    ])
    prompt = (
        "Chemical analysis of rocks reveals that just eight chemical elements account for over 98% of the total mass of Earth's crust.\n\n"
        f"Which element ranks as the **{rank}**, making up approximately **{pct}** of crustal mass?"
    )
    correct = f"{elem}."
    options = [
        correct,
        "Gold (Au).",
        "Uranium (U).",
        "Carbon (C)."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Top elements in Earth's crust by mass:\n"
        "1. Oxygen (~46,6%), 2. Silicon (~27,7%), 3. Aluminum (~8,1%), 4. Iron (~5,0%), 5. Calcium (~3,6%), 6. Sodium (~2,8%), 7. Potassium (~2,6%), 8. Magnesium (~2,1%).\n"
        f"Step 2: The {rank} is {elem}."
    )
    return {
        "id": f"ns9_lith_35_{rng.randint(100000, 999999)}",
        "subskill": "35_top_eight_abundant_elements_in_earths_crust",
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
            "tier_1": f"Recall the crustal element ranking for {rank}.",
            "tier_2": f"It is {elem}.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["crustal_element_abundance_rankings"]
    }


def arch_36_silicon_and_oxygen_dominance_silicate_minerals(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Together, **oxygen and silicon** make up approximately 75% of the total mass of the Earth's continental crust.\n\n"
        "What fundamental chemical building block forms the basis for the vast family of silicate minerals that dominate the lithosphere?"
    )
    correct = "The silicon-oxygen tetrahedron: a central silicon ion (Si⁴⁺) covalently bonded to four surrounding oxygen ions (O²⁻) in a pyramid-like structure [SiO4]⁴⁻."
    options = [
        correct,
        "A hexagonal carbon ring composed of pure diamond atoms.",
        "A metallic iron cube bonded to six liquid mercury atoms.",
        "A linear chain of water molecules frozen under atmospheric pressure."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Silicate building block:\n"
        "Over 90% of crustal minerals are silicates.\n"
        "Step 2: Tetrahedron geometry:\n"
        "The fundamental unit is the [SiO4]⁴⁻ tetrahedron. Tetrahedra link together in isolated units (olivine), single chains (pyroxenes), double chains (amphiboles), sheets (micas), or 3D frameworks (quartz, feldspar)."
    )
    return {
        "id": f"ns9_lith_36_{rng.randint(100000, 999999)}",
        "subskill": "36_silicon_and_oxygen_dominance_silicate_minerals",
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
            "tier_1": "What geometric pyramid of silicon and four oxygens forms silicates?",
            "tier_2": "The silicon-oxygen tetrahedron ([SiO4]⁴⁻).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["silicate_tetrahedron_building_block"]
    }


def arch_37_mohs_hardness_scale_talc_to_diamond_scratch_test(rng: random.Random) -> Dict[str, Any]:
    test_pair = rng.choice([
        ("a copper coin (hardness ~3,5)", "calcite (hardness 3)", "The copper coin will scratch calcite because 3,5 > 3."),
        ("a steel knife blade (hardness ~5,5)", "orthoclase feldspar (hardness 6)", "The steel knife will NOT scratch feldspar because 5,5 < 6."),
        ("a quartz crystal (hardness 7)", "window glass (hardness ~5,5)", "Quartz will easily scratch window glass because 7 > 5,5.")
    ])
    item, target, outcome = test_pair
    prompt = (
        "The **Mohs Hardness Scale** ranks minerals from 1 (softest, talc) to 10 (hardest, diamond) based on scratch resistance.\n\n"
        f"If a learner performs a scratch test using **{item}** against **{target}**, what outcome will occur?"
    )
    correct = outcome
    options = [
        correct,
        "Both objects will explode into liquid magma upon contact.",
        "The softer object will cut the harder object in half effortlessly.",
        "Both objects will permanently fuse into a single solid diamond."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Mohs scratch rule:\n"
        "A harder mineral or material will scratch a softer one; a softer material cannot scratch a harder one.\n"
        f"Step 2: Application:\n"
        f"{outcome}"
    )
    return {
        "id": f"ns9_lith_37_{rng.randint(100000, 999999)}",
        "subskill": "37_mohs_hardness_scale_talc_to_diamond_scratch_test",
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
            "tier_1": "Can a softer material scratch a harder material?",
            "tier_2": "No, only the harder material scratches the softer one.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mohs_hardness_scratch_test_rules"]
    }


def arch_38_mineral_cleavage_planes_vs_fracture_patterns(rng: random.Random) -> Dict[str, Any]:
    min_name, behavior = rng.choice([
        ("Mica (biotite/muscovite)", "perfect basal cleavage in one direction, splitting into paper-thin, flexible sheets along weak atomic bonds"),
        ("Halite (rock salt)", "cubic cleavage in three directions at 90° angles, breaking into perfect miniature cubes"),
        ("Quartz", "conchoidal fracture with curved, shell-like break surfaces because chemical bonds are equally strong in all 3D directions")
    ])
    prompt = (
        "When minerals break, they exhibit either **cleavage** or **fracture**.\n\n"
        f"What breakage behavior characterizes the mineral **{min_name}**, and what atomic arrangement causes it?"
    )
    correct = f"It exhibits {behavior}."
    options = [
        correct,
        "It explodes into radioactive sparks whenever dropped on the floor.",
        "It dissolves into atmospheric steam without breaking into pieces.",
        "It stretches like chewing gum without ever breaking."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Breakage of {min_name}:\n"
        "Cleavage reflects planes of weak chemical bonding within a crystal lattice.\n"
        f"Step 2: Specific pattern:\n"
        f"{min_name} exhibits {behavior}."
    )
    return {
        "id": f"ns9_lith_38_{rng.randint(100000, 999999)}",
        "subskill": "38_mineral_cleavage_planes_vs_fracture_patterns",
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
            "tier_1": f"How does {min_name} break (cleavage or fracture)?",
            "tier_2": f"It exhibits {behavior[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mineral_cleavage_vs_fracture_mechanisms"]
    }


def arch_39_plate_tectonics_lithospheric_plates_convection_drive(rng: random.Random) -> Dict[str, Any]:
    speed_cm = rng.choice(["2 to 10 cm per year", "a few centimeters per year (roughly the speed human fingernails grow)"])
    prompt = (
        f"Earth's lithosphere is divided into major and minor tectonic plates that move across the asthenosphere at {speed_cm}.\n\n"
        "What fundamental internal engine drives the slow movement of these massive tectonic plates?"
    )
    correct = "Thermal convection currents in the semi-solid mantle, aided by 'slab pull' (cold dense oceanic plates sinking at subduction zones) and 'ridge push'."
    options = [
        correct,
        "Ocean currents dragging the sea floor across the surface with water friction.",
        "Atmospheric trade winds blowing against mountain ranges on continents.",
        "The gravitational pull of passing satellites orbiting in outer space."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Heat dissipation from core and mantle:\n"
        "Radioactive decay of U, Th, and K heats the deep mantle.\n"
        "Step 2: Convection and plate motion:\n"
        "Hot lower mantle material rises slowly, cools near the lithosphere, and sinks back down. Tectonic plates ride on these convection cells, with subducting cold slabs pulling the trailing plate along ('slab pull')."
    )
    return {
        "id": f"ns9_lith_39_{rng.randint(100000, 999999)}",
        "subskill": "39_plate_tectonics_lithospheric_plates_convection_drive",
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
            "tier_1": "What heat process in the mantle drives plate tectonics?",
            "tier_2": "Thermal convection currents and subduction slab pull.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mantle_convection_plate_tectonics_engine"]
    }


def arch_40_convergent_plate_boundaries_subduction_and_mountains(rng: random.Random) -> Dict[str, Any]:
    bound_type = rng.choice([
        ("oceanic-continental convergence (e.g. the Andes Mountains)", "denser oceanic plate subducts beneath the lighter continental plate, creating a deep ocean trench and volcanic mountain arc"),
        ("continental-continental collision (e.g. the Himalayas)", "two buoyant continental crusts collide without subducting, crumpling and uplifting colossal non-volcanic fold mountains")
    ])
    name, mechanism = bound_type
    prompt = (
        f"At **convergent plate boundaries**, tectonic plates collide under immense compressive stress.\n\n"
        f"What geological features and processes characterize **{name}**?"
    )
    correct = f"The {mechanism}."
    options = [
        correct,
        "New oceanic crust is created as plates pull apart and create flat salt flats.",
        "Plates slide past each other horizontally without creating any mountains.",
        "The ocean floor opens up into a bottomless vacuum that drains all sea water."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Convergent collision dynamics:\n"
        f"At {name}:\n"
        f"Step 2: Geological outcome:\n"
        f"The {mechanism}."
    )
    return {
        "id": f"ns9_lith_40_{rng.randint(100000, 999999)}",
        "subskill": "40_convergent_plate_boundaries_subduction_and_mountains",
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
            "tier_1": f"What forms during {name[:25]}...?",
            "tier_2": f"Review the outcome: {mechanism[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["convergent_plate_boundary_mechanisms"]
    }


def arch_41_divergent_plate_boundaries_mid_ocean_ridges_rift_valleys(rng: random.Random) -> Dict[str, Any]:
    ex = rng.choice(["the Mid-Atlantic Ridge", "the East Pacific Rise"])
    prompt = (
        f"At **divergent plate boundaries**, such as {ex}, tectonic plates pull away from one another.\n\n"
        "What geological process takes place at mid-ocean ridge divergent boundaries?"
    )
    correct = "Sea-floor spreading: magma wells up from the mantle into the central rift valley, cooling and solidifying to continuously form brand-new basaltic oceanic crust."
    options = [
        correct,
        "Old oceanic plates are folded into giant mountain ranges like the Himalayas.",
        "The crust is destroyed as ocean water boils down to the center of the Earth.",
        "Plates slide horizontally without any magma rising to the surface."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Divergent plate divergence:\n"
        "Tensional stress pulls oceanic lithosphere apart.\n"
        "Step 2: Sea-floor spreading:\n"
        "Decompression melting in the rising mantle generates basaltic magma. The magma fills the axial fissure, solidifying into new seafloor and pushing older crust symmetrically outward."
    )
    return {
        "id": f"ns9_lith_41_{rng.randint(100000, 999999)}",
        "subskill": "41_divergent_plate_boundaries_mid_ocean_ridges_rift_valleys",
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
            "tier_1": "What forms at divergent boundaries under the ocean?",
            "tier_2": "New oceanic crust formed by sea-floor spreading.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["divergent_boundary_seafloor_spreading"]
    }


def arch_42_transform_plate_boundaries_strike_slip_earthquakes(rng: random.Random) -> Dict[str, Any]:
    ex = "the San Andreas Fault in California"
    prompt = (
        f"At **transform plate boundaries**, such as {ex}, two lithospheric plates grind past each other horizontally.\n\n"
        "What geological hazard is prominently associated with transform boundaries, and why is volcanism virtually absent?"
    )
    correct = "Frequent shallow, destructive earthquakes occur as frictional stress locks the fault until it suddenly slips; volcanism is absent because crust is neither subducted into the mantle nor pulled apart to allow magma upwelling."
    options = [
        correct,
        "Massive volcanic super-eruptions occur every week because magma floods the fault.",
        "Deep oceanic trenches form that swallow entire continents.",
        "The plates float into the sky due to gravitational cancellation."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Conservative boundary dynamics:\n"
        "At transform faults, lithosphere is neither created nor destroyed (conservative boundary).\n"
        "Step 2: Earthquakes without volcanism:\n"
        "Plates slide past each other along strike-slip faults. Friction prevents smooth sliding, accumulating immense elastic strain until brittle rupture triggers earthquakes. Because there is no subduction or decompression, volcanic magma does not form."
    )
    return {
        "id": f"ns9_lith_42_{rng.randint(100000, 999999)}",
        "subskill": "42_transform_plate_boundaries_strike_slip_earthquakes",
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
            "tier_1": "Why do transform boundaries have earthquakes but no volcanoes?",
            "tier_2": "Plates slide horizontally; crust is neither created nor melted.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["transform_fault_earthquakes_no_volcanism"]
    }


def arch_43_african_rift_valley_continental_divergence_lithosphere(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The **East African Rift System (EARS)** is an extraordinary geological spectacle cutting through eastern Africa from the Red Sea down to Mozambique.\n\n"
        "What continental plate tectonic process is actively underway in the East African Rift?"
    )
    correct = "Continental rifting: a mantle thermal plume is pulling the African Plate apart into the Nubian and Somali sub-plates, creating normal fault grabens, deep rift lakes, and active volcanoes that will eventually split the continent and create a new ocean."
    options = [
        correct,
        "Continental collision: Africa is smashing into Antarctica to form a new mountain chain.",
        "Glacial erosion: ice sheets are carving canyons across Kenya and Tanzania.",
        "Meteorite impact: an ancient asteroid crater is slowly expanding across the continent."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Continental breakup in action:\n"
        "The East African Rift is an embryonic divergent boundary.\n"
        "Step 2: Tectonic progression:\n"
        "Crustal stretching and upwelling magma create a series of down-faulted rift valleys (grabens) occupied by deep lakes (Tanganyika, Malawi) and volcanoes (Kilimanjaro). In millions of years, the rift will flood with ocean water, separating East Africa into a new island landmass."
    )
    return {
        "id": f"ns9_lith_43_{rng.randint(100000, 999999)}",
        "subskill": "43_african_rift_valley_continental_divergence_lithosphere",
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
            "tier_1": "What is happening to Africa along the East African Rift?",
            "tier_2": "Continental rifting: the continent is actively splitting apart.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["east_african_rift_continental_divergence"]
    }


def arch_44_table_mountain_geological_formation_table_sandstone(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Cape Town's iconic **Table Mountain** exhibits a famous geological unconformity with distinct horizontal rock capping.\n\n"
        "What rock formation forms the flat cliff face of Table Mountain, and upon what older basement rocks does it rest?"
    )
    correct = "Horizontally bedded, weather-resistant quartzitic Table Mountain Sandstone resting unconformably atop eroded older Cape Granite and Malmesbury shale basement rocks."
    options = [
        correct,
        "Dark basaltic lava flows resting on top of molten iron magma.",
        "Soft chalk limestone resting on volcanic pumice deposits.",
        "Pure solid gold ore resting on loose beach sand."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Table Mountain stratigraphy:\n"
        "Formed ~500–450 million years ago (Ordovician Period).\n"
        "Step 2: Rock layers:\n"
        "Ancient sedimentary quartz sand washed from braided rivers into a shallow sea, cementing into tough Table Mountain Sandstone. It lies upon an eroded unconformity surface over Precambrian Malmesbury Group shales and 540-million-year-old intrusive Cape Granite."
    )
    return {
        "id": f"ns9_lith_44_{rng.randint(100000, 999999)}",
        "subskill": "44_table_mountain_geological_formation_table_sandstone",
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
            "tier_1": "What rock forms the cliffs of Table Mountain?",
            "tier_2": "Table Mountain Sandstone resting on granite and shale.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["table_mountain_sandstone_geology"]
    }


def arch_45_karoo_supergroup_sedimentary_strata_and_reptile_fossils(rng: random.Random) -> Dict[str, Any]:
    fossil_rep = rng.choice(["therapsids (mammal-like reptiles such as Lystrosaurus)", "cynodonts (the transitional ancestors of mammals)"])
    prompt = (
        f"South Africa's **Karoo Supergroup** covers nearly two-thirds of the country, containing the world's most complete fossil record of **{fossil_rep}**.\n\n"
        "What sedimentary conditions allowed the Karoo Basin to preserve this peerless 120-million-year fossil timeline?"
    )
    correct = "Continuous, gentle accumulation of fine mud, silt, and sand in a slowly subsiding inland retro-arc basin, which rapidly buried dead organisms in anoxic river floodplains and lake beds."
    options = [
        correct,
        "Violent volcanic eruptions of boiling lava that incinerated and fossilized bones instantly.",
        "Marine coral reefs that extracted bones and turned them into calcium carbonate limestone.",
        "Underground diamond mines that preserved skeletons inside pure carbon crystals."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Karoo Basin subsidence:\n"
        "From ~300 to 180 million years ago (Carboniferous to Jurassic), the Karoo Basin subsided, receiving vast deposits from glacial Dwyka tillite to riverine Beaufort shales.\n"
        "Step 2: Fossil preservation:\n"
        "Periodic river overbank floods deposited fine silt, burying mammal-like reptiles before scavengers or weathering could destroy the skeletons."
    )
    return {
        "id": f"ns9_lith_45_{rng.randint(100000, 999999)}",
        "subskill": "45_karoo_supergroup_sedimentary_strata_and_reptile_fossils",
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
            "tier_1": "What allowed the Karoo to preserve ancient mammal-like reptiles?",
            "tier_2": "Gentle, continuous burial in subsiding river floodplain sediments.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["karoo_supergroup_fossil_preservation"]
    }


def arch_46_drakensberg_basaltic_lava_capping_flood_volcanism(rng: random.Random) -> Dict[str, Any]:
    thick_km = rng.choice([1.4, 1.5, 1.6])
    age_ma = rng.choice([180, 183, 185])
    prompt = (
        f"The towering peaks of the **Drakensberg Escarpment** (uKhahlamba) and the Lesotho highlands feature a massive "
        f"layer of dark basalt rock up to {thick_km} km thick, erupted approximately {age_ma} million years ago.\n\n"
        "What geological event caused these massive flood basalt lavas, and how do they protect the underlying sedimentary strata?"
    )
    correct = (
        "Immense continental flood volcanism during the Jurassic rifting and breakup of the supercontinent Gondwana, "
        "producing tough, erosion-resistant basalt lava caps that shield softer underlying Karoo sandstone from erosion."
    )
    options = [
        correct,
        "A single massive meteorite impact that melted surface quartz into boiling obsidian glass.",
        "Marine coral reefs that were compressed under ocean water and baked into solid granite.",
        "Deep underground magma that cooled slowly over billions of years without ever reaching the surface."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Origin of Drakensberg basalts:\n"
        f"Around {age_ma} Ma, as Gondwana began fracturing, extensive fissure eruptions spewed continental flood basalts.\n"
        "Step 2: Geomorphology:\n"
        "The dense, crystalline basalt cap resists physical weathering, creating the dramatic high-altitude plateau and steep escarpment."
    )
    return {
        "id": f"ns9_lith_46_{rng.randint(100000, 999999)}",
        "subskill": "46_drakensberg_basaltic_lava_capping_flood_volcanism",
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
            "tier_1": "What broke apart when Drakensberg flood basalts poured out?",
            "tier_2": "Breakup of supercontinent Gondwana formed flood basalts.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["drakensberg_flood_basalts_gondwana_breakup"]
    }


def arch_47_bushveld_igneous_complex_platinum_layered_intrusion(rng: random.Random) -> Dict[str, Any]:
    mineral_target = rng.choice(["platinum group metals (PGMs) and chromite", "vanadium and titaniferous magnetite"])
    prompt = (
        f"South Africa's **Bushveld Igneous Complex (BIC)** is the world's premier repository of {mineral_target}.\n\n"
        "By what geological process did these exceptionally rich, layered mineral horizons (such as the Merensky Reef) form?"
    )
    correct = (
        "Fractional crystallization and repeated magma replenishments in a vast, slowly cooling crustal magma chamber, "
        "where dense ore minerals precipitated and settled into distinct horizontal rhythmic layers."
    )
    options = [
        correct,
        "Surface rivers that washed loose gold and platinum nuggets into desert sand dunes.",
        "Sedimentary accumulation of marine shells and organic plant debris in an ancient swamp.",
        "Instant quenching of lava under icy Antarctic glacial sheets."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Bushveld Complex age and nature:\n"
        "Formed ~2.06 billion years ago, BIC is a massive layered ultramafic-to-mafic intrusion.\n"
        "Step 2: Fractional crystallization:\n"
        "As the enormous magma chamber cooled slowly, minerals crystallized at specific temperatures and settled by gravity, "
        "producing predictable, ultra-rich stratiform reef layers."
    )
    return {
        "id": f"ns9_lith_47_{rng.randint(100000, 999999)}",
        "subskill": "47_bushveld_igneous_complex_platinum_layered_intrusion",
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
            "tier_1": "How did minerals separate in the Bushveld magma chamber?",
            "tier_2": "Fractional crystallization and gravity settling in a cooling magma chamber.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["bushveld_complex_fractional_crystallization"]
    }


def arch_48_kimberlite_pipes_volcanic_diamond_transport_from_mantle(rng: random.Random) -> Dict[str, Any]:
    depth_km = rng.choice([150, 160, 180, 200])
    prompt = (
        f"Natural diamonds form under extreme thermodynamic conditions at depths exceeding **{depth_km} km** in Earth's mantle.\n\n"
        "How do diamonds reach the crust where they can be mined in volcanic **kimberlite pipes** without turning into ordinary graphite?"
    )
    correct = (
        "They are transported upward at supersonic speeds by violent, volatile-rich gas eruptions that quench and freeze the diamonds in kimberlite before they can invert into graphite."
    )
    options = [
        correct,
        "They slowly diffuse upward through solid crustal rocks over hundreds of millions of years at gentle room temperature.",
        "They are dissolved in groundwater rivers and precipitated inside sandstone sedimentary beds.",
        "They are formed directly at Earth's surface when lightning bolts strike coal seams in open fields."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Diamond stability zone:\n"
        f"Diamonds require pressures >4.5 GPa and temperatures >1000 °C found only in the mantle root (> {depth_km} km).\n"
        "Step 2: Transport mechanism:\n"
        "Kimberlite magmas are charged with CO2 and H2O, rocketing upward supersonically. This rapid ascent quenches the diamonds, locking their tetrahedral carbon lattice metastably into place."
    )
    return {
        "id": f"ns9_lith_48_{rng.randint(100000, 999999)}",
        "subskill": "48_kimberlite_pipes_volcanic_diamond_transport_from_mantle",
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
            "tier_1": "Why must diamond ascent from the mantle be rapid?",
            "tier_2": "Supersonic volatile-rich volcanic eruption quenches diamonds before graphitization.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["kimberlite_diamond_mantle_transport"]
    }


def arch_49_geological_time_scale_deep_time_rock_record(rng: random.Random) -> Dict[str, Any]:
    earth_age = rng.choice(["4.54 billion years", "approximately 4.5 billion years"])
    prompt = (
        f"Earth is calculated to be **{earth_age}** old based on radiometric dating of ancient meteorites and zircon crystals.\n\n"
        "According to Steno's **Law of Superposition**, what fundamental rule governs undisturbed sedimentary strata?"
    )
    correct = "In an undeformed sequence of sedimentary strata, each layer is older than the one above it and younger than the one below it."
    options = [
        correct,
        "The uppermost top layer is always the oldest layer because it receives sunlight first.",
        "All rock layers worldwide were deposited simultaneously on a single calendar day.",
        "Igneous rocks are always younger than any sedimentary rocks regardless of intrusive contact."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Law of Superposition (Nicolas Steno, 1669):\n"
        "Sedimentary particles settle under gravity, creating horizontal strata.\n"
        "Step 2: Chronological order:\n"
        "The lowest bed was deposited first (oldest), while progressively higher beds were deposited subsequently (younger)."
    )
    return {
        "id": f"ns9_lith_49_{rng.randint(100000, 999999)}",
        "subskill": "49_geological_time_scale_deep_time_rock_record",
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
            "tier_1": "Which sedimentary layer is deposited first?",
            "tier_2": "The bottom bed is the oldest; the top bed is the youngest.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["law_of_superposition_stratigraphy"]
    }


def arch_50_the_lithosphere_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    rock_type = rng.choice(["sedimentary shale containing plant fossils", "foliated gneiss showing light and dark banding", "coarse-grained intrusive granite"])
    if "shale" in rock_type:
        origin = "slow deposition and compaction of muddy sediments in calm lake or river water"
        fam = "sedimentary"
    elif "gneiss" in rock_type:
        origin = "intense regional metamorphism of granite or mudstone under high heat and differential tectonic pressure"
        fam = "metamorphic"
    else:
        origin = "slow subterranean cooling of silica-rich magma deep within the continental crust"
        fam = "igneous"
    prompt = (
        f"A geologist collects an unknown rock specimen identified as **{rock_type}**.\n\n"
        f"Which rock family does this specimen belong to, and what geological pathway created it?"
    )
    correct = f"It belongs to the **{fam}** rock family, formed by {origin}."
    distractors = [
        "It belongs to the igneous family, formed by instant evaporation of mineral water in deep caverns.",
        "It belongs to the sedimentary family, formed when basalt lava bubbles cool in air.",
        "It belongs to the metamorphic family, formed by ocean waves washing gravel onto beach dunes."
    ]
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"Step 1: Identify rock class for {rock_type}:\n"
        f"It is classified as a {fam} rock.\n"
        f"Step 2: Geological mechanism:\n"
        f"Formed by {origin}."
    )
    return {
        "id": f"ns9_lith_50_{rng.randint(100000, 999999)}",
        "subskill": "50_the_lithosphere_comprehensive_diagnostic_autopsy",
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
            "tier_1": f"Which of the three rock families includes {rock_type}?",
            "tier_2": f"{rock_type} is a {fam} rock formed by {origin[:30]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["lithosphere_comprehensive_rock_classification"]
    }


BUILDERS_26_50 = {
    "26_foliated_vs_non_foliated_metamorphic_textures": arch_26_foliated_vs_non_foliated_metamorphic_textures,
    "27_soapstone_talc_softness_and_traditional_carving": arch_27_soapstone_talc_softness_and_traditional_carving,
    "28_rock_cycle_complete_closed_interconversion_network": arch_28_rock_cycle_complete_closed_interconversion_network,
    "29_mineral_definition_five_criteria_inorganic_crystal": arch_29_mineral_definition_five_criteria_inorganic_crystal,
    "30_rock_vs_mineral_aggregate_distinction": arch_30_rock_vs_mineral_aggregate_distinction,
    "31_quartz_silicon_dioxide_tetrahedral_crystal_network": arch_31_quartz_silicon_dioxide_tetrahedral_crystal_network,
    "32_feldspar_group_most_abundant_crustal_mineral": arch_32_feldspar_group_most_abundant_crustal_mineral,
    "33_calcite_calcium_carbonate_effervescence_acid_test": arch_33_calcite_calcium_carbonate_effervescence_acid_test,
    "34_hematite_and_magnetite_iron_ore_oxide_minerals": arch_34_hematite_and_magnetite_iron_ore_oxide_minerals,
    "35_top_eight_abundant_elements_in_earths_crust": arch_35_top_eight_abundant_elements_in_earths_crust,
    "36_silicon_and_oxygen_dominance_silicate_minerals": arch_36_silicon_and_oxygen_dominance_silicate_minerals,
    "37_mohs_hardness_scale_talc_to_diamond_scratch_test": arch_37_mohs_hardness_scale_talc_to_diamond_scratch_test,
    "38_mineral_cleavage_planes_vs_fracture_patterns": arch_38_mineral_cleavage_planes_vs_fracture_patterns,
    "39_plate_tectonics_lithospheric_plates_convection_drive": arch_39_plate_tectonics_lithospheric_plates_convection_drive,
    "40_convergent_plate_boundaries_subduction_and_mountains": arch_40_convergent_plate_boundaries_subduction_and_mountains,
    "41_divergent_plate_boundaries_mid_ocean_ridges_rift_valleys": arch_41_divergent_plate_boundaries_mid_ocean_ridges_rift_valleys,
    "42_transform_plate_boundaries_strike_slip_earthquakes": arch_42_transform_plate_boundaries_strike_slip_earthquakes,
    "43_african_rift_valley_continental_divergence_lithosphere": arch_43_african_rift_valley_continental_divergence_lithosphere,
    "44_table_mountain_geological_formation_table_sandstone": arch_44_table_mountain_geological_formation_table_sandstone,
    "45_karoo_supergroup_sedimentary_strata_and_reptile_fossils": arch_45_karoo_supergroup_sedimentary_strata_and_reptile_fossils,
    "46_drakensberg_basaltic_lava_capping_flood_volcanism": arch_46_drakensberg_basaltic_lava_capping_flood_volcanism,
    "47_bushveld_igneous_complex_platinum_layered_intrusion": arch_47_bushveld_igneous_complex_platinum_layered_intrusion,
    "48_kimberlite_pipes_volcanic_diamond_transport_from_mantle": arch_48_kimberlite_pipes_volcanic_diamond_transport_from_mantle,
    "49_geological_time_scale_deep_time_rock_record": arch_49_geological_time_scale_deep_time_rock_record,
    "50_the_lithosphere_comprehensive_diagnostic_autopsy": arch_50_the_lithosphere_comprehensive_diagnostic_autopsy,
}
