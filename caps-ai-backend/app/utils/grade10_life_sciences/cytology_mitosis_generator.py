"""Grade 10 Life Sciences — Cells (Cytology) and Cell Division (Mitosis) Generator.
Strictly grounded in curriculum_docs_auto/LifeSciences_Gr10/Term 1/:
  - 01. Cells the basic units of life.md
  - 02. Cell division.md
Complies with Rule 20 (Term 1 metadata), Rule 21 (Deconstructibility), Rule 22 (Misconception taxonomy).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


ORGANELLES_DATA = [
    {
        "name": "Mitochondrion",
        "structure": "Double-membrane organelle with folded inner membrane (cristae) and fluid-filled matrix.",
        "function": "Site of cellular respiration; generates ATP (energy) for cellular activities.",
        "plant_animal": "Found in both plant and animal cells.",
    },
    {
        "name": "Chloroplast",
        "structure": "Double-membrane organelle containing disc-shaped thylakoids stacked into grana, embedded in stroma.",
        "function": "Site of photosynthesis; contains green chlorophyll pigment to trap radiant light energy.",
        "plant_animal": "Found in photosynthetic plant cells; absent in animal cells.",
    },
    {
        "name": "Ribosome",
        "structure": "Small, non-membrane bound granules composed of ribosomal RNA and protein.",
        "function": "Site of protein synthesis (translation of mRNA into polypeptide chains).",
        "plant_animal": "Found in both plant and animal cells, free in cytoplasm or on Rough ER.",
    },
    {
        "name": "Cell Wall",
        "structure": "Rigid outer layer composed primarily of non-living cellulose fibers with plasmodesmata.",
        "function": "Provides structural support, mechanical strength, and protection against osmotic lysis.",
        "plant_animal": "Found in plant cells, bacteria, and fungi; strictly absent in animal cells.",
    },
    {
        "name": "Cell Membrane",
        "structure": "Fluid mosaic phospholipid bilayer embedded with transport proteins, cholesterol, and carbohydrates.",
        "function": "Selectively permeable barrier controlling the movement of substances via diffusion, osmosis, and active transport.",
        "plant_animal": "Found in all plant and animal cells.",
    },
    {
        "name": "Nucleus",
        "structure": "Spherical organelle enclosed by a porous double nuclear membrane, containing nucleoplasm, nucleolus, and chromatin.",
        "function": "Controls all cellular activities and houses genetic material (DNA).",
        "plant_animal": "Found in all eukaryotic plant and animal cells.",
    },
    {
        "name": "Vacuole (Large Central)",
        "structure": "Large, fluid-filled organelle bounded by a single selectively permeable membrane called the tonoplast.",
        "function": "Stores water, dissolved mineral ions, and organic wastes; maintains turgor pressure for cell rigidity.",
        "plant_animal": "Prominent, permanent large central vacuole in plant cells; small, temporary vacuoles in animal cells.",
    },
]

MICROSCOPE_DATA = [
    {
        "type": "Transmission Electron Microscope (TEM)",
        "features": "Passes beams of electrons through ultra-thin sections cut with an ultramicrotome.",
        "advantage": "High resolving power allowing ultra-high magnification (up to 50 000 000x) to observe detailed internal ultrastructure of organelles like cristae and thylakoids.",
    },
    {
        "type": "Scanning Electron Microscope (SEM)",
        "features": "Scans the specimen surface with an electron beam, collecting knocked-off secondary electrons.",
        "advantage": "Provides realistic 3-dimensional images of external surfaces with high depth of field.",
    },
    {
        "type": "Compound Light Microscope",
        "features": "Uses visible light and glass lenses to magnify specimens up to 1 000x.",
        "advantage": "Allows observation of live, intact cells and whole microscopic organisms with natural colour.",
    },
]

MITOSIS_PHASES_DATA = [
    {
        "phase": "Prophase",
        "events": "Chromatin shortens and condenses into distinct chromosomes. Each chromosome consists of two sister chromatids joined at a centromere. The nuclear membrane breaks down, nucleolus disappears, and spindle fibers form.",
        "distinguishing_feature": "Visible condensed chromosomes and disintegrating nuclear membrane.",
    },
    {
        "phase": "Metaphase",
        "events": "Chromosomes line up in a single file along the equatorial plane (metaphase plate) of the cell. Spindle fibers attach to the centromere of each chromosome.",
        "distinguishing_feature": "Chromosomes aligned along the cell equator in single file.",
    },
    {
        "phase": "Anaphase",
        "events": "The centromere of each chromosome splits. Spindle fibers contract, pulling sister chromatids (now individual daughter chromosomes) apart toward opposite poles of the cell.",
        "distinguishing_feature": "V-shaped chromatids moving apart toward opposite cell poles.",
    },
    {
        "phase": "Telophase",
        "events": "Daughter chromosomes reach opposite poles and uncoil back into fine chromatin. Nuclear envelope and nucleoli reform around each set of chromosomes. Spindle fibers disintegrate.",
        "distinguishing_feature": "Two distinct nuclei forming in a single cell with decondensing chromatin.",
    },
    {
        "phase": "Cytokinesis",
        "events": "Division of the cytoplasm. In animal cells, an invagination/cleavage furrow constricts inward. In plant cells, a cell plate forms along the equator from Golgi vesicles.",
        "distinguishing_feature": "Physical separation into two genetically identical daughter cells.",
    },
]


# --------------------------------------------------------------------------- #
# Grade 10 Life Sciences: Cytology (Cells the Basic Units of Life)
# --------------------------------------------------------------------------- #
def _build_organelle_drill(r: random.Random) -> Dict[str, Any]:
    organelle = r.choice(ORGANELLES_DATA)
    modality = "bio_diagram"
    diagram_spec = {
        "diagram_role": "identify" if locals().get("target_pin") else "context",
        "image_type": "plant_cell" if "plant" in organelle.get("plant_animal", "").lower() else "animal_cell",
        "labels": [
            {"id": "pin_1", "name": organelle["name"], "x": 50, "y": 50, "description": organelle["function"]}
        ]
    }
    other_organelles = [o for o in ORGANELLES_DATA if o["name"] != organelle["name"]]
    distractors = r.sample(other_organelles, 3)

    qtype = r.choice(["function_to_name", "structure_to_function", "plant_vs_animal"])

    if qtype == "function_to_name":
        prompt = (
            f"Identify the organelle described by the following biological function:\n\n"
            f"> \"{organelle['function']}\"\n\n"
            f"State the name of the organelle and whether it is present in plant cells, animal cells, or both."
        )
        exp_ans = f"{organelle['name']} ({organelle['plant_animal']})"
        sol = (
            f"**Organelle:** {organelle['name']}\n\n"
            f"**Function:** {organelle['function']}\n\n"
            f"**Distribution:** {organelle['plant_animal']}"
        )
        mp = [
            {"id": "mp1", "desc": f"Accurate organelle identification: {organelle['name']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Correct plant/animal distribution: {organelle['plant_animal']}", "marks": 1, "editable": True},
        ]
        tier1 = f"Consider the physiological role: {organelle['function'][:60]}..."
        tier2 = f"This structure has the following adaptation: {organelle['structure']}"
        tier3 = f"The organelle is the {organelle['name']}."

    elif qtype == "structure_to_function":
        prompt = (
            f"Consider the **{organelle['name']}**.\n\n"
            f"1. Describe its structural adaptation.\n"
            f"2. Explain its primary function in the cell."
        )
        exp_ans = f"Structure: {organelle['structure']} Function: {organelle['function']}"
        sol = (
            f"**1. Structural Adaptation:** {organelle['structure']}\n\n"
            f"**2. Primary Function:** {organelle['function']}"
        )
        mp = [
            {"id": "mp1", "desc": f"Structural adaptation: {organelle['structure'][:80]}", "marks": 2, "editable": True},
            {"id": "mp2", "desc": f"Primary function: {organelle['function'][:80]}", "marks": 2, "editable": True},
        ]
        tier1 = f"Recall how the {organelle['name']} is built to perform its metabolic role."
        tier2 = f"Structure: {organelle['structure'][:60]}..."
        tier3 = f"Full description: {organelle['structure']} Function: {organelle['function']}"

    else:
        plant_only = [o for o in ORGANELLES_DATA if "absent in animal" in o["plant_animal"].lower() or o["name"] in ("Chloroplast", "Cell Wall", "Vacuole (Large Central)")]
        p_org = r.choice(plant_only)
        prompt = (
            f"Compare plant and animal cells with respect to the **{p_org['name']}**.\n\n"
            f"1. State whether this organelle is found in plant cells, animal cells, or both.\n"
            f"2. Explain why this structure is essential for plant survival but not required in animal cells."
        )
        exp_ans = f"Found in plant cells only. {p_org['function']}"
        sol = (
            f"**1. Occurrence:** Present in plant cells only (absent in animal cells).\n\n"
            f"**2. Biological Significance:** {p_org['function']} Animal cells have alternative structural supports (skeletons) or obtain pre-formed organic nutrients heterotrophically."
        )
        mp = [
            {"id": "mp1", "desc": "Correct statement: present in plant cells only", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Biological significance explanation: {p_org['function'][:80]}", "marks": 2, "editable": True},
        ]
        tier1 = f"Does an animal cell possess a {p_org['name']}?"
        tier2 = f"Recall that {p_org['name']} is unique to plant cells because of {p_org['function'][:50]}."
        tier3 = f"Found in plant cells only. {p_org['function']}"

    marks = sum(p["marks"] for p in mp)
    return {
        "id": f"ls10_cell_{r.randint(100000, 999999)}",
        "question_id": f"ls10_cell_{r.randint(100000, 999999)}",
        "topic": "grade10_life_sciences_cytology",
        "subskill": "organelle_structure_function",
        "learning_objective_id": "ls10_cells_organelles",
        "prompt": prompt,
        "prompt_latex": prompt,
        "expected_answer": exp_ans,
        "worked_solution": sol,
        "marks": marks,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "compound",
        "modality": modality,
        "diagram_spec": diagram_spec,
        "solution_type": "text",
        "marking_schema": {"total_marks": marks, "marking_points": mp, "deductions": []},
        "hints": {"tier_1": tier1, "tier_2": tier2, "tier_3": tier3},
        "misconception_tags": ["organelle_function_confusion", "plant_vs_animal_cell_confusion"],
    }


def _build_microscope_drill(r: random.Random) -> Dict[str, Any]:
    micro = r.choice(MICROSCOPE_DATA)
    prompt = (
        f"A Life Sciences researcher needs to examine the internal ultrastructure of a mitochondrion, specifically "
        f"the detailed folds of the cristae.\n\n"
        f"1. Identify the most suitable type of microscope ({', '.join(m['type'] for m in MICROSCOPE_DATA)}).\n"
        f"2. Justify your choice based on magnification, resolving power, and how the specimen is prepared."
    )
    exp_ans = f"Transmission Electron Microscope (TEM). {micro['advantage']}"
    sol = (
        f"**1. Selected Microscope:** Transmission Electron Microscope (TEM)\n\n"
        f"**2. Justification:** The TEM provides resolving power capable of ultra-high magnification (up to 50 000 000x), "
        f"passing an electron beam through ultra-thin sections to visualize internal organellar ultrastructure (cristae, thylakoids). "
        f"A light microscope (1 000x) lacks sufficient resolving power, while SEM only displays 3D surface topography."
    )
    mp = [
        {"id": "mp1", "desc": "Identification of Transmission Electron Microscope (TEM)", "marks": 1, "editable": True},
        {"id": "mp2", "desc": "High resolving power / magnification justification", "marks": 1, "editable": True},
        {"id": "mp3", "desc": "Ability to view internal ultrastructure / thin sections", "marks": 1, "editable": True},
    ]
    return {
        "id": f"ls10_micro_{r.randint(100000, 999999)}",
        "question_id": f"ls10_micro_{r.randint(100000, 999999)}",
        "topic": "grade10_life_sciences_cytology",
        "subskill": "microscopy_resolution",
        "learning_objective_id": "ls10_microscopy_techniques",
        "prompt": prompt,
        "prompt_latex": prompt,
        "expected_answer": exp_ans,
        "worked_solution": sol,
        "marks": 3,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "mode": "elementary_microscope",
        "modality": "semantic",
        "solution_type": "text",
        "marking_schema": {"total_marks": 3, "marking_points": mp, "deductions": []},
        "hints": {
            "tier_1": "Consider whether viewing internal folds requires light, surface scanning electrons, or transmission electrons.",
            "tier_2": "A TEM transmits electron beams through ultra-thin sections, yielding millions of times magnification.",
            "tier_3": "Correct answer is the Transmission Electron Microscope (TEM) due to its high resolution of internal organelle membranes.",
        },
        "misconception_tags": ["sem_vs_tem_confusion", "magnification_vs_resolution_confusion"],
    }


def generate_cytology(
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generates questions for Grade 10 Life Sciences: Cells the Basic Units of Life."""
    r = _rng(seed)
    questions = []
    for _ in range(max(1, count)):
        eff_mode = (mode or "").lower()
        eff_sub = (subskill or "").lower()
        if "micro" in eff_sub or eff_mode == "elementary_microscope":
            q = _build_microscope_drill(r)
        else:
            q = _build_organelle_drill(r)
        questions.append(q)
    return questions


# --------------------------------------------------------------------------- #
# Grade 10 Life Sciences: Cell Division (Mitosis)
# --------------------------------------------------------------------------- #
def _build_mitosis_drill(r: random.Random) -> Dict[str, Any]:
    phase_data = r.choice(MITOSIS_PHASES_DATA)
    qtype = r.choice(["identify_phase", "biological_significance", "cancer_connection"])
    modality = "semantic"
    diagram_spec = None

    if qtype == "identify_phase":
        prompt = (
            f"A learner examines dividing cells under a microscope and observes the following key cellular event:\n\n"
            f"> \"{phase_data['events']}\"\n\n"
            f"1. Identify the stage of mitosis / the cell cycle being described.\n"
            f"2. State what happens immediately in the subsequent stage."
        )
        idx = MITOSIS_PHASES_DATA.index(phase_data)
        next_phase = MITOSIS_PHASES_DATA[(idx + 1) % len(MITOSIS_PHASES_DATA)]
        exp_ans = f"Stage: {phase_data['phase']}. Subsequent stage ({next_phase['phase']}): {next_phase['distinguishing_feature']}"
        sol = (
            f"**1. Stage Identified:** {phase_data['phase']}\n\n"
            f"**2. Subsequent Stage:** {next_phase['phase']}\n"
            f"*{next_phase['events']}*"
        )
        mp = [
            {"id": "mp1", "desc": f"Identification of stage: {phase_data['phase']}", "marks": 1, "editable": True},
            {"id": "mp2", "desc": f"Identification of subsequent stage: {next_phase['phase']}", "marks": 1, "editable": True},
            {"id": "mp3", "desc": f"Accurate description of subsequent events: {next_phase['distinguishing_feature']}", "marks": 1, "editable": True},
        ]
        tier1 = f"Look at the arrangement of chromosomes: {phase_data['distinguishing_feature']}."
        tier2 = f"This corresponds to {phase_data['phase']} of mitosis."
        tier3 = f"Stage is {phase_data['phase']}, followed by {next_phase['phase']}."
        modality = "bio_diagram"
        diagram_spec = {
        "diagram_role": "identify" if locals().get("target_pin") else "context",
            "image_type": "mitosis_stages",
            "labels": [
                {"id": "A", "name": "Stage A: Prophase", "x": 25, "y": 18},
                {"id": "B", "name": "Stage B: Metaphase", "x": 75, "y": 18},
                {"id": "C", "name": "Stage C: Anaphase", "x": 25, "y": 64},
                {"id": "D", "name": "Stage D: Telophase & Cytokinesis", "x": 75, "y": 64},
                {"id": "E", "name": "Spindle fibers", "x": 62, "y": 35},
                {"id": "F", "name": "Centromere / Centrioles", "x": 80, "y": 35},
            ]
        }

    elif qtype == "biological_significance":
        prompt = (
            f"Explain the biological significance of mitosis in living organisms, discussing:\n\n"
            f"1. Growth in multicellular organisms\n"
            f"2. Repair of damaged tissues / replacement of worn-out cells\n"
            f"3. Preservation of genetic fidelity across generations of somatic cells"
        )
        exp_ans = "Growth (increases cell count), repair/replacement (heals wounds), genetic consistency (maintains identical 2n chromosome number)."
        sol = (
            f"**1. Growth:** Mitosis enables a single-celled zygote to develop into a complex multicellular organism by increasing the number of cells.\n\n"
            f"**2. Repair and Replacement:** Mitosis allows multicellular organisms to regenerate damaged tissues and replace dead or worn-out cells (e.g. skin cells, red blood cells).\n\n"
            f"**3. Genetic Fidelity:** Mitosis ensures each daughter cell receives an exact, identical copy of the parent cell's DNA (maintains constant diploid chromosome number $2n$)."
        )
        mp = [
            {"id": "mp1", "desc": "Role in multicellular growth / development from zygote", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Role in tissue repair and replacement of damaged cells", "marks": 1, "editable": True},
            {"id": "mp3", "desc": "Maintenance of identical diploid genetic information (2n)", "marks": 1, "editable": True},
        ]
        tier1 = "Consider what happens to an organism's cell count when growing from an embryo, and how a cut heals."
        tier2 = "Mitosis produces genetically identical daughter cells (2n) for growth and wound healing."
        tier3 = "Three core reasons: growth by cell multiplication, repair/regeneration of damaged tissues, and identical chromosome inheritance."

    else:
        prompt = (
            f"Cell division is normally strictly regulated during the cell cycle.\n\n"
            f"1. Define **cancer** in terms of the cell cycle and mitosis.\n"
            f"2. Distinguish between a **benign tumour** and a **malignant tumour**.\n"
            f"3. Name two common carcinogens and two conventional cancer medical treatments."
        )
        exp_ans = "Uncontrolled mitosis. Benign (non-invasive) vs malignant (metastatic/invasive). Carcinogens: radiation, tobacco. Treatments: chemotherapy, radiation, surgery."
        sol = (
            f"**1. Definition:** Cancer is a disease characterized by uncontrolled, repetitive mitotic cell division due to the failure of cell cycle checkpoints.\n\n"
            f"**2. Tumour Distinction:**\n"
            f"- *Benign tumour:* A non-cancerous, localized mass of cells that does not invade neighboring tissues or spread (metastasis).\n"
            f"- *Malignant tumour:* A cancerous growth capable of invading surrounding healthy tissues and spreading through blood/lymph to secondary sites (metastasis).\n\n"
            f"**3. Causes and Treatments:**\n"
            f"- *Carcinogens:* Cigarette smoke (tobacco), ultraviolet (UV) radiation, ionizing radiation, certain viruses (e.g. HPV).\n"
            f"- *Treatments:* Surgery (resection), radiotherapy (radiation therapy), chemotherapy."
        )
        mp = [
            {"id": "mp1", "desc": "Definition of cancer as uncontrolled mitotic cell division", "marks": 1, "editable": True},
            {"id": "mp2", "desc": "Accurate distinction between benign (localized) and malignant (metastatic)", "marks": 2, "editable": True},
            {"id": "mp3", "desc": "Naming two valid carcinogens and two treatments", "marks": 2, "editable": True},
        ]
        tier1 = "How does cancer relate to the speed and regulation of mitosis?"
        tier2 = "Cancer is uncontrolled mitosis forming tumours. Malignant tumours spread (metastasize) unlike benign ones."
        tier3 = "Uncontrolled mitosis; benign remains localized while malignant spreads; carcinogens include UV light and smoke; treatments include chemotherapy and surgery."

    marks = sum(p["marks"] for p in mp)
    return {
        "id": f"ls10_mitosis_{r.randint(100000, 999999)}",
        "question_id": f"ls10_mitosis_{r.randint(100000, 999999)}",
        "topic": "grade10_life_sciences_mitosis",
        "subskill": "mitosis_cell_cycle",
        "learning_objective_id": "ls10_mitosis_cell_division",
        "prompt": prompt,
        "prompt_latex": prompt,
        "expected_answer": exp_ans,
        "worked_solution": sol,
        "marks": marks,
        "term": 1,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 6,
        "mode": "compound",
        "modality": modality,
        "diagram_spec": diagram_spec,
        "solution_type": "text",
        "marking_schema": {"total_marks": marks, "marking_points": mp, "deductions": []},
        "hints": {"tier_1": tier1, "tier_2": tier2, "tier_3": tier3},
        "misconception_tags": ["mitosis_vs_meiosis_confusion", "anaphase_vs_telophase_confusion", "benign_vs_malignant_confusion"],
    }


def generate_mitosis(
    subskill: Optional[str] = None,
    difficulty: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    mode: Optional[str] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generates questions for Grade 10 Life Sciences: Cell Division (Mitosis)."""
    r = _rng(seed)
    questions = []
    for _ in range(max(1, count)):
        questions.append(_build_mitosis_drill(r))
    return questions
