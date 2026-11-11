"""Grade 9 Natural Sciences: Term 1 - Cells as the Basic Units of Life (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 1/01. Cells as the basic units of life.md.
Focus: Curated Campbell cytology plates (Plant & Animal cell ultrastructure), microscopy, cell theory, and cellular boundaries.
"""
from __future__ import annotations

import json
import os
import random
from typing import Any, Dict, List, Optional

ANCHORS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
    "data",
    "diagram_anchors",
)


def _load_anchors(master_name: str) -> Dict[str, Any]:
    path = os.path.join(ANCHORS_DIR, f"{master_name}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


PLANT_CELL_DATA = _load_anchors("plant_cell")
ANIMAL_CELL_DATA = _load_anchors("animal_cell")


def _make_cell_plate_question(
    rng: random.Random,
    master: str,
    target_key: str,
    subskill_id: str,
) -> Dict[str, Any]:
    anchor_data = PLANT_CELL_DATA if master == "plant_cell" else ANIMAL_CELL_DATA
    anchors = anchor_data["anchors"]
    cell_type = "plant cell" if master == "plant_cell" else "animal cell"
    target = anchors[target_key]

    candidate_keys = [k for k in anchors.keys() if k != target_key and k != "cytoplasm"]
    rng.shuffle(candidate_keys)
    selected_keys = [target_key] + candidate_keys[:3]
    rng.shuffle(selected_keys)

    pin_letters = ["A", "B", "C", "D"]
    pins_payload = []
    target_pin = "A"

    for idx, k in enumerate(selected_keys):
        letter = pin_letters[idx]
        ref = f"{rng.randint(100000, 999999)}_{k}"
        pins_payload.append({
            "pin": letter,
            "anchor": anchors[k]["anchor"],
            "default_box": anchors[k]["default_box"],
            "side": anchors[k]["side"],
            "ref": ref,
        })
        if k == target_key:
            target_pin = letter

    diag_payload = {
        "diagram_role": "identify",
        "image_type": master,
        "master": master,
        "view": anchor_data.get("view", "eukaryotic_ultrastructure_cross_section"),
        "viewBox": anchor_data.get("viewBox", "0 0 600 480"),
        "grade_mask": "g9",
        "pins": pins_payload,
        "target_pin": target_pin,
        "target_key": target_key,
    }

    prompt = (
        f"Study the anatomical cross-section diagram of the {cell_type} (Campbell botanical/cytological plate).\n\n"
        f"Which organelle or cellular structure is indicated by **Pin {target_pin}**?"
    )
    correct = target["name"]
    distractors = [anchors[k]["name"] for k in selected_keys if k != target_key]
    options = [correct] + distractors
    rng.shuffle(options)

    sol = (
        f"**Step 1:** Locate Pin {target_pin} on the {cell_type} anatomical plate.\n"
        f"**Step 2:** Review organelle structural position and characteristics:\n"
        f"- {target['name']}: {target['description']}\n\n"
        f"**Step 3:** The structure indicated by Pin {target_pin} is **{correct}**."
    )

    return {
        "id": f"ns9_cell_{subskill_id[:2]}_{rng.randint(100000, 999999)}",
        "subskill": subskill_id,
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": diag_payload,
        "hints": {
            "tier_1": f"Observe where Pin {target_pin} points in the {cell_type}.",
            "tier_2": f"This structure is characterized by: {target['description'][:60]}...",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": [f"organelle_identification_{target_key}_misconception"],
    }


# 01. Plant cell wall cellulose identification (Campbell Plate)
def arch_01_plant_cell_wall_cellulose_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_cell_plate_question(rng, "plant_cell", "cell_wall", "01_plant_cell_wall_cellulose_identification")


# 02. Plant cell membrane permeability identification (Campbell Plate)
def arch_02_plant_cell_membrane_permeability_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_cell_plate_question(rng, "plant_cell", "plasma_membrane", "02_plant_cell_membrane_permeability_identification")


# 03. Plant cell chloroplast photosynthesis identification (Campbell Plate)
def arch_03_plant_cell_chloroplast_photosynthesis_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_cell_plate_question(rng, "plant_cell", "chloroplast", "03_plant_cell_chloroplast_photosynthesis_identification")


# 04. Plant cell large central vacuole identification (Campbell Plate)
def arch_04_plant_cell_large_central_vacuole_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_cell_plate_question(rng, "plant_cell", "large_central_vacuole", "04_plant_cell_large_central_vacuole_identification")


# 05. Plant cell nucleus genetic control identification (Campbell Plate)
def arch_05_plant_cell_nucleus_genetic_control_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_cell_plate_question(rng, "plant_cell", "nucleus", "05_plant_cell_nucleus_genetic_control_identification")


# 06. Plant cell mitochondrion cellular respiration identification (Campbell Plate)
def arch_06_plant_cell_mitochondrion_cellular_respiration_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_cell_plate_question(rng, "plant_cell", "mitochondrion", "06_plant_cell_mitochondrion_cellular_respiration_identification")


# 07. Animal cell plasma membrane boundary identification (Campbell Plate)
def arch_07_animal_cell_plasma_membrane_boundary_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_cell_plate_question(rng, "animal_cell", "plasma_membrane", "07_animal_cell_plasma_membrane_boundary_identification")


# 08. Animal cell nucleus chromatin identification (Campbell Plate)
def arch_08_animal_cell_nucleus_chromatin_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_cell_plate_question(rng, "animal_cell", "nucleus", "08_animal_cell_nucleus_chromatin_identification")


# 09. Animal cell mitochondria ATP synthesis identification (Campbell Plate)
def arch_09_animal_cell_mitochondria_atp_synthesis_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_cell_plate_question(rng, "animal_cell", "mitochondrion", "09_animal_cell_mitochondria_atp_synthesis_identification")


# 10. Animal cell endoplasmic reticulum transport identification (Campbell Plate)
def arch_10_animal_cell_endoplasmic_reticulum_transport_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_cell_plate_question(rng, "animal_cell", "endoplasmic_reticulum", "10_animal_cell_endoplasmic_reticulum_transport_identification")


# 11. Animal cell golgi apparatus secretion identification (Campbell Plate)
def arch_11_animal_cell_golgi_apparatus_secretion_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_cell_plate_question(rng, "animal_cell", "golgi_apparatus", "11_animal_cell_golgi_apparatus_secretion_identification")


# 12. Animal cell lysosome hydrolytic digestion identification (Campbell Plate)
def arch_12_animal_cell_lysosome_hydrolytic_digestion_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_cell_plate_question(rng, "animal_cell", "lysosome", "12_animal_cell_lysosome_hydrolytic_digestion_identification")


# 13. Cell theory postulates and microscopic nature of life
def arch_13_cell_theory_postulates_and_microscopic_nature_of_life(rng: random.Random) -> Dict[str, Any]:
    tenets = [
        ("All living organisms are composed of one or more cells.", "Cellular composition tenet"),
        ("The cell is the basic structural and functional unit of life.", "Basic unit of life tenet"),
        ("All cells arise from pre-existing cells through cell division.", "Biogenesis tenet (Virchow)"),
    ]
    target_tenet, label = rng.choice(tenets)
    prompt = (
        f"The unified **Cell Theory** forms the foundational paradigm of modern biological science.\n\n"
        f"Which statement represents one of the three core postulates of the classic Cell Theory?"
    )
    correct = target_tenet
    options = [
        correct,
        "Cells spontaneously generate out of non-living dust when exposed to full moonlight.",
        "All organisms are made exclusively of solid metallic alloys and liquid mercury.",
        "Cells only exist inside multi-storey buildings and disappear in open nature.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review the three postulates of the Cell Theory:\n"
        f"1. All living organisms are composed of one or more cells.\n"
        f"2. The cell is the most fundamental structural and functional unit of all life.\n"
        f"3. All cells originate from pre-existing cells via cellular division.\n\n"
        f"**Step 2:** The correct postulate is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_13_{rng.randint(100000, 999999)}",
        "subskill": "13_cell_theory_postulates_and_microscopic_nature_of_life",
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
            "tier_1": "Do cells generate spontaneously from dust, or do they come from pre-existing cells?",
            "tier_2": "The Cell Theory states that all living organisms consist of cells, the basic units of life.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cell_theory_postulates_misconception"],
    }


# 14. Robert Hooke and discovery of cork cells in 1665
def arch_14_robert_hooke_and_discovery_of_cork_cells_in_1665(rng: random.Random) -> Dict[str, Any]:
    years = [1665, 1674, 1838]
    prompt = (
        f"In 1665, English scientist Robert Hooke examined thin slices of tree cork under his primitive compound microscope.\n\n"
        f"What did Robert Hooke observe, and why did he choose the biological term **cell**?"
    )
    correct = (
        "He observed empty, box-like porous compartments formed by dead cellulose plant cell walls, "
        "which reminded him of the small bare rooms ('cellulae') inhabited by monks in a monastery."
    )
    options = [
        correct,
        "He observed living microscopic sharks swimming inside drops of rainwater.",
        "He saw glowing radioactive particles that emitted laser beams into his eye.",
        "He observed tiny mechanical clockwork gears ticking inside the tree bark.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze Robert Hooke's historical observation:\n"
        f"- In 1665 (*Micrographia*), Hooke examined dead bark/cork of an oak tree (*Quercus suber*).\n"
        f"- He observed empty honeycomb-like compartments (the dead cellulose cell walls).\n"
        f"- He coined the Latin word *cella* (small room), giving rise to the modern biological term 'cell'.\n\n"
        f"**Step 2:** The accurate scientific history: **{correct}**."
    )
    return {
        "id": f"ns9_cell_14_{rng.randint(100000, 999999)}",
        "subskill": "14_robert_hooke_and_discovery_of_cork_cells_in_1665",
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
            "tier_1": "What did cork cells look like to Robert Hooke in 1665?",
            "tier_2": "The dead cell wall compartments resembled small rooms (monastery cells).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["robert_hooke_cork_cell_discovery_misconception"],
    }


# 15. Prokaryotic vs eukaryotic cellular organization nucleus
def arch_15_prokaryotic_vs_eukaryotic_cellular_organization_nucleus(rng: random.Random) -> Dict[str, Any]:
    organisms = [
        ("Bacterium (*Escherichia coli*)", "Prokaryote", "lacks a membrane-bound nucleus; genetic material floats as a circular nucleoid in cytoplasm"),
        ("Human cheek epithelial cell", "Eukaryote", "possesses a distinct, double-membrane-bound nucleus enclosing linear chromosomes"),
        ("Onion epidermal cell", "Eukaryote", "contains a true membrane-bound nucleus controlling cellular metabolism"),
    ]
    org_name, org_type, org_feature = rng.choice(organisms)
    prompt = (
        f"Living organisms are fundamentally divided into **prokaryotes** and **eukaryotes** based on nuclear organization.\n\n"
        f"How is **{org_name}** classified, and what is its defining nuclear characteristic?"
    )
    correct = f"It is a **{org_type}** because it {org_feature}."
    alt_type = "Eukaryote" if org_type == "Prokaryote" else "Prokaryote"
    alt_feature = (
        "possesses a distinct, double-membrane-bound nucleus" if org_type == "Prokaryote"
        else "lacks a nucleus and has a single naked circular chromosome"
    )
    options = [
        correct,
        f"It is a **{alt_type}** because it {alt_feature}.",
        "It is an acellular virus particle that contains no DNA or RNA.",
        "It is an inorganic crystal with neither cytoplasm nor genetic material.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish prokaryotic vs eukaryotic cells:\n"
        f"- Prokaryotes (e.g. bacteria): lack a true membrane-bound nucleus and membrane-bound organelles.\n"
        f"- Eukaryotes (e.g. plants, animals, fungi, protists): possess a true membrane-bound nucleus containing DNA.\n\n"
        f"**Step 2:** For {org_name}: **{correct}**."
    )
    return {
        "id": f"ns9_cell_15_{rng.randint(100000, 999999)}",
        "subskill": "15_prokaryotic_vs_eukaryotic_cellular_organization_nucleus",
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
            "tier_1": f"Does {org_name} have a true membrane-bound nucleus?",
            "tier_2": "Prokaryotes lack a nuclear membrane; eukaryotes have a distinct nucleus.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["prokaryote_vs_eukaryote_nucleus_misconception"],
    }


# 16. MRS GREN seven vital life processes cellular basis
def arch_16_mrs_gren_seven_vital_life_processes_cellular_basis(rng: random.Random) -> Dict[str, Any]:
    processes = [
        ("Respiration", "cellular respiration in mitochondria releasing energy (ATP) from glucose"),
        ("Excretion", "removal of metabolic cellular waste products such as carbon dioxide and urea"),
        ("Nutrition", "absorbing nutrients across the cell membrane for fuel and biosynthesis"),
        ("Growth", "irreversible increase in dry mass and size through cell division and protein synthesis"),
        ("Movement", "cyclosis (cytoplasmic streaming) and motility via cilia or flagella"),
        ("Sensitivity", "detecting and responding to physical and chemical changes in the external environment"),
        ("Reproduction", "asexual division (mitosis/binary fission) or gamete fusion to create new individuals"),
    ]
    target_p, target_desc = rng.choice(processes)
    prompt = (
        f"The seven fundamental characteristics of life are summarized by the mnemonic **MRS GREN**.\n\n"
        f"Which statement describes how the life process **{target_p}** manifests at the cellular level?"
    )
    correct = f"At the cellular level, {target_p.lower()} involves {target_desc}."
    alt_p = [p for p in processes if p[0] != target_p]
    distractors = [f"At the cellular level, {target_p.lower()} involves {p[1]}." for p in rng.sample(alt_p, 3)]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review MRS GREN life processes at the cellular level:\n"
        f"- Movement, Respiration, Sensitivity, Growth, Reproduction, Excretion, Nutrition.\n"
        f"- For {target_p}: {target_desc}.\n\n"
        f"**Step 2:** The correct match is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_16_{rng.randint(100000, 999999)}",
        "subskill": "16_mrs_gren_seven_vital_life_processes_cellular_basis",
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
            "tier_1": f"Think about what {target_p} means for a single biological cell.",
            "tier_2": f"Match {target_p} to its specific cellular metabolic mechanism.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["mrs_gren_cellular_manifestation_misconception"],
    }


# 17. Light microscope components optical pathway and stage
def arch_17_light_microscope_components_optical_pathway_and_stage(rng: random.Random) -> Dict[str, Any]:
    parts = [
        ("Eyepiece (ocular lens)", "Magnifies the primary image produced by the objective lens, typically by 10x, for direct human viewing"),
        ("Objective lenses (revolving nosepiece)", "Primary optical lenses (e.g. 4x, 10x, 40x) positioned closest to the specimen that provide initial magnification"),
        ("Stage and stage clips", "Flat horizontal platform that holds the glass microscope slide securely in place over the light aperture"),
        ("Iris diaphragm / Condenser", "Regulates the cone angle and intensity of light illuminating the specimen from below"),
        ("Coarse adjustment knob", "Moves the stage rapidly up and down over large distances to bring the specimen into approximate focus under low power"),
        ("Fine adjustment knob", "Moves the stage in tiny, precise increments to sharpen and resolve fine detail under high magnification"),
    ]
    target_part, function = rng.choice(parts)
    prompt = (
        f"A compound light microscope is the essential laboratory instrument for examining cell cytology.\n\n"
        f"What is the mechanical and optical function of the **{target_part}**?"
    )
    correct = function
    alt_parts = [p[1] for p in parts if p[0] != target_part]
    distractors = rng.sample(alt_parts, 3)
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review optical microscope anatomy:\n"
        f"- {target_part}: {function}.\n\n"
        f"**Step 2:** The accurate function is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_17_{rng.randint(100000, 999999)}",
        "subskill": "17_light_microscope_components_optical_pathway_and_stage",
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
            "tier_1": f"Where is the {target_part} located on a light microscope?",
            "tier_2": f"Match the component to its role in holding, illuminating, focusing, or magnifying the specimen.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["microscope_component_function_misconception"],
    }


# 18. Total magnification calculation eyepiece and objective
def arch_18_total_magnification_calculation_eyepiece_and_objective(rng: random.Random) -> Dict[str, Any]:
    eyepieces = [10, 15]
    objectives = [4, 10, 40, 100]
    eye_mag = rng.choice(eyepieces)
    obj_mag = rng.choice(objectives)
    total_mag = eye_mag * obj_mag
    prompt = (
        f"A Grade 9 learner sets up a compound light microscope fitted with a **{eye_mag}x eyepiece lens** "
        f"and selects the **{obj_mag}x objective lens** on the revolving nosepiece.\n\n"
        f"What is the **total magnification** of the specimen observed through this microscope?"
    )
    correct = f"{total_mag}x (calculated as {eye_mag} x {obj_mag})"
    wrong_add = f"{eye_mag + obj_mag}x (calculated as {eye_mag} + {obj_mag})"
    wrong_sub = f"{abs(obj_mag - eye_mag)}x (calculated as {obj_mag} - {eye_mag})"
    wrong_div = f"{round(obj_mag / eye_mag, 1)}x (calculated as {obj_mag} / {eye_mag})"
    options = [correct, wrong_add, wrong_sub, wrong_div]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** State the formula for total microscope magnification:\n"
        f"$$\\text{{Total Magnification}} = \\text{{Magnification of Eyepiece}} \\times \\text{{Magnification of Objective}}$$\n\n"
        f"**Step 2:** Substitute the lens values:\n"
        f"$$\\text{{Total Magnification}} = {eye_mag} \\times {obj_mag} = {total_mag}\\text{{x}}$$\n\n"
        f"**Step 3:** The total magnification is **{correct}**."
    )
    return {
        "id": f"ns9_cell_18_{rng.randint(100000, 999999)}",
        "subskill": "18_total_magnification_calculation_eyepiece_and_objective",
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
            "tier_1": "Do you add the two magnifications together, or multiply them?",
            "tier_2": "Total magnification is the product of eyepiece magnification and objective magnification.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["total_magnification_addition_error_misconception"],
    }


# 19. Microscope focusing technique coarse vs fine adjustment
def arch_19_microscope_focusing_technique_coarse_vs_fine_adjustment(rng: random.Random) -> Dict[str, Any]:
    powers = ["40x high-power objective", "100x oil immersion objective"]
    power = rng.choice(powers)
    prompt = (
        f"When viewing a prepared slide under a **{power}**, why is it strictly forbidden to use "
        f"the **coarse adjustment knob**?\n\n"
        f"What is the correct focusing protocol?"
    )
    correct = (
        "The coarse adjustment knob moves the stage too rapidly over large distances, which can crush "
        "and shatter the delicate glass coverslip and permanently scratch the high-power objective lens; "
        "only the fine adjustment knob should be used for focusing under high power."
    )
    options = [
        correct,
        "The coarse knob turns the glass slide into liquid mercury, causing an explosion in the classroom.",
        "The coarse adjustment knob burns out the electrical wall socket of the school laboratory.",
        "The coarse knob makes all cells disappear into a black hole inside the eyepiece.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze microscope focusing rules:\n"
        f"- Low power (4x, 10x): large working distance between slide and lens -> use coarse knob first, then fine knob.\n"
        f"- High power (40x, 100x): extremely short working distance (fraction of a millimetre).\n"
        f"- Turning the coarse knob can drive the heavy glass slide directly into the lens, breaking the slide, specimen, and lens.\n\n"
        f"**Step 2:** The correct protocol is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_19_{rng.randint(100000, 999999)}",
        "subskill": "19_microscope_focusing_technique_coarse_vs_fine_adjustment",
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
            "tier_1": "What happens if the objective lens collides with the glass slide?",
            "tier_2": "The coarse knob moves the stage too fast and can crush the slide under high power.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["coarse_focus_high_power_damage_misconception"],
    }


# 20. Wet mount slide preparation onion epidermal cells
def arch_20_wet_mount_slide_preparation_onion_epidermal_cells(rng: random.Random) -> Dict[str, Any]:
    errors = [
        ("dropping the coverslip flat from above", "traps numerous circular air bubbles that obscure the cell layer", "lowering the coverslip gently at a 45-degree angle using a mounted needle"),
        ("using a thick fleshy onion scale leaf chunk instead of a single-cell-thick peel", "creates overlapping multi-layered cells that block light transmission", "peeling a transparent single-cell-layer epidermal membrane using forceps"),
    ]
    mistake, problem, remedy = rng.choice(errors)
    prompt = (
        f"During practical wet-mount slide preparation of onion epidermal tissue, a learner makes the error of {mistake}.\n\n"
        f"What visual problem does this cause under the microscope, and what is the proper laboratory remedy?"
    )
    correct = f"Problem: It {problem}.\nRemedy: {remedy}."
    alt = [e for e in errors if e[0] != mistake][0]
    options = [
        correct,
        f"Problem: It {alt[1]}.\nRemedy: {alt[2]}.",
        "Problem: It turns the microscope light bulb into purple smoke.\nRemedy: Pouring hot tea over the objective lens.",
        "Problem: It causes the onion cells to turn into animal muscle cells.\nRemedy: Storing the microscope in the freezer.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review slide preparation principles:\n"
        f"- Light microscopes require thin specimens (single cell layer) so light can transmit through.\n"
        f"- Lowering the coverslip at a 45° angle prevents trapping air bubbles.\n\n"
        f"**Step 2:** For {mistake}: **{correct}**."
    )
    return {
        "id": f"ns9_cell_20_{rng.randint(100000, 999999)}",
        "subskill": "20_wet_mount_slide_preparation_onion_epidermal_cells",
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
            "tier_1": f"Why do air bubbles or thick peels ruin a microscope view?",
            "tier_2": f"Review proper technique: {remedy}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["wet_mount_coverslip_technique_misconception"],
    }


# 21. Biological staining iodine solution vs methylene blue
def arch_21_biological_staining_iodine_solution_vs_methylene_blue(rng: random.Random) -> Dict[str, Any]:
    stains = [
        (
            "Iodine solution (potassium triiodide)",
            "plant cells (such as onion epidermis or potato cells)",
            "stains starch granules blue-black and clearly demarcates cellulose cell walls and nuclei yellowish-brown",
        ),
        (
            "Methylene blue",
            "animal cells (such as human cheek epithelial cells)",
            "binds to negatively charged DNA in the nucleus, staining the nucleus dark blue against a pale blue cytoplasm",
        ),
    ]
    target_stain, specimen, effect = rng.choice(stains)
    prompt = (
        f"Most unstained living cells appear nearly transparent and colourless under a light microscope.\n\n"
        f"What is the primary function of applying **{target_stain}** when preparing a slide of {specimen}?"
    )
    correct = f"It provides optical contrast by selectively binding to specific cellular components: it {effect}."
    alt = [s for s in stains if s[0] != target_stain][0]
    options = [
        correct,
        f"It provides optical contrast by selectively binding to specific cellular components: it {alt[2]}.",
        "It acts as a poison that turns the specimen into solid stone to prevent air from entering.",
        "It converts all water molecules in the cell into red paint that reflects laser beams.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the role of biological stains:\n"
        f"- Cellular organelles have similar refractive indices to water, making them hard to see unstained.\n"
        f"- Stains increase visual contrast by binding specifically to organelles.\n"
        f"- For {target_stain}: {effect}.\n\n"
        f"**Step 2:** The primary function is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_21_{rng.randint(100000, 999999)}",
        "subskill": "21_biological_staining_iodine_solution_vs_methylene_blue",
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
            "tier_1": f"What specific organelle does {target_stain.split()[0]} stain clearly?",
            "tier_2": "Stains provide contrast; iodine stains starch/walls, while methylene blue stains nuclei dark blue.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["biological_stains_iodine_methylene_blue_misconception"],
    }


# 22. Biological magnification formula actual size calculation
def arch_22_biological_magnification_formula_actual_size_calculation(rng: random.Random) -> Dict[str, Any]:
    actual_um = rng.choice([20, 25, 40, 50, 80])
    magnification = rng.choice([200, 400, 500, 1000])
    image_mm = (actual_um * magnification) / 1000.0  # in mm
    prompt = (
        f"In a cytological investigation, a human cell viewed under a calibrated microscope scale "
        f"has an apparent measured size of **{image_mm:.1f} mm** when magnified by **{magnification}x**.\n\n"
        f"Using the biological formula ($M = \\frac{{I}}{{A}}$), what is the **actual size ($A$)** of the cell in micrometres (um)?\n"
        f"*(Note: 1 mm = 1 000 um)*"
    )
    correct = f"{actual_um} um"
    distractors = [
        f"{actual_um * 10} um",
        f"{actual_um / 10:.1f} um",
        f"{round(image_mm * magnification, 1)} um",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** State the magnification formula:\n"
        f"$$\\text{{Magnification}} (M) = \\frac{{\\text{{Image Size}} (I)}}{{\\text{{Actual Size}} (A)}} \\implies A = \\frac{{I}}{{M}}$$\n\n"
        f"**Step 2:** Convert image size from millimetres to micrometres:\n"
        f"$$I = {image_mm:.1f}\\text{{ mm}} \\times 1\\,000 = {image_mm * 1000:.0f}\\text{{ um}}$$\n\n"
        f"**Step 3:** Calculate actual size:\n"
        f"$$A = \\frac{{{image_mm * 1000:.0f}\\text{{ um}}}}{{{magnification}}} = {actual_um}\\text{{ um}}$$\n\n"
        f"**Step 4:** The actual size of the cell is **{correct}**."
    )
    return {
        "id": f"ns9_cell_22_{rng.randint(100000, 999999)}",
        "subskill": "22_biological_magnification_formula_actual_size_calculation",
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
            "tier_1": "Rearrange M = I / A to solve for A: A = I / M.",
            "tier_2": f"Remember to convert {image_mm:.1f} mm into micrometres by multiplying by 1 000 before dividing by {magnification}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["magnification_unit_conversion_micrometre_misconception"],
    }


# 23. Plant vs animal cells major structural differences
def arch_23_plant_vs_animal_cells_major_structural_differences(rng: random.Random) -> Dict[str, Any]:
    structures = [
        ("Cellulose cell wall", "present exclusively in plant cells (providing rigid outer support)", "completely absent in animal cells"),
        ("Photosynthetic chloroplasts", "present in green plant cells (containing chlorophyll for photosynthesis)", "never present in animal cells"),
        ("Large permanent central vacuole", "occupies up to 90% of mature plant cell volume (containing cell sap to maintain turgor pressure)", "absent, or only small, transient, non-permanent vacuoles in animal cells"),
    ]
    struct_name, plant_feat, animal_feat = rng.choice(structures)
    prompt = (
        f"When comparing the cellular ultrastructure of plant cells and animal cells under high magnification, "
        f"distinct differences are evident.\n\n"
        f"Which statement accurately contrasts **{struct_name}** between plant and animal cells?"
    )
    correct = f"Plant cells: {plant_feat};\nAnimal cells: {animal_feat}."
    options = [
        correct,
        f"Plant cells: {animal_feat};\nAnimal cells: {plant_feat}.",
        "Plant cells: Made entirely of molten lead;\nAnimal cells: Formed from crystallized sugar.",
        "Plant cells: Lacks all DNA and proteins;\nAnimal cells: Contains multiple wooden sticks.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare plant and animal cellular features:\n"
        f"- Plant cells have: rigid cellulose cell wall, large central permanent vacuole, and chloroplasts (in photosynthetic tissue).\n"
        f"- Animal cells lack cell walls and chloroplasts, and have only small temporary vacuoles.\n\n"
        f"**Step 2:** For {struct_name}: **{correct}**."
    )
    return {
        "id": f"ns9_cell_23_{rng.randint(100000, 999999)}",
        "subskill": "23_plant_vs_animal_cells_major_structural_differences",
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
            "tier_1": f"Is {struct_name} unique to plant cells, or is it also in animal cells?",
            "tier_2": "Plant cells have cell walls, chloroplasts, and a large permanent vacuole; animal cells do not.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["plant_vs_animal_cell_structures_misconception"],
    }


# 24. Cellulose cell wall mechanical support and turgor
def arch_24_cellulose_cell_wall_mechanical_support_and_turgor(rng: random.Random) -> Dict[str, Any]:
    stresses = [
        ("osmotic water influx in hypotonic pure rainwater", "prevents osmotic bursting (cell lysis) by exerting counter wall-pressure (turgor pressure)"),
        ("gravitational forces acting on non-woody herbaceous stems", "provides rigid mechanical tensile strength via criss-crossing cellulose microfibrils to keep the plant upright"),
    ]
    stress_context, adaptation = rng.choice(stresses)
    prompt = (
        f"Plant cells are encased in a non-living, fully permeable **cell wall** composed of cellulose fibres.\n\n"
        f"How does the plant cell wall protect the cell when exposed to **{stress_context}**?"
    )
    correct = f"It {adaptation}."
    alt = [s[1] for s in stresses if s[0] != stress_context][0]
    options = [
        correct,
        f"It {alt}.",
        "It dissolves immediately into water, allowing the plant cell to swim freely like an animal.",
        "It converts into radioactive carbon, vaporising all incoming water molecules.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the physiological role of the plant cell wall:\n"
        f"- The cell wall is a tough, rigid layer composed of cellulose microfibrils.\n"
        f"- Under osmotic water influx: water enters by osmosis, swelling the vacuole; the cell wall resists stretching, generating **turgor pressure** and preventing the cell from bursting (lysis).\n"
        f"- Mechanical support: gives shape and rigidity to non-woody plant organs.\n\n"
        f"**Step 2:** The correct physiological adaptation: **{correct}**."
    )
    return {
        "id": f"ns9_cell_24_{rng.randint(100000, 999999)}",
        "subskill": "24_cellulose_cell_wall_mechanical_support_and_turgor",
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
            "tier_1": "Why don't plant cells burst when soaked in pure water?",
            "tier_2": "The cellulose cell wall resists internal hydrostatic pressure, creating turgor pressure.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cell_wall_turgor_osmotic_lysis_misconception"],
    }


# 25. Plasma membrane selectively permeable barrier function
def arch_25_plasma_membrane_selectively_permeable_barrier_function(rng: random.Random) -> Dict[str, Any]:
    molecules = [
        ("small non-polar gases like oxygen and carbon dioxide", "diffuse freely across the phospholipid bilayer down their concentration gradient"),
        ("large polar glucose molecules and charged mineral ions", "cannot cross unaided and require specific embedded transport protein channels"),
        ("harmful toxins and cellular metabolic wastes", "are prevented from entering or are actively pumped out of the cytoplasm"),
    ]
    substance, handling = rng.choice(molecules)
    prompt = (
        f"The cell membrane (plasma membrane) is described as **selectively permeable** (semi-permeable).\n\n"
        f"What does selectively permeable mean regarding the movement of **{substance}** across the cell membrane?"
    )
    correct = (
        f"It controls and regulates the passage of substances into and out of the cell: "
        f"{substance} {handling}."
    )
    options = [
        correct,
        "It acts as a solid, impenetrable iron barrier that blocks absolutely all atoms from ever moving.",
        "It is a completely open hole through which all substances inside the cell leak out permanently.",
        "It only allows solid food chunks like bread and meat to pass through without any digestion.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define selective permeability:\n"
        f"- The plasma membrane consists of a phospholipid bilayer with embedded proteins (fluid mosaic model).\n"
        f"- It is **selectively permeable**: it regulates molecular traffic, allowing certain molecules to pass while restricting others.\n"
        f"- For {substance}: {handling}.\n\n"
        f"**Step 2:** The accurate definition and mechanism is: **{correct}**."
    )
    return {
        "id": f"ns9_cell_25_{rng.randint(100000, 999999)}",
        "subskill": "25_plasma_membrane_selectively_permeable_barrier_function",
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
            "tier_1": "What does 'selective' mean when applied to a cell membrane?",
            "tier_2": "The membrane controls which molecules can enter or leave based on size, charge, and permeability.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["selective_permeability_definition_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "01_plant_cell_wall_cellulose_identification": arch_01_plant_cell_wall_cellulose_identification,
    "02_plant_cell_membrane_permeability_identification": arch_02_plant_cell_membrane_permeability_identification,
    "03_plant_cell_chloroplast_photosynthesis_identification": arch_03_plant_cell_chloroplast_photosynthesis_identification,
    "04_plant_cell_large_central_vacuole_identification": arch_04_plant_cell_large_central_vacuole_identification,
    "05_plant_cell_nucleus_genetic_control_identification": arch_05_plant_cell_nucleus_genetic_control_identification,
    "06_plant_cell_mitochondrion_cellular_respiration_identification": arch_06_plant_cell_mitochondrion_cellular_respiration_identification,
    "07_animal_cell_plasma_membrane_boundary_identification": arch_07_animal_cell_plasma_membrane_boundary_identification,
    "08_animal_cell_nucleus_chromatin_identification": arch_08_animal_cell_nucleus_chromatin_identification,
    "09_animal_cell_mitochondria_atp_synthesis_identification": arch_09_animal_cell_mitochondria_atp_synthesis_identification,
    "10_animal_cell_endoplasmic_reticulum_transport_identification": arch_10_animal_cell_endoplasmic_reticulum_transport_identification,
    "11_animal_cell_golgi_apparatus_secretion_identification": arch_11_animal_cell_golgi_apparatus_secretion_identification,
    "12_animal_cell_lysosome_hydrolytic_digestion_identification": arch_12_animal_cell_lysosome_hydrolytic_digestion_identification,
    "13_cell_theory_postulates_and_microscopic_nature_of_life": arch_13_cell_theory_postulates_and_microscopic_nature_of_life,
    "14_robert_hooke_and_discovery_of_cork_cells_in_1665": arch_14_robert_hooke_and_discovery_of_cork_cells_in_1665,
    "15_prokaryotic_vs_eukaryotic_cellular_organization_nucleus": arch_15_prokaryotic_vs_eukaryotic_cellular_organization_nucleus,
    "16_mrs_gren_seven_vital_life_processes_cellular_basis": arch_16_mrs_gren_seven_vital_life_processes_cellular_basis,
    "17_light_microscope_components_optical_pathway_and_stage": arch_17_light_microscope_components_optical_pathway_and_stage,
    "18_total_magnification_calculation_eyepiece_and_objective": arch_18_total_magnification_calculation_eyepiece_and_objective,
    "19_microscope_focusing_technique_coarse_vs_fine_adjustment": arch_19_microscope_focusing_technique_coarse_vs_fine_adjustment,
    "20_wet_mount_slide_preparation_onion_epidermal_cells": arch_20_wet_mount_slide_preparation_onion_epidermal_cells,
    "21_biological_staining_iodine_solution_vs_methylene_blue": arch_21_biological_staining_iodine_solution_vs_methylene_blue,
    "22_biological_magnification_formula_actual_size_calculation": arch_22_biological_magnification_formula_actual_size_calculation,
    "23_plant_vs_animal_cells_major_structural_differences": arch_23_plant_vs_animal_cells_major_structural_differences,
    "24_cellulose_cell_wall_mechanical_support_and_turgor": arch_24_cellulose_cell_wall_mechanical_support_and_turgor,
    "25_plasma_membrane_selectively_permeable_barrier_function": arch_25_plasma_membrane_selectively_permeable_barrier_function,
}
