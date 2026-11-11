"""Grade 10 Mathematical Literacy - Term 2: Scale maps and plans Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr10/Term 2/01. Scale maps and plans.md
  - curriculum_docs/Mathematical Literacy/
  - CAPS Mathematical Literacy Grade 10-12 Curriculum Standards

Features:
  - 52 distinct subskill archetypes covering:
      * Number scale calculations & unit conversions: unit conversion factors (1 km = 100 000 cm), real distance from cm in km, real distance in metres, inverse map length from real km, inverse map length from real metres, scale ratio determination, large vs small scale comparison, 1:50 000 topographic standard, straight-line vs winding road distance (Subskills 1 to 9)
      * Bar scales, elevation & map resizing effects: bar scale segment reading, bar scale to number scale conversion, bar scale resizing advantage, number scale distortion under magnification, contour lines & spot height elevation, gradient slope calculation (rise/run), inset scale comparison, winding distance via string/paper edge (Subskills 10 to 17)
      * Compass directions, bearings & grid coordinates: 8-point compass directions from A to B, 16-point intermediate directions, True North 3-digit bearings, back-bearing reciprocal (±180°), alphanumeric street guide grid references, sequential turn-by-turn navigation, GPS coordinates in South African hemisphere (S & E), magnetic declination, cardinal elevation solar aspect (Subskills 18 to 26)
      * Travel time, speed, distance & fuel consumption: travel time calculation (t = d/v), fractional decimal hours to hours & minutes, average speed (v = d/t), arrival clock time with rest stops, fuel consumption (litres/100 km), total fuel cost, fuel economy vehicle comparison, total trip budget (fuel + tolls + food), carpooling vs bus fare comparison (Subskills 27 to 35)
      * Strip maps, road routes, tolls & distance charts: consecutive strip map segment distances sum, triangular distance chart matrix reading, toll plaza tariff aggregation, route choice (toll highway vs alternative route), safety rest stop 200 km rule, fuel range & refueling waypoint planning, average speed over distance (ASOD) enforcement, intermediate town distance subtraction, road sign destination distance & speed limit (Subskills 36 to 44)
      * Seating plans, indoor layouts & navigation: cinema/theatre grid row and seat number, sports stadium stands and turnstile gates, exam hall desk spacing and integrity, aeroplane cabin window/middle/aisle, banquet round table seating capacity, shopping mall directory navigation, emergency fire evacuation stairwells rule, universal wheelchair accessibility ramp (Subskills 45 to 52)
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

from .scale_maps import DISPATCH_TABLE, SUBSKILLS


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
