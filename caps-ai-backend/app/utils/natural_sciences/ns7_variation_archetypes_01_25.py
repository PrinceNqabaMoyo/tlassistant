"""Grade 7 Natural Sciences: Term 1 - Variation (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/04. Variation.md.
Focus: Variation Within a Species, Inherited vs Environmental Traits, Continuous vs Discontinuous Variation, and Data Analysis.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Variation within species concept
def arch_01_variation_within_species_concept(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("domestic dogs (Canis lupus familiaris)", "differences in coat colour, hair length, muzzle shape, and body mass despite all belonging to the exact same species"),
        ("human beings (Homo sapiens)", "differences in eye colour, skin pigmentation, natural height, and fingerprint patterns across individuals"),
        ("sunflowers (Helianthus annuus) in a single crop field", "subtle differences in stem height, flower head diameter, and seed oil content among individuals"),
    ]
    species, observation = rng.choice(examples)
    prompt = (
        f"Consider {species}. Individuals display {observation}.\n\n"
        f"What scientific term specifically designates these observable physical differences among individuals belonging to the same species?"
    )
    correct = "Intraspecific variation (variation within a species)"
    options = [
        correct,
        "Extinction of non-living abiotic components",
        "Cellular photosynthesis in mammal kidneys",
        "Geological weathering of sedimentary rocks",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define biological variation within a species:\n"
        f"- Intraspecific variation refers to the natural differences in physical, physiological, or behavioural traits among individuals of the same species.\n"
        f"- It is caused by genetic differences (alleles) and environmental influences.\n\n"
        f"**Step 2:** The term is: **{correct}**."
    )
    return {
        "id": f"ns7_var_01_{rng.randint(100000, 999999)}",
        "subskill": "01_variation_within_species_concept",
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
            "tier_1": "Think about the word 'vary' or 'variation'.",
            "tier_2": "Physical differences between individuals of the same species are called variation.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["variation_definition_confusion"],
    }


# 02. Dog breed morphological variation
def arch_02_dog_breed_morphological_variation(rng: random.Random) -> Dict[str, Any]:
    breeds = [
        ("a Chihuahua (mass ~2 kg) and an English Mastiff (mass ~90 kg)", "size and skeletal proportions"),
        ("a Dachshund (short elongated legs) and a Greyhound (long slender athletic limbs)", "limb anatomy and body conformation"),
        ("a Poodle (tightly curled non-shedding hair) and an Afghan Hound (long silky flowing coat)", "fur texture and hair growth cycle"),
    ]
    comparison, trait_domain = rng.choice(breeds)
    prompt = (
        f"Domestic dogs show extreme variation in {trait_domain}, as seen when comparing {comparison}. "
        f"Despite these vast physical differences, why are all domestic dogs classified as belonging to one single biological species (*Canis lupus familiaris*)?"
    )
    correct = "Because they can freely interbreed with one another and produce fertile, viable offspring."
    options = [
        correct,
        "Because all dog breeds were created in a chemistry laboratory using mineral plastic.",
        "Because dogs do not possess DNA or cellular chromosomes.",
        "Because every dog has the exact identical mass and body length on every continent.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Apply the biological species concept:\n"
        f"- A species is defined by the ability of individuals to interbreed and produce fertile offspring.\n"
        f"- Despite extreme morphological divergence created by artificial selection, a Chihuahua and a Mastiff share the same genome and can produce fertile puppies.\n\n"
        f"**Step 2:** The scientific reason is: **{correct}**."
    )
    return {
        "id": f"ns7_var_02_{rng.randint(100000, 999999)}",
        "subskill": "02_dog_breed_morphological_variation",
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
            "tier_1": "What is the biological definition of a species? The ability to produce fertile babies.",
            "tier_2": "All domestic dogs belong to one species because they can interbreed and produce fertile offspring.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["breed_vs_species_confusion"],
    }


# 03. Cattle breed Nguni coat pattern variation
def arch_03_cattle_breed_nguni_coat_pattern_variation(rng: random.Random) -> Dict[str, Any]:
    patterns = [
        ("Inyoni (white with speckled black or red patches resembling birds)", "cryptic blending against savanna bushveld shadows"),
        ("Inkomo ebomvu (solid dark reddish-brown coat)", "high skin pigmentation protecting against intense African solar UV radiation"),
        ("Ipunga (spotted or dappled like animal hides)", "disrupting body outline to confuse biting tsetse flies and tick parasites"),
    ]
    pattern_name, survival_benefit = rng.choice(patterns)
    prompt = (
        f"South Africa's indigenous Nguni cattle (*Bos taurus africanus*) are famous for their extraordinary coat colour variation and horn shapes. "
        f"In traditional Zulu cattle naming, the pattern '{pattern_name}' is recognized. "
        f"How does natural genetic variation in coat pigmentation benefit Nguni cattle in diverse African veld environments?"
    )
    correct = f"It provides ecological adaptations ({survival_benefit}) and confers resilience against heat stress and parasite burdens across changing climates."
    options = [
        correct,
        "It forces the cattle to turn into marine fish that swim in dry river sand.",
        "It stops the cattle from ever needing to eat grass or drink water.",
        "It proves that Nguni cattle are an extinct species of prehistoric dinosaur.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze variation in indigenous Nguni cattle:\n"
        f"- Nguni cattle have high genetic diversity forged over centuries in southern Africa.\n"
        f"- Coat variations provide thermal protection, camouflage, and resistance to tick-borne diseases.\n\n"
        f"**Step 2:** The benefit is: **{correct}**."
    )
    return {
        "id": f"ns7_var_03_{rng.randint(100000, 999999)}",
        "subskill": "03_cattle_breed_nguni_coat_pattern_variation",
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
            "tier_1": "Think about why indigenous Nguni cattle do so well in the harsh African climate.",
            "tier_2": "Coat variation protects against hot African sun, parasites, and predators.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["indigenous_breed_variation_underestimation"],
    }


# 04. Plant intraspecific variation flower colour
def arch_04_plant_intraspecific_variation_flower_colour(rng: random.Random) -> Dict[str, Any]:
    colours = rng.sample(["vivid red", "pale pink", "pure white", "deep purple"], 2)
    c1, c2 = colours[0], colours[1]
    prompt = (
        f"In a wild population of indigenous sweet peas growing in a nature reserve, some plants produce {c1} flowers "
        f"while other plants of the same species produce {c2} flowers. "
        f"What is the underlying biological cause of this flower colour variation?"
    )
    correct = "Different genetic alleles inherited in the plants' DNA that code for different concentrations and types of floral anthocyanin pigment molecules."
    options = [
        correct,
        "The wind blows paint onto the petals during nighttime rainstorms.",
        "Plants with white flowers have had their DNA completely removed by earthworms.",
        "Flower petals change colour only when animals speak English to them.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the genetic basis of floral color variation:\n"
        f"- Different alleles (gene variants) regulate pigment synthesis enzymes (e.g. anthocyanins, carotenoids).\n"
        f"- Variations in inherited alleles between individuals yield different petal colors ({c1} vs {c2}).\n\n"
        f"**Step 2:** The biological cause is: **{correct}**."
    )
    return {
        "id": f"ns7_var_04_{rng.randint(100000, 999999)}",
        "subskill": "04_plant_intraspecific_variation_flower_colour",
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
            "tier_1": "What controls petal color inside plant cells? Genes and pigments.",
            "tier_2": "Different alleles in DNA produce different flower pigments.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["floral_pigment_genetic_basis"],
    }


# 05. Human physical variation facial features
def arch_05_human_physical_variation_facial_features(rng: random.Random) -> Dict[str, Any]:
    features = [
        ("Attached vs free-hanging earlobes", "whether the lower lobe of the ear hangs freely or is attached directly to the side of the head"),
        ("Widow's peak hairline vs straight hairline", "whether the forehead hairline forms a distinct downward V-shaped point"),
        ("Hitchhiker's thumb vs straight thumb", "whether the distal joint of the thumb can bend backwards beyond 45 degrees"),
        ("Facial dimples vs smooth cheeks", "the presence of small indentations in cheek flesh produced by variations in the zygomaticus major muscle"),
    ]
    feat_name, feat_desc = rng.choice(features)
    prompt = (
        f"In human genetics surveys, learners observe distinct inherited morphological traits. "
        f"Which statement describes the visible variation known as '{feat_name}'?"
    )
    correct = feat_desc
    options = [feat_desc] + [f[1] for f in features if f[1] != feat_desc]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review discrete human morphological variations:\n"
        f"- Free vs attached earlobes: earlobe attachment to head.\n"
        f"- Widow's peak: V-shaped hairline.\n"
        f"- Hitchhiker's thumb: hyperextension of thumb joint.\n"
        f"- Dimples: cheek muscle indentation.\n\n"
        f"**Step 2:** For '{feat_name}', the description is: **{feat_desc}**."
    )
    return {
        "id": f"ns7_var_05_{rng.randint(100000, 999999)}",
        "subskill": "05_human_physical_variation_facial_features",
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
            "tier_1": "Match the named human facial trait to its physical appearance.",
            "tier_2": "Look at whether it describes earlobes, hairlines, thumbs, or cheek dimples.",
            "tier_3": f"The answer is: {feat_desc}.",
        },
        "misconception_tags": ["human_trait_morphology_confusion"],
    }


# 06. Human fingerprint uniqueness variation
def arch_06_human_fingerprint_uniqueness_variation(rng: random.Random) -> Dict[str, Any]:
    patterns = ["loop", "whorl", "arch"]
    pattern = rng.choice(patterns)
    prompt = (
        f"Every human being has a unique set of dermal friction ridges forming fingerprints (with {pattern} patterns). "
        f"Even identical (monozygotic) twins who share 100% of their inherited DNA have different fingerprints. "
        f"Why are fingerprints different even between identical twins?"
    )
    correct = "Because fingerprint ridge patterns are influenced by microscopic environmental variations inside the womb (such as amniotic fluid flow, pressure against the uterine wall, and umbilical cord position) during foetal development."
    options = [
        correct,
        "Because identical twins belong to two completely different mammalian species.",
        "Because fingerprints are drawn by doctors using permanent ink pens immediately after birth.",
        "Because one twin loses all their skin ridges whenever they eat breakfast.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the interplay between genetics and environment in fingerprints:\n"
        f"- General pattern type (loop, whorl, arch) has a genetic basis.\n"
        f"- The fine details of ridge endings and bifurcations (minutiae) are shaped by random physical forces and fluid currents in the amniotic sac between weeks 10 and 24 of gestation.\n"
        f"- Thus, even identical twins have unique fingerprints.\n\n"
        f"**Step 2:** The reason is: **{correct}**."
    )
    return {
        "id": f"ns7_var_06_{rng.randint(100000, 999999)}",
        "subskill": "06_human_fingerprint_uniqueness_variation",
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
            "tier_1": "Identical twins have identical genes, but their fingerprints are still different.",
            "tier_2": "Physical forces and fluid pressures in the womb shape fingerprint details.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["identical_twin_fingerprint_myth"],
    }


# 07. Inherited variation definition and mechanism
def arch_07_inherited_variation_definition_and_mechanism(rng: random.Random) -> Dict[str, Any]:
    traits = [
        ("natural eye colour (e.g. brown vs blue)", "genes located on chromosomes inside the nuclei of gametes (sperm and ovum) passed from parents to child"),
        ("ABO blood type (e.g. type A vs type O)", "inherited alleles encoding specific glycoprotein antigens on the surface of red blood cells"),
        ("cystic fibrosis genetic condition", "mutated CFTR alleles inherited from both biological parents"),
    ]
    trait_name, inheritance_mech = rng.choice(traits)
    prompt = (
        f"What is the definition of **inherited variation**, and how is '{trait_name}' transmitted across generations?"
    )
    correct = f"Differences in characteristics determined by genetic information encoded in DNA; transmitted via {inheritance_mech}."
    distractors = [
        "Characteristics acquired through gym workouts and eating nutritious vegetables during adulthood.",
        "Physical injuries caused by bicycle accidents that are passed on to grandchildren.",
        "Spoken language accents that are copied from watching television programmes.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define inherited variation:\n"
        f"- Determined by genes/DNA inherited from biological parents via sperm and egg.\n"
        f"- Cannot be altered by lifestyle choices or environment (e.g. eye color, blood group).\n\n"
        f"**Step 2:** For '{trait_name}', the definition is: **{correct}**."
    )
    return {
        "id": f"ns7_var_07_{rng.randint(100000, 999999)}",
        "subskill": "07_inherited_variation_definition_and_mechanism",
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
            "tier_1": "Inherited traits come from parents' DNA inside sperm and egg cells.",
            "tier_2": "Eye color and blood groups are inborn genetic traits passed down through genes.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["inherited_trait_transmission_error"],
    }


# 08. Environmental variation definition and causes
def arch_08_environmental_variation_definition_and_causes(rng: random.Random) -> Dict[str, Any]:
    acquired_traits = [
        ("A surgical scar on a person's knee", "physical trauma and wound healing leaving collagen scar tissue that is NOT coded in gamete DNA"),
        ("The ability to speak isiZulu fluently", "cultural learning, language acquisition, and social environment during childhood rather than genetics"),
        ("Hair dyed bright purple with chemical dye", "artificial external chemical pigmentation that does not alter the hair follicle keratin genes"),
        ("Large biceps developed by a weightlifter", "hypertrophy of skeletal muscle fibers through mechanical load training that cannot be passed to offspring"),
    ]
    trait_example, reason = rng.choice(acquired_traits)
    prompt = (
        f"Consider the characteristic: '{trait_example}'. "
        f"Why is this classified as **environmental variation** rather than inherited variation?"
    )
    correct = f"Because it is an acquired characteristic caused by external environmental influences ({reason}), and cannot be passed on to biological offspring."
    options = [
        correct,
        "Because it was written in the person's DNA chromosomes before they were born.",
        "Because any characteristic on a human body is automatically inherited from ancestors.",
        "Because scars and dyed hair are caused by volcanic rock weathering.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define environmental (acquired) variation:\n"
        f"- Caused by conditions in an organism's surroundings (diet, injury, culture, exposure).\n"
        f"- Does NOT alter the DNA in gametes (sperm/egg), so it CANNOT be inherited by children.\n\n"
        f"**Step 2:** '{trait_example}' is environmental because: **{correct}**."
    )
    return {
        "id": f"ns7_var_08_{rng.randint(100000, 999999)}",
        "subskill": "08_environmental_variation_definition_and_causes",
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
            "tier_1": "Ask: If a father gets a scar or dyes his hair purple, will his baby be born with a scar or purple hair? No.",
            "tier_2": "Acquired environmental changes do not alter genes in sex cells.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["lamarckian_inheritance_misconception"],
    }


# 09. Classifying traits inherited vs environmental
def arch_09_classifying_traits_inherited_vs_environmental(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Natural blood group (ABO)", "Inherited strictly from DNA", "A decorative skin tattoo", "Environmental acquired trait"),
        ("Tongue rolling ability", "Inherited strictly from DNA", "A broken leg from a sports injury", "Environmental acquired trait"),
        ("Attached vs free earlobes", "Inherited strictly from DNA", "Speaking fluent English and Sesotho", "Environmental acquired trait"),
    ]
    t1, cat1, t2, cat2 = rng.choice(pairs)
    prompt = (
        f"Classify the following two human traits:\n"
        f"Trait 1: '{t1}'\n"
        f"Trait 2: '{t2}'\n\n"
        f"Which option correctly classifies both characteristics?"
    )
    correct = f"Trait 1 is {cat1}; Trait 2 is {cat2}."
    distractors = [
        f"Trait 1 is {cat2}; Trait 2 is {cat1}.",
        f"Both Trait 1 and Trait 2 are {cat1}.",
        f"Both Trait 1 and Trait 2 are {cat2}.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Evaluate each trait:\n"
        f"- '{t1}': determined by genetics -> {cat1}.\n"
        f"- '{t2}': acquired from environment/lifestyle -> {cat2}.\n\n"
        f"**Step 2:** The correct classification is: **{correct}**."
    )
    return {
        "id": f"ns7_var_09_{rng.randint(100000, 999999)}",
        "subskill": "09_classifying_traits_inherited_vs_environmental",
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
            "tier_1": "Is the trait in your DNA from birth, or did you get it from life experience or an accident?",
            "tier_2": "Blood group and earlobes are genetic; tattoos and broken bones are environmental.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["trait_classification_confusion"],
    }


# 10. Interaction genes and environment height
def arch_10_interaction_genes_and_environment_height(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Human height is known to be shaped by both genetic inheritance and environmental factors. "
        f"If a child inherits tall stature genes from both tall biological parents, but suffers from chronic severe malnutrition and illnesses throughout early childhood, what is the expected outcome for their adult height?"
    )
    correct = "The child will not reach their full genetic potential height and will remain shorter as an adult, because adequate dietary protein, calcium, and calories are required to build bone tissue."
    options = [
        correct,
        "The child will grow to 3 metres tall regardless of having zero food to eat.",
        "The malnutrition will change their DNA into plant genes that photosynthesise height.",
        "Environmental factors have exactly 0% influence on any human biological characteristic.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand gene-environment interaction:\n"
        f"- Genes provide the potential or blueprint (tall stature alleles).\n"
        f"- The environment provides the materials (nutrition, healthcare) needed to realize that potential.\n"
        f"- Severe malnutrition restricts growth, showing that phenotype = genotype + environment.\n\n"
        f"**Step 2:** The outcome is: **{correct}**."
    )
    return {
        "id": f"ns7_var_10_{rng.randint(100000, 999999)}",
        "subskill": "10_interaction_genes_and_environment_height",
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
            "tier_1": "Can a building reach 50 floors without bricks, even if the architect's plan is for 50 floors?",
            "tier_2": "Genes give the height potential, but food and nutrients are needed to build bones.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["genetic_determinism_fallacy"],
    }


# 11. Interaction genes and environment skin tanning
def arch_11_interaction_genes_and_environment_skin_tanning(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A person with fair skin goes on holiday to a sunny Durban beach and develops a deep sun tan after two weeks. "
        f"Which statement scientifically explains how this skin colour change illustrates the interaction between genes and the environment?"
    )
    correct = "The baseline skin tone is determined genetically by melanin-producing genes; in response to environmental UV radiation, skin melanocytes increase melanin production to protect nuclear DNA from radiation damage."
    options = [
        correct,
        "The sun bleached all the person's cells into non-living sand crystals.",
        "The person's genetic chromosomes were completely destroyed and replaced by saltwater.",
        "The tan will automatically be inherited by all children born to this person years later.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze skin tanning as gene-environment interaction:\n"
        f"- Baseline pigmentation = genetically determined.\n"
        f"- UV light (environment) triggers protective melanin synthesis (tanning).\n"
        f"- The acquired tan is an environmental modification, not an alteration of gamete DNA.\n\n"
        f"**Step 2:** The explanation is: **{correct}**."
    )
    return {
        "id": f"ns7_var_11_{rng.randint(100000, 999999)}",
        "subskill": "11_interaction_genes_and_environment_skin_tanning",
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
            "tier_1": "Genes decide baseline skin tone; sunlight stimulates melanin to protect cells.",
            "tier_2": "Sunlight (environment) stimulates genes to produce extra protective melanin pigment.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["tanning_mechanism_misconception"],
    }


# 12. Interaction genes and environment plant growth
def arch_12_interaction_genes_and_environment_plant_growth(rng: random.Random) -> Dict[str, Any]:
    h_fertile = rng.randint(45, 60)
    h_poor = rng.randint(15, 25)
    prompt = (
        f"A gardener takes two stem cuttings from the same single geranium mother plant, meaning both cuttings are genetically identical clones. "
        f"Cutting A is planted in fertile, moist garden loam enriched with compost and grows to {h_fertile} cm. "
        f"Cutting B is planted in dry, barren sand without fertilizer and reaches only {h_poor} cm. "
        f"What does this experiment prove about organism characteristics?"
    )
    correct = "Even when organisms possess identical genetic blueprints, differences in environmental resources (soil nutrients, water) produce dramatic differences in final physical phenotype."
    options = [
        correct,
        "It proves that Cutting B mutated into a different species of desert cactus.",
        "It proves that genetics has zero influence on plant characteristics.",
        "It proves that fertile compost permanently deletes DNA from plant cells.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze clone growth in different environments:\n"
        f"- Genotype of A = Genotype of B (identical cuttings).\n"
        f"- Environment differs (fertile soil vs barren sand).\n"
        f"- Result: Height differs ({h_fertile} cm vs {h_poor} cm).\n\n"
        f"**Step 2:** This proves that: **{correct}**."
    )
    return {
        "id": f"ns7_var_12_{rng.randint(100000, 999999)}",
        "subskill": "12_interaction_genes_and_environment_plant_growth",
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
            "tier_1": "The cuttings have identical genes, but one grew in rich soil and one in poor sand.",
            "tier_2": "Environment causes differences even between identical genetic clones.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["clone_environmental_plasticity"],
    }


# 13. Discontinuous variation definition and traits
def arch_13_discontinuous_variation_definition_and_traits(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In biological genetics, how is **discontinuous (discrete) variation** defined?"
    )
    correct = "Variation that falls into distinct, separate qualitative categories with no intermediate or in-between values, controlled by one or a few genes with minimal environmental influence."
    options = [
        correct,
        "A continuous numerical spectrum of measurements spanning from minimum to maximum without distinct categories.",
        "Physical changes caused exclusively by broken bones and surgical scars.",
        "Characteristics that change every single hour depending on the weather.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define discontinuous variation:\n"
        f"- Distinct categories (e.g. tongue roller vs non-roller; blood type A, B, AB, O).\n"
        f"- No intermediate states.\n"
        f"- Usually controlled by single gene loci (monogenic).\n\n"
        f"**Step 2:** The scientific definition is: **{correct}**."
    )
    return {
        "id": f"ns7_var_13_{rng.randint(100000, 999999)}",
        "subskill": "13_discontinuous_variation_definition_and_traits",
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
            "tier_1": "Think about blood groups: you are either A, B, AB, or O. There is no blood group 2.5.",
            "tier_2": "Discontinuous variation has clear, distinct categories with no in-between spectrum.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["discontinuous_variation_definition_error"],
    }


# 14. Discontinuous variation tongue rolling
def arch_14_discontinuous_variation_tongue_rolling(rng: random.Random) -> Dict[str, Any]:
    n_learners = rng.choice([30, 35, 40])
    rollers = int(n_learners * rng.choice([0.65, 0.70, 0.75]))
    non_rollers = n_learners - rollers
    prompt = (
        f"In a Grade 7 Natural Sciences class of {n_learners} learners, {rollers} can roll their tongues into a U-shape "
        f"while {non_rollers} cannot. "
        f"Why is tongue rolling categorized as an example of **discontinuous variation**?"
    )
    correct = "Because individuals fall strictly into one of two distinct categories (roller or non-roller), with no intermediate partial stages."
    options = [
        correct,
        "Because tongue rolling increases in millimetres continuously as a person grows taller.",
        "Because tongue rolling is an acquired skill that people learn by reading dictionaries.",
        "Because learners who can roll their tongues belong to a different animal phylum.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze tongue rolling variation:\n"
        f"- You either can roll your tongue or you cannot.\n"
        f"- It is a binary, qualitative, discrete trait with no continuous spectrum.\n\n"
        f"**Step 2:** It is discontinuous because: **{correct}**."
    )
    return {
        "id": f"ns7_var_14_{rng.randint(100000, 999999)}",
        "subskill": "14_discontinuous_variation_tongue_rolling",
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
            "tier_1": "Can someone half-roll their tongue on a continuous numerical scale? No, you either roll or you can't.",
            "tier_2": "Clear either/or categories define discontinuous variation.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["tongue_rolling_categorization_error"],
    }


# 15. Discontinuous variation earlobe attachment
def arch_15_discontinuous_variation_earlobe_attachment(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Which of the following human characteristics is another classic example of **discontinuous variation**?"
    )
    correct = "Earlobe attachment (free-hanging earlobes vs attached earlobes)."
    options = [
        correct,
        "Human height measured in millimetres.",
        "Human body mass measured in kilograms.",
        "Hand span measured in centimetres.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Differentiate continuous vs discontinuous examples:\n"
        f"- Continuous: height, body mass, hand span (measurable numerical ranges).\n"
        f"- Discontinuous: earlobe attachment, blood group, tongue rolling (distinct categories).\n\n"
        f"**Step 2:** The discontinuous example is: **{correct}**."
    )
    return {
        "id": f"ns7_var_15_{rng.randint(100000, 999999)}",
        "subskill": "15_discontinuous_variation_earlobe_attachment",
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
            "tier_1": "Look for the trait that has categories rather than a tape-measure number.",
            "tier_2": "Height, mass, and hand span are measured in numbers; earlobes are free or attached.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["discontinuous_trait_identification_confusion"],
    }


# 16. Discontinuous variation ABO blood groups
def arch_16_discontinuous_variation_abo_blood_groups(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Human ABO blood types consist of four distinct groups: Blood Group A, Blood Group B, Blood Group AB, and Blood Group O. "
        f"Why is the ABO blood group system classified as **discontinuous variation**?"
    )
    correct = "Because every human belongs strictly to one of these four qualitative groups, with zero intermediate blood types, controlled purely by inherited ABO alleles without environmental modification."
    options = [
        correct,
        "Because a person's blood group changes every day depending on what they eat for lunch.",
        "Because blood group is measured along a continuous ruler from 1 cm to 100 cm.",
        "Because people with type O blood belong to the plant kingdom.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the ABO blood group system:\n"
        f"- 4 discrete categories (A, B, AB, O).\n"
        f"- Determined by IA, IB, and i alleles on chromosome 9.\n"
        f"- Environment does not alter blood type.\n\n"
        f"**Step 2:** It is discontinuous because: **{correct}**."
    )
    return {
        "id": f"ns7_var_16_{rng.randint(100000, 999999)}",
        "subskill": "16_discontinuous_variation_abo_blood_groups",
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
            "tier_1": "You cannot have a blood type between A and B; you are A, B, AB, or O.",
            "tier_2": "Distinct separate categories mean discontinuous variation.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["blood_group_variation_type_error"],
    }


# 17. Continuous variation definition and spectrum
def arch_17_continuous_variation_definition_and_spectrum(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"How is **continuous variation** scientifically defined in biology?"
    )
    correct = "Variation that exhibits a continuous numerical spectrum of measurable values ranging smoothly from one extreme to another without distinct categories, typically polygenic and influenced by environmental factors."
    options = [
        correct,
        "Variation that has only two opposite states, such as having eyes or having no eyes.",
        "Characteristics that disappear permanently whenever an organism goes to sleep.",
        "Traits that are found only in non-living mineral crystals like granite.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define continuous variation:\n"
        f"- Traits form a gradual spectrum of values (e.g. height from 140 cm to 195 cm).\n"
        f"- Polygenic (controlled by many genes acting additively).\n"
        f"- Influenced by environmental conditions.\n\n"
        f"**Step 2:** The scientific definition is: **{correct}**."
    )
    return {
        "id": f"ns7_var_17_{rng.randint(100000, 999999)}",
        "subskill": "17_continuous_variation_definition_and_spectrum",
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
            "tier_1": "Think about traits you measure with a tape measure, ruler, or scale.",
            "tier_2": "Continuous variation forms a smooth unbroken numerical range from minimum to maximum.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["continuous_variation_definition_confusion"],
    }


# 18. Continuous variation human height
def arch_18_continuous_variation_human_height(rng: random.Random) -> Dict[str, Any]:
    min_h = rng.randint(135, 142)
    max_h = rng.randint(175, 185)
    prompt = (
        f"In a Grade 7 class, learner heights range from {min_h} cm to {max_h} cm. "
        f"Why is human height classified as **continuous variation**?"
    )
    correct = "Because height is a quantitative measurement that can take any value along a continuous numerical scale between {min_h} cm and {max_h} cm, rather than falling into separate distinct boxes."
    options = [
        correct,
        "Because all humans are either exactly 1 metre or exactly 2 metres tall with no numbers in between.",
        "Because height is determined strictly by how many haircuts a person gets.",
        "Because height is an acquired scar that disappears during exercise.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze human height variation:\n"
        f"- Can be 150.2 cm, 150.5 cm, 151.1 cm, etc. (infinite intermediate gradations).\n"
        f"- Controlled by over 400 genes (polygenic) interacting with nutrition.\n\n"
        f"**Step 2:** It is continuous because: **{correct}**."
    )
    return {
        "id": f"ns7_var_18_{rng.randint(100000, 999999)}",
        "subskill": "18_continuous_variation_human_height",
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
            "tier_1": "Height is measured with a tape measure on a continuous scale.",
            "tier_2": "Any numerical value between the minimum and maximum is possible.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["height_continuity_misunderstanding"],
    }


# 19. Continuous variation hand span measurements
def arch_19_continuous_variation_hand_span_measurements(rng: random.Random) -> Dict[str, Any]:
    span_min = rng.randint(14, 16)
    span_max = rng.randint(22, 25)
    prompt = (
        f"Learners measure their hand spans (the maximum distance from the tip of the thumb to the tip of the little finger with an outstretched hand). "
        f"The class measurements range smoothly from {span_min} cm to {span_max} cm. "
        f"Which type of variation does hand span represent, and what graph type best displays this continuous data?"
    )
    correct = "Continuous variation; best displayed using a histogram or continuous frequency polygon curve."
    options = [
        correct,
        "Discontinuous variation; best displayed using a pie chart with zero numbers.",
        "Environmental injury; best displayed using a map of the world.",
        "Abiotic chemical reaction; best displayed on a periodic table.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Classify hand span:\n"
        f"- Measured on a continuous scale ({span_min} cm to {span_max} cm) -> Continuous variation.\n"
        f"- Displayed using a histogram where adjacent bars touch, reflecting continuous intervals.\n\n"
        f"**Step 2:** The correct combination is: **{correct}**."
    )
    return {
        "id": f"ns7_var_19_{rng.randint(100000, 999999)}",
        "subskill": "19_continuous_variation_hand_span_measurements",
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
            "tier_1": "Hand span is measured in centimetres and millimetres (continuous).",
            "tier_2": "Continuous data is plotted as a histogram (bars touching).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["hand_span_graph_type_confusion"],
    }


# 20. Continuous variation body mass and shoe size
def arch_20_continuous_variation_body_mass_and_shoe_size(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Which option correctly lists two examples of **continuous variation** in humans?"
    )
    correct = "Body mass (measured in kg) and foot length (measured in mm)."
    options = [
        correct,
        "ABO blood group and presence of cheek dimples.",
        "Attached earlobes and tongue rolling ability.",
        "Biological sex and natural eye colour.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify continuous traits:\n"
        f"- Body mass and foot length are quantitative, continuous measurements.\n"
        f"- Blood group, earlobes, and tongue rolling are discontinuous (qualitative categories).\n\n"
        f"**Step 2:** The two continuous traits are: **{correct}**."
    )
    return {
        "id": f"ns7_var_20_{rng.randint(100000, 999999)}",
        "subskill": "20_continuous_variation_body_mass_and_shoe_size",
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
            "tier_1": "Look for the traits that are measured on a scale or ruler.",
            "tier_2": "Body mass (kg) and foot length (mm) are continuous measurements.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["continuous_trait_selection_error"],
    }


# 21. Graphical representation bar chart vs histogram
def arch_21_graphical_representation_bar_chart_vs_histogram(rng: random.Random) -> Dict[str, Any]:
    bar_h = rng.randint(40, 80)
    hist_h1 = rng.randint(30, 60)
    hist_h2 = rng.randint(60, 95)
    hist_h3 = rng.randint(40, 70)

    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 440 220' width='100%' height='220'>"
        f"<rect width='440' height='220' fill='#F8FAFC' rx='8'/>"
        f"<text x='110' y='30' fill='#0F172A' font-size='12' font-weight='bold' text-anchor='middle'>Bar Chart (Spaces)</text>"
        f"<line x1='30' y1='170' x2='190' y2='170' stroke='#334155' stroke-width='2'/>"
        f"<rect x='45' y='{170-bar_h}' width='40' height='{bar_h}' fill='#3B82F6'/>"
        f"<text x='65' y='190' fill='#334155' font-size='10' text-anchor='middle'>Type A</text>"
        f"<rect x='115' y='{170-int(bar_h*0.7)}' width='40' height='{int(bar_h*0.7)}' fill='#3B82F6'/>"
        f"<text x='135' y='190' fill='#334155' font-size='10' text-anchor='middle'>Type B</text>"
        f"<text x='320' y='30' fill='#0F172A' font-size='12' font-weight='bold' text-anchor='middle'>Histogram (No Spaces)</text>"
        f"<line x1='230' y1='170' x2='410' y2='170' stroke='#334155' stroke-width='2'/>"
        f"<rect x='245' y='{170-hist_h1}' width='45' height='{hist_h1}' fill='#10B981'/>"
        f"<rect x='290' y='{170-hist_h2}' width='45' height='{hist_h2}' fill='#10B981'/>"
        f"<rect x='335' y='{170-hist_h3}' width='45' height='{hist_h3}' fill='#10B981'/>"
        f"<text x='267' y='190' fill='#334155' font-size='9' text-anchor='middle'>140-149</text>"
        f"<text x='312' y='190' fill='#334155' font-size='9' text-anchor='middle'>150-159</text>"
        f"<text x='357' y='190' fill='#334155' font-size='9' text-anchor='middle'>160-169</text>"
        f"</svg>"
    )
    prompt = (
        f"In biological data representation, bar charts and histograms have distinct graphical conventions. "
        f"Why must a **bar chart** have spaces between bars, while a **histogram** has contiguous bars touching each other without spaces?"
    )
    correct = "A bar chart represents discrete, separate categories of discontinuous data (spaces emphasize no continuum); a histogram represents continuous data grouped into continuous numerical intervals where one class boundary touches the next."
    options = [
        correct,
        "A bar chart is drawn with spaces so learners have room to write their homework in the gaps.",
        "Histograms have touching bars because the ink was wet and smudged together during printing.",
        "Both graphs are identical and there is zero scientific reason to draw spaces or touching bars.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Master graphing conventions for variation:\n"
        f"- Bar Chart: Discontinuous data (e.g. blood groups). Bars are separated by equal gaps because categories are distinct and independent.\n"
        f"- Histogram: Continuous data (e.g. height 140-149 cm, 150-159 cm). Bars touch because the data is on a continuous numerical scale.\n\n"
        f"**Step 2:** The reason is: **{correct}**."
    )
    return {
        "id": f"ns7_var_21_{rng.randint(100000, 999999)}",
        "subskill": "21_graphical_representation_bar_chart_vs_histogram",
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
            "tier_1": "Spaces between bars show separate categories; touching bars show a continuous number scale.",
            "tier_2": "Bar chart = discontinuous (spaces); Histogram = continuous (no spaces).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["bar_chart_vs_histogram_convention_confusion"],
    }


# 22. Frequency table grouping continuous data
def arch_22_frequency_table_grouping_continuous_data(rng: random.Random) -> Dict[str, Any]:
    c1 = rng.randint(4, 7)
    c2 = rng.randint(10, 15)
    c3 = rng.randint(12, 18)
    c4 = rng.randint(3, 6)
    total = c1 + c2 + c3 + c4

    prompt = (
        f"A learner surveyed the heights of {total} Grade 7 learners and constructed this frequency table:\n"
        f"- 130 to 139 cm: {c1} learners\n"
        f"- 140 to 149 cm: {c2} learners\n"
        f"- 150 to 159 cm: {c3} learners\n"
        f"- 160 to 169 cm: {c4} learners\n\n"
        f"Why is continuous biological data like height grouped into class intervals in a frequency table?"
    )
    correct = "Because each individual learner may have a slightly different unique height (e.g. 142.3 cm vs 142.7 cm); grouping into intervals organizes raw data into a manageable summary to reveal the distribution pattern."
    options = [
        correct,
        "Because all learners in the same interval are forced to shrink or stretch to match the average.",
        "Because scientists are not allowed to measure anything smaller than 10 metres.",
        "Because frequency tables turn living learners into non-living rocks.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand data grouping in frequency tables:\n"
        f"- Total sample size: {total} learners.\n"
        f"- Grouping into class intervals of 10 cm reveals the bell-shaped distribution pattern.\n\n"
        f"**Step 2:** The purpose of grouping is: **{correct}**."
    )
    return {
        "id": f"ns7_var_22_{rng.randint(100000, 999999)}",
        "subskill": "22_frequency_table_grouping_continuous_data",
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
            "tier_1": "Think about having 40 different heights with decimal numbers.",
            "tier_2": "Grouping into intervals summarizes continuous data so patterns can be seen.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["frequency_interval_purpose_misunderstanding"],
    }


# 23. Calculating statistical mean from variation data
def arch_23_calculating_statistical_mean_from_variation_data(rng: random.Random) -> Dict[str, Any]:
    base = rng.randint(145, 155)
    diffs = [rng.randint(-8, -3), rng.randint(-2, 1), rng.randint(2, 5), rng.randint(6, 10)]
    heights = [base + d for d in diffs]
    total_h = sum(heights)
    mean_val = total_h / len(heights)

    prompt = (
        f"Four Grade 7 learners record their heights: {heights[0]} cm, {heights[1]} cm, {heights[2]} cm, and {heights[3]} cm. "
        f"Calculate the **mean (average) height** of this group."
    )
    correct = f"{mean_val:.1f} cm"
    distractors = [
        f"{mean_val + 5:.1f} cm",
        f"{mean_val - 4:.1f} cm",
        f"{total_h} cm",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Formula for mean (average):\n"
        f"$$\\text{{Mean}} = \\frac{{\\text{{Sum of all values}}}}{{\\text{{Total number of values}}}}$$\n\n"
        f"**Step 2:** Add the four heights:\n"
        f"$$\\text{{Sum}} = {heights[0]} + {heights[1]} + {heights[2]} + {heights[3]} = {total_h}\\text{{ cm}}$$\n\n"
        f"**Step 3:** Divide by 4:\n"
        f"$$\\text{{Mean}} = \\frac{{{total_h}}}{{4}} = {mean_val:.1f}\\text{{ cm}}$$"
    )
    return {
        "id": f"ns7_var_23_{rng.randint(100000, 999999)}",
        "subskill": "23_calculating_statistical_mean_from_variation_data",
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
            "tier_1": "Add all 4 numbers together, then divide by 4.",
            "tier_2": f"Sum = {total_h}. Now divide {total_h} by 4.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["mean_calculation_arithmetic_error"],
    }


# 24. Calculating median mode range variation data
def arch_24_calculating_median_mode_range_variation_data(rng: random.Random) -> Dict[str, Any]:
    mode_val = rng.randint(148, 155)
    sorted_vals = sorted([mode_val - 6, mode_val - 2, mode_val, mode_val, mode_val + 5])
    rng.shuffle(sorted_vals)
    vals_str = ", ".join(f"{v} cm" for v in sorted_vals)
    sorted_again = sorted(sorted_vals)
    median_val = sorted_again[2]
    range_val = sorted_again[-1] - sorted_again[0]

    stat_type = rng.choice(["mode", "median", "range"])
    if stat_type == "mode":
        target_stat = f"mode (most frequent value)"
        ans = f"{mode_val} cm"
        exp = f"The value appearing most frequently is {mode_val} cm (appears twice)."
    elif stat_type == "median":
        target_stat = f"median (middle value when ordered)"
        ans = f"{median_val} cm"
        exp = f"Ordering the values: {sorted_again}. The middle value (3rd) is {median_val} cm."
    else:
        target_stat = f"range (difference between maximum and minimum)"
        ans = f"{range_val} cm"
        exp = f"Maximum ({sorted_again[-1]} cm) - Minimum ({sorted_again[0]} cm) = {range_val} cm."

    prompt = (
        f"A set of 5 hand span measurements is recorded: {vals_str}. "
        f"What is the **{target_stat}** for this dataset?"
    )
    correct = ans
    options = [ans, f"{median_val + 2} cm", f"{range_val + 3} cm", f"{mode_val - 4} cm"]
    options = list(dict.fromkeys(options))
    while len(options) < 4:
        options.append(f"{rng.randint(140, 165)} cm")
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Order the data from smallest to largest:\n"
        f"{sorted_again}\n\n"
        f"**Step 2:** Calculate {target_stat}:\n"
        f"{exp}\n\n"
        f"**Step 3:** The answer is **{ans}**."
    )
    return {
        "id": f"ns7_var_24_{rng.randint(100000, 999999)}",
        "subskill": "24_calculating_median_mode_range_variation_data",
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
            "tier_1": "Mode = most frequent; Median = middle number when arranged in order; Range = Highest minus Lowest.",
            "tier_2": f"Find the {target_stat}.",
            "tier_3": f"The answer is: {ans}.",
        },
        "misconception_tags": ["median_mode_range_confusion"],
    }


# 25. Evaluating sample size and reliability in surveys
def arch_25_evaluating_sample_size_and_reliability_in_surveys(rng: random.Random) -> Dict[str, Any]:
    small_n = rng.choice([2, 3])
    large_n = rng.choice([100, 150])
    prompt = (
        f"In a school investigation on learner hand spans, Learner A measures only {small_n} classmates and concludes that 'all Grade 7 learners have a hand span of 18 cm.' "
        f"Learner B measures {large_n} classmates across the grade. "
        f"Why is Learner B's investigation far more scientifically reliable?"
    )
    correct = f"A larger sample size ({large_n} learners) captures the full natural range of variation in the population, minimising the distortion caused by individual anomalous outliers."
    options = [
        correct,
        f"Because measuring {small_n} learners is a crime punishable by law.",
        "Because Learner B used an electric wooden ruler that changes measurements automatically.",
        "Because sample size has zero effect on the accuracy or reliability of scientific conclusions.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand sample size and reliability in scientific inquiry:\n"
        f"- Measuring only {small_n} individuals is unrepresentative and vulnerable to sampling bias.\n"
        f"- Measuring {large_n} individuals provides a reliable statistical representation of the true population mean and distribution.\n\n"
        f"**Step 2:** The justification is: **{correct}**."
    )
    return {
        "id": f"ns7_var_25_{rng.randint(100000, 999999)}",
        "subskill": "25_evaluating_sample_size_and_reliability_in_surveys",
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
            "tier_1": "Is a survey of 2 people representative of a whole school? No.",
            "tier_2": "A larger sample size reduces bias and gives a true picture of population variation.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["sample_size_reliability_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "01_variation_within_species_concept": arch_01_variation_within_species_concept,
    "02_dog_breed_morphological_variation": arch_02_dog_breed_morphological_variation,
    "03_cattle_breed_nguni_coat_pattern_variation": arch_03_cattle_breed_nguni_coat_pattern_variation,
    "04_plant_intraspecific_variation_flower_colour": arch_04_plant_intraspecific_variation_flower_colour,
    "05_human_physical_variation_facial_features": arch_05_human_physical_variation_facial_features,
    "06_human_fingerprint_uniqueness_variation": arch_06_human_fingerprint_uniqueness_variation,
    "07_inherited_variation_definition_and_mechanism": arch_07_inherited_variation_definition_and_mechanism,
    "08_environmental_variation_definition_and_causes": arch_08_environmental_variation_definition_and_causes,
    "09_classifying_traits_inherited_vs_environmental": arch_09_classifying_traits_inherited_vs_environmental,
    "10_interaction_genes_and_environment_height": arch_10_interaction_genes_and_environment_height,
    "11_interaction_genes_and_environment_skin_tanning": arch_11_interaction_genes_and_environment_skin_tanning,
    "12_interaction_genes_and_environment_plant_growth": arch_12_interaction_genes_and_environment_plant_growth,
    "13_discontinuous_variation_definition_and_traits": arch_13_discontinuous_variation_definition_and_traits,
    "14_discontinuous_variation_tongue_rolling": arch_14_discontinuous_variation_tongue_rolling,
    "15_discontinuous_variation_earlobe_attachment": arch_15_discontinuous_variation_earlobe_attachment,
    "16_discontinuous_variation_abo_blood_groups": arch_16_discontinuous_variation_abo_blood_groups,
    "17_continuous_variation_definition_and_spectrum": arch_17_continuous_variation_definition_and_spectrum,
    "18_continuous_variation_human_height": arch_18_continuous_variation_human_height,
    "19_continuous_variation_hand_span_measurements": arch_19_continuous_variation_hand_span_measurements,
    "20_continuous_variation_body_mass_and_shoe_size": arch_20_continuous_variation_body_mass_and_shoe_size,
    "21_graphical_representation_bar_chart_vs_histogram": arch_21_graphical_representation_bar_chart_vs_histogram,
    "22_frequency_table_grouping_continuous_data": arch_22_frequency_table_grouping_continuous_data,
    "23_calculating_statistical_mean_from_variation_data": arch_23_calculating_statistical_mean_from_variation_data,
    "24_calculating_median_mode_range_variation_data": arch_24_calculating_median_mode_range_variation_data,
    "25_evaluating_sample_size_and_reliability_in_surveys": arch_25_evaluating_sample_size_and_reliability_in_surveys,
}
