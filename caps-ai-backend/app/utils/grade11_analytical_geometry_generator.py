"""Grade 11 Mathematics — Analytical Geometry Generator (Backward Compatibility Forwarder).
Forwarding all generation requests to the centralized 50-archetype generator in
app.utils.grade11_mathematics.analytical_geometry_generator.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from app.utils.grade11_mathematics.analytical_geometry_generator import (
    ARCHETYPES,
    BUILDERS,
    LEGACY_BUILDERS,
    ORDERED_SUBSKILLS,
    SUBSKILLS,
    generate,
    generate_question,
    generate_questions,
    get_subskills,
)

__all__ = [
    "ARCHETYPES",
    "BUILDERS",
    "LEGACY_BUILDERS",
    "ORDERED_SUBSKILLS",
    "SUBSKILLS",
    "generate",
    "generate_question",
    "generate_questions",
    "get_subskills",
]
