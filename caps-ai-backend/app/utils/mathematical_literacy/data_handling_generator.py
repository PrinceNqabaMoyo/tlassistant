"""Grade 10 Mathematical Literacy - Term 2: Data Handling Generator.

Exhaustively grounded in:
  - curriculum_docs_auto/MathematicalLiteracy_Gr10/Term 2/01. Data handling.md
  - curriculum_docs/Mathematical Literacy/
  - CAPS Mathematical Literacy Grade 10-12 Curriculum Standards

Features:
  - 52 distinct subskill archetypes covering:
      * Data handling cycle stages, population vs sample, sample bias and fairness audits, data collection instruments, questionnaire design and leading question detection, categorical vs numerical data, discrete vs continuous data, ethical protocols and informed consent (Subskills 1 to 8)
      * Tally mark conversion (bundles of 5), total sample size frequency sums (n = ∑ f), relative frequency percentages, grouped frequency intervals and modal class identification, stem-and-leaf plot interpretation, two-way contingency table reading, missing frequency reconstruction, cumulative frequency columns (Subskills 9 to 16)
      * Measures of central tendency, arithmetic mean of raw datasets, weighted mean of frequency tables, median of odd datasets ((n+1)/2), median of even datasets (middle pair average), unsorted data sorting prerequisite, mode of unimodal datasets, bimodal distributions and no-mode conditions, modal category for qualitative data, missing test score reconstruction (Subskills 17 to 25)
      * Measures of spread and quartiles, range calculation (Max − Min), range with negative temperatures (double negative addition), lower quartile (Q1), upper quartile (Q3), interquartile range (IQR = Q3 − Q1), semi-interquartile range, outlier impact on mean vs median, identifying extreme outliers, consistency comparison between groups (Subskills 26 to 34)
      * Bar graphs, histograms & graphical displays, vertical bar graph readings, compound double bar graphs, stacked component bar graphs, continuous histograms across interval bins, bar graph vs histogram distinctions (gaps vs touching), time-series line graphs and seasonal trends, broken/truncated axis audits, frequency polygon midpoint coordinates, percentage increase between bars (Subskills 35 to 43)
      * Pie charts & advanced interpretation, sector angle from percentage, percentage from sector angle, frequency from central angle, grand total population reconstruction from slice, scatter plot correlation (positive, negative, zero), line of best fit estimation, misleading 3D perspective distortion audits, Stats SA census demographic tables, summary statistic selection for skewed distributions (Subskills 44 to 52)
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

from .data_handling import DISPATCH_TABLE, SUBSKILLS


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
