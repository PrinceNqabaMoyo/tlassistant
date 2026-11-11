"""Grade 8 Natural Sciences: Term 1 - Photosynthesis and Respiration Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 1/01. Photosynthesis and respiration.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .ns8_photosynthesis_respiration_archetypes_01_25 import BUILDERS as BUILDERS_01_25
from .ns8_photosynthesis_respiration_archetypes_26_50 import BUILDERS as BUILDERS_26_50

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
BUILDERS.update(BUILDERS_01_25)
BUILDERS.update(BUILDERS_26_50)

SUBSKILLS: List[str] = list(BUILDERS.keys())

LEGACY_MAP: Dict[str, str] = {
    "photosynthesis_chemical_equation_and_inputs": "02_photosynthesis_word_equation_and_chemical_symbols",
    "cellular_respiration_energy_release": "26_cellular_respiration_definition_and_energy_release",
    "starch_test_investigation_method": "13_testing_leaf_for_starch_step_boiling_water_kills_cells",
    "carbon_dioxide_limewater_test": "33_clear_limewater_test_for_carbon_dioxide_milky_precipitate",
    "chlorophyll_and_light_necessity_control": "15_testing_light_requirement_opaque_foil_stencil_investigation",
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


def generate(
    subskill: Optional[str] = None,
    archetype: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate deterministic questions for Grade 8 Natural Sciences: Photosynthesis and respiration."""
    chosen_target = subskill or archetype
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = rng.randint(1000, 999999) if count > 1 else seed
        sub_rng = random.Random(sub_seed) if sub_seed is not None else rng
        if chosen_target:
            chosen = _resolve_subskill(chosen_target)
        else:
            chosen = SUBSKILLS[i % len(SUBSKILLS)]
        builder = BUILDERS[chosen]
        q = builder(sub_rng)
        questions.append(q)

    return questions
