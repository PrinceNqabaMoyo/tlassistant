"""Grade 7 Natural Sciences: Term 1 - The Biosphere (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/01. The Biosphere.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Structural adaptation desert animals camel
def arch_26_structural_adaptation_desert_animals_camel(rng: random.Random) -> Dict[str, Any]:
    features = [
        ("broad, flat padded feet", "spreading body weight over soft loose sand to prevent sinking and insulate soles against hot sand surfaces"),
        ("a dorsal hump containing dense adipose fat tissue", "concentrating insulating fat in one area so heat can escape freely from the rest of the body, and metabolising fat into metabolic water"),
        ("slit-like nostrils that can close tightly and double rows of long interlocking eyelashes", "preventing airborne desert dust and sand grains from entering respiratory airways and eyes during windstorms"),
        ("a thick leathery lining inside the mouth", "allowing the animal to chew thorny desert acacia and scrub bushes without puncturing delicate oral tissues"),
    ]
    feature, survival_advantage = rng.choice(features)
    prompt = (
        f"The dromedary camel possesses remarkable structural adaptations for arid desert biomes. "
        f"Which statement scientifically explains the survival advantage of '{feature}'?"
    )
    correct = survival_advantage
    options = [survival_advantage] + [f[1] for f in features if f[1] != survival_advantage]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review camel adaptations for desert survival:\n"
        f"- Padded feet: prevent sinking in soft sand and protect against heat.\n"
        f"- Fatty hump: isolates fat, avoids trapping body heat, provides metabolic water.\n"
        f"- Slit nostrils / long eyelashes: seal against sandstorms.\n"
        f"- Leathery mouth: enables consumption of thorny desert vegetation.\n\n"
        f"**Step 2:** For '{feature}', the survival advantage is: **{survival_advantage}**."
    )
    return {
        "id": f"ns7_bio_26_{rng.randint(100000, 999999)}",
        "subskill": "26_structural_adaptation_desert_animals_camel",
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
            "tier_1": "Think about the harsh physical challenges in a desert: shifting sand, lack of water, sandstorms, and thorny food.",
            "tier_2": "Match the physical body part directly to how it counters desert conditions.",
            "tier_3": f"The correct survival advantage is: {survival_advantage}.",
        },
        "misconception_tags": ["camel_hump_water_misconception"],
    }


# 27. Structural adaptation aquatic animals fish
def arch_27_structural_adaptation_aquatic_animals_fish(rng: random.Random) -> Dict[str, Any]:
    structures = [
        ("streamlined spindle-shaped (fusiform) body", "minimising fluid drag and friction to allow rapid, energy-efficient movement through dense water"),
        ("filamentous gills with extensive capillary networks", "extracting dissolved oxygen gas directly from water via counter-current diffusion into the bloodstream"),
        ("gas-filled swim bladder", "adjusting overall buoyancy so the fish can remain suspended at varying water depths without sinking or floating"),
        ("flexible caudal (tail) and pectoral fins", "generating forward thrust and providing precise steering and balance in three-dimensional aquatic space"),
    ]
    struct, benefit = rng.choice(structures)
    prompt = (
        f"Fish exhibit specialized structural adaptations that enable survival in the hydrosphere. "
        f"What is the biological function of '{struct}' in a freshwater tilapia?"
    )
    correct = benefit
    options = [benefit] + [s[1] for s in structures if s[1] != benefit]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review aquatic adaptations in fish:\n"
        f"- Fusiform body: reduces water resistance.\n"
        f"- Gills: gas exchange of dissolved oxygen.\n"
        f"- Swim bladder: regulates hydrostatic buoyancy.\n"
        f"- Fins: propulsion and directional stability.\n\n"
        f"**Step 2:** '{struct}' functions by **{benefit}**."
    )
    return {
        "id": f"ns7_bio_27_{rng.randint(100000, 999999)}",
        "subskill": "27_structural_adaptation_aquatic_animals_fish",
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
            "tier_1": "Think about the physical challenges of moving and breathing underwater.",
            "tier_2": "Match the named fish structure to its hydrodynamic or respiratory role.",
            "tier_3": f"The function is: {benefit}.",
        },
        "misconception_tags": ["fish_water_drinking_misconception"],
    }


# 28. Structural adaptation predatory birds raptors
def arch_28_structural_adaptation_predatory_birds_raptors(rng: random.Random) -> Dict[str, Any]:
    raptors = [
        ("The African fish eagle", "large curved talons with rough spicules on toe pads", "gripping slippery, wriggling fish pulled from open water"),
        ("The peregrine falcon", "rigid pointed wings and aerodynamic teardrop silhouette", "reaching diving speeds exceeding 300 km/h to strike avian prey mid-flight"),
        ("The barn owl", "comb-like serrated leading edges on flight feathers and facial disc", "muffling wing-flapping sound for silent flight and funneling faint rodent sounds to asymmetrical ears"),
        ("The martial eagle", "a heavy hooked beak and powerful crushing foot grip", "tearing tough hides and flesh of mammalian prey like monitor lizards and small antelope"),
    ]
    bird, feature, purpose = rng.choice(raptors)
    prompt = (
        f"Predatory birds (raptors) possess specialized structural adaptations. "
        f"In '{bird}', what specific hunting role is performed by '{feature}'?"
    )
    correct = purpose
    options = [purpose] + [r[2] for r in raptors if r[2] != purpose]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze raptor hunting adaptations:\n"
        f"- African fish eagle: curved spiculed talons for catching slippery fish.\n"
        f"- Peregrine falcon: streamlined high-speed diving profile.\n"
        f"- Barn owl: silent flight feathers and parabolic facial disc.\n"
        f"- Martial eagle: powerful beak and crushing talons for large prey.\n\n"
        f"**Step 2:** For '{bird}', '{feature}' is used for **{purpose}**."
    )
    return {
        "id": f"ns7_bio_28_{rng.randint(100000, 999999)}",
        "subskill": "28_structural_adaptation_predatory_birds_raptors",
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
            "tier_1": "Consider what kind of prey this specific raptor hunts.",
            "tier_2": "Fish eagles catch wet fish, owls hunt quietly at night, falcons dive at high speed.",
            "tier_3": f"The answer is: {purpose}.",
        },
        "misconception_tags": ["raptor_adaptation_confusion"],
    }


# 29. Structural adaptation arid plants succulents
def arch_29_structural_adaptation_arid_plants_succulents(rng: random.Random) -> Dict[str, Any]:
    cuticle_um = rng.randint(25, 45)
    parenchyma_cells = rng.randint(4, 8)
    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 220' width='100%' height='220'>"
        f"<rect width='400' height='220' fill='#FBF9F5' rx='8'/>"
        f"<rect x='30' y='20' width='340' height='25' fill='#E0A93B'/>"
        f"<text x='40' y='37' fill='#FFFFFF' font-size='12' font-weight='bold'>Thick Waxy Cuticle ({cuticle_um} um)</text>"
        f"<rect x='30' y='50' width='340' height='40' fill='#5A8C4A'/>"
        f"<text x='40' y='75' fill='#FFFFFF' font-size='12' font-weight='bold'>Epidermis with Sunken Stomata</text>"
        f"<rect x='30' y='95' width='340' height='105' fill='#A7D49B'/>"
        f"<text x='40' y='145' fill='#1E4620' font-size='12' font-weight='bold'>Water-Storage Parenchyma ({parenchyma_cells} layers)</text>"
        f"<circle cx='100' cy='50' r='5' fill='#333333'/>"
        f"<text x='112' y='54' fill='#333333' font-size='10'>Sunken Pit</text>"
        f"</svg>"
    )
    prompt = (
        f"Succulent plants growing in the dry arid Karoo display specialized xerophytic leaf adaptations. "
        f"How does the combination of a thick waxy cuticle of {cuticle_um} micrometres and sunken stomata enable survival during prolonged droughts?"
    )
    correct = "It creates a physical barrier against cuticular evaporation and traps a micro-layer of humid air in stomatal pits, drastically reducing transpirational water loss."
    options = [
        correct,
        "It absorbs solar ultraviolet rays to turn all leaf cells into pure gold.",
        "It forces the succulent to absorb nitrogen gas from rocks without needing roots.",
        "It causes the plant to stop cellular respiration so it never requires oxygen or water.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze xerophytic plant structures:\n"
        f"- Thick waxy cuticle ({cuticle_um} um): waterproof lipid coating stopping non-stomatal water evaporation.\n"
        f"- Sunken stomata in pits: sheltered from dry wind currents, retaining moist air and reducing water potential gradient.\n"
        f"- Large parenchyma ({parenchyma_cells} layers): stores water accumulated during brief rainfall events.\n\n"
        f"**Step 2:** The survival mechanism is: **{correct}**."
    )
    return {
        "id": f"ns7_bio_29_{rng.randint(100000, 999999)}",
        "subskill": "29_structural_adaptation_arid_plants_succulents",
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
            "tier_1": "Recall what wax does to water droplets (it repels water and prevents evaporation).",
            "tier_2": "Sunken stomata protect the plant's pores from dry, hot desert winds.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["succulent_transpiration_misconception"],
    }


# 30. Structural adaptation aquatic plants water lily
def arch_30_structural_adaptation_aquatic_plants_water_lily(rng: random.Random) -> Dict[str, Any]:
    features = [
        ("broad circular leaves that float on the water surface with stomata strictly on the upper epidermis", "allowing direct access to atmospheric carbon dioxide and maximum exposure to sunlight for photosynthesis"),
        ("spongy internal aerenchyma tissue filled with wide air chambers throughout petioles and stems", "providing internal buoyancy so plant parts float and facilitating internal oxygen transport down to submerged roots in anoxic mud"),
        ("weak, flexible stems with minimal xylem lignin", "relying on water buoyancy for physical support rather than investing metabolic energy into rigid woody cellulose"),
        ("a thin waxy coating on upper leaf surfaces", "causing water droplets to bead and roll off rapidly, keeping stomatal pores clear for unobstructed gas exchange"),
    ]
    feature, adaptation_purpose = rng.choice(features)
    prompt = (
        f"The freshwater water lily (Nymphaea) displays specialized hydrophytic adaptations. "
        f"Which statement scientifically explains the purpose of '{feature}'?"
    )
    correct = adaptation_purpose
    options = [adaptation_purpose] + [f[1] for f in features if f[1] != adaptation_purpose]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review hydrophytic plant adaptations:\n"
        f"- Upper stomata on floating leaves: facilitates gas exchange in air rather than water.\n"
        f"- Aerenchyma air chambers: buoyancy and aeration of submerged roots.\n"
        f"- Flexible reduced stems: supported by surrounding water buoyancy.\n"
        f"- Water-repellent cuticle: prevents waterlogging of upper stomatal pores.\n\n"
        f"**Step 2:** For '{feature}', the function is: **{adaptation_purpose}**."
    )
    return {
        "id": f"ns7_bio_30_{rng.randint(100000, 999999)}",
        "subskill": "30_structural_adaptation_aquatic_plants_water_lily",
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
            "tier_1": "Think about why floating on water requires different features from growing on dry land.",
            "tier_2": "Unlike land plants with stomata on the lower leaf surface, floating leaves must breathe from the top.",
            "tier_3": f"The purpose is: {adaptation_purpose}.",
        },
        "misconception_tags": ["hydrophyte_stomatal_position_confusion"],
    }


# 31. Behavioural adaptation nocturnal desert survival
def arch_31_behavioural_adaptation_nocturnal_desert_survival(rng: random.Random) -> Dict[str, Any]:
    temp_day = rng.randint(38, 44)
    temp_night = rng.randint(14, 18)
    animals = [
        ("The aardvark", "digging deep underground burrows during daylight and emerging at night to forage on termites"),
        ("The gerbil (desert rodent)", "remaining inside sealed humid subterranean chambers by day and searching for seeds after dusk"),
        ("The horned adder", "burying itself beneath loose sand during midday heat and ambushing prey during cooler twilight hours"),
    ]
    species, behaviour = rng.choice(animals)
    prompt = (
        f"In the Kalahari Desert, midday surface temperatures reach {temp_day}°C while night temperatures drop to {temp_night}°C. "
        f"{species} survives by {behaviour}. "
        f"Why is being nocturnal considered a **behavioural adaptation** rather than a structural adaptation?"
    )
    correct = "Because it is an active pattern of action and lifestyle timing chosen by the animal, rather than a permanent physical anatomical body structure."
    options = [
        correct,
        "Because behavioural adaptations are passed down through written textbooks rather than genetics.",
        "Because any animal that sleeps during daylight permanently loses its internal skeleton.",
        "Because nocturnal animals do not carry out any cellular respiration while active.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish adaptation categories:\n"
        f"- Structural: physical body structures (e.g. claws, fur, teeth).\n"
        f"- Behavioural: actions and habits (e.g. nocturnal activity, burrowing, migrating).\n"
        f"- Functional: internal biochemical reactions (e.g. venom production, concentrated urine).\n\n"
        f"**Step 2:** Foraging at night ({temp_night}°C) instead of during midday ({temp_day}°C) is an action: **{correct}**."
    )
    return {
        "id": f"ns7_bio_31_{rng.randint(100000, 999999)}",
        "subskill": "31_behavioural_adaptation_nocturnal_desert_survival",
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
            "tier_1": "Ask: Is this an action the animal does, or a physical part of its body?",
            "tier_2": "Actions, habits, and movement schedules are behavioural adaptations.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["adaptation_category_conflation"],
    }


# 32. Behavioural adaptation migration and hibernation
def arch_32_behavioural_adaptation_migration_and_hibernation(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("Long-distance seasonal migration", "The European swallow flying thousands of kilometres to South Africa during the southern summer to escape harsh northern winters and access abundant insects"),
        ("Hibernation (winter torpor)", "An alpine mammal lowering its body temperature, heart rate, and metabolic rate inside an insulated underground den to conserve energy when food is unavailable"),
        ("Aestivation (summer dormancy)", "The African bullfrog sealing itself inside a protective subterranean mucous cocoon during hot, dry summer months until rainy season awakens it"),
    ]
    term, case_study = rng.choice(types)
    prompt = (
        f"Organisms adapt behaviourally to cope with severe seasonal environmental stress. "
        f"Consider this example: \"{case_study}.\"\n\n"
        f"Which ecological behavioural strategy is demonstrated?"
    )
    correct = term
    options = [term] + [t[0] for t in types if t[0] != term]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review seasonal behavioural adaptations:\n"
        f"- Migration = moving to another geographic region.\n"
        f"- Hibernation = metabolic dormancy during freezing winters.\n"
        f"- Aestivation = metabolic dormancy during hot, dry droughts.\n\n"
        f"**Step 2:** The case described is: **{term}**."
    )
    return {
        "id": f"ns7_bio_32_{rng.randint(100000, 999999)}",
        "subskill": "32_behavioural_adaptation_migration_and_hibernation",
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
            "tier_1": "Look at whether the animal travels across the globe or enters a dormant sleep-like state.",
            "tier_2": "Notice if the challenge is winter cold (hibernation/migration) or desert drought (aestivation).",
            "tier_3": f"The strategy is {term}.",
        },
        "misconception_tags": ["hibernation_aestivation_confusion"],
    }


# 33. Functional adaptation water conservation excretion
def arch_33_functional_adaptation_water_conservation_excretion(rng: random.Random) -> Dict[str, Any]:
    adaptations = [
        ("Reptiles and birds excreting nitrogenous waste as semi-solid uric acid paste rather than liquid urine", "Uric acid is insoluble and requires virtually zero water to eliminate, allowing extreme conservation of bodily water"),
        ("The kangaroo rat possessing exceptionally long loops of Henle in its renal nephrons", "Maximising the reabsorption of water from filtrate back into blood capillaries, producing urine that is up to five times more concentrated than seawater"),
        ("Desert scorpions producing an impermeable epicuticle rich in hydrocarbons and waxes", "Completely preventing cutaneous water loss through the exoskeleton into dry ambient desert air"),
    ]
    feature, mechanism = rng.choice(adaptations)
    prompt = (
        f"Functional (physiological) adaptations involve internal biochemical and metabolic processes. "
        f"In arid environments, what is the survival advantage of '{feature}'?"
    )
    correct = mechanism
    options = [mechanism] + [a[1] for a in adaptations if a[1] != mechanism]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze physiological water conservation:\n"
        f"- Excreting uric acid: saves water because uric acid precipitates without needing liquid solvent.\n"
        f"- Extended loops of Henle: hyper-concentrates urine by reabsorbing water.\n"
        f"- Waxy epicuticle: prevents evaporative water loss through body covering.\n\n"
        f"**Step 2:** For '{feature}', the mechanism is: **{mechanism}**."
    )
    return {
        "id": f"ns7_bio_33_{rng.randint(100000, 999999)}",
        "subskill": "33_functional_adaptation_water_conservation_excretion",
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
            "tier_1": "Think about how animals eliminate metabolic waste without wasting precious body water.",
            "tier_2": "Uric acid is white paste that uses almost no water compared to watery urea.",
            "tier_3": f"The answer is: {mechanism}.",
        },
        "misconception_tags": ["uric_acid_water_savings_misconception"],
    }


# 34. South African adaptation fynbos protea fire
def arch_34_south_african_adaptation_fynbos_protea_fire(rng: random.Random) -> Dict[str, Any]:
    years = rng.randint(10, 15)
    prompt = (
        f"The Cape Floral Kingdom (Fynbos biome) experiences natural periodic veld fires every {years} to 20 years. "
        f"Many indigenous Protea species exhibit 'serotiny' (holding seeds inside woody cones that open only after a fire). "
        f"How does this specialized adaptation ensure the survival and reproduction of Protea plants?"
    )
    correct = "The fire destroys dense competing shrubs and deposits nutrient-rich ash on the soil, giving the newly released seeds open sunlight and mineral fertility to germinate."
    options = [
        correct,
        "The fire turns the seeds into pure carbon that feeds underground earthworms.",
        "Protea cones open so that flames can enter the seeds and cook them for passing baboons.",
        "The fire permanently melts the soil rocks into volcanic lava where plants grow faster.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand fire adaptations in Fynbos vegetation:\n"
        f"- Serotiny: thick woody cones protect seeds from the scorching heat of the fire.\n"
        f"- Post-fire release: once the fire passes, the cones dry and open, releasing seeds onto mineral-rich ash.\n"
        f"- Competitive advantage: the fire has cleared canopy shade and thick undergrowth, ensuring high light and water availability for seedlings.\n\n"
        f"**Step 2:** The survival explanation is: **{correct}**."
    )
    return {
        "id": f"ns7_bio_34_{rng.randint(100000, 999999)}",
        "subskill": "34_south_african_adaptation_fynbos_protea_fire",
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
            "tier_1": "Think about what a veld fire clears away (competing bushes) and leaves behind (mineral ash).",
            "tier_2": "Protea seeds are released into ideal open, sunny conditions with fertile ash.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fire_destruction_vs_regeneration_misconception"],
    }


# 35. South African adaptation karoo aloe drought
def arch_35_south_african_adaptation_karoo_aloe_drought(rng: random.Random) -> Dict[str, Any]:
    features = [
        ("thick succulent leaves packed with gelatinous water-storing gel", "acting as an internal water reservoir to sustain cellular metabolism through months of zero rainfall"),
        ("sharp reddish thorns along leaf margins and surfaces", "deterring herbivorous mammals from browsing and consuming the moisture-rich foliage"),
        ("a rosette growth form where leaves direct morning mist and raindrops toward the central taproot", "channelling sparse dew and light rainfall straight to the root zone for rapid absorption"),
        ("a shallow but extensive spreading fibrous root network", "capturing surface moisture from brief sporadic desert rain showers before it evaporates into the dry air"),
    ]
    feature, advantage = rng.choice(features)
    prompt = (
        f"The indigenous Bitter Aloe (Aloe ferox) thrives in the semi-arid Karoo biome of South Africa. "
        f"What is the specific survival advantage of '{feature}' in this harsh environment?"
    )
    correct = advantage
    options = [advantage] + [f[1] for f in features if f[1] != advantage]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Aloe ferox adaptations:\n"
        f"- Gel-filled leaves: water storage through drought.\n"
        f"- Thorns: anti-herbivore physical defense.\n"
        f"- Rosette funneling: dew harvesting towards roots.\n"
        f"- Spreading surface roots: rapid rainwater uptake before evaporation.\n\n"
        f"**Step 2:** '{feature}' operates by **{advantage}**."
    )
    return {
        "id": f"ns7_bio_35_{rng.randint(100000, 999999)}",
        "subskill": "35_south_african_adaptation_karoo_aloe_drought",
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
            "tier_1": "Consider whether the feature protects against thirsty animals, stores water, or catches rain.",
            "tier_2": "Match the named feature of Aloe ferox to its ecological benefit.",
            "tier_3": f"The advantage is: {advantage}.",
        },
        "misconception_tags": ["succulent_adaptation_error"],
    }


# 36. South African adaptation savanna baobab water storage
def arch_36_south_african_adaptation_savanna_baobab_water_storage(rng: random.Random) -> Dict[str, Any]:
    water_litres = rng.choice([100000, 120000, 140000])
    prompt = (
        f"The iconic African Baobab (Adansonia digitata) grows in the arid savanna of Limpopo. "
        f"Its massive swollen trunk can store up to {water_litres:,} litres of water in spongy fibrous wood tissues. "
        f"In addition, the baobab sheds all its leaves during the dry winter season. "
        f"Why does dropping its leaves during winter represent an essential drought survival strategy?"
    )
    correct = "It completely halts transpiration through stomata, preventing catastrophic water loss while soil moisture is unavailable."
    options = [
        correct,
        "It stops the tree from receiving sunlight so that its trunk does not burst from too much energy.",
        "It allows elephants to climb to the top of the tree without being scratched by leaves.",
        "It converts the baobab trunk into an animal that can walk to the nearest river.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze deciduous drought behaviour:\n"
        f"- Leaves are the primary site of transpirational water loss via stomata.\n"
        f"- During the dry season, soil water is depleted.\n"
        f"- By shedding leaves, the tree closes its transpirational pathways completely, conserving the {water_litres:,} litres stored in its trunk until rains return.\n\n"
        f"**Step 2:** The biological reason is: **{correct}**."
    )
    return {
        "id": f"ns7_bio_36_{rng.randint(100000, 999999)}",
        "subskill": "36_south_african_adaptation_savanna_baobab_water_storage",
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
            "tier_1": "Recall where water escapes from a plant (stomata on leaves).",
            "tier_2": "Without leaves, transpiration stops and stored trunk water is preserved.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["leaf_loss_misinterpretation"],
    }


# 37. South African adaptation acacia thorns and taproots
def arch_37_south_african_adaptation_acacia_thorns_and_taproots(rng: random.Random) -> Dict[str, Any]:
    depth_m = rng.randint(45, 65)
    prompt = (
        f"The camel thorn tree (Vachellia erioloba) is a dominant indigenous tree of the Kalahari savanna. "
        f"It possesses an extraordinarily deep vertical taproot extending up to {depth_m} metres into the lithosphere, "
        f"as well as paired white spines (thorns) guarding its small bipinnate leaves. "
        f"Which statement correctly accounts for the combined survival advantage of these two structures?"
    )
    correct = f"The taproot reaches permanent deep groundwater aquifers ({depth_m} m down) untouched by surface drought, while the sharp thorns deter browsing herbivores like giraffes and goats."
    options = [
        correct,
        f"The taproot anchors the tree so it does not float away during snowstorms, while thorns absorb nitrogen gas from the air.",
        "The thorns conduct electricity to shock insects, while the taproot dissolves granite rocks into drinking oil.",
        "Both structures are decorative and provide zero survival advantage in the Kalahari biome.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze Vachellia erioloba adaptations:\n"
        f"- Deep taproot (up to {depth_m} m): taps deep subterranean water tables unavailable to shallow-rooted grasses.\n"
        f"- Thorns: mechanical defense against large mammalian herbivores.\n"
        f"- Bipinnate small leaflets: reduce surface area exposed to scorching sun.\n\n"
        f"**Step 2:** The combined advantage is: **{correct}**."
    )
    return {
        "id": f"ns7_bio_37_{rng.randint(100000, 999999)}",
        "subskill": "37_south_african_adaptation_acacia_thorns_and_taproots",
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
            "tier_1": "Where does a 60-metre root go? Into deep underground water.",
            "tier_2": "What do sharp thorns do to hungry animals trying to eat tender green leaves?",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["taproot_depth_function_confusion"],
    }


# 38. South African adaptation springbok arid physiology
def arch_38_south_african_adaptation_springbok_arid_physiology(rng: random.Random) -> Dict[str, Any]:
    region = rng.choice(["Kalahari Gemsbok National Park", "Great Karoo semi-desert basin", "Namaqualand arid plains", "Kgalagadi Transfrontier Park"])
    water_pct = rng.choice([75, 80, 85])
    prompt = (
        f"The springbok (Antidorcas marsupialis), South Africa's national animal, survives in the {region} without drinking standing open water. "
        f"It obtains hydration from vegetation containing up to {water_pct}% water and minimises fluid loss through excretion. "
        f"Which physiological and dietary adaptation enables the springbok to maintain its water balance in this arid habitat?"
    )
    correct = "It selects moisture-rich succulent plants, bulbs, and tubers dug up before dawn when dew content is highest, and produces highly concentrated urine and dry pellet faeces."
    options = [
        correct,
        "It drinks atmospheric nitrogen directly through its horns during midday dust storms.",
        "It absorbs water molecules across its skin surface from dry sand grains through osmosis.",
        "It permanently switches off all metabolic life processes so its cells never require water.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze springbok water conservation in {region}:\n"
        f"- Food moisture: eats succulent plants, melons, and roots containing up to {water_pct}% water, especially feeding at night when vegetation is covered in dew.\n"
        f"- Excretory conservation: extremely efficient kidneys produce concentrated urine, and rectum reabsorbs water producing dry faecal pellets.\n"
        f"- Metabolic water: cellular respiration breaks down carbohydrates releasing metabolic water.\n\n"
        f"**Step 2:** The adaptation is: **{correct}**."
    )
    return {
        "id": f"ns7_bio_38_{rng.randint(100000, 999999)}",
        "subskill": "38_south_african_adaptation_springbok_arid_physiology",
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
            "tier_1": "Think about where an animal gets water if there are no rivers or waterholes.",
            "tier_2": "Food (roots, tubers, dew on leaves) and reducing water loss in urine and droppings.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["animal_drinking_requirement_absolutism"],
    }


# 39. Compare polar vs desert mammal adaptations
def arch_39_compare_polar_vs_desert_mammal_adaptations(rng: random.Random) -> Dict[str, Any]:
    temp_polar = rng.choice([-35, -40, -45])
    temp_desert = rng.choice([42, 45, 48])
    prompt = (
        f"Compare the adaptations of a polar mammal (e.g. Arctic fox living at {temp_polar}°C) with a desert mammal (e.g. Fennec fox living at +{temp_desert}°C). "
        f"Which comparison correctly contrasts their anatomical thermoregulatory adaptations?"
    )
    correct = "The Arctic fox has short compact ears and a low surface-area-to-volume ratio to minimise heat loss, while the Fennec fox has massive vascularized ears and a high surface-area-to-volume ratio to dissipate excess body heat."
    options = [
        correct,
        "The Arctic fox has giant ears to capture desert breezes, while the Fennec fox grows 10 cm of blubber to freeze itself.",
        "Both foxes have identical physical body shapes because climate has no influence on mammal evolution.",
        "The Arctic fox is cold-blooded and hibernates in snow, while the Fennec fox converts its blood into pure ice.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Apply Allen's rule and Bergmann's rule on thermoregulation:\n"
        f"- Cold climates (Arctic fox): compact extremities (short ears, short snout) reduce surface area, thick blubber/fur insulates against heat loss.\n"
        f"- Hot climates (Fennec fox): oversized ears with rich capillary beds act as cooling radiators, releasing metabolic heat into the air.\n\n"
        f"**Step 2:** The correct contrast is: **{correct}**."
    )
    return {
        "id": f"ns7_bio_39_{rng.randint(100000, 999999)}",
        "subskill": "39_compare_polar_vs_desert_mammal_adaptations",
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
            "tier_1": "Think about ear size: big ears act like car radiators to lose heat, small ears keep heat in.",
            "tier_2": "Desert animals need to lose heat; polar animals must retain heat.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["allens_rule_thermoregulation_confusion"],
    }


# 40. Biosphere altitude and depth limits of life
def arch_40_biosphere_altitude_and_depth_limits_of_life(rng: random.Random) -> Dict[str, Any]:
    altitude_m = rng.choice([8000, 8848])
    depth_m = rng.choice([10000, 11000])
    prompt = (
        f"The biosphere forms a relatively thin veneer on planet Earth, extending from high mountain peaks (~{altitude_m:,} m) to deep oceanic trenches (~{depth_m:,} m). "
        f"Why is active life rare and specialized near these extreme vertical boundaries?"
    )
    correct = "At extreme altitudes, low atmospheric pressure, extreme cold, and scarce oxygen limit metabolism; in the deepest ocean trenches, crushing hydrostatic pressure, freezing temperatures, and total absence of sunlight restrict life to specialized chemosynthetic and barophilic organisms."
    options = [
        correct,
        "Because gravity doubles every 100 metres away from sea level, crushing all organisms.",
        "Because the biosphere is completely empty of any living organisms above 500 metres altitude.",
        "Because ocean water dissolves all cellular membranes within 10 minutes below 50 metres depth.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze physical limits of the biosphere:\n"
        f"- High altitude (Mount Everest, ~{altitude_m} m): thin atmosphere (low pO2), sub-zero temperatures, intense UV radiation limit multicellular life to birds and microbes.\n"
        f"- Deep oceans (Mariana Trench, ~{depth_m} m): over 1,000 atmospheres of hydrostatic pressure, near-freezing temperatures, zero sunlight; organisms rely on chemosynthesis around hydrothermal vents or marine snow.\n\n"
        f"**Step 2:** The limiting factors are: **{correct}**."
    )
    return {
        "id": f"ns7_bio_40_{rng.randint(100000, 999999)}",
        "subskill": "40_biosphere_altitude_and_depth_limits_of_life",
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
            "tier_1": "Think about what is missing on high mountains (oxygen, warmth) and in the deep ocean (light, warmth, manageable pressure).",
            "tier_2": "Extreme pressures, temperatures, and gas availability limit life at the edges of the biosphere.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["biosphere_boundary_misconception"],
    }


# 41. Abiotic factors shaping habitats temperature moisture
def arch_41_abiotic_factors_shaping_habitats_temperature_moisture(rng: random.Random) -> Dict[str, Any]:
    biomes = [
        ("Tropical Rainforest", "consistently high rainfall (>2000 mm/year) and warm year-round temperatures (24-28°C)", "dense multi-layered evergreen canopy with extraordinary biodiversity and rapid nutrient cycling"),
        ("Succulent Karoo", "arid to semi-arid winter rainfall (<200 mm/year) and high summer temperatures with frequent frost in winter", "dwarf succulent shrubs storing water in fleshy leaves and rapid spring flowering geophytes"),
        ("Tundra", "extremely low temperatures (-30°C in winter) with permafrost soil and short 6-8 week growing season", "low-growing mosses, lichens, and dwarf shrubs with no deep root systems"),
        ("Savanna (Grassland with scattered trees)", "distinct summer rainy season followed by prolonged dry winter with high evaporation and periodic fires", "fire-adapted grasses with underground rhizomes and drought-resistant thorny acacia trees"),
    ]
    biome_name, abiotic_profile, vegetation = rng.choice(biomes)
    prompt = (
        f"Abiotic factors such as temperature, rainfall, and soil determine the types of habitats and biomes that develop. "
        f"Which biome is shaped by the abiotic conditions: \"{abiotic_profile}\", resulting in \"{vegetation}\"?"
    )
    correct = biome_name
    options = [biome_name] + [b[0] for b in biomes if b[0] != biome_name]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Link abiotic climate factors to biomes:\n"
        f"- Tropical Rainforest: warm and wet year-round.\n"
        f"- Succulent Karoo: dry (<200 mm), succulents dominate.\n"
        f"- Tundra: permafrost, freezing, mosses and lichens.\n"
        f"- Savanna: seasonal rain/dry winter, grasses and scattered trees.\n\n"
        f"**Step 2:** The described abiotic profile corresponds to **{biome_name}**."
    )
    return {
        "id": f"ns7_bio_41_{rng.randint(100000, 999999)}",
        "subskill": "41_abiotic_factors_shaping_habitats_temperature_moisture",
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
            "tier_1": "Look at the rainfall amount and temperature range.",
            "tier_2": "Match rainfall (<200 mm vs >2000 mm) directly to desert/karoo vs rainforest vs savanna.",
            "tier_3": f"The biome is {biome_name}.",
        },
        "misconception_tags": ["biome_abiotic_factor_confusion"],
    }


# 42. Closed ecological system biosphere 2 lessons
def arch_42_closed_ecological_system_biosphere_2_lessons(rng: random.Random) -> Dict[str, Any]:
    o2_drop = rng.choice([("21% down to 14.5%", "16 months"), ("20.9% down to 14.2%", "14 months"), ("21% down to 15.0%", "18 months")])
    o2_text, duration = o2_drop
    prompt = (
        f"In the early 1990s, scientists constructed 'Biosphere 2' in Arizona, an artificial sealed 1.27-hectare glass dome containing miniature biomes, crops, and eight human researchers. "
        f"During the mission, oxygen levels steadily plummeted from {o2_text} over {duration}, requiring emergency external oxygen injection. "
        f"What was the primary scientific reason for this unexpected collapse in the closed artificial biosphere?"
    )
    correct = "Soil microbes in compost-rich agricultural soils consumed massive amounts of oxygen during aerobic cellular respiration, while unsealed concrete absorbed the resulting carbon dioxide, preventing plants from producing enough replacement oxygen."
    options = [
        correct,
        "The eight human crew members were breathing out poison gases that destroyed all plant life within days.",
        "Sunlight stopped penetrating the glass dome because the glass converted into lead.",
        "Earth's gravity leaked out of the sealed dome, causing all atmospheric gases to float into outer space.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the Biosphere 2 ecological investigation:\n"
        f"- High organic soil: rich in bacteria and fungi performing rapid cellular respiration.\n"
        f"- Respiration consumed oxygen faster than the limited plant canopy could replenish via photosynthesis ({o2_text}).\n"
        f"- Exposed concrete reacted with CO2, sequestering carbon and starving plants of the reactant needed for photosynthesis.\n\n"
        f"**Step 2:** The primary reason for oxygen collapse was: **{correct}**."
    )
    return {
        "id": f"ns7_bio_42_{rng.randint(100000, 999999)}",
        "subskill": "42_closed_ecological_system_biosphere_2_lessons",
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
            "tier_1": "Remember that soil contains billions of living microbes that breathe oxygen.",
            "tier_2": "Microbial decomposition in the rich soil consumed oxygen faster than plants could produce it.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["biosphere_2_oxygen_collapse_misconception"],
    }


# 43. Decomposers recycling dead matter to lithosphere
def arch_43_decomposers_recycling_dead_matter_to_lithosphere(rng: random.Random) -> Dict[str, Any]:
    decomposers = [
        ("Soil bacteria and fungi", "secreting extracellular digestive enzymes onto fallen dead leaves and animal corpses, breaking down complex proteins and carbohydrates into simple nitrates, phosphates, and humus"),
        ("Earthworms (annelids)", "ingesting decaying plant litter and soil, digesting organic fragments, and excreting mineral-rich worm casts that aerate and fertilize topsoil"),
        ("Termites in savanna mounds", "chewing and digesting dead woody cellulose with symbiotic gut flagellates, concentrating minerals in mound soil that enriches surrounding vegetation"),
    ]
    agent, ecological_role = rng.choice(decomposers)
    prompt = (
        f"Decomposers play a critical ecological role in connecting the biosphere to the lithosphere. "
        f"Which statement describes how '{agent}' facilitates nutrient recycling?"
    )
    correct = ecological_role
    options = [ecological_role] + [d[1] for d in decomposers if d[1] != ecological_role]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review the role of decomposers in nutrient cycles:\n"
        f"- Without decomposers, dead organic matter would accumulate indefinitely and lock up essential minerals.\n"
        f"- Decomposers convert organic remains back into inorganic mineral salts (nitrates, phosphates, potassium) returned to the soil.\n\n"
        f"**Step 2:** For '{agent}', the mechanism is: **{ecological_role}**."
    )
    return {
        "id": f"ns7_bio_43_{rng.randint(100000, 999999)}",
        "subskill": "43_decomposers_recycling_dead_matter_to_lithosphere",
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
            "tier_1": "Think about what happens to dead animals and fallen leaves in nature.",
            "tier_2": "Decomposers break down organic compounds and return minerals to the soil.",
            "tier_3": f"The answer is: {ecological_role}.",
        },
        "misconception_tags": ["decomposer_nutrient_recycling_misconception"],
    }


# 44. Photosynthesis and respiration gas exchange cycle
def arch_44_photosynthesis_and_respiration_gas_exchange_cycle(rng: random.Random) -> Dict[str, Any]:
    sugar_mg = rng.randint(15, 30)
    animal = rng.choice(["zebra", "springbok", "impala", "kudu"])
    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 420 220' width='100%' height='220'>"
        f"<rect width='420' height='220' fill='#F6F9FB' rx='8'/>"
        f"<circle cx='100' cy='110' r='60' fill='#D8ECD5' stroke='#4C8C40' stroke-width='2'/>"
        f"<text x='65' y='100' fill='#24561C' font-size='11' font-weight='bold'>Green Plant</text>"
        f"<text x='55' y='116' fill='#24561C' font-size='10'>Photosynthesis</text>"
        f"<text x='50' y='132' fill='#24561C' font-size='9'>Glucose: {sugar_mg} mg</text>"
        f"<circle cx='320' cy='110' r='60' fill='#FDE2D2' stroke='#D45728' stroke-width='2'/>"
        f"<text x='290' y='105' fill='#8A2C08' font-size='11' font-weight='bold'>{animal.capitalize()}</text>"
        f"<text x='285' y='125' fill='#8A2C08' font-size='10'>Respiration</text>"
        f"<path d='M 150 70 C 210 30, 230 30, 270 70' fill='none' stroke='#2A75D3' stroke-width='3'/>"
        f"<text x='185' y='45' fill='#1E5BA8' font-size='12' font-weight='bold'>Oxygen (O2)</text>"
        f"<path d='M 270 150 C 230 190, 210 190, 150 150' fill='none' stroke='#7A5A35' stroke-width='3'/>"
        f"<text x='165' y='190' fill='#5A4020' font-size='12' font-weight='bold'>Carbon Dioxide (CO2)</text>"
        f"</svg>"
    )
    prompt = (
        f"In the biosphere, living organisms participate in a continuous gas exchange cycle between the atmosphere and cells. "
        f"A green plant synthesises {sugar_mg} mg of glucose during daytime. "
        f"Which statement correctly describes how gases are exchanged between the plant and a {animal} in this ecosystem?"
    )
    correct = f"The plant absorbs carbon dioxide and releases oxygen during photosynthesis; the {animal} inhales oxygen for cellular respiration and exhales carbon dioxide which the plant re-uses."
    options = [
        correct,
        f"Both the plant and the {animal} absorb nitrogen gas to build glucose sugars without releasing any gas.",
        f"The plant releases carbon dioxide as its only waste product, which the {animal} uses to perform photosynthesis.",
        f"The {animal} exhales pure liquid water vapour that permanently destroys the atmosphere.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the reciprocal gas exchange cycle:\n"
        f"- Photosynthesis: 6CO2 + 6H2O + radiant energy -> C6H12O6 ({sugar_mg} mg) + 6O2 (absorbs CO2, releases O2).\n"
        f"- Cellular respiration: C6H12O6 + 6O2 -> 6CO2 + 6H2O + ATP (absorbs O2, releases CO2 in {animal}).\n\n"
        f"**Step 2:** The reciprocal exchange is: **{correct}**."
    )
    return {
        "id": f"ns7_bio_44_{rng.randint(100000, 999999)}",
        "subskill": "44_photosynthesis_and_respiration_gas_exchange_cycle",
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
            "tier_1": "Recall what gas plants release during photosynthesis that animals breathe in.",
            "tier_2": "Plants release O2 and take in CO2; animals take in O2 and release CO2.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["photosynthesis_respiration_gas_cycle_reversal"],
    }


# 45. Soil erosion impact on biosphere sustainability
def arch_45_soil_erosion_impact_on_biosphere_sustainability(rng: random.Random) -> Dict[str, Any]:
    threats = [
        ("Overgrazing by livestock removing grass cover", "exposing loose topsoil to torrential rainfall and strong winds, washing fertile humus into rivers and leaving barren subsoil"),
        ("Deforestation and clear-cutting on steep slopes", "removing root binding networks that anchor soil, triggering severe mudslides and loss of fertile arable land"),
        ("Monoculture crop cultivation without crop rotation", "depleting essential soil nitrogen and minerals, causing soil structure degradation and vulnerability to wind erosion"),
    ]
    threat, consequence = rng.choice(threats)
    prompt = (
        f"Soil in the lithosphere is a non-renewable resource on human timescales. "
        f"How does '{threat}' directly threaten the sustainability of the biosphere?"
    )
    correct = f"By {consequence.lower()}."
    distractors = [
        "By permanently turning all rainwater into solid quartz crystals.",
        "By causing the Earth's crust to fall into the Sun within months.",
        "By forcing earthworms to convert into marine fish that swim in dry sand.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand soil erosion in ecosystems:\n"
        f"- Topsoil takes hundreds of years to form through rock weathering and organic decay.\n"
        f"- When vegetation is stripped (overgrazing, deforestation), rain and wind strip the humus-rich top layer.\n"
        f"- Without topsoil, plants cannot grow, destroying the primary producer base of terrestrial food webs.\n\n"
        f"**Step 2:** The impact is: **{correct}**."
    )
    return {
        "id": f"ns7_bio_45_{rng.randint(100000, 999999)}",
        "subskill": "45_soil_erosion_impact_on_biosphere_sustainability",
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
            "tier_1": "Think about what protects the soil from being washed away by rain (plant roots and grass cover).",
            "tier_2": "Removing plants exposes topsoil to erosion, preventing future plant growth.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["soil_erosion_impact_misconception"],
    }


# 46. Water pollution impact on hydrosphere organisms
def arch_46_water_pollution_impact_on_hydrosphere_organisms(rng: random.Random) -> Dict[str, Any]:
    pollutants = [
        ("Agricultural fertilizer runoff rich in nitrates and phosphates", "eutrophication: rapid algal blooms block sunlight, and subsequent decomposition by aerobic bacteria consumes dissolved oxygen, suffocating fish"),
        ("Untreated domestic sewage discharge containing pathogenic bacteria", "spreading cholera and waterborne diseases while severe bacterial decomposition depletes dissolved oxygen in streams"),
        ("Industrial acid mine drainage with heavy metals and sulfuric acid", "drastically lowering water pH below tolerance limits and precipitating toxic heavy metal salts that poison aquatic gill membranes"),
    ]
    agent, mechanism = rng.choice(pollutants)
    prompt = (
        f"Pollution of the hydrosphere severely disrupts aquatic ecosystems in South Africa. "
        f"What is the ecological consequence when '{agent}' enters freshwater dams and rivers?"
    )
    correct = mechanism
    options = [mechanism] + [p[1] for p in pollutants if p[1] != mechanism]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze aquatic pollution pathways:\n"
        f"- Fertilizer runoff -> algal bloom -> algae die -> decomposers use all oxygen -> fish suffocate (eutrophication).\n"
        f"- Sewage -> pathogens and oxygen depletion.\n"
        f"- Acid mine drainage -> low pH and heavy metal toxicity.\n\n"
        f"**Step 2:** For '{agent}', the consequence is: **{mechanism}**."
    )
    return {
        "id": f"ns7_bio_46_{rng.randint(100000, 999999)}",
        "subskill": "46_water_pollution_impact_on_hydrosphere_organisms",
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
            "tier_1": "Notice whether the pollutant is fertilizer (algal blooms/eutrophication), sewage (pathogens), or acid mine water.",
            "tier_2": "Fertilizers cause algae to explode, which later die and rot, consuming all dissolved oxygen.",
            "tier_3": f"The consequence is: {mechanism}.",
        },
        "misconception_tags": ["eutrophication_mechanism_misconception"],
    }


# 47. Air quality impact on atmosphere and living things
def arch_47_air_quality_impact_on_atmosphere_and_living_things(rng: random.Random) -> Dict[str, Any]:
    pollutants = [
        ("Sulfur dioxide (SO2) from coal-fired power stations", "combining with atmospheric moisture to form sulfuric acid precipitation (acid rain), which leaches soil minerals and burns plant leaves"),
        ("Excess carbon dioxide (CO2) from burning fossil fuels", "intensifying the enhanced greenhouse effect by trapping outgoing terrestrial infrared radiation, driving global climate warming"),
        ("Ground-level ozone (O3) and photochemical smog from vehicle emissions", "damaging human lung tissue and oxidizing plant mesophyll cells, reducing photosynthetic efficiency in crops"),
    ]
    substance, impact = rng.choice(pollutants)
    prompt = (
        f"Atmospheric air quality is vital for sustaining healthy terrestrial organisms. "
        f"Which ecological impact is directly caused by '{substance}'?"
    )
    correct = impact
    options = [impact] + [p[1] for p in pollutants if p[1] != impact]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Match atmospheric emissions to their environmental impacts:\n"
        f"- Sulfur dioxide (SO2) -> acid rain.\n"
        f"- Carbon dioxide (CO2) -> enhanced greenhouse effect and climate warming.\n"
        f"- Photochemical smog / tropospheric ozone -> respiratory and leaf tissue damage.\n\n"
        f"**Step 2:** For '{substance}', the direct impact is: **{impact}**."
    )
    return {
        "id": f"ns7_bio_47_{rng.randint(100000, 999999)}",
        "subskill": "47_air_quality_impact_on_atmosphere_and_living_things",
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
            "tier_1": "Match sulfur dioxide to acid rain, or carbon dioxide to global warming.",
            "tier_2": "Acid rain comes from sulfur and nitrogen oxides; enhanced greenhouse effect comes from greenhouse gases like CO2.",
            "tier_3": f"The answer is: {impact}.",
        },
        "misconception_tags": ["greenhouse_vs_acid_rain_confusion"],
    }


# 48. Microorganisms role as living agents in biosphere
def arch_48_microorganisms_role_as_living_agents_in_biosphere(rng: random.Random) -> Dict[str, Any]:
    microbes = [
        ("Rhizobium bacteria in legume root nodules", "Biological nitrogen fixation: converting inert atmospheric nitrogen gas (N2) into bioavailable ammonium and nitrates that plants use to build proteins"),
        ("Phytoplankton (microscopic cyanobacteria and diatoms) in ocean surface waters", "Primary production and oxygen generation: generating over 50% of the biosphere's atmospheric oxygen via marine photosynthesis"),
        ("Saccharomyces cerevisiae (yeast)", "Fermentation: anaerobically breaking down sugars to produce ethanol and carbon dioxide, utilized in bread baking and brewing"),
        ("Gut microbiota in herbivore digestive tracts", "Cellulose digestion: breaking down tough plant cell walls using cellulase enzymes so herbivores can extract energy from grass"),
    ]
    organism, ecological_role = rng.choice(microbes)
    prompt = (
        f"Although invisible to the naked eye, microorganisms are essential living components of the biosphere. "
        f"What vital biological role is performed by '{organism}'?"
    )
    correct = ecological_role
    options = [ecological_role] + [m[1] for m in microbes if m[1] != ecological_role]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review critical microbial ecological functions:\n"
        f"- Rhizobium: fixes atmospheric N2 into nitrates.\n"
        f"- Phytoplankton: produces over 50% of Earth's oxygen.\n"
        f"- Yeast: anaerobic fermentation.\n"
        f"- Gut symbionts: digest plant cellulose for herbivores.\n\n"
        f"**Step 2:** For '{organism}', the role is: **{ecological_role}**."
    )
    return {
        "id": f"ns7_bio_48_{rng.randint(100000, 999999)}",
        "subskill": "48_microorganisms_role_as_living_agents_in_biosphere",
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
            "tier_1": "Consider whether the microbe helps plants get nitrogen, makes oxygen in the ocean, or lives in the gut.",
            "tier_2": "Rhizobium lives in root nodules; phytoplankton lives in the sea; yeast ferments sugar.",
            "tier_3": f"The answer is: {ecological_role}.",
        },
        "misconception_tags": ["all_microbes_are_germs_misconception"],
    }


# 49. Classify organism requirements matrix
def arch_49_classify_organism_requirements_matrix(rng: random.Random) -> Dict[str, Any]:
    organisms = [
        ("A freshwater river crab (Potamonautes)", "Aquatic habitat, dissolved oxygen for gill respiration, liquid water, detrital organic food, sub-surface shelter beneath rocks"),
        ("A desert succulent plant (Lithops / living stone)", "Arid gravelly soil, intense sunlight, intermittent sparse rainfall, atmospheric carbon dioxide, high daytime temperatures"),
        ("A subterranean mole-rat (Cryptomys)", "Dark underground tunnel habitat, plant bulbs/roots for nutrition and hydration, atmospheric air diffusing through porous soil, cool stable temperatures"),
    ]
    org_name, req_profile = rng.choice(organisms)
    prompt = (
        f"Every living organism in the biosphere requires a specific combination of abiotic resources to sustain life. "
        f"Which environmental resource profile accurately matches the life requirements of '{org_name}'?"
    )
    correct = req_profile
    options = [req_profile] + [o[1] for o in organisms if o[1] != req_profile]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze habitat requirements for '{org_name}':\n"
        f"- River crab: needs water, dissolved O2, rocky cover.\n"
        f"- Lithops: needs intense light, dry mineral soil, minimal water.\n"
        f"- Mole-rat: subterranean burrows, bulbs/tubers for food and water.\n\n"
        f"**Step 2:** The matching profile is: **{req_profile}**."
    )
    return {
        "id": f"ns7_bio_49_{rng.randint(100000, 999999)}",
        "subskill": "49_classify_organism_requirements_matrix",
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
            "tier_1": "Think about where this organism lives: in a river, deep underground, or on dry desert stones.",
            "tier_2": "Match the organism's natural habitat directly to its resource needs.",
            "tier_3": f"The answer is: {req_profile}.",
        },
        "misconception_tags": ["organism_habitat_mismatch"],
    }


# 50. Synthetic case study ecosystem disruption analysis
def arch_50_synthetic_case_study_ecosystem_disruption_analysis(rng: random.Random) -> Dict[str, Any]:
    disruptions = [
        (
            "An alien invasive tree species (black wattle / Acacia mearnsii) invades a South African riparian river catchment",
            "Consumes exceptionally high volumes of groundwater (hydrosphere), drying up riverbeds, crowding out native fynbos (biosphere), and increasing wildfire severity",
        ),
        (
            "An open-cast coal mine strips topsoil and discharges acidic leachate into surrounding wetlands",
            "Destroys topsoil horizons in the lithosphere, severely acidifies the hydrosphere, and causes local extinctions of aquatic invertebrates and fish in the biosphere",
        ),
        (
            "Extensive aerial pesticide spraying eliminates pollinating honeybees and hoverflies across an agricultural valley",
            "Disrupts pollination across wild plants and fruit crops in the biosphere, collapsing fruit production and starving seed-eating birds and small mammals",
        ),
    ]
    event, ecological_chain = rng.choice(disruptions)
    prompt = (
        f"Consider the following environmental crisis in South Africa:\n"
        f"\"{event}.\"\n\n"
        f"Which analysis correctly traces the cascading ecological disruption across Earth's interconnected spheres?"
    )
    correct = ecological_chain
    options = [ecological_chain] + [d[1] for d in disruptions if d[1] != ecological_chain]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze systemic ecological disruption across spheres:\n"
        f"- Biotic elements (species) interact dynamically with abiotic reserves (water, soil, air).\n"
        f"- A disturbance in one component cascades into the others.\n\n"
        f"**Step 2:** For '{event}', the cascading consequence is: **{ecological_chain}**."
    )
    return {
        "id": f"ns7_bio_50_{rng.randint(100000, 999999)}",
        "subskill": "50_synthetic_case_study_ecosystem_disruption_analysis",
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
            "tier_1": "Trace how altering one sphere (e.g. river water, topsoil, or pollinators) affects the other spheres.",
            "tier_2": "Look at the cause-and-effect relationship in the scenario.",
            "tier_3": f"The answer is: {ecological_chain}.",
        },
        "misconception_tags": ["ecosystem_interconnection_blindspot"],
    }
