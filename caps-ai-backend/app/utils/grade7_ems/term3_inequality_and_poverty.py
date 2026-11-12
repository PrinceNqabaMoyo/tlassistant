"""Grade 7 EMS — Inequality and Poverty: 50-Archetype Deterministic Generator.
100% Aligned with South African National Curriculum Standards (Term 3: The Economy).
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 4/02. Inequality and poverty.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .term3_inequality_and_poverty_archetypes_01_25 import BUILDERS_01_25
from .term3_inequality_and_poverty_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade7_ems"
SUBTOPIC_ID = "term3_inequality_and_poverty"
TOPIC_NAME = "Inequality and poverty"
CURRICULUM_REFERENCE = "Term 3 > The Economy: Inequality and Poverty"

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

LEGACY_ALIAS_MAP: Dict[str, str] = {
    "poverty_causes_mcq": "08_apartheid_structural_exclusion_causes",
    "service_delivery_mcq": "22_rural_tax_base_and_service_delivery_cost",
    "education_poverty_mcq": "14_consequences_of_poor_quality_education",
    "urban_rural_mcq": "21_urbanization_and_rural_poverty_stats_bar_graph",
    "job_creation_essay": "31_job_longevity_and_security_for_poverty_reduction",
    "education_inequality_essay": "10_twelve_year_generation_education_lag",
    "concepts": "01_socio_economic_imbalances_definition",
    "discussion": "50_integrated_anti_poverty_strategy_synthesis",
}

DISPATCH_TABLE: Dict[str, Any] = {
    **ARCHETYPE_BUILDERS,
    **{alias: ARCHETYPE_BUILDERS[target] for alias, target in LEGACY_ALIAS_MAP.items()},
}


def get_subskills() -> List[str]:
    """Return the ordered list of 50 semantic subskill identifiers."""
    return list(ORDERED_SUBSKILLS)


def _resolve_builder(subskill: Optional[str]) -> Optional[Any]:
    if not subskill:
        return None
    raw = str(subskill).strip()
    if raw in DISPATCH_TABLE:
        return DISPATCH_TABLE[raw]
    lowered = raw.lower()
    if lowered in DISPATCH_TABLE:
        return DISPATCH_TABLE[lowered]
    if lowered.startswith("elementary_"):
        stripped = lowered[len("elementary_"):]
        if stripped in DISPATCH_TABLE:
            return DISPATCH_TABLE[stripped]
        lowered = stripped
    if lowered in ("compound", "all", "mixed", "auto", "default", "none", "general"):
        return None
    for key, builder in ARCHETYPE_BUILDERS.items():
        if lowered in key.lower():
            return builder
    return None


def _apply_mode_meta(q: Dict[str, Any], difficulty: str, mode: str) -> Dict[str, Any]:
    out = dict(q)
    out.setdefault("difficulty", difficulty or "medium")
    out.setdefault("mode", mode or "compound")
    out.setdefault("curriculum_reference", CURRICULUM_REFERENCE)
    return out


def generate_question(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single question dictionary for the requested subskill or random archetype."""
    rng = random.Random(seed)
    builder = _resolve_builder(subskill)
    if builder is None:
        chosen_key = rng.choice(ORDERED_SUBSKILLS)
        builder = ARCHETYPE_BUILDERS[chosen_key]
    q = builder(rng)
    return _apply_mode_meta(q, difficulty, mode)


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    count: int = 1,
    mode: str = "scaffold",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generate `count` deterministic questions for the requested subskill or across all 50 archetypes."""
    rng = random.Random(seed)
    total = max(1, int(count or 1))
    resolved = _resolve_builder(subskill)

    results: List[Dict[str, Any]] = []
    if resolved is not None:
        for _ in range(total):
            q = resolved(rng)
            results.append(_apply_mode_meta(q, difficulty, mode))
        return results

    start_idx = rng.randrange(len(ORDERED_SUBSKILLS))
    for idx in range(total):
        key = ORDERED_SUBSKILLS[(start_idx + idx) % len(ORDERED_SUBSKILLS)]
        q = ARCHETYPE_BUILDERS[key](rng)
        results.append(_apply_mode_meta(q, difficulty, mode))
    return results
