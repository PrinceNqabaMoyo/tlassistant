"""Grade 12 Physical Sciences — The Doppler Effect (Deterministic 6-Pillar Generator).
Grounded strictly in:
  curriculum_docs_auto/PhysicalSciences_Gr12/Term 2/04. The Doppler effect.md

Complies with the 6-Pillar Generator Contract:
  1. Metadata: term=2, caps_weight_percent=15, suggested_duration_mins=9.
  2. 50 Distinct Semantic Subskill Archetypes (0 generic shims).
  3. Standardized Misconceptions.
  4. Teacher-Editable Marking Schema.
  5. Deterministic 3-Tier Pre-Baked Hints.
  6. South African comma decimal convention (",").
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List, Optional

from .doppler_effect_archetypes_01_25 import SUBSKILLS_01_25
from .doppler_effect_archetypes_26_50 import SUBSKILLS_26_50

TOPIC = "The Doppler effect"
TOPIC_KEY = "grade12_physical_sciences_doppler_effect"

# Combined roster of all 50 semantic builders
BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
BUILDERS.update(SUBSKILLS_01_25)
BUILDERS.update(SUBSKILLS_26_50)

# List of all 50 semantic subskill IDs
SUBSKILLS: List[str] = list(BUILDERS.keys())
ARCHETYPES: List[str] = list(BUILDERS.keys())

# Legacy alias mappings to ensure backward compatibility
LEGACY_ALIASES: Dict[str, str] = {
    "elementary_doppler_formula": "07_doppler_formula_moving_source_approaching_stationary_listener",
    "elementary_doppler_towards": "07_doppler_formula_moving_source_approaching_stationary_listener",
    "elementary_doppler_away": "08_doppler_formula_moving_source_receding_from_stationary_listener",
    "elementary_redshift_universe": "33_redshift_definition_and_spectral_line_displacement",
    "elementary_doppler_calc": "09_approaching_and_then_receding_pitch_drop",
    "doppler_wavefront_diagram": "25_doppler_wavefront_diagram_analysis",
    "scaffold": "25_doppler_wavefront_diagram_analysis",
    "concepts": "01_definition_and_nature_of_doppler_effect",
}


def get_subskills() -> List[str]:
    """Return all 50 semantic subskills supported by this generator."""
    return list(SUBSKILLS)


def generate_question(
    subskill: Optional[str] = None,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generate a single deterministic question for a specified subskill and seed."""
    r = random.Random(seed)

    target_sub = subskill
    if target_sub in LEGACY_ALIASES:
        target_sub = LEGACY_ALIASES[target_sub]

    if not target_sub or target_sub not in BUILDERS:
        target_sub = r.choice(SUBSKILLS)

    builder = BUILDERS[target_sub]
    return builder(r)


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    grade: str = "12",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation entry point for Grade 12 Doppler Effect questions."""
    r = random.Random(seed)
    questions: List[Dict[str, Any]] = []

    target_sub = subskill
    if target_sub in LEGACY_ALIASES:
        target_sub = LEGACY_ALIASES[target_sub]
    elif mode in LEGACY_ALIASES:
        target_sub = LEGACY_ALIASES[mode]

    for i in range(count):
        sub_seed = (seed + i * 47) if seed is not None else r.randint(1000, 99999)
        sub_r = random.Random(sub_seed)

        if target_sub and target_sub in BUILDERS:
            chosen_sub = target_sub
        else:
            chosen_sub = sub_r.choice(SUBSKILLS)

        builder = BUILDERS[chosen_sub]
        q = builder(sub_r)
        questions.append(q)

    return questions
