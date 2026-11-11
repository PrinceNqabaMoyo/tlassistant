"""Grade 10 Mathematical Literacy - Term 1: Financial Documents and Tariff Systems Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr10/Term 1/02. Financial documents and tariff ystems.md
  - curriculum_docs/Mathematical Literacy/
  - CAPS Mathematical Literacy Grade 10-12 Curriculum Standards

Features:
  - 51 distinct subskill archetypes covering:
      * Municipal accounts, account/EasyPay reference numbers, property rates calculations, electricity meter readings, water meter readings, daily average consumption, running balance forward, overdue interest penalties, refuse removal bins, sewage/sanitation percentages (Subskills 1 to 9)
      * Electricity tariffs, single block tariffs, two-tier stepped blocks, three-tier stepped blocks, fixed monthly service charges + stepped, cents to Rands conversions, prepaid token units, seasonal summer vs winter rates, appliance kWh energy consumption, average unit cost comparisons (Subskills 10 to 18)
      * Water tariffs, free basic water allowances (6 kl), two-tier stepped billing, three-tier stepped billing, drought restriction tariffs, litres to kilolitres conversions, step threshold boundary readings, daily per-person consumption, dripping tap wastage costs, JoJo rainwater tank savings (Subskills 19 to 27)
      * Telephone tariffs, contract subscriptions + bundle top-ups, per-second billing conversions, in-network vs cross-network rates, airtime balance deductions, data bundles vs out-of-bundle rates, SMS bundle unit savings, airtime depletion duration, peak vs off-peak rates (Subskills 28 to 35)
      * Transport tariffs, distance/zone train tickets, single vs monthly commuter pass savings, cost per trip on multi-ride cards, weekly clipcards vs daily return, scholar/student discounts, minibus taxi fare tables, e-toll highway gantry fees, private car fuel vs public transport, excess baggage charges (Subskills 36 to 44)
      * Till slips and store accounts, cash tendered and change, itemised total/subtotal audits, VAT-inclusive vs exempt foodstuffs breakdown, discount vouchers and loyalty points, store credit card statement limits, minimum monthly installment percentages, store account finance charges and service fees (Subskills 45 to 51)
  - Full step-by-step pedagogical worked solutions showing the thought process:
      Step 1: Financial / Mathematical Concept & Thought Process
      Step 2: Method Setup with explicit mark allocation [1 Mark: Method – ...]
      Step 3: Final Answer with currency/units and explicit mark allocation [1 Mark: Accuracy – ...]
  - Strict South African Rand formatting with 2 decimal places (e.g. R 1 250,00).
  - Clean LaTeX and math mode that renders seamlessly with KaTeX.
  - Strictly unique 4-option multiple-choice sets with zero duplicate choices.
  - 3-tier diagnostic pre-baked hints for scaffolded remediation.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .tariffs import DISPATCH_TABLE, SUBSKILLS


def generate(
    seed: Optional[int] = None,
    subskill: Optional[str] = None,
    archetype_index: Optional[int] = None,
    count: int = 1,
    **kwargs: Any
) -> List[Dict[str, Any]]:
    """Master generation function.
    Deterministic execution via seeded Random instance.
    Supports single generation, iteration mode by archetype_index (0..50),
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
