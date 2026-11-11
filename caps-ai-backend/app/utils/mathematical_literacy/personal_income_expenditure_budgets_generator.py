"""Grade 10 Mathematical Literacy - Term 1: Personal Income, Expenditure and Budgets Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr10/Term 1/01. Personal income expenditure and budgets.md
  - curriculum_docs/Mathematical Literacy/
  - CAPS Mathematical Literacy Grade 10-12 Curriculum Standards

Features:
  - 52 distinct subskill archetypes covering:
      * Personal income streams, payslip deductions (PAYE, UIF, pension), overtime, commission, piecework, SASSA grants, Cost to Company (CTC), bonuses
      * Expenditure classification (fixed, variable, occasional), needs vs wants, percentage allocation, variable subtotal, fixed ratio, deficit cost-cutting, weekly-to-monthly food, commuter transport, prepaid electricity
      * Monthly household budgets (income total, expenditure total, surplus/deficit verdict, balanced budget savings, housing fraction, inflation adjustment, income drop rebalancing, emergency expense impact, two-earner shared contributions, zero-based budgeting)
      * Event, project & travel budgeting (catering party, ticket break-even, concert attendance sensitivity, bus travel comparison, Drakensberg hike, Matric Dance, exterior wall painting, school sports tour fundraiser)
      * Statements and variance analysis (actual vs budgeted variance, running balance ledger, bank reconciliation discrepancy, cash flow statement, retail bank charges schedule, monthly savings interest, VAT inclusive 15%, unexpected medical shortfall)
      * Small business and agricultural enterprise budgets (tomato farming enterprise, broiler chicken batch, layer hen egg cash flow, feed cost per bird margin, spaza produce stall break-even, Boer goat livestock herd, crop irrigation tanker vs JoJo rainwater)
  - Full step-by-step pedagogical worked solutions showing the thought process:
      Step 1: Financial Concept & Thought Process
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

from .budgets import DISPATCH_TABLE, SUBSKILLS

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
