"""Natural Sciences Grade 9 Term 2: Reactions of Non-Metals with Oxygen Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/03. Reactions of non metals with oxygen.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .reactions_nonmetals_oxygen_archetypes_01_25 import BUILDERS_01_25
from .reactions_nonmetals_oxygen_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr9/Term 2/03. Reactions of non metals with oxygen.md"
TOPIC_NAME = "Reactions of non metals with oxygen"

ARCHETYPE_BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = SUBSKILLS

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = dict(ARCHETYPE_BUILDERS)
for idx, key in enumerate(SUBSKILLS, 1):
    DISPATCH_TABLE[idx] = ARCHETYPE_BUILDERS[key]
    DISPATCH_TABLE[f"{idx:02d}"] = ARCHETYPE_BUILDERS[key]

# Legacy backward-compatibility aliases
DISPATCH_TABLE["general_nonmetal_oxidation_rule"] = ARCHETYPE_BUILDERS["01_nonmetal_oxidation_general_word_equation"]
DISPATCH_TABLE["carbon_combustion_and_limewater_test"] = ARCHETYPE_BUILDERS["08_limewater_test_positive_milky_observation"]
DISPATCH_TABLE["sulfur_combustion_and_safety"] = ARCHETYPE_BUILDERS["15_sulfur_dioxide_toxicity_and_fume_hood_protocol"]
DISPATCH_TABLE["nonmetal_oxides_acidity"] = ARCHETYPE_BUILDERS["28_nonmetal_oxide_water_reaction_sulfurous_acid"]
DISPATCH_TABLE["acid_rain_environmental_impact"] = ARCHETYPE_BUILDERS["33_acid_rain_coal_power_stations_mpumalanga_emissions"]


def get_subskills() -> List[str]:
    """Return the ordered list of 50 semantic subskill archetype IDs."""
    return list(SUBSKILLS)


def generate(
    subskill: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    archetype_index: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate questions for Grade 9 Natural Sciences: Reactions of non metals with oxygen."""
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(max(1, count)):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None
        if subskill is not None:
            sub_key = str(subskill).strip()
            if sub_key in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[sub_key]
            else:
                sub_lower = sub_key.lower()
                for k, b in DISPATCH_TABLE.items():
                    if isinstance(k, str) and (sub_lower in k.lower() or k.lower() in sub_lower):
                        builder = b
                        break

        if builder is None and archetype_index is not None:
            try:
                idx = int(archetype_index)
                if idx in DISPATCH_TABLE:
                    builder = DISPATCH_TABLE[idx]
                elif 1 <= idx <= len(SUBSKILLS):
                    builder = ARCHETYPE_BUILDERS[SUBSKILLS[idx - 1]]
            except (ValueError, TypeError):
                pass

        if builder is None:
            builder = ARCHETYPE_BUILDERS[rng.choice(SUBSKILLS)]

        q = builder(rng)
        q.setdefault("grade", 9)
        q.setdefault("subject", "Natural Sciences")
        q.setdefault("topic", TOPIC_NAME)
        q.setdefault("term", 2)
        q.setdefault("difficulty", difficulty)
        questions.append(q)

    return questions


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
