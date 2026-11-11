"""Grade 7 Natural Sciences: Term 1 - Sexual Reproduction (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/03. Sexual reproduction.md.
Focus: Reproduction in Angiosperms, Floral Anatomy, Pollination, Fertilisation, and Seed Dispersal.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Flower outer structures calyx corolla
def arch_01_flower_outer_structures_calyx_corolla(rng: random.Random) -> Dict[str, Any]:
    parts = [
        ("Sepals (collectively the Calyx)", "small green leaf-like structures enclosing and protecting the delicate inner floral bud before it opens"),
        ("Petals (collectively the Corolla)", "often brightly coloured, scented, and equipped with nectar guides to attract specific pollinators like bees and butterflies"),
        ("Receptacle", "the thickened swollen stem base that physically supports all four whorls of floral organs"),
        ("Peduncle", "the flower stalk that attaches the individual flower to the main plant stem"),
    ]
    part_name, function = rng.choice(parts)
    prompt = (
        f"In the morphology of an angiosperm flower, what is the primary biological function of '{part_name}'?"
    )
    correct = function
    options = [function] + [p[1] for p in parts if p[1] != function]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review outer flower structures:\n"
        f"- Sepals (Calyx): protect the unopened bud.\n"
        f"- Petals (Corolla): attract pollinators with color and scent.\n"
        f"- Receptacle: supports floral whorls.\n"
        f"- Peduncle: flower stalk.\n\n"
        f"**Step 2:** '{part_name}' is responsible for: **{function}**."
    )
    return {
        "id": f"ns7_sr_01_{rng.randint(100000, 999999)}",
        "subskill": "01_flower_outer_structures_calyx_corolla",
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
            "tier_1": "Recall the outermost parts of a flower before it opens.",
            "tier_2": "Green sepals protect the bud; colourful petals attract pollinators.",
            "tier_3": f"The answer is: {function}.",
        },
        "misconception_tags": ["floral_whorl_confusion"],
    }


# 02. Flower male structures stamen anther filament
def arch_02_flower_male_structures_stamen_anther_filament(rng: random.Random) -> Dict[str, Any]:
    parts = [
        ("Anther", "the terminal pollen-producing sac containing microsporangia where male pollen grains develop and are released"),
        ("Filament", "the slender stalk that elevates and positions the anther for effective pollen transfer by wind or pollinators"),
        ("Stamen", "the collective male reproductive organ of the flower, consisting of the filament and anther"),
    ]
    target, description = rng.choice(parts)
    prompt = (
        f"In flowering plants, the male reproductive system produces male gametes. "
        f"Which statement scientifically defines the role of the '{target}'?"
    )
    correct = description
    options = [description] + [p[1] for p in parts if p[1] != description] + [
        "The sticky female surface that receives incoming pollen grains."
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review the male floral organ (Stamen):\n"
        f"- Stamen = Filament + Anther.\n"
        f"- Anther: produces and sheds pollen grains.\n"
        f"- Filament: elevates the anther.\n\n"
        f"**Step 2:** For '{target}', the role is: **{description}**."
    )
    return {
        "id": f"ns7_sr_02_{rng.randint(100000, 999999)}",
        "subskill": "02_flower_male_structures_stamen_anther_filament",
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
            "tier_1": "The stamen is the male organ; the anther holds the pollen.",
            "tier_2": "Look at whether the question asks for the pollen sac (anther), stalk (filament), or whole unit (stamen).",
            "tier_3": f"The answer is: {description}.",
        },
        "misconception_tags": ["stamen_component_confusion"],
    }


# 03. Flower female structures pistil stigma style ovary
def arch_03_flower_female_structures_pistil_stigma_style_ovary(rng: random.Random) -> Dict[str, Any]:
    female_parts = [
        ("Stigma", "the sticky, moist, or feathery top surface of the pistil specialized to capture and hold incoming pollen grains"),
        ("Style", "the elongated neck connecting the stigma to the ovary through which the pollen tube grows toward the ovules"),
        ("Ovary", "the swollen basal chamber of the pistil that encloses and protects one or more ovules"),
        ("Ovule", "the reproductive structure inside the ovary containing the female gamete (egg cell), which develops into a seed after fertilisation"),
    ]
    part_name, role = rng.choice(female_parts)
    prompt = (
        f"The female reproductive organ of a flower is the pistil (or carpel). "
        f"Which statement describes the function of the '{part_name}'?"
    )
    correct = role
    options = [role] + [p[1] for p in female_parts if p[1] != role]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review pistil / carpel structures:\n"
        f"- Stigma: sticky surface catching pollen.\n"
        f"- Style: neck connecting stigma to ovary.\n"
        f"- Ovary: protects ovules and becomes the fruit.\n"
        f"- Ovule: holds the female egg and becomes the seed.\n\n"
        f"**Step 2:** '{part_name}' functions as: **{role}**."
    )
    return {
        "id": f"ns7_sr_03_{rng.randint(100000, 999999)}",
        "subskill": "03_flower_female_structures_pistil_stigma_style_ovary",
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
            "tier_1": "Stigma is sticky on top, style is the neck, ovary holds ovules at the bottom.",
            "tier_2": "Match the named female part directly to its role in catching pollen or housing egg cells.",
            "tier_3": f"The answer is: {role}.",
        },
        "misconception_tags": ["pistil_structure_function_confusion"],
    }


# 04. Distinguish male vs female floral organs
def arch_04_distinguish_male_vs_female_floral_organs(rng: random.Random) -> Dict[str, Any]:
    organs = [
        ("Anther and Filament", "Male reproductive organs (Stamen)", "they manufacture and present pollen grains containing male gametes"),
        ("Stigma, Style, and Ovary", "Female reproductive organs (Pistil / Carpel)", "they receive pollen, guide the pollen tube, and contain ovules with female egg cells"),
    ]
    parts, classification, justification = rng.choice(organs)
    alt = organs[1] if parts == organs[0][0] else organs[0]
    prompt = (
        f"In flower dissection investigations, learners classify floral parts into male and female organs. "
        f"How should '{parts}' be scientifically classified?"
    )
    correct = f"{classification} — because {justification}."
    distractors = [
        f"{alt[1]} — because {alt[2]}.",
        "Non-reproductive vegetative organs — because they only absorb water from the air.",
        "Abiotic mineral structures — because they contain zero living plant cells.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish male vs female floral structures:\n"
        f"- Male = Stamen (Anther + Filament).\n"
        f"- Female = Pistil/Carpel (Stigma + Style + Ovary + Ovules).\n\n"
        f"**Step 2:** '{parts}' are: **{correct}**."
    )
    return {
        "id": f"ns7_sr_04_{rng.randint(100000, 999999)}",
        "subskill": "04_distinguish_male_vs_female_floral_organs",
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
            "tier_1": "Remember: Stamen is male (ends in 'men'); Pistil/carpel is female.",
            "tier_2": "Anther + filament = stamen; stigma + style + ovary = pistil.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["male_female_floral_organ_inversion"],
    }


# 05. Pollination definition self vs cross
def arch_05_pollination_definition_self_vs_cross(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("Cross-pollination", "the transfer of pollen from the anther of a flower on one plant to the stigma of a flower on a different plant of the same species, promoting genetic diversity in offspring"),
        ("Self-pollination", "the transfer of pollen from the anther to the stigma of the very same flower, or to another flower on the same individual plant"),
    ]
    target_type, defn = rng.choice(types)
    other_type, other_defn = (types[1] if target_type == types[0] else types[0])
    prompt = (
        f"Pollination is a vital process in angiosperm sexual reproduction. "
        f"Which statement defines '{target_type[0]}' and its genetic consequence?"
    )
    correct = defn
    options = [
        defn,
        other_defn,
        "The fusion of male and female nuclei inside the ovule to produce a zygote.",
        "The shedding of ripe seeds from a tree onto dry soil.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish self- vs cross-pollination:\n"
        f"- Pollination = transfer of pollen from anther to stigma.\n"
        f"- Self-pollination = within the same plant (low genetic diversity).\n"
        f"- Cross-pollination = between different plants of the same species (high genetic diversity).\n\n"
        f"**Step 2:** For '{target_type[0]}', the definition is: **{defn}**."
    )
    return {
        "id": f"ns7_sr_05_{rng.randint(100000, 999999)}",
        "subskill": "05_pollination_definition_self_vs_cross",
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
            "tier_1": "Does pollen travel to another plant (cross) or stay on the same plant (self)?",
            "tier_2": "Cross-pollination mixes genes from two different plants of the same species.",
            "tier_3": f"The answer is: {defn}.",
        },
        "misconception_tags": ["pollination_vs_fertilisation_conflation"],
    }


# 06. Insect pollination adaptations floral traits
def arch_06_insect_pollination_adaptations_floral_traits(rng: random.Random) -> Dict[str, Any]:
    insects = [
        ("Honeybees (Apis mellifera)", "bright yellow or blue petals with ultraviolet nectar guides, sweet floral scent, sugary concentrated nectar, and sticky grooved pollen grains that adhere to hairy insect legs"),
        ("Moths visiting flowers at night", "pale white or cream petals visible in moonlight, intensely sweet evening fragrance, and deep tubular corollas accessible to long proboscises"),
        ("Carrion flies visiting the Voodoo Lily / Stapelia", "dark reddish-brown mottled petals resembling rotting flesh, producing a putrid stench of decaying meat to lure flies looking for egg-laying sites"),
    ]
    pollinator, floral_traits = rng.choice(insects)
    prompt = (
        f"Insect-pollinated flowers have evolved specialized co-adaptations. "
        f"Which suite of floral characteristics has evolved specifically to attract '{pollinator}'?"
    )
    correct = floral_traits
    options = [floral_traits] + [i[1] for i in insects if i[1] != floral_traits]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Match pollinators to floral syndromes:\n"
        f"- Bees: bright yellow/blue, UV guides, sweet scent, sticky pollen.\n"
        f"- Night moths: white/cream flowers, strong evening scent, tubular petals.\n"
        f"- Carrion flies (e.g. Voodoo lily / Stapelia): reddish flesh color, foul rotting odor.\n\n"
        f"**Step 2:** For '{pollinator}', the matching floral traits are: **{floral_traits}**."
    )
    return {
        "id": f"ns7_sr_06_{rng.randint(100000, 999999)}",
        "subskill": "06_insect_pollination_adaptations_floral_traits",
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
            "tier_1": "Think about what senses the insect uses: bees see yellow/blue, night moths smell in the dark, flies seek rotting meat.",
            "tier_2": "Match the pollinator's sensory preference to the flower's color and smell.",
            "tier_3": f"The answer is: {floral_traits}.",
        },
        "misconception_tags": ["pollination_syndrome_mismatch"],
    }


# 07. Bird pollination adaptations sunbirds
def arch_07_bird_pollination_adaptations_sunbirds(rng: random.Random) -> Dict[str, Any]:
    birds = [
        ("The Malachite sunbird visiting indigenous Aloes and Proteas", "vivid red, orange, or scarlet tubular flowers with robust perianths, copious volumes of dilute nectar, and virtually no scent because birds have a poor sense of smell"),
        ("The Cape sugarbird feeding on King Protea inflorescences", "large sturdy floral heads capable of supporting the bird's weight, producing large nectar rewards and dusting pollen onto the bird's forehead feathers"),
    ]
    bird_case, adaptations = rng.choice(birds)
    prompt = (
        f"Ornithophilous (bird-pollinated) flowers in South Africa show distinctive adaptations. "
        f"Consider '{bird_case}'. Which combination of floral features scientifically characterizes bird-pollinated flowers?"
    )
    correct = adaptations
    options = [
        adaptations,
        "Tiny green flowers with long feathery dangling stigmas and dry airborne dust pollen without nectar.",
        "Foul-smelling flowers that smell like rotting fish with dark brown decaying petals.",
        "Flowers that bloom exclusively underground without any petals or nectar.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review bird pollination syndrome:\n"
        f"- Birds have keen color vision (especially red and orange) but poor olfaction (sense of smell).\n"
        f"- Flowers are bright red/orange, sturdy to support perching birds, odorless, and produce lots of dilute nectar.\n\n"
        f"**Step 2:** For '{bird_case}', the features are: **{adaptations}**."
    )
    return {
        "id": f"ns7_sr_07_{rng.randint(100000, 999999)}",
        "subskill": "07_bird_pollination_adaptations_sunbirds",
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
            "tier_1": "Birds see red very well, but they cannot smell.",
            "tier_2": "Bird flowers are bright red/orange, odorless, and full of watery nectar.",
            "tier_3": f"The answer is: {adaptations}.",
        },
        "misconception_tags": ["bird_pollination_odor_misconception"],
    }


# 08. Wind pollination adaptations grasses
def arch_08_wind_pollination_adaptations_grasses(rng: random.Random) -> Dict[str, Any]:
    grasses = [
        ("Maize (Zea mays)", "tassels at the top with dangling anthers shedding millions of lightweight pollen grains, and long silky feathery styles (corn silk) catching airborne pollen below"),
        ("Wild veld grasses (Themeda triandra / red grass)", "small, inconspicuous green/brown flowers with long flexible filaments hanging anthers outside the bracts, and branched feathery stigmas creating a wide surface area"),
        ("Restionaceae (Cape reeds) in the Fynbos", "reduced petals, massive dry pollen production, and wind-exposed pendulous stamens that shake pollen into air currents"),
    ]
    plant, traits = rng.choice(grasses)
    prompt = (
        f"Anemophilous (wind-pollinated) plants such as '{plant}' do not rely on animal pollinators. "
        f"Which set of structural adaptations enables successful wind pollination?"
    )
    correct = traits
    options = [traits] + [g[1] for g in grasses if g[1] != traits]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review wind-pollination adaptations:\n"
        f"- Flowers are small, dull green or brown (no need for bright petals).\n"
        f"- No scent and no nectar.\n"
        f"- Long flexible filaments holding anthers outside the flower.\n"
        f"- Feathery, branched stigmas to trap airborne pollen grains.\n"
        f"- Smooth, light, dry pollen produced in enormous quantities.\n\n"
        f"**Step 2:** For '{plant}', the adaptations are: **{traits}**."
    )
    return {
        "id": f"ns7_sr_08_{rng.randint(100000, 999999)}",
        "subskill": "08_wind_pollination_adaptations_grasses",
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
            "tier_1": "Wind does not care about bright colors, sweet smells, or nectar.",
            "tier_2": "Wind flowers have feathery stigmas and dangling anthers to catch breezes.",
            "tier_3": f"The answer is: {traits}.",
        },
        "misconception_tags": ["wind_pollination_floral_trait_error"],
    }


# 09. Water pollination adaptations aquatic plants
def arch_09_water_pollination_adaptations_aquatic_plants(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Hydrophilous (water-pollinated) plants like eelgrass (Vallisneria) reproduce submerged in water. "
        f"Which specialized adaptation allows pollen to reach the female flower in water?"
    )
    correct = "Male flowers or pollen grains detach and float on the water surface film, being carried by water currents until they drift into contact with the floating stigmas of female flowers."
    options = [
        correct,
        "Pollen grains develop wings and fly into clouds to wait for thunderstorms.",
        "Water lilies hire underwater scuba-diving bees to carry pollen grains between roots.",
        "Pollen grains dissolve into salt crystals and permanently leave the plant kingdom.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review water pollination (hydrophily):\n"
        f"- Occurs in submerged aquatic angiosperms (e.g. Vallisneria).\n"
        f"- Male flowers/pollen detach and float on the water meniscus.\n"
        f"- Surface currents bring floating pollen to the receptive surface of female flowers.\n\n"
        f"**Step 2:** The mechanism is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_09_{rng.randint(100000, 999999)}",
        "subskill": "09_water_pollination_adaptations_aquatic_plants",
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
            "tier_1": "Think about how pollen moves in water: floating on currents.",
            "tier_2": "Pollen floats on water currents to reach the female flowers at the surface.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["water_pollination_mechanism_error"],
    }


# 10. Pollinator mutualism and agricultural food security
def arch_10_pollinator_mutualism_and_agricultural_food_security(rng: random.Random) -> Dict[str, Any]:
    crop = rng.choice(["apples in the Western Cape", "sunflowers in the Free State", "avocados in Limpopo", "macadamia nuts in Mpumalanga"])
    prompt = (
        f"In South African agriculture, honeybees pollinate commercial crops like {crop}. "
        f"If indiscriminate pesticide spraying and habitat loss cause a catastrophic 90% decline in local bee populations, "
        f"what is the direct agricultural consequence?"
    )
    correct = f"Pollination failure drastically reduces flower fertilisation, causing severe fruit and seed yield collapse, leading to food shortages and economic losses."
    options = [
        correct,
        f"The {crop} plants will automatically transform into wind-pollinated pine trees within 48 hours.",
        "Crop yields will double because bees were stealing precious sugars from the fruit trees.",
        "Plants will stop needing sunlight, water, and soil nutrients to produce fruit.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Connect pollination to fruit development:\n"
        f"- Fruit development requires successful pollination and fertilisation of ovules.\n"
        f"- Without bees to transfer pollen, ovules remain unfertilised and flowers drop off without setting fruit.\n\n"
        f"**Step 2:** The consequence for {crop} is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_10_{rng.randint(100000, 999999)}",
        "subskill": "10_pollinator_mutualism_and_agricultural_food_security",
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
            "tier_1": "No bees = no pollination = no fertilisation = no fruit.",
            "tier_2": "Fruit trees rely on insect pollination to produce commercial fruit yields.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["pollinator_crop_dependence_underestimation"],
    }


# 11. Pollen tube germination down style
def arch_11_pollen_tube_germination_down_style(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"After a compatible pollen grain lands on the sticky stigma of a flower during pollination, what cellular process happens next?"
    )
    correct = "The pollen grain absorbs sugary fluid from the stigma and germinates, extending a microscopic pollen tube that digests its way down the style toward the ovary micropyle."
    options = [
        correct,
        "The pollen grain instantly explodes and transforms the petals into edible apples.",
        "The stigma detaches from the plant and falls into the soil to grow new roots.",
        "The pollen grain swims into the air and pollinates a passing bird.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace events between pollination and fertilisation:\n"
        f"1. Pollen grain lands on stigma.\n"
        f"2. Sugary secretions stimulate pollen germination.\n"
        f"3. Pollen tube grows down through the style tissue, carrying male gamete nuclei toward the ovule in the ovary.\n\n"
        f"**Step 2:** The correct next event is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_11_{rng.randint(100000, 999999)}",
        "subskill": "11_pollen_tube_germination_down_style",
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
            "tier_1": "How does the male cell reach the ovule inside the ovary deep below the stigma?",
            "tier_2": "A pollen tube grows down through the style carrying the sperm nucleus.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["pollen_tube_function_misunderstanding"],
    }


# 12. Plant fertilisation male gamete ovule fusion
def arch_12_plant_fertilisation_male_gamete_ovule_fusion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"What is the precise biological definition of **fertilisation** in angiosperms?"
    )
    correct = "The fusion of the haploid nucleus of a male gamete from the pollen tube with the haploid nucleus of the female egg cell inside the ovule, forming a diploid zygote."
    options = [
        correct,
        "The physical transfer of dry pollen dust from anther to stigma by wind or bees.",
        "The absorption of chemical NPK fertilizer by root hairs from moist garden soil.",
        "The shedding of dry autumn leaves to prepare for winter dormancy.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish fertilisation from pollination and soil fertilization:\n"
        f"- Pollination = physical transfer of pollen to stigma.\n"
        f"- Fertilisation = biological fusion of male and female sex cell nuclei inside the ovule.\n"
        f"- Soil fertilization = adding mineral nutrients (NPK) to ground.\n\n"
        f"**Step 2:** In angiosperms, fertilisation is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_12_{rng.randint(100000, 999999)}",
        "subskill": "12_plant_fertilisation_male_gamete_ovule_fusion",
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
            "tier_1": "Fertilisation is the fusion of sex cell nuclei (gametes).",
            "tier_2": "Do not confuse fertilisation with pollination (moving pollen) or agricultural fertilizer.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fertilisation_vs_pollination_vs_soil_fertilizer"],
    }


# 13. Post fertilisation fate ovary to fruit ovule to seed
def arch_13_post_fertilisation_fate_ovary_to_fruit_ovule_to_seed(rng: random.Random) -> Dict[str, Any]:
    fruits = [
        ("a peach", "the single fertilised ovule becomes the inner stone/seed, while the surrounding ovary wall swells and ripens into the fleshy edible fruit"),
        ("a pea pod", "each fertilised ovule develops into an individual pea seed, while the elongated ovary wall develops into the green pod fruit"),
        ("a tomato", "the numerous fertilised ovules develop into small seeds suspended in jelly, while the multi-chambered ovary becomes the fleshy red berry"),
    ]
    fruit_name, fate = rng.choice(fruits)
    prompt = (
        f"Following successful double fertilisation in a flower, profound morphological changes take place. "
        f"In the development of {fruit_name}, what are the post-fertilisation fates of the **ovary** and the **ovules**?"
    )
    correct = f"The ovary develops into the fruit, and the ovules develop into the seeds ({fate})."
    distractors = [
        "The petals develop into seeds, while the roots develop into the fruit.",
        "The ovary converts into pure carbon dioxide gas, while the ovules become green leaves.",
        "The ovules become the fruit, while the ovary becomes the flower stem.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Learn the post-fertilisation transformations in angiosperms:\n"
        f"- Ovule -> Seed.\n"
        f"- Ovary -> Fruit.\n"
        f"- Petals, sepals, and stamens wilt and fall away.\n\n"
        f"**Step 2:** For {fruit_name}: **{correct}**."
    )
    return {
        "id": f"ns7_sr_13_{rng.randint(100000, 999999)}",
        "subskill": "13_post_fertilisation_fate_ovary_to_fruit_ovule_to_seed",
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
            "tier_1": "Ovary becomes Fruit; Ovule becomes Seed.",
            "tier_2": "Remember: Ovary -> Fruit, Ovule -> Seed.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ovary_ovule_fruit_seed_reversal"],
    }


# 14. Seed structure testa cotyledon embryo
def arch_14_seed_structure_testa_cotyledon_embryo(rng: random.Random) -> Dict[str, Any]:
    parts = [
        ("Testa (seed coat)", "a tough waterproof protective outer layer that shields the embryo from mechanical injury, fungal pathogens, and desiccation"),
        ("Cotyledon (seed leaf / food store)", "stores starch, proteins, and lipids to nourish the germinating embryo until its first green leaves can photosynthesise"),
        ("Radicle", "the embryonic root that emerges first through the micropyle to anchor the seedling and absorb water and soil minerals"),
        ("Plumule", "the embryonic shoot bearing miniature young leaves that grows upward into the light to form stems and foliage"),
    ]
    part_name, role = rng.choice(parts)
    prompt = (
        f"A seed contains a dormant plant embryo and food reserves. "
        f"In a bean seed, what is the biological function of the '{part_name}'?"
    )
    correct = role
    options = [role] + [p[1] for p in parts if p[1] != role]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review seed anatomy:\n"
        f"- Testa: protective outer coat.\n"
        f"- Cotyledon: food storage.\n"
        f"- Radicle: develops into root.\n"
        f"- Plumule: develops into shoot/stem.\n\n"
        f"**Step 2:** '{part_name}' serves to: **{role}**."
    )
    return {
        "id": f"ns7_sr_14_{rng.randint(100000, 999999)}",
        "subskill": "14_seed_structure_testa_cotyledon_embryo",
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
            "tier_1": "Radicle becomes the root; plumule becomes the shoot; cotyledon stores food; testa is the coat.",
            "tier_2": "Match the named seed component to its developmental role.",
            "tier_3": f"The answer is: {role}.",
        },
        "misconception_tags": ["radicle_plumule_inversion"],
    }


# 15. Seed dispersal importance preventing competition
def arch_15_seed_dispersal_importance_preventing_competition(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Why is seed dispersal away from the parent plant critical for the survival of plant seedlings?"
    )
    correct = "It reduces intense competition between parent and offspring for sunlight, soil water, and mineral nutrients, and facilitates colonization of new habitats."
    options = [
        correct,
        "It prevents seeds from ever absorbing water or germinating in soil.",
        "It ensures all seeds fall into deep rivers where they turn into marine fish.",
        "It allows parent plants to eat their own seeds for extra protein.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the evolutionary purpose of seed dispersal:\n"
        f"- If seeds simply drop beneath the parent canopy, they face extreme overcrowding.\n"
        f"- The large parent tree blocks sunlight and monopolizes soil moisture and root space.\n"
        f"- Dispersal minimizes parent-offspring competition and spreads the species across wider geographic niches.\n\n"
        f"**Step 2:** The importance is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_15_{rng.randint(100000, 999999)}",
        "subskill": "15_seed_dispersal_importance_preventing_competition",
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
            "tier_1": "Think about what happens if 500 seedlings try to grow under one big mother tree.",
            "tier_2": "Shade and lack of water would kill them; dispersing avoids competition.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["seed_dispersal_purpose_misunderstanding"],
    }


# 16. Seed dispersal wind mechanisms wings parachutes
def arch_16_seed_dispersal_wind_mechanisms_wings_parachutes(rng: random.Random) -> Dict[str, Any]:
    wind_seeds = [
        ("Dandelion (Taraxacum)", "a fine feathery umbrella of hairs (pappus) acting as a parachute that catches gentle thermal air updrafts"),
        ("Jacaranda tree", "lightweight flat seeds surrounded by papery aerodynamic wings that spin and glide through breezes away from the parent tree"),
        ("Sycamore / Maple tree", "a winged samara fruit that autorotates like a helicopter propeller, prolonging airtime for wind transport"),
    ]
    plant, mechanism = rng.choice(wind_seeds)
    prompt = (
        f"Wind-dispersed seeds show specialized aerodynamic structures. "
        f"In '{plant}', which physical feature enables long-distance wind dispersal?"
    )
    correct = mechanism
    options = [mechanism] + [w[1] for w in wind_seeds if w[1] != mechanism]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review wind seed dispersal adaptations:\n"
        f"- Parachute hairs (pappus): dandelions, thistle.\n"
        f"- Papery wings: jacaranda, pine, sycamore.\n"
        f"- Tiny dust seeds: orchids.\n\n"
        f"**Step 2:** For '{plant}', the mechanism is: **{mechanism}**."
    )
    return {
        "id": f"ns7_sr_16_{rng.randint(100000, 999999)}",
        "subskill": "16_seed_dispersal_wind_mechanisms_wings_parachutes",
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
            "tier_1": "Is it a feathery parachute (dandelion) or a papery wing (jacaranda)?",
            "tier_2": "Match the named plant to its parachute or winged fruit structure.",
            "tier_3": f"The answer is: {mechanism}.",
        },
        "misconception_tags": ["wind_dispersal_morphology_confusion"],
    }


# 17. Seed dispersal animal mechanisms fleshy fruits
def arch_17_seed_dispersal_animal_mechanisms_fleshy_fruits(rng: random.Random) -> Dict[str, Any]:
    fruits = [
        ("Indigenous wild figs (Ficus sur) eaten by monkeys and fruit bats", "sweet nutritious fleshy pericarp that attracts frugivores; the seeds have tough acid-resistant testas that survive gut digestive juices and are excreted in fertile faeces"),
        ("Wild olive berries (Olea europaea) consumed by starlings and bulbuls", "fleshy oil-rich fruit flesh digested for energy, while the hard stone passes unharmed through the avian cloaca onto distant perches"),
    ]
    plant, adaptation = rng.choice(fruits)
    prompt = (
        f"Many flowering plants invest metabolic energy into producing succulent fleshy fruits. "
        f"In '{plant}', how does endozoochory (internal dispersal by animals) operate?"
    )
    correct = adaptation
    options = [
        adaptation,
        "The fruit attaches external sharp barbs to the animal's fur and remains hooked for six months.",
        "The fruit dries in the hot sun and explosively catapults seeds 50 metres into the air.",
        "The fruit floats down rivers on ocean currents to germinate in saltwater beaches.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand internal animal dispersal (endozoochory):\n"
        f"- Animal eats the tasty fleshy fruit for nutrition.\n"
        f"- The seeds have indigestible coats that resist stomach acids.\n"
        f"- Seeds are deposited away from the parent with natural fertilizer (faeces/droppings).\n\n"
        f"**Step 2:** For '{plant}', the mechanism is: **{adaptation}**."
    )
    return {
        "id": f"ns7_sr_17_{rng.randint(100000, 999999)}",
        "subskill": "17_seed_dispersal_animal_mechanisms_fleshy_fruits",
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
            "tier_1": "Animals eat the fruit and poop out the seeds unharmed.",
            "tier_2": "The seed coat protects the embryo from stomach acid.",
            "tier_3": f"The answer is: {adaptation}.",
        },
        "misconception_tags": ["endozoochory_mechanism_confusion"],
    }


# 18. Seed dispersal animal mechanisms hooks and burs
def arch_18_seed_dispersal_animal_mechanisms_hooks_and_burs(rng: random.Random) -> Dict[str, Any]:
    plants = [
        ("Blackjack (Bidens pilosa)", "two stiff barbed spines (awns) at the tip of the seed that latch firmly into animal fur, feathers, or human socks"),
        ("Devil's thorn (Tribulus terrestris)", "sharp woody spines that penetrate the hooves of livestock or soles of animals, being carried until dislodged"),
        ("Burdock (Arctium)", "curved hook-tipped bracts covering the seed head that cling tenaciously to passing animal hair (inspiring the invention of Velcro)"),
    ]
    burs_plant, mechanism = rng.choice(plants)
    prompt = (
        f"Epizoochory is the external transport of seeds on animals. "
        f"In '{burs_plant}', which structural feature enables seeds to hitch a ride on passing animals?"
    )
    correct = mechanism
    options = [mechanism] + [p[1] for p in plants if p[1] != mechanism]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review external animal dispersal (epizoochory):\n"
        f"- Seeds possess physical hooks, spines, or sticky mucilage.\n"
        f"- They catch onto animal fur, feathers, or human clothing.\n\n"
        f"**Step 2:** For '{burs_plant}', the structure is: **{mechanism}**."
    )
    return {
        "id": f"ns7_sr_18_{rng.randint(100000, 999999)}",
        "subskill": "18_seed_dispersal_animal_mechanisms_hooks_and_burs",
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
            "tier_1": "Think about blackjacks sticking to your socks after walking through the veld.",
            "tier_2": "Barbed hooks and spines cling to fur and clothing.",
            "tier_3": f"The answer is: {mechanism}.",
        },
        "misconception_tags": ["epizoochory_hook_adaptation_error"],
    }


# 19. Seed dispersal water mechanisms buoyant husks
def arch_19_seed_dispersal_water_mechanisms_buoyant_husks(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Hydrochory is seed dispersal by water currents. "
        f"How is the coconut (Cocos nucifera) anatomically adapted to survive ocean transport over hundreds of kilometres?"
    )
    correct = "It possesses a thick, fibrous, air-trapping middle layer (mesocarp) providing buoyancy, and a waterproof outer exocarp protecting the viable embryo inside from saltwater penetration."
    options = [
        correct,
        "It possesses feather-like wings that allow it to fly across oceans in cloud storms.",
        "It attaches sharp barbed hooks to swimming dolphins and whales.",
        "It turns into an aquatic crab that crawls across the ocean floor.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review water dispersal adaptations:\n"
        f"- Low density / buoyant husks containing air pockets.\n"
        f"- Impermeable waterproof outer layer preventing salt rot.\n\n"
        f"**Step 2:** In coconuts: **{correct}**."
    )
    return {
        "id": f"ns7_sr_19_{rng.randint(100000, 999999)}",
        "subskill": "19_seed_dispersal_water_mechanisms_buoyant_husks",
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
            "tier_1": "Why does a coconut float? Thick fibrous husk full of air.",
            "tier_2": "Air pockets provide buoyancy, and the waterproof shell keeps saltwater out.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["water_dispersal_buoyancy_adaptation"],
    }


# 20. Seed dispersal explosive mechanical dehiscence
def arch_20_seed_dispersal_explosive_mechanical_dehiscence(rng: random.Random) -> Dict[str, Any]:
    pod_plants = [
        ("The bushveld sweet pea / bean pod", "as the mature pod ripens in the hot sun, the cell layers dry unevenly creating immense mechanical tension until the pod suddenly splits and twists violently, flinging seeds meters away"),
        ("The touch-me-not (Impatiens)", "water turgor pressure builds in the ripe capsule until the slightest brush ruptures the seam, curling the valves rapidly and catapulting seeds outward"),
    ]
    plant, mechanism = rng.choice(pod_plants)
    prompt = (
        f"Autochory (self-dispersal or explosive dehiscence) does not require wind, water, or animals. "
        f"In '{plant}', which physical force drives seed ejection?"
    )
    correct = mechanism
    options = [
        mechanism,
        "Strong mountain winds sucking seeds upward into the stratosphere.",
        "Migrating birds swallowing the pod and carrying it to Antarctica.",
        "Underground earthworms pushing the pod into river currents.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review explosive dehiscence / mechanical self-dispersal:\n"
        f"- Powered by differential drying tension (pea pods) or hydrostatic turgor pressure (Impatiens).\n"
        f"- Pod violently snaps open, ejecting seeds into the surrounding area.\n\n"
        f"**Step 2:** For '{plant}', the mechanism is: **{mechanism}**."
    )
    return {
        "id": f"ns7_sr_20_{rng.randint(100000, 999999)}",
        "subskill": "20_seed_dispersal_explosive_mechanical_dehiscence",
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
            "tier_1": "Think about a dry pea pod popping open in the hot sun.",
            "tier_2": "Uneven drying creates tension that snaps the pod open like a spring.",
            "tier_3": f"The answer is: {mechanism}.",
        },
        "misconception_tags": ["explosive_dehiscence_mechanism_error"],
    }


# 21. Seed germination requirements water oxygen warmth
def arch_21_seed_germination_requirements_water_oxygen_warmth(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"What are the three essential abiotic requirements for dormant bean seeds to germinate?"
    )
    correct = "Water (to activate enzymes and soften testa), Oxygen (for aerobic cellular respiration), and Favourable Warmth (for optimal enzyme catalytic activity)."
    options = [
        correct,
        "Direct sunlight, nitrogen gas, and ice crystals.",
        "Fertile organic soil, darkness, and carbon dioxide.",
        "Chemical weedkiller, sub-zero cold, and boiling water.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify essential germination requirements (WOW: Water, Oxygen, Warmth):\n"
        f"- Water: activates metabolic enzymes, hydrolyzes starch, expands cells.\n"
        f"- Oxygen: drives cellular respiration to release ATP energy for growth.\n"
        f"- Warmth: allows enzymes to function at their optimum rate.\n"
        f"- Note: Sunlight and soil are NOT required for initial germination (seeds germinate in the dark on wet cotton wool!).\n\n"
        f"**Step 2:** The three requirements are: **{correct}**."
    )
    return {
        "id": f"ns7_sr_21_{rng.randint(100000, 999999)}",
        "subskill": "21_seed_germination_requirements_water_oxygen_warmth",
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
            "tier_1": "Remember: WOW (Water, Oxygen, Warmth).",
            "tier_2": "Do seeds need light to germinate underground? No, only water, air (oxygen), and warmth.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["light_required_for_germination_misconception"],
    }


# 22. Investigation growing bean seedlings
def arch_22_investigation_growing_bean_seedlings(rng: random.Random) -> Dict[str, Any]:
    days = rng.randint(4, 7)
    prompt = (
        f"In a classroom investigation, a Grade 7 learner soaks bean seeds and places them on damp cotton wool in a jar. "
        f"After {days} days, the learner observes a white structure emerging first from the seed and growing downwards, "
        f"followed later by a green curved structure growing upwards. "
        f"Which statement correctly identifies these two emerging plant parts?"
    )
    correct = "The downward structure is the radicle (embryonic root, showing positive geotropism), and the upward structure is the plumule (embryonic shoot, showing negative geotropism)."
    options = [
        correct,
        "The downward structure is the petal, and the upward structure is the anther.",
        "The downward structure is the plumule, and the upward structure is the radicle.",
        "Both structures are fungal mycelia that are destroying the seed.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace bean seed germination:\n"
        f"- Radicle emerges first: grows downwards (positive geotropism) to anchor the plant and absorb moisture.\n"
        f"- Plumule emerges second: arches upwards (negative geotropism / positive phototropism) to develop into the stem and green leaves.\n\n"
        f"**Step 2:** The identification is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_22_{rng.randint(100000, 999999)}",
        "subskill": "22_investigation_growing_bean_seedlings",
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
            "tier_1": "Radicle goes down (roots); Plumule goes up (shoots).",
            "tier_2": "Radicle emerges first to establish water uptake.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["radicle_plumule_emergence_order"],
    }


# 23. Sexual vs asexual reproduction in plants
def arch_23_sexual_vs_asexual_reproduction_in_plants(rng: random.Random) -> Dict[str, Any]:
    methods = [
        ("Sexual reproduction via seeds", "involves flowers, gamete fusion, and genetic recombination, producing genetically diverse offspring adapted to changing environments"),
        ("Asexual reproduction via strawberry runners / potato tubers", "involves a single parent using mitotic vegetative propagation, producing genetically identical clones without flowers or seeds"),
    ]
    target, description = rng.choice(methods)
    other = methods[1] if target == methods[0] else methods[0]
    prompt = (
        f"Plants can reproduce both sexually and asexually. "
        f"Which statement scientifically characterizes '{target[0]}'?"
    )
    correct = description
    options = [
        description,
        other[1],
        "It involves taking minerals directly from rocks without any cellular division.",
        "It is only found in extinct prehistoric marine reptiles.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare plant reproductive modes:\n"
        f"- Sexual (seeds): gamete fusion, high genetic variation.\n"
        f"- Asexual (vegetative: runners, bulbs, tubers, cuttings): single parent, identical clones.\n\n"
        f"**Step 2:** For '{target[0]}', the characteristic is: **{description}**."
    )
    return {
        "id": f"ns7_sr_23_{rng.randint(100000, 999999)}",
        "subskill": "23_sexual_vs_asexual_reproduction_in_plants",
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
            "tier_1": "Seeds = sexual reproduction with genetic variation; runners/tubers = asexual cloning.",
            "tier_2": "Match the method to whether it uses gametes or vegetative parts.",
            "tier_3": f"The answer is: {description}.",
        },
        "misconception_tags": ["asexual_vegetative_cloning_confusion"],
    }


# 24. Angiosperm life cycle chronological sequence
def arch_24_angiosperm_life_cycle_chronological_sequence(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Which option lists the events of the angiosperm sexual reproductive life cycle in the correct chronological sequence?"
    )
    correct = "1. Flower formation -> 2. Pollination -> 3. Fertilisation -> 4. Fruit and seed development -> 5. Seed dispersal -> 6. Seed germination"
    options = [
        correct,
        "1. Seed germination -> 2. Seed dispersal -> 3. Fertilisation -> 4. Pollination -> 5. Flower formation",
        "1. Fertilisation -> 2. Pollination -> 3. Flower formation -> 4. Seed germination -> 5. Seed dispersal",
        "1. Fruit development -> 2. Pollination -> 3. Seed dispersal -> 4. Fertilisation -> 5. Seed germination",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace the life cycle chronologically:\n"
        f"1. Plant matures and forms flowers.\n"
        f"2. Pollen is transferred to stigma (Pollination).\n"
        f"3. Sperm fuses with egg in ovule (Fertilisation).\n"
        f"4. Ovary swells into fruit and ovules become seeds.\n"
        f"5. Seeds are carried away (Dispersal).\n"
        f"6. Seed absorbs water and grows into seedling (Germination).\n\n"
        f"**Step 2:** The correct chronological order is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_24_{rng.randint(100000, 999999)}",
        "subskill": "24_angiosperm_life_cycle_chronological_sequence",
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
            "tier_1": "Pollination must happen BEFORE fertilisation, and dispersal happens BEFORE germination.",
            "tier_2": "Flower -> Pollen transfer -> Gamete fusion -> Seeds inside fruit -> Dispersal -> Growth.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["plant_life_cycle_sequence_error"],
    }


# 25. Flower dissection morphology diagram
def arch_25_flower_dissection_morphology_diagram(rng: random.Random) -> Dict[str, Any]:
    tested_parts = [
        ("Anther", "Stamen (male organ)", "140", "50", "produces and sheds pollen grains"),
        ("Stigma", "Pistil / Carpel (female organ)", "200", "30", "receives and catches sticky pollen grains"),
        ("Ovary", "Pistil / Carpel (female organ)", "200", "130", "encloses ovules and ripens into the fruit"),
        ("Petal", "Corolla (outer whorl)", "90", "70", "attracts insect pollinators with colour and scent"),
    ]
    target_part, organ_group, px, py, role = rng.choice(tested_parts)
    stroke_col = rng.choice(["#2563EB", "#DC2626", "#059669", "#7C3AED"])

    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 240' width='100%' height='240'>"
        f"<rect width='400' height='240' fill='#F8FAFC' rx='8'/>"
        f"<path d='M 120 180 Q 200 130, 280 180' fill='#E2E8F0' stroke='#334155' stroke-width='2'/>"
        f"<path d='M 180 170 Q 200 120, 200 50 Q 200 120, 220 170 Z' fill='#D1FAE5' stroke='#059669' stroke-width='2'/>"
        f"<circle cx='200' cy='45' r='10' fill='#10B981'/>"
        f"<ellipse cx='200' cy='140' rx='25' ry='30' fill='#A7F3D0' stroke='#059669' stroke-width='1.5'/>"
        f"<circle cx='195' cy='135' r='5' fill='#047857'/>"
        f"<circle cx='205' cy='145' r='5' fill='#047857'/>"
        f"<path d='M 150 170 Q 140 100, 140 65' fill='none' stroke='#CA8A04' stroke-width='2'/>"
        f"<ellipse cx='140' cy='60' rx='10' ry='6' fill='#EAB308'/>"
        f"<path d='M 250 170 Q 260 100, 260 65' fill='none' stroke='#CA8A04' stroke-width='2'/>"
        f"<ellipse cx='260' cy='60' rx='10' ry='6' fill='#EAB308'/>"
        f"<path d='M 130 170 Q 70 120, 80 60 Q 120 100, 160 150' fill='#FCE7F3' stroke='#DB2777' stroke-width='1.5'/>"
        f"<path d='M 270 170 Q 330 120, 320 60 Q 280 100, 240 150' fill='#FCE7F3' stroke='#DB2777' stroke-width='1.5'/>"
        f"<circle cx='{px}' cy='{py}' r='14' fill='none' stroke='{stroke_col}' stroke-width='3' stroke-dasharray='3,3'/>"
        f"<text x='{px}' y='{int(py)-18}' fill='{stroke_col}' font-size='12' font-weight='bold' text-anchor='middle'>Target Part</text>"
        f"</svg>"
    )
    prompt = (
        f"In a botanical flower dissection, the highlighted dashed circle indicates the '{target_part}' (coordinates near x={px}, y={py}). "
        f"What is the identity and primary biological function of this marked floral structure?"
    )
    correct = f"{target_part} ({organ_group}): It {role}."
    distractors = [
        f"Testa (seed coat): It protects the embryo inside dry river soil.",
        f"Radicle (root): It absorbs mineral salts from the air.",
        f"Plumule (shoot): It stores glycogen for muscle contractions.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify the indicated floral structure:\n"
        f"- Coordinates ({px}, {py}) locate the **{target_part}**.\n"
        f"- Belongs to the {organ_group}.\n"
        f"- Function: {role}.\n\n"
        f"**Step 2:** The matching answer is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_25_{rng.randint(100000, 999999)}",
        "subskill": "25_flower_dissection_morphology_diagram",
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
            "tier_1": f"Look at where the target circle is positioned: top of pistil is stigma, side stalk is anther, bottom swollen base is ovary.",
            "tier_2": f"The target part is {target_part}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["flower_diagram_part_misidentification"],
    }
