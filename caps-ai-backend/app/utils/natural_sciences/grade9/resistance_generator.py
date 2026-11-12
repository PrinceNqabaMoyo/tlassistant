"""Natural Sciences Grade 9 Term 3: Resistance Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/05. Resistance.md.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .resistance_archetypes_01_25 import BUILDERS_01_25
from .resistance_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr9/Term 2/05. Resistance.md"
TOPIC_NAME = "Resistance"

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
DISPATCH_TABLE["concept_of_electrical_resistance"] = ARCHETYPE_BUILDERS["01_resistance_definition_opposition_to_electron_flow"]
DISPATCH_TABLE["factors_affecting_resistance_length_thickness"] = ARCHETYPE_BUILDERS["30_factor2_thickness_diameter_cross_sectional_area_rule"]
DISPATCH_TABLE["factors_affecting_resistance_material_temperature"] = ARCHETYPE_BUILDERS["26_factor1_type_of_material_copper_vs_nichrome_conductivity"]
DISPATCH_TABLE["resistors_as_control_and_heating_elements"] = ARCHETYPE_BUILDERS["14_electric_kettle_and_geyser_nichrome_heating_element"]
DISPATCH_TABLE["resistor_investigation_and_graphing"] = ARCHETYPE_BUILDERS["11_ohms_law_calculating_resistance_r_equals_v_over_i"]


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
    """Generate questions for Grade 9 Natural Sciences: Resistance."""
    rng = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for _ in range(max(1, count)):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None
        target_sub = subskill if subskill is not None else kwargs.get("archetype")
        if target_sub is not None:
            sub_key = str(target_sub).strip()
            sub_lower = sub_key.lower()
            if sub_lower not in ("", "mixed", "auto", "all", "default"):
                if sub_key in DISPATCH_TABLE:
                    builder = DISPATCH_TABLE[sub_key]
                else:
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
