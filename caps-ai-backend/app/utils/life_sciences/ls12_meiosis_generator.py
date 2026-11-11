"""Life Sciences Grade 12 Term 1: Meiosis Dedicated Generator.

Fully grounded in:
- curriculum_docs_auto/LifeSciences_Gr12/Term 1/03. Meiosis.md

Subskills:
1. prophase_i_crossing_over: Bivalent formation, non-sister chromatid exchange, chiasmata, recombinant gametes.
2. meiosis_stages_sequence: Meiosis I (reduction division: 2n → n) vs Meiosis II (equational division: n → n).
3. sources_of_variation: Crossing over in Prophase I and random independent assortment in Metaphase I.
4. nondisjunction_aneuploidy: Chromosome nondisjunction in Anaphase I/II leading to Down syndrome (Trisomy 21).
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.cytology_cell_division_builders import build_meiosis_question


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "compound",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    # Check for direct diagram subskills
    if subskill in ("meiosis_crossing_over", "crossing_over", "diagram", "diagram_label"):
        return build_meiosis_question(actual_seed, grade=12, mode=mode)

    # Deterministic 4-subskill progression across topic subskills
    ALL_SUBSKILLS = [
        "meiosis_crossing_over",
        "meiosis_i_vs_ii",
        "independent_assortment",
        "nondisjunction_mechanics",
    ]
    chosen_subskill = subskill if subskill in ALL_SUBSKILLS else ALL_SUBSKILLS[actual_seed % len(ALL_SUBSKILLS)]

    if chosen_subskill == "meiosis_crossing_over":
        return build_meiosis_question(actual_seed, grade=12, mode=mode)

    if chosen_subskill == "meiosis_i_vs_ii":
        scenarios = [
            (
                "Why is **Meiosis I** specifically classified as a **reduction division**, whereas Meiosis II is an equational division?",
                "Homologous chromosome pairs separate in Anaphase I, reducing the chromosome number from diploid (2n = 46) to haploid (n = 23)",
                [
                    "Sister chromatids separate in Anaphase I, doubling the total number of chromosomes per daughter cell",
                    "The cell loses its entire cytoplasm and all organelles during Telophase I",
                    "DNA replicates twice during the interkinesis phase between Meiosis I and II",
                ],
                "Meiosis I separates whole homologous chromosomes, halving the ploidy from 2n to n.",
                ["reduction_division_misunderstanding", "meiosis_i_ii_separation_confusion"],
            ),
            (
                "During **Anaphase II** of meiosis, what physical separation occurs within each dividing cell?",
                "Centromeres split and sister chromatids separate to opposite poles as individual daughter chromosomes",
                [
                    "Whole homologous chromosome pairs separate to opposite poles without splitting centromeres",
                    "Chiasmata form between non-homologous autosomes to exchange entire chromosome arms",
                    "Nuclear membranes dissolve permanently so chromosomes disintegrate into plasmids",
                ],
                "In Anaphase II, centromeres divide and sister chromatids are pulled apart (just like mitosis).",
                ["anaphase_i_vs_ii_inversion", "centromere_division_timing_error"],
            ),
        ]
    elif chosen_subskill == "independent_assortment":
        scenarios = [
            (
                "In addition to crossing over, how does **random arrangement (independent assortment)** of chromosomes "
                "during **Metaphase I** contribute to genetic diversity among gametes?",
                "Maternal and paternal homologous chromosomes align randomly along the equator, generating $2^n$ unique gametic combinations",
                [
                    "Chromosomes fuse together into a single giant circular DNA ring before dividing",
                    "All maternal chromosomes are forced into one daughter cell while paternal go to the other",
                    "Spindle fibers mutate specific gene codons directly as they attach to centromeres",
                ],
                "Independent assortment allows random combinations of maternal and paternal chromosomes in gametes ($2^{23}$ combinations in humans).",
                ["independent_assortment_mechanism_error", "maternal_paternal_segregation_confusion"],
            ),
            (
                "If a species has a diploid chromosome number of $2n = 6$ ($n = 3$), how many genetically different "
                "chromosome combinations are possible in its gametes purely through independent assortment (ignoring crossing over)?",
                "8 combinations ($2^3 = 8$)",
                [
                    "6 combinations ($2 \\times 3 = 6$)",
                    "36 combinations ($6^2 = 36$)",
                    "3 combinations ($n = 3$)",
                ],
                "Number of combinations = $2^n = 2^3 = 8$.",
                ["gamete_combination_formula_error", "multiplicative_ploidy_misconception"],
            ),
        ]
    else:  # nondisjunction_mechanics
        scenarios = [
            (
                "What is the cellular event termed **nondisjunction** during meiosis?",
                "Failure of homologous chromosomes to separate in Anaphase I, or sister chromatids to separate in Anaphase II",
                [
                    "Failure of the nuclear envelope to break down during Prophase I",
                    "Failure of DNA polymerase to replicate the leading strand during interphase",
                    "Over-condensation of chromatin resulting in premature cell death",
                ],
                "Nondisjunction is the failure of chromosome separation, producing gametes with $n+1$ or $n-1$ chromosomes.",
                ["nondisjunction_definition_error", "chromatid_segregation_failure_confusion"],
            ),
            (
                "A karyotype analysis reveals an individual with 47 total chromosomes, featuring an extra chromosome 21 "
                "(Trisomy 21). What condition does this person have?",
                "Down syndrome",
                [
                    "Turner syndrome (XO)",
                    "Klinefelter syndrome (XXY)",
                    "Sickle cell anaemia",
                ],
                "Trisomy 21 (Down syndrome) is caused by nondisjunction of chromosome pair 21 during gametogenesis.",
                ["aneuploidy_syndrome_mismatch", "trisomy_21_identification_error"],
            ),
        ]

    prompt, correct_ans, distractors, explanation, tags = r.choice(scenarios)
    options = [correct_ans] + distractors
    r.shuffle(options)

    return {
        "id": f"ls12_meiosis_{actual_seed}_{chosen_subskill}",
        "archetype": "meiosis_crossing_over_advanced",
        "topic": "Meiosis",
        "subject": "Life Sciences",
        "grade": 12,
        "term": 1,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 3,
        "subskill": chosen_subskill,
        "question_text": prompt,
        "correct_answer": correct_ans,
        "options": options,
        "misconception_tags": tags,
        "hints": [
            "Review the distinctions between Meiosis I and Meiosis II, and the mechanisms generating variation.",
            explanation,
            f"The correct answer is: {correct_ans}.",
        ],
        "solution_steps": [
            "Step 1: Identify the meiotic phase or chromosomal mechanism.",
            f"Step 2: Recall curriculum principle: {explanation}",
            f"Step 3: Confirm correct response: {correct_ans}.",
        ],
    }
