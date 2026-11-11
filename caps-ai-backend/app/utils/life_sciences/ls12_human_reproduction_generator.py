"""Life Sciences Grade 12 Term 1: Human Reproduction Dedicated Generator.

Fully grounded in:
- curriculum_docs_auto/LifeSciences_Gr12/Term 2/01. Human Reproduction.md

Subskills:
1. male_reproductive_system: Anatomy, spermatogenesis in seminiferous tubules, accessory gland secretions.
2. female_reproductive_system: Anatomy, oogenesis, ovarian follicle development, myometrium & endometrium.
3. menstrual_cycle_hormones: Hormonal interactions (FSH, estrogen, LH surge, progesterone).
4. fertilization_and_development: Acrosome reaction, zygote cleavage, blastocyst implantation, placenta & umbilical cord.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.sensory_reproductive_builders import (
    build_male_reproductive_question,
    build_female_reproductive_question,
)


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "compound",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    # Check for direct male diagram or subskill
    if subskill in ("male_reproductive", "male_anatomy", "spermatogenesis_temperature", "semen_accessory_glands"):
        sub = None if subskill in ("male_reproductive", "male_anatomy") else subskill
        return build_male_reproductive_question(actual_seed, grade=12, mode=mode, subskill=sub)

    # Check for direct female diagram or subskill
    if subskill in ("female_reproductive", "female_anatomy", "hormonal_menstrual_cycle", "fertilization_implantation"):
        sub = None if subskill in ("female_reproductive", "female_anatomy") else subskill
        return build_female_reproductive_question(actual_seed, grade=12, mode=mode, subskill=sub)

    # Deterministic 5-subskill progression across topic subskills
    ALL_SUBSKILLS = [
        "male_reproductive",
        "female_reproductive",
        "placenta_gestation",
        "gametogenesis_meiosis",
        "ovarian_cycle",
    ]
    chosen_subskill = subskill if subskill in ALL_SUBSKILLS else ALL_SUBSKILLS[actual_seed % len(ALL_SUBSKILLS)]

    if chosen_subskill == "male_reproductive":
        return build_male_reproductive_question(actual_seed, grade=12, mode=mode)
    if chosen_subskill == "female_reproductive":
        return build_female_reproductive_question(actual_seed, grade=12, mode=mode)

    if chosen_subskill == "placenta_gestation":
        scenarios = [
            (
                "Why is it essential that maternal blood and foetal blood do not mix directly across the placenta?",
                "To prevent fatal agglutination if blood groups are incompatible, and to protect delicate foetal capillaries from high maternal arterial pressure",
                [
                    "To prevent maternal antibodies from ever entering the foetal circulation",
                    "To ensure that foetal oxygen cannot diffuse backwards into the maternal bloodstream",
                    "To allow human chorionic gonadotrophin (hCG) to bypass the umbilical vein",
                ],
                "The placenta functions via diffusion across chorionic villi without direct mixing of blood pools.",
                ["placental_barrier_misunderstanding", "maternal_foetal_blood_mixing_error"],
            ),
            (
                "Which umbilical blood vessel transports oxygenated, nutrient-rich blood from the placenta to the developing foetus?",
                "Umbilical vein (one vessel)",
                [
                    "Umbilical arteries (two vessels)",
                    "Maternal uterine vein",
                    "Amniotic lymphatic duct",
                ],
                "Like the pulmonary vein, the umbilical vein carries oxygenated blood toward the foetal heart.",
                ["umbilical_vein_artery_inversion", "foetal_circulation_confusion"],
            ),
        ]
    elif chosen_subskill == "gametogenesis_meiosis":
        scenarios = [
            (
                "Compare the outcomes of spermatogenesis and oogenesis in humans. "
                "How many viable gametes are produced from a single primary spermatocyte versus a single primary oocyte?",
                "4 viable haploid spermatozoa from 1 spermatocyte; 1 viable haploid ovum (plus 3 non-functional polar bodies) from 1 oocyte",
                [
                    "1 viable spermatozoon; 4 viable ova",
                    "2 viable spermatozoa; 2 viable ova",
                    "4 diploid spermatozoa; 1 haploid ovum",
                ],
                "Unequal cytokinesis during oogenesis conserves abundant cytoplasm in one ovum while producing polar bodies.",
                ["gametogenesis_yield_inversion", "cytokinesis_polar_body_confusion"],
            ),
            (
                "What is the chromosomal number (ploidy) of a secondary spermatocyte compared to a primary spermatocyte?",
                "Secondary spermatocytes are haploid (n = 23); primary spermatocytes are diploid (2n = 46)",
                [
                    "Secondary spermatocytes are diploid (2n = 46); primary spermatocytes are tetraploid (4n = 92)",
                    "Both primary and secondary spermatocytes are haploid (n = 23)",
                    "Secondary spermatocytes are triploid (3n = 69)",
                ],
                "Meiosis I reduces the chromosome number from diploid (2n) to haploid (n).",
                ["meiosis_reduction_division_confusion", "ploidy_number_inversion"],
            ),
        ]
    else:  # ovarian_cycle
        scenarios = [
            (
                "What direct hormonal trigger causes the mature Graafian follicle to rupture and release the secondary oocyte (ovulation) on day 14?",
                "A dramatic surge in Luteinizing Hormone (LH) from the anterior pituitary",
                [
                    "A sharp drop in progesterone secretion from the corpus luteum",
                    "A sudden increase in human chorionic gonadotrophin (hCG)",
                    "A continuous decline in Follicle Stimulating Hormone (FSH)",
                ],
                "High estrogen levels produce positive feedback triggering the pre-ovulatory LH surge.",
                ["ovulation_hormonal_trigger_error", "lh_fsh_role_inversion"],
            ),
            (
                "If fertilization and implantation do not occur, what causes the onset of menstruation (shedding of the endometrium)?",
                "Degeneration of the corpus luteum causing a sharp drop in both progesterone and estrogen levels",
                [
                    "A sudden surge in LH and FSH that tears the mucosal lining",
                    "Release of digestive enzymes from unfertilized sperm cells in the uterus",
                    "Contraction of the umbilical cord cutting off oxygen to the myometrium",
                ],
                "Without hCG from an implanted blastocyst, the corpus luteum degenerates into the corpus albicans, dropping progesterone.",
                ["menstruation_trigger_misconception", "corpus_luteum_involution_error"],
            ),
        ]

    prompt, correct_ans, distractors, explanation, tags = r.choice(scenarios)
    options = [correct_ans] + distractors
    r.shuffle(options)

    return {
        "id": f"ls12_repro_{actual_seed}_{chosen_subskill}",
        "archetype": "human_reproduction_advanced",
        "topic": "Human Reproduction",
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
            "Review the timeline of the 28-day cycle and the function of the corpus luteum.",
            explanation,
            f"The correct answer is: {correct_ans}.",
        ],
        "solution_steps": [
            "Step 1: Identify the reproductive stage or cellular event.",
            f"Step 2: Recall curriculum principle: {explanation}",
            f"Step 3: Confirm correct response: {correct_ans}.",
        ],
    }
