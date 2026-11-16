"""Grade 11-12 Technical Mathematics - Mensuration & Integration Archetypes 26-50.
Aggregates subskills 26-38 (from _26_38) and 39-50 (from _39_50).
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from app.utils.technical_mathematics.mensuration_calculus_archetypes_26_38 import (
    BUILDERS_26_38,
)
from app.utils.technical_mathematics.mensuration_calculus_archetypes_39_50 import (
    BUILDERS_39_50,
)

BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    **BUILDERS_26_38,
    **BUILDERS_39_50,
}

SUBSKILLS_26_50: List[str] = list(BUILDERS_26_50.keys())
