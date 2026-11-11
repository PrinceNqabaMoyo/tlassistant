"""Natural Sciences Grade 9 Term 1: Human Reproduction Topic Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 1/03. Human reproduction.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. male_reproductive_system: Primary structures (testes, scrotum, sperm duct, penis, prostate).
2. female_reproductive_system: Primary structures (ovaries, fallopian tubes, uterus, endometrium, vagina).
3. menstrual_cycle_stages: 28-day cycle, Day 14 ovulation, uterine blood lining preparation and menstruation.
4. fertilization_and_placental_gestation: Copulation, zygote fusion, blastocyst implantation, placenta role, 40 weeks gestation.
5. puberty_hormones_and_contraception: Secondary sexual traits, testosterone, estrogen, condoms, HIV/STI prevention.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.sensory_reproductive_builders import (
    build_male_reproductive_question,
    build_female_reproductive_question,
)

TOPIC_NAME = "Human reproduction"
ORDERED_SUBSKILLS = [
    "male_reproductive_system",
    "female_reproductive_system",
    "menstrual_cycle_stages",
    "fertilization_and_placental_gestation",
    "puberty_hormones_and_contraception",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_repro"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any]) -> Dict[str, Any]:
    if "title" not in res or not res["title"]:
        res["title"] = "Reproductive Anatomy & Gamete Formation"
    if "question" not in res or not res["question"]:
        res["question"] = res.get("prompt") or res.get("question_text", "")
    if "prompt" not in res or not res["prompt"]:
        res["prompt"] = res.get("question") or res.get("question_text", "")
    if "marking_guide" not in res and "marking_schema" in res:
        res["marking_guide"] = res["marking_schema"]
    if "marking_schema" not in res and "marking_guide" in res:
        res["marking_schema"] = res["marking_guide"]
    res["topic"] = TOPIC_NAME
    res["grade"] = "9"
    res["term"] = 1
    return res


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "practice",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    if subskill in ("mixed", "auto", "", None):
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]
    elif subskill in ("male_reproductive", "male_anatomy", "male_reproductive_system"):
        return _normalize_res(build_male_reproductive_question(actual_seed, grade=9, mode=mode, subskill="anatomy_identification"))
    elif subskill in ("female_reproductive", "female_anatomy", "female_reproductive_system"):
        return _normalize_res(build_female_reproductive_question(actual_seed, grade=9, mode=mode, subskill="anatomy_identification"))
    elif subskill in ORDERED_SUBSKILLS:
        chosen_subskill = subskill
    else:
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]

    # Subskill 1: Male Reproductive Anatomy Diagram (Role L)
    if chosen_subskill == "male_reproductive_system":
        return _normalize_res(build_male_reproductive_question(actual_seed, grade=9, mode=mode, subskill="anatomy_identification"))

    # Subskill 2: Female Reproductive Anatomy Diagram (Role L)
    if chosen_subskill == "female_reproductive_system":
        return _normalize_res(build_female_reproductive_question(actual_seed, grade=9, mode=mode, subskill="anatomy_identification"))

    # Subskill 3: Menstrual Cycle Stages (28-Day Timeline)
    if chosen_subskill == "menstrual_cycle_stages":
        question_text = (
            "The female human reproductive cycle is an approximately 28-day hormonal cycle.\n\n"
            "1. State what happens inside the ovary on approximately **Day 14** of the menstrual cycle, and name this biological event.\n"
            "2. Describe the physiological changes that occur in the **endometrium (uterine lining)** in the days leading up to Day 14.\n"
            "3. Explain what occurs during **menstruation (Days 1–5)** if fertilization does not take place.\n"
            "4. Name the two primary ovarian hormones that regulate the thickening and shedding of the uterine lining."
        )
        sample = (
            "1. **Ovulation:** One of the ovaries releases a mature egg cell (ovum) into the Fallopian tube / oviduct;\n"
            "2. **Uterine Preparation:** Under the influence of estrogen, the endometrium thickens and develops a dense network of blood vessels to prepare for potential embryo implantation;\n"
            "3. **Menstruation:** When fertilization does not occur, progesterone and estrogen levels drop, causing the thickened blood lining of the uterus to break down and be discharged through the vagina;\n"
            "4. **Hormones:** Estrogen (Oestrogen) and Progesterone."
        )
        marking = (
            "• 1 mark: Ovulation on Day 14 [1]\n"
            "• 1 mark: Endometrium thickens / vascularises [1]\n"
            "• 2 marks: Menstruation explanation: unfertilized egg causes lining breakdown [1] and discharge through vagina [1]\n"
            "• 1 mark: Estrogen and Progesterone [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "28-Day Menstrual Cycle & Ovulation",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 1,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Day 14 is the halfway point when an ovum is released from the ovary.",
                "Menstruation happens when no pregnancy occurs, shedding the blood-rich uterine lining.",
                "Day 14: Ovulation. Uterus thickens blood layer. Menstruation: lining sheds. Hormones: Estrogen & Progesterone.",
            ],
            "misconception_tags": ["ovulation_day_miscalculation", "menstruation_fertilization_confusion"],
            "learning_objective_id": "NS9.LL.03.03",
        }

    # Subskill 4: Fertilization and Placental Gestation
    if chosen_subskill == "fertilization_and_placental_gestation":
        question_text = (
            "Human pregnancy involves fertilization, implantation, and gestation.\n\n"
            "1. State the **exact site in the female reproductive tract** where fertilization typically occurs.\n"
            "2. Define the term **zygote**.\n"
            "3. Describe the vital physiological role played by the **placenta** during embryonic and foetal development.\n"
            "4. State the normal duration of human gestation in **weeks**."
        )
        sample = (
            "1. **Site of Fertilization:** Fallopian tube (oviduct);\n"
            "2. **Zygote:** The single diploid cell produced by the fusion of the nucleus of a male sperm cell and a female egg cell (ovum);\n"
            "3. **Role of Placenta:** Connects the developing foetus to the uterine wall, allowing diffusion of oxygen, glucose, and nutrients from maternal blood to foetal blood, and diffusing metabolic wastes (carbon dioxide, urea) from foetal blood into maternal blood without mixing the blood supplies;\n"
            "4. **Gestation Period:** Approximately 40 weeks (or 9 calendar months / 280 days)."
        )
        marking = (
            "• 1 mark: Fallopian tube / oviduct (NOT uterus) [1]\n"
            "• 1 mark: Zygote is the fertilized egg / fusion of sperm and ovum nuclei [1]\n"
            "• 2 marks: Placenta exchanges nutrients/oxygen [1] and removes foetal wastes (CO2/urea) without blood mixing [1]\n"
            "• 1 mark: 40 weeks [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Fertilization, Implantation & Placental Exchange",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 1,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Fertilization happens in the Fallopian tube before the fertilized egg implants in the uterus.",
                "The placenta allows diffusion of oxygen and nutrients into the foetus, and takes away wastes.",
                "Site: Fallopian tube. Zygote: fertilized egg. Placenta: nutrient/gas exchange without blood mixing. Gestation: 40 weeks.",
            ],
            "misconception_tags": ["fertilization_in_uterus_myth", "maternal_fetal_blood_mixing_misconception"],
            "learning_objective_id": "NS9.LL.03.04",
        }

    # Subskill 5: Puberty, Hormones & Contraception
    hormone_traits = [
        ("Testosterone", "Testes", "Deepening of the voice, growth of facial/body hair, enlargement of penis/testes, sperm production"),
        ("Estrogen (Oestrogen)", "Ovaries", "Enlargement of breasts, widening of hips, initiation of the menstrual cycle, pubic hair growth"),
    ]
    ht = hormone_traits[actual_seed % len(hormone_traits)]
    question_text = (
        "Puberty is triggered by hormones released from the endocrine system, and reproductive health involves contraception.\n\n"
        f"1. Name the master gland at the base of the brain that initiates puberty.\n"
        f"2. State where the sex hormone **{ht[0]}** is produced, and list **two secondary sexual characteristics** it triggers.\n"
        "3. Explain why the male/female **condom** is unique among contraceptive methods in terms of health protection.\n"
        "4. Describe the danger of consuming alcohol or smoking tobacco during pregnancy."
    )
    sample = (
        "1. **Master Gland:** Pituitary Gland;\n"
        f"2. **Site of Production:** {ht[1]}; **Secondary Characteristics:** {ht[2]};\n"
        "3. **Dual Protection of Condoms:** In addition to preventing unintended pregnancy by physically blocking sperm, condoms are the only contraceptive method that provides a barrier preventing the transmission of Sexually Transmitted Diseases (STDs) such as HIV/AIDS;\n"
        "4. Alcohol passes through the placenta into foetal circulation causing Fetal Alcohol Syndrome (FAS) and brain damage; nicotine from tobacco constricts placental blood vessels, reducing oxygen delivery and leading to low birth weight or premature birth."
    )
    marking = (
        "• 1 mark: Pituitary gland [1]\n"
        f"• 2 marks: Produced in {ht[1]} [1]; two secondary sexual characteristics stated [1]\n"
        "• 1 mark: Condom provides dual protection against both pregnancy and STDs/HIV [1]\n"
        "• 1 mark: Alcohol/smoking causes FAS / brain damage / reduced oxygen delivery [1]\n"
        "**Total: 5 marks**"
    )
    return {
        "title": "Puberty Hormones & Barrier Contraception",
        "topic": TOPIC_NAME,
        "grade": "9",
        "term": 1,
        "subskill": chosen_subskill,
        "question_type": "structured",
        "prompt": question_text,
        "question": question_text,
        "sample_answer": sample,
        "marking_guide": marking,
        "hints": [
            "The pituitary gland in the brain triggers hormone release at puberty.",
            "Condoms act as a physical barrier against both sperm and pathogens like HIV.",
            "Pituitary gland; sex hormone site; condoms prevent STDs and pregnancy; alcohol causes FAS.",
        ],
        "misconception_tags": ["contraceptive_pill_prevents_hiv_myth", "puberty_hormone_origin_error"],
        "learning_objective_id": "NS9.LL.03.05",
    }
