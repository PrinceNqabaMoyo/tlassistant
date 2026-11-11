"""Grade 7 Natural Sciences: Term 1 - Biodiversity (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/02. Biodiversity.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Kingdom Animalia heterotrophic multicellular
def arch_26_kingdom_animalia_heterotrophic_multicellular(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("A chacma baboon (Papio ursinus) foraging in the Cape Peninsula", "heterotrophic ingestion of pre-formed organic matter, lack of cell walls around cells, and nervous tissue for coordination"),
        ("A great white shark (Carcharodon carcharias) hunting seals in False Bay", "multicellularity with specialized organ systems, blastula embryonic stage, and active sensory locomotion"),
        ("A garden snail (Cornu aspersum) feeding on lettuce leaves", "internal digestion within a digestive tract, extracellular collagen support matrices, and eukaryotic multicellularity"),
    ]
    animal, traits = rng.choice(examples)
    prompt = (
        f"Kingdom Animalia is one of the five biological kingdoms. "
        f"Consider '{animal}'. Which combination of cellular and physiological characteristics defines its placement in Kingdom Animalia?"
    )
    correct = f"Multicellular eukaryotes lacking cell walls; {traits}."
    distractors = [
        "Unicellular prokaryotes possessing a peptidoglycan cell wall and photosynthetic pigments.",
        "Autotrophic plants that manufacture carbohydrates from sunlight using chlorophyll.",
        "Acellular infectious particles made only of protein capsids and viral RNA.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review defining characteristics of Kingdom Animalia:\n"
        f"- Multicellular eukaryotes.\n"
        f"- Heterotrophic by ingestion (eat food and digest internally).\n"
        f"- NO cell walls (cells are flexible, held together by extracellular matrix/collagen).\n"
        f"- Most exhibit motility and specialized nervous/muscular coordination.\n\n"
        f"**Step 2:** For '{animal}', the correct combination is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_26_{rng.randint(100000, 999999)}",
        "subskill": "26_kingdom_animalia_heterotrophic_multicellular",
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
            "tier_1": "Do animals have cell walls like plants? No, they lack cell walls.",
            "tier_2": "Animals eat other organisms (heterotrophic) and are multicellular.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["animal_cellular_characteristics_confusion"],
    }


# 27. Invertebrates vs vertebrates distinction
def arch_27_invertebrates_vs_vertebrates_distinction(rng: random.Random) -> Dict[str, Any]:
    group_split = rng.choice([
        ("Vertebrates", "possess an internal endoskeleton made of bone or cartilage that includes an articulated vertebral column (backbone) protecting the dorsal spinal nerve cord"),
        ("Invertebrates", "completely lack a vertebral column or backbone, relying instead on an external chitinous exoskeleton, a hydrostatic fluid skeleton, or a shell for support"),
    ])
    group_name, definition = group_split
    pct_invert = rng.choice([95, 97])
    prompt = (
        f"Scientists divide all animals into two primary informal divisions: vertebrates and invertebrates. "
        f"Approximately {pct_invert}% of all known animal species are invertebrates. "
        f"Which statement scientifically distinguishes '{group_name}'?"
    )
    correct = f"'{group_name}' {definition}."
    distractors = [
        f"'{group_name}' are all microscopic bacteria that reproduce by binary fission.",
        f"'{group_name}' are warm-blooded plants that feed on solar sunlight.",
        f"'{group_name}' do not possess cells and are composed of pure liquid mercury.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define the fundamental morphological divide:\n"
        f"- Vertebrates (Subphylum Vertebrata): Have an internal backbone (vertebral column).\n"
        f"- Invertebrates: Lack an internal backbone (~{pct_invert}% of animal kingdom).\n\n"
        f"**Step 2:** '{group_name}' is accurately defined: **{correct}**."
    )
    return {
        "id": f"ns7_bd_27_{rng.randint(100000, 999999)}",
        "subskill": "27_invertebrates_vs_vertebrates_distinction",
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
            "tier_1": "Recall what a backbone is (vertebral column).",
            "tier_2": "Vertebrates have backbones; invertebrates do not have backbones.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["backbone_presence_confusion"],
    }


# 28. Invertebrate phylum Porifera sponges
def arch_28_invertebrate_phylum_porifera_sponges(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Phylum Porifera includes marine and freshwater sea sponges. "
        f"Which set of anatomical and lifestyle characteristics uniquely describes organisms in Phylum Porifera?"
    )
    correct = "Asymmetrical, sessile (non-motile) organisms with bodies perforated by pores (ostia), lacking true tissues, organs, or nerves, and feeding by filter-feeding water pumped through internal flagellated collar cells."
    options = [
        correct,
        "Bilateral animals with a hard external carapace, compound eyes, and six jointed walking legs.",
        "Radial organisms with tentacles armed with stinging cnidocyte cells and a central mouth.",
        "Segmented predatory worms with closed circulatory systems and hydrostatic coeloms.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Phylum Porifera characteristics:\n"
        f"- Body symmetry: Asymmetrical (no regular planes of symmetry).\n"
        f"- Organization: Cellular level of organization (no true tissues or organs).\n"
        f"- Structure: Porous body walls (ostia) with a central cavity (spongocoel) and excurrent opening (osculum).\n"
        f"- Feeding: Filter feeders, sessile adults.\n\n"
        f"**Step 2:** The unique description is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_28_{rng.randint(100000, 999999)}",
        "subskill": "28_invertebrate_phylum_porifera_sponges",
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
            "tier_1": "Recall: Porifera means 'pore-bearer'.",
            "tier_2": "Sponges are sessile, full of holes/pores, and have no true tissues or nerves.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["sponge_tissue_level_misconception"],
    }


# 29. Invertebrate phylum Cnidaria jellyfish corals
def arch_29_invertebrate_phylum_cnidaria_jellyfish_corals(rng: random.Random) -> Dict[str, Any]:
    cnidarians = [
        ("The bluebottle / Portuguese man-o'-war (Physalia physalis) washed up on False Bay beaches", "long trailing tentacles packed with specialized stinging cells called cnidocytes (nematocysts) that fire toxic barbs to paralyze fish"),
        ("A reef-building coral polyp in Sodwana Bay", "secreting a hard calcium carbonate exoskeleton around its radial body, living in symbiosis with photosynthetic zooxanthellae algae"),
        ("A common jellyfish (Aurelia aurita)", "a swimming bell-shaped medusa exhibiting radial symmetry, with a single gastrovascular opening acting as both mouth and anus"),
    ]
    organism, trait = rng.choice(cnidarians)
    prompt = (
        f"Phylum Cnidaria includes sea anemones, corals, and jellyfish. "
        f"In '{organism}', which diagnostic cnidarian trait is demonstrated?"
    )
    correct = trait
    options = [trait] + [c[1] for c in cnidarians if c[1] != trait]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Phylum Cnidaria diagnostic traits:\n"
        f"- Radial symmetry.\n"
        f"- Stinging cells (cnidocytes containing nematocysts).\n"
        f"- Two body forms: sessile polyp (e.g. coral, sea anemone) and free-swimming medusa (e.g. jellyfish).\n"
        f"- Single opening to gastrovascular cavity.\n\n"
        f"**Step 2:** For '{organism}', the exhibited trait is: **{trait}**."
    )
    return {
        "id": f"ns7_bd_29_{rng.randint(100000, 999999)}",
        "subskill": "29_invertebrate_phylum_cnidaria_jellyfish_corals",
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
            "tier_1": "Cnidarians are famous for stinging tentacles and radial symmetry.",
            "tier_2": "Look for nematocysts (stinging cells), coral polyps, or medusa bell.",
            "tier_3": f"The answer is: {trait}.",
        },
        "misconception_tags": ["cnidarian_symmetry_confusion"],
    }


# 30. Invertebrate phylum Platyhelminthes flatworms
def arch_30_invertebrate_phylum_platyhelminthes_flatworms(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("The freshwater planarian", "a free-living flatworm with bilateral symmetry, eyespots, and a branching gut without an anus, moving via ventral epidermal cilia"),
        ("The pork tapeworm (Taenia solium)", "an endoparasitic flatworm with a scolex (head with hooks and suckers) and flattened reproductive proglottid segments, lacking a digestive tract"),
        ("The human blood fluke (Schistosoma / Bilharzia)", "a parasitic flatworm with an indirect life cycle requiring freshwater snails as intermediate hosts, infecting humans through skin penetration in rivers"),
    ]
    worm, details = rng.choice(examples)
    prompt = (
        f"Phylum Platyhelminthes comprises the flatworms. "
        f"Which statement describes the morphology and lifestyle of '{worm}'?"
    )
    correct = details
    options = [details] + [e[1] for e in examples if e[1] != details]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Phylum Platyhelminthes:\n"
        f"- Bilateral symmetry.\n"
        f"- Dorsoventrally flattened unsegmented body.\n"
        f"- Acoelomate (no body cavity).\n"
        f"- Can be free-living (planaria) or parasitic (tapeworms, bilharzia flukes).\n\n"
        f"**Step 2:** For '{worm}', the accurate description is: **{details}**."
    )
    return {
        "id": f"ns7_bd_30_{rng.randint(100000, 999999)}",
        "subskill": "30_invertebrate_phylum_platyhelminthes_flatworms",
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
            "tier_1": "Flatworms are flat like ribbons or leaves.",
            "tier_2": "Tapeworms have hooks/suckers; planarians have eyespots; bilharzia flukes live in blood vessels.",
            "tier_3": f"The answer is: {details}.",
        },
        "misconception_tags": ["flatworm_body_cavity_confusion"],
    }


# 31. Invertebrate phylum Annelida segmented worms
def arch_31_invertebrate_phylum_annelida_segmented_worms(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Phylum Annelida includes earthworms, leeches, and marine lugworms. "
        f"What structural advancement distinguishes Annelids from Platyhelminthes (flatworms)?"
    )
    correct = "A true fluid-filled body cavity (coelom) and a body divided into repeated external and internal segments (metamerism), with a one-way digestive tract having both a mouth and an anus."
    options = [
        correct,
        "An internal bony skeleton with a skull and vertebral column protecting lungs.",
        "Hard jointed legs made of chitin that allow rapid flying above ground.",
        "Total absence of blood vessels and reliance on photosynthesis to produce glucose.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare Annelida and Platyhelminthes:\n"
        f"- Platyhelminthes: acoelomate, flat, incomplete gut (no anus).\n"
        f"- Annelida: coelomate, metameric segmentation (rings/segments), complete gut (mouth and anus), closed circulatory system.\n\n"
        f"**Step 2:** The structural advancement is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_31_{rng.randint(100000, 999999)}",
        "subskill": "31_invertebrate_phylum_annelida_segmented_worms",
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
            "tier_1": "Think about the rings on an earthworm's body (segmentation).",
            "tier_2": "Earthworms have a true coelom, body rings (segments), and a complete digestive tract.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["annelid_segmentation_coelom_confusion"],
    }


# 32. Invertebrate phylum Mollusca soft bodied
def arch_32_invertebrate_phylum_mollusca_soft_bodied(rng: random.Random) -> Dict[str, Any]:
    molluscs = [
        ("The brown garden snail (Gastropoda)", "a muscular ventral foot for creeping, a coiled calcium carbonate shell, and a rasping tongue-like radula to scrape plant matter"),
        ("The black mussel / oyster (Bivalvia)", "two hinged shells enclosing a soft body with no radula, using siphon currents and large gills for filter-feeding plankton"),
        ("The common octopus (Cephalopoda)", "a foot modified into eight flexible suction-bearing arms, a parrot-like beak, a large brain with camera-type eyes, and an internal reduced shell"),
    ]
    organism, features = rng.choice(molluscs)
    prompt = (
        f"Phylum Mollusca contains soft-bodied animals typically possessing a muscular foot, visceral mass, and a mantle. "
        f"Which statement describes the specialized morphology of '{organism}'?"
    )
    correct = features
    options = [features] + [m[1] for m in molluscs if m[1] != features]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Phylum Mollusca body plan:\n"
        f"- 3 main body regions: Muscular foot (locomotion), Visceral mass (internal organs), Mantle (secretes shell).\n"
        f"- Classes: Gastropoda (snails/slugs), Bivalvia (mussels/clams), Cephalopoda (octopus/squid).\n\n"
        f"**Step 2:** For '{organism}', the morphology is: **{features}**."
    )
    return {
        "id": f"ns7_bd_32_{rng.randint(100000, 999999)}",
        "subskill": "32_invertebrate_phylum_mollusca_soft_bodied",
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
            "tier_1": "Is it a snail (crawling foot/radula), a bivalve (two hinged shells), or an octopus (8 arms/smart eyes)?",
            "tier_2": "Match the class features directly to the named mollusc.",
            "tier_3": f"The answer is: {features}.",
        },
        "misconception_tags": ["mollusc_class_body_plan_confusion"],
    }


# 33. Invertebrate phylum Echinodermata spiny skinned
def arch_33_invertebrate_phylum_echinodermata_spiny_skinned(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Phylum Echinodermata comprises marine animals such as starfish, sea urchins, and sea cucumbers. "
        f"Which combination of structural traits is diagnostic of adult echinoderms?"
    )
    correct = "Pentaradial (five-part) symmetry in adults, a spiny internal calcareous endoskeleton, and a unique water vascular system operating hydraulic tube feet for locomotion and prey capture."
    options = [
        correct,
        "Bilateral symmetry with an external segmented chitinous carapace and six walking legs.",
        "An asymmetrical porous body filled with internal collar cells that pump water through ostia.",
        "A soft flattened unsegmented body possessing a ventral muscular creeping foot and radula.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Echinodermata characteristics:\n"
        f"- Habitat: Exclusively marine.\n"
        f"- Symmetry: Bilateral in larvae, pentamerous (5-part) radial in adults.\n"
        f"- Skeleton: Spiny calcareous plates (endoskeleton under epidermis).\n"
        f"- Locomotion: Water vascular system with hydraulic tube feet.\n\n"
        f"**Step 2:** The diagnostic combination is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_33_{rng.randint(100000, 999999)}",
        "subskill": "33_invertebrate_phylum_echinodermata_spiny_skinned",
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
            "tier_1": "Think about a starfish: 5 arms (pentamerous), spiny skin, and tube feet.",
            "tier_2": "The water vascular system powers tube feet in echinoderms.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["echinoderm_symmetry_misconception"],
    }


# 34. Invertebrate phylum Arthropoda general traits
def arch_34_invertebrate_phylum_arthropoda_general_traits(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Phylum Arthropoda is the largest and most diverse phylum in the animal kingdom, containing over 80% of all animal species. "
        f"Which three anatomical characteristics are shared by ALL arthropods?"
    )
    correct = "A rigid external exoskeleton made of chitin, a segmented body, and jointed paired appendages (legs/antennae)."
    options = [
        correct,
        "A bony internal backbone, hair-covered skin, and three-chambered hearts.",
        "An unsegmented soft body, a calcareous shell, and a muscular ventral creeping foot.",
        "An asymmetrical body, stinging cnidocyte cells, and microscopic cilia for filter-feeding.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recall the 3 universal arthropod defining traits:\n"
        f"1. Chitinous exoskeleton: provides protection and muscle attachment, must be shed (moulted / ecdysis) to grow.\n"
        f"2. Segmented body (tagmata): head, thorax, abdomen (or cephalothorax and abdomen).\n"
        f"3. Jointed appendages: 'Arthro-poda' literally translates to 'jointed feet'.\n\n"
        f"**Step 2:** The 3 universal traits are: **{correct}**."
    )
    return {
        "id": f"ns7_bd_34_{rng.randint(100000, 999999)}",
        "subskill": "34_invertebrate_phylum_arthropoda_general_traits",
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
            "tier_1": "Look at the name: 'Arthro' = joint, 'Pod' = foot.",
            "tier_2": "All arthropods have jointed legs, segmented bodies, and a hard exoskeleton.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["arthropod_defining_traits_confusion"],
    }


# 35. Arthropod class Insecta diagnostic features
def arch_35_arthropod_class_insecta_diagnostic_features(rng: random.Random) -> Dict[str, Any]:
    insects = [
        ("The honeybee (Apis mellifera)", "head, thorax, and abdomen", 3, 1),
        ("The migratory locust (Locusta migratoria)", "head, thorax, and abdomen", 3, 1),
        ("The housefly (Musca domestica)", "head, thorax, and abdomen", 3, 1),
    ]
    insect_name, body_div, leg_pairs, ant_pairs = rng.choice(insects)
    prompt = (
        f"Class Insecta is the most species-rich class of animals on Earth. "
        f"Consider '{insect_name}'. Which morphological formula correctly defines an adult insect?"
    )
    correct = f"3 body parts ({body_div}), {leg_pairs} pairs of walking legs (6 legs total attached to thorax), and {ant_pairs} pair of sensory antennae."
    options = [
        correct,
        "2 body parts (cephalothorax and abdomen), 4 pairs of walking legs (8 legs total), and zero antennae.",
        "2 body parts, 5 pairs of walking legs (10 legs total), and 2 pairs of antennae.",
        "An elongated multi-segmented body with 1 or 2 pairs of legs per segment and no eyes.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Class Insecta morphology:\n"
        f"- Body divisions: 3 (head, thorax, abdomen).\n"
        f"- Walking legs: 3 pairs (6 legs), all attached to the thorax.\n"
        f"- Antennae: 1 pair on the head.\n"
        f"- Wings: usually 1 or 2 pairs attached to the thorax (in most adult insects).\n\n"
        f"**Step 2:** The defining formula is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_35_{rng.randint(100000, 999999)}",
        "subskill": "35_arthropod_class_insecta_diagnostic_features",
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
            "tier_1": "How many legs does an insect have? 6 legs (3 pairs).",
            "tier_2": "3 body parts (head, thorax, abdomen), 6 legs, 1 pair of antennae.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["insect_leg_count_confusion"],
    }


# 36. Arthropod class Arachnida spiders scorpions
def arch_36_arthropod_class_arachnida_spiders_scorpions(rng: random.Random) -> Dict[str, Any]:
    arachnids = [
        ("The baboon spider (Ceratogyrus)", "cephalothorax and abdomen", 4, 0),
        ("The thick-tailed scorpion (Parabuthus)", "cephalothorax and abdomen with stinging tail", 4, 0),
        ("The bont tick (Amblyomma hebraeum)", "fused unsegmented body", 4, 0),
    ]
    arachnid_name, body_div, leg_pairs, ant_count = rng.choice(arachnids)
    prompt = (
        f"Class Arachnida includes spiders, scorpions, ticks, and mites. "
        f"In '{arachnid_name}', which morphological formula correctly distinguishes arachnids from insects?"
    )
    correct = f"2 body regions ({body_div}), {leg_pairs} pairs of walking legs (8 legs total), zero antennae, and chelicerae for feeding."
    options = [
        correct,
        "3 body regions (head, thorax, abdomen), 3 pairs of walking legs (6 legs), and 1 pair of antennae.",
        "2 body regions, 5 pairs of walking legs (10 legs), and 2 pairs of sensory antennae.",
        "Many body segments, each possessing 2 pairs of legs, with chewing mandibles.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Class Arachnida morphology:\n"
        f"- Body divisions: 2 (cephalothorax and abdomen).\n"
        f"- Walking legs: 4 pairs (8 legs total).\n"
        f"- Antennae: ZERO antennae (arachnids have no antennae).\n"
        f"- Mouthparts: chelicerae (fangs/pincers) and pedipalps.\n\n"
        f"**Step 2:** The distinguishing formula is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_36_{rng.randint(100000, 999999)}",
        "subskill": "36_arthropod_class_arachnida_spiders_scorpions",
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
            "tier_1": "How many legs does a spider have? 8 legs (4 pairs).",
            "tier_2": "Spiders have 2 body parts, 8 legs, and NO antennae.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["spider_insect_conflation"],
    }


# 37. Arthropod class Crustacea crabs prawns
def arch_37_arthropod_class_crustacea_crabs_prawns(rng: random.Random) -> Dict[str, Any]:
    crustaceans = [
        ("The Cape rock lobster / West Coast crayfish (Jasus lalandii)", "a heavily calcified cephalothorax (carapace) and muscular abdomen, 5 pairs of walking legs (decapod), and 2 pairs of sensory antennae"),
        ("The shore crab (Cyclograpsus punctatus)", "a broad flattened cephalothorax with the abdomen tucked tightly underneath, with the first pair of legs modified as large grasping chelae (pincers)"),
        ("The common woodlouse / pill bug", "a terrestrial crustacean with an articulated armored exoskeleton that rolls into a ball and breathes through specialized pseudotracheal gills on pleopods"),
    ]
    org_name, morphology = rng.choice(crustaceans)
    prompt = (
        f"Class Crustacea comprises mostly aquatic arthropods including crabs, lobsters, and woodlice. "
        f"Which statement describes the diagnostic morphology of '{org_name}'?"
    )
    correct = morphology
    options = [morphology] + [c[1] for c in crustaceans if c[1] != morphology]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Class Crustacea diagnostic features:\n"
        f"- Body: Cephalothorax and abdomen, often covered by a hard calcified carapace.\n"
        f"- Appendages: 5 or more pairs of legs (many have pincers/chelae).\n"
        f"- Antennae: TWO pairs of antennae (unique among arthropods).\n"
        f"- Respiration: Gills (even in terrestrial woodlice).\n\n"
        f"**Step 2:** For '{org_name}', the description is: **{morphology}**."
    )
    return {
        "id": f"ns7_bd_37_{rng.randint(100000, 999999)}",
        "subskill": "37_arthropod_class_crustacea_crabs_prawns",
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
            "tier_1": "Count antennae: Crustaceans uniquely have TWO pairs of antennae.",
            "tier_2": "Crabs and lobsters have 5 pairs of legs (10 legs), gills, and a hard carapace.",
            "tier_3": f"The answer is: {morphology}.",
        },
        "misconception_tags": ["crustacean_antennae_pair_count_error"],
    }


# 38. Arthropod class Myriapoda centipedes millipedes
def arch_38_arthropod_class_myriapoda_centipedes_millipedes(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("Centipedes (Class Chilopoda)", "Flattened body; ONE pair of walking legs per body segment; fast-moving active carnivores possessing venomous poison claws (forcipules) behind the head"),
        ("Millipedes (Class Diplopoda)", "Cylindrical rounded body; TWO pairs of walking legs per body segment (diplosegments); slow-moving herbivores/detritivores that curl into a spiral when threatened and secrete foul defensive chemicals"),
    ]
    target_grp, description = rng.choice(types)
    other_grp, other_desc = (types[1] if target_grp == types[0] else types[0])
    prompt = (
        f"Myriapods have elongated bodies with numerous segments. "
        f"Which statement accurately contrasts '{target_grp[0]}' with '{other_grp[0]}'?"
    )
    correct = f"'{target_grp[0]}' have: {description}."
    distractors = [
        f"'{target_grp[0]}' have: {other_desc}.",
        f"'{target_grp[0]}' have 3 body parts and 6 legs, while '{other_grp[0]}' have wings and stingers.",
        f"'{target_grp[0]}' have soft unsegmented bodies with a ventral muscular creeping foot.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare centipedes and millipedes:\n"
        f"- Centipedes (Chilopoda): 1 pair of legs per segment, flat, fast carnivores with venom claws.\n"
        f"- Millipedes (Diplopoda): 2 pairs of legs per segment, round, slow herbivores that curl up.\n\n"
        f"**Step 2:** For '{target_grp[0]}', the correct description is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_38_{rng.randint(100000, 999999)}",
        "subskill": "38_arthropod_class_myriapoda_centipedes_millipedes",
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
            "tier_1": "Centipedes have 1 pair of legs per segment (fast meat-eater); millipedes have 2 pairs per segment (slow plant-eater).",
            "tier_2": "Look at leg pairs per segment and diet (carnivore vs herbivore).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["centipede_millipede_conflation"],
    }


# 39. Compare four arthropod classes matrix
def arch_39_compare_four_arthropod_classes_matrix(rng: random.Random) -> Dict[str, Any]:
    leg_cases = [
        ("Insecta", "6 legs (3 pairs)", "1 pair", "3 (head, thorax, abdomen)"),
        ("Arachnida", "8 legs (4 pairs)", "0 pairs", "2 (cephalothorax, abdomen)"),
        ("Crustacea", "10+ legs (5+ pairs)", "2 pairs", "2 (cephalothorax, abdomen)"),
        ("Myriapoda", "Many legs (1-2 pairs per segment)", "1 pair", "Many segments (head + trunk)"),
    ]
    target_class, legs, antennae, body_divs = rng.choice(leg_cases)
    specimen_code = rng.choice(["ART-101", "ART-202", "ART-303", "ART-404"])
    accent_col = rng.choice(["#E0F2FE", "#FEF3C7", "#DCFCE7", "#FCE7F3"])

    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 440 220' width='100%' height='220'>"
        f"<rect width='440' height='220' fill='#F8FAFC' rx='8'/>"
        f"<rect x='20' y='15' width='400' height='35' fill='#1E293B' rx='4'/>"
        f"<text x='35' y='38' fill='#FFFFFF' font-size='12' font-weight='bold'>Class</text>"
        f"<text x='130' y='38' fill='#FFFFFF' font-size='12' font-weight='bold'>Legs</text>"
        f"<text x='230' y='38' fill='#FFFFFF' font-size='12' font-weight='bold'>Antennae</text>"
        f"<text x='320' y='38' fill='#FFFFFF' font-size='12' font-weight='bold'>Body Parts [{specimen_code}]</text>"
        f"<rect x='20' y='55' width='400' height='35' fill='{'#FEF08A' if target_class == 'Insecta' else '#E2E8F0'}'/>"
        f"<text x='35' y='78' fill='#0F172A' font-size='11'>Insecta</text>"
        f"<text x='130' y='78' fill='#0F172A' font-size='11'>6 (3 pairs)</text>"
        f"<text x='230' y='78' fill='#0F172A' font-size='11'>1 pair</text>"
        f"<text x='320' y='78' fill='#0F172A' font-size='11'>Head, Thorax, Abd</text>"
        f"<rect x='20' y='95' width='400' height='35' fill='{'#FEF08A' if target_class == 'Arachnida' else accent_col}'/>"
        f"<text x='35' y='118' fill='#0F172A' font-size='11'>Arachnida</text>"
        f"<text x='130' y='118' fill='#0F172A' font-size='11'>8 (4 pairs)</text>"
        f"<text x='230' y='118' fill='#0F172A' font-size='11'>0 pairs</text>"
        f"<text x='320' y='118' fill='#0F172A' font-size='11'>Ceph, Abdomen</text>"
        f"<rect x='20' y='135' width='400' height='35' fill='{'#FEF08A' if target_class == 'Crustacea' else '#E2E8F0'}'/>"
        f"<text x='35' y='158' fill='#0F172A' font-size='11'>Crustacea</text>"
        f"<text x='130' y='158' fill='#0F172A' font-size='11'>10+ (5+ pairs)</text>"
        f"<text x='230' y='158' fill='#0F172A' font-size='11'>2 pairs</text>"
        f"<text x='320' y='158' fill='#0F172A' font-size='11'>Ceph, Abdomen</text>"
        f"<rect x='20' y='175' width='400' height='35' fill='{'#FEF08A' if target_class == 'Myriapoda' else accent_col}'/>"
        f"<text x='35' y='198' fill='#0F172A' font-size='11'>Myriapoda</text>"
        f"<text x='130' y='198' fill='#0F172A' font-size='11'>Many pairs</text>"
        f"<text x='230' y='198' fill='#0F172A' font-size='11'>1 pair</text>"
        f"<text x='320' y='198' fill='#0F172A' font-size='11'>Many segments</text>"
        f"</svg>"
    )
    prompt = (
        f"An unknown specimen labelled {specimen_code} possesses {legs}, {antennae} of antennae, and {body_divs}. "
        f"To which arthropod class does this organism belong?"
    )
    correct = target_class
    options = [target_class] + [c[0] for c in leg_cases if c[0] != target_class]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare against the diagnostic matrix for Phylum Arthropoda:\n"
        f"- Insecta: 6 legs, 1 pair antennae, 3 body parts.\n"
        f"- Arachnida: 8 legs, 0 antennae, 2 body parts.\n"
        f"- Crustacea: 10+ legs, 2 pairs antennae, 2 body parts.\n"
        f"- Myriapoda: Many legs, 1 pair antennae, multi-segmented body.\n\n"
        f"**Step 2:** The organism matches **{target_class}**."
    )
    return {
        "id": f"ns7_bd_39_{rng.randint(100000, 999999)}",
        "subskill": "39_compare_four_arthropod_classes_matrix",
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
            "tier_1": "Count the legs and antennae to determine the class.",
            "tier_2": f"6 legs = Insecta; 8 legs = Arachnida; 10+ legs & 2 pairs antennae = Crustacea; many legs = Myriapoda.",
            "tier_3": f"The class is {target_class}.",
        },
        "misconception_tags": ["arthropod_class_identification_matrix_error"],
    }


# 40. Vertebrate class Pisces fish characteristics
def arch_40_vertebrate_class_pisces_fish_characteristics(rng: random.Random) -> Dict[str, Any]:
    fish_types = [
        ("The coelacanth (Latimeria chalumnae), a living fossil off Sodwana Bay", "lobe-finned fish with paired fleshy lobed fins supported by internal bones, and a primitive lung-like organ"),
        ("The great white shark (Carcharodon carcharias)", "cartilaginous fish (Chondrichthyes) with a skeleton of flexible cartilage, 5 to 7 open gill slits, placoid denticle scales, and no swim bladder"),
        ("The freshwater yellowfish (Labeobarbus polylepis)", "bony fish (Osteichthyes) with an operculum covering its gills, overlapping cycloid scales, a swim bladder, and ray-finned appendages"),
    ]
    fish_name, desc = rng.choice(fish_types)
    prompt = (
        f"Class Pisces comprises all aquatic vertebrates. "
        f"Consider '{fish_name}'. Which statement describes its anatomical adaptations?"
    )
    correct = desc
    options = [desc] + [f[1] for f in fish_types if f[1] != desc]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review vertebrate Class Pisces traits:\n"
        f"- Ectothermic, aquatic, 2-chambered heart (one atrium, one ventricle).\n"
        f"- Respiration via filamentous gills extracting dissolved oxygen.\n"
        f"- Locomotion powered by caudal/pectoral fins and streamlined body.\n\n"
        f"**Step 2:** For '{fish_name}', the correct description is: **{desc}**."
    )
    return {
        "id": f"ns7_bd_40_{rng.randint(100000, 999999)}",
        "subskill": "40_vertebrate_class_pisces_fish_characteristics",
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
            "tier_1": "Is it a lobe-finned coelacanth, a cartilaginous shark, or a bony yellowfish?",
            "tier_2": "Sharks have cartilage skeletons and open gill slits; yellowfish have bony skeletons and an operculum.",
            "tier_3": f"The answer is: {desc}.",
        },
        "misconception_tags": ["cartilaginous_vs_bony_fish_confusion"],
    }


# 41. Vertebrate class Amphibia frogs metamorphosis
def arch_41_vertebrate_class_amphibia_frogs_metamorphosis(rng: random.Random) -> Dict[str, Any]:
    stages = [
        ("Aquatic tadpole stage", "swims with a flattened tail, breathes with external/internal gills, and feeds as a herbivorous grazer without limbs"),
        ("Terrestrial adult frog stage", "possesses four limbs for leaping, breathes using lungs and moist vascularized skin (cutaneous respiration), and hunts as a carnivorous predator"),
    ]
    stage_name, details = rng.choice(stages)
    alt_stage = stages[1] if stage_name == stages[0] else stages[0]
    prompt = (
        f"The name 'Amphibia' means 'dual life' (living both in water and on land). "
        f"In the life cycle of the common river frog (Amietia delalandii), which statement accurately describes the '{stage_name}'?"
    )
    correct = details
    options = [
        details,
        alt_stage[1],
        "Enclosed inside a hard calcareous shelled egg laid in dry desert sand with zero water.",
        "A winged flying animal with hollow bones and a four-chambered heart.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review amphibian metamorphosis:\n"
        f"- Egg -> Aquatic tadpole (gills, tail, no legs, herbivore).\n"
        f"- Metamorphosis -> Terrestrial adult (lungs, cutaneous skin breathing, 4 legs, carnivore, 3-chambered heart).\n\n"
        f"**Step 2:** The description of '{stage_name}' is: **{details}**."
    )
    return {
        "id": f"ns7_bd_41_{rng.randint(100000, 999999)}",
        "subskill": "41_vertebrate_class_amphibia_frogs_metamorphosis",
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
            "tier_1": "Tadpoles have gills and tails; adult frogs have legs, lungs, and moist skin.",
            "tier_2": "Look at whether the question asks about the swimming tadpole or leaping adult.",
            "tier_3": f"The answer is: {details}.",
        },
        "misconception_tags": ["amphibian_metamorphosis_stage_error"],
    }


# 42. Vertebrate class Reptilia scaly skin amniotic egg
def arch_42_vertebrate_class_reptilia_scaly_skin_amniotic_egg(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Class Reptilia includes snakes, lizards, tortoises, and crocodiles. "
        f"What two key evolutionary adaptations allowed reptiles to break free completely from aquatic environments and live on dry land?"
    )
    correct = "Dry waterproof skin covered in keratin scales to prevent desiccation, and an amniotic egg with a protective leathery shell that prevents the embryo from drying out."
    options = [
        correct,
        "Gills that extract oxygen from air, and laying soft jelly-covered eggs in water.",
        "Endothermic warm-blooded metabolism, and wings modified for long-distance flight.",
        "Mammary glands that produce milk, and giving birth to live young that breathe through skin.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify adaptations for dry land in Reptilia:\n"
        f"1. Keratin scales: waterproof barrier stopping cutaneous water loss.\n"
        f"2. Amniotic egg: contains amnion and yolk inside a leathery waterproof shell, eliminating the need to lay eggs in water.\n"
        f"3. Internal fertilization and efficient lungs.\n\n"
        f"**Step 2:** The two key adaptations are: **{correct}**."
    )
    return {
        "id": f"ns7_bd_42_{rng.randint(100000, 999999)}",
        "subskill": "42_vertebrate_class_reptilia_scaly_skin_amniotic_egg",
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
            "tier_1": "Think about what prevents a reptile from drying out in the desert sun (scaly skin and shelled eggs).",
            "tier_2": "Waterproof keratin scales and leathery amniotic eggs laid on dry land.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["reptilian_amniotic_egg_misunderstanding"],
    }


# 43. Vertebrate class Aves birds flight adaptations
def arch_43_vertebrate_class_aves_birds_flight_adaptations(rng: random.Random) -> Dict[str, Any]:
    adaptations = [
        ("Pneumatic (hollow) bones with internal honeycomb struts", "drastically reducing overall skeleton weight while maintaining structural strength against flight forces"),
        ("A massive keeled sternum (breastbone)", "providing an extensive anchoring surface for powerful pectoral flight muscles powering wing strokes"),
        ("Keratinized feathers (contour and flight remiges)", "providing lightweight aerodynamic lift, streamlining the body contour, and insulating against high-altitude thermal loss"),
        ("A toothless keratinous beak and internal muscular gizzard", "eliminating heavy jaw bones and teeth from the skull, shifting digestive grinding to the bird's centre of gravity"),
    ]
    feat, benefit = rng.choice(adaptations)
    prompt = (
        f"Class Aves (birds) possess extreme skeletal and anatomical specializations for powered flight. "
        f"What is the functional advantage of '{feat}'?"
    )
    correct = benefit
    options = [benefit] + [a[1] for a in adaptations if a[1] != benefit]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review avian flight adaptations:\n"
        f"- Hollow bones: lightweight skeleton.\n"
        f"- Keeled sternum: anchor for pectoralis muscles.\n"
        f"- Feathers: aerodynamic lift and thermal insulation.\n"
        f"- Toothless beak / gizzard: lowers skull weight.\n\n"
        f"**Step 2:** For '{feat}', the advantage is: **{benefit}**."
    )
    return {
        "id": f"ns7_bd_43_{rng.randint(100000, 999999)}",
        "subskill": "43_vertebrate_class_aves_birds_flight_adaptations",
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
            "tier_1": "Match the bone/feather feature directly to its aerodynamic or weight-saving role.",
            "tier_2": "Hollow bones reduce weight; keeled sternum anchors flight muscles; beak eliminates heavy teeth.",
            "tier_3": f"The answer is: {benefit}.",
        },
        "misconception_tags": ["avian_flight_adaptation_confusion"],
    }


# 44. Vertebrate class Mammalia hair and mammary glands
def arch_44_vertebrate_class_mammalia_hair_and_mammary_glands(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Class Mammalia contains animals ranging from mice to blue whales. "
        f"Which two biological features are found exclusively in mammals and in NO other vertebrate class?"
    )
    correct = "Body hair (fur) and mammary glands that produce milk to nourish newborn young."
    options = [
        correct,
        "A four-chambered heart and endothermic (warm-blooded) regulation of body temperature.",
        "Lungs for gas exchange and internal bony skeletons with backbones.",
        "Claws on digits and amniotic eggs that hatch outside the parent body.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify unique diagnostic mammalian features:\n"
        f"- Hair/fur: unique to mammals (birds have feathers, reptiles have scales).\n"
        f"- Mammary glands: produce nutrient-rich milk for young (found only in mammals).\n"
        f"- Note: 4-chambered hearts and endothermy are shared with birds, and backbones are shared with all vertebrates.\n\n"
        f"**Step 2:** The two exclusive traits are: **{correct}**."
    )
    return {
        "id": f"ns7_bd_44_{rng.randint(100000, 999999)}",
        "subskill": "44_vertebrate_class_mammalia_hair_and_mammary_glands",
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
            "tier_1": "Think about what words like 'mammal' and 'fur' come from.",
            "tier_2": "Only mammals have mammary glands (milk) and true hair/fur.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["mammalian_unique_traits_misconception"],
    }


# 45. Ectothermic vs endothermic vertebrates
def arch_45_ectothermic_vs_endothermic_vertebrates(rng: random.Random) -> Dict[str, Any]:
    groups = [
        ("Endothermic vertebrates (Birds and Mammals)", "generate metabolic heat internally from food oxidation and maintain a stable constant core body temperature regardless of ambient environmental fluctuations"),
        ("Ectothermic vertebrates (Fish, Amphibians, and Reptiles)", "rely primarily on external thermal energy sources (e.g. basking in sunlight) to regulate body temperature, with their metabolic rate varying with ambient temperature"),
    ]
    target_grp, description = rng.choice(groups)
    prompt = (
        f"Vertebrates regulate their body temperature through either ectothermy or endothermy. "
        f"Which statement scientifically explains '{target_grp}'?"
    )
    correct = description
    options = [description] + [g[1] for g in groups if g[1] != description] + [
        "Animals that have no body temperature and freeze solid during every meal.",
        "Animals that use nuclear radiation inside bone marrow to stay warm.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Contrast ectothermy and endothermy:\n"
        f"- Ectotherms ('cold-blooded'): Fish, amphibians, reptiles rely on external heat.\n"
        f"- Endotherms ('warm-blooded'): Birds and mammals generate internal heat via high metabolic rates.\n\n"
        f"**Step 2:** For '{target_grp}', the mechanism is: **{description}**."
    )
    return {
        "id": f"ns7_bd_45_{rng.randint(100000, 999999)}",
        "subskill": "45_ectothermic_vs_endothermic_vertebrates",
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
            "tier_1": "Endo = inside (heat made inside); Ecto = outside (heat from outside).",
            "tier_2": "Birds and mammals are endotherms; reptiles, fish, and frogs are ectotherms.",
            "tier_3": f"The answer is: {description}.",
        },
        "misconception_tags": ["cold_blooded_literal_misinterpretation"],
    }


# 46. Vertebrate egg adaptations jelly vs leathery vs calcareous
def arch_46_vertebrate_egg_adaptations_jelly_vs_leathery_vs_calcareous(rng: random.Random) -> Dict[str, Any]:
    egg_types = [
        ("Amphibian eggs (e.g. river frog)", "soft, shell-less eggs surrounded by a clear gelatinous capsule that must be laid in water to prevent drying out and allow gas diffusion"),
        ("Reptilian eggs (e.g. leopard tortoise)", "flexible, leathery waterproof shells laid in warm sandy soil nests on land, protecting the embryo and yolk from dehydration"),
        ("Avian bird eggs (e.g. ostrich)", "rigid, hard porous calcareous (calcium carbonate) shells laid in nests, supporting incubation by brooding parents while allowing oxygen entry"),
    ]
    egg_name, egg_desc = rng.choice(egg_types)
    prompt = (
        f"Egg structures evolved dramatically as vertebrates transitioned from aquatic habitats to land. "
        f"Which statement describes the reproductive adaptation of '{egg_name}'?"
    )
    correct = egg_desc
    options = [egg_desc] + [e[1] for e in egg_types if e[1] != egg_desc]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review egg evolutionary transitions:\n"
        f"- Amphibian eggs: gelatinous, no shell, must stay in water.\n"
        f"- Reptile eggs: leathery shell, prevents drying out on land.\n"
        f"- Bird eggs: hard calcareous shell, protects embryo and supports brooding.\n\n"
        f"**Step 2:** For '{egg_name}', the adaptation is: **{egg_desc}**."
    )
    return {
        "id": f"ns7_bd_46_{rng.randint(100000, 999999)}",
        "subskill": "46_vertebrate_egg_adaptations_jelly_vs_leathery_vs_calcareous",
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
            "tier_1": "Frog eggs are jelly balls in water; reptile eggs are leathery; bird eggs are hard shells.",
            "tier_2": "Match the named animal egg to its shell type (jelly, leathery, hard calcareous).",
            "tier_3": f"The answer is: {egg_desc}.",
        },
        "misconception_tags": ["egg_type_evolutionary_transition"],
    }


# 47. Dichotomous key navigation step by step
def arch_47_dichotomous_key_navigation_step_by_step(rng: random.Random) -> Dict[str, Any]:
    specimens = [
        ("Specimen X: Wings present, 6 legs, 1 pair of antennae", "Insect (e.g. honeybee)", "1a -> 2a"),
        ("Specimen Y: Wings absent, 8 legs, 0 antennae", "Arachnid (e.g. spider)", "1b -> 3a"),
        ("Specimen Z: Wings absent, 10 legs, 2 pairs of antennae", "Crustacean (e.g. crab)", "1b -> 3b"),
    ]
    target_specimen, identity, path = rng.choice(specimens)
    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 460 220' width='100%' height='220'>"
        f"<rect width='460' height='220' fill='#F1F5F9' rx='8'/>"
        f"<rect x='20' y='15' width='420' height='30' fill='#0F172A' rx='4'/>"
        f"<text x='30' y='35' fill='#FFFFFF' font-size='11' font-weight='bold'>Step 1: Wings present? (Yes -> Go to 2 | No -> Go to 3)</text>"
        f"<rect x='20' y='60' width='420' height='40' fill='#334155' rx='4'/>"
        f"<text x='30' y='78' fill='#FFFFFF' font-size='10'>Step 2a: 6 walking legs ........................................... Insect</text>"
        f"<text x='30' y='93' fill='#FFFFFF' font-size='10'>Step 2b: More than 6 walking legs ........................... Other</text>"
        f"<rect x='20' y='115' width='420' height='40' fill='#475569' rx='4'/>"
        f"<text x='30' y='133' fill='#FFFFFF' font-size='10'>Step 3a: 8 walking legs, 0 antennae ...................... Arachnid</text>"
        f"<text x='30' y='148' fill='#FFFFFF' font-size='10'>Step 3b: 10 walking legs, 2 pairs antennae ......... Crustacean</text>"
        f"<text x='30' y='190' fill='#0369A1' font-size='12' font-weight='bold'>Query: {target_specimen.split(':')[0]}</text>"
        f"</svg>"
    )
    prompt = (
        f"A learner navigates a dichotomous key to identify an unknown arthropod with the following features: '{target_specimen}'. "
        f"Using the dichotomous couplets, identify the specimen."
    )
    correct = identity
    options = [identity] + [s[1] for s in specimens if s[1] != identity] + ["Annelid (earthworm)"]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace the specimen through the dichotomous couplets:\n"
        f"- {target_specimen}\n"
        f"- Navigation path: {path}.\n\n"
        f"**Step 2:** The specimen is correctly identified as **{identity}**."
    )
    return {
        "id": f"ns7_bd_47_{rng.randint(100000, 999999)}",
        "subskill": "47_dichotomous_key_navigation_step_by_step",
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
            "tier_1": "Follow the clues step-by-step: Step 1 leads to either Step 2 or Step 3.",
            "tier_2": "Wings present leads to Insect; 8 legs and no antennae leads to Arachnid.",
            "tier_3": f"The answer is: {identity}.",
        },
        "misconception_tags": ["dichotomous_key_navigation_error"],
    }


# 48. Dichotomous key construction from traits
def arch_48_dichotomous_key_construction_from_traits(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When constructing a biological dichotomous key, what fundamental structural rule must always be followed?"
    )
    correct = "Each step must present exactly two mutually exclusive, contrasting choices (couplets) based on clear, observable morphological characteristics."
    options = [
        correct,
        "Each step must offer five vague opinions about how cute the organism looks.",
        "The key must rely strictly on guessing where the organism was born without looking at its body.",
        "All organisms in the key must be placed into the exact same terminal group regardless of traits.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review rules for dichotomous keys ('di' = two):\n"
        f"1. Exactly two contrasting statements per couplet (e.g. 1a vs 1b).\n"
        f"2. Choices must be mutually exclusive and based on observable physical traits (e.g. 'wings present' vs 'wings absent').\n"
        f"3. Avoid subjective terms like 'large' or 'pretty'.\n\n"
        f"**Step 2:** The fundamental rule is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_48_{rng.randint(100000, 999999)}",
        "subskill": "48_dichotomous_key_construction_from_traits",
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
            "tier_1": "Notice the prefix 'di-' means two.",
            "tier_2": "A dichotomous key always provides pairs of opposite, observable physical choices.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["dichotomous_key_rule_violation"],
    }


# 49. Dichotomous key arthropod identification
def arch_49_dichotomous_key_arthropod_identification(rng: random.Random) -> Dict[str, Any]:
    specimens = [
        ("An animal with 2 body parts, 8 walking legs, chelicerae, and no wings", "Arachnid (spider/scorpion)"),
        ("An animal with 3 body parts, 6 walking legs, 1 pair of antennae, and wings", "Insect (butterfly/bee)"),
        ("An animal with a hard calcified carapace, 10 legs with pincers, and 2 pairs of antennae", "Crustacean (crab/crayfish)"),
        ("An animal with an elongated multi-segmented body with 2 pairs of legs per segment", "Myriapod (millipede)"),
    ]
    traits, classification = rng.choice(specimens)
    prompt = (
        f"A learner examines a leaf litter organism and records the following observation: '{traits}'. "
        f"Which arthropod group does this specimen belong to?"
    )
    correct = classification
    options = [classification] + [s[1] for s in specimens if s[1] != classification]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Match observable traits to arthropod classes:\n"
        f"- 6 legs = Insect.\n"
        f"- 8 legs, 2 body parts = Arachnid.\n"
        f"- 10 legs, 2 pairs antennae = Crustacean.\n"
        f"- Multi-segmented, 2 pairs legs/segment = Myriapod (millipede).\n\n"
        f"**Step 2:** '{traits}' identifies: **{classification}**."
    )
    return {
        "id": f"ns7_bd_49_{rng.randint(100000, 999999)}",
        "subskill": "49_dichotomous_key_arthropod_identification",
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
            "tier_1": "Check the leg count first: 6, 8, 10, or many?",
            "tier_2": "8 legs = Arachnid; 6 legs = Insect; 10 legs = Crustacean; many legs = Myriapod.",
            "tier_3": f"The answer is: {classification}.",
        },
        "misconception_tags": ["arthropod_identification_error"],
    }


# 50. Synthetic biodiversity case study ecosystem stability
def arch_50_synthetic_biodiversity_case_study_ecosystem_stability(rng: random.Random) -> Dict[str, Any]:
    ecosystems = [
        ("A diverse natural Fynbos ecosystem with 120 coexisting plant species and diverse pollinators", "A monoculture pine plantation with only 1 tree species and minimal undergrowth"),
        ("A complex marine coral reef with hundreds of fish and invertebrate species", "An artificial commercial salmon farm with only 1 species in high density"),
    ]
    diverse_eco, simple_eco = rng.choice(ecosystems)
    prompt = (
        f"Compare {diverse_eco} against {simple_eco}. "
        f"When an invasive fungal disease or severe drought strikes, why does the high-biodiversity ecosystem demonstrate far greater resilience and stability?"
    )
    correct = "Because complex ecosystems have redundant ecological niches and high genetic variation; if one species is suppressed by disease, other resistant species continue performing primary production, pollination, and nutrient cycling."
    options = [
        correct,
        "Because diverse ecosystems possess a magic forcefield that blocks all abiotic weather events.",
        "Because monoculture plantations are biologically superior and never suffer from diseases or pests.",
        "Because animals in diverse ecosystems do not require water, food, or oxygen to survive.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Connect biodiversity to ecosystem resilience:\n"
        f"- High biodiversity provides ecological redundancy (multiple species fulfilling similar functional roles).\n"
        f"- Monocultures are extremely vulnerable to total collapse when a single pathogen or drought event strikes.\n\n"
        f"**Step 2:** The scientific rationale is: **{correct}**."
    )
    return {
        "id": f"ns7_bd_50_{rng.randint(100000, 999999)}",
        "subskill": "50_synthetic_biodiversity_case_study_ecosystem_stability",
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
            "tier_1": "Think about not putting all your eggs in one basket.",
            "tier_2": "A forest with 100 species survives a disease that kills 1 species; a plantation of 1 species dies completely.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["biodiversity_stability_relationship_error"],
    }
