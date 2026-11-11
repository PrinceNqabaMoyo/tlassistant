"""Grade 8 Natural Sciences: Term 1 - Photosynthesis and Respiration (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 1/01. Photosynthesis and respiration.md.
Focus: Photosynthesis mechanism, equations, reactants, products, chlorophyll, leaf structure, starch testing, and investigative experiments.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Photosynthesis radiant to chemical energy conversion
def arch_01_photosynthesis_radiant_to_chemical_energy_conversion(rng: random.Random) -> Dict[str, Any]:
    plants = [
        ("maize crops (*Zea mays*) in the Free State", "grains of sweet corn"),
        ("indigenous Rooibos shrubs (*Aspalathus linearis*) in the Cederberg", "leaves used for herbal tea"),
        ("sunflowers (*Helianthus annuus*) in Mpumalanga", "nutrient-rich oily seeds"),
    ]
    crop, product = rng.choice(plants)
    prompt = (
        f"Consider {crop}. Green leaves absorb radiant energy from sunlight and convert it into chemical potential energy "
        f"stored in {product}.\n\n"
        f"What fundamental biological process carries out this specific energy conversion in green plants?"
    )
    correct = "Photosynthesis"
    options = [
        correct,
        "Cellular respiration",
        "Geological sedimentation",
        "Mechanical transpiration",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify the core energy conversion in plant biology:\n"
        f"- Radiant (light) energy from the Sun is trapped by chlorophyll pigments.\n"
        f"- This energy is converted into chemical potential energy stored in the chemical bonds of glucose molecules.\n\n"
        f"**Step 2:** The process is **{correct}**."
    )
    return {
        "id": f"ns8_pr_01_{rng.randint(100000, 999999)}",
        "subskill": "01_photosynthesis_radiant_to_chemical_energy_conversion",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Recall the process plants use to make food using sunlight.",
            "tier_2": "The word combines 'photo' (light) and 'synthesis' (putting together).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["photosynthesis_energy_conversion_confusion"],
    }


# 02. Photosynthesis word equation and chemical symbols
def arch_02_photosynthesis_word_equation_and_chemical_symbols(rng: random.Random) -> Dict[str, Any]:
    equations = [
        ("carbon dioxide + water -> glucose + oxygen (in the presence of sunlight and chlorophyll)", True),
        ("glucose + oxygen -> carbon dioxide + water + energy", False),
        ("carbon dioxide + oxygen -> glucose + water", False),
        ("water + glucose -> starch + carbon dioxide", False),
    ]
    correct = equations[0][0]
    options = [eq[0] for eq in equations]
    rng.shuffle(options)
    prompt = (
        f"Photosynthesis is the fundamental chemical reaction sustaining ecosystems on Earth.\n\n"
        f"Which of the following represents the correct word equation for photosynthesis in green plants?"
    )
    sol = (
        f"**Step 1:** Identify the chemical reactants and products of photosynthesis:\n"
        f"- Reactants: carbon dioxide ($\text{{CO}}_2$) + water ($\text{{H}}_2\text{{O}}$)\n"
        f"- Conditions: radiant light energy and chlorophyll\n"
        f"- Products: glucose ($\text{{C}}_6\text{{H}}_{{12}}\text{{O}}_6$) + oxygen ($\text{{O}}_2$)\n\n"
        f"**Step 2:** The correct word equation is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_02_{rng.randint(100000, 999999)}",
        "subskill": "02_photosynthesis_word_equation_and_chemical_symbols",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What two raw materials go in, and what food and gas come out?",
            "tier_2": "Carbon dioxide and water react to form glucose and oxygen.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["photosynthesis_equation_reversal_error"],
    }


# 03. Photosynthesis reactants carbon dioxide and water
def arch_03_photosynthesis_reactants_carbon_dioxide_and_water(rng: random.Random) -> Dict[str, Any]:
    sources = [
        ("carbon dioxide", "the surrounding atmospheric air via microscopic pores called stomata on leaves", "water", "the moist soil through root hair cells via osmosis"),
        ("water", "the soil by root osmosis and transported up through xylem vessels", "carbon dioxide", "the atmosphere through stomatal apertures"),
    ]
    chosen = rng.choice(sources)
    target_gas = chosen[0]
    target_source = chosen[1]
    prompt = (
        f"During photosynthesis, green plants synthesize glucose using two primary inorganic chemical reactants: "
        f"**{chosen[0]}** and **{chosen[2]}**.\n\n"
        f"From which specific environmental source does a terrestrial plant obtain its **{target_gas}**?"
    )
    correct = f"From {target_source}"
    options = [
        correct,
        "From solid granite rocks absorbed directly through bark",
        "From moonlight absorbed by flower petals at midnight",
        "From digestive enzymes produced by subterranean earthworms",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify plant uptake mechanisms:\n"
        f"- Carbon dioxide is absorbed directly from the air through open stomata.\n"
        f"- Water is absorbed from the soil by root hair cells and pulled upward through xylem vessels.\n\n"
        f"**Step 2:** The plant obtains {target_gas} **{correct.lower()}**."
    )
    return {
        "id": f"ns8_pr_03_{rng.randint(100000, 999999)}",
        "subskill": "03_photosynthesis_reactants_carbon_dioxide_and_water",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Where does a plant take in {target_gas}: air or soil?",
            "tier_2": f"Consider whether {target_gas} is taken in via leaves or roots.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["plant_nutrient_source_misconception"],
    }


# 04. Photosynthesis products glucose and oxygen
def arch_04_photosynthesis_products_glucose_and_oxygen(rng: random.Random) -> Dict[str, Any]:
    products = [
        ("glucose (simple sugar)", "organic chemical food containing chemical potential energy used by the plant and herbivores"),
        ("oxygen gas", "a vital gaseous by-product released into the atmosphere that sustains aerobic respiration in living organisms"),
    ]
    product, role = rng.choice(products)
    prompt = (
        f"Photosynthesis yields two primary chemical products: **glucose** and **oxygen**.\n\n"
        f"What is the biological significance of **{product}** in the biosphere?"
    )
    correct = f"It serves as {role}."
    options = [
        correct,
        "It acts as liquid nitrogen to freeze soil microbes solid.",
        "It transforms plant stems into pure volcanic quartz crystals.",
        "It stops all animal reproduction by emitting high-frequency radio waves.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the dual outputs of photosynthesis:\n"
        f"- Glucose: the basic chemical fuel produced by plants, supporting food webs.\n"
        f"- Oxygen: released through stomata into the atmosphere, allowing aerobic organisms to respire.\n\n"
        f"**Step 2:** The primary role of {product} is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_04_{rng.randint(100000, 999999)}",
        "subskill": "04_photosynthesis_products_glucose_and_oxygen",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"How is {product} used by living things?",
            "tier_2": "Glucose provides energy; oxygen provides gas for aerobic breathing.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["photosynthesis_product_roles_misconception"],
    }


# 05. Role of chlorophyll trapping radiant energy
def arch_05_role_of_chlorophyll_trapping_radiant_energy(rng: random.Random) -> Dict[str, Any]:
    pigment_names = ["chlorophyll", "carotenoids", "anthocyanin"]
    prompt = (
        f"Green leaves contain the specialized pigment **chlorophyll**. "
        f"What is the exact biological function of chlorophyll during photosynthesis, "
        f"and what happens to the chlorophyll molecule after the reaction occurs?"
    )
    correct = (
        "Chlorophyll traps radiant light energy from the Sun and transfers it into the reaction; "
        "chlorophyll is neither consumed nor created during the process."
    )
    options = [
        correct,
        "Chlorophyll is completely destroyed and eaten as food by the plant during every minute of sunlight.",
        "Chlorophyll turns directly into glucose molecules by losing all its green colour permanently.",
        "Chlorophyll absorbs heavy metals from the air to build the cell walls of the plant.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the role of chlorophyll:\n"
        f"- Chlorophyll is a green light-absorbing pigment in chloroplasts.\n"
        f"- Its sole function is to absorb radiant energy from sunlight and channel that energy to drive chemical bond formation.\n"
        f"- It is not used up or manufactured as a product in the reaction.\n\n"
        f"**Step 2:** The true statement is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_05_{rng.randint(100000, 999999)}",
        "subskill": "05_role_of_chlorophyll_trapping_radiant_energy",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Is chlorophyll a fuel that gets burned up, or a pigment that absorbs light?",
            "tier_2": "Chlorophyll traps radiant energy and is not consumed in the reaction.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["chlorophyll_consumed_misconception"],
    }


# 06. Chloroplast organelle structure and function (with dynamic SVG)
def arch_06_chloroplast_organelle_structure_and_function(rng: random.Random) -> Dict[str, Any]:
    granum_count = rng.randint(3, 5)
    leaf_cell_type = rng.choice(["palisade mesophyll cell", "spongy mesophyll cell"])
    green_shade = rng.choice(["#22c55e", "#16a34a", "#15803d"])

    svg = (
        f'<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="210" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Chloroplast Organelle in {leaf_cell_type}</text>'
        f'<ellipse cx="210" cy="120" rx="170" ry="75" fill="#dcfce7" stroke="{green_shade}" stroke-width="3" />'
        f'<ellipse cx="210" cy="120" rx="155" ry="65" fill="#f0fdf4" stroke="{green_shade}" stroke-width="1.5" stroke-dasharray="4,2" />'
        f'<g fill="{green_shade}">'
        f'<rect x="90" y="90" width="30" height="10" rx="3" /><rect x="90" y="105" width="30" height="10" rx="3" /><rect x="90" y="120" width="30" height="10" rx="3" /><rect x="90" y="135" width="30" height="10" rx="3" />'
        f'<rect x="150" y="85" width="30" height="10" rx="3" /><rect x="150" y="100" width="30" height="10" rx="3" /><rect x="150" y="115" width="30" height="10" rx="3" /><rect x="150" y="130" width="30" height="10" rx="3" />'
        f'<rect x="210" y="90" width="30" height="10" rx="3" /><rect x="210" y="105" width="30" height="10" rx="3" /><rect x="210" y="120" width="30" height="10" rx="3" />'
        f'<rect x="270" y="85" width="30" height="10" rx="3" /><rect x="270" y="100" width="30" height="10" rx="3" /><rect x="270" y="115" width="30" height="10" rx="3" /><rect x="270" y="130" width="30" height="10" rx="3" />'
        f'</g>'
        f'<line x1="330" y1="60" x2="270" y2="105" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow)" />'
        f'<text x="335" y="60" font-size="11" fill="#0f172a" font-weight="bold">Grana (thylakoid stacks)</text>'
        f'<text x="335" y="75" font-size="9" fill="#475569">Chlorophyll pigments here</text>'
        f'<line x1="70" y1="50" x2="130" y2="110" stroke="#334155" stroke-width="1.5" />'
        f'<text x="40" y="45" font-size="11" fill="#0f172a" font-weight="bold">Double membrane</text>'
        f'<text x="210" y="205" font-size="10" fill="#475569" text-anchor="middle">Showing {granum_count} major thylakoid granum clusters inside stroma fluid</text>'
        f'</svg>'
    )

    prompt = (
        f"In plant leaves, photosynthesis takes place inside specialized microscopic cellular structures "
        f"called **chloroplasts**, located primarily in the {leaf_cell_type}.\n\n"
        f"Why are chloroplasts found in plant cells but absent in almost all animal cells?"
    )
    correct = (
        "Plants are autotrophic producers that manufacture their own food via photosynthesis, "
        "whereas animals are heterotrophs that must ingest organic food produced by other organisms."
    )
    options = [
        correct,
        "Animal cells are too small to fit any internal organelles or nucleus.",
        "Animals possess chloroplasts until they reach 5 years of age, after which they shed them.",
        "Chloroplasts produce toxic cyanide if placed inside animal tissue.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Contrast plant autotrophy with animal heterotrophy:\n"
        f"- Plants produce their own glucose using chloroplasts containing chlorophyll.\n"
        f"- Animals are heterotrophic consumers: they obtain chemical energy by feeding on plants or other animals, so they do not require photosynthetic machinery.\n\n"
        f"**Step 2:** The fundamental biological reason is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_06_{rng.randint(100000, 999999)}",
        "subskill": "06_chloroplast_organelle_structure_and_function",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "hints": {
            "tier_1": "Can animals produce their own food from sunlight?",
            "tier_2": "Plants are producers (autotrophs) while animals are consumers (heterotrophs).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["autotroph_heterotroph_chloroplast_misconception"],
    }


# 07. Leaf adaptations for photosynthesis stomata and mesophyll
def arch_07_leaf_adaptations_for_photosynthesis_stomata_and_mesophyll(rng: random.Random) -> Dict[str, Any]:
    adaptations = [
        ("broad, flattened leaf lamina (blade)", "maximises the surface area available to intercept and absorb sunlight"),
        ("thin leaf cross-section", "minimises diffusion distance for carbon dioxide entering internal cells"),
        ("tightly packed palisade mesophyll cells near the upper surface", "densely loaded with chloroplasts to capture maximum light rays"),
        ("waxy, transparent upper cuticle", "prevents excessive water loss while allowing sunlight to penetrate directly into photosynthetic cells"),
    ]
    feature, advantage = rng.choice(adaptations)
    prompt = (
        f"Plant leaves exhibit several structural adaptations to maximise the efficiency of photosynthesis.\n\n"
        f"What specific functional advantage is provided by the **{feature}**?"
    )
    correct = f"It {advantage}."
    options = [
        correct,
        "It produces high-voltage electricity to repel herbivores.",
        "It acts as a mechanical pump to circulate blood throughout the root system.",
        "It absorbs nitrogen gas to produce volcanic lava on the leaf margins.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the structural adaptation:\n"
        f"- {feature.capitalize()}: adapted to optimise sunlight capture and gas diffusion.\n"
        f"- Specifically, it {advantage}.\n\n"
        f"**Step 2:** The correct physiological function is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_07_{rng.randint(100000, 999999)}",
        "subskill": "07_leaf_adaptations_for_photosynthesis_stomata_and_mesophyll",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Think about how {feature} helps the leaf capture light or gases.",
            "tier_2": f"It {advantage}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["leaf_adaptation_photosynthesis_misconception"],
    }


# 08. Glucose solubility and translocation as sucrose
def arch_08_glucose_solubility_and_translocation_as_sucrose(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Glucose produced in leaf cells is highly **soluble** in water. "
        f"Why is this water-solubility of glucose a biological advantage for internal transport, "
        f"and through which specialized plant tissue is this sugar translocated to other organs?"
    )
    correct = (
        "Being soluble allows glucose to dissolve in water and be transported readily in sap "
        "through the **phloem** vessels to roots, fruits, and growing buds."
    )
    options = [
        correct,
        "Being soluble allows glucose to evaporate into steam and travel through dry air tubes in the wood.",
        "Being soluble enables glucose to turn into diamond crystals inside dead xylem vessels.",
        "Solubility causes glucose to be destroyed immediately so the plant does not gain weight.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand glucose transport in plants:\n"
        f"- Glucose is a simple soluble monosaccharide sugar.\n"
        f"- Because it dissolves readily in water, it can be transported in aqueous solution through the **phloem** tissue.\n"
        f"- Phloem translocates manufactured nutrients from leaves ('source') to roots and storage organs ('sink').\n\n"
        f"**Step 2:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_08_{rng.randint(100000, 999999)}",
        "subskill": "08_glucose_solubility_and_translocation_as_sucrose",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Which vascular tissue transports organic sugars: xylem or phloem?",
            "tier_2": "Phloem transports dissolved food substances to non-photosynthetic organs.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["xylem_phloem_translocation_confusion"],
    }


# 09. Glucose conversion to insoluble storage starch
def arch_09_glucose_conversion_to_insoluble_storage_starch(rng: random.Random) -> Dict[str, Any]:
    storage_organs = [
        ("potato tubers (*Solanum tuberosum*) underground", "potato starch granules"),
        ("sweet potato roots (*Ipomoea batatas*)", "dense starch deposits"),
        ("maize kernels on a cob", "starch grains within the endosperm"),
    ]
    organ, deposit = rng.choice(storage_organs)
    prompt = (
        f"Plants convert surplus glucose into **starch** for storage in {organ}. "
        f"Starch is **insoluble** in water.\n\n"
        f"Why must a plant convert soluble glucose into insoluble starch for long-term storage?"
    )
    correct = (
        "Insoluble starch does not dissolve in cell water, preventing osmotic disruption "
        "(water from rushing into cells) and preventing the food from washing away."
    )
    options = [
        correct,
        "Because starch is poisonous to all plant-eating animals and insects.",
        "Because glucose is a non-living mineral that cannot be held inside living cells.",
        "Because starch weighs nothing and allows plants to float into the sky.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the osmotic and physical implications of starch storage:\n"
        f"- If large amounts of soluble glucose remained in cells, osmotic potential would drop sharply, causing excessive water influx and cell swelling/bursting.\n"
        f"- Converting glucose into large, compact, insoluble starch polymers keeps the storage inert, stable, and osmotically neutral.\n\n"
        f"**Step 2:** The justification is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_09_{rng.randint(100000, 999999)}",
        "subskill": "09_glucose_conversion_to_insoluble_storage_starch",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What would happen to cell water balance if thousands of soluble sugar particles dissolved inside?",
            "tier_2": "Insoluble starch prevents water from being drawn in by osmosis and stays stored safely.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["starch_storage_osmotic_misconception"],
    }


# 10. Other glucose fates cellulose proteins lipids
def arch_10_other_glucose_fates_cellulose_proteins_lipids(rng: random.Random) -> Dict[str, Any]:
    compounds = [
        ("cellulose", "combining glucose units into strong insoluble fibres to construct rigid cell walls for structural support"),
        ("plant oils and lipids (e.g. sunflower seed oil)", "converting glucose into energy-dense fatty reserves for seeds and embryo nourishment"),
        ("proteins and enzymes", "combining glucose carbon skeletons with mineral nitrates absorbed from the soil to build protoplasm"),
    ]
    substance, function = rng.choice(compounds)
    prompt = (
        f"Not all glucose manufactured during photosynthesis is stored as starch or burned in respiration. "
        f"Plants convert glucose into various vital organic molecules.\n\n"
        f"What is the biological role of **{substance}** synthesized by the plant from glucose?"
    )
    correct = f"It is used for {function}."
    options = [
        correct,
        "It is transformed into radioactive uranium to power cellular nuclear reactions.",
        "It is expelled into deep underground caves to attract earthworms for company.",
        "It acts as a metallic shield to stop atmospheric oxygen from touching the plant.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace secondary metabolic pathways from glucose:\n"
        f"- Cellulose: structural polysaccharide forming plant cell walls.\n"
        f"- Lipids: energy-dense storage in seeds (e.g. canola, sunflower).\n"
        f"- Proteins: built from glucose + nitrogen (nitrates) for cellular enzymes and tissue repair.\n\n"
        f"**Step 2:** The correct role for {substance} is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_10_{rng.randint(100000, 999999)}",
        "subskill": "10_other_glucose_fates_cellulose_proteins_lipids",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Think about what plant structure or reserve is made from {substance}.",
            "tier_2": f"It is used for {function}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["glucose_fate_cellulose_protein_misconception"],
    }


# 11. Iodine test for starch colour change
def arch_11_iodine_test_for_starch_colour_change(rng: random.Random) -> Dict[str, Any]:
    food_items = [
        ("a freshly cut raw potato slice", "blue-black", True),
        ("a teaspoon of pure white maize cornstarch in a petri dish", "blue-black", True),
        ("a piece of boiled egg white containing only albumin protein", "yellow-brown (no change)", False),
        ("a slice of white bread made from wheat flour", "blue-black", True),
    ]
    item, observed_color, is_starch = rng.choice(food_items)
    prompt = (
        f"A learner adds a few drops of **iodine solution** to {item}. "
        f"What colour change indicates the presence of starch, and what will be observed in this test?"
    )
    if is_starch:
        correct = f"Iodine changes from yellow-brown to **blue-black**, confirming the presence of starch."
    else:
        correct = f"The iodine remains **yellow-brown (no colour change)**, confirming that starch is absent."
    options = [
        correct,
        "The solution turns brilliant neon pink, confirming that starch has turned into salt.",
        "The food immediately bubbles violently producing toxic purple chlorine gas.",
        "The food dissolves completely into transparent liquid mercury within 1 second.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recall the diagnostic colour test for starch:\n"
        f"- Reagent: Iodine solution (originally yellow-brown / amber-brown).\n"
        f"- Positive result (starch present): turns intense **blue-black**.\n"
        f"- Negative result (no starch): remains **yellow-brown**.\n\n"
        f"**Step 2:** For {item}, the correct observation is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_11_{rng.randint(100000, 999999)}",
        "subskill": "11_iodine_test_for_starch_colour_change",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What colour does iodine turn when dropped on bread or potato?",
            "tier_2": "Iodine turns blue-black in the presence of starch.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["iodine_colour_test_misconception"],
    }


# 12. Destarching plants purpose and protocol
def arch_12_destarching_plants_purpose_and_protocol(rng: random.Random) -> Dict[str, Any]:
    hours = rng.choice([24, 48])
    plant_type = rng.choice(["potted geranium (*Pelargonium*) plant", "potted bean seedling"])
    prompt = (
        f"Before conducting any investigation to test whether light or carbon dioxide is necessary for photosynthesis, "
        f"scientists place a healthy {plant_type} in a dark cupboard for {hours} hours.\n\n"
        f"What is the scientific purpose of this 'destarching' step?"
    )
    correct = (
        f"To ensure that all pre-existing starch stored in the leaves is converted to glucose and used up in respiration, "
        f"guaranteeing that any starch detected later was newly made during the experiment."
    )
    options = [
        correct,
        "To kill the plant completely so that it stops absorbing water from the soil.",
        "To bleach the green chlorophyll out of the leaves using darkness.",
        "To convert all cellulose in the cell walls into pure crystalline cane sugar.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the role of experimental destarching:\n"
        f"- If leaves already contain starch from the previous days of sun, any starch test will test positive regardless of experimental conditions.\n"
        f"- In the dark for {hours} hours, photosynthesis stops, but cellular respiration continues.\n"
        f"- The plant breaks down all stored leaf starch into glucose to sustain its life processes, clearing the leaves of starch.\n\n"
        f"**Step 2:** The purpose is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_12_{rng.randint(100000, 999999)}",
        "subskill": "12_destarching_plants_purpose_and_protocol",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Why must you start with leaves that have zero starch inside them?",
            "tier_2": "Destarching ensures any starch detected after the experiment was made during the test.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["destarching_purpose_misconception"],
    }


# 13. Testing leaf for starch step boiling water kills cells
def arch_13_testing_leaf_for_starch_step_boiling_water_kills_cells(rng: random.Random) -> Dict[str, Any]:
    duration_secs = rng.choice([30, 60, 90])
    prompt = (
        f"When testing a leaf for starch in the laboratory, **Step 1** involves plunging the fresh leaf into "
        f"a beaker of boiling water for approximately {duration_secs} seconds.\n\n"
        f"What is the exact biological reason for boiling the leaf in water?"
    )
    correct = (
        "It kills the leaf cells, denatures enzymes to stop all chemical reactions immediately, "
        "and breaks down cell membranes so chemicals can penetrate."
    )
    options = [
        correct,
        "It adds extra starch molecules into the leaf from the boiling water.",
        "It cools the leaf down to 0 degrees Celsius to freeze chlorophyll pigments.",
        "It burns off the waxy cuticle using open flames inside the water.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the first step of the leaf starch test:\n"
        f"- Plunging the leaf into boiling water:\n"
        f"  1. Kills living protoplasm and denatures cellular enzymes, arresting metabolic reactions.\n"
        f"  2. Disrupts the selectively permeable cell membranes, increasing permeability for iodine penetration.\n\n"
        f"**Step 2:** The biological reason is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_13_{rng.randint(100000, 999999)}",
        "subskill": "13_testing_leaf_for_starch_step_boiling_water_kills_cells",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What happens to living cells and enzymes when placed in boiling water?",
            "tier_2": "It kills cells, halts reactions, and softens cell membranes.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["leaf_boiling_water_purpose_misconception"],
    }


# 14. Testing leaf for starch step ethanol water bath safety (with dynamic SVG)
def arch_14_testing_leaf_for_starch_step_ethanol_water_bath_safety(rng: random.Random) -> Dict[str, Any]:
    temp_c = rng.choice([78, 80, 85])
    tube_color = rng.choice(["#38bdf8", "#60a5fa", "#818cf8"])

    svg = (
        f'<svg viewBox="0 0 380 230" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="190" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Water Bath Decolorisation of Leaf (Ethanol at ~{temp_c}&#176;C)</text>'
        f'<rect x="90" y="90" width="200" height="90" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" rx="4" />'
        f'<text x="190" y="170" font-size="11" fill="#0369a1" text-anchor="middle">Beaker of Hot Water (Water Bath)</text>'
        f'<rect x="170" y="50" width="40" height="110" fill="{tube_color}" fill-opacity="0.3" stroke="#2563eb" stroke-width="2" rx="4" />'
        f'<rect x="175" y="80" width="30" height="75" fill="#22c55e" fill-opacity="0.5" />'
        f'<text x="190" y="115" font-size="10" fill="#14532d" font-weight="bold" text-anchor="middle">Ethanol</text>'
        f'<line x1="220" y1="120" x2="270" y2="120" stroke="#0f172a" stroke-width="1.5" />'
        f'<text x="275" y="123" font-size="10" fill="#0f172a">Leaf loses chlorophyll</text>'
        f'<text x="190" y="210" font-size="10" fill="#dc2626" font-weight="bold" text-anchor="middle">SAFETY: Never heat ethanol directly over a Bunsen flame!</text>'
        f'</svg>'
    )

    prompt = (
        f"In **Step 2** of testing a leaf for starch, the leaf is placed inside a test tube of methylated spirits (ethanol) "
        f"which is heated inside a beaker of hot water (a water bath).\n\n"
        f"What is the function of the ethanol, and why must a water bath be used instead of heating the tube directly over an open Bunsen flame?"
    )
    correct = (
        "Ethanol dissolves and extracts the green chlorophyll pigment (decolorising the leaf so colour changes are visible); "
        "a water bath is mandatory because ethanol is highly flammable and its vapours can easily ignite."
    )
    options = [
        correct,
        "Ethanol turns the starch into sugar; a water bath is used because water freezes ethanol into solid ice.",
        "Ethanol creates oxygen gas; a water bath prevents the test tube from floating to the ceiling.",
        "Ethanol paints the leaf with blue ink; an open flame would turn the leaf into gold metal.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the role of ethanol and lab safety:\n"
        f"- Role: Chlorophyll is insoluble in water but soluble in alcohol (ethanol). Heating extracts chlorophyll, leaving the leaf pale/white so the blue-black iodine colour change can be clearly observed.\n"
        f"- Safety: Ethanol boils at ~78°C and is extremely flammable. Direct heating over an open flame poses a severe fire hazard. A water bath safely transfers heat without open flames.\n\n"
        f"**Step 2:** The dual answer is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_14_{rng.randint(100000, 999999)}",
        "subskill": "14_testing_leaf_for_starch_step_ethanol_water_bath_safety",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "hints": {
            "tier_1": "What property of alcohol makes it dangerous near fire, and what green substance does it remove?",
            "tier_2": "Ethanol extracts green chlorophyll, and it is flammable so it requires a water bath.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ethanol_water_bath_safety_misconception"],
    }


# 15. Testing light requirement opaque foil stencil investigation
def arch_15_testing_light_requirement_opaque_foil_stencil_investigation(rng: random.Random) -> Dict[str, Any]:
    stencil_shape = rng.choice(["a black cardboard strip across the middle", "an opaque star-shaped stencil of aluminum foil"])
    prompt = (
        f"A learner destarches a potted plant, clips {stencil_shape} onto both sides of a green leaf, "
        f"and places the plant in bright sunlight for 6 hours. "
        f"After decolorising the leaf and applying iodine solution, what pattern of results will be observed?"
    )
    correct = (
        f"The exposed areas that received sunlight turn **blue-black** (starch present), "
        f"while the area covered by {stencil_shape} remains **yellow-brown** (no starch produced)."
    )
    options = [
        correct,
        "The entire leaf turns uniform pitch black including all covered sections.",
        "The covered section turns bright purple, while exposed parts dissolve into water.",
        "The entire leaf remains completely transparent with zero chemical reaction anywhere.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the experimental variable (Light):\n"
        f"- Independent variable: presence or absence of sunlight.\n"
        f"- Exposed parts received radiant energy -> photosynthesised -> produced glucose converted to starch -> stained blue-black with iodine.\n"
        f"- Covered part received zero light -> could not photosynthesise -> no starch formed -> stained yellow-brown (iodine color).\n\n"
        f"**Step 2:** The result is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_15_{rng.randint(100000, 999999)}",
        "subskill": "15_testing_light_requirement_opaque_foil_stencil_investigation",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Can the covered part of the leaf perform photosynthesis without light?",
            "tier_2": "Only the uncovered, light-exposed regions can make starch.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["light_requirement_stencil_misconception"],
    }


# 16. Testing chlorophyll requirement variegated leaf investigation
def arch_16_testing_chlorophyll_requirement_variegated_leaf_investigation(rng: random.Random) -> Dict[str, Any]:
    leaf_variety = rng.choice(["a variegated *Coleus* leaf (green center, white border)", "a variegated *Pelargonium* leaf (green zones, creamy-white margins)"])
    prompt = (
        f"To investigate whether chlorophyll is required for photosynthesis, a destarched plant with {leaf_variety} "
        f"is exposed to bright sunlight for several hours. "
        f"The leaf is subsequently plucked, decolorised in an ethanol bath, and stained with iodine.\n\n"
        f"What will be the observed distribution of the blue-black colour?"
    )
    correct = (
        "Only the previously green areas containing chlorophyll turn **blue-black**, "
        "while the white non-green areas remain **yellow-brown**."
    )
    options = [
        correct,
        "The white areas turn blue-black, while the green areas remain yellow-brown.",
        "The entire leaf turns bright orange because chlorophyll repels iodine.",
        "The green areas produce diamonds while the white areas produce table salt.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the role of chlorophyll using variegated leaves:\n"
        f"- Green areas contain chloroplasts with chlorophyll -> can trap sunlight -> produce starch -> stain blue-black.\n"
        f"- White areas lack chlorophyll -> cannot trap light energy -> cannot produce starch -> remain yellow-brown.\n\n"
        f"**Step 2:** The observation is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_16_{rng.randint(100000, 999999)}",
        "subskill": "16_testing_chlorophyll_requirement_variegated_leaf_investigation",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Which part of a variegated leaf contains the pigment that traps sunlight?",
            "tier_2": "Only the green parts with chlorophyll can make starch.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["variegated_leaf_chlorophyll_misconception"],
    }


# 17. Testing carbon dioxide requirement sodium hydroxide investigation
def arch_17_testing_carbon_dioxide_requirement_sodium_hydroxide_investigation(rng: random.Random) -> Dict[str, Any]:
    chemical = rng.choice(["sodium hydroxide (NaOH) pellets / solution", "potassium hydroxide (KOH) solution"])
    prompt = (
        f"In an experiment to determine if carbon dioxide is required for photosynthesis, two destarched potted plants "
        f"are placed under separate transparent sealed bell jars in bright light.\n"
        f"- **Bell Jar A:** Contains a petri dish of **{chemical}**.\n"
        f"- **Bell Jar B:** Contains a petri dish of **pure water**.\n\n"
        f"What is the chemical function of the {chemical} in Jar A, and what will the iodine starch test show on a leaf from Plant A?"
    )
    correct = (
        f"The {chemical} absorbs carbon dioxide from the air inside the jar; "
        f"deprived of CO2, Plant A cannot photosynthesise, so its leaf tests negative for starch (remains yellow-brown)."
    )
    options = [
        correct,
        f"The {chemical} creates vast amounts of extra CO2; Plant A explodes with starch.",
        f"The {chemical} freezes the air; Plant A turns into solid green glass.",
        f"The {chemical} absorbs all water; Plant A drinks carbon dioxide from the glass bell jar directly.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the experimental setup:\n"
        f"- {chemical.capitalize()} reacts with and removes atmospheric carbon dioxide from enclosed air.\n"
        f"- Plant A has sunlight, water, and chlorophyll, but lacks $\text{{CO}}_2$.\n"
        f"- Without $\text{{CO}}_2$, photosynthesis cannot occur: no starch is produced.\n"
        f"- When tested with iodine, the leaf from Plant A remains yellow-brown.\n\n"
        f"**Step 2:** The result is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_17_{rng.randint(100000, 999999)}",
        "subskill": "17_testing_carbon_dioxide_requirement_sodium_hydroxide_investigation",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What does sodium hydroxide or potassium hydroxide do to carbon dioxide in an enclosed space?",
            "tier_2": "It absorbs CO2, starving the plant of the raw material needed to make glucose.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["co2_absorber_naoh_misconception"],
    }


# 18. Testing oxygen production elodea glowing splint test (with dynamic SVG)
def arch_18_testing_oxygen_production_elodea_glowing_splint_test(rng: random.Random) -> Dict[str, Any]:
    bubbles_min = rng.randint(25, 45)
    tube_height = rng.randint(20, 35)

    svg = (
        f'<svg viewBox="0 0 380 240" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="190" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Aquatic Photosynthesis: Gas Collection ({bubbles_min} bubbles/min)</text>'
        f'<rect x="90" y="80" width="200" height="130" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" rx="4" />'
        f'<path d="M 120 190 L 190 120 L 260 190 Z" fill="#94a3b8" fill-opacity="0.4" stroke="#475569" stroke-width="1.5" />'
        f'<text x="190" y="175" font-size="10" fill="#15803d" font-weight="bold" text-anchor="middle">Elodea pondweed</text>'
        f'<rect x="175" y="45" width="30" height="85" fill="#f8fafc" stroke="#334155" stroke-width="1.5" />'
        f'<rect x="176" y="46" width="28" height="{tube_height}" fill="#fef08a" />'
        f'<text x="190" y="{40 + tube_height // 2}" font-size="9" fill="#854d0e" font-weight="bold" text-anchor="middle">O2 gas</text>'
        f'<circle cx="187" cy="110" r="3" fill="#bae6fd" stroke="#0284c7" />'
        f'<circle cx="193" cy="95" r="4" fill="#bae6fd" stroke="#0284c7" />'
        f'<circle cx="189" cy="80" r="3" fill="#bae6fd" stroke="#0284c7" />'
        f'<text x="190" y="228" font-size="10" fill="#0f172a" text-anchor="middle">Gas relights a glowing wooden splint -> proves Oxygen</text>'
        f'</svg>'
    )

    prompt = (
        f"A submerged sprig of Canadian pondweed (*Elodea*) placed under an inverted glass funnel inside a beaker of water "
        f"in bright light releases approximately {bubbles_min} gas bubbles per minute. "
        f"The gas accumulates at the top of an inverted test tube.\n\n"
        f"How is this collected gas scientifically tested, and what is its identity?"
    )
    correct = (
        "Insert a glowing wooden splint into the mouth of the tube; the splint relights (bursts into flame), "
        "proving the gas is **oxygen**."
    )
    options = [
        correct,
        "Bubble the gas through clear limewater; it turns milky white, proving it is pure carbon monoxide.",
        "Add table salt to the gas; it turns into strawberry milkshake, proving it is helium.",
        "Expose the gas to a magnet; the gas sticks to the magnet, proving it is iron vapor.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify the gas produced and its standard confirmation test:\n"
        f"- Photosynthesis by submerged green plants releases oxygen gas bubbles ({bubbles_min} bubbles/min).\n"
        f"- The diagnostic confirmation test for oxygen: a glowing (embering) wooden splint relights with a flame.\n\n"
        f"**Step 2:** The test and identity: **{correct}**."
    )
    return {
        "id": f"ns8_pr_18_{rng.randint(100000, 999999)}",
        "subskill": "18_testing_oxygen_production_elodea_glowing_splint_test",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "hints": {
            "tier_1": "What gas is released as a by-product during photosynthesis?",
            "tier_2": "Oxygen relights a glowing splint.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["oxygen_glowing_splint_test_misconception"],
    }


# 19. Rate of photosynthesis light intensity bubbles per minute
def arch_19_rate_of_photosynthesis_light_intensity_bubbles_per_minute(rng: random.Random) -> Dict[str, Any]:
    distances = [
        (10, rng.randint(48, 55)),
        (20, rng.randint(32, 38)),
        (30, rng.randint(18, 24)),
        (40, rng.randint(8, 12)),
    ]
    near_dist, near_rate = distances[0]
    far_dist, far_rate = distances[3]
    prompt = (
        f"A learner measures the rate of photosynthesis in an *Elodea* shoot by counting oxygen bubbles emitted per minute "
        f"as a desk lamp is moved to different distances:\n"
        f"- At {near_dist} cm distance: {near_rate} bubbles/min\n"
        f"- At {far_dist} cm distance: {far_rate} bubbles/min\n\n"
        f"What general biological relationship between light intensity and the rate of photosynthesis does this experiment demonstrate?"
    )
    correct = (
        "As light intensity increases (closer lamp distance), the rate of photosynthesis increases proportionally "
        "until another environmental factor becomes limiting."
    )
    options = [
        correct,
        "Moving the lamp closer causes the plant to enter deep winter hibernation.",
        "Light intensity has zero measurable effect on plant photosynthetic activity.",
        "Increased light causes plants to absorb oxygen and release nitrogen liquid.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the data trend:\n"
        f"- At {near_dist} cm (higher light intensity), rate is {near_rate} bubbles/min.\n"
        f"- At {far_dist} cm (lower light intensity), rate drops to {far_rate} bubbles/min.\n"
        f"- Conclusion: Rate of photosynthesis is directly stimulated by light intensity.\n\n"
        f"**Step 2:** The relationship is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_19_{rng.randint(100000, 999999)}",
        "subskill": "19_rate_of_photosynthesis_light_intensity_bubbles_per_minute",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does more light speed up or slow down photosynthesis?",
            "tier_2": "More light provides more radiant energy, speeding up the reaction.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["light_intensity_rate_misconception"],
    }


# 20. Rate of photosynthesis carbon dioxide concentration
def arch_20_rate_of_photosynthesis_carbon_dioxide_concentration(rng: random.Random) -> Dict[str, Any]:
    bicarb_levels = [
        ("0.1% sodium bicarbonate (low CO2)", rng.randint(10, 16)),
        ("0.5% sodium bicarbonate (moderate CO2)", rng.randint(28, 35)),
        ("1.0% sodium bicarbonate (high CO2)", rng.randint(48, 56)),
    ]
    prompt = (
        f"An agricultural researcher enriches water containing aquatic plants with different concentrations of dissolved sodium bicarbonate (a source of carbon dioxide):\n"
        f"- {bicarb_levels[0][0]}: {bicarb_levels[0][1]} bubbles/min\n"
        f"- {bicarb_levels[1][0]}: {bicarb_levels[1][1]} bubbles/min\n"
        f"- {bicarb_levels[2][0]}: {bicarb_levels[2][1]} bubbles/min\n\n"
        f"Why does increasing the carbon dioxide concentration increase the rate of oxygen release up to a plateau?"
    )
    correct = (
        "Carbon dioxide is an essential raw reactant; increasing its availability speeds up the reaction "
        "until another factor (such as light intensity or enzyme saturation) becomes limiting."
    )
    options = [
        correct,
        "Carbon dioxide boils the water, which creates steam bubbles that learners mistake for oxygen.",
        "Carbon dioxide kills the plant so it expels all its internal organs as gas.",
        "Sodium bicarbonate turns the plant cells into pure sea salt crystals.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Apply the concept of limiting factors:\n"
        f"- Carbon dioxide is a primary substrate for photosynthesis.\n"
        f"- When $\text{{CO}}_2$ is scarce, it acts as a limiting factor.\n"
        f"- Adding bicarbonate increases available dissolved $\text{{CO}}_2$, boosting photosynthetic velocity from {bicarb_levels[0][1]} to {bicarb_levels[2][1]} bubbles/min.\n\n"
        f"**Step 2:** The reason is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_20_{rng.randint(100000, 999999)}",
        "subskill": "20_rate_of_photosynthesis_carbon_dioxide_concentration",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What happens when you supply more of a required ingredient to a factory?",
            "tier_2": "More CO2 reactant allows more glucose and oxygen products to be formed.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["co2_limiting_factor_misconception"],
    }


# 21. Rate of photosynthesis temperature and enzyme limits
def arch_21_rate_of_photosynthesis_temperature_and_enzyme_limits(rng: random.Random) -> Dict[str, Any]:
    optimal_t = rng.choice([25, 30])
    denature_t = rng.choice([48, 52])
    prompt = (
        f"Photosynthetic rate in a greenhouse plant rises steadily as ambient temperature increases from 10 °C to {optimal_t} °C. "
        f"However, when temperature exceeds {denature_t} °C, the rate of photosynthesis plummets abruptly to near zero.\n\n"
        f"What biological cause explains this sharp collapse at high temperatures?"
    )
    correct = (
        f"Photosynthetic chemical reactions are catalyzed by proteins called enzymes; "
        f"temperatures above {denature_t} °C permanently denature (destroy the three-dimensional shape of) these enzymes."
    )
    options = [
        correct,
        f"At {denature_t} °C, all sunlight reflects off the Earth and leaves the solar system.",
        "The plant turns into an animal to avoid the heat waves.",
        "Carbon dioxide molecules freeze solid into dry ice at high temperatures.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze temperature effects on biological enzymes:\n"
        f"- Photosynthesis involves biochemical reactions governed by enzymes (e.g. RuBisCO).\n"
        f"- Up to the optimum (~{optimal_t} °C), heat increases molecular kinetic energy and collision rates.\n"
        f"- Excessive heat (>{denature_t} °C) breaks molecular bonds holding enzyme active sites, causing denaturation and loss of catalytic function.\n\n"
        f"**Step 2:** The explanation is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_21_{rng.randint(100000, 999999)}",
        "subskill": "21_rate_of_photosynthesis_temperature_and_enzyme_limits",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What happens to cellular protein enzymes when exposed to extreme heat?",
            "tier_2": "High heat denatures enzymes, stopping the chemical reactions.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["enzyme_denaturation_temperature_misconception"],
    }


# 22. Identifying variables independent dependent fixed in photosynthesis
def arch_22_identifying_variables_independent_dependent_fixed_in_photosynthesis(rng: random.Random) -> Dict[str, Any]:
    experiments = [
        ("the effect of lamp distance on the number of oxygen bubbles released per minute by Elodea", "lamp distance (light intensity)", "number of oxygen bubbles per minute (rate of photosynthesis)", "water temperature and plant species"),
        ("the effect of sodium bicarbonate concentration on Elodea bubble rate", "concentration of sodium bicarbonate (CO2 level)", "bubble count per minute", "light distance and water temperature"),
    ]
    investigation, ind_var, dep_var, ctrl_vars = rng.choice(experiments)
    prompt = (
        f"A Grade 8 class designs a scientific investigation to study {investigation}.\n\n"
        f"Identify the **independent variable** and the **dependent variable** in this investigation."
    )
    correct = f"Independent variable: {ind_var} | Dependent variable: {dep_var}"
    options = [
        correct,
        f"Independent variable: {dep_var} | Dependent variable: {ind_var}",
        f"Independent variable: {ctrl_vars} | Dependent variable: room atmospheric pressure",
        "There are zero variables in biological scientific inquiries.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define scientific variables:\n"
        f"- Independent variable: the factor deliberately altered or tested by the investigator ({ind_var}).\n"
        f"- Dependent variable: the resulting factor measured or observed ({dep_var}).\n"
        f"- Controlled (fixed) variables: factors kept strictly constant ({ctrl_vars}).\n\n"
        f"**Step 2:** The correct assignment is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_22_{rng.randint(100000, 999999)}",
        "subskill": "22_identifying_variables_independent_dependent_fixed_in_photosynthesis",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Which variable is changed by the experimenter, and which is measured as the outcome?",
            "tier_2": "The independent variable is changed; the dependent variable is measured.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["independent_dependent_variable_confusion"],
    }


# 23. Scientific graphing photosynthesis rate vs light distance (with dynamic SVG)
def arch_23_scientific_graphing_photosynthesis_rate_vs_light_distance(rng: random.Random) -> Dict[str, Any]:
    r1 = rng.randint(45, 52)
    r2 = rng.randint(28, 34)
    r3 = rng.randint(14, 18)
    r4 = rng.randint(5, 8)
    line_color = rng.choice(["#2563eb", "#059669", "#7c3aed"])

    # Plot coordinates for 4 points
    # x: 10cm -> 80px, 20cm -> 160px, 30cm -> 240px, 40cm -> 320px
    # y: 200 - r*2.8
    y1 = int(200 - r1 * 2.8)
    y2 = int(200 - r2 * 2.8)
    y3 = int(200 - r3 * 2.8)
    y4 = int(200 - r4 * 2.8)

    svg = (
        f'<svg viewBox="0 0 420 250" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="210" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Photosynthetic Rate vs Lamp Distance</text>'
        f'<line x1="50" y1="200" x2="380" y2="200" stroke="#64748b" stroke-width="2" />'
        f'<line x1="50" y1="200" x2="50" y2="40" stroke="#64748b" stroke-width="2" />'
        f'<polyline points="80,{y1} 160,{y2} 240,{y3} 320,{y4}" fill="none" stroke="{line_color}" stroke-width="2.5" />'
        f'<circle cx="80" cy="{y1}" r="4" fill="{line_color}" />'
        f'<circle cx="160" cy="{y2}" r="4" fill="{line_color}" />'
        f'<circle cx="240" cy="{y3}" r="4" fill="{line_color}" />'
        f'<circle cx="320" cy="{y4}" r="4" fill="{line_color}" />'
        f'<text x="80" y="{y1 - 8}" font-size="10" fill="#1e293b" text-anchor="middle">{r1}</text>'
        f'<text x="160" y="{y2 - 8}" font-size="10" fill="#1e293b" text-anchor="middle">{r2}</text>'
        f'<text x="240" y="{y3 - 8}" font-size="10" fill="#1e293b" text-anchor="middle">{r3}</text>'
        f'<text x="320" y="{y4 - 8}" font-size="10" fill="#1e293b" text-anchor="middle">{r4}</text>'
        f'<text x="80" y="215" font-size="10" fill="#475569" text-anchor="middle">10 cm</text>'
        f'<text x="160" y="215" font-size="10" fill="#475569" text-anchor="middle">20 cm</text>'
        f'<text x="240" y="215" font-size="10" fill="#475569" text-anchor="middle">30 cm</text>'
        f'<text x="320" y="215" font-size="10" fill="#475569" text-anchor="middle">40 cm</text>'
        f'<text x="210" y="238" font-size="11" fill="#334155" text-anchor="middle">Distance from Lamp (cm)</text>'
        f'<text x="20" y="120" font-size="11" fill="#334155" transform="rotate(-90 20,120)" text-anchor="middle">Bubbles / min</text>'
        f'</svg>'
    )

    prompt = (
        f"A learner plotted experimental data recording the number of oxygen bubbles produced per minute "
        f"at lamp distances of 10 cm ({r1}), 20 cm ({r2}), 30 cm ({r3}), and 40 cm ({r4}).\n\n"
        f"Based on the plotted data points, which conclusion is scientifically valid?"
    )
    correct = (
        f"There is an inverse relationship between lamp distance and photosynthetic rate: "
        f"increasing the distance fourfold (from 10 cm to 40 cm) causes bubble rate to decline from {r1} to {r4} bubbles/min."
    )
    options = [
        correct,
        "Increasing the distance makes the plant produce more oxygen due to darkness.",
        "Photosynthetic rate is completely unaffected by changes in lamp distance.",
        "The plant stops producing oxygen at 10 cm because light destroys pondweed leaves.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Read and interpret the graph data:\n"
        f"- At 10 cm: {r1} bubbles/min (maximum rate, highest light intensity).\n"
        f"- At 40 cm: {r4} bubbles/min (lowest rate, lowest light intensity).\n"
        f"- The downward-sloping curve shows an inverse relationship with distance (and direct relationship with light intensity).\n\n"
        f"**Step 2:** The valid conclusion is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_23_{rng.randint(100000, 999999)}",
        "subskill": "23_scientific_graphing_photosynthesis_rate_vs_light_distance",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "hints": {
            "tier_1": "Look at the trend: as distance increases, what happens to bubbles per minute?",
            "tier_2": "The rate drops steadily as the lamp is moved further away.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["graph_interpretation_photosynthesis_misconception"],
    }


# 24. Stomata and guard cells gas exchange mechanism
def arch_24_stomata_and_guard_cells_gas_exchange_mechanism(rng: random.Random) -> Dict[str, Any]:
    states = [
        ("turgid (swollen with water during the day)", "open", "allowing CO2 to diffuse in for photosynthesis while oxygen diffuses out"),
        ("flaccid (water-stressed or during darkness)", "closed", "preventing excessive transpirational water loss from the leaf"),
    ]
    state_desc, pore_state, function = rng.choice(states)
    prompt = (
        f"Microscopic pores called **stomata** are surrounded by pairs of specialized **guard cells** on the lower leaf surface. "
        f"When guard cells become {state_desc}, the stomatal pore becomes **{pore_state}**.\n\n"
        f"What is the biological importance of this stomatal regulation for the plant?"
    )
    correct = f"It regulates gas exchange and water conservation by {function}."
    options = [
        correct,
        "It generates sonic booms to scare away predatory aphids.",
        "It pumps liquid iron into flower petals to give them red coloration.",
        "It allows the leaf to capture insects and digest them for table sugar.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand guard cell biomechanics:\n"
        f"- When water is abundant, guard cells absorb water, swell (become turgid), curve outward, and open the stomatal aperture -> allowing $\text{{CO}}_2$ intake.\n"
        f"- Under dry or dark conditions, guard cells lose turgor, become flaccid, and close the pore -> conserving precious water from evaporating.\n\n"
        f"**Step 2:** The function is: **{correct}**."
    )
    return {
        "id": f"ns8_pr_24_{rng.randint(100000, 999999)}",
        "subskill": "24_stomata_and_guard_cells_gas_exchange_mechanism",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What two things move through stomata: gases and water vapor?",
            "tier_2": f"Guard cells control stomata by {function}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["stomata_guard_cells_mechanism_misconception"],
    }


# 25. Xylem and phloem transport vessels in photosynthesis
def arch_25_xylem_and_phloem_transport_vessels_in_photosynthesis(rng: random.Random) -> Dict[str, Any]:
    vessels = [
        ("xylem", "water and dissolved inorganic mineral salts from roots upward to photosynthetic leaves"),
        ("phloem", "dissolved sucrose and amino acids manufactured in leaves downward and upward to all living tissues"),
    ]
    target_vessel, transport_role = rng.choice(vessels)
    prompt = (
        f"A plant possesses a dual vascular transport network comprising **xylem** and **phloem**.\n\n"
        f"What specific substance is transported by **{target_vessel}**, and in which direction does it flow relative to photosynthesis?"
    )
    correct = f"{target_vessel.capitalize()} transports {transport_role}."
    alt_role = vessels[1][1] if target_vessel == "xylem" else vessels[0][1]
    options = [
        correct,
        f"{target_vessel.capitalize()} transports {alt_role}.",
        f"{target_vessel.capitalize()} transports pure oxygen gas bubbles downward to feed earthworms.",
        f"{target_vessel.capitalize()} transports solid granite stones to weight the roots down.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish plant vascular tissues:\n"
        f"- Xylem: dead hollow lignified tubes transporting water and mineral salts unidirectionally upwards from roots to leaves.\n"
        f"- Phloem: living sieve tubes translocating manufactured organic food (sugars) bidirectionally from source to sink.\n\n"
        f"**Step 2:** For {target_vessel}: **{correct}**."
    )
    return {
        "id": f"ns8_pr_25_{rng.randint(100000, 999999)}",
        "subskill": "25_xylem_and_phloem_transport_vessels_in_photosynthesis",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Remember: Xylem = water up from roots; Phloem = food from leaves.",
            "tier_2": f"{target_vessel.capitalize()} transports {transport_role}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["xylem_phloem_distinction_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "01_photosynthesis_radiant_to_chemical_energy_conversion": arch_01_photosynthesis_radiant_to_chemical_energy_conversion,
    "02_photosynthesis_word_equation_and_chemical_symbols": arch_02_photosynthesis_word_equation_and_chemical_symbols,
    "03_photosynthesis_reactants_carbon_dioxide_and_water": arch_03_photosynthesis_reactants_carbon_dioxide_and_water,
    "04_photosynthesis_products_glucose_and_oxygen": arch_04_photosynthesis_products_glucose_and_oxygen,
    "05_role_of_chlorophyll_trapping_radiant_energy": arch_05_role_of_chlorophyll_trapping_radiant_energy,
    "06_chloroplast_organelle_structure_and_function": arch_06_chloroplast_organelle_structure_and_function,
    "07_leaf_adaptations_for_photosynthesis_stomata_and_mesophyll": arch_07_leaf_adaptations_for_photosynthesis_stomata_and_mesophyll,
    "08_glucose_solubility_and_translocation_as_sucrose": arch_08_glucose_solubility_and_translocation_as_sucrose,
    "09_glucose_conversion_to_insoluble_storage_starch": arch_09_glucose_conversion_to_insoluble_storage_starch,
    "10_other_glucose_fates_cellulose_proteins_lipids": arch_10_other_glucose_fates_cellulose_proteins_lipids,
    "11_iodine_test_for_starch_colour_change": arch_11_iodine_test_for_starch_colour_change,
    "12_destarching_plants_purpose_and_protocol": arch_12_destarching_plants_purpose_and_protocol,
    "13_testing_leaf_for_starch_step_boiling_water_kills_cells": arch_13_testing_leaf_for_starch_step_boiling_water_kills_cells,
    "14_testing_leaf_for_starch_step_ethanol_water_bath_safety": arch_14_testing_leaf_for_starch_step_ethanol_water_bath_safety,
    "15_testing_light_requirement_opaque_foil_stencil_investigation": arch_15_testing_light_requirement_opaque_foil_stencil_investigation,
    "16_testing_chlorophyll_requirement_variegated_leaf_investigation": arch_16_testing_chlorophyll_requirement_variegated_leaf_investigation,
    "17_testing_carbon_dioxide_requirement_sodium_hydroxide_investigation": arch_17_testing_carbon_dioxide_requirement_sodium_hydroxide_investigation,
    "18_testing_oxygen_production_elodea_glowing_splint_test": arch_18_testing_oxygen_production_elodea_glowing_splint_test,
    "19_rate_of_photosynthesis_light_intensity_bubbles_per_minute": arch_19_rate_of_photosynthesis_light_intensity_bubbles_per_minute,
    "20_rate_of_photosynthesis_carbon_dioxide_concentration": arch_20_rate_of_photosynthesis_carbon_dioxide_concentration,
    "21_rate_of_photosynthesis_temperature_and_enzyme_limits": arch_21_rate_of_photosynthesis_temperature_and_enzyme_limits,
    "22_identifying_variables_independent_dependent_fixed_in_photosynthesis": arch_22_identifying_variables_independent_dependent_fixed_in_photosynthesis,
    "23_scientific_graphing_photosynthesis_rate_vs_light_distance": arch_23_scientific_graphing_photosynthesis_rate_vs_light_distance,
    "24_stomata_and_guard_cells_gas_exchange_mechanism": arch_24_stomata_and_guard_cells_gas_exchange_mechanism,
    "25_xylem_and_phloem_transport_vessels_in_photosynthesis": arch_25_xylem_and_phloem_transport_vessels_in_photosynthesis,
}
