"""Natural Sciences Grade 9 Term 1: Cells as the Basic Units of Life Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 1/01. Cells as the basic units of life.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. organelle_identification: Plant and animal cell ultrastructure (calls reusable cytology builders with g9 scope).
2. plant_vs_animal_comparison: Differences between plant and animal cells (cell wall, vacuole, chloroplast).
3. respiration_vs_photosynthesis: Chemical energy transformations in mitochondria vs chloroplasts.
4. specialized_cells: Adaptations of nerve cells, red blood cells, muscle cells, and root hair cells.
5. biological_hierarchy_and_microscopy: Hierarchy from cells to organisms and magnification calculation (M = I / A).
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.cytology_cell_division_builders import (
    build_plant_cell_question,
    build_animal_cell_question,
)

TOPIC_NAME = "Cells as the basic units of life"
ORDERED_SUBSKILLS = [
    "organelle_identification",
    "plant_vs_animal_comparison",
    "respiration_vs_photosynthesis",
    "specialized_cells",
    "biological_hierarchy_and_microscopy",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_cells"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any]) -> Dict[str, Any]:
    if "marking_guide" not in res and "marking_schema" in res:
        res["marking_guide"] = res["marking_schema"]
    if "marking_schema" not in res and "marking_guide" in res:
        res["marking_schema"] = res["marking_guide"]
    res["topic"] = TOPIC_NAME
    res["grade"] = "9"
    res["term"] = 1
    return res


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "practice",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    if subskill in ("mixed", "auto", "", None):
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]
    elif subskill in ("plant_cell", "plant_cell_anatomy"):
        return _normalize_res(build_plant_cell_question(actual_seed, grade=9, mode=mode))
    elif subskill in ("animal_cell", "animal_cell_anatomy"):
        return _normalize_res(build_animal_cell_question(actual_seed, grade=9, mode=mode))
    elif subskill in ORDERED_SUBSKILLS:
        chosen_subskill = subskill
    else:
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]

    # Subskill 1: Organelle Identification (Rotates Plant Cell vs Animal Cell with g9 scope)
    if chosen_subskill == "organelle_identification":
        if actual_seed % 2 == 0:
            return _normalize_res(build_plant_cell_question(actual_seed, grade=9, mode=mode))
        else:
            return _normalize_res(build_animal_cell_question(actual_seed, grade=9, mode=mode))

    # Subskill 2: Plant vs Animal Comparison
    if chosen_subskill == "plant_vs_animal_comparison":
        scenarios = [
            {
                "question": (
                    "Which combination of cell structures is found **only in plant cells** and never in animal cells?"
                ),
                "correct": "Cellulose cell wall, chloroplasts, and a large permanent central vacuole",
                "distractors": [
                    "Cell membrane, nucleus, and mitochondria",
                    "Centrioles, lysosomes, and small temporary vacuoles",
                    "Endoplasmic reticulum, ribosomes, and cytoplasm",
                ],
                "explanation": (
                    "Plant cells possess rigid cellulose cell walls for support, photosynthetic chloroplasts "
                    "containing chlorophyll, and large central sap vacuoles. Animal cells lack cell walls and chloroplasts, "
                    "and have only small, temporary vacuoles if any."
                ),
                "misconceptions": ["cell_wall_membrane_confusion", "plant_animal_organelle_interchange"],
                "learning_objective_id": "NS9.LL.01.02",
            },
            {
                "question": (
                    "When placed into pure distilled water, why do animal red blood cells burst (lyse) "
                    "while plant cells become turgid without bursting?"
                ),
                "correct": "Plant cells have a rigid cellulose cell wall that exerts wall pressure against osmotic swelling",
                "distractors": [
                    "Plant cell membranes are completely impermeable to water molecules",
                    "Animal cells actively pump water out using chloroplasts",
                    "Plant cells absorb water through their mitochondria to make starch",
                ],
                "explanation": (
                    "The cellulose cell wall is rigid and exerts an inward turgor pressure that prevents the plant cell "
                    "from taking in excess water and bursting. Animal cells lack a cell wall; water influx via osmosis causes lysis."
                ),
                "misconceptions": ["osmotic_turgor_misconception", "cell_wall_osmotic_resistance_error"],
                "learning_objective_id": "NS9.LL.01.02",
            },
            {
                "question": (
                    "A student examines an unknown microscopic slide and observes a regular rectangular shape, "
                    "green oval organelles, and a nucleus pushed against the side of the cell. What type of cell is this?"
                ),
                "correct": "Plant cell, because chloroplasts and a large central vacuole pushing the nucleus aside are diagnostic features",
                "distractors": [
                    "Animal cell, because animal cells have a rectangular shape to fit tightly into tissues",
                    "Bacterial cell, because bacteria possess green chloroplasts for anaerobic respiration",
                    "Fungal cell, because only fungi have chloroplasts and central vacuoles",
                ],
                "explanation": (
                    "Chloroplasts and large central vacuoles pushing the nucleus to the cell periphery are unique to plant cells."
                ),
                "misconceptions": ["organelle_diagnostic_confusion", "cell_type_misidentification"],
                "learning_objective_id": "NS9.LL.01.02",
            },
        ]
        scen = scenarios[actual_seed % len(scenarios)]
        options = [scen["correct"]] + scen["distractors"]
        r.shuffle(options)
        return {
            "title": "Plant vs Animal Cell Comparison",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 1,
            "subskill": chosen_subskill,
            "question_type": "multiple_choice",
            "prompt": scen["question"],
            "question": scen["question"],
            "options": options,
            "correct_answer": scen["correct"],
            "sample_answer": f"**Correct Answer:** {scen['correct']}\n\n**Scientific Reason:** {scen['explanation']}",
            "marking_guide": f"1 mark for selecting the correct answer: {scen['correct']}.",
            "hints": [
                "Think about which structures provide green color, rigidity, and support in plants.",
                "Plant cells have three distinct features absent in animal cells: cell walls, chloroplasts, and permanent large vacuoles.",
                f"The correct option is: {scen['correct']}",
            ],
            "misconception_tags": scen["misconceptions"],
            "learning_objective_id": scen["learning_objective_id"],
        }

    # Subskill 3: Respiration vs Photosynthesis
    if chosen_subskill == "respiration_vs_photosynthesis":
        processes = [
            {
                "prompt": (
                    "Mitochondria are known as the 'powerhouses of the cell'.\n\n"
                    "1. Name the biochemical process that takes place inside the mitochondria.\n"
                    "2. State the word equation for this process.\n"
                    "3. Explain why active muscle cells contain significantly more mitochondria than fat storage cells."
                ),
                "sample": (
                    "1. **Cellular Respiration** (aerobic respiration);\n"
                    "2. **Word Equation:** Glucose + Oxygen → Carbon Dioxide + Water + Energy (ATP);\n"
                    "3. Muscle cells constantly contract and relax, requiring a continuous, large supply of energy (ATP) released by mitochondria, whereas fat cells are inactive storage sites."
                ),
                "marking": (
                    "• 1 mark: Cellular respiration [1]\n"
                    "• 2 marks: Glucose + Oxygen [1] → Carbon Dioxide + Water + Energy [1]\n"
                    "• 2 marks: Muscle cells require high energy / ATP for contraction [1]; fat cells have low metabolic activity [1]\n"
                    "**Total: 5 marks**"
                ),
                "hints": [
                    "Remember that respiration releases energy from digested food molecules.",
                    "The reactants are glucose and oxygen, releasing energy, carbon dioxide, and water.",
                    "Mitochondria break down glucose with oxygen to release energy (ATP) for muscle work.",
                ],
                "misconceptions": ["respiration_breathing_conflation", "photosynthesis_respiration_confusion"],
                "learning_objective_id": "NS9.LL.01.03",
            },
            {
                "prompt": (
                    "Photosynthesis and cellular respiration are complementary chemical processes in living systems.\n\n"
                    "1. Name the organelle where photosynthesis occurs.\n"
                    "2. Write the balanced chemical formula equation for photosynthesis.\n"
                    "3. Explain whether plant cells perform cellular respiration during the night."
                ),
                "sample": (
                    "1. **Chloroplast** (containing chlorophyll);\n"
                    "2. **Chemical Equation:** 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂ (in the presence of light energy and chlorophyll);\n"
                    "3. **Yes**, plant cells perform cellular respiration 24 hours a day (day and night) to release energy from glucose for cellular metabolism."
                ),
                "marking": (
                    "• 1 mark: Chloroplast [1]\n"
                    "• 2 marks: 6CO₂ + 6H₂O [1] → C₆H₁₂O₆ + 6O₂ [1]\n"
                    "• 2 marks: Yes [1]; plant cells require energy for life processes continuously / Day and night [1]\n"
                    "**Total: 5 marks**"
                ),
                "hints": [
                    "Photosynthesis uses carbon dioxide, water, and sunlight to produce glucose and oxygen in chloroplasts.",
                    "Plant cells must respire all the time, even when it is completely dark.",
                    "Chloroplast is the organelle; the equation is 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂; plants respire continuously.",
                ],
                "misconceptions": ["plants_only_photosynthesize_myth", "respiration_only_in_animals_myth"],
                "learning_objective_id": "NS9.LL.01.03",
            },
        ]
        proc = processes[actual_seed % len(processes)]
        return {
            "title": "Cellular Respiration & Photosynthesis",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 1,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": proc["prompt"],
            "question": proc["prompt"],
            "sample_answer": proc["sample"],
            "marking_guide": proc["marking"],
            "hints": proc["hints"],
            "misconception_tags": proc["misconceptions"],
            "learning_objective_id": proc["learning_objective_id"],
        }

    # Subskill 4: Specialized Cells
    if chosen_subskill == "specialized_cells":
        cell_types = [
            (
                "Nerve cell (Neuron)",
                "Long axon and branched dendrites",
                "Transmit electrical impulses quickly over long distances across the body",
                "nerve_cell_specialization_error",
            ),
            (
                "Red blood cell (Erythrocyte)",
                "Biconcave disc shape and absence of a nucleus",
                "Increase surface area-to-volume ratio for rapid oxygen diffusion and maximize space for hemoglobin",
                "rbc_adaptation_misconception",
            ),
            (
                "Root hair cell",
                "Long, thin cytoplasmic extension (hair)",
                "Significantly increase surface area for rapid absorption of water and dissolved mineral ions from soil",
                "root_hair_absorption_error",
            ),
            (
                "Muscle cell",
                "Elongated fiber shape packed with contractile protein filaments and abundant mitochondria",
                "Contract and relax forcefully to produce locomotion and body movement",
                "muscle_cell_specialization_error",
            ),
        ]
        target_cell = cell_types[actual_seed % len(cell_types)]
        question_text = (
            f"Specialized cells are adapted in structure to perform specific physiological functions.\n\n"
            f"1. Describe **one key structural adaptation** of a **{target_cell[0]}**.\n"
            f"2. Explain how this structural adaptation enables the cell to perform its specific function in the organism.\n"
            f"3. State whether this specialized cell can divide by itself indefinitely, and name the undifferentiated cells capable of becoming specialized."
        )
        sample = (
            f"1. **Structural Adaptation:** {target_cell[1]};\n"
            f"2. **Functional Advantage:** {target_cell[2]};\n"
            f"3. Most mature specialized cells cannot divide indefinitely; undifferentiated cells capable of dividing and specializing are **stem cells**."
        )
        marking = (
            f"• 1 mark: Structural feature stated accurately ({target_cell[1]}) [1]\n"
            f"• 2 marks: Clear functional explanation relating structure to adaptation ({target_cell[2]}) [2]\n"
            f"• 1 mark: Identification of stem cells [1]\n"
            "**Total: 4 marks**"
        )
        return {
            "title": f"Specialized Cells: {target_cell[0]}",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 1,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                f"Consider what unique shape or feature a {target_cell[0]} has that normal round cells lack.",
                f"How does {target_cell[1].lower()} make its job easier?",
                f"Structural adaptation: {target_cell[1]}. Function: {target_cell[2]}. Undifferentiated cells are stem cells.",
            ],
            "misconception_tags": [target_cell[3], "stem_cell_specialization_confusion"],
            "learning_objective_id": "NS9.LL.01.04",
        }

    # Subskill 5: Biological Hierarchy and Microscopy
    levels_seq = ["Cells", "Tissues", "Organs", "Organ Systems", "Organism"]
    img_size_mm = r.choice([15, 20, 30, 40, 50])
    mag_power = r.choice([100, 200, 400, 500])
    actual_size_mm = img_size_mm / mag_power
    actual_size_microns = actual_size_mm * 1000

    question_text = (
        "Living organisms exhibit a hierarchical structural organization, and microscopes are used to study them.\n\n"
        "1. Arrange the following organizational levels in order from **simplest to most complex**:\n"
        "   *Organs, Cells, Organism, Tissues, Organ Systems*\n"
        "2. A learner views a cheek cell under a light microscope. The measured image width on paper is "
        f"**{img_size_mm} mm** under a magnification of **{mag_power}×**.\n"
        "   Calculate the **actual size** of the cell in micrometers (µm). "
        "*(Use the formula: $\\text{Actual Size} = \\frac{\\text{Image Size}}{\\text{Magnification}}$)*"
    )
    sample = (
        "1. **Hierarchical Sequence:** Cells → Tissues → Organs → Organ Systems → Organism;\n"
        f"2. **Actual Size Calculation:**\n"
        f"   $$\\text{{Actual Size}} = \\frac{{\\text{{Image Size}}}}{{\\text{{Magnification}}}} = \\frac{{{img_size_mm}\\text{{ mm}}}}{{{mag_power}}} = {actual_size_mm:.4f}\\text{{ mm}}$$\n"
        f"   $$\\text{{In micrometers: }} {actual_size_mm:.4f} \\times 1000 = {actual_size_microns:.1f}\\text{{ µm}}$$"
    )
    marking = (
        "• 2 marks: Correct hierarchical sequence (Cells → Tissues → Organs → Organ Systems → Organism) [2]\n"
        "• 1 mark: Formula statement and substitution [1]\n"
        f"• 1 mark: Calculation in mm ({actual_size_mm:.4f} mm) [1]\n"
        f"• 1 mark: Final unit conversion to µm ({actual_size_microns:.1f} µm) [1]\n"
        "**Total: 5 marks**"
    )
    d_spec = {
        "kind": "micrograph_scale_view",
        "diagram_role": "context",
        "title": f"Cheek Cell Micrograph ({mag_power}×)",
        "magnification": f"{mag_power}×",
        "image_size_mm": img_size_mm,
        "specimen": "Human Cheek Cell (Epithelial)",
        "scale_bar_label": f"Image Width = {img_size_mm} mm",
    }

    return {
        "title": "Biological Hierarchy & Microscopy Calculations",
        "topic": TOPIC_NAME,
        "grade": "9",
        "term": 1,
        "subskill": chosen_subskill,
        "question_type": "structured",
        "prompt": question_text,
        "question": question_text,
        "diagram_spec": d_spec,
        "sample_answer": sample,
        "marking_guide": marking,
        "hints": [
            "Start with the basic unit of life, then groups of similar cells, then functioning structures.",
            "Remember that 1 millimeter (mm) = 1000 micrometers (µm). Divide image size by magnification.",
            f"Sequence: Cells → Tissues → Organs → Systems → Organism. Actual size = {actual_size_microns:.1f} µm.",
        ],
        "misconceptions": ["hierarchy_sequence_inversion", "microscopy_unit_conversion_error"],
        "learning_objective_id": "NS9.LL.01.05",
    }
