"""Life Sciences Grade 10 Term 1: Plant and Animal Cells Dedicated Generator.

Fully grounded in:
- curriculum_docs_auto/LifeSciences_Gr10/Term 1/01. Cells the basic units of life.md

Subskills:
1. plant_cell: Plant cell ultrastructure (cellulose wall, vacuole tonoplast, chloroplast thylakoids).
2. animal_cell: Animal cell ultrastructure (plasma membrane, centrosome centrioles, mitochondria cristae, lysosomes).
3. organelle_biochemistry: Enzymatic and metabolic functions (ATP synthesis, protein packaging in Golgi, translation in ribosomes).
4. membrane_transport: Fluid mosaic model, diffusion down concentration gradients, osmosis, and active transport.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.cytology_cell_division_builders import (
    build_plant_cell_question,
    build_animal_cell_question,
)


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
    if subskill in ("plant_cell", "plant_cell_ultrastructure"):
        return build_plant_cell_question(actual_seed, grade=10, mode=mode)

    if subskill in ("animal_cell", "animal_cell_ultrastructure"):
        return build_animal_cell_question(actual_seed, grade=10, mode=mode)

    # Deterministic 4-subskill progression across topic subskills
    ALL_SUBSKILLS = [
        "plant_cell",
        "animal_cell",
        "organelle_biochemistry",
        "membrane_transport",
    ]
    chosen_subskill = subskill if subskill in ALL_SUBSKILLS else ALL_SUBSKILLS[actual_seed % len(ALL_SUBSKILLS)]

    if chosen_subskill == "plant_cell":
        return build_plant_cell_question(actual_seed, grade=10, mode=mode)
    if chosen_subskill == "animal_cell":
        return build_animal_cell_question(actual_seed, grade=10, mode=mode)

    if chosen_subskill == "organelle_biochemistry":
        scenarios = [
            (
                "Which organelle receives nascent proteins from the rough endoplasmic reticulum, "
                "chemically modifies them by adding oligosaccharide chains, and packages them into secretory vesicles?",
                "Golgi apparatus (Golgi body)",
                [
                    "Mitochondrion",
                    "Lysosome",
                    "Chloroplast",
                ],
                "The Golgi apparatus modifies, sorts, and packages proteins synthesized on rough ER ribosomes.",
                ["golgi_er_sequence_confusion", "protein_trafficking_error"],
            ),
            (
                "Why do mitochondrial inner membranes have deeply folded invaginations called **cristae**?",
                "To drastically increase surface area for electron transport chain enzyme complexes and ATP synthase",
                [
                    "To store large amounts of glucose starch granules inside the matrix",
                    "To prevent oxygen gas from reacting with pyruvate molecules",
                    "To allow the organelle to divide independently via binary fission",
                ],
                "Increased membrane surface area maximizes ATP generation per mitochondrion.",
                ["cristae_surface_area_misconception", "mitochondrial_function_confusion"],
            ),
        ]
    else:  # membrane_transport
        scenarios = [
            (
                "According to the **Fluid Mosaic Model** of cell membranes, what is the primary structural matrix "
                "and what role do intrinsic proteins play?",
                "A fluid phospholipid bilayer matrix with embedded proteins acting as transport channels, carriers, and receptors",
                [
                    "A rigid cellulose carbohydrate sheet with static lipid droplets floating on top",
                    "A solid layer of proteins sandwiched between two impermeable nucleic acid sheets",
                    "A single layer of cholesterol molecules glued by glycoproteins",
                ],
                "The membrane is a dynamic phospholipid bilayer with floating mosaic protein complexes.",
                ["fluid_mosaic_model_misconception", "membrane_lipid_protein_relation_error"],
            ),
            (
                "How does **active transport** across a plasma membrane differ fundamentally from passive diffusion and osmosis?",
                "Active transport moves solute molecules against their concentration gradient using metabolic energy (ATP) via carrier proteins",
                [
                    "Active transport moves molecules down their concentration gradient without requiring ATP",
                    "Active transport occurs only across the non-living cellulose cell wall of plants",
                    "Active transport is restricted exclusively to the movement of free water molecules",
                ],
                "Active transport requires ATP phosphorylation to pump molecules against electrochemical gradients.",
                ["active_vs_passive_transport_inversion", "atp_carrier_protein_misunderstanding"],
            ),
        ]

    prompt, correct_ans, distractors, explanation, tags = r.choice(scenarios)
    options = [correct_ans] + distractors
    r.shuffle(options)

    return {
        "id": f"ls10_cyto_{actual_seed}_{chosen_subskill}",
        "archetype": "plant_animal_cells_advanced",
        "topic": "Cells the basic units of life",
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
            "Think about the biochemical functions carried out by specialized organelles.",
            explanation,
            f"The correct answer is: {correct_ans}.",
        ],
        "solution_steps": [
            "Step 1: Identify the cell physiological process or organelle ultrastructure.",
            f"Step 2: Recall curriculum principle: {explanation}",
            f"Step 3: Confirm correct response: {correct_ans}.",
        ],
    }
