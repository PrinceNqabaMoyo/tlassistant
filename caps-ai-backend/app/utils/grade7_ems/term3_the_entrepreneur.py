"""Grade 7 EMS: Term 3 - The Entrepreneur Generator (50 Semantic Archetypes).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/EMS_Gr7/Term 3/01. The entrepreneur.md.
Adheres strictly to the 6-Pillar Generator Contract.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .term3_the_entrepreneur_archetypes_01_25 import BUILDERS_01_25
from .term3_the_entrepreneur_archetypes_26_50 import BUILDERS_26_50

CURRICULUM_DOC = "curriculum_docs_auto/EMS_Gr7/Term 3/01. The entrepreneur.md"
TOPIC_NAME = "The entrepreneur"

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
DISPATCH_TABLE["def_entrepreneur"] = ARCHETYPE_BUILDERS["01_definition_of_an_entrepreneur"]
DISPATCH_TABLE["entrepreneurial_traits"] = ARCHETYPE_BUILDERS["11_trait_perseverance_in_adversity"]
DISPATCH_TABLE["needs_wants_opportunity"] = ARCHETYPE_BUILDERS["07_needs_wants_community_opportunities"]
DISPATCH_TABLE["explain_imbalances"] = ARCHETYPE_BUILDERS["37_fighting_unemployment_and_inequality"]
DISPATCH_TABLE["def_poverty_line"] = ARCHETYPE_BUILDERS["38_poverty_line_household_threshold"]


def get_subskills() -> List[str]:
    """Return the ordered list of 50 semantic subskill archetype IDs."""
    return list(SUBSKILLS)


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "compound",
    seed: Optional[int] = None,
    archetype_index: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate questions for Grade 7 EMS Term 3: The entrepreneur."""
    rng = _rng(seed)
    results: List[Dict[str, Any]] = []
    mode_norm = str(mode or "compound").strip()

    for idx_loop in range(max(1, int(count))):
        builder: Optional[Callable[[random.Random], Dict[str, Any]]] = None
        if subskill is not None:
            sub_key = str(subskill).strip()
            if sub_key in DISPATCH_TABLE:
                builder = DISPATCH_TABLE[sub_key]
            else:
                sub_lower = sub_key.lower()
                if sub_lower not in ("", "mixed", "all", "compound", "auto", "default", "none"):
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
            chosen = SUBSKILLS[(idx_loop if count > 1 else rng.randrange(len(SUBSKILLS))) % len(SUBSKILLS)]
            builder = ARCHETYPE_BUILDERS[chosen]

        q = builder(rng)
        q.setdefault("grade", 7)
        q.setdefault("subject", "Economic and Management Sciences")
        q.setdefault("term", 3)
        q.setdefault("topic", TOPIC_NAME)
        q.setdefault("caps_weight_percent", 30)
        q.setdefault("difficulty", difficulty)
        q.setdefault("suggested_duration_mins", max(2, int(int(q.get("marks", 2)) * 1.2)))
        if mode_norm.lower() in ("elementary", "scaffold"):
            q.setdefault("mode", f"elementary_{q.get('subskill', '')}")
        else:
            q.setdefault("mode", mode_norm or "compound")
        results.append(q)

    return results


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Single question generation entry point."""
    return generate(subskill=subskill, count=1, seed=seed, **kwargs)[0]
