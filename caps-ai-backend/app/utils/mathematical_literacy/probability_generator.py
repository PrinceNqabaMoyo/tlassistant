r"""Grade 10 Mathematical Literacy - Term 4: Probability Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr10/Term 4/02. Probability.md
  - curriculum_docs/Mathematical Literacy/
  - CAPS Mathematical Literacy Grade 10-12 Curriculum Standards

Features:
  - 52 distinct subskill archetypes covering:
      * The probability scale & number formats: verbal classification (impossible, unlikely, even chance, likely, certain); common fraction to decimal and percentage conversion; percentage to simplified fraction; decimal to percentage; probability bounds and validity ($0 \le P \le 1$); complementary event rule ($P(\text{not } E) = 1 - P(E)$); weather forecast precipitation complement; sum of all mutually exclusive outcomes equals 1; ordering events by likelihood (Subskills 1 to 9)
      * Single-stage theoretical probability & equipment: single fair coin toss ($P = 1/2$); single 6-sided die specific number ($1/6$); even and odd numbers on 6-sided die ($1/2$); prime numbers on 6-sided die ($2, 3, 5 \implies 1/2$); greater than or less than die thresholds; 8-sided octahedral die probability; standard 52-card deck suit probability ($13/52 = 1/4$); picture/face card probability ($12/52 = 3/13$); drawing an Ace from a standard deck ($4/52 = 1/13$) (Subskills 10 to 18)
      * Coloured objects, bags & spinners: single colour marble selection from total; compound disjunction (colour A OR colour B); drawing a colour complement (NOT colour A); finding missing colour count from probability; circular spinner with equal sectors; circular spinner with unequal sector angles ($\theta / 360^\circ$); raffle single ticket winning chance ($1/N$); raffle multiple tickets winning chance ($k/N$); church fête lucky draw token selection (Subskills 19 to 27)
      * Relative frequency & experimental probability: experimental relative frequency calculation ($f / N$); comparing relative frequency with theoretical probability; Law of Large Numbers (convergence of empirical relative frequency to theoretical probability); expected frequency prediction in future trials ($E = P \times N$); gambler's fallacy and independence of random coin flips; detecting a biased / loaded die from trial frequencies; asymmetrical object orientation (drawing pin point-up); batch quality sampling defect estimation; school class tally survey empirical probability (Subskills 28 to 36)
      * Combined events, tree diagrams & two-way tables: full sample space enumeration for two coins $\{HH, HT, TH, TT\}$; probability of two Heads ($1/4 = 25\%$); probability of at least one Head ($3/4 = 75\%$); coin and 6-sided die combined outcomes grid ($2 \times 6 = 12$); two dice sum grid ($6 \times 6 = 36$ outcomes); two-way contingency table subgroup probability; two-stage tree diagram branch paths with replacement; mathematical audit of fair vs unfair 2-player dice game rules (Subskills 37 to 44)
      * Real-world applications (weather, medicine & risk): 5-day weather forecast precipitation table interpretation; National Veld and Forest Fire Danger Index (FDI) warning levels; manufacturing quality assurance pass rate; rapid medical screening test accuracy and false results; South African National Lottery (Lotto) sample space odds (1 in 14 million); motor vehicle insurance risk tiering; blood group donor compatibility probability; mathematical decision making under uncertainty (Subskills 45 to 52)
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

from .probability import DISPATCH_TABLE, SUBSKILLS


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
