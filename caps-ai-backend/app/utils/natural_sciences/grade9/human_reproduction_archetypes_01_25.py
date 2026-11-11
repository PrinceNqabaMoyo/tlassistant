"""Grade 9 Natural Sciences: Term 1 - Human Reproduction (Archetypes 01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 1/03. Human reproduction.md.
Focus: Curated Campbell organ plates (Male & Female Reproductive Systems), puberty, gametogenesis, menstrual cycle, and fertilization.
"""
from __future__ import annotations

import json
import os
import random
from typing import Any, Dict, List, Optional

ANCHORS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
    "data",
    "diagram_anchors",
)


def _load_anchors(master_name: str) -> Dict[str, Any]:
    path = os.path.join(ANCHORS_DIR, f"{master_name}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


MALE_REPRO_DATA = _load_anchors("male_reproductive")
FEMALE_REPRO_DATA = _load_anchors("female_reproductive")


def _make_repro_plate_question(
    rng: random.Random,
    master: str,
    target_key: str,
    subskill_id: str,
    system_label: str,
) -> Dict[str, Any]:
    anchor_data = MALE_REPRO_DATA if master == "male_reproductive" else FEMALE_REPRO_DATA
    anchors = anchor_data["anchors"]
    target = anchors[target_key]

    candidate_keys = [k for k in anchors.keys() if k != target_key]
    rng.shuffle(candidate_keys)
    selected_keys = [target_key] + candidate_keys[:3]
    rng.shuffle(selected_keys)

    pin_letters = ["A", "B", "C", "D"]
    pins_payload = []
    target_pin = "A"

    for idx, k in enumerate(selected_keys):
        letter = pin_letters[idx]
        ref = f"{rng.randint(100000, 999999)}_{k}"
        pins_payload.append({
            "pin": letter,
            "anchor": anchors[k]["anchor"],
            "default_box": anchors[k]["default_box"],
            "side": anchors[k]["side"],
            "ref": ref,
        })
        if k == target_key:
            target_pin = letter

    diag_payload = {
        "diagram_role": "identify",
        "image_type": master,
        "master": master,
        "view": anchor_data.get("view", "pelvic_section"),
        "viewBox": anchor_data.get("viewBox", "0 0 600 480"),
        "grade_mask": "g9",
        "pins": pins_payload,
        "target_pin": target_pin,
        "target_key": target_key,
    }

    prompt = (
        f"Study the anatomical plate of the human **{system_label}**.\n\n"
        f"Which anatomical structure is indicated by **Pin {target_pin}**?"
    )
    correct = target["name"]
    distractors = [anchors[k]["name"] for k in selected_keys if k != target_key]
    options = [correct] + distractors
    rng.shuffle(options)

    sol = (
        f"**Step 1:** Locate Pin {target_pin} on the {system_label} plate.\n"
        f"**Step 2:** Review anatomical position and physiological characteristics:\n"
        f"- {target['name']}: {target['description']}\n\n"
        f"**Step 3:** The structure indicated by Pin {target_pin} is **{correct}**."
    )

    return {
        "id": f"ns9_rep_{subskill_id[:2]}_{rng.randint(100000, 999999)}",
        "subskill": subskill_id,
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": diag_payload,
        "hints": {
            "tier_1": f"Observe the position of Pin {target_pin} on the {system_label} diagram.",
            "tier_2": f"This structure is known for: {target['description'][:60]}...",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": [f"reproductive_anatomy_pin_{target_key}_misconception"],
    }


# 01. Male anatomy testis spermatogenesis plate identification
def arch_01_male_anatomy_testis_spermatogenesis_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "male_reproductive", "testis", "01_male_anatomy_testis_spermatogenesis_plate_identification", "male reproductive system")


# 02. Male anatomy scrotum thermoregulation plate identification
def arch_02_male_anatomy_scrotum_thermoregulation_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "male_reproductive", "scrotum", "02_male_anatomy_scrotum_thermoregulation_plate_identification", "male reproductive system")


# 03. Male anatomy epididymis sperm maturation plate identification
def arch_03_male_anatomy_epididymis_sperm_maturation_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "male_reproductive", "epididymis", "03_male_anatomy_epididymis_sperm_maturation_plate_identification", "male reproductive system")


# 04. Male anatomy vas deferens propulsion plate identification
def arch_04_male_anatomy_vas_deferens_propulsion_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "male_reproductive", "vas_deferens", "04_male_anatomy_vas_deferens_propulsion_plate_identification", "male reproductive system")


# 05. Male anatomy seminal vesicle fructose fluid plate identification
def arch_05_male_anatomy_seminal_vesicle_fructose_fluid_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "male_reproductive", "seminal_vesicle", "05_male_anatomy_seminal_vesicle_fructose_fluid_plate_identification", "male reproductive system")


# 06. Male anatomy prostate gland alkaline fluid plate identification
def arch_06_male_anatomy_prostate_gland_alkaline_fluid_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "male_reproductive", "prostate_gland", "06_male_anatomy_prostate_gland_alkaline_fluid_plate_identification", "male reproductive system")


# 07. Male anatomy cowpers gland neutralizing secretion plate identification
def arch_07_male_anatomy_cowpers_gland_neutralizing_secretion_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "male_reproductive", "cowpers_gland", "07_male_anatomy_cowpers_gland_neutralizing_secretion_plate_identification", "male reproductive system")


# 08. Male anatomy urethra urogenital passage plate identification
def arch_08_male_anatomy_urethra_urogenital_passage_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "male_reproductive", "urethra", "08_male_anatomy_urethra_urogenital_passage_plate_identification", "male reproductive system")


# 09. Female anatomy ovary oogenesis plate identification
def arch_09_female_anatomy_ovary_oogenesis_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "female_reproductive", "ovary", "09_female_anatomy_ovary_oogenesis_plate_identification", "female reproductive system")


# 10. Female anatomy fimbriae ovum sweep plate identification
def arch_10_female_anatomy_fimbriae_ovum_sweep_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "female_reproductive", "fimbriae", "10_female_anatomy_fimbriae_ovum_sweep_plate_identification", "female reproductive system")


# 11. Female anatomy fallopian tube fertilization site plate identification
def arch_11_female_anatomy_fallopian_tube_fertilization_site_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "female_reproductive", "fallopian_tube", "11_female_anatomy_fallopian_tube_fertilization_site_plate_identification", "female reproductive system")


# 12. Female anatomy uterus myometrium gestation plate identification
def arch_12_female_anatomy_uterus_myometrium_gestation_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "female_reproductive", "uterus_myometrium", "12_female_anatomy_uterus_myometrium_gestation_plate_identification", "female reproductive system")


# 13. Female anatomy endometrium blastocyst implantation plate identification
def arch_13_female_anatomy_endometrium_blastocyst_implantation_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "female_reproductive", "endometrium", "13_female_anatomy_endometrium_blastocyst_implantation_plate_identification", "female reproductive system")


# 14. Female anatomy cervix dilation and barrier plate identification
def arch_14_female_anatomy_cervix_dilation_and_barrier_plate_identification(rng: random.Random) -> Dict[str, Any]:
    return _make_repro_plate_question(rng, "female_reproductive", "cervix", "14_female_anatomy_cervix_dilation_and_barrier_plate_identification", "female reproductive system")


# 15. Puberty secondary sexual characteristics testosterone effects in males
def arch_15_puberty_secondary_sexual_characteristics_testosterone_effects_males(rng: random.Random) -> Dict[str, Any]:
    traits = [
        ("Deepening of the voice", "Enlargement of the larynx (Adam's apple) and elongation/thickening of vocal cords under testosterone"),
        ("Facial and body hair growth", "Stimulation of androgen receptors in hair follicles in the beard, chest, and axillary regions"),
        ("Increased muscle mass and broad shoulders", "Anabolic protein synthesis stimulated by circulating testosterone expanding skeletal muscle fibers"),
        ("Enlargement of testes and penis", "Primary and secondary maturation of external and internal genitalia triggered by LH and FSH signaling"),
    ]
    name, mechanism = rng.choice(traits)
    prompt = (
        f"During male puberty, the pituitary gland secretes gonadotropins that stimulate the testes to produce testosterone.\n\n"
        f"Which biological mechanism explains the development of **{name}**?"
    )
    correct = mechanism
    distractors = [t[1] for t in traits if t[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze male secondary sexual characteristics driven by testosterone.\n"
        f"**Step 2:** Match characteristic to physiological mechanism:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct mechanism is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_15_{rng.randint(100000, 999999)}",
        "subskill": "15_puberty_secondary_sexual_characteristics_testosterone_effects_males",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Recall the role of testosterone in causing: {name}.",
            "tier_2": "Testosterone promotes anabolic muscle growth, laryngeal enlargement, and hair follicle stimulation.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["male_puberty_testosterone_action_misconception"],
    }


# 16. Puberty secondary sexual characteristics estrogen effects in females
def arch_16_puberty_secondary_sexual_characteristics_estrogen_effects_females(rng: random.Random) -> Dict[str, Any]:
    traits = [
        ("Development of breast tissue (thelarche)", "Estrogen stimulates proliferation of glandular ductal tissue and adipose deposition in the mammary glands"),
        ("Widening of the pelvic girdle and hips", "Estrogen stimulates lateral pelvic bone remodeling to facilitate future childbirth"),
        ("Onset of the menstrual cycle (menarche)", "Cyclical hormonal surges of estrogen and progesterone driving endometrial thickening and cyclical shed"),
        ("Subcutaneous fat deposition around thighs and hips", "Estrogen shifts metabolic adipose storage patterns creating gynoid body fat distribution"),
    ]
    name, mechanism = rng.choice(traits)
    prompt = (
        f"During female puberty, the ovaries are stimulated by pituitary hormones to produce estrogen and progesterone.\n\n"
        f"Which physiological mechanism accounts for **{name}**?"
    )
    correct = mechanism
    distractors = [t[1] for t in traits if t[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review female secondary sexual maturation regulated by estrogen.\n"
        f"**Step 2:** Match feature to developmental process:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The accurate explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_16_{rng.randint(100000, 999999)}",
        "subskill": "16_puberty_secondary_sexual_characteristics_estrogen_effects_females",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Consider the physiological effects of estrogen on: {name}.",
            "tier_2": "Estrogen directs pelvic remodeling, mammary adipose development, and endometrial cyclicity.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["female_puberty_estrogen_action_misconception"],
    }


# 17. Gametogenesis spermatogenesis vs oogenesis comparison
def arch_17_gametogenesis_spermatogenesis_vs_oogenesis_comparison(rng: random.Random) -> Dict[str, Any]:
    params = [
        (
            "gamete yield per meiotic division",
            "Spermatogenesis produces 4 functional equal-sized haploid spermatozoa, whereas oogenesis yields only 1 functional haploid ovum plus 2-3 non-functional polar bodies",
            "Spermatogenesis produces 1 sperm cell and 3 polar bodies, while oogenesis produces 4 functional ova",
            "Both processes produce exactly 2 diploid gametes per meiotic cycle",
        ),
        (
            "timing of onset and duration across lifespan",
            "Spermatogenesis begins at puberty and continues continuously throughout life until old age, whereas oogenesis initiates before birth, arrests in prophase I, and ceases at menopause",
            "Spermatogenesis begins in the fetus and stops at puberty, while oogenesis begins only at menopause",
            "Both processes begin at birth and run uninterrupted every single 28 days until age 70",
        ),
        (
            "cytoplasmic division (cytokinesis)",
            "Spermatogenesis features equal cytoplasmic division yielding streamlined motile cells, whereas oogenesis features extremely unequal cytokinesis reserving all nutrient yolk inside the ovum",
            "Oogenesis divides cytoplasm equally while spermatogenesis discards 90% of cellular material as polar bodies",
            "Neither gamete retains cytoplasm; both become naked nuclear chromatin shells",
        ),
    ]
    feature, correct, d1, d2 = rng.choice(params)
    prompt = (
        f"Gametogenesis is the specialized meiotic process producing haploid gametes in the gonads.\n\n"
        f"Which statement accurately contrasts spermatogenesis and oogenesis regarding **{feature}**?"
    )
    d3 = "Spermatozoa and ova are formed by identical mitotic binary fission in somatic epithelial tissues."
    options = [correct, d1, d2, d3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare gametogenesis pathways regarding {feature}.\n"
        f"**Step 2:** Confirm biological facts:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The correct comparison is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_17_{rng.randint(100000, 999999)}",
        "subskill": "17_gametogenesis_spermatogenesis_vs_oogenesis_comparison",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Think about how {feature} differs between testes and ovaries.",
            "tier_2": "Sperm are small, continuous, and fourfold; eggs are large, solitary per cycle, and stock nutrients.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["gametogenesis_spermatogenesis_oogenesis_comparison_misconception"],
    }


# 18. Human life cycle chromosome numbers diploid zygote vs haploid gametes
def arch_18_human_life_cycle_chromosome_numbers_diploid_zygote_vs_haploid_gametes(rng: random.Random) -> Dict[str, Any]:
    cells = [
        ("Sperm cell", "haploid (n)", 23, "Contains a single set of unpaired chromosomes produced by meiosis"),
        ("Secondary oocyte (ovum)", "haploid (n)", 23, "Female sex cell containing one complete maternal chromosome set"),
        ("Zygote", "diploid (2n)", 46, "Formed by the fusion of paternal (n=23) and maternal (n=23) pronuclei at fertilization"),
        ("Somatic body cell (e.g. skin or liver cell)", "diploid (2n)", 46, "Contains 23 homologous pairs replicated through mitosis"),
    ]
    name, ploidy, count, reason = rng.choice(cells)
    prompt = (
        f"In the human sexual life cycle, the alternation of meiosis and fertilization maintains a constant chromosome number across generations.\n\n"
        f"What is the ploidy level and total chromosome count of a normal human **{name}**?"
    )
    correct = f"{ploidy} with {count} chromosomes ({reason})."
    options = [
        correct,
        f"diploid (2n) with 23 chromosomes (Contains 23 pairs that duplicate during cytokinesis).",
        f"haploid (n) with 46 chromosomes (Double the normal gametic count).",
        f"triploid (3n) with 69 chromosomes (Formed by three gametic pronuclei).",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify cell type: {name}.\n"
        f"**Step 2:** Determine ploidy and chromosome number:\n"
        f"- Gametes (sperm/ovum): n = 23 (haploid).\n"
        f"- Zygote and somatic cells: 2n = 46 (diploid).\n\n"
        f"**Step 3:** The correct description is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_18_{rng.randint(100000, 999999)}",
        "subskill": "18_human_life_cycle_chromosome_numbers_diploid_zygote_vs_haploid_gametes",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Is a {name.lower()} a gamete (n) or a body cell / zygote (2n)?",
            "tier_2": "Gametes have 23 chromosomes (haploid, n); zygotes and body cells have 46 (diploid, 2n).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ploidy_chromosome_number_diploid_haploid_misconception"],
    }


# 19. Sperm cell specialized structure acrosome midpiece flagellum
def arch_19_sperm_cell_specialized_structure_acrosome_midpiece_flagellum(rng: random.Random) -> Dict[str, Any]:
    parts = [
        ("Acrosome (cap of head)", "Contains hydrolytic digestive enzymes that dissolve the protective jelly coat (corona radiata and zona pellucida) of the ovum"),
        ("Head (nucleus)", "Houses the condensed haploid paternal genome of 23 chromosomes to combine with maternal DNA"),
        ("Midpiece (middle section)", "Tightly packed with spiral mitochondria generating ATP energy to power swimming locomotion"),
        ("Tail (flagellum)", "Long contractile microtubular whip that propels the sperm forward through fluid in the female reproductive tract"),
    ]
    part_name, fn = rng.choice(parts)
    prompt = (
        f"The mature human spermatozoon is a highly specialized cellular projectile adapted for swimming toward and penetrating an ovum.\n\n"
        f"What is the specialized function of the sperm **{part_name}**?"
    )
    correct = fn
    distractors = [p[1] for p in parts if p[0] != part_name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze spermatozoon structural adaptations.\n"
        f"**Step 2:** Relate {part_name} to its specialized role:\n"
        f"- {part_name}: {correct}\n\n"
        f"**Step 3:** The correct functional adaptation is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_19_{rng.randint(100000, 999999)}",
        "subskill": "19_sperm_cell_specialized_structure_acrosome_midpiece_flagellum",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Think about what the {part_name} contains and why it is needed.",
            "tier_2": "Acrosome = enzymes; Midpiece = mitochondria for ATP; Tail = flagellum for swimming; Head = haploid nucleus.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["sperm_cell_structural_specialization_misconception"],
    }


# 20. Ovum structure corona radiata zona pellucida cytoplasm
def arch_20_ovum_structure_corona_radiata_zona_pellucida_cytoplasm(rng: random.Random) -> Dict[str, Any]:
    layers = [
        ("Corona radiata", "Outer protective mantle of follicle (granulosa) cells nourishing the egg during ovulation and acting as the first barrier to sperm"),
        ("Zona pellucida", "Thick extracellular glycoprotein coat that binds species-specific sperm and hardens immediately after fertilization (cortical reaction) to prevent polyspermy"),
        ("Nutrient-rich cytoplasm (yolk/ooplasm)", "Abundant food reserves, organelles, and enzymes supporting the dividing blastocyst before uterine implantation"),
        ("Cortical granules", "Specialized secretory vesicles beneath the plasma membrane that exocytose enzymes to cross-link the zona pellucida upon sperm entry"),
    ]
    layer_name, desc = rng.choice(layers)
    prompt = (
        f"The human ovum is one of the largest cells in the human body, engineered to receive genetic material and support early embryonic cleavage.\n\n"
        f"What is the functional role of the **{layer_name}** surrounding the ovum?"
    )
    correct = desc
    distractors = [l[1] for l in layers if l[0] != layer_name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review ovum anatomy and protective coats.\n"
        f"**Step 2:** Match {layer_name} to its biological purpose:\n"
        f"- {layer_name}: {correct}\n\n"
        f"**Step 3:** The correct functional role is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_20_{rng.randint(100000, 999999)}",
        "subskill": "20_ovum_structure_corona_radiata_zona_pellucida_cytoplasm",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Recall the protective layers around the ovum: {layer_name}.",
            "tier_2": "Corona radiata is outer follicle cells; Zona pellucida is the glycoprotein matrix blocking polyspermy.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ovum_protective_layer_and_cortical_reaction_misconception"],
    }


# 21. Menstrual cycle four phases menstruation follicular ovulation luteal
def arch_21_menstrual_cycle_four_phases_menstruation_follicular_ovulation_luteal(rng: random.Random) -> Dict[str, Any]:
    phases = [
        (
            "Menstrual phase (Days 1-5)",
            "Sloughing and shedding of the functional endometrium accompanied by bleeding due to falling progesterone and estrogen levels",
            "Days 1 to 5",
        ),
        (
            "Follicular / Proliferative phase (Days 6-13)",
            "Under pituitary FSH stimulation, an ovarian follicle matures and secretes estrogen, stimulating rapid mitotic repair and vascularization of the endometrium",
            "Days 6 to 13",
        ),
        (
            "Ovulation phase (Day 14)",
            "A sharp surge in pituitary Luteinizing Hormone (LH) triggers the rupture of the Graafian follicle and release of the secondary oocyte into the fallopian tube",
            "Day 14 (in a standard 28-day cycle)",
        ),
        (
            "Luteal / Secretory phase (Days 15-28)",
            "The ruptured follicle collapses into the corpus luteum, which secretes high progesterone to prepare the thickened spongy endometrium for blastocyst implantation",
            "Days 15 to 28",
        ),
    ]
    name, events, timing = rng.choice(phases)
    prompt = (
        f"In a standard 28-day human menstrual cycle, synchronized cyclical changes occur simultaneously in the ovaries and uterus.\n\n"
        f"Which clinical sequence of biological events defines the **{name}**?"
    )
    correct = events
    distractors = [p[1] for p in phases if p[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze events of the menstrual cycle phase: {name}.\n"
        f"**Step 2:** Confirm cycle characteristics:\n"
        f"- Timing: {timing}\n"
        f"- Key biological event: {correct}\n\n"
        f"**Step 3:** The correct sequence of events is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_21_{rng.randint(100000, 999999)}",
        "subskill": "21_menstrual_cycle_four_phases_menstruation_follicular_ovulation_luteal",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"What happens in the ovary and uterine lining during the {name}?",
            "tier_2": "Days 1-5 shed lining; Days 6-13 estrogen rebuilds; Day 14 LH surge causes ovulation; Days 15-28 corpus luteum secretes progesterone.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["menstrual_cycle_four_phases_timing_misconception"],
    }


# 22. Hormonal regulation fsh and lh pituitary gonadotropins
def arch_22_hormonal_regulation_fsh_and_lh_pituitary_gonadotropins(rng: random.Random) -> Dict[str, Any]:
    hormones = [
        (
            "Follicle Stimulating Hormone (FSH)",
            "Anterior pituitary gland",
            "Stimulates primordial ovarian follicles to grow and mature in females; stimulates spermatogenesis in seminiferous tubules in males",
        ),
        (
            "Luteinizing Hormone (LH)",
            "Anterior pituitary gland",
            "Surges sharply mid-cycle to trigger follicle rupture and ovulation in females; stimulates Leydig cells to produce testosterone in males",
        ),
    ]
    h_name, source, target_action = rng.choice(hormones)
    prompt = (
        f"The anterior pituitary gland regulates reproductive cycles by secreting gonadotropic hormones.\n\n"
        f"What is the principal biological action of **{h_name}** in the human reproductive system?"
    )
    correct = f"Produced by {source}; {target_action}."
    alt = [h for h in hormones if h[0] != h_name][0]
    options = [
        correct,
        f"Produced by {alt[1]}; {alt[2]}.",
        "Produced by the adrenal cortex; directly breaks down glycogen in muscles into glucose during stressful digestion.",
        "Produced by the thyroid gland; accelerates the rate of cellular respiration across renal nephrons.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify gonadotropin hormone: {h_name}.\n"
        f"**Step 2:** Note glandular origin and target effect:\n"
        f"- Origin: {source}\n"
        f"- Effect: {target_action}\n\n"
        f"**Step 3:** The correct statement is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_22_{rng.randint(100000, 999999)}",
        "subskill": "22_hormonal_regulation_fsh_and_lh_pituitary_gonadotropins",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Is {h_name} responsible for growing the follicle or causing ovulation?",
            "tier_2": "FSH grows the follicle; LH surges on Day 14 to cause ovulation and maintain corpus luteum.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["pituitary_gonadotropins_fsh_lh_action_misconception"],
    }


# 23. Hormonal regulation estrogen and progesterone ovarian feedback
def arch_23_hormonal_regulation_estrogen_and_progesterone_ovarian_feedback(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (
            "High levels of estrogen secreted by the maturing Graafian follicle around Day 12-13",
            "Switches from negative to positive feedback on the pituitary, triggering the massive LH surge that causes ovulation",
        ),
        (
            "High levels of progesterone and estrogen secreted by the corpus luteum during the luteal phase",
            "Exerts negative feedback on the pituitary, inhibiting further secretion of FSH and LH to prevent new follicle maturation during potential pregnancy",
        ),
        (
            "Sudden degeneration of the corpus luteum around Day 27-28 in the absence of fertilization",
            "Causes a steep drop in circulating progesterone and estrogen, triggering vasoconstriction of endometrial spiral arteries and menstruation",
        ),
    ]
    situation, consequence = rng.choice(cases)
    prompt = (
        f"Ovarian hormones exert precise feedback regulation on the brain and uterine lining during the menstrual cycle.\n\n"
        f"What is the physiological consequence of: **{situation}**?"
    )
    correct = consequence
    distractors = [c[1] for c in cases if c[0] != situation]
    distractors.append("Causes direct conversion of the urinary bladder into an extra reproductive duct.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze hormonal feedback state: {situation}.\n"
        f"**Step 2:** Relate to endocrinological outcome:\n"
        f"- Result: {correct}\n\n"
        f"**Step 3:** The accurate consequence is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_23_{rng.randint(100000, 999999)}",
        "subskill": "23_hormonal_regulation_estrogen_and_progesterone_ovarian_feedback",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Recall how high progesterone affects FSH and LH.",
            "tier_2": "Progesterone inhibits FSH/LH (negative feedback); falling progesterone triggers menstruation.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ovarian_hormone_feedback_estrogen_progesterone_misconception"],
    }


# 24. Ovulation timing and fertile window calculation
def arch_24_ovulation_timing_and_fertile_window_calculation(rng: random.Random) -> Dict[str, Any]:
    cycle_length = rng.choice([26, 28, 30, 32])
    # Luteal phase is strictly 14 days
    ovulation_day = cycle_length - 14
    # Sperm survive up to 3-5 days, ovum survives 1-2 days
    fertile_start = ovulation_day - 3
    fertile_end = ovulation_day + 1
    prompt = (
        f"A woman tracks her menstrual calendar and determines that her regular cycle length is **{cycle_length} days**.\n\n"
        f"Given that the luteal (post-ovulatory) phase is consistently 14 days long, on which cycle day does **ovulation** occur, "
        f"and what is the estimated **fertile window**?"
    )
    correct = f"Ovulation occurs on Day {ovulation_day}; fertile window is approximately Days {fertile_start} to {fertile_end}."
    wrong1 = f"Ovulation occurs on Day {cycle_length // 2}; fertile window is approximately Days {cycle_length // 2 - 1} to {cycle_length // 2 + 1}."
    wrong2 = f"Ovulation occurs on Day 14 regardless of cycle length; fertile window is Days 11 to 15."
    wrong3 = f"Ovulation occurs on Day 1 of menstruation; fertile window is Days 1 to 5."
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Calculate ovulation day: Total cycle length minus 14 days of luteal phase.\n"
        f"- {cycle_length} - 14 = Day {ovulation_day}.\n"
        f"**Step 2:** Determine fertile window accounting for sperm survival (3-5 days) and ovum viability (12-24 hours):\n"
        f"- Day {ovulation_day} - 3 = Day {fertile_start}.\n"
        f"- Day {ovulation_day} + 1 = Day {fertile_end}.\n\n"
        f"**Step 3:** The correct timing is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_24_{rng.randint(100000, 999999)}",
        "subskill": "24_ovulation_timing_and_fertile_window_calculation",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Remember: Ovulation occurs 14 days BEFORE the start of the next period (Cycle length - 14).",
            "tier_2": f"For a {cycle_length}-day cycle: {cycle_length} - 14 = Day {ovulation_day}.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fertile_window_and_ovulation_calculation_misconception"],
    }


# 25. Fertilization acrosome reaction cortical reaction zygote formation
def arch_25_fertilization_acrosome_reaction_cortical_reaction_zygote_formation(rng: random.Random) -> Dict[str, Any]:
    events = [
        (
            "Acrosome reaction",
            "The sperm head releases hydrolytic digestive enzymes that break down the corona radiata and digest a path through the glycoprotein zona pellucida",
        ),
        (
            "Membrane fusion",
            "The plasma membranes of the sperm and secondary oocyte fuse, triggering the egg to immediately complete its second meiotic division",
        ),
        (
            "Cortical reaction (slow block to polyspermy)",
            "Cortical granules beneath the ovum membrane exocytose enzymes into the perivitelline space, cross-linking and hardening the zona pellucida to prevent polyspermy",
        ),
        (
            "Syngamy (pronuclei fusion)",
            "The haploid male pronucleus (n=23) fuses with the haploid female pronucleus (n=23) to establish a diploid (2n=46) single-celled zygote",
        ),
    ]
    name, detail = rng.choice(events)
    prompt = (
        f"Fertilization normally takes place in the upper third of the fallopian tube (oviduct) when a single spermatozoon fertilizes an ovum.\n\n"
        f"Which biochemical event describes the **{name}**?"
    )
    correct = detail
    distractors = [e[1] for e in events if e[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the cellular and biochemical sequence of fertilization.\n"
        f"**Step 2:** Relate {name} to its physiological mechanism:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The accurate description is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_25_{rng.randint(100000, 999999)}",
        "subskill": "25_fertilization_acrosome_reaction_cortical_reaction_zygote_formation",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"What occurs during the {name} stage of fertilization?",
            "tier_2": "Acrosome digests outer layers; cortical reaction hardens zona pellucida to block multiple sperm; syngamy fuses pronuclei.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fertilization_acrosome_cortical_reaction_polyspermy_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "01_male_anatomy_testis_spermatogenesis_plate_identification": arch_01_male_anatomy_testis_spermatogenesis_plate_identification,
    "02_male_anatomy_scrotum_thermoregulation_plate_identification": arch_02_male_anatomy_scrotum_thermoregulation_plate_identification,
    "03_male_anatomy_epididymis_sperm_maturation_plate_identification": arch_03_male_anatomy_epididymis_sperm_maturation_plate_identification,
    "04_male_anatomy_vas_deferens_propulsion_plate_identification": arch_04_male_anatomy_vas_deferens_propulsion_plate_identification,
    "05_male_anatomy_seminal_vesicle_fructose_fluid_plate_identification": arch_05_male_anatomy_seminal_vesicle_fructose_fluid_plate_identification,
    "06_male_anatomy_prostate_gland_alkaline_fluid_plate_identification": arch_06_male_anatomy_prostate_gland_alkaline_fluid_plate_identification,
    "07_male_anatomy_cowpers_gland_neutralizing_secretion_plate_identification": arch_07_male_anatomy_cowpers_gland_neutralizing_secretion_plate_identification,
    "08_male_anatomy_urethra_urogenital_passage_plate_identification": arch_08_male_anatomy_urethra_urogenital_passage_plate_identification,
    "09_female_anatomy_ovary_oogenesis_plate_identification": arch_09_female_anatomy_ovary_oogenesis_plate_identification,
    "10_female_anatomy_fimbriae_ovum_sweep_plate_identification": arch_10_female_anatomy_fimbriae_ovum_sweep_plate_identification,
    "11_female_anatomy_fallopian_tube_fertilization_site_plate_identification": arch_11_female_anatomy_fallopian_tube_fertilization_site_plate_identification,
    "12_female_anatomy_uterus_myometrium_gestation_plate_identification": arch_12_female_anatomy_uterus_myometrium_gestation_plate_identification,
    "13_female_anatomy_endometrium_blastocyst_implantation_plate_identification": arch_13_female_anatomy_endometrium_blastocyst_implantation_plate_identification,
    "14_female_anatomy_cervix_dilation_and_barrier_plate_identification": arch_14_female_anatomy_cervix_dilation_and_barrier_plate_identification,
    "15_puberty_secondary_sexual_characteristics_testosterone_effects_males": arch_15_puberty_secondary_sexual_characteristics_testosterone_effects_males,
    "16_puberty_secondary_sexual_characteristics_estrogen_effects_females": arch_16_puberty_secondary_sexual_characteristics_estrogen_effects_females,
    "17_gametogenesis_spermatogenesis_vs_oogenesis_comparison": arch_17_gametogenesis_spermatogenesis_vs_oogenesis_comparison,
    "18_human_life_cycle_chromosome_numbers_diploid_zygote_vs_haploid_gametes": arch_18_human_life_cycle_chromosome_numbers_diploid_zygote_vs_haploid_gametes,
    "19_sperm_cell_specialized_structure_acrosome_midpiece_flagellum": arch_19_sperm_cell_specialized_structure_acrosome_midpiece_flagellum,
    "20_ovum_structure_corona_radiata_zona_pellucida_cytoplasm": arch_20_ovum_structure_corona_radiata_zona_pellucida_cytoplasm,
    "21_menstrual_cycle_four_phases_menstruation_follicular_ovulation_luteal": arch_21_menstrual_cycle_four_phases_menstruation_follicular_ovulation_luteal,
    "22_hormonal_regulation_fsh_and_lh_pituitary_gonadotropins": arch_22_hormonal_regulation_fsh_and_lh_pituitary_gonadotropins,
    "23_hormonal_regulation_estrogen_and_progesterone_ovarian_feedback": arch_23_hormonal_regulation_estrogen_and_progesterone_ovarian_feedback,
    "24_ovulation_timing_and_fertile_window_calculation": arch_24_ovulation_timing_and_fertile_window_calculation,
    "25_fertilization_acrosome_reaction_cortical_reaction_zygote_formation": arch_25_fertilization_acrosome_reaction_cortical_reaction_zygote_formation,
}
