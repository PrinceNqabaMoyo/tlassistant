"""Grade 10 Mathematical Literacy - Term 1: Measuring Length, Weight, Volume and Temperature Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr10/Term 1/01. Measuring length weight volume and temperature.md
  - CAPS Mathematical Literacy Grade 10-12 Curriculum Standards (Paper 2: Measurement)

Features:
  - 52 distinct subskill archetypes covering length/distance, mass/weight scales, volume/capacity,
    temperature/thermometers, and integrated practical costing.
  - Modular architecture (all files strictly < 2000 lines).
"""

from __future__ import annotations

from .measuring import (
    SUBSKILLS,
    DISPATCH_TABLE,
    generate,
)

# Export all individual subskill generators for dynamic reflection and registry discovery
from .measuring.length_distance import *
from .measuring.mass_weight import *
from .measuring.volume_capacity import *
from .measuring.temperature_integrated import *

__all__ = ["SUBSKILLS", "DISPATCH_TABLE", "generate"]
