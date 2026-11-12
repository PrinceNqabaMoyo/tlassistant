"""Natural Sciences Grade 9 Term 3: Forces Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/01. Forces.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .forces_archetypes_01_25 import BUILDERS_01_25
from .forces_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr9/Term 3/01. Forces.md"
TOPIC_NAME = "Forces"

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
DISPATCH_TABLE["contact_vs_field_forces"] = ARCHETYPE_BUILDERS["10_contact_vs_non_contact_field_force_classification"]
DISPATCH_TABLE["gravitational_force_and_weight_calc"] = ARCHETYPE_BUILDERS["23_calculating_weight_w_equals_m_times_g_on_earth"]
DISPATCH_TABLE["magnetic_field_and_poles"] = ARCHETYPE_BUILDERS["30_magnetic_poles_north_south_and_law_of_attraction_repulsion"]
DISPATCH_TABLE["electrostatic_forces_and_charging"] = ARCHETYPE_BUILDERS["39_electrostatic_charging_by_friction_electron_transfer"]
DISPATCH_TABLE["atmospheric_electrostatics_and_lightning"] = ARCHETYPE_BUILDERS["48_thundercloud_charge_separation_and_lightning_discharge_mechanism"]


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
    """Generate questions for Grade 9 Natural Sciences: Forces."""
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
        q.setdefault("term", 3)
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
