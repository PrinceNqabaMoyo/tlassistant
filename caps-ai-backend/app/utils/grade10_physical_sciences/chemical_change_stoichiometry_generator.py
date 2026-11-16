"""Grade 10 Physical Sciences — Chemical Change & Quantitative Chemistry Generator.
Deterministic 6-pillar generator aggregating 50 distinct semantic archetypes across 4 topics:
1. States of matter and the kinetic theory molecular theory (Term 1)
2. Physical and Chemical Changes (Term 2)
3. Representing chemical change (Term 2)
4. Quantitative aspects of chemical change (Term 3)

Complies with the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade10_physical_sciences.chemical_change_archetypes_01_25 import BUILDERS_01_25
from app.utils.grade10_physical_sciences.chemical_change_archetypes_26_50 import ARCHETYPES_26_50

TOPIC = "grade10_physical_sciences_chemical_change"

BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **ARCHETYPES_26_50,
}

ARCHETYPES: Dict[str, Any] = BUILDERS
SUBSKILLS: List[str] = list(BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
AVAILABLE_SUBSKILLS: List[str] = list(SUBSKILLS)

LEGACY_ALIASES: Dict[str, str] = {
    "compound": "50_stoichiometry_and_quantitative_chemistry_diagnostic_autopsy",
    "elementary_empirical": "26_empirical_formula_from_percentage_composition",
    "elementary_stoich": "42_stoichiometric_mass_to_gas_volume_at_stp",
    "empirical": "26_empirical_formula_from_percentage_composition",
    "stoich": "42_stoichiometric_mass_to_gas_volume_at_stp",
}


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def get_subskills() -> List[str]:
    """Return ordered list of all 50 semantic subskill identifiers."""
    return list(SUBSKILLS)


def _resolve_builder(target: Optional[str]):
    if not target or target in ("mixed", "all", "default"):
        return None
    if target in BUILDERS:
        return BUILDERS[target]
    if target in LEGACY_ALIASES and LEGACY_ALIASES[target] in BUILDERS:
        return BUILDERS[LEGACY_ALIASES[target]]
    t_low = str(target).lower()
    for k, b in BUILDERS.items():
        if t_low in k.lower():
            return b
    return None


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic 6-pillar question for Grade 10 Chemical Change."""
    r = _rng(seed)
    target = subskill or kwargs.get("subskill_id") or kwargs.get("archetype") or kwargs.get("mode")
    builder = _resolve_builder(target)
    if not builder:
        chosen = r.choice(SUBSKILLS)
        builder = BUILDERS[chosen]
    q = builder(r)
    if seed is not None:
        q["seed"] = int(seed)
    return q


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Main generator entrypoint adhering to the 6-pillar contract."""
    base_seed = 42 if seed is None else int(seed)
    effective_target = (
        subskill
        or kwargs.get("subskill_id")
        or kwargs.get("archetype")
        or (mode if mode != "compound" else None)
    )

    questions: List[Dict[str, Any]] = []
    for i in range(max(1, count)):
        item_seed = base_seed if count == 1 else (base_seed * 1000 + i)
        r = _rng(item_seed)
        builder = _resolve_builder(effective_target)
        if not builder:
            chosen = SUBSKILLS[(base_seed + i) % len(SUBSKILLS)]
            builder = BUILDERS[chosen]
        q = builder(r)
        q["seed"] = item_seed
        questions.append(q)

    if count == 1 and questions:
        return {"questions": questions, **questions[0]}
    return {"questions": questions}
