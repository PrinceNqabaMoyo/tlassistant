"""Grade 7 Natural Sciences: Term 1 - Variation Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/04. Variation.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .ns7_variation_archetypes_01_25 import BUILDERS as BUILDERS_01_25
from .ns7_variation_archetypes_26_50 import BUILDERS as BUILDERS_26_50

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
BUILDERS.update(BUILDERS_01_25)
BUILDERS.update(BUILDERS_26_50)

SUBSKILLS: List[str] = list(BUILDERS.keys())

LEGACY_MAP: Dict[str, str] = {
    "variation_within_species_definition": "01_variation_within_species_concept",
    "inherited_vs_environmental_variation": "07_inherited_variation_definition_and_mechanism",
    "continuous_vs_discontinuous_variation": "17_continuous_variation_definition_and_spectrum",
    "survival_value_of_variation": "26_survival_value_of_variation_environmental_change",
    "species_concept_and_interbreeding": "48_distinguishing_species_variation_vs_inter_species_differences",
}


def _resolve_subskill(subskill: Optional[str]) -> str:
    if not subskill:
        return random.choice(SUBSKILLS)
    s = subskill.strip().lower()
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
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate deterministic questions for Grade 7 Natural Sciences: Variation."""
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = rng.randint(1000, 999999) if count > 1 else seed
        sub_rng = random.Random(sub_seed) if sub_seed is not None else rng
        if subskill:
            chosen = _resolve_subskill(subskill)
        else:
            chosen = SUBSKILLS[i % len(SUBSKILLS)]
        builder = BUILDERS[chosen]
        q = builder(sub_rng)
        questions.append(q)

    return questions
