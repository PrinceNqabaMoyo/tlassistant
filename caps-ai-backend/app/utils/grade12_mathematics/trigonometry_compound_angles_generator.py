"""Grade 12 Mathematics - Trigonometry: 50-Archetype Deterministic Generator.
100% Aligned with South African National Curriculum Standards (CAPS Grade 12 Paper 2).
Grounded strictly in curriculum_docs_auto/Mathematics_Gr12/Term 1/05. Trigonometry.md and Syllabus.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .trigonometry_compound_angles_archetypes_01_25 import BUILDERS_01_25
from .trigonometry_compound_angles_archetypes_26_50 import BUILDERS_26_50

TOPIC_ID = "grade12_mathematics"
SUBTOPIC_ID = "grade12_math_trigonometry"
TOPIC_NAME = "Trigonometry"
CURRICULUM_REFERENCE = "Grade 12 Mathematics > Term 1 & 2 > Trigonometry (Paper 2)"

ARCHETYPE_BUILDERS: Dict[str, Any] = {
    **BUILDERS_01_25,
    **BUILDERS_26_50,
}

ORDERED_SUBSKILLS: List[str] = list(ARCHETYPE_BUILDERS.keys())
SUBSKILLS: List[str] = list(ORDERED_SUBSKILLS)

LEGACY_ALIAS_MAP: Dict[str, str] = {
    "special_angle_compound": "01_compound_angle_cos_expansion_numerical",
    "double_angle_identity": "12_trig_identity_proof_lhs_rhs_basic",
    "general_solution_quadratic": "19_general_solution_double_angle_cos_quadratic",
    "double_angle_numerical": "06_double_angle_sin_numerical",
    "concepts": "01_compound_angle_cos_expansion_numerical",
}

DISPATCH_TABLE: Dict[str, Any] = {
    **ARCHETYPE_BUILDERS,
    **{alias: ARCHETYPE_BUILDERS[target] for alias, target in LEGACY_ALIAS_MAP.items() if target in ARCHETYPE_BUILDERS},
}

BUILDERS: Dict[str, Any] = DISPATCH_TABLE


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
    if mode and (mode == "compound" or str(mode).startswith("elementary_")):
        out["mode"] = mode
    else:
        out.setdefault("mode", "compound")
    out.setdefault("curriculum_reference", CURRICULUM_REFERENCE)
    out.setdefault("term", 1)
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
    target = subskill or (mode if isinstance(mode, str) and mode.startswith("elementary_") else None)
    builder = _resolve_builder(target)
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
    """Generate `count` deterministic questions for Grade 12 Trigonometry."""
    total = max(1, int(count or 1))
    rng = random.Random(seed)
    target = subskill or (mode if isinstance(mode, str) and mode.startswith("elementary_") else None)
    fixed_builder = _resolve_builder(target)
    results: List[Dict[str, Any]] = []
    pool = list(ORDERED_SUBSKILLS)
    if fixed_builder is None and total <= len(pool):
        chosen_keys = rng.sample(pool, total)
        for key in chosen_keys:
            item_seed = rng.randint(1, 10_000_000)
            q = ARCHETYPE_BUILDERS[key](random.Random(item_seed))
            results.append(_apply_mode_meta(q, difficulty, mode))
        return results
    for idx in range(total):
        item_seed = None if seed is None else (seed * 1009 + idx * 97 + 13)
        item_rng = random.Random(item_seed)
        if fixed_builder is not None:
            q = fixed_builder(item_rng)
        else:
            key = rng.choice(pool)
            q = ARCHETYPE_BUILDERS[key](item_rng)
        results.append(_apply_mode_meta(q, difficulty, mode))
    return results
