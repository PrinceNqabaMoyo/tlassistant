"""Grade 9 Natural Sciences: Term 4 - The Earth as a System Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 4/01. The earth as a system.md.
50 Distinct Semantic Archetypes (01 to 50).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .earth_system_archetypes_01_25 import BUILDERS_01_25
from .earth_system_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr9/Term 4/01. The earth as a system.md"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate questions for The Earth as a System.

    Returns a list of question dicts adhering to the 6-pillar contract.
    """
    rng = random.Random(seed) if seed is not None else random.Random()
    results: List[Dict[str, Any]] = []

    for _ in range(max(1, count)):
        chosen_subskill = subskill
        if not chosen_subskill or chosen_subskill not in ARCHETYPE_BUILDERS:
            chosen_subskill = rng.choice(SUBSKILLS)
        builder = ARCHETYPE_BUILDERS[chosen_subskill]
        q = builder(rng)
        # Ensure common metadata
        q.setdefault("grade", 9)
        q.setdefault("subject", "Natural Sciences")
        q.setdefault("term", 4)
        q.setdefault("topic", "The earth as a system")
        results.append(q)

    return results


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
