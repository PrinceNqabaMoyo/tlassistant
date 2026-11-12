"""Natural Sciences Grade 9 Term 3: Safety with Electricity Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 3/03. Safety with electricity.md and Syllabus.md.
"""
from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Callable, Dict, List, Optional

from .safety_electricity_archetypes_01_25 import BUILDERS_01_25
from .safety_electricity_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr9/Term 3/03. Safety with electricity.md"
TOPIC_NAME = "Safety with electricity"

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
DISPATCH_TABLE["three_pin_plug_wiring_and_color_codes"] = ARCHETYPE_BUILDERS["28_three_pin_plug_terminal_pin_positions_opened_view"]
DISPATCH_TABLE["fuse_operation_and_current_rating"] = ARCHETYPE_BUILDERS["16_fuse_current_rating_selection_for_appliances"]
DISPATCH_TABLE["circuit_breakers_and_earth_leakage"] = ARCHETYPE_BUILDERS["40_earth_leakage_unit_differential_current_detection"]
DISPATCH_TABLE["earthing_principle_and_shock_prevention"] = ARCHETYPE_BUILDERS["36_earthing_metal_casing_fault_protection_mechanism"]
DISPATCH_TABLE["domestic_hazards_and_illegal_connections"] = ARCHETYPE_BUILDERS["48_illegal_connections_physical_dangers_exposed_wires"]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_sfe"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


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
    """Generate questions for Grade 9 Natural Sciences: Safety with electricity."""
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
