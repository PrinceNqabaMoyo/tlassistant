"""Grade 7 Natural Sciences: Term 1 - Variation (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/04. Variation.md.
Focus: Natural Selection, Survival Advantage, Inheritance, Selective Breeding, and Genetic Variation.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Survival value of variation in environmental change
def arch_26_survival_value_of_variation_environmental_change(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("a sudden prolonged drought in the Karoo semi-desert", "wild grass species", "individuals with deeper root systems and thicker leaf cuticles"),
        ("a severe fungal disease epidemic spreading through an indigenous forest", "yellowwood trees (Podocarpus)", "individual trees carrying natural immune resistance alleles"),
        ("an unusually cold winter with sub-zero frosts in the Highveld", "aloe succulent populations", "succulent plants with higher cellular sugar concentrations that lower freezing point"),
    ]
    env_event, species_name, surviving_trait = rng.choice(scenarios)
    prompt = (
        f"Consider a natural population of {species_name}. When {env_event} occurs, "
        f"{surviving_trait} are able to survive and reproduce while others perish.\n\n"
        f"Why is genetic variation within a species considered essential for the long-term survival of that species?"
    )
    correct = (
        f"Variation ensures that at least some individuals possess advantageous traits that allow them to survive "
        f"drastic environmental changes, preventing the complete extinction of the population."
    )
    options = [
        correct,
        "Variation ensures that all individuals become genetically identical clones over time.",
        "Variation causes animals to stop reproducing sexually so that food supplies increase.",
        "Variation guarantees that organisms never face competition or predation in nature.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the evolutionary importance of genetic variation:\n"
        f"- In a uniform population with zero variation, an environmental catastrophe (such as {env_event}) could wipe out all individuals.\n"
        f"- Natural variation provides the biological raw material: some individuals with {surviving_trait} survive and pass on their alleles.\n\n"
        f"**Step 2:** The core reason is: **{correct}**."
    )
    return {
        "id": f"ns7_var_26_{rng.randint(100000, 999999)}",
        "subskill": "26_survival_value_of_variation_environmental_change",
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
            "tier_1": "Think about what happens if every organism is identical when a lethal virus arrives.",
            "tier_2": "If all are identical, all die. If there is variation, resistant individuals survive.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["variation_survival_misconception"],
    }


# 27. Natural selection concept and mechanism
def arch_27_natural_selection_concept_and_mechanism(rng: random.Random) -> Dict[str, Any]:
    steps = [
        "1. Overproduction of offspring -> 2. Natural variation in population -> 3. Struggle for existence (competition) -> 4. Survival and reproduction of best adapted -> 5. Inheritance of advantageous traits",
        "1. Organisms decide which traits they want -> 2. Traits mutate consciously -> 3. Environment changes to match organisms",
        "1. Natural cloning occurs -> 2. Zero competition -> 3. All organisms survive equally",
        "1. Extinction of all predators -> 2. Prey animals stop reproducing -> 3. Zero variation",
    ]
    correct = steps[0]
    options = list(steps)
    rng.shuffle(options)
    prompt = (
        f"Charles Darwin proposed the theory of evolution by natural selection to explain biological adaptation.\n\n"
        f"Which sequence correctly outlines the logical stages of natural selection occurring within a natural population?"
    )
    sol = (
        f"**Step 1:** Recall the 5 logical pillars of natural selection:\n"
        f"1. Overproduction of offspring (more born than can survive).\n"
        f"2. Variation exists naturally within the species.\n"
        f"3. Competition for limited resources (struggle for existence).\n"
        f"4. Differential survival and reproduction (individuals with favourable variations survive).\n"
        f"5. Advantageous traits are passed to the next generation.\n\n"
        f"**Step 2:** The correct logical sequence is: **{correct}**."
    )
    return {
        "id": f"ns7_var_27_{rng.randint(100000, 999999)}",
        "subskill": "27_natural_selection_concept_and_mechanism",
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
            "tier_1": "Recall the order: more offspring born than resources, natural differences exist, only adapted survive.",
            "tier_2": "Overproduction leads to competition, where naturally adapted variants survive and reproduce.",
            "tier_3": f"The correct sequence is: {correct}.",
        },
        "misconception_tags": ["natural_selection_stages_misconception"],
    }


# 28. Peppered moth pre-industrial lichen camouflage (with dynamic SVG)
def arch_28_peppered_moth_pre_industrial_lichen_camouflage(rng: random.Random) -> Dict[str, Any]:
    pale_count = rng.randint(85, 95)
    dark_count = 100 - pale_count
    lichen_color = rng.choice(["#C8D6AF", "#D1E2C4", "#B8C9A3"])

    svg = (
        f'<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<rect x="20" y="20" width="360" height="200" fill="{lichen_color}" rx="6" />'
        f'<text x="200" y="45" font-size="14" font-weight="bold" fill="#2d3748" text-anchor="middle">Pre-Industrial Forest: Pale Lichen-Covered Bark</text>'
        f'<ellipse cx="120" cy="130" rx="35" ry="20" fill="#E2E8F0" stroke="#94A3B8" stroke-dasharray="3,3" />'
        f'<text x="120" y="135" font-size="11" fill="#475569" font-weight="bold" text-anchor="middle">Pale Moth ({pale_count}%)</text>'
        f'<text x="120" y="175" font-size="10" fill="#1e293b" text-anchor="middle">[Camouflaged]</text>'
        f'<ellipse cx="280" cy="130" rx="35" ry="20" fill="#1E293B" stroke="#0F172A" />'
        f'<text x="280" y="135" font-size="11" fill="#FFFFFF" font-weight="bold" text-anchor="middle">Dark Moth ({dark_count}%)</text>'
        f'<text x="280" y="175" font-size="10" fill="#dc2626" font-weight="bold" text-anchor="middle">[High Predation Risk]</text>'
        f'<text x="200" y="210" font-size="10" fill="#4b5563" text-anchor="middle">Observed morph proportions: Pale={pale_count}%, Dark={dark_count}%</text>'
        f'</svg>'
    )

    prompt = (
        f"In England before the Industrial Revolution, tree trunks were heavily covered in pale lichens. "
        f"Surveys recorded that pale peppered moths (*Biston betularia*) made up approximately {pale_count}% of the population, "
        f"while dark (melanic) moths made up only {dark_count}%.\n\n"
        f"What was the primary evolutionary reason for the dominance of the pale morph in this environment?"
    )
    correct = "Pale moths were well camouflaged against pale lichen-covered bark, making them harder for predatory birds to see and eat."
    options = [
        correct,
        "Dark moths were poisonous to eat, so birds ate all the pale moths instead.",
        "Pale moths produced toxic fumes that killed all dark moths in the forest.",
        "Lichens fed exclusively on dark moths, leaving pale moths untouched.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the selective pressure in the pre-industrial habitat:\n"
        f"- Tree trunks were covered in pale lichens.\n"
        f"- Pale peppered moths blended seamlessly into the pale background (crypsis/camouflage).\n"
        f"- Visual predators (insectivorous birds) easily spotted the contrasting dark moths, keeping their numbers low ({dark_count}%).\n\n"
        f"**Step 2:** The reason is: **{correct}**."
    )
    return {
        "id": f"ns7_var_28_{rng.randint(100000, 999999)}",
        "subskill": "28_peppered_moth_pre_industrial_lichen_camouflage",
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
            "tier_1": "Which moth blends into pale lichen on a tree trunk?",
            "tier_2": "Pale moths camouflage against pale lichens, avoiding bird predation.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["peppered_moth_camouflage_misconception"],
    }


# 29. Peppered moth industrial melanism sooty bark
def arch_29_peppered_moth_industrial_melanism_sooty_bark(rng: random.Random) -> Dict[str, Any]:
    soot_density = rng.choice(["heavy coal smoke and sulfur dioxide", "dense industrial airborne soot and sulfur emissions"])
    dark_percentage = rng.randint(88, 98)
    prompt = (
        f"During the Industrial Revolution in British manufacturing regions, {soot_density} killed the pale lichens "
        f"and blackened tree trunks with soot. Within decades, dark (melanic) moths surged to {dark_percentage}% of the population.\n\n"
        f"What biological process caused this dramatic shift in allele frequency and phenotype?"
    )
    correct = "Industrial melanism driven by natural selection, where dark moths gained a camouflage advantage on soot-blackened trees."
    options = [
        correct,
        "Individual white moths flew into chimney smoke and got physically stained black for life.",
        "White moths spontaneously morphed into black beetles due to air pressure.",
        "Dark moths decided to stop laying eggs so pale moths could survive.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Explain industrial melanism:\n"
        f"- The environment changed: lichens died and tree trunks became blackened by soot.\n"
        f"- Now, dark moths had the camouflage advantage, while pale moths stood out against black bark and were preyed upon by birds.\n"
        f"- Dark moths survived at higher rates, reproduced, and passed the melanic allele to offspring, reaching {dark_percentage}%.\n\n"
        f"**Step 2:** This phenomenon is: **{correct}**."
    )
    return {
        "id": f"ns7_var_29_{rng.randint(100000, 999999)}",
        "subskill": "29_peppered_moth_industrial_melanism_sooty_bark",
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
            "tier_1": "Did soot stain individual moths, or did birds eat the conspicuous ones?",
            "tier_2": "Birds ate pale moths that no longer matched the sooty trees, leaving dark moths to reproduce.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["lamarckian_staining_misconception"],
    }


# 30. Peppered moth Clean Air Act recovery
def arch_30_peppered_moth_clean_air_act_recovery(rng: random.Random) -> Dict[str, Any]:
    year = rng.choice([1956, 1968])
    pale_recovery = rng.randint(70, 85)
    prompt = (
        f"Following the passage of Clean Air legislation in the United Kingdom around {year}, coal smoke emissions were strictly regulated. "
        f"Soot levels declined, and pale lichens gradually recolonised the tree trunks. "
        f"Biologists subsequently observed that pale peppered moths recovered to over {pale_recovery}% of the population.\n\n"
        f"What does this reversal demonstrate about natural selection?"
    )
    correct = "Natural selection is reversible and dynamic; when the environment shifts back, the trait that provides survival advantage changes accordingly."
    options = [
        correct,
        "Natural selection is a permanent one-way process that can never reverse once dark alleles dominate.",
        "Air legislation directly modified the DNA of moths through government chemicals.",
        "Moths stopped undergoing sexual reproduction and cloned themselves to survive.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the impact of environmental restoration:\n"
        f"- Clean air allowed lichens to regrow, making tree bark pale again.\n"
        f"- The selective pressure reversed: pale moths once again had superior camouflage, while dark moths became conspicuous prey.\n"
        f"- This shows that natural selection is not static; it dynamically responds to environmental conditions.\n\n"
        f"**Step 2:** The deduction is: **{correct}**."
    )
    return {
        "id": f"ns7_var_30_{rng.randint(100000, 999999)}",
        "subskill": "30_peppered_moth_clean_air_act_recovery",
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
            "tier_1": "What happened to tree colour when the air became clean again?",
            "tier_2": "Trees became pale again, so pale moths had the survival advantage once more.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["evolution_directionality_misconception"],
    }


# 31. Antibiotic resistance as natural selection
def arch_31_antibiotic_resistance_as_natural_selection(rng: random.Random) -> Dict[str, Any]:
    bacteria_types = [
        ("Staphylococcus aureus", "Methicillin / Penicillin"),
        ("Mycobacterium tuberculosis", "Rifampicin / Isoniazid"),
        ("Streptococcus pneumoniae", "Amoxicillin"),
    ]
    bacterium, antibiotic = rng.choice(bacteria_types)
    prompt = (
        f"A patient infected with {bacterium} starts taking the antibiotic {antibiotic}. "
        f"After a few days, the patient feels better and stops taking the pills before completing the prescribed course. "
        f"Two weeks later, the infection returns much worse and {antibiotic} no longer works.\n\n"
        f"How does natural selection explain the emergence of antibiotic-resistant bacteria in this patient?"
    )
    correct = (
        f"Natural variation meant a few bacteria had partial resistance mutations; stopping the treatment early killed "
        f"the sensitive bacteria but allowed the resistant variants to survive, multiply, and dominate the population."
    )
    options = [
        correct,
        f"The antibiotic changed into sugar and fed the bacteria so they grew much larger.",
        f"The bacteria learned to love {antibiotic} and taught other bacteria how to drink it.",
        f"The patient's immune system turned into bacteria to fight off the antibiotic.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Explain antibiotic resistance through natural selection:\n"
        f"- Bacterial populations contain billions of individuals with random genetic mutations.\n"
        f"- Incomplete antibiotic treatment kills the most vulnerable bacteria first.\n"
        f"- Naturally resistant mutants survive the sub-lethal dose, reproduce rapidly without competition, and pass their resistance genes to billions of descendants.\n\n"
        f"**Step 2:** The mechanism is: **{correct}**."
    )
    return {
        "id": f"ns7_var_31_{rng.randint(100000, 999999)}",
        "subskill": "31_antibiotic_resistance_as_natural_selection",
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
            "tier_1": "Which bacteria survive when an antibiotic dose is cut short?",
            "tier_2": "The naturally resistant bacteria survive, reproduce, and pass resistance genes to offspring.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["antibiotic_resistance_misconception"],
    }


# 32. Pesticide resistance in crop pests
def arch_32_pesticide_resistance_in_crop_pests(rng: random.Random) -> Dict[str, Any]:
    crops = [
        ("maize stem borer (Busseola fusca)", "maize crops in the Free State"),
        ("cotton bollworm (Helicoverpa armigera)", "cotton fields in Mpumalanga"),
        ("citrus red mite (Panonychus citri)", "citrus orchards in the Eastern Cape"),
    ]
    pest, field = rng.choice(crops)
    years = rng.choice([3, 5, 7])
    prompt = (
        f"A commercial farmer spraying synthetic chemical pesticide against {pest} on {field} "
        f"finds that after {years} consecutive years of spraying the same chemical, the pesticide is almost completely ineffective.\n\n"
        f"What is the correct scientific explanation for this failure of pest control?"
    )
    correct = (
        "Rare individual pests carried random pre-existing genetic resistance; continuous spraying killed susceptible pests, "
        "allowing resistant survivors to breed and form a resistant population."
    )
    options = [
        correct,
        "Individual insects drank small drops of pesticide every day to build muscular tolerance.",
        "The pesticide transformed into a nutritious plant fertilizer that pests enjoyed eating.",
        "The crop plants developed empathy for the pests and protected them from the chemical spray.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand artificial selection of resistance alleles:\n"
        f"- The pesticide does not induce mutations; pre-existing natural variation already contained rare resistance alleles.\n"
        f"- Repeated spraying exerts intense selective pressure, eliminating susceptible individuals.\n"
        f"- The few resistant individuals survive, reproduce, and rapidly replace the susceptible population.\n\n"
        f"**Step 2:** The scientific explanation is: **{correct}**."
    )
    return {
        "id": f"ns7_var_32_{rng.randint(100000, 999999)}",
        "subskill": "32_pesticide_resistance_in_crop_pests",
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
            "tier_1": "Did the chemical cause the insects to become immune intentionally, or did resistant ones survive?",
            "tier_2": "Resistant individuals already existed by chance and survived to produce the next generations.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["pesticide_resistance_misconception"],
    }


# 33. Predation pressure driving cryptic camouflage
def arch_33_predation_pressure_driving_cryptic_camouflage(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("Namaqua dwarf adder (Bitis schneideri)", "pale coastal sand dunes of the Northern Cape", "sandy speckled grey and brown scales"),
        ("stick insect (Phasmatodea)", "fynbos shrub branches in the Western Cape", "slender elongated green and brown twig-like body"),
        ("chameleon (Bradypodion pumilum)", "dense green foliage of indigenous gardens", "foliage-matching green skin patterns"),
    ]
    animal, habitat, trait = rng.choice(examples)
    prompt = (
        f"The {animal} inhabits {habitat}. Individuals display {trait} that makes them difficult to distinguish from their background.\n\n"
        f"How does natural selection drive the evolution of such cryptic camouflage over generations?"
    )
    correct = (
        "Individuals whose variations matched their surroundings were less visible to predators, survived longer, "
        "and produced more offspring inheriting those camouflage traits."
    )
    options = [
        correct,
        "Individual animals consciously painted their bodies using mud and sap whenever danger approached.",
        "Predators advised the prey on what skin colours were most fashionable for the upcoming season.",
        "Camouflage is caused entirely by non-living minerals seeping into living tissue without any genetics.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze predation pressure as a selective agent:\n"
        f"- Visual predators actively hunt and kill prey individuals that stand out from the background.\n"
        f"- Individuals with {trait} evade detection, survive to reproductive age, and pass their alleles on.\n"
        f"- Over many generations, cryptic camouflage traits become widespread across the population.\n\n"
        f"**Step 2:** The mechanism is: **{correct}**."
    )
    return {
        "id": f"ns7_var_33_{rng.randint(100000, 999999)}",
        "subskill": "33_predation_pressure_driving_cryptic_camouflage",
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
            "tier_1": "Which prey animals get eaten first by hunting birds or carnivores?",
            "tier_2": "Those that do not blend in get eaten; camouflaged variants survive to reproduce.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["predation_camouflage_misconception"],
    }


# 34. Sexual selection display variation peacock
def arch_34_sexual_selection_display_variation_peacock(rng: random.Random) -> Dict[str, Any]:
    birds = [
        ("male Indian peacock (Pavo cristatus)", "an elaborate, iridescent train with multiple vibrant eye-spots", "peahen (female) choosing mates with the most symmetrical, colourful trains"),
        ("Southern red bishop bird (Euplectes orix)", "vivid scarlet-and-black breeding plumage and puffed display flight", "female bishop bird inspecting territory quality and male plumage vibrancy"),
        ("Cape sugarbird (Promerops cafer)", "extremely elongated tail feathers (up to 30 cm) used in aerial courtship displays", "female sugarbird selecting males exhibiting vigorous flight with long tails"),
    ]
    species, male_display, female_choice = rng.choice(birds)
    prompt = (
        f"In the {species}, males exhibit {male_display}. Courtship observation reveals {female_choice}.\n\n"
        f"What form of natural selection is operating when female mate preference drives the evolution of exaggerated male physical traits?"
    )
    correct = "Sexual selection (intersexual selection / mate choice)"
    options = [
        correct,
        "Artificial selection by veterinary farmers",
        "Cellular respiration during anaerobic fermentation",
        "Geological plate tectonic continental drift",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define sexual selection:\n"
        f"- Sexual selection is a mode of natural selection where individuals of one sex (often females) preferentially choose mates of the other sex based on specific phenotypic display traits.\n"
        f"- Males with more pronounced displays have higher reproductive success, passing those alleles to sons.\n\n"
        f"**Step 2:** The term is: **{correct}**."
    )
    return {
        "id": f"ns7_var_34_{rng.randint(100000, 999999)}",
        "subskill": "34_sexual_selection_display_variation_peacock",
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
            "tier_1": "Which term describes selection based on mate attraction and reproductive competition?",
            "tier_2": "Selection driven by female mate choice is known as sexual selection.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["sexual_selection_concept_misconception"],
    }


# 35. Drought resistance variation in wild acacias
def arch_35_drought_resistance_variation_in_wild_acacias(rng: random.Random) -> Dict[str, Any]:
    acacia = rng.choice([
        ("sweet thorn (Vachellia karroo)", "arid savannahs of the Karoo and Kalahari"),
        ("umbrella thorn (Vachellia tortilis)", "hot dry mopane woodlands of Limpopo"),
        ("camel thorn (Vachellia erioloba)", "deep red sands of the Kalahari desert"),
    ])
    depth = rng.randint(25, 45)
    prompt = (
        f"The {acacia[0]} thrives in the {acacia[1]}. In a wild population, some individual saplings "
        f"develop taproots reaching {depth} metres into deep underground water tables, while others possess shallower root systems.\n\n"
        f"During prolonged multi-year droughts, what will happen to the genetic composition of this tree population over generations?"
    )
    correct = (
        f"Saplings with deep taproot alleles will survive the drought, reproduce, and increase the frequency of "
        f"deep-root alleles in subsequent generations."
    )
    options = [
        correct,
        "All trees will shed their bark and walk to the ocean to absorb salt water.",
        "Deep-rooted trees will immediately die because underground water is poisonous to plants.",
        "The trees will alter their DNA within 5 minutes to become floating water lilies.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze drought as an environmental filter:\n"
        f"- In arid habitats, surface water vanishes during extended droughts.\n"
        f"- Only trees capable of tapping deep groundwater aquifers ({depth} m taproots) survive desiccating conditions.\n"
        f"- Survivors flower, set seed pods, and pass on the alleles responsible for rapid deep root elongation.\n\n"
        f"**Step 2:** The result is: **{correct}**."
    )
    return {
        "id": f"ns7_var_35_{rng.randint(100000, 999999)}",
        "subskill": "35_drought_resistance_variation_in_wild_acacias",
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
            "tier_1": "Which trees survive when rain does not fall for years?",
            "tier_2": "Deep-rooted trees survive, reproduce, and pass on their deep-root genes.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["plant_drought_adaptation_misconception"],
    }


# 36. Disease resistance variation in indigenous crops
def arch_36_disease_resistance_variation_in_indigenous_crops(rng: random.Random) -> Dict[str, Any]:
    crops = [
        ("Sorghum bicolor (grain sorghum)", "leaf blight fungus (Exserohilum turcicum)"),
        ("Vigna unguiculata (cowpea)", "bacterial blight (Xanthomonas axonopodis)"),
        ("Pennisetum glaucum (pearl millet)", "downy mildew pathogen (Sclerospora graminicola)"),
    ]
    crop, pathogen = rng.choice(crops)
    prompt = (
        f"Traditional subsistence smallholders in southern Africa cultivate diverse landraces of {crop}. "
        f"When an outbreak of {pathogen} strikes, some individual plants show severe lesions while others remain healthy and productive.\n\n"
        f"Why is genetic diversity within indigenous landrace crops a valuable safeguard against agricultural catastrophe?"
    )
    correct = (
        "Genetic diversity ensures that some plants carry innate disease resistance genes, preventing total crop failure "
        "and providing breeding material for future resilient harvests."
    )
    options = [
        correct,
        "Genetic diversity causes all plants to ripen on the exact same second so pathogens cannot land.",
        "Diverse plants emit sound waves that scare insects and fungi away completely.",
        "Genetic diversity forces farmers to abandon agriculture and rely solely on mining.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the security value of genetic diversity in crops:\n"
        f"- Monoculture fields of genetically uniform clones can suffer 100% loss during an epidemic.\n"
        f"- Traditional landraces of {crop} contain wide genetic variation; plants carrying resistance genes against {pathogen} survive.\n"
        f"- This biological diversity protects rural food security.\n\n"
        f"**Step 2:** The justification is: **{correct}**."
    )
    return {
        "id": f"ns7_var_36_{rng.randint(100000, 999999)}",
        "subskill": "36_disease_resistance_variation_in_indigenous_crops",
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
            "tier_1": "What happens to a field where all plants are identical clones when a disease strikes?",
            "tier_2": "Genetic diversity ensures some resistant plants survive, preventing total starvation.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["crop_diversity_food_security_misconception"],
    }


# 37. Sickle cell trait and malaria resistance in Africa
def arch_37_sickle_cell_trait_and_malaria_resistance_in_africa(rng: random.Random) -> Dict[str, Any]:
    genotypes = [
        ("HbA/HbS (heterozygous sickle cell trait carrier)", "substantial natural protection against lethal cerebral malaria caused by Plasmodium falciparum"),
        ("HbA/HbA (homozygous normal haemoglobin)", "fully susceptible to severe and fatal complications of Plasmodium malaria"),
        ("HbS/HbS (homozygous sickle cell disease)", "severe chronic anaemia and vaso-occlusive crises"),
    ]
    target_geno, consequence = genotypes[0]
    prompt = (
        f"In equatorial and sub-Saharan Africa where malaria is endemic, individuals with the genotype {target_geno} experience {consequence}.\n\n"
        f"Why has the sickle cell allele remained at relatively high frequencies in these populations despite causing severe sickle cell anaemia in homozygous (HbS/HbS) individuals?"
    )
    correct = (
        "Heterozygote advantage: carriers (HbA/HbS) survive malaria at much higher rates than homozygous normal individuals, "
        "allowing the sickle allele to be maintained in the gene pool by natural selection."
    )
    options = [
        correct,
        "Because mosquitoes selectively sting only individuals without any haemoglobin at all.",
        "Because the sickle allele magically cures all bacterial and viral diseases known to medical science.",
        "Because the allele was introduced by modern synthetic pharmaceutical laboratories in 2010.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand heterozygote advantage (balancing selection):\n"
        f"- Homozygous normal (HbA/HbA) individuals often die of severe malaria in endemic zones.\n"
        f"- Homozygous mutated (HbS/HbS) individuals suffer from severe sickle cell disease.\n"
        f"- Heterozygous carriers (HbA/HbS) survive both conditions: their red blood cells inhibit malaria parasite proliferation without causing fatal sickling.\n"
        f"- This survival advantage keeps the allele present in malaria-prone regions.\n\n"
        f"**Step 2:** The reason is: **{correct}**."
    )
    return {
        "id": f"ns7_var_37_{rng.randint(100000, 999999)}",
        "subskill": "37_sickle_cell_trait_and_malaria_resistance_in_africa",
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
            "tier_1": "What disease does the sickle cell trait provide protection against?",
            "tier_2": "Carriers have resistance against malaria, so natural selection maintains the gene.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["sickle_cell_malaria_misconception"],
    }


# 38. Human skin pigmentation clinal variation UV
def arch_38_human_skin_pigmentation_clinal_variation_uv(rng: random.Random) -> Dict[str, Any]:
    regions = [
        ("high equatorial solar radiation zones (e.g. tropical Africa)", "high melanin pigmentation (dark skin)", "protects circulating blood folate from photodegradation and prevents harmful sunburn and skin carcinomas"),
        ("low UV northern latitude regions (e.g. northern Eurasia)", "lower melanin pigmentation (fair skin)", "maximises UV-B penetration into the dermis to synthesise essential Vitamin D for healthy bone growth"),
    ]
    region, adaptation, reason = rng.choice(regions)
    prompt = (
        f"Human populations around the world exhibit a geographic cline in skin pigmentation. In {region}, "
        f"populations historically evolved {adaptation} because it {reason}.\n\n"
        f"What does this evolutionary adaptation illustrate about human variation?"
    )
    correct = (
        "Human skin colour is an adaptive trait driven by natural selection balancing protection against UV folate damage "
        "with the need for Vitamin D synthesis."
    )
    options = [
        correct,
        "Skin colour represents distinct, unrelated biological species created independently.",
        "Skin pigmentation changes completely whenever an individual eats citrus fruit.",
        "Human skin pigmentation is entirely determined by the language a person speaks.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the evolutionary trade-off in skin colour:\n"
        f"- High UV near the equator: dark skin rich in eumelanin shields folate from photolysis and guards against UV cellular damage.\n"
        f"- Low UV far from the equator: light skin allows scarce UV-B rays to penetrate and catalyse Vitamin D synthesis, preventing rickets.\n"
        f"- Human variation in pigmentation is continuous and adaptive, not discrete or racial species boundaries.\n\n"
        f"**Step 2:** The conclusion is: **{correct}**."
    )
    return {
        "id": f"ns7_var_38_{rng.randint(100000, 999999)}",
        "subskill": "38_human_skin_pigmentation_clinal_variation_uv",
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
            "tier_1": "What essential vitamin requires sunlight, and what nutrient is broken down by strong UV?",
            "tier_2": "Melanin balances protection of folate with synthesis of Vitamin D.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["skin_pigmentation_adaptation_misconception"],
    }


# 39. Lactose tolerance variation pastoral populations
def arch_39_lactose_tolerance_variation_pastoral_populations(rng: random.Random) -> Dict[str, Any]:
    groups = [
        ("traditional Maasai and Fulani cattle pastoralist communities in Africa", "high levels of adult lactase persistence enabling consumption of fresh bovine milk"),
        ("historical agricultural societies without domestic dairy animals", "typical mammalian lactase non-persistence (adult lactose intolerance) after weaning"),
    ]
    chosen_group, trait = rng.choice(groups)
    prompt = (
        f"Across human populations, the ability to digest lactose (the sugar in milk) into adulthood varies dramatically. "
        f"For example, {chosen_group} exhibit {trait}.\n\n"
        f"What cultural and evolutionary process caused lactase persistence alleles to rise to high frequencies in certain human populations?"
    )
    correct = "Gene-culture co-evolution: cattle domestication created a rich nutritional food source, granting a strong survival advantage to adults carrying lactase persistence mutations."
    options = [
        correct,
        "Cows injected human infants with lactase enzymes using their horns.",
        "Adults forced their stomachs to grow new organs through mental meditation.",
        "Lactose intolerance was created by modern supermarkets to sell soy milk.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand gene-culture co-evolution:\n"
        f"- Most adult mammals stop producing the enzyme lactase after infancy.\n"
        f"- When human societies domesticated dairy livestock (cattle, goats, camels), milk became a reliable source of protein, fat, and uncontaminated water.\n"
        f"- Individuals with genetic mutations that kept the lactase gene turned on (lactase persistence) survived droughts and famines better, passing this allele to their descendants.\n\n"
        f"**Step 2:** The mechanism is: **{correct}**."
    )
    return {
        "id": f"ns7_var_39_{rng.randint(100000, 999999)}",
        "subskill": "39_lactose_tolerance_variation_pastoral_populations",
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
            "tier_1": "How did farming and herding cattle change human diet and natural selection?",
            "tier_2": "Cattle herding provided milk, giving lactase-persistent individuals a survival advantage.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["lactase_persistence_evolution_misconception"],
    }


# 40. Genetic mutation as ultimate source of new variation
def arch_40_genetic_mutation_as_ultimate_source_of_new_variation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In any biological species, sexual reproduction reshuffles existing alleles, but what is the "
        f"ultimate, primary source of completely novel genetic alleles and variations in living organisms?"
    )
    correct = "Random genetic mutations (spontaneous alterations in DNA nucleotide sequences)"
    options = [
        correct,
        "Extensive physical exercise and healthy nutrition during adult life",
        "The gravitational pull of distant planets during meiosis",
        "Direct conscious decision-making by parent organisms before mating",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify the origin of new genetic information:\n"
        f"- Crossing over and independent assortment only reshuffle existing alleles.\n"
        f"- Completely new alleles arise solely through spontaneous mutations (errors in DNA replication, mutagenic radiation, or chemical damage).\n"
        f"- Without mutations, there would be no new genetic variation for natural selection to act upon.\n\n"
        f"**Step 2:** The ultimate source is: **{correct}**."
    )
    return {
        "id": f"ns7_var_40_{rng.randint(100000, 999999)}",
        "subskill": "40_genetic_mutation_as_ultimate_source_of_new_variation",
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
            "tier_1": "What process changes the base letters of DNA to create a new gene variant?",
            "tier_2": "Spontaneous DNA mutations are the only source of brand new alleles.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["mutation_source_variation_misconception"],
    }


# 41. Meiosis and crossing over generating variation
def arch_41_meiosis_and_crossing_over_generating_variation(rng: random.Random) -> Dict[str, Any]:
    mechanisms = [
        ("Crossing over (chiasmata formation)", "homologous chromosomes exchange reciprocal segments of non-sister chromatids during prophase I"),
        ("Independent assortment", "homologous chromosome pairs align randomly at the metaphase plate in metaphase I"),
        ("Random fertilisation", "any one of millions of genetically unique sperm cells can fuse with a genetically unique ovum"),
    ]
    mech, description = rng.choice(mechanisms)
    prompt = (
        f"During sexual reproduction, genetic diversity is generated through several cellular processes. "
        f"In one such process, {description}.\n\n"
        f"What is this specific cellular mechanism called?"
    )
    correct = mech
    options = [
        correct,
        "Mitotic cytokinesis creating identical clone cells",
        "Anaerobic alcoholic fermentation in yeast vacuoles",
        "Sedimentary fossilisation under high pressure",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recall the mechanisms of meiotic variation:\n"
        f"- 1. Crossing over: exchange of genetic material between homologous chromosomes in prophase I.\n"
        f"- 2. Independent assortment: random orientation and segregation of maternal and paternal chromosomes in metaphase I/anaphase I.\n"
        f"- 3. Random fertilisation: random combination of diverse gametes.\n\n"
        f"**Step 2:** The mechanism described is: **{correct}**."
    )
    return {
        "id": f"ns7_var_41_{rng.randint(100000, 999999)}",
        "subskill": "41_meiosis_and_crossing_over_generating_variation",
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
            "tier_1": "Read the description carefully: homologous chromosomes exchange segments.",
            "tier_2": "Exchange of chromosome parts during prophase I is called crossing over.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["meiosis_variation_mechanism_misconception"],
    }


# 42. Identical twins vs fraternal twins variation
def arch_42_identical_twins_vs_fraternal_twins_variation(rng: random.Random) -> Dict[str, Any]:
    twin_types = [
        ("Identical (monozygotic) twins", "develop from a single fertilized zygote that splits into two embryos", "100% of their nuclear DNA", "environmental factors (e.g. nutrition, lifestyle, sun exposure, epigenetic marks)"),
        ("Fraternal (dizygotic) twins", "develop from two separate ova fertilized by two different sperm cells", "approximately 50% of their DNA (the same as normal full siblings)", "both genetic differences and environmental influences"),
    ]
    twin_name, origin, shared_dna, cause_diff = rng.choice(twin_types)
    prompt = (
        f"{twin_name} {origin}, sharing {shared_dna}. "
        f"Despite this, when observed as teenagers, they display subtle differences in body weight, personality, and athletic stamina.\n\n"
        f"What is the primary cause of phenotypic differences between individuals in this twin pair?"
    )
    correct = cause_diff
    options = [
        correct,
        "One twin was born from a reptile egg while the other was a mammal embryo.",
        "Zero environmental factors can ever affect human physical appearance.",
        "Their DNA is constantly replaced by the school teachers they interact with.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand twin biology and phenotypic variation:\n"
        f"- Monozygotic twins share identical genotypes; any observed differences are strictly environmental.\n"
        f"- Dizygotic twins are genetically as distinct as ordinary brothers and sisters (sharing ~50% alleles).\n\n"
        f"**Step 2:** The primary cause of variation here is: **{correct}**."
    )
    return {
        "id": f"ns7_var_42_{rng.randint(100000, 999999)}",
        "subskill": "42_identical_twins_vs_fraternal_twins_variation",
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
            "tier_1": "If identical twins have the exact same genes, why do they look slightly different?",
            "tier_2": "Environmental factors like diet, exercise, and sun exposure create phenotypic differences.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["twin_genetics_environment_misconception"],
    }


# 43. Selective breeding artificial selection in crops
def arch_43_selective_breeding_artificial_selection_in_crops(rng: random.Random) -> Dict[str, Any]:
    ancestor = "wild mustard (Brassica oleracea)"
    cultivars = [
        ("cabbage", "enlarged terminal leaf buds"),
        ("broccoli", "condensed flower buds and thick fleshy stems"),
        ("cauliflower", "dense sterile white flower clusters"),
        ("kale", "enlarged, ruffled vegetative leaves"),
        ("kohlrabi", "swollen bulb-like edible stem base"),
    ]
    cultivar, trait = rng.choice(cultivars)
    prompt = (
        f"The common vegetable **{cultivar}** was created by agriculturalists repeatedly choosing and propagating "
        f"plants of the ancestral species *{ancestor}* that naturally exhibited {trait}.\n\n"
        f"What term describes the process where humans deliberately choose which organisms breed based on desirable traits?"
    )
    correct = "Artificial selection (selective breeding)"
    options = [
        correct,
        "Natural selection by wild jungle predators",
        "Spontaneous radioactive nuclear decay",
        "Cellular osmosis across semi-permeable membranes",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define artificial selection:\n"
        f"- Artificial selection (selective breeding) is the human-directed process of breeding organisms with specific desired characteristics over successive generations.\n"
        f"- All diverse cultivars of *Brassica oleracea* (cabbage, broccoli, kale, etc.) originated from wild mustard through human selection for different parts of the plant.\n\n"
        f"**Step 2:** The term is: **{correct}**."
    )
    return {
        "id": f"ns7_var_43_{rng.randint(100000, 999999)}",
        "subskill": "43_selective_breeding_artificial_selection_in_crops",
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
            "tier_1": "Who does the selecting in artificial selection: nature or humans?",
            "tier_2": "When humans choose desirable traits to breed, it is called artificial selection or selective breeding.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["artificial_selection_concept_misconception"],
    }


# 44. Selective breeding artificial selection in animals
def arch_44_selective_breeding_artificial_selection_in_animals(rng: random.Random) -> Dict[str, Any]:
    breeds = [
        ("Nguni cattle", "indigenous South African pastoralists selecting for tick resistance, disease tolerance, and mottled hide camouflage against predators"),
        ("Merino sheep", "commercial livestock farmers selecting for exceptionally fine, dense, crimped wool production"),
        ("Boer goats", "commercial goat breeders selecting for rapid growth rates, heavy muscling, and high meat yield in dry bushveld conditions"),
        ("Border Collie dogs", "herders selectively breeding working canines for acute intelligence, obedience, and herd-controlling eye-stalking behaviour"),
    ]
    breed, criteria = rng.choice(breeds)
    prompt = (
        f"The **{breed}** was developed through generations of human breeders {criteria}.\n\n"
        f"How does artificial selection differ primarily from natural selection?"
    )
    correct = (
        "In artificial selection, humans decide which traits are desirable and control mating, whereas in natural selection, "
        "environmental pressures determine which individuals survive and reproduce."
    )
    options = [
        correct,
        "Artificial selection produces wild organisms, while natural selection produces only plastic toys.",
        "Artificial selection takes billions of years, while natural selection occurs in 20 minutes.",
        "Natural selection involves farmers injecting hormones, while artificial selection has no genetics.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare artificial vs natural selection:\n"
        f"- Natural selection: nature (climate, predators, disease) acts as the selective filter; traits that increase fitness in the wild survive.\n"
        f"- Artificial selection: human breeders choose traits that serve human utility, aesthetics, or agricultural profit (such as in the breeding of {breed}).\n\n"
        f"**Step 2:** The fundamental distinction is: **{correct}**."
    )
    return {
        "id": f"ns7_var_44_{rng.randint(100000, 999999)}",
        "subskill": "44_selective_breeding_artificial_selection_in_animals",
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
            "tier_1": "Who decides which individuals reproduce in artificial selection?",
            "tier_2": "Humans select traits in artificial selection, whereas the environment selects in natural selection.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["artificial_vs_natural_selection_misconception"],
    }


# 45. Biodiversity loss through artificial monocultures
def arch_45_biodiversity_loss_through_artificial_monocultures(rng: random.Random) -> Dict[str, Any]:
    historical_events = [
        ("the Great Irish Potato Famine (1845-1852)", "millions of acres were planted with a single clone cultivar (the 'Lumper' potato)", "the water mould Phytophthora infestans arrived and destroyed the entire genetically identical harvest"),
        ("the Southern Corn Leaf Blight epidemic of 1970", "over 85% of US maize fields shared a single cytoplasm gene (Texas-male-sterile)", "the fungus Bipolaris maydis swept through causing billions in catastrophic harvest losses"),
        ("the Cavendish banana monoculture threat", "global commercial banana exports rely almost 100% on genetically identical Cavendish clones", "Tropical Race 4 (TR4) Fusarium wilt is wiping out plantations unable to resist the fungus"),
    ]
    event, cause, outcome = rng.choice(historical_events)
    prompt = (
        f"During {event}, {cause}. As a consequence, {outcome}.\n\n"
        f"What major ecological vulnerability of agricultural monocultures and intensive selective breeding does this disaster demonstrate?"
    )
    correct = (
        "Lack of genetic variation means every single individual is equally susceptible to a virulent pathogen, "
        "enabling a single disease to eradicate the entire crop population."
    )
    options = [
        correct,
        "Monocultures attract space aliens that extract soil moisture using giant suction pumps.",
        "Genetically uniform crops always turn into carnivorous wild weeds within 3 months.",
        "High biodiversity causes crops to catch fire spontaneously when exposed to morning sun.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the danger of genetic uniformity:\n"
        f"- In nature, genetic variation ensures some individuals possess resistance.\n"
        f"- In a clonal or highly inbred monoculture (as in {event}), all plants have identical weaknesses.\n"
        f"- If a pathogen can infect one plant, it can infect and destroy 100% of the population.\n\n"
        f"**Step 2:** The core vulnerability is: **{correct}**."
    )
    return {
        "id": f"ns7_var_45_{rng.randint(100000, 999999)}",
        "subskill": "45_biodiversity_loss_through_artificial_monocultures",
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
            "tier_1": "What happens when all plants in a field are genetically identical and a deadly disease arrives?",
            "tier_2": "Because there is zero variation, none have resistance and all die.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["monoculture_vulnerability_misconception"],
    }


# 46. Frequency distribution histogram interpretation (with dynamic SVG)
def arch_46_frequency_distribution_histogram_interpretation(rng: random.Random) -> Dict[str, Any]:
    # Dynamic values for bins
    b1 = rng.randint(2, 5)
    b2 = rng.randint(9, 14)
    b3 = rng.randint(22, 28)  # Modal class
    b4 = rng.randint(10, 15)
    b5 = rng.randint(3, 6)
    total_learners = b1 + b2 + b3 + b4 + b5
    bar_color = rng.choice(["#3b82f6", "#0ea5e9", "#2563eb", "#6366f1"])

    # Max bar height is 120 px for count ~30
    h1 = int(b1 * 3.8)
    h2 = int(b2 * 3.8)
    h3 = int(b3 * 3.8)
    h4 = int(b4 * 3.8)
    h5 = int(b5 * 3.8)

    svg = (
        f'<svg viewBox="0 0 450 250" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="225" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Learner Height Distribution (N = {total_learners})</text>'
        f'<line x1="60" y1="200" x2="410" y2="200" stroke="#64748b" stroke-width="2" />'
        f'<line x1="60" y1="200" x2="60" y2="40" stroke="#64748b" stroke-width="2" />'
        f'<rect x="70" y="{200 - h1}" width="60" height="{h1}" fill="{bar_color}" stroke="#1e3a8a" />'
        f'<text x="100" y="{190 - h1}" font-size="11" fill="#1e293b" font-weight="bold" text-anchor="middle">{b1}</text>'
        f'<rect x="135" y="{200 - h2}" width="60" height="{h2}" fill="{bar_color}" stroke="#1e3a8a" />'
        f'<text x="165" y="{190 - h2}" font-size="11" fill="#1e293b" font-weight="bold" text-anchor="middle">{b2}</text>'
        f'<rect x="200" y="{200 - h3}" width="60" height="{h3}" fill="#ef4444" stroke="#991b1b" />'
        f'<text x="230" y="{190 - h3}" font-size="11" fill="#991b1b" font-weight="bold" text-anchor="middle">{b3}</text>'
        f'<rect x="265" y="{200 - h4}" width="60" height="{h4}" fill="{bar_color}" stroke="#1e3a8a" />'
        f'<text x="295" y="{190 - h4}" font-size="11" fill="#1e293b" font-weight="bold" text-anchor="middle">{b4}</text>'
        f'<rect x="330" y="{200 - h5}" width="60" height="{h5}" fill="{bar_color}" stroke="#1e3a8a" />'
        f'<text x="360" y="{190 - h5}" font-size="11" fill="#1e293b" font-weight="bold" text-anchor="middle">{b5}</text>'
        f'<text x="100" y="218" font-size="9" fill="#475569" text-anchor="middle">130-139</text>'
        f'<text x="165" y="218" font-size="9" fill="#475569" text-anchor="middle">140-149</text>'
        f'<text x="230" y="218" font-size="9" fill="#475569" font-weight="bold" text-anchor="middle">150-159</text>'
        f'<text x="295" y="218" font-size="9" fill="#475569" text-anchor="middle">160-169</text>'
        f'<text x="360" y="218" font-size="9" fill="#475569" text-anchor="middle">170-179</text>'
        f'<text x="230" y="240" font-size="11" fill="#334155" text-anchor="middle">Height Intervals (cm)</text>'
        f'<text x="25" y="125" font-size="11" fill="#334155" transform="rotate(-90 25,125)" text-anchor="middle">Number of Learners</text>'
        f'</svg>'
    )

    prompt = (
        f"A Grade 7 science class collected height data for {total_learners} learners and plotted the frequencies "
        f"across five height intervals (130-139 cm: {b1}, 140-149 cm: {b2}, 150-159 cm: {b3}, 160-169 cm: {b4}, 170-179 cm: {b5}).\n\n"
        f"What is the modal class (the most frequent category of variation) in this dataset, and how many learners fall into it?"
    )
    correct = f"Modal class: 150-159 cm, with {b3} learners"
    options = [
        correct,
        f"Modal class: 130-139 cm, with {b1} learners",
        f"Modal class: 170-179 cm, with {b5} learners",
        f"Modal class: 140-149 cm, with {b4} learners",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define modal class in frequency data:\n"
        f"- The mode is the category with the highest frequency.\n"
        f"- Comparing the intervals:\n"
        f"  - 130-139 cm: {b1}\n"
        f"  - 140-149 cm: {b2}\n"
        f"  - 150-159 cm: **{b3}** (highest frequency bar)\n"
        f"  - 160-169 cm: {b4}\n"
        f"  - 170-179 cm: {b5}\n\n"
        f"**Step 2:** The modal class is **150-159 cm** containing **{b3}** learners."
    )
    return {
        "id": f"ns7_var_46_{rng.randint(100000, 999999)}",
        "subskill": "46_frequency_distribution_histogram_interpretation",
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
            "tier_1": "Which bar is the tallest in the frequency distribution?",
            "tier_2": "The tallest bar corresponds to 150-159 cm.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["histogram_interpretation_misconception"],
    }


# 47. Normal distribution bell curve properties
def arch_47_normal_distribution_bell_curve_properties(rng: random.Random) -> Dict[str, Any]:
    traits = [
        ("human adult height in a large city population", "continuous polygenic variation"),
        ("birth weights of newborn infants in South African hospitals", "stabilising natural selection"),
        ("mature leaf lengths of Podocarpus falcatus trees in a forest", "multifactorial genetic and environmental inputs"),
    ]
    trait, reason = rng.choice(traits)
    prompt = (
        f"When {trait} ({reason}) is plotted as a large-scale frequency polygon, it forms a symmetrical, "
        f"bell-shaped curve known as a normal distribution.\n\n"
        f"What is a defining mathematical and biological characteristic of a pure normal distribution?"
    )
    correct = (
        "The majority of individuals cluster closely around the central average (mean, median, and mode coincide), "
        "with frequencies tapering symmetrically towards the rare extreme values at both ends."
    )
    options = [
        correct,
        "Every single measurement in the entire population has the exact same frequency with zero average.",
        "There are zero individuals in the middle, and 100% of individuals are located at the extreme ends.",
        "The curve forms a jagged zig-zag shape with alternating vertical spikes.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the properties of a normal distribution bell curve:\n"
        f"- Polygenic traits governed by multiple additive genes plus environmental factors form a continuous bell-shaped distribution.\n"
        f"- Most individuals have intermediate values near the population mean.\n"
        f"- Extreme phenotypes (e.g. exceptionally short or exceptionally tall) are rare, tapering evenly on both tails.\n\n"
        f"**Step 2:** The defining property is: **{correct}**."
    )
    return {
        "id": f"ns7_var_47_{rng.randint(100000, 999999)}",
        "subskill": "47_normal_distribution_bell_curve_properties",
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
            "tier_1": "Where do most individuals lie on a normal bell curve: in the middle or at the extremes?",
            "tier_2": "Most individuals cluster around the central mean, with few at the extreme tails.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["normal_distribution_properties_misconception"],
    }


# 48. Distinguishing species variation vs inter-species differences
def arch_48_distinguishing_species_variation_vs_inter_species_differences(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("A comparison between a Great Dane dog and a tiny Chihuahua", "Intraspecific variation (variation within the single species Canis lupus familiaris)", "both can interbreed to produce fertile offspring"),
        ("A comparison between a lion (Panthera leo) and a leopard (Panthera pardus)", "Interspecific difference (differences between two separate distinct species)", "they cannot interbreed in nature to produce fertile offspring"),
        ("A comparison between an African elephant (Loxodonta africana) and an Asian elephant (Elephas maximus)", "Interspecific difference (differences between two separate biological species)", "they belong to different biological species and genera"),
        ("A comparison between a blue-eyed human and a brown-eyed human", "Intraspecific variation (variation within the single species Homo sapiens)", "both belong to the same species and can reproduce fertile offspring"),
    ]
    pair, classification, reason = rng.choice(scenarios)
    prompt = (
        f"Consider the following biological comparison: {pair}.\n\n"
        f"How is this comparison scientifically classified, and what is the biological justification?"
    )
    correct = f"{classification}, because {reason}."
    options = [
        correct,
        f"Non-biological mineral variation, because neither possesses living cells or nucleic acids.",
        f"Asexual bacterial budding, because both organisms clone themselves in fresh milk.",
        f"Extinction classification, because both organisms have been completely extinct for 500 million years.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish intraspecific variation from interspecific differences:\n"
        f"- Intraspecific: differences among members of the *same* species (can interbreed freely in nature producing fertile offspring).\n"
        f"- Interspecific: biological differences between *different* distinct species.\n\n"
        f"**Step 2:** Classification: **{correct}**."
    )
    return {
        "id": f"ns7_var_48_{rng.randint(100000, 999999)}",
        "subskill": "48_distinguishing_species_variation_vs_inter_species_differences",
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
            "tier_1": "Do these organisms belong to the same species or two different species?",
            "tier_2": "Check if they can interbreed to produce fertile offspring.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["intra_vs_inter_specific_variation_misconception"],
    }


# 49. Cloning and lack of variation vulnerabilities
def arch_49_cloning_and_lack_of_variation_vulnerabilities(rng: random.Random) -> Dict[str, Any]:
    commercial_plants = [
        ("commercial forestry pine trees (Pinus patula) produced via vegetative cuttings", "Sirex woodwasp and pitch canker fungus"),
        ("sugarcane (Saccharum officinarum) established via stalk setts", "sugarcane smut fungus (Sporisorium scitamineum)"),
        ("commercial apple orchards grafted onto uniform M9 rootstocks", "fire blight bacteria (Erwinia amylovora)"),
    ]
    plant, threat = rng.choice(commercial_plants)
    prompt = (
        f"An agricultural company establishes thousands of hectares of {plant}. All trees are genetic clones. "
        f"A regional outbreak of {threat} begins spreading.\n\n"
        f"What is the main biological danger of relying on cloned crops lacking genetic variation?"
    )
    correct = (
        "Because all individuals share the exact same genetic code, if one individual is susceptible to the disease, "
        "all individuals are susceptible, creating the risk of catastrophic 100% loss."
    )
    options = [
        correct,
        "Cloned crops spontaneously transform into carnivorous predatory animals overnight.",
        "Clones will refuse to photosynthesise because they are angry at the farm manager.",
        "Zero danger exists because clones have impenetrable titanium cell walls.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the biological consequence of zero genetic variation:\n"
        f"- Clones share identical genomes (zero genetic diversity).\n"
        f"- While uniform growth facilitates harvesting, it leaves the population defenseless against novel pathogens.\n"
        f"- If the pathogen {threat} overcomes one clone's immune defenses, every clone is equally vulnerable.\n\n"
        f"**Step 2:** The fundamental hazard is: **{correct}**."
    )
    return {
        "id": f"ns7_var_49_{rng.randint(100000, 999999)}",
        "subskill": "49_cloning_and_lack_of_variation_vulnerabilities",
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
            "tier_1": "If all plants have identical genes, can any of them have a special resistance gene?",
            "tier_2": "No, because there is no variation; if one gets infected, all get infected.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cloning_vulnerability_misconception"],
    }


# 50. Synthetic case study conservation genetics cheetah
def arch_50_synthetic_case_study_conservation_genetics_cheetah(rng: random.Random) -> Dict[str, Any]:
    years_ago = rng.choice(["10 000 to 12 000", "roughly 10 millennia"])
    prompt = (
        f"South African wildlife geneticists studying the cheetah (*Acinonyx jubatus*) found that the species passed through "
        f"a severe population bottleneck approximately {years_ago} years ago at the end of the last Ice Age. "
        f"As a result, modern cheetahs exhibit extraordinarily low genetic variation — skin grafts between unrelated cheetahs are accepted without immune rejection.\n\n"
        f"What serious conservation crisis does this extreme lack of genetic variation create for cheetah populations today?"
    )
    correct = (
        "High vulnerability to fatal epidemics (such as feline infectious peritonitis), reduced reproductive sperm quality, "
        "and inability to adapt to emerging climate and disease pressures."
    )
    options = [
        correct,
        "Cheetahs become herbivorous and spend all their time grazing on indigenous acacia grasses.",
        "Cheetahs grow wings and migrate across oceans to live in polar glaciers.",
        "Cheetahs lose their ability to run because their bones turn into hollow wooden twigs.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze genetic bottlenecks and conservation genetics:\n"
        f"- When a population shrinks to a handful of individuals, inbreeding occurs and genetic diversity collapses.\n"
        f"- Cheetahs lack polymorphic diversity in their Major Histocompatibility Complex (MHC) immune genes.\n"
        f"- A single deadly viral pathogen could wipe out entire reserves because no individuals possess resistant immune alleles.\n\n"
        f"**Step 2:** The conservation crisis is: **{correct}**."
    )
    return {
        "id": f"ns7_var_50_{rng.randint(100000, 999999)}",
        "subskill": "50_synthetic_case_study_conservation_genetics_cheetah",
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
            "tier_1": "What happens to an animal population when immune genes are almost identical across all individuals?",
            "tier_2": "A single disease can kill the entire population, and inbreeding lowers fertility.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["conservation_bottleneck_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "26_survival_value_of_variation_environmental_change": arch_26_survival_value_of_variation_environmental_change,
    "27_natural_selection_concept_and_mechanism": arch_27_natural_selection_concept_and_mechanism,
    "28_peppered_moth_pre_industrial_lichen_camouflage": arch_28_peppered_moth_pre_industrial_lichen_camouflage,
    "29_peppered_moth_industrial_melanism_sooty_bark": arch_29_peppered_moth_industrial_melanism_sooty_bark,
    "30_peppered_moth_clean_air_act_recovery": arch_30_peppered_moth_clean_air_act_recovery,
    "31_antibiotic_resistance_as_natural_selection": arch_31_antibiotic_resistance_as_natural_selection,
    "32_pesticide_resistance_in_crop_pests": arch_32_pesticide_resistance_in_crop_pests,
    "33_predation_pressure_driving_cryptic_camouflage": arch_33_predation_pressure_driving_cryptic_camouflage,
    "34_sexual_selection_display_variation_peacock": arch_34_sexual_selection_display_variation_peacock,
    "35_drought_resistance_variation_in_wild_acacias": arch_35_drought_resistance_variation_in_wild_acacias,
    "36_disease_resistance_variation_in_indigenous_crops": arch_36_disease_resistance_variation_in_indigenous_crops,
    "37_sickle_cell_trait_and_malaria_resistance_in_africa": arch_37_sickle_cell_trait_and_malaria_resistance_in_africa,
    "38_human_skin_pigmentation_clinal_variation_uv": arch_38_human_skin_pigmentation_clinal_variation_uv,
    "39_lactose_tolerance_variation_pastoral_populations": arch_39_lactose_tolerance_variation_pastoral_populations,
    "40_genetic_mutation_as_ultimate_source_of_new_variation": arch_40_genetic_mutation_as_ultimate_source_of_new_variation,
    "41_meiosis_and_crossing_over_generating_variation": arch_41_meiosis_and_crossing_over_generating_variation,
    "42_identical_twins_vs_fraternal_twins_variation": arch_42_identical_twins_vs_fraternal_twins_variation,
    "43_selective_breeding_artificial_selection_in_crops": arch_43_selective_breeding_artificial_selection_in_crops,
    "44_selective_breeding_artificial_selection_in_animals": arch_44_selective_breeding_artificial_selection_in_animals,
    "45_biodiversity_loss_through_artificial_monocultures": arch_45_biodiversity_loss_through_artificial_monocultures,
    "46_frequency_distribution_histogram_interpretation": arch_46_frequency_distribution_histogram_interpretation,
    "47_normal_distribution_bell_curve_properties": arch_47_normal_distribution_bell_curve_properties,
    "48_distinguishing_species_variation_vs_inter_species_differences": arch_48_distinguishing_species_variation_vs_inter_species_differences,
    "49_cloning_and_lack_of_variation_vulnerabilities": arch_49_cloning_and_lack_of_variation_vulnerabilities,
    "50_synthetic_case_study_conservation_genetics_cheetah": arch_50_synthetic_case_study_conservation_genetics_cheetah,
}
