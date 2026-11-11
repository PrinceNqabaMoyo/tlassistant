"""Grade 8 Natural Sciences: Term 2 - Microorganisms (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/03. Microorganisms.md.
Focus: Fungi, ecological roles, biotechnology, food preservation, water treatment, immunity, vaccines, and scientific investigation.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Yeast unicellular fungus budding reproduction
def arch_26_yeast_unicellular_fungus_budding_reproduction(rng: random.Random) -> Dict[str, Any]:
    temperatures = [25, 28, 30, 32, 35]
    temp = rng.choice(temperatures)
    sugar_conc = rng.choice([5, 10, 15])
    prompt = (
        f"A culture of baker's yeast (*Saccharomyces cerevisiae*) is incubated in a {sugar_conc}% glucose solution "
        f"at an optimal temperature of {temp} °C.\n\n"
        f"Under a compound light microscope, small cellular outgrowths are observed developing from the parent yeast cells.\n\n"
        f"Which statement scientifically explains how yeast cells reproduce under these conditions?"
    )
    correct = (
        "Yeast is a unicellular fungus that reproduces asexually by budding, "
        "where a small outgrowth (bud) develops on the parent cell, receives a replicated nucleus, "
        "and pinches off into an independent daughter cell."
    )
    options = [
        correct,
        "Yeast produces flowering organs that attract pollinating insects in the nutrient broth.",
        "Yeast cells lay microscopic eggs with hard calcium carbonate shells in the liquid medium.",
        "Yeast particles are non-living crystals that multiply exclusively by chemical evaporation.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze yeast classification and reproduction:\n"
        f"- Yeast is a microscopic unicellular fungus.\n"
        f"- The primary mode of reproduction in nutrient-rich conditions is asexual reproduction by **budding**.\n"
        f"- During budding, mitosis produces a duplicate nucleus; a small bulge (bud) forms on the parent cell wall, accepts the nucleus, grows, and eventually pinches off.\n\n"
        f"**Step 2:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_26_{rng.randint(100000, 999999)}",
        "subskill": "26_yeast_unicellular_fungus_budding_reproduction",
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
            "tier_1": "Is yeast unicellular or multicellular, and does it form flowers, eggs, or buds?",
            "tier_2": "Yeast is a single-celled fungus that multiplies through a process called budding.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["yeast_budding_reproduction_misconception"],
    }


# 27. Yeast alcoholic fermentation baking and brewing
def arch_27_yeast_alcoholic_fermentation_baking_and_brewing(rng: random.Random) -> Dict[str, Any]:
    temp = rng.choice([25, 30, 35, 38])
    bubbles_min = rng.choice([12, 18, 24, 30, 36])
    co2_vol = rng.choice([15, 20, 25, 30])
    tube_id = rng.choice(["A", "B", "C"])

    svg = (
        f'<svg viewBox="0 0 440 260" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="440" height="260" fill="#f8fafc" rx="8"/>'
        f'<text x="220" y="24" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Apparatus {tube_id}: Yeast Alcoholic Fermentation Investigation ({temp}°C)</text>'
        f'<!-- Conical flask -->'
        f'<path d="M 80 180 L 110 90 L 130 90 L 160 180 Z" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
        f'<path d="M 82 178 L 95 130 L 145 130 L 158 178 Z" fill="#bae6fd" opacity="0.8"/>'
        f'<rect x="110" y="80" width="20" height="12" fill="#78716c" rx="2"/>'
        f'<text x="120" y="155" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0369a1">Yeast + Glucose ({temp}°C)</text>'
        f'<!-- Delivery tube -->'
        f'<path d="M 120 80 L 120 55 L 290 55 L 290 140" fill="none" stroke="#475569" stroke-width="3"/>'
        f'<!-- Test tube -->'
        f'<rect x="275" y="100" width="30" height="90" rx="15" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/>'
        f'<path d="M 276 135 L 276 175 A 14 14 0 0 0 304 175 L 304 135 Z" fill="#cbd5e1" opacity="0.9"/>'
        f'<text x="290" y="210" text-anchor="middle" font-family="sans-serif" font-size="10" font-weight="bold" fill="#334155">Limewater Test Tube</text>'
        f'<!-- Bubbles -->'
        f'<circle cx="290" cy="130" r="3" fill="#38bdf8"/>'
        f'<circle cx="290" cy="115" r="4" fill="#38bdf8"/>'
        f'<!-- Data box -->'
        f'<rect x="40" y="222" width="360" height="26" rx="4" fill="#e2e8f0" stroke="#94a3b8"/>'
        f'<text x="220" y="239" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#1e293b">Observed gas rate: {bubbles_min} bubbles/min | Accumulated gas: {co2_vol} mL</text>'
        f'</svg>'
    )
    prompt = (
        f"A Natural Sciences class sets up the experimental apparatus shown to investigate anaerobic respiration "
        f"in yeast incubated at {temp} °C.\n\n"
        f"Over 20 minutes, gas bubbles are released into the limewater at a steady rate of {bubbles_min} bubbles/min, "
        f"causing the clear limewater to turn milky/cloudy.\n\n"
        f"Which gas causes the limewater to turn milky, and what is the complete biological word equation for this fermentation process?"
    )
    correct = (
        "Carbon dioxide (CO2); "
        "Glucose -> Ethanol + Carbon dioxide + Energy (ATP)"
    )
    options = [
        correct,
        "Oxygen (O2); Glucose + Oxygen -> Water + Carbon dioxide + Energy",
        "Nitrogen gas (N2); Protein -> Nitrogen + Ammonia + Energy",
        "Hydrogen gas (H2); Glucose -> Hydrogen + Lactic acid + Water",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify the gas detected by limewater:\n"
        f"- Carbon dioxide ($CO_2$) reacts with clear limewater ($Ca(OH)_2$) to precipitate calcium carbonate ($CaCO_3$), turning the liquid cloudy/milky.\n\n"
        f"**Step 2:** Formulate the word equation for yeast alcoholic fermentation:\n"
        f"- Yeast breaks down glucose in the absence of oxygen (anaerobic respiration) into ethanol (alcohol) and carbon dioxide, releasing small amounts of energy (ATP):\n"
        f"  $$\\text{{Glucose}} \\rightarrow \\text{{Ethanol}} + \\text{{Carbon dioxide}} + \\text{{Energy}}$$\n\n"
        f"**Step 3:** Applications:\n"
        f"- Baking: $CO_2$ bubbles get trapped in gluten dough, causing bread to rise; ethanol evaporates during baking.\n"
        f"- Brewing: Ethanol provides alcohol in beer and wine.\n\n"
        f"**Step 4:** The correct match is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_27_{rng.randint(100000, 999999)}",
        "subskill": "27_yeast_alcoholic_fermentation_baking_and_brewing",
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
            "tier_1": "Which gas turns limewater milky?",
            "tier_2": "Yeast breaks down glucose anaerobically to produce ethanol and carbon dioxide.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["yeast_alcoholic_fermentation_products_misconception"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# 28. Mould fungi Rhizopus bread mould and Penicillium
def arch_28_mould_fungi_rhizopus_bread_mould_and_penicillium(rng: random.Random) -> Dict[str, Any]:
    moulds = [
        (
            "*Rhizopus stolonifer* (black bread mould)",
            "grows on damp, warm bread; produces black spore-containing sporangia at the tips of upright aerial hyphae",
            "food spoilage of baked carbohydrates",
        ),
        (
            "*Penicillium chrysogenum* (blue-green mould)",
            "grows on citrus peel and damp organic matter; produces brush-like conidiophores that secrete the antibiotic penicillin",
            "medicinal discovery of antimicrobial substances that destroy bacterial walls",
        ),
    ]
    target_mould, features, significance = rng.choice(moulds)
    prompt = (
        f"Filamentous microscopic fungi known as moulds commonly grow on household foods when exposed to warm, moist conditions.\n\n"
        f"Which statement accurately describes **{target_mould}** and its biological significance?"
    )
    correct = f"It {features}, and is scientifically significant for {significance}."
    distractors = [
        "It is a photosynthesizing flowering plant that generates seeds inside apples.",
        "It is an acellular mineral salt that crystallizes purely from cold sea water.",
        "It is an insect larva that builds honeycombs using secreted beeswax.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the fungal mould characteristics:\n"
        f"- Moulds are multicellular filamentous fungi composed of hyphae.\n"
        f"- For {target_mould}: {features}.\n"
        f"- Significance: {significance}.\n\n"
        f"**Step 2:** The accurate statement is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_28_{rng.randint(100000, 999999)}",
        "subskill": "28_mould_fungi_rhizopus_bread_mould_and_penicillium",
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
            "tier_1": f"Think about where {target_mould} grows and what structures it produces.",
            "tier_2": "Moulds produce hyphae and spores; Penicillium produces penicillin, while Rhizopus produces black sporangia on bread.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["mould_fungi_rhizopus_penicillium_misconception"],
    }


# 29. Fungal diseases athletes foot ringworm and thrush
def arch_29_fungal_diseases_athletes_foot_ringworm_and_thrush(rng: random.Random) -> Dict[str, Any]:
    diseases = [
        (
            "Athlete's foot (*Tinea pedis*)",
            "Fungus growing between damp, warm toes; causes itching, scaling, and cracking of the skin.",
            "Walking barefoot in communal showers, locker rooms, or wearing damp, unventilated shoes.",
        ),
        (
            "Ringworm (*Tinea corporis*)",
            "Fungal infection causing raised, red, itchy, circular ring-like patches on human skin.",
            "Direct skin-to-skin contact with infected people, domestic animals, or shared towels.",
        ),
        (
            "Thrush (*Candida albicans*)",
            "Opportunistic yeast infection causing white curdy patches on the tongue and mucous membranes of the mouth or vagina.",
            "Overgrowth of naturally occurring yeast when the normal bacterial microbiome is disrupted (e.g. following broad-spectrum antibiotic treatment).",
        ),
    ]
    dis_name, symptoms, transmission = rng.choice(diseases)
    prompt = (
        f"Microscopic fungi can act as pathogens causing human infections known as mycoses.\n\n"
        f"Which clinical description and transmission route correctly identifies **{dis_name}**?"
    )
    correct = f"Symptoms: {symptoms}\nTransmission: {transmission}"
    alt_diseases = [d for d in diseases if d[0] != dis_name]
    distractors = [f"Symptoms: {d[1]}\nTransmission: {d[2]}" for d in alt_diseases]
    distractors.append(
        "Symptoms: High fever, coughing blood, and severe tooth decay caused by drinking cold fruit juice.\n"
        "Transmission: Breathing clean high-altitude mountain air."
    )
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review human fungal conditions:\n"
        f"- Athlete's foot: damp feet, itching/scaling between toes.\n"
        f"- Ringworm: circular ring-shaped lesions on skin; not caused by a worm.\n"
        f"- Thrush: yeast overgrowth (*Candida*) causing white oral or vaginal patches.\n\n"
        f"**Step 2:** For {dis_name}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_29_{rng.randint(100000, 999999)}",
        "subskill": "29_fungal_diseases_athletes_foot_ringworm_and_thrush",
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
            "tier_1": f"Is {dis_name} associated with feet, circular skin patches, or mucosal yeast overgrowth?",
            "tier_2": f"Review how {dis_name} manifests and spreads in warm, moist human environments.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fungal_human_diseases_misconception"],
    }


# 30. Antifungal medications vs antibacterial agents
def arch_30_antifungal_medications_vs_antibacterial_agents(rng: random.Random) -> Dict[str, Any]:
    infections = [
        ("athlete's foot (*Tinea pedis*)", "antifungal cream (e.g. clotrimazole)", "fungal cell membranes (ergosterol) and chitin walls"),
        ("ringworm (*Tinea corporis*)", "antifungal ointment (e.g. miconazole)", "fungal sterols and cellular targets"),
        ("oral thrush (*Candida albicans*)", "antifungal suspension (e.g. nystatin)", "fungal yeast cell membranes"),
    ]
    inf_name, med, target = rng.choice(infections)
    prompt = (
        f"A patient suffering from {inf_name} is mistakenly advised by a friend to swallow leftover penicillin (an antibacterial antibiotic).\n\n"
        f"Why is an antibacterial antibiotic completely ineffective against this condition, and what treatment is required?"
    )
    correct = (
        f"Antibacterial antibiotics specifically target bacterial cell walls (peptidoglycan) or bacterial ribosomes, "
        f"which fungi lack. Fungi are eukaryotic organisms with chitin cell walls, so they must be treated with an "
        f"{med} that specifically targets {target}."
    )
    options = [
        correct,
        "Antibacterial antibiotics kill all living things instantly, which would turn the patient's toes into solid rock.",
        "Fungi are acellular viruses that can only be destroyed by radioactive x-rays and drinking lemon juice.",
        "Antibiotics only work when applied directly to animal fur, but cannot enter human skin pores.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare cellular targets of antibiotics vs antifungals:\n"
        f"- Bacteria are prokaryotes with peptidoglycan walls and 70S ribosomes -> targeted by antibiotics.\n"
        f"- Fungi are eukaryotes with chitin walls and ergosterol membranes -> completely unaffected by antibacterial drugs.\n"
        f"- To treat a fungal infection like {inf_name}, the patient requires an **antifungal agent** ({med}).\n\n"
        f"**Step 2:** The scientific explanation is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_30_{rng.randint(100000, 999999)}",
        "subskill": "30_antifungal_medications_vs_antibacterial_agents",
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
            "tier_1": "Do bacteria and fungi have the same cell structure?",
            "tier_2": "Fungi are eukaryotes with chitin walls; antibacterial antibiotics only affect prokaryotic bacterial targets.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["antibacterial_vs_antifungal_distinction_misconception"],
    }


# 31. Decomposers role in nutrient cycling carbon and nitrogen
def arch_31_decomposers_role_in_nutrient_cycling_carbon_and_nitrogen(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("autumn leaf litter fallen on a forest floor in Mpumalanga", "decay fungi and saprophytic bacteria", "carbon dioxide into the air and mineral nitrates/phosphates into the soil"),
        ("an animal carcass in a Kruger National Park grassland", "putrefying bacteria and fungi", "ammonium, nitrates, and mineral salts to soil, and CO2 to the atmosphere"),
        ("organic vegetable scraps placed inside a school compost heap", "aerobic bacteria and compost fungi", "rich humus with bioavailable nitrogen, phosphorus, and potassium"),
    ]
    substrate, decomposer, returned = rng.choice(scenarios)
    prompt = (
        f"Consider the ecological decomposition of {substrate}.\n\n"
        f"What vital role do **decomposers** ({decomposer}) play in this ecosystem's nutrient cycles?"
    )
    correct = (
        f"They secrete extracellular digestive enzymes to break down complex dead organic matter, "
        f"releasing {returned} that primary producers (plants) can reabsorb."
    )
    options = [
        correct,
        "They synthesize sunlight into toxic plastic polymers that seal the soil permanently.",
        "They act as apex predators that hunt living grazing mammals at night.",
        "They permanently remove all carbon and nitrogen from planet Earth, depleting the atmosphere.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the ecological role of decomposers:\n"
        f"- Decomposers (bacteria and fungi) feed saprophytically.\n"
        f"- They break down organic compounds in dead organisms and excreta.\n"
        f"- They return essential nutrients ({returned}) back to the abiotic environment for reuse by plants.\n\n"
        f"**Step 2:** The fundamental ecological role: **{correct}**."
    )
    return {
        "id": f"ns8_mic_31_{rng.randint(100000, 999999)}",
        "subskill": "31_decomposers_role_in_nutrient_cycling_carbon_and_nitrogen",
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
            "tier_1": "What would happen to dead matter if decomposers did not break it down?",
            "tier_2": "Decomposers recycle dead biomass back into simple inorganic nutrients for plants.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["decomposers_nutrient_cycling_misconception"],
    }


# 32. Symbiotic nitrogen fixation Rhizobium in legume nodules
def arch_32_symbiotic_nitrogen_fixation_rhizobium_in_legume_nodules(rng: random.Random) -> Dict[str, Any]:
    crops = [
        ("groundnuts (peanuts)", "Limpopo crop rotations"),
        ("cowpeas (black-eyed peas)", "smallholder farming in KwaZulu-Natal"),
        ("soybeans", "commercial rotational farming in the Free State"),
        ("lucerne (alfalfa)", "fodder production in the Western Cape"),
    ]
    crop, region = rng.choice(crops)
    prompt = (
        f"In South African agriculture, leguminous crops such as {crop} ({region}) "
        f"form specialised root nodules housing *Rhizobium* bacteria.\n\n"
        f"Which statement scientifically explains the **mutualistic symbiotic relationship** between *Rhizobium* and the host legume?"
    )
    correct = (
        "The bacteria fix inert atmospheric nitrogen gas (N2) into bioavailable ammonium/nitrates for the plant to build proteins, "
        "while the legume plant supplies the bacteria with carbohydrates (sugars from photosynthesis) and a protected shelter."
    )
    options = [
        correct,
        "The bacteria consume the entire plant root, destroying the legume within two days.",
        "The plant provides the bacteria with animal meat, while the bacteria emit pure ozone gas into the roots.",
        "The bacteria absorb liquid petroleum from the soil and transform it into gold nanoparticles for the plant.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze nitrogen fixation mutualism:\n"
        f"- Atmospheric nitrogen ($N_2$) is inert and unusable by green plants directly.\n"
        f"- *Rhizobium* bacteria contain the nitrogenase enzyme to convert $N_2 \\rightarrow NH_4^+$ / nitrates.\n"
        f"- The legume provides shelter (root nodules) and photosynthesized sugars (carbohydrates) to power the high-energy fixation process.\n"
        f"- Both species benefit -> mutualistic symbiosis.\n\n"
        f"**Step 2:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_32_{rng.randint(100000, 999999)}",
        "subskill": "32_symbiotic_nitrogen_fixation_rhizobium_in_legume_nodules",
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
            "tier_1": "What does Rhizobium provide to the plant, and what does the plant provide in return?",
            "tier_2": "Rhizobium fixes nitrogen into nitrates for protein synthesis; the plant provides sugars from photosynthesis.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["nitrogen_fixation_rhizobium_symbiosis_misconception"],
    }


# 33. Lactic acid fermentation Lactobacillus yoghurt and amasi
def arch_33_lactic_acid_fermentation_lactobacillus_yoghurt_and_amasi(rng: random.Random) -> Dict[str, Any]:
    dairy_products = [
        ("amasi (maas / traditional fermented sour milk)", "traditional calabash or container fermentation"),
        ("yoghurt", "commercial milk fermentation using Lactobacillus bulgaricus"),
        ("cheddar and cottage cheese", "curd coagulation through lactic acid production"),
    ]
    product, method = rng.choice(dairy_products)
    prompt = (
        f"The production of {product} ({method}) relies on the activity of lactic acid bacteria such as *Lactobacillus*.\n\n"
        f"What biochemical change takes place during this bacterial fermentation, and how does it preserve the dairy product?"
    )
    correct = (
        "Lactobacillus ferments milk sugar (lactose) into lactic acid; "
        "the accumulation of lactic acid lowers the pH (increases acidity), which curdles milk proteins (casein) "
        "and inhibits the growth of harmful food-spoilage and pathogenic microorganisms."
    )
    options = [
        correct,
        "Lactobacillus boils the milk to 500 °C using radioactive decay, vaporising all liquid into steam.",
        "Lactobacillus converts milk calcium into diamond crystals, preventing any oxygen from contacting the milk.",
        "Lactobacillus produces large volumes of poisonous carbon monoxide gas that suffocates all insects.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Describe the lactic fermentation mechanism:\n"
        f"- Substrate: Lactose (milk sugar).\n"
        f"- Pathogen/fermenter: *Lactobacillus* bacteria.\n"
        f"- Product: Lactic acid.\n\n"
        f"**Step 2:** Effects of lactic acid:\n"
        f"- Acidity drops (pH decreases below 4.5).\n"
        f"- Low pH precipitates milk proteins (casein), thickening milk into {product}.\n"
        f"- The acidic environment prevents spoilage organisms and pathogens from multiplying, naturally preserving the milk.\n\n"
        f"**Step 3:** The accurate biochemical change is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_33_{rng.randint(100000, 999999)}",
        "subskill": "33_lactic_acid_fermentation_lactobacillus_yoghurt_and_amasi",
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
            "tier_1": "What sugar in milk is converted into acid by Lactobacillus?",
            "tier_2": "Lactose is converted to lactic acid, which drops the pH, curdles protein, and preserves milk.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["lactic_acid_fermentation_amasi_misconception"],
    }


# 34. Human microbiome gut flora digestion and immunity
def arch_34_human_microbiome_gut_flora_digestion_and_immunity(rng: random.Random) -> Dict[str, Any]:
    vitamins = [("vitamin K", "essential for blood clotting"), ("vitamin B12", "vital for red blood cell formation and nervous system function")]
    vit, vit_role = rng.choice(vitamins)
    prompt = (
        f"The human large intestine (colon) hosts trillions of symbiotic bacteria collectively known as the **gut microbiome**.\n\n"
        f"Which statement correctly details how these gut bacteria contribute to human health and physiological survival?"
    )
    correct = (
        f"They ferment indigestible dietary fibre into beneficial short-chain fatty acids, synthesize {vit} ({vit_role}), "
        f"and competitively exclude harmful pathogens from colonizing the intestinal lining."
    )
    options = [
        correct,
        "They eat holes through the human stomach lining to release food directly into the lungs.",
        "They replace human DNA with fungal spores so that humans can carry out green photosynthesis.",
        "They turn all ingested water into solid ice crystals to keep the abdomen refrigerated.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review functions of the human gut flora:\n"
        f"- Digestion: fermenting dietary fiber and complex polysaccharides humans cannot digest.\n"
        f"- Vitamin synthesis: producing {vit} ({vit_role}) and biotin.\n"
        f"- Immune defence: competing with pathogens for space and nutrients (competitive exclusion) and stimulating mucosal immunity.\n\n"
        f"**Step 2:** The correct statement is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_34_{rng.randint(100000, 999999)}",
        "subskill": "34_human_microbiome_gut_flora_digestion_and_immunity",
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
            "tier_1": "Think about vitamins made in the human colon and competitive exclusion of pathogens.",
            "tier_2": "Gut bacteria ferment fiber, make essential vitamins like vitamin K, and protect against pathogens.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["gut_microbiome_functions_misconception"],
    }


# 35. Industrial and environmental biotechnology bioremediation
def arch_35_industrial_and_environmental_biotechnology_bioremediation(rng: random.Random) -> Dict[str, Any]:
    applications = [
        (
            "Bioremediation of crude oil spills along coastal shipping lanes",
            "Hydrocarbon-degrading bacteria (such as *Pseudomonas*) that break down toxic alkanes into carbon dioxide and water",
        ),
        (
            "Municipal wastewater and sewage treatment plants",
            "Anaerobic sludge digester bacteria and aerobic biofilter microbes that consume organic waste and produce biogas (methane)",
        ),
        (
            "Bioleaching and biomining in South African mineral extraction",
            "Chemolithotrophic acidophilic bacteria (such as *Acidithiobacillus*) that oxidize sulfur and iron minerals to extract copper and gold",
        ),
    ]
    app_name, microbe_role = rng.choice(applications)
    prompt = (
        f"Microorganisms are widely applied in industrial and environmental biotechnology.\n\n"
        f"Which description scientifically outlines **{app_name}**?"
    )
    correct = f"It employs {microbe_role}."
    alt_apps = [a[1] for a in applications if a[0] != app_name]
    distractors = [f"It employs {role}." for role in alt_apps]
    distractors.append("It employs synthetic nuclear warheads that detonate underground to burn all chemicals.")
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review biotechnology applications:\n"
        f"- Bioremediation uses microbes to clean polluted environments.\n"
        f"- Wastewater treatment uses aerobic/anaerobic bacteria to decompose organic human waste.\n"
        f"- Bioleaching uses bacteria to dissolve low-grade ores and extract metals.\n\n"
        f"**Step 2:** For {app_name}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_35_{rng.randint(100000, 999999)}",
        "subskill": "35_industrial_and_environmental_biotechnology_bioremediation",
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
            "tier_1": f"What specific microorganisms are used for {app_name}?",
            "tier_2": f"Match {app_name} to the targeted biological action of the microbes.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["biotechnology_bioremediation_applications_misconception"],
    }


# 36. Food preservation refrigeration and freezing temperature inhibition
def arch_36_food_preservation_refrigeration_and_freezing_temperature_inhibition(rng: random.Random) -> Dict[str, Any]:
    foods = [
        ("fresh milk and poultry meat", "refrigeration at 2 °C to 4 °C", "freezing at -18 °C"),
        ("leftover beef stew and vegetables", "chilling in a household fridge at 3 °C", "deep freezing at -20 °C"),
        ("fresh fish and seafood", "storing on crushed ice at 0 °C to 4 °C", "commercial blast freezing at -25 °C"),
    ]
    food_name, refrig, freeze = rng.choice(foods)
    prompt = (
        f"When storing {food_name}, households and supermarkets rely on {refrig} and {freeze} to prevent spoilage.\n\n"
        f"What is the accurate biological explanation for how low temperatures preserve food, and do they completely sterilise it?"
    )
    correct = (
        "Low temperatures slow down or suspend microbial enzyme activity and metabolic reactions, "
        "and freezing turns liquid water into ice so microbes cannot absorb nutrients; "
        "however, low temperatures do NOT kill all bacteria or endospores, so microbes resume growth when food thaws."
    )
    options = [
        correct,
        "Low temperatures vaporise all bacteria into gas molecules that vanish permanently, ensuring 100% eternal sterilisation.",
        "Cold temperatures convert all bacteria into pure sugar crystals that make spoiled meat sweet and sterile.",
        "Refrigerators emit gamma rays that disintegrate all organic matter into harmless liquid oxygen.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze temperature effects on microbial physiology:\n"
        f"- Enzymes operate at optimum temperatures (25 °C - 37 °C).\n"
        f"- Refrigeration (2 °C - 5 °C): dramatically slows enzyme kinetics and cell division.\n"
        f"- Freezing (-18 °C): turns liquid water into ice crystals, halting microbial metabolism and reproduction.\n"
        f"- Crucial fact: Freezing is bacteriostatic (preservative), NOT bactericidal (it does NOT sterilise); when thawed, dormant bacteria and endospores multiply rapidly.\n\n"
        f"**Step 2:** The accurate explanation is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_36_{rng.randint(100000, 999999)}",
        "subskill": "36_food_preservation_refrigeration_and_freezing_temperature_inhibition",
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
            "tier_1": "Does freezing kill all bacteria, or does it merely slow down / stop their growth?",
            "tier_2": "Low temperatures deactivate enzyme reactions without necessarily killing bacteria or bacterial endospores.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["freezing_does_not_sterilise_misconception"],
    }


# 37. Food preservation heat pasteurisation and canning sterilisation
def arch_37_food_preservation_heat_pasteurisation_and_canning_sterilisation(rng: random.Random) -> Dict[str, Any]:
    methods = [
        (
            "Pasteurisation of fresh commercial milk",
            "Heating milk to 72 °C for 15 seconds (or 63 °C for 30 minutes) followed by rapid cooling",
            "kills harmful pathogenic bacteria (such as *Mycobacterium tuberculosis* and *Salmonella*) without denaturing milk proteins or altering taste; milk must still be refrigerated",
        ),
        (
            "Canning and autoclaving of canned fish or beans",
            "Heating sealed tins to 121 °C under high steam pressure for 15 to 30 minutes",
            "achieves commercial sterilisation by destroying both vegetative bacteria and heat-resistant bacterial endospores (such as *Clostridium botulinum*), allowing multi-year room temperature storage",
        ),
    ]
    target_method, procedure, outcome = rng.choice(methods)
    prompt = (
        f"Heat treatment is a cornerstone of industrial food processing.\n\n"
        f"Which statement correctly details **{target_method}** and its biological outcome?"
    )
    correct = f"Procedure: {procedure}.\nOutcome: It {outcome}."
    alt = [m for m in methods if m[0] != target_method][0]
    options = [
        correct,
        f"Procedure: {alt[1]}.\nOutcome: It {alt[2]}.",
        "Procedure: Exposing food to liquid nitrogen at -196 °C for 2 hours.\nOutcome: It burns all food into white charcoal.",
        "Procedure: Submerging food in pure table vinegar for 5 minutes.\nOutcome: It changes vegetable cells into gold nuggets.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish between pasteurisation and canning:\n"
        f"- Pasteurisation: mild heat (72 °C, 15 s); destroys vegetative pathogens; food remains perishable and needs refrigeration.\n"
        f"- Canning/Autoclaving: severe heat under pressure (121 °C); kills endospores (*Clostridium botulinum*); yields indefinite shelf-stability in sealed airtight cans.\n\n"
        f"**Step 2:** For {target_method}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_37_{rng.randint(100000, 999999)}",
        "subskill": "37_food_preservation_heat_pasteurisation_and_canning_sterilisation",
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
            "tier_1": f"What temperature and outcome are associated with {target_method}?",
            "tier_2": "Pasteurisation kills pathogens without destroying taste; canning at 121 °C destroys endospores.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["pasteurisation_vs_canning_sterilisation_misconception"],
    }


# 38. Food preservation dehydration salting and sugaring osmotic control
def arch_38_food_preservation_dehydration_salting_and_sugaring_osmotic_control(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("making traditional South African biltong and droëwors", "heavy salt coating and air drying"),
        ("making fruit jam and marmalade", "cooking fruit in high sugar concentration (>65% sucrose)"),
        ("preserving salted snoek and cod fish", "heavy salting and sun curing"),
        ("producing dried peaches, apricots, and raisins", "sun drying and moisture removal"),
    ]
    food_ex, technique = rng.choice(examples)
    prompt = (
        f"When {food_ex} ({technique}), water is removed or bound chemically.\n\n"
        f"What biological mechanism prevents bacteria and moulds from spoiling these foods?"
    )
    correct = (
        "High salt or sugar concentrations create a hypertonic environment with low water activity; "
        "water is drawn out of microbial cells by osmosis (plasmolysis), dehydrating the microbes "
        "and preventing cellular metabolism and reproduction."
    )
    options = [
        correct,
        "Salt and sugar supply extra fuel that makes bacteria grow so large that they explode.",
        "Drying turns bacterial cells into hard metal screws that cannot digest food.",
        "Sugar binds to air nitrogen, removing all gravity from the food container.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze osmotic food preservation:\n"
        f"- Water is essential for microbial enzymatic reactions and transport.\n"
        f"- Adding salt or sugar makes the surrounding medium hypertonic (lower water potential).\n"
        f"- Water moves by **osmosis** from inside the bacterial/fungal cells to the outside.\n"
        f"- Microbial cells shrink and undergo **plasmolysis**, causing metabolic arrest and inhibiting growth.\n\n"
        f"**Step 2:** The mechanism is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_38_{rng.randint(100000, 999999)}",
        "subskill": "38_food_preservation_dehydration_salting_and_sugaring_osmotic_control",
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
            "tier_1": "What happens to water inside bacterial cells when surrounded by heavy salt or sugar?",
            "tier_2": "Osmosis draws water out of microbial cells (plasmolysis), stopping their growth.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["osmotic_dehydration_preservation_misconception"],
    }


# 39. Food preservation pickling and acidification ph inhibition
def arch_39_food_preservation_pickling_and_acidification_ph_inhibition(rng: random.Random) -> Dict[str, Any]:
    pickled_items = [
        ("pickled onions and beetroot", "submerging vegetables in vinegar (acetic acid)"),
        ("traditional South African mango atchar", "spicing and oil pickling with acidic mustard and acetic compounds"),
        ("pickled cucumbers (gherkins)", "steeping in a vinegar and salt brine solution"),
    ]
    item, prep = rng.choice(pickled_items)
    prompt = (
        f"The culinary preservation of {item} involves {prep}.\n\n"
        f"How does the chemical property of vinegar (acetic acid) prevent food spoilage by microorganisms?"
    )
    correct = (
        "Vinegar contains acetic acid, which lowers the food's pH below 4.6 (creating an acidic environment); "
        "this low pH denatures microbial enzymes and disrupts membrane transport, preventing bacterial and fungal survival."
    )
    options = [
        correct,
        "Vinegar increases the pH to 14, turning all microbes into soapy bubbles.",
        "Vinegar removes all carbon atoms from food molecules, starving the microbes of oxygen.",
        "Vinegar freezes the food instantly into solid carbon dioxide blocks.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze acid pickling:\n"
        f"- Vinegar contains acetic acid ($CH_3COOH$).\n"
        f"- Most food-spoilage and pathogenic bacteria (such as *Clostridium botulinum* and *Salmonella*) cannot grow at a pH below 4.6.\n"
        f"- The acidic environment alters enzyme active sites (denaturation) and disrupts proton gradients across microbial membranes.\n\n"
        f"**Step 2:** The mechanism is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_39_{rng.randint(100000, 999999)}",
        "subskill": "39_food_preservation_pickling_and_acidification_ph_inhibition",
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
            "tier_1": "Is vinegar an acid or a base, and what does it do to pH?",
            "tier_2": "Vinegar lowers pH (acidic), denaturing enzymes and stopping microbial growth.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["pickling_ph_inhibition_misconception"],
    }


# 40. Water purification boiling chlorination and filtration methods
def arch_40_water_purification_boiling_chlorination_and_filtration_methods(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        (
            "Boiling stream water rolling for 1 to 3 minutes",
            "Thermal heat denatures microbial enzymes and ruptures membranes, killing vegetative bacteria, viruses, and parasites",
            "Water treatment during rural field expeditions or boil-water municipal alerts",
        ),
        (
            "Domestic chlorination adding 1 teaspoon (5 mL) of unscented household bleach (e.g. Jik) to 20 to 25 litres of clear water and waiting 30 minutes",
            "Chlorine acts as a strong oxidising agent that oxidises microbial proteins and destroys bacterial and viral membranes",
            "Emergency household purification when tap water supplies are compromised",
        ),
        (
            "Multi-stage sand and gravel filtration followed by solar disinfection (SODIS in clear PET bottles for 6 hours)",
            "Filtration removes suspended particulates and larger parasites; solar UV-A radiation and thermal heat destroy remaining pathogens",
            "Low-cost off-grid water purification in sunny rural areas",
        ),
    ]
    target_method, mechanism, context = rng.choice(scenarios)
    prompt = (
        f"Access to safe drinking water is essential for preventing waterborne epidemics like cholera.\n\n"
        f"Consider the purification method: **{target_method}** ({context}).\n\n"
        f"What is the accurate biological and chemical mechanism by which this method disinfects contaminated water?"
    )
    correct = mechanism
    alt_mechs = [s[1] for s in scenarios if s[0] != target_method]
    distractors = alt_mechs + [
        "It transforms all water molecules into pure carbon atoms that repel all living cells."
    ]
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review domestic water disinfection mechanisms:\n"
        f"- Boiling: intense heat denatures proteins and kills pathogens.\n"
        f"- Chlorination: hypochlorous acid oxidises cell membranes and enzymes.\n"
        f"- Filtration + SODIS: removes particulate carriers, and UV radiation damages microbial DNA.\n\n"
        f"**Step 2:** For {target_method}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_40_{rng.randint(100000, 999999)}",
        "subskill": "40_water_purification_boiling_chlorination_and_filtration_methods",
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
            "tier_1": f"What specific scientific action does {target_method.split()[0]} perform on microorganisms?",
            "tier_2": "Heat denatures proteins, chlorine oxidises structures, and UV damages DNA.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["water_purification_mechanisms_misconception"],
    }


# 41. Transmission routes airborne waterborne direct contact vector
def arch_41_transmission_routes_airborne_waterborne_direct_contact_vector(rng: random.Random) -> Dict[str, Any]:
    routes = [
        (
            "Airborne droplet transmission (e.g. Tuberculosis, Influenza, Measles)",
            "Inhalation of microscopic aerosol droplets expelled when an infected person coughs, sneezes, or talks",
            "Wearing face masks, ensuring adequate room ventilation, covering coughs",
        ),
        (
            "Waterborne fecal-oral transmission (e.g. Cholera, Typhoid, Dysentery)",
            "Ingestion of drinking water or food contaminated by human feces containing pathogens",
            "Boiling drinking water, adding chlorine/bleach, proper sewage sanitation",
        ),
        (
            "Biological vector transmission (e.g. Malaria transmitted by female *Anopheles* mosquitoes)",
            "Bite of an insect carrier that transfers the pathogen directly into the human bloodstream",
            "Using insecticide-treated bed nets, applying insect repellent, draining stagnant water",
        ),
        (
            "Direct physical contact transmission (e.g. Athlete's foot, Ringworm)",
            "Direct skin-to-skin touch or sharing contaminated personal items like towels, shoes, or combs",
            "Maintaining personal hygiene, wearing flip-flops in public showers, not sharing towels",
        ),
    ]
    target_route, mech, prevent = rng.choice(routes)
    prompt = (
        f"Infectious diseases are categorized by their mode of transmission.\n\n"
        f"Which pathogen transmission route and prevention protocol defines **{target_route}**?"
    )
    correct = f"Mechanism: {mech}.\nPrevention: {prevent}."
    alt_routes = [r for r in routes if r[0] != target_route]
    distractors = [f"Mechanism: {r[1]}.\nPrevention: {r[2]}." for r in alt_routes[:3]]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze pathogen transmission pathways:\n"
        f"- Airborne: droplets in air -> masks and ventilation.\n"
        f"- Waterborne: contaminated water -> boiling/chlorine and sanitation.\n"
        f"- Vector: insect bites -> bed nets and repellents.\n"
        f"- Direct contact: physical contact -> hygiene and clean personal items.\n\n"
        f"**Step 2:** For {target_route}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_41_{rng.randint(100000, 999999)}",
        "subskill": "41_transmission_routes_airborne_waterborne_direct_contact_vector",
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
            "tier_1": f"How do pathogens travel in {target_route}?",
            "tier_2": f"Match the disease pathway with the targeted prevention protocol.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["disease_transmission_routes_misconception"],
    }


# 42. Personal hygiene soap and handwashing lipid membrane disruption
def arch_42_personal_hygiene_soap_and_handwashing_lipid_membrane_disruption(rng: random.Random) -> Dict[str, Any]:
    soap_actions = [
        ("enveloped viruses (such as Influenza and Coronaviruses)", "viral lipid bilayer envelope"),
        ("gram-negative and gram-positive bacteria", "bacterial lipid membranes and surface proteins"),
    ]
    target_pathogen, target_struct = rng.choice(soap_actions)
    prompt = (
        f"Health authorities recommend washing hands thoroughly with soap and running water for at least 20 seconds.\n\n"
        f"What is the biophysical mechanism by which soap destroys {target_pathogen} on skin?"
    )
    correct = (
        f"Soap molecules are amphipathic (possessing a hydrophilic head and a hydrophobic/lipophilic tail); "
        f"the hydrophobic tails wedge into the {target_struct}, breaking it apart and dissolving the pathogen, "
        f"while mechanical friction and running water wash away the cellular debris."
    )
    options = [
        correct,
        "Soap contains microscopic scissors that physically snip bacterial DNA into paper confetti.",
        "Soap heats human skin to 300 °C, vaporising all microorganisms into steam without hurting skin cells.",
        "Soap emits loud sound waves that scare bacteria off the hands into the drain.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the molecular structure and action of soap:\n"
        f"- Soap consists of amphipathic surfactant molecules.\n"
        f"- Hydrophobic tails interact with and disrupt the lipid membranes/envelopes of pathogens.\n"
        f"- Hydrophilic heads face water, trapping debris in micelles.\n"
        f"- 20 seconds of lathering allows time for molecular disruption and mechanical detaching.\n\n"
        f"**Step 2:** The mechanism is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_42_{rng.randint(100000, 999999)}",
        "subskill": "42_personal_hygiene_soap_and_handwashing_lipid_membrane_disruption",
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
            "tier_1": "What are the two parts of a soap molecule?",
            "tier_2": "The hydrophobic tail wedges into lipid membranes/envelopes, breaking them apart.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["soap_membrane_disruption_mechanism_misconception"],
    }


# 43. Immune system innate barriers skin mucus and stomach acid
def arch_43_immune_system_innate_barriers_skin_mucus_and_stomach_acid(rng: random.Random) -> Dict[str, Any]:
    barriers = [
        (
            "Intact skin (epidermis)",
            "A tough, continuous physical barrier of keratinised dead cells that prevents microbes from entering underlying tissues, producing acidic sebum and sweat to inhibit growth.",
        ),
        (
            "Respiratory tract mucus and cilia",
            "Sticky mucus secreted by goblet cells traps inhaled dust and microbes; microscopic hair-like cilia beat rhythmically to sweep mucus upwards towards the throat to be swallowed or coughed out.",
        ),
        (
            "Gastric stomach acid (hydrochloric acid, pH 1.5 - 2.0)",
            "A highly acidic chemical fluid that denatures microbial proteins and destroys most ingested bacteria and parasites before they reach the intestines.",
        ),
        (
            "Lysozyme in tears and saliva",
            "An antimicrobial enzyme that chemically breaks down peptidoglycan bonds in bacterial cell walls, protecting the eyes and oral cavity.",
        ),
    ]
    target_b, target_mech = rng.choice(barriers)
    prompt = (
        f"The human body's **first line of defence** consists of non-specific physical and chemical innate barriers.\n\n"
        f"Which statement scientifically explains how **{target_b}** protects the body from pathogen invasion?"
    )
    correct = target_mech
    alt_mechs = [b[1] for b in barriers if b[0] != target_b]
    options = [correct] + alt_mechs
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review innate first-line barriers:\n"
        f"- Skin: tough physical keratin shield + antimicrobial sebum.\n"
        f"- Mucus & Cilia: traps pathogens in respiratory passages and sweeps them out.\n"
        f"- Stomach acid: $HCl$ destroys ingested pathogens.\n"
        f"- Lysozyme: enzyme hydrolysing bacterial cell walls in tears/saliva.\n\n"
        f"**Step 2:** For {target_b}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_43_{rng.randint(100000, 999999)}",
        "subskill": "43_immune_system_innate_barriers_skin_mucus_and_stomach_acid",
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
            "tier_1": f"Is {target_b} a physical barrier, a cilia escalator, an acid, or an enzyme?",
            "tier_2": f"Match {target_b} to its specific physiological protective action.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["innate_immune_barriers_misconception"],
    }


# 44. Immune system white blood cells phagocytes and lymphocytes
def arch_44_immune_system_white_blood_cells_phagocytes_and_lymphocytes(rng: random.Random) -> Dict[str, Any]:
    cells = [
        (
            "Phagocytes (such as macrophages and neutrophils)",
            "Carry out non-specific phagocytosis: they flow around, engulf, and ingest foreign pathogens into a phagosome vesicle, which fuses with lysosomes containing digestive enzymes to destroy the microbe.",
        ),
        (
            "Lymphocytes (specifically B-lymphocytes)",
            "Carry out specific adaptive immunity: they recognize specific foreign antigens on pathogens and produce complementary Y-shaped antibody proteins that neutralize or clump pathogens for destruction.",
        ),
    ]
    target_c, target_action = rng.choice(cells)
    prompt = (
        f"When pathogens penetrate innate barriers and enter human blood or lymphatic vessels, "
        f"white blood cells (leukocytes) launch a cellular defence.\n\n"
        f"Which description scientifically outlines the role of **{target_c}**?"
    )
    correct = target_action
    other_action = [c[1] for c in cells if c[0] != target_c][0]
    distractors = [
        other_action,
        "They carry oxygen gas bound to iron hemoglobin to power skeletal muscle contraction.",
        "They solidify blood inside brain arteries to stop all cellular thought processes.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare phagocytes and lymphocytes:\n"
        f"- Phagocytes: non-specific; engulf and digest pathogens by phagocytosis.\n"
        f"- Lymphocytes: specific; produce complementary antibodies or coordinate targeted immune memory.\n\n"
        f"**Step 2:** For {target_c}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_44_{rng.randint(100000, 999999)}",
        "subskill": "44_immune_system_white_blood_cells_phagocytes_and_lymphocytes",
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
            "tier_1": "Do phagocytes engulf, or do they produce antibodies?",
            "tier_2": "Phagocytes engulf and ingest microbes; lymphocytes produce antibodies.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["phagocytes_vs_lymphocytes_functions_misconception"],
    }


# 45. Antibodies and antigens specific immune recognition
def arch_45_antibodies_and_antigens_specific_immune_recognition(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Antigen", "A foreign molecular marker or protein on the outer surface of a pathogen that stimulates an immune response"),
        ("Antibody", "A specific Y-shaped protective protein produced by B-lymphocytes that binds precisely to a complementary antigen"),
    ]
    target_term, target_def = rng.choice(pairs)
    prompt = (
        f"In immunological defence, the human body distinguishes between 'self' and 'non-self' using molecular markers.\n\n"
        f"What is the precise biological definition of an **{target_term}**?"
    )
    correct = target_def
    other_def = [p[1] for p in pairs if p[0] != target_term][0]
    options = [
        correct,
        other_def,
        "A metallic particle ingested in food that conducts nerve impulses across the spinal cord.",
        "An organelle inside plant chloroplasts that produces starch during darkness.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define antigen vs antibody:\n"
        f"- **Antigen**: foreign protein or carbohydrate on pathogen surface that triggers an immune response.\n"
        f"- **Antibody**: specific protein produced by B-lymphocytes with variable binding sites complementary to the antigen (lock-and-key fit).\n\n"
        f"**Step 2:** For {target_term}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_45_{rng.randint(100000, 999999)}",
        "subskill": "45_antibodies_and_antigens_specific_immune_recognition",
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
            "tier_1": "Which one is on the pathogen surface, and which one is made by white blood cells?",
            "tier_2": "Antigens are foreign surface markers; antibodies are Y-shaped proteins made by lymphocytes.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["antigen_vs_antibody_definition_misconception"],
    }


# 46. Vaccination principles Edward Jenner and immune memory
def arch_46_vaccination_principles_edward_jenner_and_immune_memory(rng: random.Random) -> Dict[str, Any]:
    day_1 = rng.choice([7, 10, 14])
    day_2 = rng.choice([28, 30, 35])
    peak_1 = rng.choice([20, 25, 30])
    peak_2 = rng.choice([80, 90, 100])
    disease = rng.choice(["Measles", "Tetanus", "Hepatitis B"])

    svg = (
        f'<svg viewBox="0 0 460 260" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="460" height="260" fill="#f8fafc" rx="8"/>'
        f'<text x="230" y="24" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0f172a">Antibody Concentration: Primary Vaccination vs Secondary Exposure ({disease})</text>'
        f'<!-- Axes -->'
        f'<line x1="60" y1="210" x2="420" y2="210" stroke="#475569" stroke-width="2"/>'
        f'<line x1="60" y1="210" x2="60" y2="50" stroke="#475569" stroke-width="2"/>'
        f'<text x="240" y="245" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#334155">Time (Days)</text>'
        f'<text x="25" y="130" text-anchor="middle" transform="rotate(-90 25 130)" font-family="sans-serif" font-size="11" fill="#334155">Antibody Titer (AU)</text>'
        f'<!-- Primary curve -->'
        f'<path d="M 60 210 Q 110 210 130 {210 - peak_1} Q 160 210 190 200" fill="none" stroke="#2563eb" stroke-width="3"/>'
        f'<text x="130" y="{195 - peak_1}" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#1d4ed8">Primary Peak ({peak_1} AU)</text>'
        f'<!-- Injection markers -->'
        f'<line x1="60" y1="210" x2="60" y2="190" stroke="#dc2626" stroke-width="2" stroke-dasharray="2,2"/>'
        f'<text x="60" y="225" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#dc2626">Day 0 (Vaccine)</text>'
        f'<line x1="200" y1="210" x2="200" y2="70" stroke="#dc2626" stroke-width="2" stroke-dasharray="2,2"/>'
        f'<text x="200" y="225" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#dc2626">Day {day_2} (Exposure)</text>'
        f'<!-- Secondary curve -->'
        f'<path d="M 200 200 Q 230 60 270 {210 - peak_2} Q 350 {210 - peak_2 + 20} 410 {210 - peak_2 + 35}" fill="none" stroke="#16a34a" stroke-width="3"/>'
        f'<text x="270" y="{190 - peak_2}" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#15803d">Secondary Peak ({peak_2} AU)</text>'
        f'</svg>'
    )
    prompt = (
        f"A learner receives an initial vaccine dose against {disease} on Day 0 and encounters the actual live pathogen "
        f"on Day {day_2}, producing the antibody response curves depicted.\n\n"
        f"Why is the secondary immune response significantly faster and higher ({peak_2} AU) than the primary response ({peak_1} AU)?"
    )
    correct = (
        "The primary vaccine exposure triggered B-lymphocytes to produce long-lived memory cells; "
        "upon secondary encounter, memory cells immediately recognize the antigen and rapidly divide "
        "into plasma cells that synthesize vast quantities of antibodies."
    )
    options = [
        correct,
        "The secondary infection heats the bloodstream to 100 °C, boiling all pathogen cells.",
        "The vaccine converted all red blood cells into steel plates that physically block the virus.",
        "The human body stopped breathing oxygen, which suffocated the pathogen within seconds.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the vaccination mechanism:\n"
        f"- Vaccines contain weakened (attenuated), dead pathogens, or harmless antigen fragments.\n"
        f"- Primary response: Lymphocytes identify the antigen, produce antibodies slowly, and form **memory cells**.\n"
        f"- Secondary response: When the live pathogen enters, memory cells recognize it instantly.\n"
        f"- Result: Antibodies are produced much faster, in far greater concentration ({peak_2} AU vs {peak_1} AU), and persist longer, destroying the pathogen before symptoms develop.\n\n"
        f"**Step 2:** The scientific explanation is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_46_{rng.randint(100000, 999999)}",
        "subskill": "46_vaccination_principles_edward_jenner_and_immune_memory",
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
            "tier_1": "What type of immune cells remain in the body after the first vaccination?",
            "tier_2": "Memory cells persist and rapidly produce large amounts of antibodies upon re-exposure.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["vaccination_memory_cells_response_misconception"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
    }


# 47. Herd immunity community protection thresholds
def arch_47_herd_immunity_community_protection_thresholds(rng: random.Random) -> Dict[str, Any]:
    thresholds = [
        ("Measles (highly contagious)", "92% to 95%"),
        ("Polio", "80% to 85%"),
        ("Rubella (German measles)", "83% to 85%"),
    ]
    disease, thresh = rng.choice(thresholds)
    prompt = (
        f"Public health campaigns emphasize reaching a high vaccination coverage threshold ({thresh}) "
        f"to achieve **herd immunity** against infectious diseases like {disease}.\n\n"
        f"What is the principle of herd immunity, and who does it protect?"
    )
    correct = (
        f"When a high percentage of the population ({thresh}) is vaccinated and immune, "
        f"the pathogen cannot find enough susceptible hosts to transmit efficiently; "
        f"this breaks transmission chains and indirectly protects vulnerable individuals who cannot be vaccinated "
        f"(such as newborn infants and immunocompromised individuals)."
    )
    options = [
        correct,
        "When cattle and sheep are vaccinated, they release magical dust into clouds that protects humans.",
        "When 10% of a city is vaccinated, everyone can safely drink untreated raw sewage water.",
        "Herd immunity means humans stop requiring food or clean water because they are immune to starvation.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define herd immunity:\n"
        f"- Herd immunity occurs when sufficient community members are immune that disease transmission slows or halts.\n"
        f"- Crucial benefit: Protects vulnerable groups (newborns, patients undergoing chemotherapy, people with severe allergies to vaccine ingredients) who cannot receive vaccines.\n\n"
        f"**Step 2:** The correct principle is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_47_{rng.randint(100000, 999999)}",
        "subskill": "47_herd_immunity_community_protection_thresholds",
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
            "tier_1": "Who benefits from herd immunity even if they cannot be vaccinated themselves?",
            "tier_2": "Herd immunity breaks chains of transmission, protecting vulnerable and unvaccinated individuals.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["herd_immunity_principle_misconception"],
    }


# 48. Epidemics vs pandemics historical and modern outbreaks
def arch_48_epidemics_vs_pandemics_historical_and_modern_outbreaks(rng: random.Random) -> Dict[str, Any]:
    terms = [
        (
            "Epidemic",
            "A sudden, widespread outbreak of an infectious disease that affects a large number of people within a specific geographic community or region over a limited time (e.g. a cholera outbreak in a municipal district)",
        ),
        (
            "Pandemic",
            "An infectious disease epidemic that has spread across multiple countries, continents, or worldwide, affecting substantial proportions of the global population (e.g. the 1918 influenza or COVID-19)",
        ),
    ]
    target_t, target_d = rng.choice(terms)
    prompt = (
        f"In epidemiology, public health scientists monitor how infectious diseases spread across populations.\n\n"
        f"Which definition scientifically defines an **{target_t}**?"
    )
    correct = target_d
    other_d = [t[1] for t in terms if t[0] != target_t][0]
    options = [
        correct,
        other_d,
        "A non-communicable genetic condition caused by eating too many cold apples.",
        "A weather pattern where ocean winds blow warm air across desert sand dunes.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish epidemic vs pandemic:\n"
        f"- **Endemic**: constantly present at baseline levels in a local area (e.g. malaria in tropical regions).\n"
        f"- **Epidemic**: sudden spike in disease cases exceeding normal expectancy in a specific community or region.\n"
        f"- **Pandemic**: an epidemic that spreads globally across international borders and continents.\n\n"
        f"**Step 2:** For {target_t}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_48_{rng.randint(100000, 999999)}",
        "subskill": "48_epidemics_vs_pandemics_historical_and_modern_outbreaks",
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
            "tier_1": "Is an epidemic regional/local, or does it cover multiple continents worldwide?",
            "tier_2": "Epidemics affect a specific region; pandemics spread across multiple countries or worldwide.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["epidemic_vs_pandemic_distinction_misconception"],
    }


# 49. Evaluating fair test investigation bread mould growth factors
def arch_49_evaluating_fair_test_investigation_bread_mould_growth_factors(rng: random.Random) -> Dict[str, Any]:
    variables = [
        (
            "moisture (dry bread slice vs bread slice sprinkled with 5 mL of water)",
            "moisture presence/level",
            "the percentage surface area of the bread covered by mould colonies after 7 days",
            "same type/brand of bread, same slice thickness, identical incubation temperature (25 °C), kept in sealed transparent ziploc bags in dark cupboards",
        ),
        (
            "temperature (bread slice incubated in a warm cupboard at 28 °C vs bread slice in a refrigerator at 4 °C)",
            "incubation temperature",
            "the growth rate and surface coverage of mould colonies after 7 days",
            "same brand of bread, same moisture added (5 mL water per slice), sealed ziploc bags, identical darkness",
        ),
        (
            "light exposure (bread slice exposed to continuous daylight vs bread slice kept in total darkness)",
            "light exposure vs darkness",
            "the diameter and surface coverage of mould colonies after 7 days",
            "same bread slice size, same moisture added, identical room temperature (22 °C), sealed bags",
        ),
    ]
    investigation_desc, indep, dep, controlled = rng.choice(variables)
    prompt = (
        f"Grade 8 learners design a fair test scientific investigation to determine how environmental conditions affect "
        f"the growth of bread mould (*Rhizopus*).\n\n"
        f"They test the effect of **{investigation_desc}**.\n\n"
        f"Which option accurately identifies the **independent variable**, the **dependent variable**, and the **controlled variables**?"
    )
    correct = (
        f"Independent: {indep};\n"
        f"Dependent: {dep};\n"
        f"Controlled: {controlled}"
    )
    options = [
        correct,
        f"Independent: {dep};\nDependent: {indep};\nControlled: None (fair tests do not require controls)",
        f"Independent: {controlled};\nDependent: {dep};\nControlled: {indep}",
        "Independent: The colour of the kitchen floor tiles;\nDependent: The time the school bell rings;\nControlled: Sunspots",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define investigation variables:\n"
        f"- **Independent variable**: the condition deliberately changed/manipulated by the experimenter ({indep}).\n"
        f"- **Dependent variable**: the factor measured to determine the outcome ({dep}).\n"
        f"- **Controlled variables**: all factors kept constant to ensure a valid fair test ({controlled}).\n\n"
        f"**Step 2:** The correct identification is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_49_{rng.randint(100000, 999999)}",
        "subskill": "49_evaluating_fair_test_investigation_bread_mould_growth_factors",
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
            "tier_1": "Which factor did the learners deliberately change, and which factor did they measure?",
            "tier_2": "The independent variable is the factor changed; the dependent variable is the measured growth.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fair_test_variables_mould_investigation_misconception"],
    }


# 50. Synthetic case study public health outbreak investigation and containment
def arch_50_synthetic_case_study_public_health_outbreak_investigation_and_containment(rng: random.Random) -> Dict[str, Any]:
    outbreaks = [
        (
            "a rural settlement in KwaZulu-Natal experiencing a sudden surge of acute watery diarrhea and vomiting",
            "water samples from a local river revealing high concentrations of *Vibrio cholerae* bacteria following heavy flooding",
            "distributing Oral Rehydration Salts (ORS) packets immediately to save lives, issuing urgent boil-water notices, dosing community water tanks with chlorine, and repairing damaged sewage pipelines",
        ),
        (
            "a boarding school hostel in Gauteng reporting severe coughing, night sweats, fatigue, and chest pains among several dormitories",
            "sputum microscopy confirming airborne transmission of *Mycobacterium tuberculosis* bacteria",
            "isolating infectious patients, conducting contact tracing, initiating a 6-month DOTS antibiotic treatment regimen, and improving dormitory ventilation and window airflow",
        ),
        (
            "a peri-urban community clinic in Mpumalanga recording sudden spikes of recurring high fever, chills, and severe headache during the rainy season",
            "blood smear examination detecting *Plasmodium* parasites transmitted by nocturnal female *Anopheles* mosquitoes",
            "administering artemisinin-based combination therapies (ACTs), distributing insecticide-treated mosquito bed nets, and implementing indoor residual insecticide spraying",
        ),
    ]
    outbreak_setting, lab_confirmation, containment = rng.choice(outbreaks)
    prompt = (
        f"A South African public health outbreak investigation team is deployed to respond to **{outbreak_setting}**.\n\n"
        f"Laboratory diagnostic confirmation: **{lab_confirmation}**.\n\n"
        f"What is the comprehensive protocol required to treat affected individuals and contain further spread?"
    )
    correct = containment
    alt_containment = [o[2] for o in outbreaks if o[0] != outbreak_setting]
    distractors = alt_containment + [
        "Advising the community to stay awake 24 hours a day and drink salt water mixed with cooking oil."
    ]
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the public health outbreak:\n"
        f"- Setting and diagnostic result: {lab_confirmation}.\n"
        f"- Primary clinical priority: immediate life-saving care (e.g. hydration, direct antimicrobial therapy).\n"
        f"- Epidemiological containment: breaking the transmission chain (sanitation, isolation, vector control, ventilation).\n\n"
        f"**Step 2:** The comprehensive protocol is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_50_{rng.randint(100000, 999999)}",
        "subskill": "50_synthetic_case_study_public_health_outbreak_investigation_and_containment",
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
            "tier_1": f"Look at the pathogen identified: {lab_confirmation.split()[0] if lab_confirmation else 'pathogen'}.",
            "tier_2": "Match the specific pathogen and transmission route to its direct clinical treatment and public health containment measures.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["public_health_outbreak_investigation_containment_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "26_yeast_unicellular_fungus_budding_reproduction": arch_26_yeast_unicellular_fungus_budding_reproduction,
    "27_yeast_alcoholic_fermentation_baking_and_brewing": arch_27_yeast_alcoholic_fermentation_baking_and_brewing,
    "28_mould_fungi_rhizopus_bread_mould_and_penicillium": arch_28_mould_fungi_rhizopus_bread_mould_and_penicillium,
    "29_fungal_diseases_athletes_foot_ringworm_and_thrush": arch_29_fungal_diseases_athletes_foot_ringworm_and_thrush,
    "30_antifungal_medications_vs_antibacterial_agents": arch_30_antifungal_medications_vs_antibacterial_agents,
    "31_decomposers_role_in_nutrient_cycling_carbon_and_nitrogen": arch_31_decomposers_role_in_nutrient_cycling_carbon_and_nitrogen,
    "32_symbiotic_nitrogen_fixation_rhizobium_in_legume_nodules": arch_32_symbiotic_nitrogen_fixation_rhizobium_in_legume_nodules,
    "33_lactic_acid_fermentation_lactobacillus_yoghurt_and_amasi": arch_33_lactic_acid_fermentation_lactobacillus_yoghurt_and_amasi,
    "34_human_microbiome_gut_flora_digestion_and_immunity": arch_34_human_microbiome_gut_flora_digestion_and_immunity,
    "35_industrial_and_environmental_biotechnology_bioremediation": arch_35_industrial_and_environmental_biotechnology_bioremediation,
    "36_food_preservation_refrigeration_and_freezing_temperature_inhibition": arch_36_food_preservation_refrigeration_and_freezing_temperature_inhibition,
    "37_food_preservation_heat_pasteurisation_and_canning_sterilisation": arch_37_food_preservation_heat_pasteurisation_and_canning_sterilisation,
    "38_food_preservation_dehydration_salting_and_sugaring_osmotic_control": arch_38_food_preservation_dehydration_salting_and_sugaring_osmotic_control,
    "39_food_preservation_pickling_and_acidification_ph_inhibition": arch_39_food_preservation_pickling_and_acidification_ph_inhibition,
    "40_water_purification_boiling_chlorination_and_filtration_methods": arch_40_water_purification_boiling_chlorination_and_filtration_methods,
    "41_transmission_routes_airborne_waterborne_direct_contact_vector": arch_41_transmission_routes_airborne_waterborne_direct_contact_vector,
    "42_personal_hygiene_soap_and_handwashing_lipid_membrane_disruption": arch_42_personal_hygiene_soap_and_handwashing_lipid_membrane_disruption,
    "43_immune_system_innate_barriers_skin_mucus_and_stomach_acid": arch_43_immune_system_innate_barriers_skin_mucus_and_stomach_acid,
    "44_immune_system_white_blood_cells_phagocytes_and_lymphocytes": arch_44_immune_system_white_blood_cells_phagocytes_and_lymphocytes,
    "45_antibodies_and_antigens_specific_immune_recognition": arch_45_antibodies_and_antigens_specific_immune_recognition,
    "46_vaccination_principles_edward_jenner_and_immune_memory": arch_46_vaccination_principles_edward_jenner_and_immune_memory,
    "47_herd_immunity_community_protection_thresholds": arch_47_herd_immunity_community_protection_thresholds,
    "48_epidemics_vs_pandemics_historical_and_modern_outbreaks": arch_48_epidemics_vs_pandemics_historical_and_modern_outbreaks,
    "49_evaluating_fair_test_investigation_bread_mould_growth_factors": arch_49_evaluating_fair_test_investigation_bread_mould_growth_factors,
    "50_synthetic_case_study_public_health_outbreak_investigation_and_containment": arch_50_synthetic_case_study_public_health_outbreak_investigation_and_containment,
}
