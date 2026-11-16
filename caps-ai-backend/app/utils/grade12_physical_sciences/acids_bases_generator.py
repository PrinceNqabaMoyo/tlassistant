"""Grade 12 Physical Sciences — Acids and Bases Generator.

Deterministic 6-pillar CAPS question generator covering Paper 2 (Chemistry Term 2):
1. Arrhenius and Brønsted-Lowry theories: Proton donors and proton acceptors.
2. Conjugate acid-base pairs in simple, organic, and polyprotic systems.
3. Ampholytes (amphiprotic substances) and auto-protolysis of water (Kw).
4. Strong vs weak acids and bases, concentrated vs dilute, electrical conductivity.
5. Equilibrium constants Ka and Kb expressions, calculations, and ranking.
6. pH and pOH calculations: strong monoprotic, strong diprotic, strong monobasic, strong dibasic, dilution.
7. Salt hydrolysis: neutral, basic, and acidic salts with predictive models.
8. Titration curves, indicators, and end-point color transitions.
9. Practical volumetric analysis: apparatus, standard solution preparation, and stoichiometry.
10. Advanced applications: vinegar % purity, oxalic acid standardization, antacid capacity, excess reagent mixtures, back-titration, acid rain, chloralkali industry, cosmetic hair chemistry, and capstone exam autopsy.

Zero-Meta-Curriculum Invariant strictly enforced. 100% Procedural & Deterministic.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade12_physical_sciences.acids_bases_archetypes_01_25 import (
    BUILDERS_01_25,
)
from app.utils.grade12_physical_sciences.acids_bases_archetypes_26_50 import (
    BUILDERS_26_50,
)

TOPIC = "grade12_physical_sciences_acids_bases"

BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

ARCHETYPE_BUILDERS: Dict[str, Any] = BUILDERS
ARCHETYPES: Dict[str, Any] = BUILDERS
SUBSKILLS: List[str] = list(BUILDERS.keys())
ORDERED_SUBSKILLS: List[str] = list(SUBSKILLS)
AVAILABLE_SUBSKILLS: List[str] = list(SUBSKILLS)

LEGACY_ALIASES: Dict[str, str] = {
    "compound": "50_capstone_exam_titration_autopsy",
    "elementary_definitions_conjugate": "03_conjugate_acid_base_pairs",
    "elementary_ph_calc": "18_ph_strong_monoprotic_acid",
    "elementary_titration": "38_titration_stoichiometry_1_to_1",
    "conjugate": "03_conjugate_acid_base_pairs",
    "ph": "18_ph_strong_monoprotic_acid",
    "titration": "38_titration_stoichiometry_1_to_1",
    "hydrolysis": "26_salt_hydrolysis_concept_definition",
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
    """Generate a single deterministic 6-pillar question for Grade 12 Acids and Bases."""
    target = subskill or kwargs.get("subskill_id") or kwargs.get("archetype") or kwargs.get("mode")
    builder = _resolve_builder(target)
    if not builder:
        r = _rng(seed)
        chosen = r.choice(SUBSKILLS)
        builder = BUILDERS[chosen]
    q = builder(seed=seed)
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
) -> Any:
    """Main generator entrypoint adhering to the 6-pillar contract."""
    base_seed = 42 if seed is None else int(seed)
    effective_target = (
        subskill
        or kwargs.get("subskill_id")
        or kwargs.get("archetype")
        or (mode if mode not in ("compound", "auto", "default") else None)
    )

    questions: List[Dict[str, Any]] = []
    for i in range(max(1, count)):
        item_seed = base_seed if count == 1 else (base_seed * 1000 + i)
        builder = _resolve_builder(effective_target)
        if not builder:
            chosen = SUBSKILLS[(base_seed + i) % len(SUBSKILLS)]
            builder = BUILDERS[chosen]
        q = builder(seed=item_seed)
        q["seed"] = item_seed
        questions.append(q)

    as_list = kwargs.get("as_list", False)
    if count == 1 and not as_list and questions:
        return {"questions": questions, **questions[0]}
    return questions if as_list else {"questions": questions}
