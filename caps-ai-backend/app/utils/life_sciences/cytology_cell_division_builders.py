"""Cytology, Mitosis, and Meiosis Diagram Subskill Builders.

Provides deterministic, 3-layer subskill builders for:
1. Plant Cell Ultrastructure (plant_cell)
2. Animal Cell Ultrastructure (animal_cell)
3. Mitosis Stages (mitosis_stages)
4. Meiosis Crossing Over & Recombination (meiosis_crossing_over)

Implements:
- 6-pillar contract (term, caps_weight_percent, duration, misconception_tags, 3-tier hints).
- Anti-leak security: client receives opaque randomized `ref` tokens; zero structure names in DOM.
- Multi-grade support (Grade 9 Natural Sciences macroscopic vs Grade 10/12 Life Sciences biochemical mechanisms).
- Single locked view mode in question cards.
"""

from __future__ import annotations

import json
import os
import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

ANCHORS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "data",
    "diagram_anchors",
)


def _load_anchors(master_name: str) -> Dict[str, Any]:
    path = os.path.join(ANCHORS_DIR, f"{master_name}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


PLANT_CELL_DATA = _load_anchors("plant_cell")
ANIMAL_CELL_DATA = _load_anchors("animal_cell")
MITOSIS_DATA = _load_anchors("mitosis_stages")
MEIOSIS_DATA = _load_anchors("meiosis_crossing_over")


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_cyto_salt"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


# ============================================================================
# 1. PLANT CELL BUILDER
# ============================================================================

def build_plant_cell_question(
    seed: int,
    grade: int = 10,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = PLANT_CELL_DATA["anchors"]
    grade_str = f"g{grade}"
    # Exclude cytoplasm (empty ground space between organelles) from Role L pin targets and distractors (Rule R8)
    empty_space_keys = {"cytoplasm"}
    allowed_keys = [
        k for k, v in anchors.items()
        if grade_str in v.get("grades", ["g9", "g10"]) and k not in empty_space_keys
    ]
    if len(allowed_keys) < 4:
        allowed_keys = [k for k in anchors.keys() if k not in empty_space_keys]

    if grade < 10:
        if subskill is None or subskill in ("plant_cell", "plant_cell_anatomy", "plant_unique_features"):
            subskill = r.choice(["organelle_identification", "organelle_functions"])
    else:
        if subskill is None or subskill in ("plant_cell", "plant_cell_anatomy"):
            subskill = r.choice(["organelle_identification", "plant_unique_features", "organelle_functions"])

    if subskill == "plant_unique_features" and "chloroplast" in allowed_keys:
        target_key = "chloroplast"
    else:
        target_key = r.choice(allowed_keys)
    target = anchors[target_key]

    other_keys = [k for k in allowed_keys if k != target_key]
    r.shuffle(other_keys)
    selected_keys = [target_key] + other_keys[:3]
    r.shuffle(selected_keys)

    pin_letters = ["A", "B", "C", "D"]
    pins_payload = []
    target_pin = "A"

    for idx, k in enumerate(selected_keys):
        letter = pin_letters[idx]
        ref = _make_ref(seed, k, idx)
        pins_payload.append({
            "pin": letter,
            "anchor": anchors[k]["anchor"],
            "default_box": anchors[k]["default_box"],
            "side": anchors[k]["side"],
            "ref": ref,
        })
        if k == target_key:
            target_pin = letter

    landmarks = [
        {
            "id": p["ref"],
            "label": f"Structure {p['pin']}",
            "x": p["anchor"][0],
            "y": p["anchor"][1],
        }
        for p in pins_payload
    ]
    view_mode = "textbook"

    if subskill == "plant_unique_features":
        question_text = (
            f"Which organelle indicated by **Pin {target_pin}** is present in eukaryotic plant cells "
            f"to carry out autotrophic carbohydrate synthesis, but is strictly absent from animal cells?"
        )
        correct_answer = "Chloroplast (Thylakoids & Stroma)"
        distractors = [
            "Mitochondrion (Cristae & Matrix)",
            "Nucleus (Chromatin & Nuclear Envelope)",
            "Plasma Membrane (Cell Membrane)",
        ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["chloroplast_mitochondria_confusion", "plant_vs_animal_organelle_error"]
        hints = [
            "Plants are autotrophic and produce their own organic food using sunlight.",
            "Chloroplasts contain chlorophyll pigments organized into thylakoid grana.",
            f"The correct organelle is {correct_answer}.",
        ]
    elif subskill == "organelle_functions":
        question_text = (
            f"Study the plant cell diagram. What is the physiological function of the organelle "
            f"indicated by **Pin {target_pin}**?"
        )
        correct_answer = target["description"]
        distractors = [anchors[k]["description"] for k in other_keys[:3]]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["organelle_function_mismatch", "turgor_pressure_vacuole_misconception"]
        hints = [
            f"Consider the structural position and ultrastructure of Pin {target_pin}.",
            f"This organelle is the {target['name']}.",
            f"The function of this structure is: {correct_answer}.",
        ]
    else:  # organelle_identification
        question_text = (
            f"Study the ultrastructure cross-section of the plant cell. "
            f"Identify the organelle indicated by **Pin {target_pin}**."
        )
        correct_answer = target["name"]
        distractor_names = [anchors[k]["name"] for k in other_keys[:3]]
        options = [correct_answer] + distractor_names
        r.shuffle(options)
        misconception_tags = ["cell_wall_membrane_confusion", "vacuole_tonoplast_inversion"]
        hints = [
            f"Observe Pin {target_pin} inside or surrounding the plant cell.",
            f"{target['description'][:80]}...",
            f"The organelle indicated by Pin {target_pin} is {correct_answer}.",
        ]

    diag_payload = {
        "diagram_role": "identify" if locals().get("target_pin") else "context",
        "image_type": "plant_cell",
        "master": "plant_cell",
        "view": view_mode,
        "viewBox": "0 0 600 480",
        "grade_mask": grade_str,
        "pins": pins_payload,
        "landmarks": landmarks,
        "target_pin": target_pin,
        "target_key": target_key,
    }

    return {
        "id": f"plant_cell_{grade}_{seed}_{subskill}",
        "archetype": "plant_cell_ultrastructure",
        "topic": "Cells the basic units of life" if grade == 10 else "Cells as the basic units of life",
        "subject": "Life Sciences" if grade == 10 else "Natural Sciences",
        "grade": grade,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": subskill,
        "modality": "bio_diagram",
        "question_type": "mcq",
        "prompt": question_text,
        "question_text": question_text,
        "correct_answer": correct_answer,
        "options": options,
        "diagram_meta": diag_payload,
        "diagram_spec": diag_payload,
        "misconception_tags": misconception_tags,
        "hints": hints,
        "marks": 2,

        "total_marks": 2,

        "sample_answer": correct_answer,

        "worked_solution": f"Step 1: Locate Pin {target_pin} on the plant cell plate..\nStep 2: Recall organelle characteristics: {target['description']}\nStep 3: Confirm that the correct answer is {correct_answer}.",

        "canonical_solution": f"Step 1: Locate Pin {target_pin} on the plant cell plate..\nStep 2: Recall organelle characteristics: {target['description']}\nStep 3: Confirm that the correct answer is {correct_answer}.",

        "explanation": f"Pin {target_pin} indicates {target['name']}: {target['description']}.",

        "solution_steps": [
            f"Step 1: Locate Pin {target_pin} on the plant cell plate..",
            f"Step 2: Recall organelle characteristics: {target['description']}",
            f"Step 3: Confirm that the correct answer is {correct_answer}.",
        ],
    }


# ============================================================================
# 2. ANIMAL CELL BUILDER
# ============================================================================

def build_animal_cell_question(
    seed: int,
    grade: int = 10,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = ANIMAL_CELL_DATA["anchors"]
    grade_str = f"g{grade}"
    # Exclude cytoplasm (empty ground space between organelles) from Role L pin targets and distractors (Rule R8)
    empty_space_keys = {"cytoplasm"}
    allowed_keys = [
        k for k, v in anchors.items()
        if grade_str in v.get("grades", ["g9", "g10"]) and k not in empty_space_keys
    ]
    if len(allowed_keys) < 4:
        allowed_keys = [k for k in anchors.keys() if k not in empty_space_keys]

    # Senior Phase (Grade 7-9 Natural Sciences) restricts FET-only centriole/oxidative phosphorylation subskills
    if grade < 10:
        if subskill is None or subskill in ("animal_cell", "animal_cell_anatomy", "animal_unique_features", "mitochondria_cellular_respiration"):
            subskill = r.choice(["organelle_identification", "organelle_functions"])
    else:
        if subskill is None or subskill in ("animal_cell", "animal_cell_anatomy"):
            subskill = r.choice(["organelle_identification", "animal_unique_features", "mitochondria_cellular_respiration"])

    if subskill == "animal_unique_features" and "centrosome_centrioles" in allowed_keys:
        target_key = "centrosome_centrioles"
    elif subskill == "mitochondria_cellular_respiration" and "mitochondrion" in allowed_keys:
        target_key = "mitochondrion"
    else:
        target_key = r.choice(allowed_keys)
    target = anchors[target_key]

    other_keys = [k for k in allowed_keys if k != target_key]
    r.shuffle(other_keys)
    selected_keys = [target_key] + other_keys[:3]
    r.shuffle(selected_keys)

    pin_letters = ["A", "B", "C", "D"]
    pins_payload = []
    target_pin = "A"

    for idx, k in enumerate(selected_keys):
        letter = pin_letters[idx]
        ref = _make_ref(seed, k, idx)
        pins_payload.append({
            "pin": letter,
            "anchor": anchors[k]["anchor"],
            "default_box": anchors[k]["default_box"],
            "side": anchors[k]["side"],
            "ref": ref,
        })
        if k == target_key:
            target_pin = letter

    landmarks = [
        {
            "id": p["ref"],
            "label": f"Structure {p['pin']}",
            "x": p["anchor"][0],
            "y": p["anchor"][1],
        }
        for p in pins_payload
    ]
    view_mode = "textbook"

    if subskill == "animal_unique_features":
        question_text = (
            f"Which organelle indicated by **Pin {target_pin}** occurs as a pair of perpendicular "
            f"microtubular cylinders that organize spindle fibers during animal cell division, but is absent in higher plants?"
        )
        correct_answer = "Centrosome with Centrioles"
        distractors = [
            "Mitochondrion (ATP Powerhouse)",
            "Lysosome (Digestive Hydrolases)",
            "Golgi Apparatus (Packaging Cisternae)",
        ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["centriole_absence_misconception", "animal_organelle_specialization_error"]
        hints = [
            "Animal cells use specialized barrel-shaped microtubule structures to organize mitotic spindles.",
            "This structure is situated near the nucleus and consists of two centrioles.",
            f"The correct structure is {correct_answer}.",
        ]
    elif subskill == "mitochondria_cellular_respiration":
        question_text = (
            f"Muscle cells require abundant ATP for contraction. Which organelle indicated by **Pin {target_pin}** "
            f"is especially numerous in metabolically active cells to perform oxidative phosphorylation?"
        )
        correct_answer = "Mitochondrion (ATP Powerhouse)"
        distractors = [
            "Nucleolus",
            "Small Temporary Vacuoles / Vesicles",
            "Golgi Apparatus (Packaging Cisternae)",
        ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["mitochondria_energy_conversion_error", "atp_site_misattribution"]
        hints = [
            "Look for the double-membraned organelle with cristae folds.",
            "Aerobic respiration occurs in the mitochondrial matrix and cristae.",
            f"The correct organelle is {correct_answer}.",
        ]
    elif subskill == "organelle_functions":
        question_text = (
            f"Study the animal cell diagram. What is the primary biological function of the structure "
            f"indicated by **Pin {target_pin}**?"
        )
        correct_answer = target["description"]
        distractors = [anchors[k]["description"] for k in other_keys[:3]]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["organelle_function_mismatch", "animal_cell_membrane_confusion"]
        hints = [
            f"Consider the structural position of Pin {target_pin} in the animal cell.",
            f"This structure is the {target['name']}.",
            f"Its function is: {correct_answer}.",
        ]
    else:  # organelle_identification
        question_text = (
            f"Study the ultrastructure cross-section of the animal cell. "
            f"Identify the organelle indicated by **Pin {target_pin}**."
        )
        correct_answer = target["name"]
        distractor_names = [anchors[k]["name"] for k in other_keys[:3]]
        options = [correct_answer] + distractor_names
        r.shuffle(options)
        misconception_tags = ["rough_smooth_er_confusion", "lysosome_peroxisome_misidentification"]
        hints = [
            f"Observe Pin {target_pin} within the cytoplasmic matrix.",
            f"{target['description'][:80]}...",
            f"The structure indicated by Pin {target_pin} is {correct_answer}.",
        ]

    diag_payload = {
        "diagram_role": "identify" if locals().get("target_pin") else "context",
        "image_type": "animal_cell",
        "master": "animal_cell",
        "view": view_mode,
        "viewBox": "0 0 600 480",
        "grade_mask": grade_str,
        "pins": pins_payload,
        "landmarks": landmarks,
        "target_pin": target_pin,
        "target_key": target_key,
    }

    return {
        "id": f"animal_cell_{grade}_{seed}_{subskill}",
        "archetype": "animal_cell_ultrastructure",
        "topic": "Cells the basic units of life" if grade == 10 else "Cells as the basic units of life",
        "subject": "Life Sciences" if grade == 10 else "Natural Sciences",
        "grade": grade,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": subskill,
        "modality": "bio_diagram",
        "question_type": "mcq",
        "prompt": question_text,
        "question_text": question_text,
        "correct_answer": correct_answer,
        "options": options,
        "diagram_meta": diag_payload,
        "diagram_spec": diag_payload,
        "misconception_tags": misconception_tags,
        "hints": hints,
        "marks": 2,

        "total_marks": 2,

        "sample_answer": correct_answer,

        "worked_solution": f"Step 1: Locate Pin {target_pin} on the animal cell plate..\nStep 2: Recall organelle characteristics: {target['description']}\nStep 3: Confirm that the correct answer is {correct_answer}.",

        "canonical_solution": f"Step 1: Locate Pin {target_pin} on the animal cell plate..\nStep 2: Recall organelle characteristics: {target['description']}\nStep 3: Confirm that the correct answer is {correct_answer}.",

        "explanation": f"Pin {target_pin} indicates {target['name']}: {target['description']}.",

        "solution_steps": [
            f"Step 1: Locate Pin {target_pin} on the animal cell plate..",
            f"Step 2: Recall organelle characteristics: {target['description']}",
            f"Step 3: Confirm that the correct answer is {correct_answer}.",
        ],
    }


# ============================================================================
# 3. MITOSIS BUILDER
# ============================================================================

def build_mitosis_question(
    seed: int,
    grade: int = 10,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = MITOSIS_DATA["anchors"]
    grade_str = f"g{grade}"
    allowed_keys = [k for k, v in anchors.items() if grade_str in v.get("grades", ["g10"])]
    if len(allowed_keys) < 4:
        allowed_keys = list(anchors.keys())

    if subskill is None or subskill in ("mitosis_stages", "mitosis_stages_grid"):
        subskill = r.choice(["stage_identification", "chromosome_behavior", "mitosis_significance"])

    if subskill == "chromosome_behavior" and "metaphase" in allowed_keys:
        target_key = "metaphase"
    else:
        target_key = r.choice(allowed_keys)
    target = anchors[target_key]

    other_keys = [k for k in allowed_keys if k != target_key]
    r.shuffle(other_keys)
    selected_keys = [target_key] + other_keys[:3]
    r.shuffle(selected_keys)

    pin_letters = ["A", "B", "C", "D"]
    pins_payload = []
    target_pin = "A"

    for idx, k in enumerate(selected_keys):
        letter = pin_letters[idx]
        ref = _make_ref(seed, k, idx)
        pins_payload.append({
            "pin": letter,
            "anchor": anchors[k]["anchor"],
            "default_box": anchors[k]["default_box"],
            "side": anchors[k]["side"],
            "ref": ref,
        })
        if k == target_key:
            target_pin = letter

    landmarks = [
        {
            "id": p["ref"],
            "label": f"Structure {p['pin']}",
            "x": p["anchor"][0],
            "y": p["anchor"][1],
        }
        for p in pins_payload
    ]
    view_mode = "textbook"

    if subskill == "chromosome_behavior":
        question_text = (
            f"During which mitotic stage indicated by **Pin {target_pin}** do duplicated chromosomes "
            f"align in single file along the equatorial plane of the spindle apparatus?"
        )
        correct_answer = "Stage 2: Metaphase"
        distractors = [
            "Stage 1: Prophase",
            "Stage 3: Anaphase",
            "Stage 4: Telophase & Cytokinesis",
        ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["metaphase_anaphase_sequence_inversion", "equatorial_plate_misidentification"]
        hints = [
            "Remember 'M' for Metaphase = Middle / equator.",
            "Chromosomes are attached to spindle fibers at their centromeres along the center line.",
            f"The correct mitotic stage is {correct_answer}.",
        ]
    elif subskill == "mitosis_significance":
        question_text = (
            f"What is the primary biological significance of mitotic somatic cell division in multicellular organisms?"
        )
        correct_answer = "To produce genetically identical diploid (2n) cells for growth, tissue repair, and replacement"
        distractors = [
            "To halve the chromosome number from diploid (2n) to haploid (n) for gametogenesis",
            "To promote maximum genetic recombination and crossing over between non-sister chromatids",
            "To generate diverse haploid daughter cells that double fertilization success",
        ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["mitosis_vs_meiosis_significance_confusion", "chromosome_number_invariance_error"]
        hints = [
            "Mitosis occurs in somatic (body) cells, not germline sex cells.",
            "Each daughter cell receives an exact duplicate set of parental chromosomes (2n = 2n).",
            f"The correct significance is: {correct_answer}.",
        ]
    else:  # stage_identification
        question_text = (
            f"Study the 4-stage mitotic division schematic. "
            f"Identify the mitotic stage or chromosome structure indicated by **Pin {target_pin}**."
        )
        correct_answer = target["name"]
        distractor_names = [anchors[k]["name"] for k in other_keys[:3]]
        options = [correct_answer] + distractor_names
        r.shuffle(options)
        misconception_tags = ["mitosis_phase_identification_error", "centromere_centriole_confusion"]
        hints = [
            f"Observe Pin {target_pin} in the 4-phase sequence (Prophase → Metaphase → Anaphase → Telophase).",
            f"{target['description'][:80]}...",
            f"The structure/phase indicated by Pin {target_pin} is {correct_answer}.",
        ]

    diag_payload = {
        "diagram_role": "identify" if locals().get("target_pin") else "context",
        "image_type": "mitosis_stages",
        "master": "mitosis_stages",
        "view": view_mode,
        "viewBox": "0 0 600 480",
        "grade_mask": grade_str,
        "pins": pins_payload,
        "landmarks": landmarks,
        "target_pin": target_pin,
        "target_key": target_key,
    }

    return {
        "id": f"mitosis_{grade}_{seed}_{subskill}",
        "archetype": "mitosis_stages_grid",
        "topic": "Cell division",
        "subject": "Life Sciences",
        "grade": grade,
        "term": 1,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 3,
        "subskill": subskill,
        "modality": "bio_diagram",
        "question_type": "mcq",
        "prompt": question_text,
        "question_text": question_text,
        "correct_answer": correct_answer,
        "options": options,
        "diagram_meta": diag_payload,
        "diagram_spec": diag_payload,
        "misconception_tags": misconception_tags,
        "hints": hints,
        "marks": 2,

        "total_marks": 2,

        "sample_answer": correct_answer,

        "worked_solution": f"Step 1: Locate Pin {target_pin} on the mitotic grid..\nStep 2: Recall phase characteristics: {target['description']}\nStep 3: Confirm that the correct answer is {correct_answer}.",

        "canonical_solution": f"Step 1: Locate Pin {target_pin} on the mitotic grid..\nStep 2: Recall phase characteristics: {target['description']}\nStep 3: Confirm that the correct answer is {correct_answer}.",

        "explanation": f"Pin {target_pin} indicates {target['name']}: {target['description']}.",

        "solution_steps": [
            f"Step 1: Locate Pin {target_pin} on the mitotic grid..",
            f"Step 2: Recall phase characteristics: {target['description']}",
            f"Step 3: Confirm that the correct answer is {correct_answer}.",
        ],
    }


# ============================================================================
# 4. MEIOSIS & CROSSING OVER BUILDER
# ============================================================================

def build_meiosis_question(
    seed: int,
    grade: int = 12,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = MEIOSIS_DATA["anchors"]
    grade_str = f"g{grade}"
    allowed_keys = [k for k, v in anchors.items() if grade_str in v.get("grades", ["g12"])]
    if len(allowed_keys) < 4:
        allowed_keys = list(anchors.keys())

    if subskill is None or subskill in ("meiosis_crossing_over", "crossing_over"):
        subskill = r.choice(["chiasma_and_synapsis", "genetic_variation_significance", "meiosis_abnormalities"])

    if subskill == "chiasma_and_synapsis" and "chiasma" in allowed_keys:
        target_key = "chiasma"
    else:
        target_key = r.choice(allowed_keys)
    target = anchors[target_key]

    other_keys = [k for k in allowed_keys if k != target_key]
    r.shuffle(other_keys)
    selected_keys = [target_key] + other_keys[:3]
    r.shuffle(selected_keys)

    pin_letters = ["A", "B", "C", "D"]
    pins_payload = []
    target_pin = "A"

    for idx, k in enumerate(selected_keys):
        letter = pin_letters[idx]
        ref = _make_ref(seed, k, idx)
        pins_payload.append({
            "pin": letter,
            "anchor": anchors[k]["anchor"],
            "default_box": anchors[k]["default_box"],
            "side": anchors[k]["side"],
            "ref": ref,
        })
        if k == target_key:
            target_pin = letter

    landmarks = [
        {
            "id": p["ref"],
            "label": f"Structure {p['pin']}",
            "x": p["anchor"][0],
            "y": p["anchor"][1],
        }
        for p in pins_payload
    ]
    view_mode = "textbook"

    if subskill == "chiasma_and_synapsis":
        question_text = (
            f"Study the diagram of Prophase I. What is the name of the X-shaped physical point of contact "
            f"indicated by **Pin {target_pin}** where non-sister chromatids break and exchange genetic material?"
        )
        correct_answer = "Chiasma (Point of Genetic Exchange)"
        distractors = [
            "Centromere",
            "Centrosome with Centrioles",
            "Cleavage Furrow",
        ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["chiasma_centromere_confusion", "synapsis_contact_point_error"]
        hints = [
            "A chiasma (plural: chiasmata) is the visible cross-over point between non-sister chromatids.",
            "Centromeres hold sister chromatids together; chiasmata form between non-sister homologous chromatids.",
            f"The correct term is {correct_answer}.",
        ]
    elif subskill == "genetic_variation_significance":
        question_text = (
            f"How does crossing over during Prophase I of meiosis contribute to evolutionary adaptation and genetic diversity?"
        )
        correct_answer = "It breaks linkage groups and creates recombinant chromatids with novel combinations of maternal and paternal alleles"
        distractors = [
            "It doubles the chromosome number to ensure offspring have 92 chromosomes",
            "It permanently prevents mutations from occurring in gametes",
            "It ensures all 4 gametes are genetically identical to the father",
        ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["crossing_over_significance_error", "recombinant_allele_misconception"]
        hints = [
            "Crossing over produces recombinant chromosomes that carry alleles from both parents.",
            "This ensures that every gamete has a unique genetic composition.",
            f"The correct answer is: {correct_answer}.",
        ]
    elif subskill == "meiosis_abnormalities":
        question_text = (
            f"If homologous chromosomes fail to separate during Anaphase I, or sister chromatids fail to separate "
            f"during Anaphase II (nondisjunction), what chromosomal condition can result upon fertilization of an n + 1 gamete?"
        )
        correct_answer = "Trisomy (such as Trisomy 21 / Down syndrome with 47 chromosomes)"
        distractors = [
            "Monoploidy (having only 23 total chromosomes in somatic cells)",
            "Polyploidy with complete absence of autosomes",
            "Klinefelter syndrome restricted exclusively to females",
        ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["nondisjunction_karyotype_confusion", "down_syndrome_aneuploidy_error"]
        hints = [
            "Nondisjunction leads to aneuploidy (abnormal chromosome count).",
            "An extra chromosome 21 results in Down syndrome (47 chromosomes).",
            f"The correct condition is {correct_answer}.",
        ]
    else:  # anatomy_identification
        question_text = (
            f"Study the Prophase I crossing over schematic. "
            f"Identify the chromosomal structure indicated by **Pin {target_pin}**."
        )
        correct_answer = target["name"]
        distractor_names = [anchors[k]["name"] for k in other_keys[:3]]
        options = [correct_answer] + distractor_names
        r.shuffle(options)
        misconception_tags = ["sister_vs_nonsister_chromatid_confusion", "recombinant_vs_parental_error"]
        hints = [
            f"Observe Pin {target_pin} on the synapsed bivalent or recombinant chromatids.",
            f"{target['description'][:80]}...",
            f"The structure indicated by Pin {target_pin} is {correct_answer}.",
        ]

    diag_payload = {
        "diagram_role": "identify" if locals().get("target_pin") else "context",
        "master": "meiosis_crossing_over",
        "image_type": "meiosis_crossing_over",
        "view": view_mode,
        "viewBox": "0 0 600 480",
        "grade_mask": grade_str,
        "pins": pins_payload,
        "landmarks": landmarks,
        "state": "static",
        "target_pin": target_pin,
        "target_key": target_key,
    }

    return {
        "id": f"meiosis_{grade}_{seed}_{subskill}",
        "archetype": "meiosis_crossing_over",
        "topic": "Meiosis",
        "subject": "Life Sciences",
        "grade": grade,
        "term": 1,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 3,
        "subskill": subskill,
        "modality": "bio_diagram",
        "question_type": "mcq",
        "prompt": question_text,
        "question_text": question_text,
        "correct_answer": correct_answer,
        "options": options,
        "diagram_meta": diag_payload,
        "diagram_spec": diag_payload,
        "misconception_tags": misconception_tags,
        "hints": hints,
        "marks": 2,

        "total_marks": 2,

        "sample_answer": correct_answer,

        "worked_solution": f"Step 1: Locate Pin {target_pin} on the crossing over schematic..\nStep 2: Note chromosomal relationship: {target['description']}\nStep 3: Confirm that the correct answer is {correct_answer}.",

        "canonical_solution": f"Step 1: Locate Pin {target_pin} on the crossing over schematic..\nStep 2: Note chromosomal relationship: {target['description']}\nStep 3: Confirm that the correct answer is {correct_answer}.",

        "explanation": f"Pin {target_pin} indicates {target['name']}: {target['description']}.",

        "solution_steps": [
            f"Step 1: Locate Pin {target_pin} on the crossing over schematic..",
            f"Step 2: Note chromosomal relationship: {target['description']}",
            f"Step 3: Confirm that the correct answer is {correct_answer}.",
        ],
    }
