"""Life Sciences Grade 10 Term 1: Cell Division (Mitosis) Dedicated Generator.

Fully grounded in:
- curriculum_docs_auto/LifeSciences_Gr10/Term 1/02. Cell division.md

Subskills:
1. mitosis_stages: Visual identification and chronological sequence of Prophase, Metaphase, Anaphase, Telophase.
2. chromosome_behavior: Centromere splitting, chromatid segregation, spindle fiber apparatus.
3. cytokinesis_plant_vs_animal: Cleavage furrow pinching (animal) vs cell plate synthesis (plant).
4. cancer_and_cell_cycle: Uncontrolled mitotic cell division, carcinogens, benign vs malignant tumours.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.cytology_cell_division_builders import build_mitosis_question


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "compound",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    # Check for direct diagram subskills
    if subskill in ("mitosis_stages", "mitosis", "diagram", "diagram_label"):
        return build_mitosis_question(actual_seed, grade=10, mode=mode)

    # Deterministic 3-subskill progression across topic subskills
    ALL_SUBSKILLS = [
        "mitosis_stages",
        "cytokinesis_plant_animal",
        "cancer_cell_cycle",
    ]
    chosen_subskill = subskill if subskill in ALL_SUBSKILLS else ALL_SUBSKILLS[actual_seed % len(ALL_SUBSKILLS)]

    if chosen_subskill == "mitosis_stages":
        return build_mitosis_question(actual_seed, grade=10, mode=mode)

    if chosen_subskill == "cytokinesis_plant_animal":
        scenarios = [
            (
                "How does **cytokinesis** (cytoplasmic division) differ between dividing animal cells and plant cells?",
                "Animal cells form a cleavage furrow by contracting actin filaments; plant cells construct a rigid cell plate from Golgi vesicles",
                [
                    "Plant cells pinch in half using a cleavage furrow; animal cells build a cellulose wall",
                    "Animal cells divide their cytoplasm during Metaphase; plant cells divide during Prophase",
                    "Plant cells discard one daughter cell; animal cells preserve both daughter cells",
                ],
                "Due to the rigid cell wall, plant cells cannot pinch inward; they fuse Golgi vesicles along the phragmoplast into a new cell plate.",
                ["cytokinesis_mechanism_inversion", "phragmoplast_cleavage_confusion"],
            ),
            (
                "What provides the membrane and cell wall precursor materials needed to build the new **cell plate** "
                "across the equator of a dividing plant cell?",
                "Pectin- and cellulose-filled vesicles budding from the Golgi apparatus",
                [
                    "Mitochondrial fragments that disintegrate at the equator",
                    "Contractile centrioles that pull the wall inward from outside",
                    "Disintegrating nuclear envelope chromatin fibers",
                ],
                "Golgi vesicles fuse along the equatorial plane to lay down the middle lamella and primary cell wall.",
                ["cell_plate_origin_misunderstanding", "golgi_vesicle_role_confusion"],
            ),
        ]
    else:  # cancer_cell_cycle
        scenarios = [
            (
                "What is the underlying cellular defect that characterizes **cancer**?",
                "Uncontrolled, repeated mitotic cell division resulting from mutations in cell cycle checkpoint genes",
                [
                    "Failure of homologous chromosomes to cross over during meiosis in somatic cells",
                    "Complete cessation of ATP production by mitochondria causing cell dormancy",
                    "Spontaneous conversion of diploid somatic cells into haploid gametes",
                ],
                "Cancer arises when cell cycle control genes (proto-oncogenes and tumor suppressors) mutate, allowing unchecked mitosis.",
                ["cancer_etiology_misconception", "mitosis_regulation_failure_error"],
            ),
            (
                "What distinction separates a **malignant tumour** from a **benign tumour**?",
                "Malignant tumours invade adjacent healthy tissues and can metastasize through the bloodstream to distant organs",
                [
                    "Benign tumours spread aggressively throughout the entire lymph system",
                    "Malignant tumours are surrounded by a fibrous capsule that prevents metastasis",
                    "Benign tumours are caused exclusively by bacterial infections",
                ],
                "Malignant tumors lack capsules, invade surrounding tissues, and metastasize via blood/lymph.",
                ["benign_vs_malignant_inversion", "metastasis_definition_error"],
            ),
        ]

    prompt, correct_ans, distractors, explanation, tags = r.choice(scenarios)
    options = [correct_ans] + distractors
    r.shuffle(options)

    return {
        "id": f"ls10_mitosis_{actual_seed}_{chosen_subskill}",
        "archetype": "mitosis_cell_cycle",
        "topic": "Cell division",
        "subject": "Life Sciences",
        "grade": 10,
        "term": 1,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 3,
        "subskill": chosen_subskill,
        "question_text": prompt,
        "correct_answer": correct_ans,
        "options": options,
        "misconception_tags": tags,
        "hints": [
            "Consider the stages of the cell cycle and the regulation of somatic division.",
            explanation,
            f"The correct answer is: {correct_ans}.",
        ],
        "solution_steps": [
            "Step 1: Analyze the mitotic stage or regulatory event.",
            f"Step 2: Recall curriculum principle: {explanation}",
            f"Step 3: Confirm correct response: {correct_ans}.",
        ],
    }
