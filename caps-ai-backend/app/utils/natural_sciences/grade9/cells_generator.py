"""Natural Sciences Grade 9 Term 1: Cells as the Basic Units of Life Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 1/01. Cells as the basic units of life.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .cells_archetypes_01_25 import BUILDERS as BUILDERS_01_25
from .cells_archetypes_26_50 import BUILDERS as BUILDERS_26_50

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
BUILDERS.update(BUILDERS_01_25)
BUILDERS.update(BUILDERS_26_50)

SUBSKILLS: List[str] = list(BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS
TOPIC_NAME = "Cells as the basic units of life"

LEGACY_MAP: Dict[str, str] = {
    "organelle_identification": "01_plant_cell_wall_cellulose_identification",
    "plant_vs_animal_comparison": "23_plant_vs_animal_cells_major_structural_differences",
    "respiration_vs_photosynthesis": "28_mitochondria_cellular_respiration_atp_energy_powerhouse",
    "specialized_cells": "38_specialized_cells_differentiation_and_division_of_labour",
    "biological_hierarchy_and_microscopy": "18_total_magnification_calculation_eyepiece_and_objective",
    "plant_cell": "01_plant_cell_wall_cellulose_identification",
    "plant_cell_anatomy": "01_plant_cell_wall_cellulose_identification",
    "animal_cell": "07_animal_cell_plasma_membrane_boundary_identification",
    "animal_cell_anatomy": "07_animal_cell_plasma_membrane_boundary_identification",
}


def get_archetypes() -> List[str]:
    return list(SUBSKILLS)


def _resolve_subskill(target: Optional[str]) -> str:
    if not target:
        return random.choice(SUBSKILLS)
    s = target.strip().lower()
    if s in BUILDERS:
        return s
    if s in LEGACY_MAP:
        return LEGACY_MAP[s]
    for k in SUBSKILLS:
        if k.startswith(s) or s in k:
            return k
    return SUBSKILLS[0]


def _normalize_res(res: Dict[str, Any]) -> Dict[str, Any]:
    if "topic" not in res:
        res["topic"] = TOPIC_NAME
    if "grade" not in res:
        res["grade"] = "9"
    if "term" not in res:
        res["term"] = 1
    if "question" not in res and "prompt" in res:
        res["question"] = res["prompt"]
    if "prompt" not in res and "question" in res:
        res["prompt"] = res["question"]
    if "marking_guide" not in res and "marking_schema" in res:
        res["marking_guide"] = res["marking_schema"]
    if "marking_schema" not in res and "marking_guide" in res:
        res["marking_schema"] = res["marking_guide"]
    return res


def generate(
    subskill: Optional[str] = None,
    archetype: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate deterministic questions for Grade 9 Natural Sciences: Cells as the basic units of life."""
    chosen_target = subskill or archetype
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = rng.randint(1000, 999999) if count > 1 else seed
        sub_rng = random.Random(sub_seed) if sub_seed is not None else rng
        if chosen_target and chosen_target not in ("mixed", "auto", "default", ""):
            chosen = _resolve_subskill(chosen_target)
        else:
            chosen = SUBSKILLS[i % len(SUBSKILLS)]
        builder = BUILDERS[chosen]
        q = builder(sub_rng)
        questions.append(_normalize_res(q))

    return questions
