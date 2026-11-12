"""Grade 7 EMS — The Production Process: 50-Archetype Deterministic Generator.
100% Aligned with South African National Curriculum Standards (Term 4: The Economy).
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 3/03. The production process.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .term3_production_process_archetypes_01_25 import BUILDERS_01_25
from .term3_production_process_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade7_ems"
SUBTOPIC_ID = "term3_production_process"
TOPIC_NAME = "The production process"
CURRICULUM_REFERENCE = "Term 4 > The Economy: The Production Process"

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

LEGACY_ALIAS_MAP: Dict[str, str] = {
    "sector_id": "16_sector_classification_schedule_table",
    "sector_chain": "15_three_sector_production_chain_diagram",
    "in_out_id": "05_inputs_process_outputs_ipo_flowchart",
    "prod_ratio": "30_productivity_ratio_calculation",
    "tech_impact": "43_technology_impact_employment_unskilled_vs_skilled",
    "resource_types": "21_renewable_resources_definition_and_examples",
    "concepts": "01_production_definition_transformation",
    "discussion": "50_integrated_sa_production_and_growth_synthesis",
    "elementary_sectors": "12_primary_sector_extraction_role",
    "elementary_inputs_outputs": "04_tangible_vs_intangible_inputs",
    "elementary_productivity": "29_productivity_definition_output_per_input",
    "elementary_resources": "22_non_renewable_resources_finite_depletion",
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
