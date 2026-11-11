"""Grade 8 Natural Sciences: Term 2 - Microorganisms (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/03. Microorganisms.md.
Focus: Biodiversity of microorganisms, 5 kingdoms, prokaryotes vs eukaryotes, viruses, bacteria, protists, fungi, and pathogenic mechanisms.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 01. Microorganisms definition and microscopic scale
def arch_01_microorganisms_definition_and_microscopic_scale(rng: random.Random) -> Dict[str, Any]:
    microbe_sizes = [
        ("viruses", "20 to 300 nanometres (nm)", "electron microscope"),
        ("bacteria", "0.5 to 5 micrometres (um)", "compound light microscope"),
        ("unicellular protists and yeasts", "10 to 100 micrometres (um)", "compound light microscope"),
    ]
    microbe_type, size_range, instrument = rng.choice(microbe_sizes)
    prompt = (
        f"Microscopic organisms such as {microbe_type} range in size from approximately {size_range}. "
        f"They cannot be resolved by the unaided human eye and require a {instrument} to observe.\n\n"
        f"What is the formal scientific definition of a **microorganism**?"
    )
    correct = (
        "An organism that is microscopic (too small to be seen with the naked human eye), "
        "existing as a single cell, acellular entity, or simple colony."
    )
    options = [
        correct,
        "A non-living metallic grain created inside computer microchips.",
        "An adult animal with four legs that lives exclusively underground.",
        "A fossilized mineral rock formed during volcanic eruptions.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define microorganisms:\n"
        f"- Microorganisms (microbes) are minute organisms invisible to the naked eye (requiring magnification by light or electron microscopy).\n"
        f"- They include bacteria, viruses, microscopic fungi (yeasts and moulds), and protists.\n\n"
        f"**Step 2:** The scientific definition is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_01_{rng.randint(100000, 999999)}",
        "subskill": "01_microorganisms_definition_and_microscopic_scale",
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
            "tier_1": "What does the prefix 'micro-' mean? Tiny / microscopic.",
            "tier_2": "Microorganisms are living (or acellular) entities too small to be seen with the naked eye.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["microorganism_scale_definition_misconception"],
    }


# 02. Five kingdom classification system overview
def arch_02_five_kingdom_classification_system_overview(rng: random.Random) -> Dict[str, Any]:
    kingdoms = [
        ("Kingdom Monera", "Prokaryotic, unicellular microorganisms lacking a true membrane-bound nucleus (e.g. bacteria and cyanobacteria)"),
        ("Kingdom Protista", "Eukaryotic, predominantly unicellular organisms that do not fit into animals, plants, or fungi (e.g. Amoeba, algae)"),
        ("Kingdom Fungi", "Eukaryotic, heterotrophic organisms with chitin cell walls that feed by saprophytic absorption (e.g. yeasts, moulds)"),
        ("Kingdom Plantae", "Eukaryotic, multicellular autotrophic organisms with cellulose cell walls that carry out photosynthesis"),
        ("Kingdom Animalia", "Eukaryotic, multicellular heterotrophs that ingest food and typically possess nervous systems and locomotion"),
    ]
    target_k, target_desc = rng.choice(kingdoms)
    prompt = (
        f"In biological taxonomy, living organisms are grouped into five major **Kingdoms**.\n\n"
        f"Which defining characteristics scientifically describe **{target_k}**?"
    )
    correct = target_desc
    alt_desc = [k[1] for k in kingdoms if k[0] != target_k]
    options = [correct] + rng.sample(alt_desc, 3)
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review the 5 kingdoms of life:\n"
        f"- Monera: prokaryotes (bacteria).\n"
        f"- Protista: simple eukaryotes (protozoa and algae).\n"
        f"- Fungi: chitin-walled saprophytic heterotrophs.\n"
        f"- Plantae: multicellular photosynthetic autotrophs.\n"
        f"- Animalia: multicellular ingestive heterotrophs.\n\n"
        f"**Step 2:** For {target_k}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_02_{rng.randint(100000, 999999)}",
        "subskill": "02_five_kingdom_classification_system_overview",
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
            "tier_1": f"Think about whether members of {target_k} have a nucleus, make their own food, or are single-celled.",
            "tier_2": f"{target_k}: {target_desc}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["five_kingdoms_classification_misconception"],
    }


# 03. Prokaryote vs eukaryote cellular distinction
def arch_03_prokaryote_vs_eukaryote_cellular_distinction(rng: random.Random) -> Dict[str, Any]:
    cells = [
        ("a bacterium cell (*Escherichia coli*)", "Prokaryotic", "its circular DNA is loose in the cytoplasm (nucleoid) without any nuclear membrane"),
        ("a human white blood cell (lymphocyte)", "Eukaryotic", "its DNA is enclosed within a true membrane-bound nucleus and possesses membrane-bound organelles"),
        ("a brewer's yeast cell (*Saccharomyces cerevisiae*)", "Eukaryotic", "it possesses a distinct membrane-bound nucleus and mitochondria"),
    ]
    organism, classification, reason = rng.choice(cells)
    prompt = (
        f"Consider {organism}.\n\n"
        f"How is this cell fundamentally classified in biology, and what is the primary structural basis for this classification?"
    )
    correct = f"{classification}, because {reason}."
    alt_class = "Eukaryotic" if classification == "Prokaryotic" else "Prokaryotic"
    options = [
        correct,
        f"{alt_class}, because it contains zero chemical molecules or atoms.",
        "Acellular, because it is an inanimate mineral rock crystal.",
        f"{classification}, because it lives exclusively inside automobile gasoline engines.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish prokaryotic from eukaryotic cells:\n"
        f"- Prokaryotes ('before nucleus'): lack a membrane-bound nucleus; DNA floats in nucleoid region; lack membrane-bound organelles (bacteria).\n"
        f"- Eukaryotes ('true nucleus'): DNA is housed within a double-membrane nucleus; possess mitochondria, ER, Golgi (protists, fungi, plants, animals).\n\n"
        f"**Step 2:** For {organism}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_03_{rng.randint(100000, 999999)}",
        "subskill": "03_prokaryote_vs_eukaryote_cellular_distinction",
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
            "tier_1": "Does this cell have a membrane-bound nucleus?",
            "tier_2": "Prokaryotes lack a membrane-bound nucleus; eukaryotes have a true nucleus.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["prokaryote_vs_eukaryote_distinction_misconception"],
    }


# 04. Viruses acellular nature living vs nonliving boundary
def arch_04_viruses_acellular_nature_living_vs_nonliving_boundary(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Viruses do not belong to any of the five biological kingdoms. Biologists often describe them as "
        f"straddling the boundary between the living and non-living worlds.\n\n"
        f"What biological evidence supports classifying viruses as **non-living** when outside a host cell?"
    )
    correct = (
        "They are acellular (lack cytoplasm, cell membranes, and organelles), carry out zero independent metabolism "
        "(cannot feed, respire, or excrete), and can be crystallized like non-living chemicals."
    )
    options = [
        correct,
        "They are made of solid steel and walk around using mechanical gears.",
        "They photosynthesise continuously using green chlorophyll to make honey.",
        "They give birth to live mammal babies every morning.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the non-living characteristics of viruses:\n"
        f"- Acellular (not composed of cells; fails cell theory).\n"
        f"- Zero intrinsic metabolism: cannot perform cellular respiration, generate ATP, or synthesize proteins on their own.\n"
        f"- Inert when extracellular: behaves like a chemical nanoparticle until contacting a host.\n\n"
        f"**Step 2:** The justification is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_04_{rng.randint(100000, 999999)}",
        "subskill": "04_viruses_acellular_nature_living_vs_nonliving_boundary",
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
            "tier_1": "Do viruses have cells, cytoplasm, or cellular respiration?",
            "tier_2": "Viruses are acellular and have zero independent metabolism.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["virus_living_vs_nonliving_misconception"],
    }


# 05. Viral structure capsid protein and DNA or RNA core (with dynamic SVG)
def arch_05_viral_structure_capsid_protein_and_dna_or_rna_core(rng: random.Random) -> Dict[str, Any]:
    nucleic_acid = rng.choice(["DNA", "RNA"])
    capsid_color = rng.choice(["#3b82f6", "#8b5cf6", "#06b6d4"])

    svg = (
        f'<svg viewBox="0 0 380 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="190" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Typical Viral Architecture ({nucleic_acid} Core)</text>'
        f'<polygon points="190,45 250,80 250,140 190,175 130,140 130,80" fill="#f8fafc" stroke="{capsid_color}" stroke-width="3" />'
        f'<text x="190" y="65" font-size="10" fill="{capsid_color}" font-weight="bold" text-anchor="middle">Protein Capsid</text>'
        f'<path d="M 170 95 Q 190 85 210 95 T 190 125 T 180 145" fill="none" stroke="#ef4444" stroke-width="2.5" />'
        f'<text x="190" y="115" font-size="11" fill="#dc2626" font-weight="bold" text-anchor="middle">{nucleic_acid} Core</text>'
        f'<line x1="250" y1="110" x2="310" y2="110" stroke="#475569" stroke-width="1.5" />'
        f'<text x="315" y="113" font-size="10" fill="#0f172a">Protein coat</text>'
        f'<line x1="190" y1="125" x2="270" y2="160" stroke="#475569" stroke-width="1.5" />'
        f'<text x="275" y="163" font-size="10" fill="#0f172a">Genetic payload</text>'
        f'<text x="190" y="205" font-size="10" fill="#475569" text-anchor="middle">Contains either DNA or RNA, enclosed by a protective protein capsid</text>'
        f'</svg>'
    )

    prompt = (
        f"A viral particle (virion) has a remarkably simple structural composition compared to a living biological cell.\n\n"
        f"What are the two basic structural components found in every viral particle?"
    )
    correct = (
        "A central core of genetic nucleic acid (either DNA or RNA, but never both) "
        "enclosed inside an outer protective protein coat called a **capsid**."
    )
    options = [
        correct,
        "A nucleus surrounded by mitochondria and chloroplasts enclosed in a cellulose cell wall.",
        "A muscular heart surrounded by red blood cells and cartilage bones.",
        "A solid ball of molten sulfur covered in petroleum jelly.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recall viral anatomy:\n"
        f"- All viruses consist of:\n"
        f"  1. Nucleic acid genome: single- or double-stranded DNA or RNA (never both together).\n"
        f"  2. Capsid: a protective shell assembled from protein subunits (capsomeres).\n"
        f"- Some animal viruses also possess an outer lipid envelope stolen from host cell membranes.\n\n"
        f"**Step 2:** The fundamental components are: **{correct}**."
    )
    return {
        "id": f"ns8_mic_05_{rng.randint(100000, 999999)}",
        "subskill": "05_viral_structure_capsid_protein_and_dna_or_rna_core",
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
            "tier_1": "What is the genetic core and what is the protein shell called?",
            "tier_2": "A nucleic acid core (DNA or RNA) inside a protein coat (capsid).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["viral_structure_capsid_core_misconception"],
    }


# 06. Viruses as obligate intracellular parasites mechanism
def arch_06_viruses_as_obligate_intracellular_parasites_mechanism(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Viruses are scientifically defined as **obligate intracellular parasites**.\n\n"
        f"What does this designation mean regarding how viruses reproduce and multiply?"
    )
    correct = (
        "A virus cannot reproduce on its own; it must invade a living host cell and hijack the host cell's "
        "enzymes, ribosomes, and metabolic machinery to assemble new viral copies."
    )
    options = [
        correct,
        "A virus reproduces by laying microscopic eggs on dry wooden tables.",
        "A virus undergoes binary fission in sterile distilled water.",
        "A virus eats soil minerals to grow into a multicellular plant.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define obligate intracellular parasitism:\n"
        f"- 'Obligate' = strictly necessary / no alternative.\n"
        f"- 'Intracellular' = inside the cell.\n"
        f"- Viruses lack ribosomes and enzymes to replicate their own genes or translate proteins.\n"
        f"- They inject their nucleic acid into a living host, commandeering host cellular machinery to manufacture viral components until the host cell lyses (bursts) to release new virions.\n\n"
        f"**Step 2:** The mechanism is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_06_{rng.randint(100000, 999999)}",
        "subskill": "06_viruses_as_obligate_intracellular_parasites_mechanism",
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
            "tier_1": "Can a virus multiply on a clean glass table without a living cell?",
            "tier_2": "No, it must hijack the machinery inside a living host cell.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["obligate_parasite_virus_misconception"],
    }


# 07. Bacteriophages structure and bacterial infection
def arch_07_bacteriophages_structure_and_bacterial_infection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A specialized group of viruses called **bacteriophages** possesses an icosahedral head, "
        f"a hollow helical sheath, and tail fibers that resemble a lunar landing module.\n\n"
        f"What specific type of organism do bacteriophages target and infect?"
    )
    correct = "Bacterial cells exclusively (the word 'phage' means 'eater of bacteria')"
    options = [
        correct,
        "Human brain neurons exclusively",
        "Indigenous fynbos protea shrubs",
        "Marine sharks and dolphin calves",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify bacteriophages:\n"
        f"- Bacteriophages (phages) are viruses that specifically parasitize bacteria.\n"
        f"- Tail fibers bind to specific receptors on the bacterial cell wall, injecting viral DNA through the peptidoglycan layer.\n\n"
        f"**Step 2:** They target: **{correct}**."
    )
    return {
        "id": f"ns8_mic_07_{rng.randint(100000, 999999)}",
        "subskill": "07_bacteriophages_structure_and_bacterial_infection",
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
            "tier_1": "Look at the name: 'bacterio-' + '-phage'.",
            "tier_2": "Bacteriophages infect bacteria.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["bacteriophage_host_misconception"],
    }


# 08. Human viral diseases HIV influenza measles rabies
def arch_08_human_viral_diseases_hiv_influenza_measles_rabies(rng: random.Random) -> Dict[str, Any]:
    viral_diseases = [
        ("Human Immunodeficiency Virus (HIV)", "attacks and destroys CD4+ T-helper immune cells, leading to Acquired Immunodeficiency Syndrome (AIDS)"),
        ("Influenza virus", "infects the respiratory tract causing fever, chills, severe muscle aches, and sore throat"),
        ("Rabies virus", "transmitted via saliva through the bite of an infected mammal, attacking the central nervous system with fatal encephalitis"),
        ("Measles virus", "highly contagious airborne virus causing high fever, cough, and a widespread reddish-purple skin rash"),
    ]
    virus_name, pathogenesis = rng.choice(viral_diseases)
    prompt = (
        f"In humans, pathogenic viruses cause severe contagious diseases. "
        f"For example, **{virus_name}** {pathogenesis}.\n\n"
        f"Which of the following lists contains **ONLY** human diseases caused by viruses?"
    )
    correct = "HIV/AIDS, influenza (flu), measles, chickenpox, and rabies"
    options = [
        correct,
        "Tuberculosis, cholera, tetanus, and bubonic plague",
        "Malaria, amoebic dysentery, and sleeping sickness",
        "Athlete's foot, ringworm, and thrush",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish pathogen types by disease:\n"
        f"- Viral: HIV, influenza, measles, chickenpox, polio, rabies, mumps.\n"
        f"- Bacterial: TB, cholera, tetanus, typhoid.\n"
        f"- Protist: malaria, amoebic dysentery.\n"
        f"- Fungal: athlete's foot, ringworm, thrush.\n\n"
        f"**Step 2:** The list containing only viral diseases is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_08_{rng.randint(100000, 999999)}",
        "subskill": "08_human_viral_diseases_hiv_influenza_measles_rabies",
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
            "tier_1": "Recall which diseases are viral: flu, measles, chickenpox, rabies, HIV.",
            "tier_2": "TB and cholera are bacterial; malaria is protist.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["viral_disease_identification_misconception"],
    }


# 09. Why antibiotics are ineffective against viruses
def arch_09_why_antibiotics_are_ineffective_against_viruses(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A patient suffering from the common cold or viral influenza visits a clinic and demands a prescription for "
        f"the antibiotic penicillin. The doctor correctly refuses to prescribe antibiotics.\n\n"
        f"Why are **antibiotics completely ineffective** against viral infections?"
    )
    correct = (
        "Antibiotics specifically target bacterial structures (such as peptidoglycan cell walls or bacterial ribosomes) "
        "and metabolic pathways that viruses do not possess."
    )
    options = [
        correct,
        "Because antibiotics feed viruses and make them grow into giant insects.",
        "Because viruses are too intelligent and persuade antibiotics to switch sides.",
        "Because antibiotics only work on non-living rocks and plastics.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand antibiotic mechanism of action:\n"
        f"- Antibiotics (e.g. penicillin, amoxicillin) inhibit bacterial cell wall synthesis or bacterial protein translation.\n"
        f"- Viruses are acellular nanoparticles lacking cell walls, ribosomes, and independent metabolism; they replicate inside human host cells.\n"
        f"- Antibiotics have zero chemical targets on viruses; taking antibiotics for viral colds is medically useless and breeds antibiotic resistance.\n\n"
        f"**Step 2:** The reason is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_09_{rng.randint(100000, 999999)}",
        "subskill": "09_why_antibiotics_are_ineffective_against_viruses",
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
            "tier_1": "Do viruses have bacterial cell walls or ribosomes?",
            "tier_2": "Antibiotics target bacterial features that viruses lack completely.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["antibiotics_against_viruses_misconception"],
    }


# 10. Bacteria prokaryotic cell anatomy nucleoid and plasmids
def arch_10_bacteria_prokaryotic_cell_anatomy_nucleoid_and_plasmids(rng: random.Random) -> Dict[str, Any]:
    structures = [
        ("the nucleoid", "the irregularly shaped cytoplasmic region containing the single circular main bacterial chromosome"),
        ("plasmids", "small, circular, double-stranded extra-chromosomal DNA molecules that often carry antibiotic resistance genes"),
        ("flagella", "long, whip-like protein filaments that rotate to propel the bacterium through liquid media"),
        ("the capsule / slime layer", "an outer polysaccharide layer protecting the bacterium from desiccation and phagocytosis by host white blood cells"),
    ]
    organelle, function = rng.choice(structures)
    prompt = (
        f"In a generalized bacterial cell (Kingdom Monera), microscopic examination identifies **{organelle}**.\n\n"
        f"What is the specific biological structure and function of **{organelle}**?"
    )
    correct = f"It is {function}."
    options = [
        correct,
        "It is a double-membrane nucleus containing 46 linear human chromosomes.",
        "It is a digestive stomach lined with teeth to chew solid meat.",
        "It is a photosynthetic chloroplast storing green chlorophyll for animal cells.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review bacterial prokaryotic anatomy:\n"
        f"- {organelle.capitalize()}: {function}.\n"
        f"- Bacteria lack a nuclear envelope; genetic material resides in the nucleoid and independent plasmid rings.\n\n"
        f"**Step 2:** The true statement is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_10_{rng.randint(100000, 999999)}",
        "subskill": "10_bacteria_prokaryotic_cell_anatomy_nucleoid_and_plasmids",
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
            "tier_1": f"Think about the role of {organelle} in a bacterial cell.",
            "tier_2": f"It is {function}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["bacterial_anatomy_nucleoid_plasmid_misconception"],
    }


# 11. Bacterial morphology cocci bacilli spirilla vibrios (with dynamic SVG)
def arch_11_bacterial_morphology_cocci_bacilli_spirilla_vibrios(rng: random.Random) -> Dict[str, Any]:
    shapes = [
        ("coccus (plural: cocci)", "spherical or round-shaped cells (e.g. *Streptococcus*, *Staphylococcus*)"),
        ("bacillus (plural: bacilli)", "rod-shaped cylindrical cells (e.g. *Lactobacillus*, *Bacillus anthracis*)"),
        ("spirillum (plural: spirilla)", "rigid spiral or corkscrew-shaped cells (e.g. *Spirillum volutans*)"),
        ("vibrio (plural: vibrios)", "comma-shaped curved rod cells (e.g. *Vibrio cholerae*)"),
    ]
    target_shape, description = rng.choice(shapes)
    cell_fill = rng.choice(["#38bdf8", "#34d399", "#f472b6"])
    sample_code = rng.randint(100, 999)
    mag = rng.choice([1000, 1500, 2000])

    svg = (
        f'<svg viewBox="0 0 420 180" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="210" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Bacterial Morphological Shapes (Slide #{sample_code})</text>'
        f'<circle cx="60" cy="85" r="22" fill="{cell_fill}" stroke="#0369a1" stroke-width="2" />'
        f'<text x="60" y="130" font-size="10" fill="#0369a1" font-weight="bold" text-anchor="middle">Coccus (Round)</text>'
        f'<rect x="135" y="70" width="55" height="30" rx="15" fill="{cell_fill}" stroke="#059669" stroke-width="2" />'
        f'<text x="162" y="130" font-size="10" fill="#059669" font-weight="bold" text-anchor="middle">Bacillus (Rod)</text>'
        f'<path d="M 235 70 Q 250 85 240 100 T 255 115" fill="none" stroke="#7c3aed" stroke-width="3" />'
        f'<text x="250" y="130" font-size="10" fill="#7c3aed" font-weight="bold" text-anchor="middle">Spirillum (Spiral)</text>'
        f'<path d="M 335 75 Q 355 80 345 105" fill="none" stroke="#d97706" stroke-width="4" stroke-linecap="round" />'
        f'<text x="345" y="130" font-size="10" fill="#d97706" font-weight="bold" text-anchor="middle">Vibrio (Comma)</text>'
        f'<text x="210" y="162" font-size="10" fill="#64748b" text-anchor="middle">Magnification: {mag}x | Target feature: {target_shape.split()[0]}</text>'
        f'</svg>'
    )

    prompt = (
        f"Microbiologists classify bacteria into four primary morphological groups based on cellular shape.\n\n"
        f"Which bacterial morphology describes **{target_shape}**?"
    )
    correct = description
    alt_desc = [s[1] for s in shapes if s[0] != target_shape]
    options = [correct] + alt_desc
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review standard bacterial shapes:\n"
        f"- Coccus = spherical/round.\n"
        f"- Bacillus = rod-shaped.\n"
        f"- Spirillum = spiral/corkscrew.\n"
        f"- Vibrio = comma-shaped.\n\n"
        f"**Step 2:** {target_shape} corresponds to: **{correct}**."
    )
    return {
        "id": f"ns8_mic_11_{rng.randint(100000, 999999)}",
        "subskill": "11_bacterial_morphology_cocci_bacilli_spirilla_vibrios",
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
            "tier_1": f"Think about what shape {target_shape.split()[0]} means: round, rod, spiral, or comma?",
            "tier_2": f"{target_shape} is {description}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["bacterial_shape_classification_misconception"],
    }


# 12. Bacterial binary fission asexual reproduction dynamics
def arch_12_bacterial_binary_fission_asexual_reproduction_dynamics(rng: random.Random) -> Dict[str, Any]:
    gen_time_mins = rng.choice([20, 30])
    hours = 2
    generations = (hours * 60) // gen_time_mins
    start_bacteria = 1
    final_count = start_bacteria * (2 ** generations)
    prompt = (
        f"Under optimal laboratory conditions (warmth, moisture, and nutrients), a single bacterium of *E. coli* "
        f"divides by **binary fission** every {gen_time_mins} minutes.\n\n"
        f"How many bacterial cells will be produced from a single starting bacterium after {hours} hours of unhindered growth?"
    )
    correct = f"{final_count} cells (doubling {generations} times: 2^{generations} = {final_count})"
    wrong_1 = generations * 2
    wrong_2 = final_count // 2
    wrong_3 = start_bacteria + generations
    options = [
        correct,
        f"{wrong_1} cells",
        f"{wrong_2} cells",
        f"{wrong_3} cells",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Calculate number of division cycles (generations):\n"
        f"- Total time = {hours} hours = {hours * 60} minutes.\n"
        f"- Generation time = {gen_time_mins} minutes.\n"
        f"- Number of generations = {hours * 60} / {gen_time_mins} = **{generations} cycles**.\n\n"
        f"**Step 2:** Apply exponential binary fission ($N = N_0 \\times 2^n$):\n"
        f"- $N = 1 \\times 2^{{{generations}}} = **{final_count} cells**.\n\n"
        f"**Step 3:** The answer is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_12_{rng.randint(100000, 999999)}",
        "subskill": "12_bacterial_binary_fission_asexual_reproduction_dynamics",
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
            "tier_1": f"How many {gen_time_mins}-minute intervals are there in {hours} hours? That is {generations}.",
            "tier_2": f"Double the population {generations} times: 2^{generations} = {final_count}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["binary_fission_exponential_growth_misconception"],
    }


# 13. Bacterial endospores survival in extreme conditions
def arch_13_bacterial_endospores_survival_in_extreme_conditions(rng: random.Random) -> Dict[str, Any]:
    bacteria_sp = rng.choice([
        ("Clostridium tetani (causes tetanus in deep puncture wounds)", "soil and rusty nails"),
        ("Bacillus anthracis (causes anthrax in livestock)", "arid grazing pastures"),
        ("Clostridium botulinum (causes lethal food botulism in canned foods)", "anaerobic sealed containers"),
    ])
    prompt = (
        f"Certain bacteria such as **{bacteria_sp[0]}** can survive for decades in {bacteria_sp[1]} despite "
        f"extreme drought, intense heat, freezing cold, and chemical disinfectants by forming **endospores**.\n\n"
        f"What is a bacterial **endospore**, and what is its biological purpose?"
    )
    correct = (
        "A tough, dormant, non-reproductive structure enclosing the bacterial DNA and essential cytoplasm "
        "that allows the bacterium to survive lethal environmental conditions until favourable conditions return."
    )
    options = [
        correct,
        "A sexual reproductive egg that hatches into swimming tadpoles.",
        "A venomous tooth used by bacteria to bite human skin.",
        "A green leaf bud that carries out photosynthesis in pitch darkness.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define bacterial endospores:\n"
        f"- An endospore is not a method of reproduction (1 bacterium produces 1 endospore, which germinates into 1 bacterium; no numerical increase).\n"
        f"- It is a survival capsule: thick peptidoglycan and keratin-like protein coat protecting dehydrated bacterial DNA.\n"
        f"- When moisture and nutrients return, the spore germinates into an active vegetative cell.\n\n"
        f"**Step 2:** The purpose is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_13_{rng.randint(100000, 999999)}",
        "subskill": "13_bacterial_endospores_survival_in_extreme_conditions",
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
            "tier_1": "Is an endospore a baby bacterium or a tough survival capsule for hard times?",
            "tier_2": "It is a dormant survival structure to withstand extreme heat, drought, and chemicals.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["endospore_reproduction_vs_survival_misconception"],
    }


# 14. Autotrophic vs heterotrophic bacteria nutrition
def arch_14_autotrophic_vs_heterotrophic_bacteria_nutrition(rng: random.Random) -> Dict[str, Any]:
    types = [
        ("cyanobacteria (blue-green bacteria in freshwater dams)", "Autotrophic (photosynthetic)", "synthesising organic glucose using light energy and chlorophyll"),
        ("saprophytic soil decomposer bacteria", "Heterotrophic (saprophytic)", "secreting extracellular enzymes to digest dead organic plant and animal tissues"),
        ("pathogenic *Mycobacterium tuberculosis* in human lung tissue", "Heterotrophic (parasitic)", "absorbing organic nutrients directly from living human host tissue and causing damage"),
    ]
    bacteria_name, nutrition_mode, description = rng.choice(types)
    prompt = (
        f"Bacteria exhibit diverse nutritional modes. Consider {bacteria_name}, which obtains energy by {description}.\n\n"
        f"How is this bacterium classified according to its mode of nutrition?"
    )
    correct = nutrition_mode
    alt_modes = [t[1] for t in types if t[1] != nutrition_mode]
    options = [correct] + alt_modes
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Classify bacterial nutrition:\n"
        f"- Autotrophic: synthesizes own food (e.g. photosynthetic cyanobacteria).\n"
        f"- Heterotrophic: obtains food from external organic sources.\n"
        f"  - Saprophytic: feeds on dead matter (decomposers).\n"
        f"  - Parasitic: feeds on living hosts (pathogens).\n\n"
        f"**Step 2:** For {bacteria_name}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_14_{rng.randint(100000, 999999)}",
        "subskill": "14_autotrophic_vs_heterotrophic_bacteria_nutrition",
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
            "tier_1": "Does it make its own food or feed on external dead or living matter?",
            "tier_2": f"It is classified as {nutrition_mode}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["bacterial_nutrition_mode_misconception"],
    }


# 15. Pathogenic bacteria tuberculosis transmission and symptoms
def arch_15_pathogenic_bacteria_tuberculosis_transmission_and_symptoms(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Tuberculosis (TB) is a major public health priority in South Africa, caused by the bacterium "
        f"***Mycobacterium tuberculosis*.\n\n"
        f"How is Tuberculosis transmitted between individuals, and what are its primary clinical symptoms?"
    )
    correct = (
        "Transmitted via airborne droplet infection when an infected person coughs, sneezes, or spits; "
        "symptoms include persistent coughing (often coughing up blood), night sweats, chronic fever, and dramatic weight loss."
    )
    options = [
        correct,
        "Transmitted by eating uncooked green cabbage; symptoms include blue skin and growing extra teeth.",
        "Transmitted by touching metallic computer keyboards; symptoms include temporary loss of eyesight.",
        "Transmitted through mosquito bites in winter; symptoms include swelling of fingernails.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Detail Tuberculosis pathology:\n"
        f"- Pathogen: *Mycobacterium tuberculosis* (rod-shaped bacillus).\n"
        f"- Transmission: airborne droplet infection through aerosols exhaled during coughing or sneezing.\n"
        f"- Primary site: lungs (pulmonary TB), forming tubercles in alveoli.\n"
        f"- Symptoms: persistent cough >2 weeks, chest pains, hemoptysis (coughing blood), fever, fatigue, drenching night sweats, weight loss ('consumption').\n\n"
        f"**Step 2:** The mode and symptoms are: **{correct}**."
    )
    return {
        "id": f"ns8_mic_15_{rng.randint(100000, 999999)}",
        "subskill": "15_pathogenic_bacteria_tuberculosis_transmission_and_symptoms",
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
            "tier_1": "How does TB spread: in the air by coughing or in food?",
            "tier_2": "TB is airborne; symptoms include persistent coughing, night sweats, and weight loss.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["tuberculosis_transmission_symptoms_misconception"],
    }


# 16. Pathogenic bacteria cholera waterborne dehydration and treatment
def arch_16_pathogenic_bacteria_cholera_waterborne_dehydration_and_treatment(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Cholera outbreaks, caused by the comma-shaped bacterium ***Vibrio cholerae***, occasionally occur "
        f"in communities where municipal sanitation infrastructure fails.\n\n"
        f"What is the primary mode of cholera transmission, and what is the urgent life-saving medical treatment for severe cholera?"
    )
    correct = (
        "Transmission occurs via ingestion of water or food contaminated with human fecal waste; "
        "immediate life-saving treatment requires aggressive **Oral Rehydration Therapy (ORT)** "
        "using a balanced solution of clean water, salts, and glucose to replace massive fluid loss."
    )
    options = [
        correct,
        "Transmission occurs by breathing desert dust; treatment requires drinking pure sulfuric acid.",
        "Transmission occurs through radioactive cell phone signals; treatment requires sleeping in a magnetic box.",
        "Transmission occurs from touching dog fur; treatment requires eating dry potato flour.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze cholera transmission and treatment:\n"
        f"- Pathogen: *Vibrio cholerae* produces cholera toxin in the small intestine, causing severe watery diarrhea ('rice-water stools') and vomiting.\n"
        f"- Route: fecal-oral via contaminated drinking water supplies.\n"
        f"- Danger: rapid fatal dehydration and electrolyte shock within hours.\n"
        f"- Immediate treatment: Oral Rehydration Salts (ORS) / ORT restoring electrolytes and water balance.\n\n"
        f"**Step 2:** The transmission and treatment: **{correct}**."
    )
    return {
        "id": f"ns8_mic_16_{rng.randint(100000, 999999)}",
        "subskill": "16_pathogenic_bacteria_cholera_waterborne_dehydration_and_treatment",
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
            "tier_1": "How does cholera spread in poor sanitation, and how do you stop dehydration?",
            "tier_2": "Spread via contaminated water; treated with Oral Rehydration Therapy (ORT).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cholera_waterborne_rehydration_misconception"],
    }


# 17. Antibiotic treatment discovery penicillin and mechanism
def arch_17_antibiotic_treatment_discovery_penicillin_and_mechanism(rng: random.Random) -> Dict[str, Any]:
    year = 1928
    scientist = "Alexander Fleming"
    mould = "*Penicillium notatum*"
    prompt = (
        f"In {year}, Scottish scientist {scientist} noticed that an agar culture plate of *Staphylococcus* bacteria "
        f"had become accidentally contaminated with the blue-green mould {mould}. "
        f"Around the mould, a clear halo had formed where bacteria could not grow.\n\n"
        f"What revolutionary medical substance did Fleming discover, and how does it kill bacteria?"
    )
    correct = (
        "**Penicillin** (the first true antibiotic); it inhibits the enzyme that builds bacterial cell walls, "
        "causing multiplying bacteria to burst (lyse) due to osmotic pressure."
    )
    options = [
        correct,
        "Paracetamol; it cures all headaches by freezing brain cells.",
        "Chloroform; it makes bacteria fall asleep so human white blood cells can arrest them.",
        "Aspirin; it permanently stops human blood from circulating to starve bacteria.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Recall the historical discovery of penicillin:\n"
        f"- In {year}, {scientist} discovered that *Penicillium* mould secretes a chemical that kills bacteria: penicillin.\n"
        f"- Mechanism: Penicillin blocks transpeptidase enzymes that cross-link peptidoglycan cell walls in Gram-positive bacteria.\n"
        f"- Without rigid cell walls, growing bacterial cells burst under internal osmotic pressure.\n\n"
        f"**Step 2:** The discovery and mechanism: **{correct}**."
    )
    return {
        "id": f"ns8_mic_17_{rng.randint(100000, 999999)}",
        "subskill": "17_antibiotic_treatment_discovery_penicillin_and_mechanism",
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
            "tier_1": "What famous antibiotic was discovered from Penicillium mould by Alexander Fleming?",
            "tier_2": "It was penicillin, which destroys bacterial cell walls.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["penicillin_discovery_mechanism_misconception"],
    }


# 18. Antibiotic resistance evolution and superbugs
def arch_18_antibiotic_resistance_evolution_and_superbugs(rng: random.Random) -> Dict[str, Any]:
    superbug = rng.choice([
        ("MDR-TB (Multi-Drug Resistant Tuberculosis)", "strains of *Mycobacterium tuberculosis* that have evolved resistance to first-line antibiotics isoniazid and rifampicin"),
        ("MRSA (Methicillin-Resistant Staphylococcus aureus)", "strains of *Staphylococcus* hospital bacteria that survive powerful beta-lactam antibiotics"),
    ])
    prompt = (
        f"Global health authorities warn of the dangerous rise of 'superbugs', such as {superbug[0]} ({superbug[1]}).\n\n"
        f"Which human medical practices are accelerating the natural selection of **antibiotic-resistant bacteria**?"
    )
    correct = (
        "Overprescribing antibiotics for viral infections, failing to finish the full prescribed antibiotic course, "
        "and widespread routine overuse of sub-therapeutic antibiotics in intensive livestock farming."
    )
    options = [
        correct,
        "Washing hands with warm tap water and ordinary toilet soap after using the restroom.",
        "Exercising regularly in the morning and eating fresh indigenous fruits.",
        "Boiling drinking water to sterilize microbial pathogens before drinking.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze drivers of antibiotic resistance:\n"
        f"- Bacteria naturally evolve mutations providing resistance (e.g. producing beta-lactamase or efflux pumps).\n"
        f"- Inappropriate human antibiotic use creates intense artificial selective pressure:\n"
        f"  1. Stopping medication early kills sensitive strains, leaving resistant mutants to proliferate.\n"
        f"  2. Overuse for colds/flu exposes normal flora to selective pressures needlessly.\n"
        f"  3. Agricultural livestock use promotes widespread resistance in farm runoff.\n\n"
        f"**Step 2:** The accelerating practices are: **{correct}**."
    )
    return {
        "id": f"ns8_mic_18_{rng.randint(100000, 999999)}",
        "subskill": "18_antibiotic_resistance_evolution_and_superbugs",
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
            "tier_1": "What happens when patients stop taking their antibiotic pills as soon as they feel better?",
            "tier_2": "Resistant bacteria survive, multiply, and spread.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["antibiotic_resistance_misuse_misconception"],
    }


# 19. Kingdom Protista eukaryotic diversity overview
def arch_19_kingdom_protista_eukaryotic_diversity_overview(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The **Kingdom Protista** is often referred to by biologists as a taxonomic 'catch-all' kingdom.\n\n"
        f"What primary cellular and evolutionary characteristic unites all organisms classified within Kingdom Protista?"
    )
    correct = (
        "They are all **eukaryotic** organisms (possessing a true membrane-bound nucleus and organelles), "
        "mostly unicellular or simple colonial, that cannot be classified as true plants, true animals, or true fungi."
    )
    options = [
        correct,
        "They are all acellular nanoparticles containing only radioactive uranium.",
        "They are all prokaryotes lacking any cellular chromosomes or nucleic acids.",
        "They are all multicellular mammals with warm blood and mammary glands.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define Kingdom Protista:\n"
        f"- Protists are eukaryotes (have a true nucleus and mitochondria).\n"
        f"- Most are single-celled (e.g. *Amoeba*, *Euglena*, *Paramecium*), though some are simple multicellular (e.g. giant kelp seaweed).\n"
        f"- They do not develop specialized tissues or organs characteristic of higher plants, animals, or fungi.\n\n"
        f"**Step 2:** The uniting characteristic is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_19_{rng.randint(100000, 999999)}",
        "subskill": "19_kingdom_protista_eukaryotic_diversity_overview",
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
            "tier_1": "Are protists prokaryotes (like bacteria) or eukaryotes (with a nucleus)?",
            "tier_2": "Protists are simple eukaryotic organisms.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["protista_eukaryote_definition_misconception"],
    }


# 20. Plant-like protists algae photosynthesis and ecological role
def arch_20_plant_like_protists_algae_photosynthesis_and_ecological_role(rng: random.Random) -> Dict[str, Any]:
    algae_types = [
        ("*Spirogyra*", "filamentous green freshwater algae with spiral ribbon-like chloroplasts", "freshwater streams and farm dams"),
        ("diatoms", "microscopic single-celled algae with intricate silica (glass-like) cell walls", "surface marine and freshwater plankton"),
        ("sea bamboo kelp (*Ecklonia maxima*)", "large brown marine algae forming dense underwater coastal kelp forests", "the cold Benguela current off the Western Cape"),
    ]
    alga, feature, habitat = rng.choice(algae_types)
    prompt = (
        f"Consider the plant-like protist **{alga}** ({feature}), found in {habitat}.\n\n"
        f"What is the vital ecological role of plant-like protists (algae) in global aquatic ecosystems?"
    )
    correct = (
        "They are primary autotrophic producers that perform photosynthesis, capturing radiant solar energy, "
        "producing organic food that forms the foundation of aquatic food webs, and releasing vast amounts of oxygen."
    )
    options = [
        correct,
        "They hunt small fish using venomous claws to suck out their blood.",
        "They turn ocean water into solid granite stone to build coral reefs.",
        "They absorb all dissolved oxygen to freeze the ocean floor solid.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the ecological role of algae:\n"
        f"- Plant-like protists contain chloroplasts with chlorophyll.\n"
        f"- They carry out photosynthesis: producing glucose and oxygen.\n"
        f"- Phytoplankton algae form the base (Trophic Level 1) of all aquatic and marine food webs.\n\n"
        f"**Step 2:** The vital role is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_20_{rng.randint(100000, 999999)}",
        "subskill": "20_plant_like_protists_algae_photosynthesis_and_ecological_role",
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
            "tier_1": "Do algae make food by photosynthesis?",
            "tier_2": "Algae are primary producers that generate food and oxygen in aquatic ecosystems.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["algae_ecological_role_misconception"],
    }


# 21. Animal-like protists protozoa amoeba and paramecium locomotion
def arch_21_animal_like_protists_protozoa_amoeba_and_paramecium_locomotion(rng: random.Random) -> Dict[str, Any]:
    protozoans = [
        ("*Amoeba proteus*", "pseudopodia ('false feet')", "streaming cytoplasm into temporary projections for locomotion and engulfing prey via phagocytosis"),
        ("*Paramecium caudatum*", "cilia", "thousands of coordinated microscopic hair-like beats propelling the organism smoothly through pond water"),
        ("*Euglena gracilis*", "a flagellum", "a long whip-like filament that pulls the single-celled organism through water toward light"),
    ]
    organism, organ_of_locomotion, action = rng.choice(protozoans)
    prompt = (
        f"The single-celled animal-like protist **{organism}** moves actively through pond water using **{organ_of_locomotion}** ({action}).\n\n"
        f"How is **{organism}** classified biologically based on its feeding and cellular structure?"
    )
    correct = "A single-celled eukaryotic protozoan (Kingdom Protista)"
    options = [
        correct,
        "A prokaryotic bacterium lacking any cellular nucleus (Kingdom Monera)",
        "An acellular pathogenic virus enclosed in a protein capsid",
        "A multicellular invertebrate animal with a bony skeleton (Kingdom Animalia)",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Classify protozoans:\n"
        f"- Protozoa are animal-like single-celled eukaryotes.\n"
        f"- They possess true nuclei, food vacuoles, contractile vacuoles, and specialized organelles of locomotion ({organ_of_locomotion}).\n\n"
        f"**Step 2:** The classification is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_21_{rng.randint(100000, 999999)}",
        "subskill": "21_animal_like_protists_protozoa_amoeba_and_paramecium_locomotion",
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
            "tier_1": f"Is {organism.split()[0]} a single-celled eukaryote or a bacterium?",
            "tier_2": "It is a single-celled eukaryotic protozoan.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["protozoa_locomotion_classification_misconception"],
    }


# 22. Malaria Plasmodium life cycle and Anopheles mosquito vector (with dynamic SVG)
def arch_22_malaria_plasmodium_life_cycle_and_anopheles_mosquito_vector(rng: random.Random) -> Dict[str, Any]:
    province = rng.choice(["Mpumalanga lowveld", "Limpopo river valleys", "northeastern KwaZulu-Natal"])
    vector_color = rng.choice(["#78350f", "#451a03", "#292524"])

    svg = (
        f'<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px;">'
        f'<text x="210" y="24" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">Malaria Transmission Cycle ({province})</text>'
        f'<rect x="30" y="55" width="160" height="75" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5" rx="6" />'
        f'<text x="110" y="80" font-size="11" fill="#991b1b" font-weight="bold" text-anchor="middle">Human Host</text>'
        f'<text x="110" y="100" font-size="9" fill="#7f1d1d" text-anchor="middle">Liver cells &gt; Red Blood Cells</text>'
        f'<text x="110" y="118" font-size="9" fill="#dc2626" font-weight="bold" text-anchor="middle">RBCs burst (chills &amp; fever)</text>'
        f'<rect x="230" y="55" width="160" height="75" fill="#fefce8" stroke="{vector_color}" stroke-width="1.5" rx="6" />'
        f'<text x="310" y="80" font-size="11" fill="{vector_color}" font-weight="bold" text-anchor="middle">Mosquito Vector</text>'
        f'<text x="310" y="100" font-size="9" fill="#713f12" text-anchor="middle">Female Anopheles mosquito</text>'
        f'<text x="310" y="118" font-size="9" fill="#a16207" text-anchor="middle">Injects sporozoites in saliva</text>'
        f'<path d="M 190 75 L 230 75" stroke="#dc2626" stroke-width="2" marker-end="url(#arrow)" />'
        f'<path d="M 230 115 L 190 115" stroke="#2563eb" stroke-width="2" marker-end="url(#arrow)" />'
        f'<text x="210" y="180" font-size="11" fill="#1e293b" font-weight="bold" text-anchor="middle">Pathogen: Plasmodium (Protist) | Vector: Female Anopheles Mosquito</text>'
        f'<text x="210" y="202" font-size="10" fill="#64748b" text-anchor="middle">Mosquito is the vector (carrier), NOT the pathogen itself</text>'
        f'</svg>'
    )

    prompt = (
        f"In endemic regions of South Africa such as the {province}, **malaria** poses a serious health risk.\n\n"
        f"What is the specific **causative pathogen** of malaria, and what organism acts as the **biological vector** transmitting it to humans?"
    )
    correct = (
        "Causative pathogen: ***Plasmodium*** (a parasitic unicellular protist) | "
        "Biological vector: the **female *Anopheles* mosquito**"
    )
    options = [
        correct,
        "Causative pathogen: the female Anopheles mosquito | Biological vector: dirty stagnant river water",
        "Causative pathogen: a bacterium called *E. coli* | Biological vector: houseflies",
        "Causative pathogen: an airborne respiratory virus | Biological vector: domestic dogs",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish pathogen from vector in malaria:\n"
        f"- Pathogen (the microscopic organism causing the disease): *Plasmodium falciparum* (Kingdom Protista).\n"
        f"- Vector (the carrier transmitting the pathogen): the female *Anopheles* mosquito (which requires a blood meal to develop eggs).\n"
        f"- Inside humans, *Plasmodium* multiplies in the liver and destroys red blood cells, triggering periodic fever cycles.\n\n"
        f"**Step 2:** The pathogen and vector: **{correct}**."
    )
    return {
        "id": f"ns8_mic_22_{rng.randint(100000, 999999)}",
        "subskill": "22_malaria_plasmodium_life_cycle_and_anopheles_mosquito_vector",
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
            "tier_1": "Is the mosquito the disease organism itself or the carrier vector?",
            "tier_2": "The pathogen is Plasmodium (a protist); the vector is the female Anopheles mosquito.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["malaria_pathogen_vs_vector_misconception"],
    }


# 23. Malaria symptoms prevention bednets and treatment
def arch_23_malaria_symptoms_prevention_bednets_and_treatment(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When traveling to malaria-endemic regions in southern Africa, health authorities recommend "
        f"strict preventative measures.\n\n"
        f"Which combination represents the most effective proven strategy for preventing malaria infection?"
    )
    correct = (
        "Sleeping under insecticide-treated bed nets, applying DEET insect repellent, installing window screens, "
        "eliminating standing stagnant water where mosquitoes breed, and taking prophylactic antimalarial medication."
    )
    options = [
        correct,
        "Drinking 10 litres of unboiled river water every hour to wash out mosquitoes.",
        "Taking heavy courses of antibacterial penicillin pills every night.",
        "Wearing bright yellow clothing to blind mosquitoes with reflective glare.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze malaria preventative strategies:\n"
        f"- *Anopheles* mosquitoes bite predominantly between dusk and dawn.\n"
        f"- Physical/chemical barriers: insecticide-treated nets (ITNs) and repellents prevent mosquito bites.\n"
        f"- Vector control: removing standing water (disrupts mosquito larval stage).\n"
        f"- Chemoprophylaxis: preventative antimalarials destroy *Plasmodium* parasites before symptoms develop.\n\n"
        f"**Step 2:** The effective strategy is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_23_{rng.randint(100000, 999999)}",
        "subskill": "23_malaria_symptoms_prevention_bednets_and_treatment",
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
            "tier_1": "How do you stop mosquitoes from biting you while you sleep?",
            "tier_2": "Insecticide-treated bed nets, repellents, and antimalarial medication.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["malaria_prevention_strategy_misconception"],
    }


# 24. Kingdom Fungi eukaryotic saprophytes chitin cell walls
def arch_24_kingdom_fungi_eukaryotic_saprophytes_chitin_cell_walls(rng: random.Random) -> Dict[str, Any]:
    fungi_examples = [
        ("field mushrooms (*Agaricus bisporus*)", "multicellular fruiting bodies emerging from underground mycelia in rich soil"),
        ("black bread mould (*Rhizopus stolonifer*)", "fuzzy dark mould colonies spreading across moist stale bread"),
        ("baker's yeast (*Saccharomyces cerevisiae*)", "microscopic single-celled fungi used in bread making and beer brewing"),
    ]
    fungus, desc = rng.choice(fungi_examples)
    prompt = (
        f"Organisms belonging to the **Kingdom Fungi**, such as {fungus} ({desc}), were historically grouped with plants.\n\n"
        f"Why are fungi classified in their own distinct kingdom separate from Kingdom Plantae?"
    )
    correct = (
        "Fungi are **heterotrophic** (lack chlorophyll and cannot photosynthesise, feeding instead by extracellular digestion) "
        "and have cell walls constructed of **chitin** rather than plant cellulose."
    )
    options = [
        correct,
        "Fungi are non-living minerals made of pure silica and volcanic glass.",
        "Fungi are animals that possess eyes, legs, and a beating heart.",
        "Fungi produce radioactive energy that dissolves all nearby plant cells.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish Fungi from Plantae:\n"
        f"- Nutrition: Plants are autotrophic (photosynthetic); Fungi are heterotrophic saprophytes (secrete digestive enzymes externally and absorb soluble nutrients).\n"
        f"- Cell wall: Plant walls = cellulose; Fungal walls = chitin (the same tough structural polymer found in arthropod exoskeletons).\n"
        f"- Energy storage: Fungi store energy as glycogen (like animals), not starch (like plants).\n\n"
        f"**Step 2:** The fundamental distinction is: **{correct}**."
    )
    return {
        "id": f"ns8_mic_24_{rng.randint(100000, 999999)}",
        "subskill": "24_kingdom_fungi_eukaryotic_saprophytes_chitin_cell_walls",
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
            "tier_1": "Do mushrooms have green chlorophyll to make food from sunlight?",
            "tier_2": "Fungi cannot photosynthesise (heterotrophs) and have chitin cell walls.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fungi_vs_plant_distinction_misconception"],
    }


# 25. Fungal morphology hyphae mycelium and spore reproduction
def arch_25_fungal_morphology_hyphae_mycelium_and_spore_reproduction(rng: random.Random) -> Dict[str, Any]:
    structures = [
        ("hyphae", "thread-like branching filaments that secrete enzymes and absorb digested nutrients"),
        ("mycelium", "the dense interwoven subterranean or substrate-embedded vegetative network of hyphae"),
        ("sporangium", "a rounded structure borne on aerial stalks that produces and releases thousands of microscopic airborne spores"),
    ]
    target_part, function = rng.choice(structures)
    prompt = (
        f"In multicellular fungi (such as bread mould or forest mushrooms), the fungal body exhibits specialized structures: "
        f"hyphae, mycelium, and sporangia.\n\n"
        f"What is the definition and structural role of **{target_part}**?"
    )
    correct = f"It is {function}."
    options = [
        correct,
        "It is a muscular pumping heart that circulates warm red blood.",
        "It is a green photosynthetic leaf that absorbs radiant sunlight.",
        "It is a hard metallic shell that reflects ultraviolet radiation.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review multicellular fungal anatomy:\n"
        f"- Hyphae: microscopic thread-like filaments forming the building blocks of fungi.\n"
        f"- Mycelium: the mass/network of interconnected hyphae.\n"
        f"- Sporangium: spore-producing capsule releasing reproductive spores.\n\n"
        f"**Step 2:** For {target_part}: **{correct}**."
    )
    return {
        "id": f"ns8_mic_25_{rng.randint(100000, 999999)}",
        "subskill": "25_fungal_morphology_hyphae_mycelium_and_spore_reproduction",
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
            "tier_1": f"Think about whether {target_part} is a single thread, a whole network, or a spore capsule.",
            "tier_2": f"{target_part.capitalize()} is {function}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fungal_morphology_hyphae_mycelium_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "01_microorganisms_definition_and_microscopic_scale": arch_01_microorganisms_definition_and_microscopic_scale,
    "02_five_kingdom_classification_system_overview": arch_02_five_kingdom_classification_system_overview,
    "03_prokaryote_vs_eukaryote_cellular_distinction": arch_03_prokaryote_vs_eukaryote_cellular_distinction,
    "04_viruses_acellular_nature_living_vs_nonliving_boundary": arch_04_viruses_acellular_nature_living_vs_nonliving_boundary,
    "05_viral_structure_capsid_protein_and_dna_or_rna_core": arch_05_viral_structure_capsid_protein_and_dna_or_rna_core,
    "06_viruses_as_obligate_intracellular_parasites_mechanism": arch_06_viruses_as_obligate_intracellular_parasites_mechanism,
    "07_bacteriophages_structure_and_bacterial_infection": arch_07_bacteriophages_structure_and_bacterial_infection,
    "08_human_viral_diseases_hiv_influenza_measles_rabies": arch_08_human_viral_diseases_hiv_influenza_measles_rabies,
    "09_why_antibiotics_are_ineffective_against_viruses": arch_09_why_antibiotics_are_ineffective_against_viruses,
    "10_bacteria_prokaryotic_cell_anatomy_nucleoid_and_plasmids": arch_10_bacteria_prokaryotic_cell_anatomy_nucleoid_and_plasmids,
    "11_bacterial_morphology_cocci_bacilli_spirilla_vibrios": arch_11_bacterial_morphology_cocci_bacilli_spirilla_vibrios,
    "12_bacterial_binary_fission_asexual_reproduction_dynamics": arch_12_bacterial_binary_fission_asexual_reproduction_dynamics,
    "13_bacterial_endospores_survival_in_extreme_conditions": arch_13_bacterial_endospores_survival_in_extreme_conditions,
    "14_autotrophic_vs_heterotrophic_bacteria_nutrition": arch_14_autotrophic_vs_heterotrophic_bacteria_nutrition,
    "15_pathogenic_bacteria_tuberculosis_transmission_and_symptoms": arch_15_pathogenic_bacteria_tuberculosis_transmission_and_symptoms,
    "16_pathogenic_bacteria_cholera_waterborne_dehydration_and_treatment": arch_16_pathogenic_bacteria_cholera_waterborne_dehydration_and_treatment,
    "17_antibiotic_treatment_discovery_penicillin_and_mechanism": arch_17_antibiotic_treatment_discovery_penicillin_and_mechanism,
    "18_antibiotic_resistance_evolution_and_superbugs": arch_18_antibiotic_resistance_evolution_and_superbugs,
    "19_kingdom_protista_eukaryotic_diversity_overview": arch_19_kingdom_protista_eukaryotic_diversity_overview,
    "20_plant_like_protists_algae_photosynthesis_and_ecological_role": arch_20_plant_like_protists_algae_photosynthesis_and_ecological_role,
    "21_animal_like_protists_protozoa_amoeba_and_paramecium_locomotion": arch_21_animal_like_protists_protozoa_amoeba_and_paramecium_locomotion,
    "22_malaria_plasmodium_life_cycle_and_anopheles_mosquito_vector": arch_22_malaria_plasmodium_life_cycle_and_anopheles_mosquito_vector,
    "23_malaria_symptoms_prevention_bednets_and_treatment": arch_23_malaria_symptoms_prevention_bednets_and_treatment,
    "24_kingdom_fungi_eukaryotic_saprophytes_chitin_cell_walls": arch_24_kingdom_fungi_eukaryotic_saprophytes_chitin_cell_walls,
    "25_fungal_morphology_hyphae_mycelium_and_spore_reproduction": arch_25_fungal_morphology_hyphae_mycelium_and_spore_reproduction,
}
