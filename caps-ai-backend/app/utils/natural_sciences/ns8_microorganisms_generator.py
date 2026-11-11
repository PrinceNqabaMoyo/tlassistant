"""Grade 8 Natural Sciences: Term 2 - Microorganisms Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/03. Microorganisms.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .ns8_microorganisms_archetypes_01_25 import BUILDERS as BUILDERS_01_25
from .ns8_microorganisms_archetypes_26_50 import BUILDERS as BUILDERS_26_50

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
BUILDERS.update(BUILDERS_01_25)
BUILDERS.update(BUILDERS_26_50)

SUBSKILLS: List[str] = list(BUILDERS.keys())

LEGACY_MAP: Dict[str, str] = {
    "microorganism_types_and_characteristics": "01_microorganisms_definition_and_microscopic_scale",
    "pathogens_and_infectious_diseases": "15_pathogenic_bacteria_tuberculosis_transmission_and_symptoms",
    "beneficial_uses_of_microorganisms": "27_yeast_alcoholic_fermentation_baking_and_brewing",
    "preventing_spread_and_sterilisation": "37_food_preservation_heat_pasteurisation_and_canning_sterilisation",
    "antibiotics_vs_antivirals_efficacy": "09_why_antibiotics_are_ineffective_against_viruses",
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
    """Generate deterministic questions for Grade 8 Natural Sciences: Microorganisms."""
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
