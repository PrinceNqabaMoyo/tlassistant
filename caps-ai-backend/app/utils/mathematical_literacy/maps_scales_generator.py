"""Grade 10 Mathematical Literacy - Term 2: Maps and Scales Generator facade.
Forwards to the modular 52-archetype generator in `scale_maps_and_plans_generator.py`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional
from .scale_maps_and_plans_generator import generate, DISPATCH_TABLE, SUBSKILLS

__all__ = ["generate", "DISPATCH_TABLE", "SUBSKILLS"]
