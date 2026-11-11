"""Grade 8 Natural Sciences: Term 1 - Interactions and Interdependence Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 1/02. Interactions and interdependence within the environment.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .ns8_ecology_interactions_archetypes_01_25 import BUILDERS as BUILDERS_01_25
from .ns8_ecology_interactions_archetypes_26_50 import BUILDERS as BUILDERS_26_50

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
BUILDERS.update(BUILDERS_01_25)
BUILDERS.update(BUILDERS_26_50)

SUBSKILLS: List[str] = list(BUILDERS.keys())

LEGACY_MAP: Dict[str, str] = {
    "ecological_levels_organisation": "01_levels_of_ecological_organisation_hierarchy",
    "food_webs_and_trophic_levels": "16_food_web_analysis_interpreting_interconnected_chains",
    "ecological_pyramid_energy_loss": "18_pyramid_of_energy_and_the_ten_percent_energy_rule",
    "abiotic_biotic_ecosystem_balance": "04_ecosystem_definition_biotic_and_abiotic_synthesis",
    "human_impact_and_adaptation": "36_human_impact_habitat_destruction_and_fragmentation",
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
    """Generate deterministic questions for Grade 8 Natural Sciences: Interactions and interdependence."""
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
