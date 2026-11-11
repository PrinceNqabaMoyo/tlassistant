"""Natural Sciences Grade 9 Term 1: Systems in the Human Body Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 1/02. Systems in the human body.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .human_systems_archetypes_01_25 import BUILDERS as BUILDERS_01_25
from .human_systems_archetypes_26_50 import BUILDERS as BUILDERS_26_50

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
BUILDERS.update(BUILDERS_01_25)
BUILDERS.update(BUILDERS_26_50)

SUBSKILLS: List[str] = list(BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS
TOPIC_NAME = "Systems in the human body"

LEGACY_MAP: Dict[str, str] = {
    "human_system_purposes": "13_human_body_systems_overview_and_integration",
    "nervous_system_reflex_arc": "29_reflex_arc_neural_pathway_stimulus_to_effector_response",
    "excretory_system_filtration": "01_nephron_glomerulus_filtration_plate_identification",
    "musculoskeletal_mechanics": "26_antagonistic_muscle_pairs_biceps_and_triceps_arm_movement",
    "pathology_and_lifestyle": "47_healthy_lifestyle_balanced_diet_hydration_exercise_rest",
    "excretory": "01_nephron_glomerulus_filtration_plate_identification",
    "nephron": "01_nephron_glomerulus_filtration_plate_identification",
    "kidney_nephron": "01_nephron_glomerulus_filtration_plate_identification",
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
    """Generate deterministic questions for Grade 9 Natural Sciences: Systems in the human body."""
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
