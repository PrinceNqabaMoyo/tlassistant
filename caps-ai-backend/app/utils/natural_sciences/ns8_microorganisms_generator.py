"""Natural Sciences Grade 8 Term 2: Microorganisms Generator.

Strictly grounded in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/03. Microorganisms.md.
Covers:
- microorganism_types_and_characteristics: Viruses (capsid + nucleic acid), Bacteria, Protists, Fungi.
- pathogens_and_infectious_diseases: Transmission vectors, cholera, tuberculosis, malaria, HIV, fungal infections.
- beneficial_uses_of_microorganisms: Fermentation (yeast, lactic bacteria), nutrient cycling, penicillin, vaccines.
- preventing_spread_and_sterilisation: Pasteurisation, sterilization, refrigeration, hygiene, water treatment.
- antibiotics_vs_antivirals_efficacy: Antibiotic action on bacteria vs ineffectiveness on viral capsids; resistance.

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


SUBSKILLS = [
    "microorganism_types_and_characteristics",
    "pathogens_and_infectious_diseases",
    "beneficial_uses_of_microorganisms",
    "preventing_spread_and_sterilisation",
    "antibiotics_vs_antivirals_efficacy",
]


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _build_microorganism_types(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    types = [
        {
            "name": "Viruses",
            "feature": "Acellular microscopic particles (20-300 nm) consisting of a core of DNA or RNA surrounded by a protein capsid, requiring a living host cell to replicate",
            "kingdom": "Not classified in the 5 kingdoms because they show both living and non-living characteristics",
            "distractors": ["Kingdom Monera (prokaryotic cells)", "Kingdom Protista (eukaryotic single cells)", "Kingdom Fungi (spore-forming multicellular decomposers)"]
        },
        {
            "name": "Bacteria",
            "feature": "Single-celled prokaryotic microscopic organisms belonging to Kingdom Monera that lack a membrane-bound nucleus and reproduce by binary fission",
            "kingdom": "Kingdom Monera",
            "distractors": ["Acellular infectious nucleic acid capsules", "Multicellular autotrophic flowering plants", "Complex eukaryotic animals with vertebrate skeletons"]
        },
        {
            "name": "Fungi (Yeasts and Moulds)",
            "feature": "Eukaryotic organisms possessing chitinous cell walls that absorb nutrients from their surroundings as heterotrophic saprophytes",
            "kingdom": "Kingdom Fungi",
            "distractors": ["Acellular obligate intracellular parasites", "Prokaryotic organisms without nuclear membranes", "Photosynthetic algae with cellulose walls"]
        }
    ]
    t = rng.choice(types)
    prompt = (
        f"In biological classification, micro-organisms are grouped according to their cellular structure and metabolic behavior.\n\n"
        f"Which group of micro-organisms is described by the following characteristics?\n"
        f"\"{t['feature']}\""
    )
    correct_ans = f"{t['name']} ({t['kingdom']})"
    options = [correct_ans] + [f"{d}" for d in t["distractors"]]
    rng.shuffle(options)
    c_idx = options.index(correct_ans)
    c_letter = chr(65 + c_idx)
    sample_ans = f"{c_letter}. {correct_ans}"
    sol = (
        f"**{sample_ans}** [2 marks]\n\n"
        f"Step 1: Analyze cellular features:\n"
        f"{t['feature']}.\n\n"
        f"Step 2: Match to taxonomic classification:\n"
        f"This precisely defines **{t['name']}**, which are classified under {t['kingdom']}."
    )
    return {
        "id": _make_id("ns8_micro_types", seed, idx),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": correct_ans,
        "sample_answer": sample_ans,
        "ideal_answer": sample_ans,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "microorganism_types_and_characteristics",
        "question_family_id": "microorganism_types_and_characteristics",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Microorganisms > Classification of microorganisms",
        "hints": {
            "tier_1": "Determine whether the organism is cellular or acellular, prokaryotic or eukaryotic.",
            "tier_2": "Viruses lack cells and have protein capsids; bacteria lack a nucleus; fungi have chitin walls.",
            "tier_3": f"The organism described is {t['name']}."
        },
        "misconception_tags": ["confuses_viruses_with_bacteria"]
    }


def _build_pathogens_diseases(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    diseases = [
        {
            "disease": "Cholera",
            "agent": "Vibrio cholerae bacterium",
            "transmission": "Drinking water contaminated with human fecal sewage",
            "symptoms": "Severe acute watery diarrhea and rapid dehydration",
            "prevention": "Boiling or chlorinating drinking water and proper sanitation infrastructure"
        },
        {
            "disease": "Tuberculosis (TB)",
            "agent": "Mycobacterium tuberculosis bacterium",
            "transmission": "Inhaling airborne microscopic droplets expelled when an infected person coughs or sneezes",
            "symptoms": "Persistent cough with blood, chest pains, fever, and severe weight loss",
            "prevention": "BCG vaccination, well-ventilated rooms, and a completed 6-month course of antibiotics"
        },
        {
            "disease": "Malaria",
            "agent": "Plasmodium parasite (a single-celled protozoan / protist)",
            "transmission": "Bite of an infected female Anopheles mosquito vector",
            "symptoms": "High recurrent fevers, chills, profuse sweating, and anemia",
            "prevention": "Insecticide-treated bed nets, draining stagnant water, and antimalarial medication"
        }
    ]
    d = rng.choice(diseases)
    other_d = [x for x in diseases if x["disease"] != d["disease"]]

    correct_opt = f"Pathogen: {d['agent']}; Transmission: {d['transmission']}; Prevention: {d['prevention']}."
    distractor_1 = f"Pathogen: {other_d[0]['agent']}; Transmission: {other_d[0]['transmission']}; Prevention: {other_d[0]['prevention']}."
    distractor_2 = f"Pathogen: {other_d[1]['agent']}; Transmission: {d['transmission']}; Prevention: {other_d[1]['prevention']}."
    distractor_3 = f"Pathogen: Influenza virus; Transmission: Casual skin contact; Prevention: Taking multivitamin supplements."

    opts = [correct_opt, distractor_1, distractor_2, distractor_3]
    rng.shuffle(opts)
    c_idx = opts.index(correct_opt)
    c_letter = chr(65 + c_idx)
    sample_ans = f"{c_letter}. {correct_opt}"
    worked_sol = (
        f"**{sample_ans}** [2 marks]\n\n"
        f"Explanation: {d['disease']} is caused by {d['agent']}. It is transmitted via {d['transmission'].lower()}, "
        f"and the primary prevention strategy is {d['prevention'].lower()}."
    )

    prompt = (
        f"In South African healthcare and community epidemiology, waterborne and airborne diseases pose major public health challenges.\n\n"
        f"Which of the following correctly identifies the causative pathogen, transmission method, and primary prevention measure for **{d['disease']}**?"
    )

    return {
        "id": _make_id("ns8_pathogen", seed, idx),
        "question_type": "mcq",
        "prompt": prompt,
        "options": opts,
        "correct_index": str(c_idx),
        "sample_answer": sample_ans,
        "ideal_answer": sample_ans,
        "worked_solution": worked_sol,
        "canonical_solution": worked_sol,
        "explanation": worked_sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "pathogens_and_infectious_diseases",
        "question_family_id": "pathogens_and_infectious_diseases",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Microorganisms > Harmful microorganisms and diseases",
        "hints": {
            "tier_1": "Recall whether the disease is caused by a virus, bacterium, or protist.",
            "tier_2": "Think about whether it spreads through water, air droplets, or an insect vector.",
            "tier_3": f"{d['disease']} is caused by {d['agent']} and spreads via {d['transmission']}."
        },
        "misconception_tags": ["mosquitoes_cause_malaria_directly_misconception"]
    }

def _build_beneficial_uses(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    uses = [
        {
            "organism": "Yeast (Saccharomyces cerevisiae, a unicellular fungus)",
            "process": "Anaerobic alcoholic fermentation: converts sugars into ethanol and carbon dioxide gas",
            "application": "Bread baking (CO2 gas makes dough rise) and brewing",
            "output": "Carbon dioxide and ethanol"
        },
        {
            "organism": "Lactobacillus acidophilus (Lactic acid bacteria)",
            "process": "Lactic acid fermentation of lactose milk sugar",
            "application": "Yoghurt, maas (amasi), and cheese production (preserves milk proteins)",
            "output": "Lactic acid"
        },
        {
            "organism": "Penicillium mould (a filamentous fungus)",
            "process": "Secretes chemical compounds that destroy bacterial cell wall synthesis",
            "application": "Production of penicillin, the life-saving antibiotic medication",
            "output": "Penicillin antibiotic"
        }
    ]
    u = rng.choice(uses)
    other_u = [x for x in uses if x["organism"] != u["organism"]]

    correct_opt = f"Process: {u['process']}; Product/Application: {u['application']}."
    distractor_1 = f"Process: {other_u[0]['process']}; Product/Application: {other_u[0]['application']}."
    distractor_2 = f"Process: {other_u[1]['process']}; Product/Application: {other_u[1]['application']}."
    distractor_3 = f"Process: Aerobic cellular respiration; Product/Application: Synthetic plastic polymers."

    opts = [correct_opt, distractor_1, distractor_2, distractor_3]
    rng.shuffle(opts)
    c_idx = opts.index(correct_opt)
    c_letter = chr(65 + c_idx)
    sample_ans = f"{c_letter}. {correct_opt}"
    worked_sol = (
        f"**{sample_ans}** [2 marks]\n\n"
        f"Explanation: **{u['organism']}** carries out {u['process']}. It is utilized commercially in {u['application']}, producing {u['output']}."
    )

    prompt = (
        f"Micro-organisms are not solely harmful pathogens; they are essential for biotechnology, medicine, and food production.\n\n"
        f"Which of the following correctly pairs the micro-organism **{u['organism']}** with its biological/chemical process and manufactured product?"
    )

    return {
        "id": _make_id("ns8_beneficial", seed, idx),
        "question_type": "mcq",
        "prompt": prompt,
        "options": opts,
        "correct_index": str(c_idx),
        "sample_answer": sample_ans,
        "ideal_answer": sample_ans,
        "worked_solution": worked_sol,
        "canonical_solution": worked_sol,
        "explanation": worked_sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "beneficial_uses_of_microorganisms",
        "question_family_id": "beneficial_uses_of_microorganisms",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Microorganisms > Useful microorganisms",
        "hints": {
            "tier_1": "Recall the traditional foods and medicines made using fermentation.",
            "tier_2": "Yeast makes bread rise and alcohol; lactobacillus turns milk into maas/yoghurt; penicillium produces penicillin.",
            "tier_3": f"Process involves {u['process']}."
        },
        "misconception_tags": ["all_microorganisms_are_germs_misconception"]
    }

def _build_preventing_spread(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    methods = [
        {
            "method": "Pasteurisation",
            "description": "Heating milk or fruit juice to approximately 72°C for 15 seconds, followed by rapid cooling",
            "mechanism": "Destroys pathogenic bacteria without altering the nutritional quality or curdling the liquid"
        },
        {
            "method": "Autoclaving / Steam Sterilisation",
            "description": "Exposing surgical and laboratory instruments to high-pressure saturated steam at 121°C for 15-20 minutes",
            "mechanism": "Kills all living micro-organisms including highly resistant bacterial endospores"
        },
        {
            "method": "Refrigeration and Freezing",
            "description": "Storing perishable food items at low temperatures (below 4°C or -18°C)",
            "mechanism": "Slows down or temporarily halts the metabolic enzymes and reproduction of micro-organisms without killing them"
        }
    ]
    m = rng.choice(methods)
    prompt = (
        f"Various techniques are employed in homes, hospitals, and food factories to control the proliferation of micro-organisms.\n\n"
        f"What is the operational definition and purpose of **{m['method']}**?"
    )
    correct_opt = f"{m['description']} so that it {m['mechanism']}"
    distractors = [
        "Adding concentrated antibiotics to public drinking water reservoirs to immunize the entire population",
        "Storing biological samples at boiling temperatures above 100°C for multiple months",
        "Washing surfaces exclusively with pure cold water without soap or sanitizers"
    ]
    options = [correct_opt] + distractors
    rng.shuffle(options)
    c_idx = options.index(correct_opt)
    c_letter = chr(65 + c_idx)
    sample_ans = f"{c_letter}. {correct_opt}"
    sol = (
        f"**{sample_ans}** [2 marks]\n\n"
        f"Step 1: Define {m['method']}:\n"
        f"{m['description']}.\n\n"
        f"Step 2: Mechanism of action:\n"
        f"{m['mechanism']}."
    )
    return {
        "id": _make_id("ns8_steril", seed, idx),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": correct_opt,
        "sample_answer": sample_ans,
        "ideal_answer": sample_ans,
        "worked_solution": sol,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "preventing_spread_and_sterilisation",
        "question_family_id": "preventing_spread_and_sterilisation",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Microorganisms > Preservation and sterilization methods",
        "hints": {
            "tier_1": "Think about how temperature controls bacterial growth in food or medical tools.",
            "tier_2": "Pasteurisation heats milk quickly; refrigeration slows enzymes; autoclaving kills all spores.",
            "tier_3": f"The answer is {correct_opt}."
        },
        "misconception_tags": ["freezing_kills_all_bacteria_misconception"]
    }


def _build_antibiotics_vs_antivirals(rng: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    patients = [
        "A patient visits a community medical clinic suffering from acute seasonal influenza",
        "A high school learner with severe rhinovirus symptoms (the common cold) visits a local doctor",
        "An adult presenting with a viral upper respiratory tract infection visits a clinic"
    ]
    chosen_pt = rng.choice(patients)
    prompt = (
        f"{chosen_pt} and demands that the healthcare practitioner prescribe penicillin or amoxicillin (antibiotics).\n\n"
        f"Which of the following scientifically explains why the medical doctor refuses to prescribe antibiotics for this viral infection?"
    )

    correct_opt = "Antibiotics target bacterial cell structures (such as peptidoglycan cell walls) which acellular viruses lack, and unnecessary use promotes drug-resistant bacterial strains."
    distractor_1 = "Antibiotics are only effective against large parasitic worms, whereas viruses require anti-fungal ointments."
    distractor_2 = "Antibiotics accelerate the viral replication rate inside human host cells, making viral infections twice as severe."
    distractor_3 = "Antibiotics destroy human white blood cells, completely suppressing antibody production in the bloodstream."

    opts = [correct_opt, distractor_1, distractor_2, distractor_3]
    rng.shuffle(opts)
    c_idx = opts.index(correct_opt)
    c_letter = chr(65 + c_idx)
    sample_ans = f"{c_letter}. {correct_opt}"
    worked_sol = (
        f"**{sample_ans}** [2 marks]\n\n"
        f"Explanation: Antibiotics specifically inhibit bacterial metabolic pathways and bacterial cell wall synthesis. "
        f"Viruses are non-cellular entities that replicate entirely inside host cells and lack bacterial structures, rendering antibiotics completely ineffective. "
        f"Inappropriate antibiotic use creates selective pressure that promotes antibiotic-resistant superbugs."
    )

    return {
        "id": _make_id("ns8_antibi", seed, idx),
        "question_type": "mcq",
        "prompt": prompt,
        "options": opts,
        "correct_index": str(c_idx),
        "sample_answer": sample_ans,
        "ideal_answer": sample_ans,
        "worked_solution": worked_sol,
        "canonical_solution": worked_sol,
        "explanation": worked_sol,
        "marks": 2,
        "total_marks": 2,
        "subskill": "antibiotics_vs_antivirals_efficacy",
        "question_family_id": "antibiotics_vs_antivirals_efficacy",
        "curriculum_reference": "Natural Sciences Gr8 Term 2 > Microorganisms > Antibiotics and immunity",
        "hints": {
            "tier_1": "Antibiotics kill bacteria, not viruses.",
            "tier_2": "Viruses do not have cell walls or bacterial metabolism to disrupt.",
            "tier_3": "Taking antibiotics for viral colds causes antibiotic resistance; vaccines prevent viral infections."
        },
        "misconception_tags": ["antibiotics_cure_flu_misconception"]
    }

def generate(archetype: Optional[str] = None, seed: Optional[int] = None, count: int = 1, **kwargs) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    results = []
    for idx in range(count):
        target = archetype or rng.choice(SUBSKILLS)
        if target == "microorganism_types_and_characteristics":
            item = _build_microorganism_types(rng, seed, idx)
        elif target == "pathogens_and_infectious_diseases":
            item = _build_pathogens_diseases(rng, seed, idx)
        elif target == "beneficial_uses_of_microorganisms":
            item = _build_beneficial_uses(rng, seed, idx)
        elif target == "preventing_spread_and_sterilisation":
            item = _build_preventing_spread(rng, seed, idx)
        elif target == "antibiotics_vs_antivirals_efficacy":
            item = _build_antibiotics_vs_antivirals(rng, seed, idx)
        else:
            item = _build_microorganism_types(rng, seed, idx)
        results.append(item)
    return results


def get_archetypes() -> List[str]:
    return list(SUBSKILLS)
