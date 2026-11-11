"""Grade 9 Natural Sciences: Term 1 - Cells as the Basic Units of Life (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 1/01. Cells as the basic units of life.md.
Focus: Organelle physiology, cellular hierarchy, specialized cells, and practical microscopy investigations.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Nucleus chromatin DNA and hereditary control centre
def arch_26_nucleus_chromatin_dna_and_hereditary_control_centre(rng: random.Random) -> Dict[str, Any]:
    functions = [
        ("encloses linear chromosomes composed of deoxyribonucleic acid (DNA)", "stores genetic instructions for synthesizing all cellular proteins"),
        ("contains the dense nucleolus", "synthesizes ribosomal RNA (rRNA) and assembles ribosome subunits"),
        ("is enveloped by a double nuclear membrane with nuclear pores", "controls the transport of macromolecules between the nucleoplasm and cytoplasm"),
    ]
    target_comp, target_role = rng.choice(functions)
    prompt = (
        f"The nucleus is often described as the **control centre of the eukaryotic cell**.\n\n"
        f"Which statement scientifically explains how the nuclear component **{target_comp}** fulfills this role?"
    )
    correct = f"It {target_role}."
    alt = [f[1] for f in functions if f[0] != target_comp]
    distractors = [f"It {r}." for r in alt]
    distractors.append("It burns glucose in flames to heat the cell to 100 °C.")
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze nuclear ultrastructure and function:\n"
        f"- The nucleus contains hereditary material (DNA/chromatin).\n"
        f"- For {target_comp}: {target_role}.\n\n"
        f"**Step 2:** The accurate functional explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_26_{rng.randint(100000, 999999)}",
        "subskill": "26_nucleus_chromatin_dna_and_hereditary_control_centre",
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
            "tier_1": f"What specific function is carried out by {target_comp}?",
            "tier_2": "The nucleus controls cellular activities by directing protein synthesis via DNA.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["nucleus_genetic_control_mechanism_misconception"],
    }


# 27. Cytoplasm cytosol medium for metabolic biochemical reactions
def arch_27_cytoplasm_cytosol_medium_for_metabolic_biochemical_reactions(rng: random.Random) -> Dict[str, Any]:
    reactions = [
        ("glycolysis (initial breakdown of glucose into pyruvate)", "anaerobic stage of cellular respiration"),
        ("translation of mRNA into polypeptides on ribosomes", "protein synthesis"),
        ("cytoplasmic streaming (cyclosis)", "distribution of nutrients and organelles throughout the cell"),
    ]
    target_rxn, pathway = rng.choice(reactions)
    prompt = (
        f"The cytoplasm consists of a semi-fluid jelly-like cytosol in which organelles are suspended.\n\n"
        f"What critical biological role does the cytoplasm serve regarding **{target_rxn}** ({pathway})?"
    )
    correct = (
        f"It provides a fluid, aqueous environment with dissolved enzymes, salts, and organic solutes "
        f"where {target_rxn} can take place efficiently."
    )
    options = [
        correct,
        "It acts as a vacuum chamber with zero water molecules where no chemical reactions can ever occur.",
        "It converts all cellular proteins into radioactive uranium to power the cell.",
        "It freezes all cellular contents into solid rock crystals to prevent movement.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the properties and role of cytoplasm:\n"
        f"- Cytosol is ~80% water containing ions, glucose, amino acids, and dissolved enzymes.\n"
        f"- It acts as the medium for vital metabolic reactions like {target_rxn}.\n\n"
        f"**Step 2:** The primary role is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_27_{rng.randint(100000, 999999)}",
        "subskill": "27_cytoplasm_cytosol_medium_for_metabolic_biochemical_reactions",
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
            "tier_1": "What is the physical state of the cytoplasm, and why is liquid water essential?",
            "tier_2": "The cytoplasm provides an aqueous medium for cellular enzymes and metabolic reactions.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cytoplasm_metabolic_medium_misconception"],
    }


# 28. Mitochondria cellular respiration ATP energy powerhouse
def arch_28_mitochondria_cellular_respiration_atp_energy_powerhouse(rng: random.Random) -> Dict[str, Any]:
    cells = [
        ("active mammalian heart muscle cells (cardiomyocytes)", "thousands of densely packed mitochondria", "continuous ATP required for rhythmic pumping"),
        ("human sperm cells", "a spiral collar of mitochondria in the midpiece", "ATP needed to power flagellar swimming towards the ovum"),
        ("flight muscle cells of birds and flying insects", "dense cristae-rich mitochondria", "high-energy output for sustained flight"),
    ]
    cell_name, density, reason = rng.choice(cells)
    prompt = (
        f"Mitochondria are often referred to as the **powerhouses of the cell**.\n\n"
        f"Why do **{cell_name}** contain {density}?"
    )
    correct = (
        f"Mitochondria carry out aerobic cellular respiration, breaking down glucose in the presence of oxygen "
        f"to produce adenosine triphosphate (ATP); {cell_name} have very high metabolic activity and need {reason}."
    )
    options = [
        correct,
        f"Mitochondria carry out photosynthesis to produce green chlorophyll for {cell_name}.",
        f"Mitochondria freeze water into ice to store {cell_name} during cold weather.",
        f"Mitochondria produce toxic sulfur gas to kill surrounding animal tissues.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review mitochondrial function:\n"
        f"- Cellular respiration word equation:\n"
        f"  $$\\text{{Glucose}} + \\text{{Oxygen}} \\rightarrow \\text{{Carbon Dioxide}} + \\text{{Water}} + \\text{{ATP}}$$\n"
        f"- Cells with high metabolic demands ({cell_name}) require abundant mitochondria to synthesize sufficient ATP.\n\n"
        f"**Step 2:** The accurate explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_28_{rng.randint(100000, 999999)}",
        "subskill": "28_mitochondria_cellular_respiration_atp_energy_powerhouse",
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
            "tier_1": "What energy molecule do mitochondria generate during respiration?",
            "tier_2": "Mitochondria produce ATP via cellular respiration, powering cells with high energy requirements.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["mitochondria_energy_respiration_misconception"],
    }


# 29. Chloroplasts chlorophyll and photosynthetic sugar synthesis
def arch_29_chloroplasts_chlorophyll_and_photosynthetic_sugar_synthesis(rng: random.Random) -> Dict[str, Any]:
    tissues = [
        ("palisade mesophyll cells in leaves", "abundant chloroplasts packed densely near the upper surface", "maximize radiant light absorption for photosynthesis"),
        ("root cortex cells underground", "zero chloroplasts", "underground tissues receive no sunlight and carry out no photosynthesis"),
        ("guard cells surrounding leaf stomata", "moderate numbers of chloroplasts", "generate ATP and sugars needed to regulate stomatal opening and closing"),
    ]
    tissue_name, count_feat, adapt = rng.choice(tissues)
    prompt = (
        f"Chloroplasts are green double-membraned plastids containing internal disc-like thylakoids and chlorophyll.\n\n"
        f"Why do **{tissue_name}** exhibit {count_feat}?"
    )
    correct = f"Because chloroplasts trap radiant light energy to synthesize glucose from carbon dioxide and water; {adapt}."
    options = [
        correct,
        "Because chloroplasts are digestive stomachs that ingest whole insects inside plant roots.",
        "Because chloroplasts are magnetic poles that align the plant with Earth's gravitational center.",
        "Because chloroplasts absorb sound waves from singing birds to make flowers bloom.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze chloroplast physiology:\n"
        f"- Photosynthesis equation:\n"
        f"  $$\\text{{Carbon dioxide}} + \\text{{Water}} + \\text{{Light Energy}} \\rightarrow \\text{{Glucose}} + \\text{{Oxygen}}$$\n"
        f"- Chloroplast distribution relates directly to light availability and functional need ({adapt}).\n\n"
        f"**Step 2:** For {tissue_name}: **{correct}**."
    )
    return {
        "id": f"ns9_cell_29_{rng.randint(100000, 999999)}",
        "subskill": "29_chloroplasts_chlorophyll_and_photosynthetic_sugar_synthesis",
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
            "tier_1": f"Do {tissue_name} receive sunlight, and what is the function of chloroplasts?",
            "tier_2": "Chloroplasts capture light energy for photosynthesis; their presence matches light exposure and function.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["chloroplast_distribution_photosynthesis_misconception"],
    }


# 30. Large central sap vacuole tonoplast and osmotic turgidity
def arch_30_large_central_sap_vacuole_tonoplast_and_osmotic_turgidity(rng: random.Random) -> Dict[str, Any]:
    states = [
        (
            "well-watered herbaceous plant cells",
            "hypertonic cell sap draws water in by osmosis, swelling the central vacuole against the rigid cell wall",
            "the cell becomes firm and turgid, keeping leaves upright and stems erect without woody bark",
        ),
        (
            "severely drought-stressed or dehydrated plant cells",
            "water leaves the central vacuole by osmosis, causing vacuolar shrinkage and loss of hydrostatic pressure",
            "the cell becomes flaccid (plasmolysis), causing the plant shoot to wilt and droop",
        ),
    ]
    condition, mechanism, result = rng.choice(states)
    prompt = (
        f"In mature plant cells, the **large central vacuole** is bounded by the selectively permeable tonoplast membrane.\n\n"
        f"In **{condition}**, what happens to the central vacuole and how does it affect the mechanical state of the plant?"
    )
    correct = f"Mechanism: {mechanism}.\nResult: {result}."
    alt = [s for s in states if s[0] != condition][0]
    options = [
        correct,
        f"Mechanism: {alt[1]}.\nResult: {alt[2]}.",
        "Mechanism: The vacuole boils into carbon gas.\nResult: The plant turns into molten lava.",
        "Mechanism: The vacuole divides into ten thousand seeds.\nResult: The plant flies away.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze vacuolar hydrostatic dynamics:\n"
        f"- The central vacuole contains cell sap (water, dissolved sugars, amino acids, mineral ions).\n"
        f"- Water movement by osmosis creates internal turgor pressure against the cell wall.\n"
        f"- In {condition}: {mechanism} -> {result}.\n\n"
        f"**Step 2:** The accurate physiological outcome is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_30_{rng.randint(100000, 999999)}",
        "subskill": "30_large_central_sap_vacuole_tonoplast_and_osmotic_turgidity",
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
            "tier_1": f"What happens to plant turgor pressure in {condition}?",
            "tier_2": "The vacuole maintains turgidity in watered plants; loss of water causes flaccidity and wilting.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["vacuole_turgor_pressure_wilting_misconception"],
    }


# 31. Ribosomes site of protein synthesis
def arch_31_ribosomes_site_of_protein_synthesis(rng: random.Random) -> Dict[str, Any]:
    proteins = [
        ("digestive enzymes like amylase and pepsin", "catalyze hydrolysis of macronutrients"),
        ("hormones like insulin", "regulate cellular glucose uptake in blood"),
        ("structural proteins like collagen and keratin", "provide tensile strength to connective tissues and skin"),
        ("antibodies produced by white blood cells", "neutralize pathogenic foreign antigens"),
    ]
    prot_name, prot_role = rng.choice(proteins)
    prompt = (
        f"Cells require vast quantities of proteins such as {prot_name} ({prot_role}).\n\n"
        f"Which microscopic non-membrane-bound organelles serve as the primary site of **protein synthesis** in all living cells?"
    )
    correct = "Ribosomes"
    options = [correct, "Lysosomes", "Centrosomes", "Peroxisomes"]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify the organelle responsible for protein synthesis:\n"
        f"- Ribosomes translate messenger RNA (mRNA) into polypeptide chains using amino acids.\n"
        f"- They exist free in the cytoplasm (synthesizing intracellular proteins) or attached to the rough endoplasmic reticulum (synthesizing secretory or membrane proteins).\n\n"
        f"**Step 2:** The correct organelle is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_31_{rng.randint(100000, 999999)}",
        "subskill": "31_ribosomes_site_of_protein_synthesis",
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
            "tier_1": "Which organelle translates mRNA into chains of amino acids?",
            "tier_2": "Ribosomes are the universal protein-making factories of the cell.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ribosome_protein_synthesis_identification_misconception"],
    }


# 32. Endoplasmic reticulum rough vs smooth transport channels
def arch_32_endoplasmic_reticulum_rough_vs_smooth_transport_channels(rng: random.Random) -> Dict[str, Any]:
    types = [
        (
            "Rough Endoplasmic Reticulum (Rough ER)",
            "Studded with ribosomes on its outer surface; folds and transports newly synthesized proteins into transport vesicles destined for the Golgi apparatus.",
        ),
        (
            "Smooth Endoplasmic Reticulum (Smooth ER)",
            "Lacks ribosomes; synthesizes lipids and phospholipids, metabolizes carbohydrates, and detoxifies drugs and chemical poisons.",
        ),
    ]
    target_er, feature = rng.choice(types)
    prompt = (
        f"The endoplasmic reticulum (ER) forms an extensive membranous network of tubules and cisternae throughout the eukaryotic cell.\n\n"
        f"Which structural and functional description correctly defines **{target_er}**?"
    )
    correct = feature
    other_feat = [t[1] for t in types if t[0] != target_er][0]
    options = [
        correct,
        other_feat,
        "It is an open hole in the outer cell wall that releases all genetic material into the air.",
        "It acts as an optical lens that focuses sunlight directly onto the chromosomes.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish rough ER vs smooth ER:\n"
        f"- Rough ER has ribosomes -> protein folding and transport.\n"
        f"- Smooth ER lacks ribosomes -> lipid synthesis and detoxification.\n\n"
        f"**Step 2:** For {target_er}: **{correct}**."
    )
    return {
        "id": f"ns9_cell_32_{rng.randint(100000, 999999)}",
        "subskill": "32_endoplasmic_reticulum_rough_vs_smooth_transport_channels",
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
            "tier_1": f"Does {target_er} have ribosomes attached to its membrane?",
            "tier_2": "Rough ER has ribosomes for protein transport; Smooth ER lacks ribosomes and synthesizes lipids.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["rough_vs_smooth_er_distinction_misconception"],
    }


# 33. Golgi body packaging sorting and secretory vesicles
def arch_33_golgi_body_packaging_sorting_and_secretory_vesicles(rng: random.Random) -> Dict[str, Any]:
    secretions = [
        ("pancreatic acinar cells secreting digestive enzymes into the duodenum", "copious Golgi complexes", "processing and packaging enzymes into secretory zymogen granules"),
        ("mucus-secreting goblet cells lining the respiratory epithelium", "highly developed Golgi bodies", "synthesizing mucin glycoproteins and budding off mucus vesicles"),
    ]
    cell_ex, g_feat, role = rng.choice(secretions)
    prompt = (
        f"Consider **{cell_ex}**, which exhibit {g_feat}.\n\n"
        f"What is the biological function of the **Golgi apparatus (Golgi body)** in these secretory cells?"
    )
    correct = (
        f"It chemically modifies, sorts, and packages proteins received from the rough ER into membrane-bound vesicles "
        f"for {role} or incorporation into the plasma membrane."
    )
    options = [
        correct,
        "It breaks down glucose to produce carbon dioxide during photosynthesis.",
        "It stores genetic chromosomes in long coils during cellular division.",
        "It turns all cell water into mineral salt crystals to preserve the tissue.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the physiological function of the Golgi body:\n"
        f"- The Golgi apparatus acts as the cell's 'post office'.\n"
        f"- It receives transport vesicles from the rough ER, adds carbohydrate chains (glycosylation), sorts, and packages products into secretory vesicles for exocytosis.\n\n"
        f"**Step 2:** The correct statement is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_33_{rng.randint(100000, 999999)}",
        "subskill": "33_golgi_body_packaging_sorting_and_secretory_vesicles",
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
            "tier_1": "Which organelle acts as the packaging and distribution centre of the cell?",
            "tier_2": "The Golgi apparatus modifies, sorts, and packages proteins into secretory vesicles.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["golgi_apparatus_secretion_packaging_misconception"],
    }


# 34. Biological hierarchy organelles cells tissues organs systems
def arch_34_biological_hierarchy_organelles_cells_tissues_organs_systems(rng: random.Random) -> Dict[str, Any]:
    levels = [
        ("Organelle", "A specialized microscopic subcellular structure with a specific function (e.g. mitochondrion)"),
        ("Cell", "The basic structural and functional living unit of life (e.g. cardiac muscle cell)"),
        ("Tissue", "A group of similar specialized cells working together to perform a specific function (e.g. cardiac muscle tissue)"),
        ("Organ", "A group of different tissues joined structurally to perform complex physiological activities (e.g. the heart)"),
        ("Organ System", "A group of cooperating organs working together to carry out major body functions (e.g. the circulatory system)"),
        ("Organism", "A complete, individual living entity composed of cooperating organ systems (e.g. a human)"),
    ]
    target_lvl, target_def = rng.choice(levels)
    prompt = (
        f"Multicellular life is structured in a precise **hierarchical levels of organization**:\n"
        f"$$\\text{{Organelle}} \\rightarrow \\text{{Cell}} \\rightarrow \\text{{Tissue}} \\rightarrow \\text{{Organ}} \\rightarrow \\text{{Organ System}} \\rightarrow \\text{{Organism}}$$\n\n"
        f"Which definition and example correctly defines the level: **{target_lvl}**?"
    )
    correct = target_def
    other_defs = [l[1] for l in levels if l[0] != target_lvl]
    options = [correct] + rng.sample(other_defs, 3)
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review the biological hierarchy:\n"
        f"- Organelle < Cell < Tissue < Organ < Organ System < Organism.\n"
        f"- For {target_lvl}: {target_def}.\n\n"
        f"**Step 2:** The correct definition is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_34_{rng.randint(100000, 999999)}",
        "subskill": "34_biological_hierarchy_organelles_cells_tissues_organs_systems",
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
            "tier_1": f"Where does {target_lvl} sit in the hierarchy from organelle to organism?",
            "tier_2": f"Match {target_lvl} to its biological definition.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["biological_hierarchy_levels_misconception"],
    }


# 35. Tissues definition and examples in plants and animals
def arch_35_tissues_definition_and_examples_in_plants_and_animals(rng: random.Random) -> Dict[str, Any]:
    kingdoms = [
        (
            "Plants",
            "Epidermal tissue (protective outer layer), Xylem tissue (water transport and support), and Palisade mesophyll tissue (photosynthesis)",
        ),
        (
            "Animals",
            "Epithelial tissue (protective linings), Connective tissue (blood and bone support), Muscle tissue (contraction), and Nervous tissue (impulse transmission)",
        ),
    ]
    target_k, examples = rng.choice(kingdoms)
    prompt = (
        f"In biological hierarchy, a **tissue** is formed by groups of specialized cells working cooperatively.\n\n"
        f"Which group of biological tissues represents major tissue types in **{target_k}**?"
    )
    correct = examples
    other_ex = [k[1] for k in kingdoms if k[0] != target_k][0]
    options = [
        correct,
        other_ex,
        "Plastic polymer tissue, copper wiring tissue, and glass window tissue",
        "Volcanic magma tissue, basalt rock tissue, and granite crystal tissue",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define biological tissue:\n"
        f"- A tissue consists of similar cells performing a common function.\n"
        f"- For {target_k}: {examples}.\n\n"
        f"**Step 2:** The correct tissue group is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_35_{rng.randint(100000, 999999)}",
        "subskill": "35_tissues_definition_and_examples_in_plants_and_animals",
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
            "tier_1": f"Are xylem and phloem in plants or animals?",
            "tier_2": f"Match the major tissue types with {target_k}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["plant_vs_animal_tissues_distinction_misconception"],
    }


# 36. Organs definition and tissue integration examples
def arch_36_organs_definition_and_tissue_integration_examples(rng: random.Random) -> Dict[str, Any]:
    organs = [
        ("The human stomach", "integrates epithelial tissue (secretes acid and enzymes), smooth muscle tissue (churns food), and nervous tissue (coordinates peristalsis)"),
        ("A plant leaf", "integrates upper/lower epidermal tissue, palisade and spongy mesophyll tissue, and vascular bundle tissue (xylem and phloem)"),
        ("The human heart", "integrates cardiac muscle tissue, connective tissue valves, epithelial endocardium, and conductive nervous tissue"),
    ]
    org_name, integration = rng.choice(organs)
    prompt = (
        f"Why is **{org_name}** classified as an **organ** rather than simply a tissue?"
    )
    correct = (
        f"Because it is composed of several distinct, coordinated tissues that work together to perform complex physiological tasks: it {integration}."
    )
    options = [
        correct,
        "Because it consists of only one single giant cell measuring two metres in length.",
        "Because it is a non-living mineral formed purely by limestone sedimentation.",
        "Because it floats outside the body with no connection to any blood vessels.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish an organ from a tissue:\n"
        f"- A tissue = one group of similar cells.\n"
        f"- An organ = multiple different tissues integrated structurally.\n"
        f"- For {org_name}: {integration}.\n\n"
        f"**Step 2:** The accurate scientific reason is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_36_{rng.randint(100000, 999999)}",
        "subskill": "36_organs_definition_and_tissue_integration_examples",
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
            "tier_1": "What is the difference between a tissue and an organ?",
            "tier_2": "An organ is built from several different tissues working together.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["organ_vs_tissue_integration_misconception"],
    }


# 37. Organ systems collective organ cooperation overview
def arch_37_organ_systems_collective_organ_cooperation_overview(rng: random.Random) -> Dict[str, Any]:
    systems = [
        ("Digestive system", "mouth, esophagus, stomach, small intestine, large intestine, liver, and pancreas", "ingest, digest, and absorb nutrients into the bloodstream"),
        ("Respiratory system", "trachea, bronchi, bronchioles, lungs, and diaphragm", "exchange oxygen and carbon dioxide between atmospheric air and blood"),
        ("Circulatory system", "heart, arteries, veins, and capillaries", "transport oxygen, glucose, hormones, and metabolic wastes throughout the body"),
    ]
    sys_name, organs_list, sys_purpose = rng.choice(systems)
    prompt = (
        f"In human physiology, organs do not operate in isolation; they form integrated **organ systems**.\n\n"
        f"Which group of organs cooperates to form the **{sys_name}**, and what is its primary physiological purpose?"
    )
    correct = f"Organs: {organs_list}.\nPurpose: To {sys_purpose}."
    alt = [s for s in systems if s[0] != sys_name]
    distractors = [f"Organs: {s[1]}.\nPurpose: To {s[2]}." for s in alt]
    distractors.append("Organs: Teeth and fingernails.\nPurpose: To fly through the clouds.")
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review organ systems in the human body:\n"
        f"- An organ system is a group of organs cooperating to carry out a major life function.\n"
        f"- For {sys_name}: {organs_list} -> {sys_purpose}.\n\n"
        f"**Step 2:** The correct statement is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_37_{rng.randint(100000, 999999)}",
        "subskill": "37_organ_systems_collective_organ_cooperation_overview",
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
            "tier_1": f"Which organs belong to the {sys_name}?",
            "tier_2": f"Match the {sys_name} to its composite organs and core physiological function.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["organ_system_composite_organs_misconception"],
    }


# 38. Specialized cells differentiation and division of labour
def arch_38_specialized_cells_differentiation_and_division_of_labour(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"During embryonic development, unspecialized stem cells undergo **cellular differentiation**.\n\n"
        f"What is the biological advantage of **cellular specialization** and division of labour in multicellular organisms?"
    )
    correct = (
        "Each specialized cell type develops specific structural adaptations suited to carry out one particular function efficiently, "
        "enabling the organism to perform diverse, complex physiological activities that a single unspecialized cell could not accomplish."
    )
    options = [
        correct,
        "Specialization causes every cell to turn into solid wood, allowing humans to live without oxygen.",
        "Specialization forces all cells to stop using DNA, preventing cell division permanently.",
        "It ensures that all cells in the body look completely identical and carry out the exact same task.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand cellular differentiation and specialization:\n"
        f"- In multicellular organisms, different cells express different genes to specialize.\n"
        f"- Division of labour: specialization increases metabolic efficiency and enables complex physiological systems.\n\n"
        f"**Step 2:** The primary advantage is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_38_{rng.randint(100000, 999999)}",
        "subskill": "38_specialized_cells_differentiation_and_division_of_labour",
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
            "tier_1": "Why do humans have nerve cells, red blood cells, and muscle cells instead of only one cell type?",
            "tier_2": "Specialization allows division of labour, optimizing cells for distinct survival functions.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cellular_differentiation_division_of_labour_misconception"],
    }


# 39. Root hair cells elongated surface area water absorption
def arch_39_root_hair_cells_elongated_surface_area_water_absorption(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Root hair cells are specialized epidermal cells found at the root tips of terrestrial plants.\n\n"
        f"Which structural adaptations enable root hair cells to absorb water and dissolved mineral salts with maximum efficiency?"
    )
    correct = (
        "A long, thin finger-like extension that greatly amplifies the surface-area-to-volume ratio, "
        "a thin cellulose cell wall for short diffusion distance, and a concentrated vacuolar cell sap to maintain osmotic water uptake."
    )
    options = [
        correct,
        "A thick waterproof waxy cuticle layer and hundreds of bright green chloroplasts.",
        "A pair of flapping bird wings that pump oxygen directly into the soil.",
        "A hard metallic shell with zero water permeability to keep the root completely dry.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze root hair cell adaptations:\n"
        f"- Elongated hair: increases surface area for osmosis and active transport.\n"
        f"- Thin cell wall: reduces diffusion path.\n"
        f"- No chloroplasts: roots are underground in darkness.\n"
        f"- Concentrated sap in vacuole: lowers water potential, driving osmosis into the root.\n\n"
        f"**Step 2:** The structural adaptations are: **{correct}**."
    )
    return {
        "id": f"ns9_cell_39_{rng.randint(100000, 999999)}",
        "subskill": "39_root_hair_cells_elongated_surface_area_water_absorption",
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
            "tier_1": "Do root hair cells have chloroplasts, and how does the long extension help?",
            "tier_2": "The long extension maximizes surface area for osmosis; they lack chloroplasts because they are underground.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["root_hair_chloroplast_surface_area_misconception"],
    }


# 40. Palisade mesophyll cells chloroplast density photosynthesis
def arch_40_palisade_mesophyll_cells_chloroplast_density_photosynthesis(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a dicotyledonous leaf cross-section, **palisade mesophyll cells** form a distinct layer directly beneath the upper epidermis.\n\n"
        f"How are palisade mesophyll cells structurally specialized for their primary physiological function?"
    )
    correct = (
        "They are vertically elongated, columnar cells packed closely together with abundant chloroplasts positioned "
        "near the cell periphery to maximize the absorption of incident radiant sunlight for photosynthesis."
    )
    options = [
        correct,
        "They are completely round cells with thick wooden shells that reflect 100% of all sunlight away.",
        "They are hollow dead cells with no cytoplasm that pump blood through the flower petals.",
        "They are mobile amoeba-like cells that crawl out of the leaf at night to hunt insects.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze palisade mesophyll adaptations:\n"
        f"- Location: upper part of leaf where sunlight intensity is highest.\n"
        f"- Shape: columnar and closely packed to absorb maximum photons.\n"
        f"- Abundant chloroplasts: maximize rate of photosynthesis.\n\n"
        f"**Step 2:** The accurate adaptation is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_40_{rng.randint(100000, 999999)}",
        "subskill": "40_palisade_mesophyll_cells_chloroplast_density_photosynthesis",
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
            "tier_1": "Where in the leaf are palisade cells located, and why do they have so many chloroplasts?",
            "tier_2": "Palisade cells are columnar and rich in chloroplasts to capture maximum sunlight for photosynthesis.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["palisade_mesophyll_adaptations_misconception"],
    }


# 41. Guard cells stomata regulation transpiration and gas exchange
def arch_41_guard_cells_stomata_regulation_transpiration_and_gas_exchange(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Specialized bean-shaped **guard cells** occur in pairs within the leaf epidermis, flanking microscopic pores called stomata.\n\n"
        f"What unique structural feature allows guard cells to bend and open the stoma when they become turgid?"
    )
    correct = (
        "The inner cellulose cell wall facing the stomatal pore is much thicker and less elastic than the outer wall; "
        "when guard cells absorb water and swell, the flexible outer walls expand outward, pulling the inner thick walls apart and opening the pore."
    )
    options = [
        correct,
        "Guard cells have magnetic hinges that flip open when exposed to moonlight.",
        "Guard cells completely dissolve into gas every morning and reform at night.",
        "Guard cells use muscle tendons that physically pull the pore open like a door.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the stomatal opening mechanism:\n"
        f"- Guard cell walls have uneven thickness (thick inner wall, thin outer wall).\n"
        f"- When potassium ions and water enter, turgor pressure rises.\n"
        f"- The thin outer wall stretches more than the thick inner wall, causing the cell to curve into a bean shape and opening the stomatal aperture for $CO_2$ uptake.\n\n"
        f"**Step 2:** The accurate structural adaptation is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_41_{rng.randint(100000, 999999)}",
        "subskill": "41_guard_cells_stomata_regulation_transpiration_and_gas_exchange",
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
            "tier_1": "Are the inner and outer cell walls of a guard cell equally thick?",
            "tier_2": "The inner wall is thicker and less elastic; when turgid, the thin outer wall bows out, pulling the pore open.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["guard_cells_asymmetric_wall_turgor_misconception"],
    }


# 42. Red blood cells biconcave anucleate hemoglobin adaptation
def arch_42_red_blood_cells_biconcave_anucleate_hemoglobin_adaptation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Mature human red blood cells (erythrocytes) possess remarkable specializations for respiratory gas transport.\n\n"
        f"Which combination of structural adaptations enables red blood cells to transport oxygen with extraordinary efficiency?"
    )
    correct = (
        "A biconcave disc shape (maximizing surface-area-to-volume ratio for gas diffusion), "
        "loss of the nucleus and mitochondria upon maturity (creating maximum interior volume for hemoglobin), "
        "and a flexible membrane to squeeze single-file through narrow capillaries."
    )
    options = [
        correct,
        "A spherical spiky shape, multiple nuclei, and abundant green chlorophyll pigments.",
        "A square cube shape made of chitin with rigid wooden edges to resist blood pressure.",
        "A long tail with three flagella that propel the cell through the nervous system.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review erythrocyte adaptations:\n"
        f"- Biconcave shape: increases surface area for rapid $O_2$ diffusion and decreases diffusion distance to the centre.\n"
        f"- Anucleate (no nucleus): maximizes cytoplasmic space for ~270 million hemoglobin molecules.\n"
        f"- Flexibility: allows deformation through narrow 5-7 um capillaries.\n\n"
        f"**Step 2:** The correct combination is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_42_{rng.randint(100000, 999999)}",
        "subskill": "42_red_blood_cells_biconcave_anucleate_hemoglobin_adaptation",
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
            "tier_1": "Do mature human red blood cells have a nucleus?",
            "tier_2": "They have a biconcave disc shape, no nucleus (more hemoglobin room), and flexible membranes.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["red_blood_cell_anucleate_biconcave_misconception"],
    }


# 43. Nerve cells neurons axon dendrites and electrical impulses
def arch_43_nerve_cells_neurons_axon_dendrites_and_electrical_impulses(rng: random.Random) -> Dict[str, Any]:
    parts = [
        ("Dendrites", "highly branched cytoplasmic extensions that receive chemical synaptic signals from other neurons and conduct impulses toward the cell body"),
        ("Axon", "an elongated nerve fibre that conducts electrical action potentials away from the cell body over long distances to target cells"),
        ("Myelin sheath", "an insulating fatty lipid layer produced by Schwann cells that speeds up electrical impulse transmission via saltatory conduction"),
    ]
    target_p, target_fn = rng.choice(parts)
    prompt = (
        f"Nerve cells (neurons) are specialized for rapid long-distance communication in the nervous system.\n\n"
        f"What is the specific anatomical adaptation and function of the **{target_p}** of a neuron?"
    )
    correct = f"It consists of {target_fn}."
    alt = [p[1] for p in parts if p[0] != target_p]
    distractors = [f"It consists of {fn}." for fn in alt]
    distractors.append("It consists of wooden teeth that chew solid food inside the brain.")
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review neuron anatomy:\n"
        f"- Dendrites: receive signals -> conduct toward soma.\n"
        f"- Axon: carries impulses away from soma over distances up to 1 metre.\n"
        f"- Myelin sheath: lipid insulation speeding up conduction.\n\n"
        f"**Step 2:** For {target_p}: **{correct}**."
    )
    return {
        "id": f"ns9_cell_43_{rng.randint(100000, 999999)}",
        "subskill": "43_nerve_cells_neurons_axon_dendrites_and_electrical_impulses",
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
            "tier_1": f"Does {target_p} receive signals, transmit them away, or insulate the fibre?",
            "tier_2": f"Match {target_p} to its specific role in electrical impulse conduction.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["neuron_structural_adaptations_misconception"],
    }


# 44. Muscle cells fibres contractile proteins and movement
def arch_44_muscle_cells_fibres_contractile_proteins_and_movement(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Skeletal muscle cells (muscle fibres) are specialized to produce mechanical force and movement.\n\n"
        f"Which specialized cellular adaptations allow skeletal muscle cells to contract repeatedly?"
    )
    correct = (
        "Elongated cylindrical fibres containing organized parallel myofibrils of actin and myosin contractile proteins, "
        "abundant mitochondria to supply high ATP levels, and multiple nuclei to coordinate protein synthesis."
    )
    options = [
        correct,
        "Rigid cellulose boxes containing solid granite stones that prevent all motion.",
        "Acellular oil droplets that evaporate into steam when exposed to cold air.",
        "Round hollow bags filled with pure hydrochloric acid to digest surrounding bones.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze muscle cell adaptations:\n"
        f"- Contractile proteins (actin and myosin) slide past each other during contraction.\n"
        f"- High mitochondrial count: provides ATP energy required for contraction and relaxation cycles.\n"
        f"- Elongated multinucleated fibres: allow coordinated contraction along the entire muscle length.\n\n"
        f"**Step 2:** The structural adaptations are: **{correct}**."
    )
    return {
        "id": f"ns9_cell_44_{rng.randint(100000, 999999)}",
        "subskill": "44_muscle_cells_fibres_contractile_proteins_and_movement",
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
            "tier_1": "What proteins slide past each other in muscle cells, and why do they have many mitochondria?",
            "tier_2": "Actin and myosin myofibrils contract using ATP generated by abundant mitochondria.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["muscle_fibre_contractile_proteins_misconception"],
    }


# 45. Ciliated epithelial cells mucus trapping and sweeping action
def arch_45_ciliated_epithelial_cells_mucus_trapping_and_sweeping_action(rng: random.Random) -> Dict[str, Any]:
    locations = [
        ("the human respiratory tract (trachea and bronchi)", "trap inhaled dust, bacteria, and allergens in sticky mucus, and beat cilia rhythmically upwards to the pharynx to be coughed or swallowed"),
        ("the female fallopian tubes (oviducts)", "beat microscopic cilia rhythmically to gently propel the ovum (egg cell) or early embryo from the ovary toward the uterus"),
    ]
    loc_name, action = rng.choice(locations)
    prompt = (
        f"Ciliated epithelial cells line internal tubes in the human body, such as **{loc_name}**.\n\n"
        f"What is the cooperative physiological mechanism of ciliated epithelial cells in this location?"
    )
    correct = f"They {action}."
    alt = [l[1] for l in locations if l[0] != loc_name][0]
    options = [
        correct,
        f"They {alt}.",
        "They synthesize bone calcium to turn the tube into a solid limestone rod.",
        "They shoot digestive hydrochloric acid into the air to burn flying insects.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze ciliated epithelium function:\n"
        f"- Cilia are microscopic hair-like projections beating in coordinated waves.\n"
        f"- In {loc_name}: {action}.\n\n"
        f"**Step 2:** The correct physiological mechanism is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_45_{rng.randint(100000, 999999)}",
        "subskill": "45_ciliated_epithelial_cells_mucus_trapping_and_sweeping_action",
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
            "tier_1": f"What do cilia do in {loc_name}?",
            "tier_2": "Cilia beat in coordinated waves to sweep mucus and trapped particles or transport ova.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ciliated_epithelial_cilia_sweeping_misconception"],
    }


# 46. Sperm cells flagellum acrosome and mitochondria adaptations
def arch_46_sperm_cells_flagellum_acrosome_and_mitochondria_adaptations(rng: random.Random) -> Dict[str, Any]:
    parts = [
        ("Acrosome at the tip of the head", "contains hydrolytic digestive enzymes that break down the protective jelly coat (zona pellucida) of the egg cell to allow fertilization"),
        ("Midpiece (middle section)", "packed with spiral mitochondria that generate abundant ATP energy to fuel flagellar movement"),
        ("Flagellum (long tail)", "whip-like protein structure that lashes from side to side to propel the sperm through female reproductive fluids"),
    ]
    target_p, target_role = rng.choice(parts)
    prompt = (
        f"Human sperm cells (male spermatozoa) are highly specialized mobile gametes adapted for fertilization.\n\n"
        f"What is the specific structural adaptation and biological role of the **{target_p}**?"
    )
    correct = f"It {target_role}."
    alt = [p[1] for p in parts if p[0] != target_p]
    distractors = [f"It {r}." for r in alt]
    distractors.append("It photosynthesizes green chlorophyll using sunlight inside the testes.")
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze sperm cell adaptations:\n"
        f"- Head with haploid nucleus + acrosome (enzymes to penetrate egg).\n"
        f"- Midpiece: mitochondria producing ATP.\n"
        f"- Tail (flagellum): motility.\n"
        f"- For {target_p}: {target_role}.\n\n"
        f"**Step 2:** The correct statement is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_46_{rng.randint(100000, 999999)}",
        "subskill": "46_sperm_cells_flagellum_acrosome_and_mitochondria_adaptations",
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
            "tier_1": f"What is the function of the {target_p}?",
            "tier_2": "The acrosome has enzymes, the midpiece has mitochondria, and the flagellum propels the sperm.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["sperm_cell_organelle_adaptations_misconception"],
    }


# 47. Egg cells ovum nutrient yolk and protective coat adaptations
def arch_47_egg_cells_ovum_nutrient_yolk_and_protective_coat_adaptations(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Human egg cells (ova) are among the largest cells in the human body, visible as tiny specks to the unaided eye.\n\n"
        f"Which combination of structural adaptations characterizes the mature human ovum?"
    )
    correct = (
        "A large cytoplasm packed with nutrient yolk (providing energy and substrates for early embryonic cleavage), "
        "a haploid nucleus with maternal chromosomes, and a protective outer jelly coat (zona pellucida) that hardens "
        "immediately after the entry of a single sperm to prevent polyspermy."
    )
    options = [
        correct,
        "A long tail that allows the egg cell to run across dry soil like a spider.",
        "A thick cellulose cell wall with chlorophyll that photosynthesizes inside the uterus.",
        "An iron shell that explodes when contacted by a red blood cell.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze ovum adaptations:\n"
        f"- Large size: extensive cytoplasm containing nutrient reserves for the early blastocyst before implantation.\n"
        f"- Haploid nucleus ($n = 23$ chromosomes).\n"
        f"- Zona pellucida: cortical reaction after single sperm entry hardens the coat, preventing polyspermy.\n\n"
        f"**Step 2:** The accurate combination of adaptations is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_47_{rng.randint(100000, 999999)}",
        "subskill": "47_egg_cells_ovum_nutrient_yolk_and_protective_coat_adaptations",
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
            "tier_1": "Why is the egg cell so much larger than a sperm cell?",
            "tier_2": "The ovum contains a large nutrient-rich cytoplasm for the embryo and a jelly coat preventing polyspermy.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ovum_structural_adaptations_misconception"],
    }


# 48. White blood cells phagocytic and antibody immune defence
def arch_48_white_blood_cells_phagocytic_and_antibody_immune_defence(rng: random.Random) -> Dict[str, Any]:
    leukocytes = [
        (
            "Phagocytes (such as neutrophils and macrophages)",
            "can alter their cellular shape and produce pseudopodia to engulf and ingest foreign bacteria into phagocytic vacuoles, fusing with lysosomes containing hydrolytic enzymes to destroy the pathogen",
        ),
        (
            "B-lymphocytes",
            "possess membrane-bound antigen receptors that bind specifically to complementary antigens on invading pathogens, triggering rapid clonal division into plasma cells that secrete vast amounts of antibodies",
        ),
    ]
    target_l, action = rng.choice(leukocytes)
    prompt = (
        f"White blood cells (leukocytes) defend the body against infectious disease.\n\n"
        f"Which specialized cellular adaptation and immune function distinguishes **{target_l}**?"
    )
    correct = f"They {action}."
    other_l = [l[1] for l in leukocytes if l[0] != target_l][0]
    options = [
        correct,
        f"They {other_l}.",
        "They carry oxygen gas bound to iron hemoglobin across the pulmonary vein.",
        "They form hard enamel shells on teeth to prevent dental cavities.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare phagocytes and lymphocytes:\n"
        f"- Phagocytes: lobed nucleus, flexible membrane, engulf pathogens (phagocytosis).\n"
        f"- Lymphocytes: large spherical nucleus, synthesize antibodies against complementary antigens.\n\n"
        f"**Step 2:** For {target_l}: **{correct}**."
    )
    return {
        "id": f"ns9_cell_48_{rng.randint(100000, 999999)}",
        "subskill": "48_white_blood_cells_phagocytic_and_antibody_immune_defence",
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
            "tier_1": f"Do {target_l.split()[0]} engulf pathogens or synthesize antibodies?",
            "tier_2": "Phagocytes engulf and digest pathogens; lymphocytes produce specific antibodies.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["white_blood_cell_types_adaptations_misconception"],
    }


# 49. Evaluating fair test microscope field of view measurement
def arch_49_evaluating_fair_test_microscope_field_of_view_measurement(rng: random.Random) -> Dict[str, Any]:
    fov_low_mm = rng.choice([4.0, 4.5, 5.0])
    mag_low = 40
    mag_high = rng.choice([100, 200, 400])
    fov_high_mm = (fov_low_mm * mag_low) / mag_high
    prompt = (
        f"A learner measures the **diameter of the field of view (FOV)** of a compound microscope using a transparent plastic ruler.\n"
        f"- At low power (**{mag_low}x** total magnification), the FOV diameter is **{fov_low_mm:.1f} mm** ({fov_low_mm * 1000:.0f} um).\n\n"
        f"Using the inverse proportionality relationship between magnification and field of view:\n"
        f"$$\\text{{FOV}}_{{\\text{{high}}}} = \\frac{{\\text{{FOV}}_{{\\text{{low}}}} \\times \\text{{Mag}}_{{\\text{{low}}}}}}{{\\text{{Mag}}_{{\\text{{high}}}}}}$$\n\n"
        f"What will be the FOV diameter when switching to high power (**{mag_high}x** total magnification)?"
    )
    correct = f"{fov_high_mm:.2f} mm ({fov_high_mm * 1000:.0f} um)"
    wrong_1 = f"{fov_low_mm * (mag_high / mag_low):.2f} mm"
    wrong_2 = f"{fov_low_mm * 10:.1f} mm"
    wrong_3 = f"{fov_low_mm / 2:.2f} mm"
    options = [correct, wrong_1, wrong_2, wrong_3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** State the inverse proportion formula:\n"
        f"$$\\text{{FOV}}_{{\\text{{high}}}} = \\frac{{{fov_low_mm:.1f}\\text{{ mm}} \\times {mag_low}}}{{{mag_high}}} = {fov_high_mm:.2f}\\text{{ mm}}$$\n\n"
        f"**Step 2:** Convert to micrometres:\n"
        f"$${fov_high_mm:.2f}\\text{{ mm}} \\times 1\\,000 = {fov_high_mm * 1000:.0f}\\text{{ um}}$$\n\n"
        f"**Step 3:** The high-power field of view diameter is **{correct}**."
    )
    return {
        "id": f"ns9_cell_49_{rng.randint(100000, 999999)}",
        "subskill": "49_evaluating_fair_test_microscope_field_of_view_measurement",
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
            "tier_1": "As magnification increases, does the field of view get larger or smaller?",
            "tier_2": "Field of view is inversely proportional to magnification: multiply by low mag and divide by high mag.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["microscope_field_of_view_inverse_proportion_misconception"],
    }


# 50. Synthetic case study cellular pathology and organelle malfunction
def arch_50_synthetic_case_study_cellular_pathology_and_organelle_malfunction(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (
            "Mitochondrial myopathy",
            "A patient presents with chronic muscle fatigue, inability to sustain physical exercise, and lactic acid buildup in the blood.",
            "Mitochondria (cellular respiration failure causing deficient ATP production)",
        ),
        (
            "Tay-Sachs disease (lysosomal storage disorder)",
            "An infant exhibits progressive neurological deterioration due to toxic lipid accumulation inside brain cells.",
            "Lysosomes (deficiency of hydrolytic enzymes unable to break down ganglioside lipids)",
        ),
        (
            "Ciliary dyskinesia (Kartagener's syndrome)",
            "A child suffers from chronic recurrent lung infections, sinusitis, and bronchiectasis from birth.",
            "Cilia on epithelial cells (immotile cilia failing to clear pathogen-trapping mucus from the respiratory tract)",
        ),
    ]
    disease, symptoms, organelle_cause = rng.choice(cases)
    prompt = (
        f"A medical team investigates a patient diagnosed with **{disease}**.\n\n"
        f"Clinical presentation: *\"{symptoms}\"*\n\n"
        f"Which cellular organelle or structure is pathologically malfunctioning, and why?"
    )
    correct = organelle_cause
    alt = [c[2] for c in cases if c[0] != disease]
    distractors = alt + [
        "Chloroplasts (lack of green photosynthesis in human skeletal muscles)"
    ]
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze clinical symptoms:\n"
        f"- Patient presentation: {symptoms}.\n"
        f"- Direct cellular cause: {organelle_cause}.\n\n"
        f"**Step 2:** The pathologically malfunctioning organelle is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_50_{rng.randint(100000, 999999)}",
        "subskill": "50_synthetic_case_study_cellular_pathology_and_organelle_malfunction",
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
            "tier_1": f"Think about which organelle provides ATP, digests waste, or moves mucus in {disease.split()[0]}.",
            "tier_2": f"Match the symptom profile to the specific organelle failure: {organelle_cause.split()[0]}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cellular_pathology_organelle_malfunction_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "26_nucleus_chromatin_dna_and_hereditary_control_centre": arch_26_nucleus_chromatin_dna_and_hereditary_control_centre,
    "27_cytoplasm_cytosol_medium_for_metabolic_biochemical_reactions": arch_27_cytoplasm_cytosol_medium_for_metabolic_biochemical_reactions,
    "28_mitochondria_cellular_respiration_atp_energy_powerhouse": arch_28_mitochondria_cellular_respiration_atp_energy_powerhouse,
    "29_chloroplasts_chlorophyll_and_photosynthetic_sugar_synthesis": arch_29_chloroplasts_chlorophyll_and_photosynthetic_sugar_synthesis,
    "30_large_central_sap_vacuole_tonoplast_and_osmotic_turgidity": arch_30_large_central_sap_vacuole_tonoplast_and_osmotic_turgidity,
    "31_ribosomes_site_of_protein_synthesis": arch_31_ribosomes_site_of_protein_synthesis,
    "32_endoplasmic_reticulum_rough_vs_smooth_transport_channels": arch_32_endoplasmic_reticulum_rough_vs_smooth_transport_channels,
    "33_golgi_body_packaging_sorting_and_secretory_vesicles": arch_33_golgi_body_packaging_sorting_and_secretory_vesicles,
    "34_biological_hierarchy_organelles_cells_tissues_organs_systems": arch_34_biological_hierarchy_organelles_cells_tissues_organs_systems,
    "35_tissues_definition_and_examples_in_plants_and_animals": arch_35_tissues_definition_and_examples_in_plants_and_animals,
    "36_organs_definition_and_tissue_integration_examples": arch_36_organs_definition_and_tissue_integration_examples,
    "37_organ_systems_collective_organ_cooperation_overview": arch_37_organ_systems_collective_organ_cooperation_overview,
    "38_specialized_cells_differentiation_and_division_of_labour": arch_38_specialized_cells_differentiation_and_division_of_labour,
    "39_root_hair_cells_elongated_surface_area_water_absorption": arch_39_root_hair_cells_elongated_surface_area_water_absorption,
    "40_palisade_mesophyll_cells_chloroplast_density_photosynthesis": arch_40_palisade_mesophyll_cells_chloroplast_density_photosynthesis,
    "41_guard_cells_stomata_regulation_transpiration_and_gas_exchange": arch_41_guard_cells_stomata_regulation_transpiration_and_gas_exchange,
    "42_red_blood_cells_biconcave_anucleate_hemoglobin_adaptation": arch_42_red_blood_cells_biconcave_anucleate_hemoglobin_adaptation,
    "43_nerve_cells_neurons_axon_dendrites_and_electrical_impulses": arch_43_nerve_cells_neurons_axon_dendrites_and_electrical_impulses,
    "44_muscle_cells_fibres_contractile_proteins_and_movement": arch_44_muscle_cells_fibres_contractile_proteins_and_movement,
    "45_ciliated_epithelial_cells_mucus_trapping_and_sweeping_action": arch_45_ciliated_epithelial_cells_mucus_trapping_and_sweeping_action,
    "46_sperm_cells_flagellum_acrosome_and_mitochondria_adaptations": arch_46_sperm_cells_flagellum_acrosome_and_mitochondria_adaptations,
    "47_egg_cells_ovum_nutrient_yolk_and_protective_coat_adaptations": arch_47_egg_cells_ovum_nutrient_yolk_and_protective_coat_adaptations,
    "48_white_blood_cells_phagocytic_and_antibody_immune_defence": arch_48_white_blood_cells_phagocytic_and_antibody_immune_defence,
    "49_evaluating_fair_test_microscope_field_of_view_measurement": arch_49_evaluating_fair_test_microscope_field_of_view_measurement,
    "50_synthetic_case_study_cellular_pathology_and_organelle_malfunction": arch_50_synthetic_case_study_cellular_pathology_and_organelle_malfunction,
}
