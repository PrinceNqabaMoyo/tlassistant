"""Grade 10 Mathematical Literacy - Term 2: Assembly diagrams, floor plans and packaging Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr10/Term 2/02. Assembly diagrams floor plans and packaging.md
  - curriculum_docs/Mathematical Literacy/
  - CAPS Mathematical Literacy Grade 10-12 Curriculum Standards

Features:
  - 52 distinct subskill archetypes covering:
      * Assembly diagrams & component hardware, parts lists, assembly order, tool selection (Allen key, screwdrivers, spanners), fastener quantities, directional arrows, safety warning icons, electronic device disassembly/assembly (SIM & battery), drawer runner orientation, shelf spacing (Subskills 1 to 9)
      * Domestic electrical plug & appliance wiring, wire colour standards (Brown=Live, Blue=Neutral, Green/Yellow=Earth), prong placement, cord clamp strain relief, 2-pin vs 3-pin earthing, copper strand twisting (5 mm), current and fuse ratings (I=P/V), wiring hazard diagnosis, tensile earth wire margins (Subskills 10 to 17)
      * Floor plans — architectural symbols & layout analysis, walls, door swing quarter arcs, room types from fixtures, Southern Hemisphere North-facing aspect, kitchen work triangle, architectural design flaw audits, furniture clearance, window placement rules, doorway furniture ingress clearance (Subskills 18 to 26)
      * Scaled floor plans & cost calculations, numeric scale conversions (1:50, 1:100), inverse drawing length calculations, bar scale conversions, floor area (L × W), tile box estimates with 10% wastage and rounding up, tile project costs, skirting perimeter deducting doors, wall painting area deducting openings, apartment rental per m² (Subskills 27 to 35)
      * 3D packaging arrangements & orientation optimization, single-layer box grids, 3D multi-layer box stacking, lengthwise vs widthwise orientation comparisons, cylindrical cans packaging using diameter footprints, area/volume division fallacy explanation, void space calculations, mass limit vs volume capacity, master carton order requirements, parcel freight budget (Subskills 36 to 44)
      * 2D nets, models & pallet stacking, rectangular prism net faces and tabs, cube nets and dice opposite faces (sum=7), cylinder nets (wrapper C=πd), triangular prism nets, standard industrial pallet interlocking patterns (1 200 × 1 000 mm), container ceiling height stacking bounds, scale cardboard models, tessellating triangular prisms vs circular void efficiency (Subskills 45 to 52)
  - Full step-by-step pedagogical worked solutions showing the thought process:
      Step 1: Conceptual Reasoning & Identification
      Step 2: Technical Method & Working Setup with explicit mark allocation [1 Mark: Method – ...]
      Step 3: Final Calculation & Answer with explicit mark allocation [1 Mark: Accuracy – ...]
  - Strict South African Rand formatting with 2 decimal places where currency is calculated (e.g. R 1 250,00).
  - Clean LaTeX and math mode that renders seamlessly with KaTeX.
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints for scaffolded remediation.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .assembly_packaging import DISPATCH_TABLE, SUBSKILLS


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation function.
    Deterministic execution via seeded Random instance.
    Supports single generation, iteration mode by archetype_index (0..51),
    subskill filtering, or batch count.
    """
    actual_seed = seed if seed is not None else random.randint(1, 10_000_000)
    r = random.Random(actual_seed)

    questions: List[Dict[str, Any]] = []

    for i in range(max(1, count)):
        if archetype_index is not None and 0 <= archetype_index < len(SUBSKILLS):
            chosen_subskill = SUBSKILLS[archetype_index]
        elif subskill and subskill in DISPATCH_TABLE:
            chosen_subskill = subskill
        elif count > 1:
            chosen_subskill = SUBSKILLS[i % len(SUBSKILLS)]
        else:
            chosen_subskill = r.choice(SUBSKILLS)

        generator_fn = DISPATCH_TABLE[chosen_subskill]
        # Seed individual question generator for independent entropy
        q_seed = r.randint(1, 10_000_000)
        q_rng = random.Random(q_seed)
        q = generator_fn(q_rng)
        questions.append(q)

    return questions
