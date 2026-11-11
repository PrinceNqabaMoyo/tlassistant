"""Natural Sciences Grade 9 Term 1: Human Reproduction Topic Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 1/03. Human reproduction.md

Subskills:
1. male_reproductive_system: Primary structures (testes, scrotum, sperm duct, penis, prostate).
2. female_reproductive_system: Primary structures (ovaries, fallopian tubes, uterus, vagina).
3. puberty_and_hormones: Secondary sexual characteristics, testosterone, and estrogen.
4. contraception_and_stis: Barrier methods, hormonal contraception, prevention of STIs (HIV/AIDS).
5. fertilization_and_pregnancy: Gamete fusion, gestation period (~40 weeks), and embryo nourishment.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.sensory_reproductive_builders import (
    build_male_reproductive_question,
    build_female_reproductive_question,
)


SUBSKILLS = [
    "male_reproductive",
    "female_reproductive",
    "puberty_and_hormones",
    "contraception_and_stis",
    "pregnancy_gestation",
]


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "compound",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    if subskill in ("mixed", "auto", "", None):
        chosen_subskill = SUBSKILLS[actual_seed % len(SUBSKILLS)]
    else:
        chosen_subskill = subskill

    # Check for direct male diagram or subskill
    if chosen_subskill in ("male_reproductive", "male_anatomy", "male_reproductive_system"):
        return build_male_reproductive_question(actual_seed, grade=9, mode=mode, subskill="anatomy_identification")

    # Check for direct female diagram or subskill
    if chosen_subskill in ("female_reproductive", "female_anatomy", "female_reproductive_system"):
        return build_female_reproductive_question(actual_seed, grade=9, mode=mode, subskill="anatomy_identification")

    # Conceptual Subskills: puberty_and_hormones, contraception_and_stis, pregnancy_gestation
    subskills_pool = ["puberty_and_hormones", "contraception_and_stis", "pregnancy_gestation"]
    if chosen_subskill not in subskills_pool:
        chosen_subskill = subskills_pool[actual_seed % len(subskills_pool)]

    if chosen_subskill == "puberty_and_hormones":
        scenarios = [
            (
                "During puberty, the pituitary gland releases hormones that stimulate the gonads. "
                "Which hormone secreted by the testes triggers the development of male secondary sexual characteristics "
                "(such as deepening of voice, facial hair, and muscle enlargement)?",
                "Testosterone",
                [
                    "Estrogen",
                    "Progesterone",
                    "Insulin",
                ],
                "Testosterone is the primary male sex hormone produced by the interstitial cells of the testes.",
                ["hormone_gonad_mismatch", "puberty_hormone_confusion"],
            ),
            (
                "Which hormone produced by the ovaries during puberty triggers female secondary sexual characteristics, "
                "such as breast enlargement, widening of hips, and onset of the menstrual cycle?",
                "Estrogen (Oestrogen)",
                [
                    "Testosterone",
                    "Adrenaline",
                    "Thyroxine",
                ],
                "Estrogen drives the development of female secondary sexual characteristics during puberty.",
                ["estrogen_function_misidentification", "female_puberty_hormone_error"],
            ),
        ]
    elif chosen_subskill == "contraception_and_stis":
        scenarios = [
            (
                "Which contraceptive method provides dual protection by both preventing unintended pregnancy "
                "AND significantly reducing the transmission of Sexually Transmitted Infections (STIs), including HIV?",
                "Condoms (male or female latex barrier)",
                [
                    "Oral contraceptive birth control pills",
                    "Intrauterine contraceptive device (IUD)",
                    "Calendar/rhythm rhythm method",
                ],
                "Only barrier methods like condoms prevent the exchange of infective bodily fluids.",
                ["barrier_vs_hormonal_contraception_confusion", "sti_prevention_misconception"],
            ),
            (
                "How does the oral contraceptive pill prevent pregnancy in females?",
                "It supplies synthetic estrogen and progesterone to prevent ovulation (release of an egg) from the ovaries",
                [
                    "It physically blocks sperm from entering the vagina",
                    "It destroys sperm cells using acidic chemicals in the uterus",
                    "It causes permanent closure of the Fallopian tubes",
                ],
                "Hormonal pills suppress FSH and LH release from the pituitary, preventing follicle maturation and ovulation.",
                ["contraceptive_mechanism_error", "hormonal_pill_misunderstanding"],
            ),
        ]
    else:  # pregnancy_gestation
        scenarios = [
            (
                "Approximately how long is the normal human gestation (pregnancy) period from fertilization to birth?",
                "40 weeks (approx. 9 calendar months / 280 days)",
                [
                    "24 weeks (approx. 5 months)",
                    "52 weeks (approx. 12 months)",
                    "16 weeks (approx. 4 months)",
                ],
                "Full-term human gestation averages 40 weeks calculated from the last menstrual period.",
                ["gestation_duration_error", "pregnancy_timeline_confusion"],
            ),
            (
                "What is the function of the amniotic fluid surrounding the developing embryo inside the amniotic sac?",
                "It acts as a shock absorber protecting the foetus against mechanical jolts and stabilizes temperature",
                [
                    "It provides the embryo with direct oxygen gas through its nostrils",
                    "It absorbs all embryonic waste and eliminates it through the vagina",
                    "It stimulates the production of maternal breast milk during the first trimester",
                ],
                "Amniotic fluid provides hydraulic cushioning, allows free foetal movement, and maintains constant temperature.",
                ["amniotic_fluid_function_confusion", "shock_absorption_misconception"],
            ),
        ]

    prompt, correct_ans, distractors, explanation, tags = r.choice(scenarios)
    options = [correct_ans] + distractors
    r.shuffle(options)

    steps = [
        "Step 1: Identify the reproductive concept or anatomical adaptation.",
        f"Step 2: Recall curriculum principle: {explanation}",
        f"Step 3: Confirm correct response: {correct_ans}.",
    ]
    sol_str = "\n".join(steps)
    return {
        "id": f"ns9_repro_{actual_seed}_{chosen_subskill}",
        "archetype": "human_reproduction_intro",
        "topic": "Human reproduction",
        "subject": "Natural Sciences",
        "grade": 9,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": chosen_subskill,
        "prompt": prompt,
        "question_text": prompt,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "options": options,
        "marks": 2,
        "total_marks": 2,
        "worked_solution": sol_str,
        "canonical_solution": sol_str,
        "explanation": explanation,
        "misconception_tags": tags,
        "hints": [
            "Think about the biological mechanisms that allow the species to reproduce and survive.",
            explanation,
            f"The correct answer is: {correct_ans}.",
        ],
        "solution_steps": steps,
    }
