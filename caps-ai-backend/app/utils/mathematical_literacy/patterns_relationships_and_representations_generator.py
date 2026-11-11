r"""Grade 10 Mathematical Literacy - Term 3: Patterns, relationships and representations Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr10/Term 3/02. Patterns relationships and representations.md
  - curriculum_docs/Mathematical Literacy/
  - CAPS Mathematical Literacy Grade 10-12 Curriculum Standards

Features:
  - 52 distinct subskill archetypes covering:
      * Graphs that tell a story & trend interpretation: increasing, decreasing, or constant trends; steepness and rate of change comparison; meaning of flat horizontal segments (resting/stationary); discrete vs continuous data classification; discrete separate points vs continuous unbroken lines; independent (x) vs dependent (y) variables; practical meaning of vertical y-intercept (fixed starting cost/value); practical meaning of horizontal x-intercept (empty tank/zero balance); distance-time average speed calculation ($v = \Delta d / \Delta t$) (Subskills 1 to 9)
      * Linear patterns & tables of values: constant first difference identification; finding missing output ($y$) in linear table; finding missing input ($x$) in linear table; toothpick and tile geometric pattern growth formula derivation ($T_n = mn + c$); predicting high term values (term 50 or 100); determining pattern number from total pieces ($n = (T_n - c)/m$); direct proportion constant ratio ($k = y/x$); direct proportion straight line through origin $(0; 0)$ property; constructing and reading Cartesian coordinates $(x; y)$ from tables (Subskills 10 to 18)
      * Formulating linear equations ($y = mx + c$): formula from verbal word description; linear equation from table of values; identifying variable rate and fixed constant; cell phone contract monthly bill formula (subscription + extra minutes); electrician/artisan call-out fee plus hourly labour; metered taxi fare (base flagfall + per km); community event catering (venue hire + guest rate); calculating maximum affordable units within budget; linear temperature conversion between Celsius and Fahrenheit ($F = 1,8C + 32$) (Subskills 19 to 27)
      * Inverse proportion relationships: constant product verification ($x \times y = k$); sharing cash jackpot prize among $n$ winners ($S = P/n$); workers and days to complete a task ($W_1 \times D_1 = W_2 \times D_2$); rectangular garden dimensions with fixed area ($b = A/l$); travel speed and time for fixed distance ($t = d/v$); pump discharge rate and reservoir emptying time; finding missing values in an inverse proportion table; hyperbola curve characteristics (asymptotic to axes); distinguishing direct proportion from inverse proportion (Subskills 28 to 36)
      * Two-graph comparisons & break-even analysis: reading coordinates of point of intersection; practical meaning of intersection point (equal cost/time); determining cheaper option below vs above intersection point; car rental package comparisons (unlimited km vs base + km rate); break-even quantity calculation where $\text{Income} = \text{Total Cost}$; profit or loss calculation for specified sales volumes; business revenue line formula $I = \text{price} \times n$ passing through origin; production cost line formula $C = \text{fixed} + (\text{unit} \times n)$ with vertical intercept (Subskills 37 to 44)
      * Advanced representations, step graphs & modeling: evaluating multi-step formula to populate table rows; reading shopping centre parking fees from stepped tariff graph; courier parcel delivery cost from tiered mass brackets; interpreting inclining block municipal water consumption graphs with changing slopes; bank account simple interest linear growth ($A = P + Pin$); straight-line asset depreciation ($V = \text{Cost} - Dt$); loan repayment linear balance reduction; selecting the best mathematical representation for communication (Subskills 45 to 52)
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

from .patterns_relationships import DISPATCH_TABLE, SUBSKILLS


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
