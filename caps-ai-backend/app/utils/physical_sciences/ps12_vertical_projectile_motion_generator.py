"""Physical Sciences Grade 12 — Vertical Projectile Motion in 1D Dedicated Generator.

Curriculum Grounding:
- curriculum_docs_auto/PhysicalSciences_Gr12/Term 1/02. Vertical projectile motion in one dimension.md

Complies with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: term=1, caps_weight_percent=20, suggested_duration_mins=12.
2. Deconstructible compound questions & atomic sub-drills.
3. Standardized Misconceptions.
4. Teacher-Editable Marking Schema.
5. Deterministic 3-Tier Hints.
6. South African comma decimal convention (",").
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.grade12_physical_sciences.vertical_projectile_generator import generate as base_generate

TOPIC = "grade12_vertical_projectile_motion"


def generate(
    subskill: str = "concepts",
    difficulty: str = "medium",
    count: int = 1,
    grade: str = "12",
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generation endpoint for Grade 12 Vertical Projectile Motion."""
    res = base_generate(
        subskill=subskill,
        difficulty=difficulty,
        count=count,
        grade=grade,
        seed=seed,
        mode=mode,
        **kwargs,
    )
    qs = res.get("questions", []) if isinstance(res, dict) else res
    for q in qs:
        if isinstance(q, dict) and not q.get("diagram_spec"):
            q["diagram_spec"] = {"kind": "motion_graph", "v0": 19.6, "t_apex": 2.0, "t_total": 4.0}
    if isinstance(q.get("diagram_spec"), dict):
        q["diagram_spec"].setdefault("diagram_role", "identify" if q["diagram_spec"].get("target_pin") or q["diagram_spec"].get("pins") else "context")
    return res
