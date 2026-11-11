"""Grade 7 Natural Sciences: Term 1 - Biodiversity (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/02. Biodiversity.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Biodiversity definition and three levels
def arch_01_biodiversity_definition_and_three_levels(rng: random.Random) -> Dict[str, Any]:
    levels = [
        ("Genetic diversity", "the total variety of inherited genes and alleles present within a single population or species, allowing adaptation to changing conditions"),
        ("Species diversity", "the variety and abundance of different biological species coexisting within a particular habitat or ecological community"),
        ("Ecosystem diversity", "the variety of different habitats, ecological niches, biomes, and biological communities interacting with their abiotic environments across a geographic region"),
    ]
    level_name, description = rng.choice(levels)
    prompt = (
        f"Biodiversity encompasses all living variety on Earth across three hierarchical levels. "
        f"Which level of biodiversity is defined as '{description}'?"
    )
    correct = level_name
    options = [level_name] + [l[0] for l in levels if l[0] != level_name]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review the three levels of biodiversity:\n"
        f"- Genetic diversity: variation in genes within a species.\n"
        f"- Species diversity: variety of species in a region.\n"
        f"- Ecosystem diversity: variety of habitats, biomes, and ecological processes.\n\n"
        f"**Step 2:** The described level is **{level_name}**."
    )
    return {
        "id": f"ns7_bd_01_{rng.randint(100000, 999999)}",
        "subskill": "01_biodiversity_definition_and_three_levels",
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
            "tier_1": "Recall the three scales: genes inside one species, species inside a community, or communities across ecosystems.",
            "tier_2": "Look at whether the definition mentions genes, species variety, or broad ecosystems/biomes.",
            "tier_3": f"The answer is: {level_name}.",
        },
        "misconception_tags": ["biodiversity_level_confusion"],
    }


# 02. South African biodiversity hotspots Cape Floral
def arch_02_south_african_biodiversity_hotspots_cape_floral(rng: random.Random) -> Dict[str, Any]:
    species_count = rng.choice([9000, 9500])
    endemism_pct = rng.choice([69, 70])
    prompt = (
        f"The Cape Floral Kingdom (Fynbos biome) covers less than 0.5% of Africa's land surface yet contains over {species_count:,} plant species, "
        f"with approximately {endemism_pct}% being endemic. "
        f"What does the term 'endemic' mean in the context of biodiversity conservation?"
    )
    correct = "Species that occur naturally in one specific geographic area and nowhere else on Earth."
    options = [
        correct,
        "Species imported from foreign continents by human settlers for gardening.",
        "Species that have completely died out and exist only as stone fossils in rocks.",
        "Species of predatory animals that feed strictly on marine mammals.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define conservation terminology:\n"
        f"- Indigenous: naturally occurring in a country or region.\n"
        f"- Endemic: naturally restricted to a unique defined geographic location and found nowhere else globally.\n"
        f"- Exotic / alien: introduced from outside native range.\n\n"
        f"**Step 2:** In Fynbos, {endemism_pct}% of the {species_count:,} species are found exclusively in this biome: **{correct}**."
    )
    return {
        "id": f"ns7_bd_02_{rng.randint(100000, 999999)}",
        "subskill": "02_south_african_biodiversity_hotspots_cape_floral",
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
            "tier_1": "Think about whether 'endemic' means local to one spot or found everywhere.",
            "tier_2": "Endemic plants grow only in that unique region and nowhere else on the globe.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["endemic_vs_indigenous_confusion"],
    }


# 03. South African biodiversity hotspots Succulent Karoo
def arch_03_south_african_biodiversity_hotspots_succulent_karoo(rng: random.Random) -> Dict[str, Any]:
    succulent_spp = rng.choice([6000, 6300])
    prompt = (
        f"The Succulent Karoo is recognized internationally as the world's only entirely arid biodiversity hotspot, "
        f"housing over {succulent_spp:,} plant species, about 40% of which are endemic. "
        f"Which ecological feature makes this arid hotspot scientifically unique?"
    )
    correct = "It possesses the richest desert succulent flora on Earth, with thousands of miniature dwarf succulents adapted to winter rainfall and coastal sea fogs."
    options = [
        correct,
        "It is covered in dense tropical rainforest with 4 000 mm of annual rainfall.",
        "It contains zero plant or animal life due to extreme toxic volcanic soil.",
        "It is composed entirely of open freshwater lakes holding giant polar icebergs.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Succulent Karoo biodiversity:\n"
        f"- The world's only arid biodiversity hotspot.\n"
        f"- Boasts over {succulent_spp:,} plant species, predominantly dwarf succulents (e.g. Mesembryanthemums / vygies, Crassulas, Aloes).\n"
        f"- High endemism sustained by predictable winter rainfall and coastal advection fog.\n\n"
        f"**Step 2:** The unique ecological feature is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_03_{rng.randint(100000, 999999)}",
        "subskill": "03_south_african_biodiversity_hotspots_succulent_karoo",
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
            "tier_1": "Succulent Karoo is an arid/desert region in South Africa.",
            "tier_2": "It is famous for dwarf succulents and vygies adapted to low rainfall.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["desert_biodiversity_underestimation"],
    }


# 04. South African biodiversity hotspots Maputaland Albany
def arch_04_south_african_biodiversity_hotspots_maputaland_albany(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"South Africa contains three globally recognized biodiversity hotspots: the Cape Floristic Region, the Succulent Karoo, "
        f"and the Maputaland-Pondoland-Albany hotspot along the eastern seaboard. "
        f"Why is the Maputaland-Pondoland-Albany corridor vital for biodiversity?"
    )
    correct = "It represents a critical floristic transition zone containing subtropical coastal forests, Albany thicket, and high bird and vascular plant endemism."
    options = [
        correct,
        "It is an artificial concrete botanical garden built in the middle of Johannesburg.",
        "It consists of active sub-zero glaciers where polar bears breed.",
        "It is completely devoid of vegetation and used strictly as an open industrial landfill.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review South Africa's 3 biodiversity hotspots:\n"
        f"1. Cape Floristic Region (Fynbos).\n"
        f"2. Succulent Karoo (arid succulents).\n"
        f"3. Maputaland-Pondoland-Albany (subtropical forests and Albany thicket).\n\n"
        f"**Step 2:** The eastern corridor is vital because **{correct}**."
    )
    return {
        "id": f"ns7_bd_04_{rng.randint(100000, 999999)}",
        "subskill": "04_south_african_biodiversity_hotspots_maputaland_albany",
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
            "tier_1": "Think about South Africa's eastern subtropical coast (KwaZulu-Natal to Eastern Cape).",
            "tier_2": "It features subtropical forests, Albany thicket, and diverse indigenous wildlife.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["biodiversity_hotspot_geography_error"],
    }


# 05. Threats to biodiversity habitat destruction
def arch_05_threats_to_biodiversity_habitat_destruction(rng: random.Random) -> Dict[str, Any]:
    threats = [
        ("Clearing native renosterveld grassland for commercial wheat agriculture", "irreversible fragmentation and loss of natural vegetation, reducing breeding territory and food resources for endemic fauna"),
        ("Open-cast coal mining stripping topsoil in Mpumalanga wetlands", "complete destruction of hydric soils, wetland sponge functions, and local extinction of wetland-dependent species"),
        ("Rapid urban sprawl and infrastructure construction across coastal dunes", "bulldozing sensitive dune vegetation, causing coastal erosion and destroying habitats of nesting shorebirds and burrowing reptiles"),
    ]
    activity, impact = rng.choice(threats)
    prompt = (
        f"Habitat destruction is identified globally as the single greatest threat to biodiversity. "
        f"How does '{activity}' lead directly to species extinction?"
    )
    correct = f"By causing {impact.lower()}."
    distractors = [
        "By causing all animals to suddenly evolve wings and fly to Jupiter.",
        "By increasing genetic variation across all native plants by 500%.",
        "By turning non-living granite rocks into living mammals.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the ecological consequences of habitat loss:\n"
        f"- When natural habitats are cleared, food, shelter, and breeding sites disappear.\n"
        f"- Populations become fragmented and small, leading to inbreeding depression and local extinction.\n\n"
        f"**Step 2:** For '{activity}', the direct mechanism is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_05_{rng.randint(100000, 999999)}",
        "subskill": "05_threats_to_biodiversity_habitat_destruction",
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
            "tier_1": "Think about what happens to wild animals when their natural home is cleared.",
            "tier_2": "Habitat fragmentation destroys breeding grounds and food sources.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["habitat_destruction_mechanism_error"],
    }


# 06. Threats to biodiversity invasive alien species
def arch_06_threats_to_biodiversity_invasive_alien_species(rng: random.Random) -> Dict[str, Any]:
    invaders = [
        ("Black wattle (Acacia mearnsii) from Australia", "consuming massive volumes of water along riverbanks, drying up watercourses and outcompeting indigenous riparian fynbos"),
        ("Water hyacinth (Pontederia crassipes) from South America", "forming dense floating mats over dams, blocking sunlight from submerged plants and depleting dissolved oxygen during decomposition"),
        ("Pine trees (Pinus radiata) in mountain catchments", "acidifying fynbos soil with resinous pine needle litter, out-shading indigenous proteas, and fueling catastrophic intense wildfires"),
        ("The house crow (Corvus splendens) in coastal cities", "preying aggressively on eggs and chicks of indigenous songbirds and displacing native avian species"),
    ]
    species, ecological_damage = rng.choice(invaders)
    prompt = (
        f"Invasive alien species pose a major threat to South Africa's indigenous biodiversity. "
        f"What ecological disruption is caused by '{species}'?"
    )
    correct = ecological_damage
    options = [ecological_damage] + [i[1] for i in invaders if i[1] != ecological_damage]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the impact of invasive alien species:\n"
        f"- Free from native natural predators and pathogens, alien species proliferate rapidly.\n"
        f"- They outcompete indigenous species for water, sunlight, soil nutrients, and food.\n\n"
        f"**Step 2:** For '{species}', the specific disruption is: **{ecological_damage}**."
    )
    return {
        "id": f"ns7_bd_06_{rng.randint(100000, 999999)}",
        "subskill": "06_threats_to_biodiversity_invasive_alien_species",
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
            "tier_1": "Consider whether the invasive species is an aquatic weed, a water-thirsty tree, or a predatory bird.",
            "tier_2": "Match the named alien organism to its known South African environmental damage.",
            "tier_3": f"The answer is: {ecological_damage}.",
        },
        "misconception_tags": ["invasive_alien_ecological_impact"],
    }


# 07. Threats to biodiversity poaching and overexploitation
def arch_07_threats_to_biodiversity_poaching_and_overexploitation(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("White and black rhinos poached for horn", "rhino horn is falsely marketed in traditional markets for medicinal properties, despite being composed simply of keratin identical to fingernails"),
        ("Abalone (perlemoen) illegally harvested from coastal reefs", "stripping intertidal and subtidal reefs of breeding adults faster than populations can naturally replenish, destabilizing kelp forest food webs"),
        ("Cycads dug up and smuggled from wild habitats", "ancient slow-growing indigenous gymnosperms targeted by unscrupulous collectors, driving several species to the brink of total extinction in the wild"),
    ]
    species, driver = rng.choice(cases)
    prompt = (
        f"Overexploitation and illegal wildlife trade threaten iconic South African species. "
        f"In the case of '{species}', which statement explains the conservation crisis?"
    )
    correct = driver
    options = [driver] + [c[1] for c in cases if c[1] != driver]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze overexploitation in South Africa:\n"
        f"- Overharvesting removes individuals faster than the species' natural reproductive rate.\n"
        f"- Poaching of rhinos, abalone, and cycads is driven by lucrative illegal syndicates.\n\n"
        f"**Step 2:** For '{species}', the crisis is: **{driver}**."
    )
    return {
        "id": f"ns7_bd_07_{rng.randint(100000, 999999)}",
        "subskill": "07_threats_to_biodiversity_poaching_and_overexploitation",
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
            "tier_1": "Match the species (rhino, abalone, cycad) to why it is being illegally targeted.",
            "tier_2": "Rhinos are targeted for keratin horn; abalone for meat export; cycads as rare ornamental plants.",
            "tier_3": f"The answer is: {driver}.",
        },
        "misconception_tags": ["poaching_motivation_misconception"],
    }


# 08. Threats to biodiversity pollution and climate change
def arch_08_threats_to_biodiversity_pollution_and_climate_change(rng: random.Random) -> Dict[str, Any]:
    threats = [
        ("Rising ocean temperatures and seawater acidification from absorbed atmospheric CO2", "causing extensive coral bleaching, killing reef polyps and dissolving calcium carbonate shells of marine molluscs and plankton"),
        ("Widespread plastic pollution in coastal oceans", "marine mammals and seabirds ingesting or becoming entangled in non-biodegradable plastics, leading to starvation and fatal internal perforations"),
        ("Shifting climate zones and altered rainfall patterns in the Karoo", "aridification occurring faster than slow-growing indigenous succulent flora can migrate or adapt, causing population collapse"),
    ]
    scenario, effect = rng.choice(threats)
    prompt = (
        f"Global atmospheric changes and pollution place immense stress on ecosystems. "
        f"What is the ecological impact of '{scenario}'?"
    )
    correct = effect
    options = [effect] + [t[1] for t in threats if t[1] != effect]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Connect climate change and pollution to biodiversity loss:\n"
        f"- Ocean acidification dissolves marine shells.\n"
        f"- Plastic pollution causes mechanical obstruction and entanglement.\n"
        f"- Rapid climate warming shifts geographic niches faster than species can adapt.\n\n"
        f"**Step 2:** For '{scenario}', the effect is: **{effect}**."
    )
    return {
        "id": f"ns7_bd_08_{rng.randint(100000, 999999)}",
        "subskill": "08_threats_to_biodiversity_pollution_and_climate_change",
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
            "tier_1": "Look at whether the stressor affects coral/shellfish, marine birds, or desert succulents.",
            "tier_2": "Acidic oceans dissolve calcium carbonate; plastics cause ingestion deaths; warming causes range shifts.",
            "tier_3": f"The answer is: {effect}.",
        },
        "misconception_tags": ["climate_pollution_consequence_error"],
    }


# 09. IUCN Red List conservation status categories
def arch_09_iucn_red_list_conservation_status_categories(rng: random.Random) -> Dict[str, Any]:
    statuses = [
        ("Critically Endangered (CR)", "facing an extremely high risk of extinction in the wild in the immediate future, with drastic population declines of 80% or more over ten years"),
        ("Endangered (EN)", "facing a very high risk of extinction in the wild, with severe geographic fragmentation or adult population under 2,500 individuals"),
        ("Vulnerable (VU)", "facing a high risk of endangerment in the wild, likely to become endangered unless circumstances threatening its survival improve"),
        ("Extinct in the Wild (EW)", "known only to survive in captivity, cultivation, or as a naturalized population outside its historic geographic range"),
        ("Extinct (EX)", "beyond reasonable doubt that the last individual of the species has died globally"),
    ]
    cat_name, definition = rng.choice(statuses)
    prompt = (
        f"The IUCN Red List classifies species according to extinction risk. "
        f"Which category is defined as '{definition}'?"
    )
    correct = cat_name
    options = [cat_name] + [s[0] for s in statuses if s[0] != cat_name]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review IUCN Red List hierarchy:\n"
        f"- Extinct (EX): Last individual has died.\n"
        f"- Extinct in the Wild (EW): Survives only in zoos/cultivation.\n"
        f"- Critically Endangered (CR): Extremely high risk of immediate wild extinction.\n"
        f"- Endangered (EN): Very high risk of wild extinction.\n"
        f"- Vulnerable (VU): High risk of endangerment.\n\n"
        f"**Step 2:** The described category is **{cat_name}**."
    )
    return {
        "id": f"ns7_bd_09_{rng.randint(100000, 999999)}",
        "subskill": "09_iucn_red_list_conservation_status_categories",
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
            "tier_1": "Pay attention to the severity keywords: 'extremely high risk', 'very high risk', 'high risk', or 'last individual died'.",
            "tier_2": "Critically Endangered is worse than Endangered, which is worse than Vulnerable.",
            "tier_3": f"The answer is: {cat_name}.",
        },
        "misconception_tags": ["red_list_category_confusion"],
    }


# 10. Indigenous vs exotic vs endemic species
def arch_10_indigenous_vs_exotic_vs_endemic_species(rng: random.Random) -> Dict[str, Any]:
    triplets = [
        ("The King Protea (Protea cynaroides)", "Endemic to South Africa", "it naturally occurs in the Fynbos biome of South Africa and nowhere else in the world"),
        ("The Blue Crane (Anthropoides paradiseus)", "Near-endemic / Indigenous to South Africa", "it naturally occurs and breeds primarily within South Africa's grasslands and Karoo"),
        ("The Jacaranda tree (Jacaranda mimosifolia)", "Exotic (alien) species", "it was introduced by humans from South America and is not native to South Africa"),
        ("The Common Guava (Psidium guajava)", "Exotic invasive species", "it originates from tropical America and invades South African river catchments, displacing native vegetation"),
    ]
    organism, status, justification = rng.choice(triplets)
    prompt = (
        f"In South African ecological classification, how is '{organism}' classified, and what is the scientific justification?"
    )
    correct = f"{status}: {justification}."
    distractors = [
        f"{'Exotic' if 'Endemic' in status else 'Endemic'}: It was created in a chemistry laboratory using mineral rocks.",
        f"{status}: It has completely stopped all life processes and turned into an abiotic fossil.",
        f"{'Exotic' if 'Endemic' in status else 'Endemic'}: It can live without needing water, oxygen, or food.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review biological origin terms:\n"
        f"- Indigenous: Native to the region naturally.\n"
        f"- Endemic: Naturally restricted only to that geographic region.\n"
        f"- Exotic (alien): Introduced from a foreign continent/country.\n\n"
        f"**Step 2:** For '{organism}', the classification is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_10_{rng.randint(100000, 999999)}",
        "subskill": "10_indigenous_vs_exotic_vs_endemic_species",
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
            "tier_1": "Ask: Is it native to South Africa, unique only to SA, or brought from overseas?",
            "tier_2": "Jacaranda is South American (exotic); King Protea is unique to SA Fynbos (endemic).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["origin_classification_confusion"],
    }


# 11. Importance of classification in science
def arch_11_importance_of_classification_in_science(rng: random.Random) -> Dict[str, Any]:
    estimated_millions = rng.choice([8.7, 10.0, 12.0])
    prompt = (
        f"Biologists estimate that there are between 8 and {estimated_millions} million living species on planet Earth. "
        f"Why is a systematic, hierarchical biological classification system essential in Natural Sciences?"
    )
    correct = "It organizes vast biodiversity into logical categories, identifies evolutionary relationships, and provides a universal global communication standard across all languages."
    options = [
        correct,
        "It forces all animals to physically change their body structures to match textbook chapters.",
        "It guarantees that no new species can ever evolve or be discovered in nature.",
        "It allows scientists to rename living animals using made-up random numbers every week.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the purpose of biological classification (taxonomy):\n"
        f"- Organization: structuring millions of species into manageable groups based on shared characteristics.\n"
        f"- Relationship identification: tracing phylogenetic and morphological patterns.\n"
        f"- Standardization: providing unique scientific names that eliminate confusion caused by common names in different languages.\n\n"
        f"**Step 2:** The essential reason is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_11_{rng.randint(100000, 999999)}",
        "subskill": "11_importance_of_classification_in_science",
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
            "tier_1": "Think about why a library organizes books into genres and Dewey decimal numbers.",
            "tier_2": "Classification organizes vast biodiversity and enables universal communication among scientists.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["classification_purpose_misunderstanding"],
    }


# 12. Historical classification Aristotle limitations
def arch_12_historical_classification_aristotle_limitations(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Around 350 BC, the ancient Greek philosopher Aristotle created one of the earliest recorded classification systems: "
        f"he divided living things into Plants (subdivided by stem height: herbs, shrubs, trees) and Animals (subdivided by habitat: land, water, air). "
        f"What is the major scientific limitation of Aristotle's classification system?"
    )
    correct = "It relies on artificial superficial characteristics rather than true biological and cellular relationships, grouping unrelated animals together (e.g. grouping bats, birds, and insects together simply because they fly in air)."
    options = [
        correct,
        "It correctly anticipated DNA gene sequencing and cell biology 2 000 years before microscopes existed.",
        "It proved that all plants on Earth are completely non-living abiotic objects.",
        "It only classified animals that had already gone extinct millions of years before humans.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze Aristotle's classification scheme:\n"
        f"- Artificial system based on superficial habitat (air/water/land) and gross size (tree/shrub/herb).\n"
        f"- Major flaw: unrelated organisms with analogous adaptations are lumped together (e.g. whales grouped with fish because both swim; bats grouped with birds and butterflies because all fly).\n\n"
        f"**Step 2:** The scientific limitation is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_12_{rng.randint(100000, 999999)}",
        "subskill": "12_historical_classification_aristotle_limitations",
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
            "tier_1": "Think about whether a bat is related to a mosquito just because both fly in the air.",
            "tier_2": "Aristotle's system grouped unrelated creatures together based on where they lived.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["aristotle_artificial_system_limitation"],
    }


# 13. Historical classification Carolus Linnaeus contribution
def arch_13_historical_classification_carolus_linnaeus_contribution(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In the 18th century, the Swedish naturalist Carolus Linnaeus revolutionized biological science. "
        f"What were his two foundational contributions to biological classification?"
    )
    correct = "Developing a hierarchical taxonomic ranking scheme (Kingdom down to Species) and establishing the two-part binomial nomenclature system for naming organisms."
    options = [
        correct,
        "Inventing the electron microscope and discovering viral replication inside bacterial cells.",
        "Proving that Earth is flat and that all organisms live inside an underground cave.",
        "Creating the 100-kingdom classification scheme based on musical notes.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Carolus Linnaeus's key achievements:\n"
        f"1. Hierarchical ranking system: grouping species into genus, family, order, class, phylum, kingdom.\n"
        f"2. Binomial nomenclature: giving every species a standardized two-part Latin scientific name (Genus + species).\n\n"
        f"**Step 2:** His foundational contributions were: **{correct}**."
    )
    return {
        "id": f"ns7_bd_13_{rng.randint(100000, 999999)}",
        "subskill": "13_historical_classification_carolus_linnaeus_contribution",
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
            "tier_1": "Linnaeus is called the 'father of taxonomy' and binomial naming.",
            "tier_2": "He introduced the two-part naming system (Genus species) and taxonomic ranks.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["linnaeus_contribution_misattribution"],
    }


# 14. Historical classification Ernst Haeckel Protista
def arch_14_historical_classification_ernst_haeckel_protista(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Carolus Linnaeus originally classified all life into only two kingdoms: Plantae and Animalia. "
        f"In 1866, Ernst Haeckel proposed adding a third kingdom, **Protista**. "
        f"Why was the traditional two-kingdom model no longer sufficient?"
    )
    correct = "The invention and improvement of light microscopes revealed unicellular organisms (like Euglena and Amoeba) that exhibited both plant-like traits (chloroplasts) and animal-like traits (motility), fitting into neither traditional kingdom."
    options = [
        correct,
        "Because all plants on Earth had died out and been replaced by mechanical robots.",
        "Because animals had learned to talk and requested their own private kingdom.",
        "Because scientists discovered that rocks and minerals carry out sexual reproduction.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand why the 2-kingdom system was expanded:\n"
        f"- Microscopic single-celled organisms discovered after Linnaeus did not fit neatly into Plantae (sessile, photosynthesising) or Animalia (motile, ingestive).\n"
        f"- For example, Euglena swims with a flagellum (animal trait) but possesses chloroplasts for photosynthesis (plant trait).\n"
        f"- Haeckel introduced Kingdom Protista to accommodate these unicellular microorganisms.\n\n"
        f"**Step 2:** The reason was: **{correct}**."
    )
    return {
        "id": f"ns7_bd_14_{rng.randint(100000, 999999)}",
        "subskill": "14_historical_classification_ernst_haeckel_protista",
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
            "tier_1": "Think about what microscopes revealed: tiny single-celled pond organisms.",
            "tier_2": "Microbes like Euglena have both plant and animal characteristics.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["two_kingdom_breakdown_misconception"],
    }


# 15. Taxonomic hierarchy ranks domain to species
def arch_15_taxonomic_hierarchy_ranks_domain_to_species(rng: random.Random) -> Dict[str, Any]:
    ranks = ["Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"]
    idx = rng.randint(1, 5)
    target_rank = ranks[idx]
    prev_rank = ranks[idx - 1]
    next_rank = ranks[idx + 1]

    example_animal = rng.choice(["Panthera leo (Lion)", "Homo sapiens (Human)", "Loxodonta africana (Elephant)", "Anthropoides paradiseus (Blue crane)"])
    fill_col = rng.choice(["#E0F2FE", "#FEF3C7", "#DCFCE7", "#F3E8FF"])

    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 240' width='100%' height='240'>"
        f"<rect width='400' height='240' fill='#FAFAFA' rx='8'/>"
        f"<polygon points='200,20 30,220 370,220' fill='{fill_col}' stroke='#999999' stroke-width='2'/>"
        f"<line x1='170' y1='50' x2='230' y2='50' stroke='#333333' stroke-width='1.5'/>"
        f"<text x='200' y='42' fill='#1A365D' font-size='10' font-weight='bold' text-anchor='middle'>Kingdom</text>"
        f"<line x1='145' y1='80' x2='255' y2='80' stroke='#333333' stroke-width='1.5'/>"
        f"<text x='200' y='72' fill='#1A365D' font-size='10' font-weight='bold' text-anchor='middle'>Phylum</text>"
        f"<line x1='120' y1='110' x2='280' y2='110' stroke='#333333' stroke-width='1.5'/>"
        f"<text x='200' y='102' fill='#1A365D' font-size='10' font-weight='bold' text-anchor='middle'>Class</text>"
        f"<line x1='95' y1='140' x2='305' y2='140' stroke='#333333' stroke-width='1.5'/>"
        f"<text x='200' y='132' fill='#1A365D' font-size='10' font-weight='bold' text-anchor='middle'>Order</text>"
        f"<line x1='70' y1='170' x2='330' y2='170' stroke='#333333' stroke-width='1.5'/>"
        f"<text x='200' y='162' fill='#1A365D' font-size='10' font-weight='bold' text-anchor='middle'>Family</text>"
        f"<line x1='45' y1='200' x2='355' y2='200' stroke='#333333' stroke-width='1.5'/>"
        f"<text x='200' y='192' fill='#1A365D' font-size='10' font-weight='bold' text-anchor='middle'>Genus</text>"
        f"<text x='200' y='215' fill='#9B2C2C' font-size='11' font-weight='bold' text-anchor='middle'>Species ({example_animal.split()[0]})</text>"
        f"</svg>"
    )
    prompt = (
        f"In the Linnaean taxonomic hierarchy classifying organisms like {example_animal}, what rank sits immediately below '{prev_rank}' and immediately above '{next_rank}'?"
    )
    correct = target_rank
    options = [target_rank] + [r for r in ranks if r not in (target_rank, prev_rank, next_rank)][:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recite the taxonomic hierarchy from broadest to most specific:\n"
        f"Kingdom -> Phylum -> Class -> Order -> Family -> Genus -> Species.\n"
        f"(Mnemonic: 'King Philip Came Over For Good Soup')\n\n"
        f"**Step 2:** Below '{prev_rank}' and above '{next_rank}' is **{target_rank}**."
    )
    return {
        "id": f"ns7_bd_15_{rng.randint(100000, 999999)}",
        "subskill": "15_taxonomic_hierarchy_ranks_domain_to_species",
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
            "tier_1": "Recall: King Philip Came Over For Good Soup.",
            "tier_2": f"Find what comes between {prev_rank} and {next_rank}.",
            "tier_3": f"The answer is: {target_rank}.",
        },
        "misconception_tags": ["taxonomic_rank_order_error"],
    }


# 16. Taxonomic hierarchy inclusive vs specific relationships
def arch_16_taxonomic_hierarchy_inclusive_vs_specific_relationships(rng: random.Random) -> Dict[str, Any]:
    levels_comparison = [
        ("two organisms belonging to the same Genus (e.g. Panthera leo and Panthera pardus)", "two organisms belonging only to the same Order (e.g. lion and walrus in Order Carnivora)", "the same Genus indicates far more recent evolutionary ancestry and sharing almost all anatomical, physiological, and genetic traits"),
        ("two organisms belonging to the same Family (e.g. domestic cat and cheetah in Felidae)", "two organisms belonging only to the same Class (e.g. cat and whale in Mammalia)", "the same Family represents a much more specific rank with closely matched skeletal and dental structures"),
    ]
    high_sim, low_sim, rationale = rng.choice(levels_comparison)
    prompt = (
        f"Consider two pairs of organisms: Pair A consists of {high_sim}, while Pair B consists of {low_sim}. "
        f"Which pair shares greater biological similarity, and why?"
    )
    correct = f"Pair A shares greater similarity because {rationale}."
    distractors = [
        "Pair B shares greater similarity because broader taxonomic ranks always contain identical identical twins.",
        "Both pairs share exactly zero similarity because Linnaean ranks are completely arbitrary numbers.",
        "Pair B shares greater similarity because Order contains fewer species than Genus.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand specificity in taxonomic ranks:\n"
        f"- Higher ranks (Kingdom, Phylum, Class) are broad and contain diverse organisms.\n"
        f"- Lower ranks (Family, Genus, Species) are highly specific; members share a high degree of DNA sequence similarity and structural traits.\n\n"
        f"**Step 2:** Pair A ({high_sim}) is at a much lower/narrower rank: **{correct}**."
    )
    return {
        "id": f"ns7_bd_16_{rng.randint(100000, 999999)}",
        "subskill": "16_taxonomic_hierarchy_inclusive_vs_specific_relationships",
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
            "tier_1": "Remember: The lower down the taxonomic hierarchy, the more closely related organisms are.",
            "tier_2": "Species in the same Genus are very close relatives, like lions and leopards.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["taxonomic_inclusivity_inversion"],
    }


# 17. Binomial nomenclature naming rules
def arch_17_binomial_nomenclature_naming_rules(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("the African elephant", "Loxodonta africana", "loxodonta africana", "Loxodonta Africana", "LOXODONTA AFRICANA"),
        ("the lion", "Panthera leo", "panthera leo", "Panthera Leo", "PANTHERA LEO"),
        ("modern humans", "Homo sapiens", "homo sapiens", "Homo Sapiens", "HOMO SAPIENS"),
        ("the blue crane", "Anthropoides paradiseus", "anthropoides paradiseus", "Anthropoides Paradiseus", "ANTHROPOIDES PARADISEUS"),
    ]
    animal, correct_fmt, err1, err2, err3 = rng.choice(examples)
    prompt = (
        f"According to the international rules of binomial nomenclature established by Linnaeus, "
        f"which option displays the correct scientific formatting for the scientific name of {animal}?"
    )
    correct = f"*{correct_fmt}* (Genus capitalized, species lower-case, italicized)"
    options = [
        correct,
        f"{err1} (both genus and species in lower-case with no capitalization)",
        f"{err2} (both genus and species capitalized)",
        f"{err3} (all capital letters without italicization)",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review binomial nomenclature formatting rules:\n"
        f"1. The scientific name consists of two parts: Genus followed by species epithet.\n"
        f"2. Genus must start with a CAPITAL letter.\n"
        f"3. Species must start with a LOWER-CASE letter.\n"
        f"4. The entire name must be italicized in print (or underlined if handwritten).\n\n"
        f"**Step 2:** For {animal}, the correctly formatted name is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_17_{rng.randint(100000, 999999)}",
        "subskill": "17_binomial_nomenclature_naming_rules",
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
            "tier_1": "Genus is capitalized, species is lower-case, and both words are italicized.",
            "tier_2": "Look for: Capital letter on the first word, small letter on the second word, in italics.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["binomial_nomenclature_formatting_error"],
    }


# 18. Binomial nomenclature common vs scientific names
def arch_18_binomial_nomenclature_common_vs_scientific_names(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("a 'crayfish' in the Western Cape vs 'crayfish' in the United States", "Common names cause confusion because 'crayfish' in Cape Town refers to a marine spiny lobster (Jasus lalandii), while in America it refers to freshwater astacid crustaceans"),
        ("a 'starfish' and a 'jellyfish'", "Common names are misleading because neither animal is a fish (starfish are echinoderms and jellyfish are cnidarians)"),
        ("the South African 'daisy'", "Over a thousand different plant species in Family Asteraceae are loosely called 'daisies' in colloquial speech, making precise identification impossible without scientific names"),
    ]
    example_subj, explanation = rng.choice(cases)
    prompt = (
        f"Why do international biologists strictly prefer binomial scientific names over common vernacular names? "
        f"Consider this case: \"{example_subj}.\""
    )
    correct = f"{explanation}; binomial names provide a unique universal Latin identifier understood worldwide."
    distractors = [
        "Because common names are illegal under international criminal law.",
        "Because scientific names change every month, making them more exciting to read.",
        "Because common names are only used for plants and never for animals.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Evaluate common names vs scientific names:\n"
        f"- Common names differ between languages and geographic regions, and can be scientifically misleading (e.g. starfish is not a fish).\n"
        f"- Scientific names are universal, stable, and uniquely designate exactly one biological species worldwide.\n\n"
        f"**Step 2:** The justification is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_18_{rng.randint(100000, 999999)}",
        "subskill": "18_binomial_nomenclature_common_vs_scientific_names",
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
            "tier_1": "Think about how different languages have different names for the same animal.",
            "tier_2": "Common names can be misleading (like jellyfish not being a fish) or vary by country.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["common_name_ambiguity_misconception"],
    }


# 19. Biological species concept interbreeding
def arch_19_biological_species_concept_interbreeding(rng: random.Random) -> Dict[str, Any]:
    crosses = [
        ("A female horse (Equus caballus) mated with a male donkey (Equus asinus)", "a mule", "mules are sterile and cannot produce fertile offspring, proving horses and donkeys belong to two separate biological species"),
        ("A male lion (Panthera leo) mated with a female tiger (Panthera tigris)", "a liger", "ligers are inter-species hybrids with severe fertility defects, confirming lions and tigers are distinct species"),
    ]
    cross, offspring, significance = rng.choice(crosses)
    prompt = (
        f"Under the biological species concept, a species is defined as a group of organisms that can interbreed in nature to produce fertile, viable offspring. "
        f"When {cross} breed, they produce {offspring}. "
        f"Why does this cross confirm that the two parent animals are separate species?"
    )
    correct = f"Because {significance}."
    distractors = [
        "Because the offspring immediately converts into a reptile.",
        "Because horses and donkeys belong to different biological kingdoms.",
        "Because all animals with four legs belong to the exact same species.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Apply the biological species definition:\n"
        f"- Members of the same species must produce FERTILE offspring.\n"
        f"- If offspring are sterile/infertile (like the mule produced from horse + donkey), a post-zygotic reproductive barrier exists.\n\n"
        f"**Step 2:** Therefore, {significance}."
    )
    return {
        "id": f"ns7_bd_19_{rng.randint(100000, 999999)}",
        "subskill": "19_biological_species_concept_interbreeding",
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
            "tier_1": "Key word in the definition of a species is 'fertile' offspring.",
            "tier_2": "Mules cannot have babies of their own (they are sterile).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["hybrid_sterility_species_concept"],
    }


# 20. Prokaryote vs eukaryote cellular differences
def arch_20_prokaryote_vs_eukaryote_cellular_differences(rng: random.Random) -> Dict[str, Any]:
    features = [
        ("Membrane-bound nucleus", "Absent in prokaryotes (naked circular DNA in nucleoid); Present in eukaryotes (enclosed by a double nuclear membrane)"),
        ("Membrane-bound organelles (e.g. mitochondria, chloroplasts, endoplasmic reticulum)", "Completely absent in prokaryotes; Present in eukaryotes with specialized compartmentalized functions"),
        ("Cell size and complexity", "Prokaryotes are microscopic and simple (typically 0.1-5 um); Eukaryotes are significantly larger and complex (typically 10-100 um)"),
        ("Chromosomal structure", "Prokaryotes possess a single circular DNA chromosome without histones; Eukaryotes possess multiple linear DNA chromosomes associated with histone proteins"),
    ]
    feature_name, contrast = rng.choice(features)
    prompt = (
        f"All living cells are classified as either prokaryotic or eukaryotic. "
        f"Which statement correctly compares prokaryotes and eukaryotes with respect to '{feature_name}'?"
    )
    correct = contrast
    options = [contrast] + [f[1] for f in features if f[1] != contrast]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Contrast prokaryotic and eukaryotic cells:\n"
        f"- Prokaryotes (e.g. bacteria): No true nucleus, no membrane-bound organelles, circular DNA.\n"
        f"- Eukaryotes (protists, fungi, plants, animals): True nucleus with nuclear membrane, membrane-bound organelles (mitochondria), linear chromosomes.\n\n"
        f"**Step 2:** For '{feature_name}', the correct contrast is: **{contrast}**."
    )
    return {
        "id": f"ns7_bd_20_{rng.randint(100000, 999999)}",
        "subskill": "20_prokaryote_vs_eukaryote_cellular_differences",
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
            "tier_1": "Recall: 'Pro' = before (before nucleus); 'Eu' = true (true nucleus).",
            "tier_2": "Bacteria are prokaryotes (no nucleus); animals and plants are eukaryotes (have a nucleus).",
            "tier_3": f"The answer is: {contrast}.",
        },
        "misconception_tags": ["prokaryote_eukaryote_conflation"],
    }


# 21. Five kingdom overview diagnostic criteria
def arch_21_five_kingdom_overview_diagnostic_criteria(rng: random.Random) -> Dict[str, Any]:
    kingdoms = [
        ("Kingdom Monera", "Prokaryotic unicellular organisms lacking membrane-bound organelles, with peptidoglycan cell walls (e.g. bacteria)"),
        ("Kingdom Protista", "Eukaryotic, predominantly unicellular or colonial aquatic organisms without complex tissue differentiation (e.g. Amoeba, Euglena)"),
        ("Kingdom Fungi", "Eukaryotic, heterotrophic absorptive decomposers with chitin cell walls, reproducing via spores (e.g. mushrooms, bread mould, yeast)"),
        ("Kingdom Plantae", "Eukaryotic, multicellular autotrophs with cellulose cell walls containing chlorophyll for photosynthesis (e.g. ferns, mosses, flowering plants)"),
        ("Kingdom Animalia", "Eukaryotic, multicellular ingestive heterotrophs lacking cell walls, typically showing motility and specialized sensory nervous systems"),
    ]
    k_name, diagnostic = rng.choice(kingdoms)
    prompt = (
        f"In the widely accepted Five Kingdom classification system, which kingdom is uniquely diagnosed by the following biological traits:\n"
        f"\"{diagnostic}\"?"
    )
    correct = k_name
    options = [k_name] + [k[0] for k in kingdoms if k[0] != k_name]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review diagnostic traits of the Five Kingdoms:\n"
        f"- Monera: prokaryotic, bacteria.\n"
        f"- Protista: eukaryotic unicellular/simple colonial.\n"
        f"- Fungi: chitin cell walls, absorptive heterotrophs.\n"
        f"- Plantae: cellulose cell walls, autotrophic.\n"
        f"- Animalia: no cell walls, ingestive heterotrophs.\n\n"
        f"**Step 2:** The described diagnostic traits belong to **{k_name}**."
    )
    return {
        "id": f"ns7_bd_21_{rng.randint(100000, 999999)}",
        "subskill": "21_five_kingdom_overview_diagnostic_criteria",
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
            "tier_1": "Check: Is it prokaryotic or eukaryotic? Does it have a cell wall, and what is it made of (chitin, cellulose, peptidoglycan)?",
            "tier_2": "Match nutrition mode (photosynthesis vs absorption vs ingestion) to the kingdom.",
            "tier_3": f"The answer is: {k_name}.",
        },
        "misconception_tags": ["five_kingdom_diagnostic_confusion"],
    }


# 22. Kingdom Monera bacteria characteristics
def arch_22_kingdom_monera_bacteria_characteristics(rng: random.Random) -> Dict[str, Any]:
    bacteria_types = [
        ("Mycobacterium tuberculosis", "a pathogenic rod-shaped bacterium that causes tuberculosis (TB) by infecting lung tissues in humans"),
        ("Staphylococcus aureus", "a spherical bacterium (coccus) forming clusters, causing skin boils, respiratory infections, and food poisoning"),
        ("Escherichia coli (E. coli)", "a rod-shaped bacterium naturally inhabiting mammalian intestines, assisting in vitamin K production while certain strains cause gastroenteritis"),
        ("Rhizobium species", "a beneficial soil bacterium forming symbiotic root nodules on legumes to fix atmospheric nitrogen into nitrates"),
    ]
    bacterium, description = rng.choice(bacteria_types)
    prompt = (
        f"Kingdom Monera contains all bacterial prokaryotes. "
        f"Consider '{bacterium}'. Which statement accurately describes its characteristics and ecological impact?"
    )
    correct = description
    options = [description] + [b[1] for b in bacteria_types if b[1] != description]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Monera organisms from Curriculum Chapter 10:\n"
        f"- Monerans are prokaryotic unicellular bacteria.\n"
        f"- Some are pathogenic (e.g. M. tuberculosis, S. aureus), while others are beneficial symbionts (e.g. Rhizobium, gut E. coli).\n\n"
        f"**Step 2:** For '{bacterium}', the correct statement is: **{description}**."
    )
    return {
        "id": f"ns7_bd_22_{rng.randint(100000, 999999)}",
        "subskill": "22_kingdom_monera_bacteria_characteristics",
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
            "tier_1": "Recall the diseases or benefits associated with TB bacteria, Staph, or Rhizobium.",
            "tier_2": "Tuberculosis affects lungs; Staph causes skin/food poisoning; Rhizobium fixes nitrogen.",
            "tier_3": f"The answer is: {description}.",
        },
        "misconception_tags": ["all_bacteria_are_harmful_misconception"],
    }


# 23. Kingdom Protista single-celled eukaryotes
def arch_23_kingdom_protista_single_celled_eukaryotes(rng: random.Random) -> Dict[str, Any]:
    protists = [
        ("Amoeba proteus", "moves and captures food by extending temporary projections of cytoplasm called pseudopodia (false feet) through phagocytosis"),
        ("Euglena viridis", "possesses a whip-like flagellum for swimming, a light-sensitive eyespot (stigma), and chloroplasts for autotrophic photosynthesis in light"),
        ("Paramecium caudatum", "a slipper-shaped protozoan covered in coordinated hair-like cilia for locomotion and sweeping food into its oral groove"),
        ("Diatoms (microscopic algae)", "photosynthetic aquatic protists enclosed in intricately patterned silica glass cell walls (frustules), forming the base of marine food webs"),
    ]
    protist_name, traits = rng.choice(protists)
    prompt = (
        f"Kingdom Protista is an exceptionally diverse group of simple eukaryotic organisms. "
        f"Which statement describes the locomotion and feeding traits of '{protist_name}'?"
    )
    correct = traits
    options = [traits] + [p[1] for p in protists if p[1] != traits]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review representative protists:\n"
        f"- Amoeba: pseudopodia for creeping and engulfing prey.\n"
        f"- Euglena: flagellum, eyespot, mixotrophic with chloroplasts.\n"
        f"- Paramecium: cilia for swimming and feeding.\n"
        f"- Diatoms: silica glass shells, phytoplankton photosynthesis.\n\n"
        f"**Step 2:** For '{protist_name}', the description is: **{traits}**."
    )
    return {
        "id": f"ns7_bd_23_{rng.randint(100000, 999999)}",
        "subskill": "23_kingdom_protista_single_celled_eukaryotes",
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
            "tier_1": "Match the organelle of movement: pseudopodia (Amoeba), flagellum (Euglena), cilia (Paramecium), silica wall (Diatoms).",
            "tier_2": "Look at how the named protist moves and feeds.",
            "tier_3": f"The answer is: {traits}.",
        },
        "misconception_tags": ["protist_locomotion_confusion"],
    }


# 24. Kingdom Fungi absorptive heterotrophs
def arch_24_kingdom_fungi_absorptive_heterotrophs(rng: random.Random) -> Dict[str, Any]:
    fungus_examples = [
        ("The button mushroom (Agaricus bisporus)", "composed of an underground mycelium network of thread-like hyphae that produces an above-ground fruiting body shedding millions of microscopic spores from gills"),
        ("Bread mould (Rhizopus stolonifer)", "grows as a white fuzzy network of hyphae producing upright sporangiophores with black spore-bearing globes (sporangia) on damp starch substrates"),
        ("Baker's yeast (Saccharomyces cerevisiae)", "a microscopic unicellular fungus that reproduces asexually by budding and performs alcoholic fermentation of sugars"),
    ]
    fungus_name, features = rng.choice(fungus_examples)
    prompt = (
        f"Organisms in Kingdom Fungi were once mistakenly classified as plants. "
        f"Why are fungi classified in their own distinct kingdom, and what characterizes '{fungus_name}'?"
    )
    correct = f"Fungi lack chlorophyll, possess cell walls made of chitin (not cellulose), and feed by absorptive heterotrophy; {features}."
    distractors = [
        f"Fungi are classified as animals because they possess four legs and a heart; {features}.",
        f"Fungi are non-living minerals that dissolve into rainwater within minutes.",
        f"Fungi perform photosynthesis using green chlorophyll just like oak trees.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish Fungi from Plantae:\n"
        f"- Fungi do NOT possess chlorophyll and cannot perform photosynthesis.\n"
        f"- Cell walls are made of chitin (the same polymer found in arthropod exoskeletons), not cellulose.\n"
        f"- Nutrition is saprophytic/heterotrophic (secreting enzymes externally and absorbing digested nutrients).\n\n"
        f"**Step 2:** The justification and feature of '{fungus_name}' is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_24_{rng.randint(100000, 999999)}",
        "subskill": "24_kingdom_fungi_absorptive_heterotrophs",
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
            "tier_1": "Do mushrooms have chlorophyll? No, they cannot make their own food.",
            "tier_2": "Fungal cell walls are made of chitin, and they absorb nutrients as decomposers.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fungi_are_plants_misconception"],
    }


# 25. Kingdom Plantae autotrophic chloroplasts
def arch_25_kingdom_plantae_autotrophic_chloroplasts(rng: random.Random) -> Dict[str, Any]:
    plant_groups = [
        ("Bryophytes (Mosses)", "Non-vascular plants lacking true roots, stems, or xylem/phloem vessels; absorb water across thin leaves and reproduce via spores in moist habitats"),
        ("Pteridophytes (Ferns)", "Seedless vascular plants possessing true xylem and phloem, producing reproductive spore clusters (sori) on the underside of fronds"),
        ("Gymnosperms (Conifers and Cycads)", "Vascular seed plants that produce 'naked' seeds borne on woody cones without enclosing ovaries or flowers"),
        ("Angiosperms (Flowering plants)", "Vascular plants with specialized reproductive flowers whose pollinated ovules develop into seeds protected inside fleshy or dry fruits"),
    ]
    group_name, defining_traits = rng.choice(plant_groups)
    prompt = (
        f"Kingdom Plantae contains all multicellular autotrophic organisms. "
        f"Which major plant division is characterized as: \"{defining_traits}\"?"
    )
    correct = group_name
    options = [group_name] + [g[0] for g in plant_groups if g[0] != group_name]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review major plant divisions:\n"
        f"- Bryophytes (mosses): non-vascular, spores.\n"
        f"- Pteridophytes (ferns): vascular, spores (sori).\n"
        f"- Gymnosperms (conifers/cycads): vascular, cones with naked seeds.\n"
        f"- Angiosperms (flowering plants): flowers and enclosed fruit seeds.\n\n"
        f"**Step 2:** The described division is **{group_name}**."
    )
    return {
        "id": f"ns7_bd_25_{rng.randint(100000, 999999)}",
        "subskill": "25_kingdom_plantae_autotrophic_chloroplasts",
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
            "tier_1": "Notice if the plant has vascular tissue, flowers, cones, or spores.",
            "tier_2": "Mosses have no vascular veins; ferns have sori spores; conifers have cones; angiosperms have flowers.",
            "tier_3": f"The answer is: {group_name}.",
        },
        "misconception_tags": ["plant_division_traits_confusion"],
    }
