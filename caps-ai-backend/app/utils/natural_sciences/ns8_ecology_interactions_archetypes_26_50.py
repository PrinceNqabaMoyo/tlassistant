"""Grade 8 Natural Sciences: Term 1 - Interactions and Interdependence (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 1/02. Interactions and interdependence within the environment.md.
Focus: Carrying capacity, population sampling, balance in ecosystems, natural & human disruptions, poaching, invasive alien species, pollution, bioaccumulation, and South African conservation.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Carrying capacity and limiting factors in ecosystems (with dynamic SVG)
def arch_26_carrying_capacity_and_limiting_factors_in_ecosystems(rng: random.Random) -> Dict[str, Any]:
    k_val = rng.randint(320, 420)
    animal = rng.choice(["Cape Mountain Zebra", "Blesbok population", "Impala herd"])
    curve_color = rng.choice(["#2563eb", "#059669", "#7c3aed"])

    # S-curve path: starts at 180, rises, levels off at carrying capacity y=70 (k_val)
    svg = (
        f'<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="210" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Logistic Growth: Carrying Capacity (K = {k_val})</text>'
        f'<line x1="50" y1="180" x2="390" y2="180" stroke="#64748b" stroke-width="2" />'
        f'<line x1="50" y1="180" x2="50" y2="40" stroke="#64748b" stroke-width="2" />'
        f'<line x1="50" y1="70" x2="390" y2="70" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="5,3" />'
        f'<text x="320" y="62" font-size="10" fill="#dc2626" font-weight="bold">Carrying Capacity (K = {k_val})</text>'
        f'<path d="M 50 175 Q 150 175 200 110 T 380 70" fill="none" stroke="{curve_color}" stroke-width="2.5" />'
        f'<text x="220" y="202" font-size="11" fill="#475569" text-anchor="middle">Time (Years)</text>'
        f'<text x="20" y="110" font-size="11" fill="#475569" transform="rotate(-90 20,110)" text-anchor="middle">Population Size</text>'
        f'</svg>'
    )

    prompt = (
        f"In a private nature reserve in the Eastern Cape, a {animal} increases rapidly at first, "
        f"but over several years its growth levels off and fluctuates gently around an upper limit of approximately {k_val} individuals.\n\n"
        f"What ecological concept defines this maximum population size that a specific habitat can sustainably support over time?"
    )
    correct = "The carrying capacity (K) of the ecosystem"
    options = [
        correct,
        "The absolute extinction boundary",
        "The minimum viable embryo mass",
        "The atmospheric solar constant",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define carrying capacity:\n"
        f"- Carrying capacity (K) is the maximum population size of a biological species that an environment can sustain indefinitely, given the food, habitat, water, and other necessities available in the environment.\n"
        f"- When population approaches K ({k_val} individuals), environmental resistance (competition, food scarcity, disease) slows population growth to zero, producing a logistic S-shaped curve.\n\n"
        f"**Step 2:** The concept is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_26_{rng.randint(100000, 999999)}",
        "subskill": "26_carrying_capacity_and_limiting_factors_in_ecosystems",
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
            "tier_1": "What do ecologists call the maximum number of animals a game reserve can feed?",
            "tier_2": "It is called the carrying capacity (K).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["carrying_capacity_definition_misconception"],
    }


# 27. Population growth parameters natality mortality migration
def arch_27_population_growth_parameters_natality_mortality_migration(rng: random.Random) -> Dict[str, Any]:
    births = rng.randint(45, 60)
    deaths = rng.randint(15, 25)
    immigration = rng.randint(10, 18)
    emigration = rng.randint(5, 12)
    net_growth = (births + immigration) - (deaths + emigration)

    prompt = (
        f"A wildlife reserve monitors a herd of springbok over one calendar year and records the following parameters:\n"
        f"- Births (natality): +{births}\n"
        f"- Deaths (mortality): -{deaths}\n"
        f"- Immigration (animals joining herd): +{immigration}\n"
        f"- Emigration (animals leaving herd): -{emigration}\n\n"
        f"What was the overall population change for this herd over the year, and which formula governs this calculation?"
    )
    correct = (
        f"Net change = +{net_growth} individuals, calculated using the formula: "
        f"Population Change = (Births + Immigration) - (Deaths + Emigration)"
    )
    options = [
        correct,
        f"Net change = +{births * deaths} individuals, calculated by multiplying births and deaths together.",
        f"Net change = -{deaths + emigration} individuals, ignoring all newborn births entirely.",
        "Net change cannot be determined because wild animal numbers are purely random magic.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Apply the demographic growth equation:\n"
        f"- Population Change = (Natality + Immigration) - (Mortality + Emigration)\n"
        f"- Inputs = {births} + {immigration} = {births + immigration}\n"
        f"- Outputs = {deaths} + {emigration} = {deaths + emigration}\n"
        f"- Net Change = {births + immigration} - {deaths + emigration} = **+{net_growth}**.\n\n"
        f"**Step 2:** The result and formula: **{correct}**."
    )
    return {
        "id": f"ns8_eco_27_{rng.randint(100000, 999999)}",
        "subskill": "27_population_growth_parameters_natality_mortality_migration",
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
            "tier_1": "Add the additions (births + immigration) and subtract the losses (deaths + emigration).",
            "tier_2": f"({births} + {immigration}) - ({deaths} + {emigration}) = +{net_growth}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["population_growth_formula_misconception"],
    }


# 28. Estimating population size quadrat sampling method
def arch_28_estimating_population_size_quadrat_sampling_method(rng: random.Random) -> Dict[str, Any]:
    quadrat_area = 1  # 1 m^2
    counts = [rng.randint(3, 7) for _ in range(5)]
    avg_count = sum(counts) / len(counts)
    field_area = rng.choice([200, 500, 1000])
    total_est = int(avg_count * field_area)
    flower = rng.choice(["indigenous Barberton daisies (*Gerbera jamesonii*)", "wild rooibos shrubs", "succulent *Crassula* plants"])

    prompt = (
        f"A botanist estimates the population of {flower} in a {field_area} m^2 grassland field. "
        f"Five random 1 m^2 quadrats are sampled, yielding plant counts of: {counts[0]}, {counts[1]}, {counts[2]}, {counts[3]}, and {counts[4]}.\n\n"
        f"What is the estimated total population of {flower} in the {field_area} m^2 field?"
    )
    correct = f"Approximately {total_est} plants (average density of {avg_count:.1f} plants/m^2 multiplied by {field_area} m^2)"
    options = [
        correct,
        f"Exactly {sum(counts)} plants, because plants only exist inside the 5 sampled quadrats.",
        f"Approximately {total_est * 10} plants, assuming every square metre contains 50 plants.",
        "Zero plants, because quadrats destroy all vegetation within 10 kilometres.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Calculate mean quadrat density:\n"
        f"- Total counted in 5 quadrats = {sum(counts)} plants.\n"
        f"- Mean density = {sum(counts)} / 5 = {avg_count:.1f} plants per m^2.\n\n"
        f"**Step 2:** Scale up to total field area:\n"
        f"- Total Population = Mean density * Total Area = {avg_count:.1f} * {field_area} = **{total_est} plants**.\n\n"
        f"**Step 3:** The answer is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_28_{rng.randint(100000, 999999)}",
        "subskill": "28_estimating_population_size_quadrat_sampling_method",
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
            "tier_1": "Find the average number of plants in 1 quadrat, then multiply by the total field area.",
            "tier_2": f"Average is {avg_count:.1f}. Multiply by {field_area} m^2.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["quadrat_sampling_calculation_misconception"],
    }


# 29. Estimating population size mark recapture Lincoln index (with dynamic SVG)
def arch_29_estimating_population_size_mark_recapture_lincoln_index(rng: random.Random) -> Dict[str, Any]:
    # M = marked in sample 1, C = caught in sample 2, R = marked in sample 2
    # N = (M * C) / R
    R = rng.choice([4, 5, 6])
    M = R * rng.choice([8, 10, 12])
    C = R * rng.choice([6, 8, 10])
    N_est = (M * C) // R
    species = rng.choice(["African marsh terrapins in a wetland", "striped field mice in a fynbos valley", "bream fish in a farm dam"])

    svg = (
        f'<svg viewBox="0 0 420 190" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="210" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Lincoln-Petersen Mark-Recapture Method</text>'
        f'<rect x="30" y="50" width="160" height="70" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5" rx="4" />'
        f'<text x="110" y="75" font-size="11" fill="#15803d" font-weight="bold" text-anchor="middle">Sample 1 (Marked)</text>'
        f'<text x="110" y="100" font-size="13" fill="#14532d" font-weight="bold" text-anchor="middle">M = {M}</text>'
        f'<rect x="230" y="50" width="160" height="70" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5" rx="4" />'
        f'<text x="310" y="75" font-size="11" fill="#1d4ed8" font-weight="bold" text-anchor="middle">Sample 2 (Recaptured)</text>'
        f'<text x="310" y="100" font-size="13" fill="#1e3a8a" font-weight="bold" text-anchor="middle">Total (C) = {C} | Marked (R) = {R}</text>'
        f'<text x="210" y="150" font-size="11" fill="#7c3aed" font-weight="bold" text-anchor="middle">Estimated Population: N = (M \u00d7 C) / R = {N_est}</text>'
        f'<text x="210" y="175" font-size="10" fill="#64748b" text-anchor="middle">Assumes closed population and mark does not harm the organism</text>'
        f'</svg>'
    )

    prompt = (
        f"An ecologist uses the Lincoln-Petersen mark-recapture technique to estimate the population of {species}:\n"
        f"- Sample 1: {M} individuals are captured, marked with harmless biological tags, and released.\n"
        f"- Sample 2 (one week later): {C} individuals are captured, of which {R} carry the original mark.\n\n"
        f"Using the Lincoln index formula: $N = \\frac{{M \\times C}}{{R}}$, what is the estimated total population size?"
    )
    correct = f"{N_est} individuals"
    wrong_1 = (M + C) - R
    wrong_2 = (M * C)
    wrong_3 = N_est // 2
    options = [
        correct,
        f"{wrong_1} individuals",
        f"{wrong_2} individuals",
        f"{wrong_3} individuals",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Apply the Lincoln-Petersen formula:\n"
        f"$$N = \\frac{{M \\times C}}{{R}}$$\n"
        f"Where:\n"
        f"- $M = {M}$ (number marked in 1st sample)\n"
        f"- $C = {C}$ (total caught in 2nd sample)\n"
        f"- $R = {R}$ (recaptured marked individuals in 2nd sample)\n\n"
        f"**Step 2:** Calculate:\n"
        f"$$N = \\frac{{{M} \\times {C}}}{{{R}}} = \\frac{{{M * C}}}{{{R}}} = **{N_est}**$$\n\n"
        f"**Step 3:** The estimated population is **{correct}**."
    )
    return {
        "id": f"ns8_eco_29_{rng.randint(100000, 999999)}",
        "subskill": "29_estimating_population_size_mark_recapture_lincoln_index",
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
            "tier_1": f"Multiply {M} by {C}, then divide by {R}.",
            "tier_2": f"({M} * {C}) / {R} = {N_est}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["lincoln_index_formula_misconception"],
    }


# 30. Ecosystem balance dynamic equilibrium concept
def arch_30_ecosystem_balance_dynamic_equilibrium_concept(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In an undisturbed natural savanna ecosystem, populations of grasses, antelopes, and predators fluctuate "
        f"from season to season, yet the overall community structure remains stable over centuries.\n\n"
        f"What ecological term describes this self-regulating state of balance in a healthy ecosystem?"
    )
    correct = "Dynamic equilibrium (ecosystem balance)"
    options = [
        correct,
        "Static eternal freezing",
        "Total abiotic extinction",
        "Permanent artificial monoculture",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand ecological balance:\n"
        f"- Ecosystems are not frozen or rigid ('static'); birth, death, predation, and climate oscillate constantly.\n"
        f"- However, negative feedback loops (predator-prey relationships, nutrient recycling, carrying capacity) return populations toward balance.\n"
        f"- This state of fluctuating stability is called **dynamic equilibrium**.\n\n"
        f"**Step 2:** The term is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_30_{rng.randint(100000, 999999)}",
        "subskill": "30_ecosystem_balance_dynamic_equilibrium_concept",
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
            "tier_1": "What kind of equilibrium is active and fluctuating, not stationary?",
            "tier_2": "It is called dynamic equilibrium.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["dynamic_equilibrium_concept_misconception"],
    }


# 31. Impact of removing top predator trophic cascade
def arch_31_impact_of_removing_top_predator_trophic_cascade(rng: random.Random) -> Dict[str, Any]:
    predator_case = rng.choice([
        ("the eradication of apex predators like lions and leopards from a game reserve", "herbivorous antelopes overpopulate, overgraze grass and shrubs, leading to severe soil erosion and starvation"),
        ("the historical extermination of wolves from Yellowstone National Park", "deer and elk numbers exploded, destroying riverbank willow trees and wiping out beavers and songbirds"),
    ])
    prompt = (
        f"Ecological studies show that {predator_case[0]} leads to a catastrophic chain reaction known as a **trophic cascade**: {predator_case[1]}.\n\n"
        f"Why are apex predators essential for maintaining biodiversity and ecosystem health?"
    )
    correct = (
        "Apex predators control the population size and grazing behavior of herbivores, "
        "preventing overgrazing and protecting the plant foundation that supports all other organisms."
    )
    options = [
        correct,
        "Apex predators pollinate flowering trees by carrying pollen in their teeth.",
        "Apex predators produce rainfall by roaring loudly at thunder clouds.",
        "Apex predators manufacture glucose in their fur using radiant sunlight.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the top-down regulation of ecosystems:\n"
        f"- Top predators exert top-down control over herbivore numbers.\n"
        f"- Removing top carnivores releases herbivores from predation pressure ('mesopredator/herbivore release').\n"
        f"- Herbivore overpopulation strips vegetation, degrading soils and crashing wider community biodiversity.\n\n"
        f"**Step 2:** The ecological role is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_31_{rng.randint(100000, 999999)}",
        "subskill": "31_impact_of_removing_top_predator_trophic_cascade",
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
            "tier_1": "What happens to herbivore numbers when there are no carnivores to hunt them?",
            "tier_2": "Herbivores overpopulate and overgraze the plants, causing ecosystem collapse.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["top_predator_keystone_role_misconception"],
    }


# 32. Impact of removing keystone producer or pollinator
def arch_32_impact_of_removing_keystone_producer_or_pollinator(rng: random.Random) -> Dict[str, Any]:
    keystone = rng.choice([
        ("honeybees (*Apis mellifera*) as generalist pollinators", "hundreds of indigenous flowering plants fail to set seeds, causing plant populations and dependent fruit-eating birds to collapse"),
        ("fig trees (*Ficus*) that bear fruit continuously throughout the dry season", "monkeys, bats, and frugivorous birds starve during months when all other trees have no fruit"),
    ])
    prompt = (
        f"In conservation biology, certain species are designated **keystone species**. "
        f"For example, if {keystone[0]} are eliminated, {keystone[1]}.\n\n"
        f"What is the defining ecological characteristic of a **keystone species**?"
    )
    correct = (
        "A species that exerts a disproportionately large impact on its natural environment "
        "relative to its abundance, such that its removal causes ecosystem collapse."
    )
    options = [
        correct,
        "A species carved out of solid stone that sits at the gate of national parks.",
        "A species with the exact highest number of individual organisms on Earth.",
        "A species that does not interact with any other living organism in any way.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define a keystone species:\n"
        f"- Just as the central keystone holds an archway together, a keystone species holds an ecosystem's structure together.\n"
        f"- Its impact on community diversity and stability is extraordinarily large relative to its population biomass.\n"
        f"- Loss of {keystone[0]} triggers cascading extinctions across multiple trophic levels.\n\n"
        f"**Step 2:** The definition is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_32_{rng.randint(100000, 999999)}",
        "subskill": "32_impact_of_removing_keystone_producer_or_pollinator",
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
            "tier_1": "Does a keystone species have a small or huge impact on its ecosystem?",
            "tier_2": "It has a disproportionately large impact relative to its numbers.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["keystone_species_definition_misconception"],
    }


# 33. Natural disruptions prolonged drought impact
def arch_33_natural_disruptions_prolonged_drought_impact(rng: random.Random) -> Dict[str, Any]:
    years = rng.choice([3, 4, 5])
    region = rng.choice(["the Karoo semi-desert", "the Limpopo savanna basin", "the Zululand thornveld"])
    prompt = (
        f"A multi-year drought strikes {region} for {years} consecutive years. "
        f"Rivers dry into isolated mud pools, grass biomass drops by 80%, and herbivore mortality surges.\n\n"
        f"How does a severe natural drought disrupt the trophic balance of an ecosystem?"
    )
    correct = (
        "Lack of water drasticaly curtails primary producer plant growth; with less plant biomass, "
        "carrying capacity crashes, starving primary consumers and subsequently starving secondary carnivores."
    )
    options = [
        correct,
        "Drought causes all animals to turn into aquatic fish that swim inside underground rocks.",
        "Drought causes plants to photosynthesise 10 times faster using dry dust instead of water.",
        "Drought produces freezing blizzards that bury all trees in 50 metres of snow.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace the ecological impact of drought:\n"
        f"- Water is a core abiotic requirement for plant photosynthesis and cell turgor.\n"
        f"- Water scarcity -> primary productivity collapses (bottom-up limitation).\n"
        f"- Herbivore populations crash from dehydration and starvation.\n"
        f"- Carnivores temporarily feast on dead carcasses (scavenging), then crash as prey numbers dwindle.\n\n"
        f"**Step 2:** The mechanism is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_33_{rng.randint(100000, 999999)}",
        "subskill": "33_natural_disruptions_prolonged_drought_impact",
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
            "tier_1": "What happens to the base of the food chain (plants) when there is no rain?",
            "tier_2": "Plants cannot photosynthesise without water, starving all consumer levels above them.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["drought_ecosystem_cascade_misconception"],
    }


# 34. Natural disruptions flooding and soil loss
def arch_34_natural_disruptions_flooding_and_soil_loss(rng: random.Random) -> Dict[str, Any]:
    river_basin = rng.choice(["the Tugela River basin in KwaZulu-Natal", "the Orange River floodplains in the Northern Cape"])
    prompt = (
        f"Catastrophic flash flooding along {river_basin} washes away millions of tons of topsoil, "
        f"uprooting riparian vegetation and submerging animal habitats.\n\n"
        f"Why is the loss of **topsoil** during severe flooding such a long-term setback for ecological recovery?"
    )
    correct = (
        "Topsoil contains the vast majority of organic humus, seed banks, and essential mineral nutrients; "
        "once washed away, soil formation takes hundreds to thousands of years to regenerate."
    )
    options = [
        correct,
        "Because topsoil is made of pure diamonds that animals use to purchase food.",
        "Because plants can only grow on solid concrete foundations once flooded.",
        "Because flooding reverses the Earth's gravity in the affected river valleys.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the ecological value of topsoil:\n"
        f"- The top horizon (A-horizon) contains weathered minerals, mycorrhizal fungi, nitrogen-fixing bacteria, and rich organic humus.\n"
        f"- It takes centuries of biological weathering to generate just a few centimetres of topsoil.\n"
        f"- Washing it into rivers strips the substrate of nutrients, leaving bare subsoil/bedrock where vegetation struggle to re-establish.\n\n"
        f"**Step 2:** The reason is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_34_{rng.randint(100000, 999999)}",
        "subskill": "34_natural_disruptions_flooding_and_soil_loss",
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
            "tier_1": "How long does it take for nature to create new fertile soil?",
            "tier_2": "Soil formation takes centuries; losing topsoil strips the nutrients needed for plant regrowth.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["topsoil_loss_recovery_misconception"],
    }


# 35. Natural disruptions veldfires and fynbos regeneration
def arch_35_natural_disruptions_veldfires_and_fynbos_regeneration(rng: random.Random) -> Dict[str, Any]:
    plant_adaptation = rng.choice([
        ("serotiny in king proteas (*Protea cynaroides*)", "seeds are stored inside fire-proof cones and released only after smoke and heat melt the protective resin"),
        ("geophytes (e.g. fire lilies *Cyrtanthus ventricosus*)", "underground bulbs survive the blaze and burst into flower within days after fire clears the canopy"),
    ])
    prompt = (
        f"In the Cape Floral Kingdom (Fynbos biome), periodic veldfires occur naturally every 10 to 15 years. "
        f"Plants display remarkable adaptations, such as {plant_adaptation[0]}: {plant_adaptation[1]}.\n\n"
        f"Why are natural periodic fires considered a vital ecological requirement rather than a destructive disaster in the Fynbos biome?"
    )
    correct = (
        "Fire clears old overgrown vegetation, returns locked nutrients to the soil in ash, "
        "and provides the essential heat and chemical smoke cues needed to stimulate seed germination and regeneration."
    )
    options = [
        correct,
        "Fire burns all soil into pure glass so that alien trees cannot grow roots.",
        "Fire freezes the mountain slopes so that snow leopards can colonize South Africa.",
        "Fire forces plants to undergo sexual reproduction with passing ocean birds.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand fire ecology in fire-prone ecosystems:\n"
        f"- Fynbos is a fire-dependent Mediterranean-climate ecosystem.\n"
        f"- Without fire (fire suppression), fynbos becomes senescent (moribund), woody species dominate, and biodiversity crashes.\n"
        f"- Smoke chemicals (butenolides) and heat trigger germination of dormant seed banks in the soil.\n\n"
        f"**Step 2:** The ecological value is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_35_{rng.randint(100000, 999999)}",
        "subskill": "35_natural_disruptions_veldfires_and_fynbos_regeneration",
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
            "tier_1": "Do fynbos plants need fire to release seeds and clear the canopy?",
            "tier_2": "Periodic fires stimulate seed germination, clear competition, and recycle nutrients in ash.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fynbos_fire_ecology_misconception"],
    }


# 36. Human impact habitat destruction and fragmentation
def arch_36_human_impact_habitat_destruction_and_fragmentation(rng: random.Random) -> Dict[str, Any]:
    developments = [
        ("construction of a 6-lane fenced national highway through an indigenous forest", "splits animal populations into two isolated subpopulations that cannot cross"),
        ("clearing natural renosterveld shrubland for residential housing estates", "reduces continuous natural habitat into tiny disconnected vegetation islands surrounded by urban concrete"),
    ]
    project, impact = rng.choice(developments)
    prompt = (
        f"Human development often causes **habitat fragmentation**, as seen when {project} ({impact}).\n\n"
        f"What serious biological danger does habitat fragmentation create for wildlife populations?"
    )
    correct = (
        "It prevents natural animal migration, restricts gene flow (leading to dangerous inbreeding in small isolated groups), "
        "and increases vulnerability to local extinction from disease or edge effects."
    )
    options = [
        correct,
        "It causes animals to learn human speech and take over municipal government offices.",
        "It transforms wild mammals into photosynthetic trees within three generations.",
        "It makes all animals permanently immune to all predators and diseases.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze habitat fragmentation:\n"
        f"- Habitat destruction reduces total available living area.\n"
        f"- Fragmentation breaks large continuous populations into tiny, isolated subpopulations.\n"
        f"- Consequences: inbreeding depression, genetic drift, inability to find mates or forage across seasonal ranges, and vulnerability to catastrophic wipeout.\n\n"
        f"**Step 2:** The primary danger is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_36_{rng.randint(100000, 999999)}",
        "subskill": "36_human_impact_habitat_destruction_and_fragmentation",
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
            "tier_1": "What happens when animals are trapped in small isolated patches with fences?",
            "tier_2": "Isolated groups suffer from inbreeding and cannot migrate to find food or mates.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["habitat_fragmentation_consequences_misconception"],
    }


# 37. Human impact poaching and illegal wildlife trade
def arch_37_human_impact_poaching_and_illegal_wildlife_trade(rng: random.Random) -> Dict[str, Any]:
    species = [
        ("pangolins (*Smutsia temminckii*)", "poached illegally for their keratin scales and meat in transnational trafficking"),
        ("succulent plants (e.g. dwarf *Conophytum* species in the succulent Karoo)", "illegally uprooted from wild rock crevices for illicit international collectors"),
        ("abalone / perlemoen (*Haliotis midae*)", "poached by organized syndicates along the rocky South African coastline"),
    ]
    animal, trade_desc = rng.choice(species)
    prompt = (
        f"In South Africa, {animal} are {trade_desc}.\n\n"
        f"What is the ecological impact of unsustainable commercial poaching on wild biodiversity?"
    )
    correct = (
        "It causes rapid population collapse far faster than natural reproduction rates can replenish, "
        "pushing species toward critical endangerment and extinction while destabilizing community food webs."
    )
    options = [
        correct,
        "It forces the poached species to mutate and reproduce asexually inside caves.",
        "It causes the species to triple its birth rate and conquer city centres.",
        "Poaching has zero ecological effect because wild populations are infinitely large.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze commercial poaching:\n"
        f"- Driven by black market demand, poaching targets specific species at unsustainable extraction velocities.\n"
        f"- For slow-reproducing species like {animal[0]}, harvesting exceeds reproductive replacement rate.\n"
        f"- The removal of vital ecosystem engineers or grazers undermines community ecological integrity.\n\n"
        f"**Step 2:** The ecological impact is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_37_{rng.randint(100000, 999999)}",
        "subskill": "37_human_impact_poaching_and_illegal_wildlife_trade",
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
            "tier_1": "Can wild populations survive when hunted faster than they can breed?",
            "tier_2": "Poaching drives species toward extinction and destabilizes ecosystems.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["poaching_ecological_impact_misconception"],
    }


# 38. Human impact rhino and elephant conservation crisis
def arch_38_human_impact_rhino_and_elephant_conservation_crisis(rng: random.Random) -> Dict[str, Any]:
    crisis = rng.choice([
        ("white and black rhinos (*Ceratotherium simum* and *Diceros bicornis*)", "horn composed of compacted keratin (the same protein as human fingernails)", "false traditional beliefs about medicinal and status value in East Asia"),
        ("African savanna elephants (*Loxodonta africana*)", "tusks composed of ivory (extended incisor teeth)", "illegal international demand for carved ivory ornaments and trinkets"),
    ])
    prompt = (
        f"South Africa faces an intensive conservation crisis protecting {crisis[0]}. "
        f"These animals are killed illegally for their {crisis[1]}, fueled by {crisis[2]}.\n\n"
        f"Which multi-faceted conservation strategy is actively used in South Africa to protect these endangered megaherbivores?"
    )
    correct = (
        "Armed anti-poaching field ranger patrols, satellite and drone surveillance, DNA forensic profiling (RhODIS), "
        "community engagement, and strict legal prosecution of trafficking syndicates."
    )
    options = [
        correct,
        "Spraying national parks with toxic nerve gas to kill all living animals permanently.",
        "Relocating all wild rhinos into domestic swimming pools in residential suburbs.",
        "Allowing unrestricted hunting by poachers so the animals learn to fight back with weapons.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Detail modern conservation methodologies for megaherbivores:\n"
        f"- Combating poaching requires a multi-pronged approach:\n"
        f"  1. Boots on the ground: dedicated armed ranger patrols with tracking dogs.\n"
        f"  2. High-tech monitoring: infrared drone surveillance and satellite tracking.\n"
        f"  3. Forensic science: South Africa's RhODIS DNA database linking seized horns to poached carcasses.\n"
        f"  4. Community partnerships and demand-reduction international campaigns.\n\n"
        f"**Step 2:** The active strategy is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_38_{rng.randint(100000, 999999)}",
        "subskill": "38_human_impact_rhino_and_elephant_conservation_crisis",
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
            "tier_1": "What methods do South African national parks use to stop rhino poachers?",
            "tier_2": "Rangers, drones, DNA forensics, and strict legal protection.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["rhino_elephant_conservation_strategy_misconception"],
    }


# 39. Invasive alien species water hyacinth aquatic choking
def arch_39_invasive_alien_species_water_hyacinth_aquatic_choking(rng: random.Random) -> Dict[str, Any]:
    water_body = rng.choice(["Hartbeespoort Dam in North West", "Roodeplaat Dam in Gauteng", "the Vaal River system"])
    prompt = (
        f"The South American **water hyacinth** (*Pontederia crassipes*) has invaded {water_body}, "
        f"multiplying into dense, impenetrable green mats covering the water surface.\n\n"
        f"What ecological damage does an invasive water hyacinth infestation inflict on an aquatic ecosystem?"
    )
    correct = (
        "It blocks sunlight from reaching submerged indigenous water plants (halting photosynthesis), "
        "depletes dissolved oxygen when rotting matter decomposes, causing mass fish suffocations and water stagnation."
    )
    options = [
        correct,
        "It drinks all the water within 2 hours, turning the dam into a dry sandy desert.",
        "It produces high-voltage electricity that electrocutes all passing motorboats.",
        "It transforms freshwater into boiling mineral oil.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the ecological consequences of water hyacinth invasion:\n"
        f"- Water hyacinth forms thick floating carpets that block 95% of sunlight -> submerged plants die.\n"
        f"- Decaying weed biomass is broken down by aerobic decomposer bacteria, which consume all dissolved oxygen in the water (anoxia).\n"
        f"- Fish, amphibians, and invertebrates die of asphyxiation.\n\n"
        f"**Step 2:** The ecological damage is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_39_{rng.randint(100000, 999999)}",
        "subskill": "39_invasive_alien_species_water_hyacinth_aquatic_choking",
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
            "tier_1": "What happens to underwater life when floating weeds block all sunlight and rot in the water?",
            "tier_2": "Sunlight is blocked and oxygen is depleted, killing fish and native plants.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["water_hyacinth_ecological_impact_misconception"],
    }


# 40. Invasive alien species black wattle water depletion
def arch_40_invasive_alien_species_black_wattle_water_depletion(rng: random.Random) -> Dict[str, Any]:
    alien_tree = rng.choice([
        ("black wattle (*Acacia mearnsii*)", "an invasive Australian tree", "riparian river catchments of Mpumalanga and KwaZulu-Natal"),
        ("blue gum (*Eucalyptus*)", "an introduced Australian timber species", "fynbos water catchment mountains of the Western Cape"),
        ("pine trees (*Pinus pinaster*)", "an introduced European softwood species", "fynbos mountain catchment slopes"),
    ])
    prompt = (
        f"In South African water catchment areas, invasive alien trees like {alien_tree[0]} ({alien_tree[1]}) "
        f"form dense stands across {alien_tree[2]}.\n\n"
        f"Why are these invasive woody plants such a critical threat to South Africa's national water security and biodiversity?"
    )
    correct = (
        "They consume vastly more groundwater and streamflow than indigenous vegetation (drying up rivers and wetlands), "
        "fuel unnaturally intense veldfires, and outcompete indigenous biodiversity."
    )
    options = [
        correct,
        "They release carbon monoxide gas that causes rain clouds to dissolve into space.",
        "They transform indigenous animals into domestic sheep within 5 days.",
        "They freeze groundwater into solid ice during summer heatwaves.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze invasive alien trees and water depletion:\n"
        f"- Indigenous fynbos and grasslands have low transpiration rates adapted to water scarcity.\n"
        f"- Invasive trees ({alien_tree[0]}) have massive root systems with high transpiration rates, guzzling billions of litres of water per year.\n"
        f"- The South African government launched the 'Working for Water' programme to clear these invasives to restore streamflow and native biodiversity.\n\n"
        f"**Step 2:** The primary threat is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_40_{rng.randint(100000, 999999)}",
        "subskill": "40_invasive_alien_species_black_wattle_water_depletion",
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
            "tier_1": "How do deep-rooted Australian wattle and gum trees affect South African river levels?",
            "tier_2": "They consume enormous amounts of water, drying up streams and outcompeting native plants.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["invasive_trees_water_consumption_misconception"],
    }


# 41. Biological control of invasive species agent selection
def arch_41_biological_control_of_invasive_species_agent_selection(rng: random.Random) -> Dict[str, Any]:
    biocontrol = rng.choice([
        ("water hyacinth (*Pontederia crassipes*)", "the water hyacinth weevil (*Neochetina eichhorniae*)", "feeds strictly on water hyacinth petioles and leaves"),
        ("prickly pear (*Opuntia ficus-indica*)", "cochineal scale insects (*Dactylopius opuntiae*)", "sucks the sap of prickly pear cactus pads causing them to collapse"),
        ("sesbania weed (*Sesbania punicea*)", "the sesbania stem-boring weevil (*Trichapion lativentre*)", "lays eggs into the flower buds, destroying seed production"),
    ])
    weed, insect, feeding_action = rng.choice([biocontrol])
    prompt = (
        f"To control invasive {weed} without relying on hazardous synthetic chemicals, "
        f"South African entomologists introduced a specialized natural enemy: {insect} ({feeding_action}).\n\n"
        f"What is this ecological pest management method called, and what critical safety requirement must be met before introducing the insect?"
    )
    correct = (
        "**Biological control (biocontrol)**; the biocontrol agent must be strictly **host-specific**, "
        "meaning it can feed and reproduce only on the target alien weed and will never attack indigenous plants or agricultural crops."
    )
    options = [
        correct,
        "Chemical warfare; the insect must be dipped in radioactive plutonium before release.",
        "Mechanical deforestation; the insect must be trained to operate chainsaws.",
        "Artificial hybridization; the insect must mate with human livestock to create new species.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define biological control and host-specificity testing:\n"
        f"- Biological control utilizes a pest's natural co-evolved enemies (insects, mites, fungi) to reduce its population to non-damaging levels.\n"
        f"- Strict quarantine testing ensures **host-specificity**: if the target weed dies, the biocontrol insect starves rather than switching to indigenous flora or crops.\n\n"
        f"**Step 2:** The method and safety criterion: **{correct}**."
    )
    return {
        "id": f"ns8_eco_41_{rng.randint(100000, 999999)}",
        "subskill": "41_biological_control_of_invasive_species_agent_selection",
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
            "tier_1": "What is it called when you use one living organism to control another?",
            "tier_2": "It is biological control, and the agent must be strictly host-specific.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["biocontrol_host_specificity_misconception"],
    }


# 42. Chemical vs mechanical clearing of invasive plants
def arch_42_chemical_vs_mechanical_clearing_of_invasive_plants(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When land managers eradicate woody invasive alien trees (such as black wattle or rooikrans), "
        f"they compare **mechanical clearing** (cutting stems with hand saws or chainsaws) and "
        f"**chemical control** (applying registered herbicide to cut stumps).\n\n"
        f"Why is spraying widespread aerial chemical herbicide generally discouraged near natural waterways?"
    )
    correct = (
        "Chemical herbicides can run off into water bodies, poisoning aquatic organisms (fish and amphibians), "
        "killing non-target indigenous riverside flora, and contaminating drinking water supplies."
    )
    options = [
        correct,
        "Because water dissolves herbicide into nutritious orange fruit juice.",
        "Because herbicides cause rivers to turn into solid granite rocks.",
        "Because aerial herbicide attracts hungry sharks into freshwater dams.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Evaluate chemical vs mechanical weed eradication:\n"
        f"- Mechanical control is labour-intensive but environmentally safe.\n"
        f"- Indiscriminate chemical spraying near rivers risks runoff, water contamination, toxicity to aquatic fauna, and collateral damage to native plants.\n"
        f"- Best practice: integrated control (cut stems mechanically, then precisely paint herbicide onto cut stumps to prevent resprouting without aquatic runoff).\n\n"
        f"**Step 2:** The ecological reason is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_42_{rng.randint(100000, 999999)}",
        "subskill": "42_chemical_vs_mechanical_clearing_of_invasive_plants",
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
            "tier_1": "What happens when toxic weedkiller washes into a river?",
            "tier_2": "It poisons fish, native plants, and human drinking water.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["chemical_herbicide_water_pollution_misconception"],
    }


# 43. Human pollution water eutrophication algal blooms (with dynamic SVG)
def arch_43_human_pollution_water_eutrophication_algal_blooms(rng: random.Random) -> Dict[str, Any]:
    pollutant_source = rng.choice([
        "agricultural chemical fertilizers (rich in nitrates and phosphates) leaching off crop fields",
        "untreated domestic sewage discharge containing detergents and nitrogenous human waste",
    ])
    algae_color = rng.choice(["#15803d", "#16a34a", "#22c55e"])
    nitrate_mg = rng.randint(45, 95)
    bloom_depth = rng.randint(25, 40)

    svg = (
        f'<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="210" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Eutrophication: Nitrate Influx ({nitrate_mg} mg/L)</text>'
        f'<rect x="40" y="50" width="340" height="130" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" rx="4" />'
        f'<rect x="42" y="52" width="336" height="{bloom_depth}" fill="{algae_color}" fill-opacity="0.8" />'
        f'<text x="210" y="72" font-size="11" fill="#ffffff" font-weight="bold" text-anchor="middle">Dense Green Algal Bloom on Surface</text>'
        f'<text x="210" y="115" font-size="10" fill="#dc2626" font-weight="bold" text-anchor="middle">Dead algae decompose -> Bacteria consume all O2</text>'
        f'<text x="210" y="145" font-size="10" fill="#475569" text-anchor="middle">Severe Anoxia (Oxygen Depletion) -> Mass Fish Kill</text>'
        f'<text x="210" y="202" font-size="10" fill="#0f172a" text-anchor="middle">Nitrate/Phosphate runoff triggers algal explosion and ecosystem suffocation</text>'
        f'</svg>'
    )

    prompt = (
        f"When {pollutant_source} enters a freshwater dam, it causes rapid nutrient enrichment known as **eutrophication**. "
        f"Microscopic green algae explode into a thick surface algal bloom. Within weeks, the water smells foul and thousands of fish float dead on the surface.\n\n"
        f"Which sequence correctly outlines the biological mechanism that leads to mass fish deaths during eutrophication?"
    )
    correct = (
        "1. Nutrient overload (nitrates/phosphates) -> 2. Algal bloom covers surface -> 3. Algae die and sink -> "
        "4. Decomposer bacteria multiply rapidly and consume all dissolved oxygen in respiration -> 5. Fish die of suffocation (anoxia)."
    )
    options = [
        correct,
        "1. Fertilizer turns water into ice -> 2. Fish freeze solid -> 3. Birds eat the ice -> 4. Algae grow inside birds.",
        "1. Algae turn into carnivorous sharks -> 2. Sharks eat all freshwater fish -> 3. Sharks walk onto land.",
        "1. Water evaporates immediately -> 2. Fish choke on dry dust -> 3. Algae produce nuclear radiation.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace the 5-step sequence of eutrophication:\n"
        f"1. Inflow of excess nitrates and phosphates.\n"
        f"2. Explosive growth of green surface algae (algal bloom).\n"
        f"3. Sunlight cannot reach lower layers; algae die when nutrients exhaust.\n"
        f"4. Huge populations of aerobic decomposing bacteria decompose dead algal biomass, consuming dissolved $\text{{O}}_2$ via rapid cellular respiration.\n"
        f"5. Water becomes anoxic; fish and aquatic animals suffocate.\n\n"
        f"**Step 2:** The sequence is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_43_{rng.randint(100000, 999999)}",
        "subskill": "43_human_pollution_water_eutrophication_algal_blooms",
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
            "tier_1": "What organism eats the dead algae and uses up all the oxygen in the water?",
            "tier_2": "Decomposing bacteria multiply and use up all the dissolved oxygen, suffocating fish.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["eutrophication_mechanism_misconception"],
    }


# 44. Human pollution plastic accumulation in marine webs
def arch_44_human_pollution_plastic_accumulation_in_marine_webs(rng: random.Random) -> Dict[str, Any]:
    marine_life = [
        ("loggerhead sea turtles (*Caretta caretta*) mistaking floating plastic bags for jellyfish prey", "plastic impaction in the digestive tract causing starvation and bowel obstruction"),
        ("Cape fur seals (*Arctocephalus pusillus*) becoming entangled in discarded plastic monofilament fishing lines", "deep lacerations, restricted movement, and inability to swim or forage"),
        ("filter-feeding sardines and baleen whales ingesting microscopic microplastic fragments", "toxin transfer and mechanical blockage of digestive and respiratory membranes"),
    ]
    animal, injury = rng.choice(marine_life)
    prompt = (
        f"Millions of tons of non-biodegradable synthetic plastic enter the oceans annually. "
        f"Marine surveys off the South African coastline document {animal}, resulting in {injury}.\n\n"
        f"Why does plastic waste pose such a persistent and destructive ecological threat to marine food webs?"
    )
    correct = (
        "Plastics are non-biodegradable, remaining in the environment for hundreds of years; they fragment into toxic microplastics "
        "that are ingested by marine organisms, causing physical blockage, starvation, and chemical toxicity throughout food webs."
    )
    options = [
        correct,
        "Plastics dissolve into liquid gold that makes ocean water too heavy for fish to swim through.",
        "Plastics emit radio waves that force sea turtles to fly into the upper atmosphere.",
        "Plastics turn marine fish into land-dwelling reptiles within 48 hours.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze plastic pollution in marine ecology:\n"
        f"- Synthetic polymers are not recognized or decomposed by natural decomposers (non-biodegradable).\n"
        f"- Mechanical photodegradation breaks larger plastics into microplastics (<5 mm).\n"
        f"- Organisms across all trophic levels (plankton, fish, turtles, seabirds, marine mammals) ingest plastics or become entangled, causing malnutrition, death, and toxin transfer.\n\n"
        f"**Step 2:** The fundamental threat is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_44_{rng.randint(100000, 999999)}",
        "subskill": "44_human_pollution_plastic_accumulation_in_marine_webs",
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
            "tier_1": "Can natural bacteria easily decompose synthetic plastic bottles and bags? No.",
            "tier_2": "Plastics persist for centuries, choking digestive systems and poisoning food webs.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["marine_plastic_pollution_misconception"],
    }


# 45. Human pollution acid mine drainage on the Highveld
def arch_45_human_pollution_acid_mine_drainage_on_the_highveld(rng: random.Random) -> Dict[str, Any]:
    mining_basin = rng.choice([
        "the Witwatersrand gold mining basin in Gauteng",
        "the Mpumalanga coal mining Highveld region",
    ])
    prompt = (
        f"In {mining_basin}, abandoned underground shafts flood with groundwater. "
        f"Pyrite minerals (iron sulfide) react with oxygen and water to produce **Acid Mine Drainage (AMD)**: "
        f"an orange, highly acidic effluent (pH 2 to 3) laden with toxic dissolved heavy metals (arsenic, lead, uranium) "
        f"seeping into local wetlands and streams.\n\n"
        f"What is the devastating ecological impact of Acid Mine Drainage on aquatic ecosystems?"
    )
    correct = (
        "The extreme acidity and dissolved toxic heavy metals eradicate aquatic life (fish, invertebrates, amphibians), "
        "sterilize the water, destroy riverbank vegetation, and render water completely unfit for animal or human consumption."
    )
    options = [
        correct,
        "AMD turns stream water into sparkling fresh spring water with zero minerals.",
        "AMD acts as fertilizer that causes indigenous wetland grasses to turn into solid gold.",
        "AMD cools water to absolute zero so that aquatic animals hibernate happily.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the environmental consequences of Acid Mine Drainage (AMD):\n"
        f"- Reaction: oxidation of iron sulfide ($2\\text{{FeS}}_2$) produces sulfuric acid ($\\text{{H}}_2\\text{{SO}}_4$).\n"
        f"- The low pH (2-3) leaches heavy metals (lead, cadmium, arsenic, uranium) from surrounding rock strata.\n"
        f"- In waterways, extreme acidity denatures cellular enzymes, suffocates fish by precipitating iron hydroxide on gills, and destroys freshwater biodiversity.\n\n"
        f"**Step 2:** The ecological impact is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_45_{rng.randint(100000, 999999)}",
        "subskill": "45_human_pollution_acid_mine_drainage_on_the_highveld",
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
            "tier_1": "Can fish and water plants survive in water as acidic as lemon juice with dissolved toxic metals?",
            "tier_2": "Extreme acidity and toxic heavy metals kill aquatic organisms and sterilize ecosystems.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["acid_mine_drainage_impact_misconception"],
    }


# 46. Bioaccumulation and biomagnification of toxins
def arch_46_bioaccumulation_and_biomagnification_of_toxins(rng: random.Random) -> Dict[str, Any]:
    toxin_case = rng.choice([
        ("the synthetic pesticide DDT used to control malaria mosquitoes", "DDT accumulates in fat tissue and concentrates up the food chain, causing top raptors (like peregrine falcons and fish eagles) to lay eggs with brittle, fragile shells that crack during incubation"),
        ("heavy metal mercury released from coal-fired power stations", "microscopic plankton absorb trace mercury; predatory tuna and sharks end up with mercury concentrations millions of times higher than surrounding seawater"),
    ])
    prompt = (
        f"Consider the environmental phenomenon involving {toxin_case[0]}: {toxin_case[1]}.\n\n"
        f"What is the difference between **bioaccumulation** and **biomagnification** in ecology?"
    )
    correct = (
        "Bioaccumulation is the buildup of a persistent toxin within the tissues of a single individual organism over its lifetime, "
        "whereas biomagnification is the progressive increase in toxin concentration at each successively higher trophic level in a food chain."
    )
    options = [
        correct,
        "Bioaccumulation occurs only in outer space, while biomagnification occurs only inside volcanic lava.",
        "Bioaccumulation cleans toxins from animal bodies, while biomagnification creates brand new vitamins.",
        "There is zero difference; both words refer to how plants manufacture sugar using sunlight.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish bioaccumulation from biomagnification:\n"
        f"- Bioaccumulation: occurs within ONE organism (intake rate > excretion rate of fat-soluble toxin over time).\n"
        f"- Biomagnification: occurs ACROSS the food chain (each predator eats many contaminated prey animals, concentrating the non-degradable chemical at higher trophic levels).\n"
        f"- Apex predators suffer the most severe toxic damage.\n\n"
        f"**Step 2:** The distinction is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_46_{rng.randint(100000, 999999)}",
        "subskill": "46_bioaccumulation_and_biomagnification_of_toxins",
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
            "tier_1": "Which term describes toxin buildup in one individual, and which describes buildup up the food chain?",
            "tier_2": "Bioaccumulation is within an individual; biomagnification is across trophic levels.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["bioaccumulation_vs_biomagnification_misconception"],
    }


# 47. South African conservation Kruger and transfrontier parks
def arch_47_south_african_conservation_kruger_and_transfrontier_parks(rng: random.Random) -> Dict[str, Any]:
    parks = [
        ("the Great Limpopo Transfrontier Park", "links South Africa's Kruger National Park with Limpopo National Park in Mozambique and Gonarezhou National Park in Zimbabwe"),
        ("the Kgalagadi Transfrontier Park", "unites South Africa's Kalahari Gemsbok National Park with Botswana's Gemsbok National Park across an open unfenced desert boundary"),
    ]
    park_name, countries = rng.choice(parks)
    prompt = (
        f"South Africa has pioneered international conservation initiatives such as {park_name}, which {countries}.\n\n"
        f"What is the primary ecological benefit of establishing large **Transfrontier Conservation Areas (Peace Parks)** across national borders?"
    )
    correct = (
        "They drop international boundary fences, restoring ancient seasonal animal migration routes, "
        "expanding contiguous habitat, and promoting genetic exchange across large, resilient populations."
    )
    options = [
        correct,
        "They allow poachers to hunt animals without needing any passports or visas.",
        "They turn wild protected animals into domesticated farm pets for commercial meat sales.",
        "They replace natural vegetation with concrete car parks to generate revenue.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand transfrontier conservation ecology:\n"
        f"- Political borders create artificial ecological barriers with game fences.\n"
        f"- Removing border fences establishes massive interconnected bioregions ({park_name}).\n"
        f"- Animals (elephants, wildebeest, predators) can migrate naturally in response to seasonal rainfall, drought, and grazing availability, reducing local overgrazing and boosting genetic health.\n\n"
        f"**Step 2:** The primary benefit is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_47_{rng.randint(100000, 999999)}",
        "subskill": "47_south_african_conservation_kruger_and_transfrontier_parks",
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
            "tier_1": "What happens when you take down fences between national parks in different countries?",
            "tier_2": "It restores natural migration corridors and expands unbroken habitats.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["transfrontier_conservation_benefits_misconception"],
    }


# 48. Sustainable resource management and ecotourism
def arch_48_sustainable_resource_management_and_ecotourism(rng: random.Random) -> Dict[str, Any]:
    initiatives = [
        ("community-owned wildlife conservancies in rural Limpopo and Mpumalanga", "local communities receive safari tourism revenues, employment as field rangers, and educational bursaries"),
        ("sustainable marine protected areas (MPAs) along the Wild Coast", "designated 'no-take' breeding zones allow fish stocks to recover and replenish adjacent artisanal fishing grounds"),
    ]
    project, benefit = rng.choice(initiatives)
    prompt = (
        f"In South African conservation, sustainable development models such as {project} ({benefit}) "
        f"are increasingly replacing older exclusionary conservation practices.\n\n"
        f"Why is the active economic involvement of **local communities** essential for long-term conservation success?"
    )
    correct = (
        "When local communities derive tangible economic benefits, jobs, and food security from conservation, "
        "they become active custodians and defenders of wildlife, drastically reducing poaching and illegal exploitation."
    )
    options = [
        correct,
        "Local communities can transform all wild animals into plastic electronic toys.",
        "Local involvement allows developers to pave national parks with asphalt highways.",
        "Because wild ecosystems survive better when all humans abandon agriculture forever.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze community-based natural resource management (CBNRM):\n"
        f"- Historical 'fortress conservation' excluded local people, creating conflict and poverty.\n"
        f"- Modern sustainable ecotourism integrates local communities as equal partners.\n"
        f"- When community livelihoods depend directly on intact ecosystems, local people are incentivised to protect biodiversity against poaching and unsustainable exploitation.\n\n"
        f"**Step 2:** The justification is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_48_{rng.randint(100000, 999999)}",
        "subskill": "48_sustainable_resource_management_and_ecotourism",
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
            "tier_1": "Will people protect animals if the animals help bring them jobs and community income?",
            "tier_2": "Economic benefits make local communities active partners in conservation.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["community_conservation_ecotourism_misconception"],
    }


# 49. Ecological footprint and individual conservation actions
def arch_49_ecological_footprint_and_individual_conservation_actions(rng: random.Random) -> Dict[str, Any]:
    actions = [
        ("planting indigenous water-wise flora (like spekboom *Portulacaria afra* and aloes) in gardens", "reduces municipal tap water consumption and provides natural habitat for indigenous birds and pollinators"),
        ("reducing single-use plastic packaging and sorting recyclable paper, glass, and metals", "minimises landfill overflow and stops plastic trash from reaching marine food chains via storm drains"),
        ("switching household lighting to LED bulbs and installing solar water geysers", "lowers household electricity demand from coal-burning power stations, reducing greenhouse gas emissions"),
    ]
    action, consequence = rng.choice(actions)
    prompt = (
        f"An individual's **ecological footprint** measures the amount of environmental land and water area "
        f"required to supply the resources they consume and absorb the waste they produce. "
        f"An action like {action} ({consequence}).\n\n"
        f"What is the primary environmental objective of reducing one's personal ecological footprint?"
    )
    correct = (
        "To ensure that resource consumption and waste generation remain within the Earth's natural regenerative capacity, "
        "conserving ecosystems and biodiversity for future generations."
    )
    options = [
        correct,
        "To force the Earth to stop spinning on its axis during winter months.",
        "To make all wild animals migrate into domestic kitchens for shelter.",
        "To completely eradicate all solar radiation from reaching the planet.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define the ecological footprint concept:\n"
        f"- Human consumption currently exceeds Earth's biocapacity (ecological overshoot).\n"
        f"- Everyday actions (water conservation, recycling, renewable energy, eating lower on the food chain) reduce resource draw.\n"
        f"- Sustainable living balances consumption with the Earth's carrying capacity.\n\n"
        f"**Step 2:** The objective is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_49_{rng.randint(100000, 999999)}",
        "subskill": "49_ecological_footprint_and_individual_conservation_actions",
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
            "tier_1": "What does living sustainably mean for future generations?",
            "tier_2": "Living within Earth's regenerative capacity ensures resources remain for the future.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ecological_footprint_objective_misconception"],
    }


# 50. Synthetic case study ecosystem collapse and recovery
def arch_50_synthetic_case_study_ecosystem_collapse_and_recovery(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("Baviaanskloof Mega-Reserve in the Eastern Cape", "overgrazing by domestic goats destroyed dense spekboom thickets, causing severe soil erosion and water loss; a multi-million rand restoration project replanted millions of spekboom cuttings, successfully restoring groundwater recharge and native wildlife"),
        ("St Lucia Estuary in the iSimangaliso Wetland Park", "dredging and artificial canal diversion starved the estuary of freshwater, increasing salinity and crashing fish nurseries; restoring natural river linkages re-established estuarine ecology, bird life, and fish populations"),
    ])
    location, history = case
    prompt = (
        f"Consider the South African ecological restoration case study of **{location}**: "
        f"{history}.\n\n"
        f"What fundamental ecological principle does this successful habitat rehabilitation demonstrate?"
    )
    correct = (
        "Degraded ecosystems can recover their biodiversity, soil stability, and dynamic equilibrium "
        "when the root causes of degradation are removed and key native plant species are actively restored."
    )
    options = [
        correct,
        "Once an ecosystem suffers any damage, recovery is biologically impossible for 50 billion years.",
        "Restoration requires paving over all natural soil with synthetic rubber tarmac.",
        "Ecosystems recover only when all living animals are replaced with mechanical robotic replicas.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze ecological restoration principles:\n"
        f"- Ecosystems exhibit natural ecological resilience.\n"
        f"- When humans reverse damage (removing invasive alien species, replanting keystone engineer species like spekboom, restoring hydrology), natural succession and dynamic equilibrium can be successfully re-established.\n"
        f"- Case study: {location}.\n\n"
        f"**Step 2:** The fundamental principle is: **{correct}**."
    )
    return {
        "id": f"ns8_eco_50_{rng.randint(100000, 999999)}",
        "subskill": "50_synthetic_case_study_ecosystem_collapse_and_recovery",
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
            "tier_1": "Can damaged ecosystems be restored if humans help replant native plants?",
            "tier_2": "Yes, degraded ecosystems can recover resilience and dynamic equilibrium.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ecosystem_restoration_resilience_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "26_carrying_capacity_and_limiting_factors_in_ecosystems": arch_26_carrying_capacity_and_limiting_factors_in_ecosystems,
    "27_population_growth_parameters_natality_mortality_migration": arch_27_population_growth_parameters_natality_mortality_migration,
    "28_estimating_population_size_quadrat_sampling_method": arch_28_estimating_population_size_quadrat_sampling_method,
    "29_estimating_population_size_mark_recapture_lincoln_index": arch_29_estimating_population_size_mark_recapture_lincoln_index,
    "30_ecosystem_balance_dynamic_equilibrium_concept": arch_30_ecosystem_balance_dynamic_equilibrium_concept,
    "31_impact_of_removing_top_predator_trophic_cascade": arch_31_impact_of_removing_top_predator_trophic_cascade,
    "32_impact_of_removing_keystone_producer_or_pollinator": arch_32_impact_of_removing_keystone_producer_or_pollinator,
    "33_natural_disruptions_prolonged_drought_impact": arch_33_natural_disruptions_prolonged_drought_impact,
    "34_natural_disruptions_flooding_and_soil_loss": arch_34_natural_disruptions_flooding_and_soil_loss,
    "35_natural_disruptions_veldfires_and_fynbos_regeneration": arch_35_natural_disruptions_veldfires_and_fynbos_regeneration,
    "36_human_impact_habitat_destruction_and_fragmentation": arch_36_human_impact_habitat_destruction_and_fragmentation,
    "37_human_impact_poaching_and_illegal_wildlife_trade": arch_37_human_impact_poaching_and_illegal_wildlife_trade,
    "38_human_impact_rhino_and_elephant_conservation_crisis": arch_38_human_impact_rhino_and_elephant_conservation_crisis,
    "39_invasive_alien_species_water_hyacinth_aquatic_choking": arch_39_invasive_alien_species_water_hyacinth_aquatic_choking,
    "40_invasive_alien_species_black_wattle_water_depletion": arch_40_invasive_alien_species_black_wattle_water_depletion,
    "41_biological_control_of_invasive_species_agent_selection": arch_41_biological_control_of_invasive_species_agent_selection,
    "42_chemical_vs_mechanical_clearing_of_invasive_plants": arch_42_chemical_vs_mechanical_clearing_of_invasive_plants,
    "43_human_pollution_water_eutrophication_algal_blooms": arch_43_human_pollution_water_eutrophication_algal_blooms,
    "44_human_pollution_plastic_accumulation_in_marine_webs": arch_44_human_pollution_plastic_accumulation_in_marine_webs,
    "45_human_pollution_acid_mine_drainage_on_the_highveld": arch_45_human_pollution_acid_mine_drainage_on_the_highveld,
    "46_bioaccumulation_and_biomagnification_of_toxins": arch_46_bioaccumulation_and_biomagnification_of_toxins,
    "47_south_african_conservation_kruger_and_transfrontier_parks": arch_47_south_african_conservation_kruger_and_transfrontier_parks,
    "48_sustainable_resource_management_and_ecotourism": arch_48_sustainable_resource_management_and_ecotourism,
    "49_ecological_footprint_and_individual_conservation_actions": arch_49_ecological_footprint_and_individual_conservation_actions,
    "50_synthetic_case_study_ecosystem_collapse_and_recovery": arch_50_synthetic_case_study_ecosystem_collapse_and_recovery,
}
