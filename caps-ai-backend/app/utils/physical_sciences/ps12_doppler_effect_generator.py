"""Physical Sciences Grade 12 — The Doppler Effect Dedicated Generator.

Curriculum Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 2/04. The Doppler effect.md

Complies with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=2, caps_weight_percent=15, suggested_duration_mins=9.
2. 50 Distinct Semantic Subskill Archetypes (0 generic shims).
3. Standardized Misconceptions.
4. Teacher-Editable Marking Schema.
5. Deterministic 3-Tier Hints.
6. South African comma decimal convention (",").
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from app.utils.grade12_physical_sciences.doppler_effect_generator import (
    BUILDERS,
    SUBSKILLS,
    ARCHETYPES,
    LEGACY_ALIASES,
    get_subskills,
    generate_question,
    generate,
)

TOPIC = "The Doppler effect"
TOPIC_KEY = "grade12_physical_sciences_doppler_effect"
__all__ = [
    "BUILDERS",
    "SUBSKILLS",
    "ARCHETYPES",
    "LEGACY_ALIASES",
    "get_subskills",
    "generate_question",
    "generate",
]
