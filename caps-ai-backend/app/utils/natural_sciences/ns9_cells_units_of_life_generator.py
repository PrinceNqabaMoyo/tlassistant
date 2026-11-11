"""Natural Sciences Grade 9 Term 1: Cells as the Basic Units of Life Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 1/01. Cells as the basic units of life.md

Subskills:
1. plant_cell: Plant cell structure (cell wall, chloroplasts, large vacuole, nucleus, cytoplasm).
2. animal_cell: Animal cell structure (plasma membrane, nucleus, mitochondria, cytoplasm).
3. plant_vs_animal_comparison: Differences between plant and animal cells.
4. cell_theory_and_microscopy: Principles of cell theory and light microscope functioning.
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
    if subskill in ("plant_cell", "plant_cell_anatomy"):
        return build_plant_cell_question(actual_seed, grade=9, mode=mode)

    if subskill in ("animal_cell", "animal_cell_anatomy"):
        return build_animal_cell_question(actual_seed, grade=9, mode=mode)

    # Deterministic 4-subskill progression across topic subskills
    ALL_SUBSKILLS = [
        "plant_cell",
        "animal_cell",
        "plant_vs_animal_comparison",
        "cell_theory_microscopy",
    ]
    chosen_subskill = subskill if subskill in ALL_SUBSKILLS else ALL_SUBSKILLS[actual_seed % len(ALL_SUBSKILLS)]

    if chosen_subskill == "plant_cell":
        return build_plant_cell_question(actual_seed, grade=9, mode=mode)
    if chosen_subskill == "animal_cell":
        return build_animal_cell_question(actual_seed, grade=9, mode=mode)

    if chosen_subskill == "plant_vs_animal_comparison":
        scenarios = [
            (
                "Which combination of cell structures is found **only in plant cells** and never in animal cells?",
                "Cellulose cell wall, chloroplasts, and a large permanent central vacuole",
                [
                    "Plasma membrane, nucleus, and mitochondria",
                    "Centrioles, lysosomes, and small temporary vacuoles",
                    "Endoplasmic reticulum, ribosomes, and Golgi bodies",
                ],
                "Only plant cells possess rigid cellulose cell walls, photosynthetic chloroplasts, and large central vacuoles.",
                ["plant_animal_organelle_confusion", "cell_wall_membrane_interchange"],
            ),
            (
                "When placed into pure distilled water, why do animal red blood cells burst (lyse) while plant cells do not?",
                "Plant cells have a rigid cellulose cell wall that withstands internal turgor pressure",
                [
                    "Plant cell membranes are completely impermeable to water molecules",
                    "Animal cells actively pump water out using chloroplasts",
                    "Plant cells absorb water through their mitochondria to make starch",
                ],
                "The cellulose cell wall provides mechanical resistance against internal osmotic pressure.",
                ["cell_wall_osmotic_resistance_error", "turgidity_lysis_misconception"],
            ),
        ]
    else:  # cell_theory_microscopy
        scenarios = [
            (
                "Which statement represents one of the core postulates of classical **Cell Theory**?",
                "All living organisms are composed of one or more cells, and all cells arise from pre-existing cells",
                [
                    "All cells contain a membrane-bound nucleus and chloroplasts",
                    "Cells can spontaneously generate from non-living organic matter",
                    "Every living cell undergoes meiosis during tissue growth",
                ],
                "Cell theory states that the cell is the basic structural and functional unit of life, arising from pre-existing cells.",
                ["cell_theory_postulate_confusion", "spontaneous_generation_misconception"],
            ),
            (
                "A learner views an onion epidermal cell using a light microscope with a 10× eyepiece and a 40× objective lens. "
                "What is the total magnification of the specimen?",
                "400× (10 × 40)",
                [
                    "50× (10 + 40)",
                    "30× (40 - 10)",
                    "4000× (10 × 40 × 10)",
                ],
                "Total magnification = Eyepiece magnification × Objective lens magnification (10 × 40 = 400×).",
                ["magnification_calculation_error", "additive_magnification_misconception"],
            ),
        ]

    prompt, correct_ans, distractors, explanation, tags = r.choice(scenarios)
    options = [correct_ans] + distractors
    r.shuffle(options)

    steps = [
        "Step 1: Analyze the cellular question prompt and structures.",
        f"Step 2: Recall curriculum principle: {explanation}",
        f"Step 3: Confirm correct response: {correct_ans}.",
    ]
    sol_str = "\n".join(steps)
    return {
        "id": f"ns9_cyto_{actual_seed}_{chosen_subskill}",
        "archetype": "cells_basic_units_of_life",
        "topic": "Cells as the basic units of life",
        "subject": "Natural Sciences",
        "grade": 9,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": chosen_subskill,
        "prompt": prompt,
        "question_text": prompt,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "options": options,
        "marks": 2,
        "total_marks": 2,
        "worked_solution": sol_str,
        "canonical_solution": sol_str,
        "explanation": explanation,
        "misconception_tags": tags,
        "hints": [
            "Consider the microscopic differences between plant and animal cells.",
            explanation,
            f"The correct answer is: {correct_ans}.",
        ],
        "solution_steps": steps,
    }
