r"""Grade 10 Mathematical Literacy - Term 3: Measurement of perimeter and area Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr10/Term 3/01. Measurement of perimeter and area.md
  - curriculum_docs/Mathematical Literacy/
  - CAPS Mathematical Literacy Grade 10-12 Curriculum Standards

Features:
  - 52 distinct subskill archetypes covering:
      * Perimeter of Polygons & Basic Shapes: Square perimeter ($4s$), rectangle perimeter ($2(l+w)$), triangle 3 sides sum ($a+b+c$), equilateral and isosceles triangles, right-angled triangle perimeter with Pythagoras hypotenuse calculation, circumference from radius ($2\pi r$), circumference from diameter ($\pi d$), closed semicircle perimeter ($\pi r + 2r$), closed quarter-circle perimeter ($\frac{1}{2}\pi r + 2r$) (Subskills 1 to 9)
      * Composite Perimeters & Boundary Applications: L-shaped boundary perimeter (opposite edge sum conservation), U-shaped courtyard perimeter, rectangle with semicircular bay extension (internal boundary omitted), athletics running track (2 straights + 2 semicircles), garden perimeter fencing deducting gate opening, multi-strand barbed wire paddock fencing ($P \times \text{strands}$), fence posts interval spacing ($P \div \text{spacing}$), interior room skirting boards deducting door openings, picture frame outer and inner border perimeter (Subskills 10 to 18)
      * Area of Polygons & Standard Shapes: Square area ($s^2$), rectangle area ($l \times w$), triangle area ($\frac{1}{2} b \times h$), right-angled triangle area from perpendicular legs, circle area from radius ($\pi r^2$), circle area from diameter ($\pi (d/2)^2$), semicircle area ($\frac{1}{2}\pi r^2$), quarter-circle area ($\frac{1}{4}\pi r^2$), trapezium area ($\frac{1}{2}(a+b)h$) (Subskills 19 to 27)
      * Composite Areas & Cutouts: L-shaped composite area (sum of 2 rectangles), T-shaped corridor area (top crossbar + stem), rectangle plus attached semicircular patio, rectangle wall plus triangular gable roof, back garden lawn minus rectangular swimming pool cutout, rectangular patio minus circular fish pond cutout, wall surface area minus door and window cutouts, concentric circular ring / washer / annulus ($\pi(R^2 - r^2)$), percentage of total property land area occupied by buildings (Subskills 28 to 36)
      * Surface Materials, Tiling, Paving & Turf: Number of floor tiles needed for bathroom ($A_{\text{room}} \div A_{\text{tile}}$), tile boxes required with 10% cutting wastage and rounding up, total cost of tiling project (tiles + adhesive), cobblestone pavers count for driveway ($A \times \text{pavers/m}^2$), cobblestones purchased in 500-paver pallets with upward rounding and cost, instant lawn turf rolls ($1\text{ m} \times 0,5\text{ m}$) with 5% cutting wastage, wall-to-wall carpeting and underlay budget, swimming pool thermal safety cover area with 0,5 m border overlap on all sides (Subskills 37 to 44)
      * Painting, Agriculture & Commercial Area Applications: Room wall painting gross area ($2(l+w) \times h$) minus doors and windows, paint litres required for 2 coats based on spread rate ($m^2/\text{L}$), paint purchased in 5L tins with upward rounding and total cost, vegetable garden organic compost application rate (1 bag per 2 m²), seedling planting density (seedlings/m²), crop field fertilizer application rate ($g/\text{m}^2$) converted to kg and cost, commercial retail shop rental per m², municipal residential property rates assessment (land area $\times$ value/m² $\times$ tariff factor $\div$ 12) (Subskills 45 to 52)
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

from .perimeter_area import DISPATCH_TABLE, SUBSKILLS


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

    for i in range(count):
        # Determine archetype function
        if archetype_index is not None:
            idx = (archetype_index + i) % len(SUBSKILLS)
            chosen_subskill = SUBSKILLS[idx]
            fn = DISPATCH_TABLE[chosen_subskill]
        elif subskill and subskill in DISPATCH_TABLE:
            fn = DISPATCH_TABLE[subskill]
        else:
            chosen_subskill = r.choice(SUBSKILLS)
            fn = DISPATCH_TABLE[chosen_subskill]

        q = fn(r)
        q["seed"] = actual_seed + i
        questions.append(q)

    return questions
