"""Grade 10 Mathematical Literacy - Term 1: Banking, Interest and Taxation Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr10/Term 1/02. Banking interest and taxation.md
  - curriculum_docs/Mathematical Literacy/
  - CAPS Mathematical Literacy Grade 10-12 Curriculum Standards

Features:
  - 52 distinct subskill archetypes covering:
      * Bank accounts, FICA regulations, debit vs credit cards, overdraft interest, stop orders, 32-day notice penalties, ATM/channel costs, anti-fraud PIN security (Subskills 1 to 8)
      * Bank statements, debits vs credits, missing running balance, opening balance reconstruction, fee totals, fee ratios, bounced debit orders, statement reconciliation, eWallet/InstantMoney (Subskills 9 to 17)
      * Fee schedules, sliding-scale ATM withdrawal formulas, percentage cash deposit tariffs, teller vs ATM savings, tillpoint cashout, bundled vs PAYT pricing, fee waivers, SMS alert totals, forex commissions (Subskills 18 to 25)
      * Simple interest investments, fractional year months, rate determination, duration years, hire purchase total costs, total interest paid, cash vs credit price differences, effective interest percentages, personal unsecured loans, lay-by agreements (Subskills 26 to 35)
      * Compound interest annual formula, year-by-year stepwise calculation tables, simple vs compound comparisons, interest-only subtraction, fixed deposit tiered schedules, real interest vs CPI inflation, Rule of 72 doubling time, semi-annual compounding, endowment policies (Subskills 36 to 44)
      * Value Added Tax (VAT 15%), VAT-inclusive prices, VAT-exclusive prices, VAT extraction, zero-rated basic foodstuffs on till slips, Unemployment Insurance Fund (UIF 1% + 1%), SARS personal income tax brackets, primary tax rebates, medical scheme fees tax credits (Subskills 45 to 52)
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

from .banking_tax import DISPATCH_TABLE, SUBSKILLS


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
