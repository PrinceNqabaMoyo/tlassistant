"""Grade 7 Natural Sciences: Term 1 - Sexual Reproduction (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 1/03. Sexual reproduction.md.
Focus: Human Reproduction, Puberty, Reproductive Anatomy, Gestation, and Reproductive Health.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Purpose of human reproduction species continuation
def arch_26_purpose_of_human_reproduction_species_continuation(rng: random.Random) -> Dict[str, Any]:
    years = rng.choice([70, 75, 80])
    prompt = (
        f"Individual human beings have a finite lifespan of approximately {years} years. "
        f"From an ecological and evolutionary perspective, why is sexual reproduction essential for Homo sapiens?"
    )
    correct = "It ensures the ongoing continuation of the human species, replaces aging individuals who die, and introduces genetic variation in each new generation."
    options = [
        correct,
        "It stops humans from needing cellular respiration or oxygen to survive.",
        "It converts human children into plant autotrophs that photosynthesise.",
        "It guarantees that every newborn child is an identical genetic clone of its parents.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review the biological necessity of reproduction:\n"
        f"- Reproduction is not required for an individual organism's immediate survival (an individual can live a full life without reproducing).\n"
        f"- However, reproduction is vital for SPECIES survival to prevent extinction when older generations die.\n"
        f"- Sexual reproduction mixes genetic alleles, providing diversity against diseases and environmental change.\n\n"
        f"**Step 2:** The evolutionary purpose is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_26_{rng.randint(100000, 999999)}",
        "subskill": "26_purpose_of_human_reproduction_species_continuation",
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
            "tier_1": "Think about what happens to a species if no individuals have offspring.",
            "tier_2": "Reproduction replaces dying individuals and ensures the species does not go extinct.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["individual_vs_species_survival_confusion"],
    }


# 27. Puberty definition and hormonal trigger
def arch_27_puberty_definition_and_hormonal_trigger(rng: random.Random) -> Dict[str, Any]:
    gland = "Pituitary gland (at the base of the brain)"
    hormones = [
        ("Testosterone (secreted by the testes in males)", "triggers the development of male secondary sexual characteristics and initiates active spermatogenesis (sperm production)"),
        ("Estrogen and Progesterone (secreted by the ovaries in females)", "triggers female secondary sexual characteristics, initiates the menstrual cycle, and stimulates monthly ovulation"),
    ]
    target_hormone, target_action = rng.choice(hormones)
    prompt = (
        f"Puberty is the developmental life stage during which an adolescent's body undergoes sexual and physical maturation to become capable of sexual reproduction. "
        f"Which endocrine gland initiates puberty by releasing gonadotropic hormones, and what is the specific role of '{target_hormone}'?"
    )
    correct = f"{gland} triggers hormone release; '{target_hormone}' {target_action}."
    distractors = [
        f"Thyroid gland in the neck triggers puberty; '{target_hormone}' converts body fat into pure iron metal.",
        f"Adrenal gland triggers puberty; '{target_hormone}' permanently turns off all hormone production.",
        f"Pancreas triggers puberty; '{target_hormone}' causes the skeleton to shrink by half its height.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review endocrine regulation of puberty:\n"
        f"- The pituitary gland at the base of the brain secretes FSH and LH.\n"
        f"- In males: stimulates testes to produce testosterone (sperm production, secondary traits).\n"
        f"- In females: stimulates ovaries to produce estrogen/progesterone (menstrual cycle, ovulation, secondary traits).\n\n"
        f"**Step 2:** The mechanism is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_27_{rng.randint(100000, 999999)}",
        "subskill": "27_puberty_definition_and_hormonal_trigger",
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
            "tier_1": "The master gland at the base of the brain is the pituitary gland.",
            "tier_2": "Testosterone regulates male changes; estrogen/progesterone regulate female changes.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["puberty_hormone_trigger_confusion"],
    }


# 28. Male secondary sexual characteristics
def arch_28_male_secondary_sexual_characteristics(rng: random.Random) -> Dict[str, Any]:
    traits = [
        ("Deepening of the voice (voice breaking)", "the larynx (voice box) enlarges and vocal cords lengthen and thicken under testosterone stimulation"),
        ("Broadening of the shoulders and increased muscle mass", "testosterone acts as an anabolic steroid promoting skeletal muscle protein synthesis"),
        ("Growth of facial, chest, and pubic hair", "hair follicles in androgen-sensitive dermal zones respond to rising circulatory testosterone"),
        ("Enlargement of the testes, scrotum, and penis with commencement of sperm production", "maturation of seminiferous tubules and Leydig cells in the gonads"),
    ]
    trait_name, bio_explanation = rng.choice(traits)
    prompt = (
        f"During male puberty, rising testosterone levels drive distinctive physical changes. "
        f"What is the biological explanation for '{trait_name}' in adolescent boys?"
    )
    correct = bio_explanation
    options = [bio_explanation] + [t[1] for t in traits if t[1] != bio_explanation]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review male secondary sexual characteristics:\n"
        f"- Voice deepening (laryngeal enlargement).\n"
        f"- Shoulder broadening and muscle growth.\n"
        f"- Facial/body/pubic hair growth.\n"
        f"- Genital growth and onset of sperm production.\n\n"
        f"**Step 2:** For '{trait_name}', the explanation is: **{bio_explanation}**."
    )
    return {
        "id": f"ns7_sr_28_{rng.randint(100000, 999999)}",
        "subskill": "28_male_secondary_sexual_characteristics",
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
            "tier_1": "Match the physical male trait to what testosterone does in that body part.",
            "tier_2": "Voice changes are caused by larynx growth; muscle growth by protein synthesis.",
            "tier_3": f"The answer is: {bio_explanation}.",
        },
        "misconception_tags": ["male_puberty_trait_confusion"],
    }


# 29. Female secondary sexual characteristics
def arch_29_female_secondary_sexual_characteristics(rng: random.Random) -> Dict[str, Any]:
    traits = [
        ("Development of breast tissue and enlargement of nipples", "estrogen stimulates the growth of mammary ducts and the deposition of adipose fat tissue"),
        ("Widening of the hips and pelvic girdle", "adaptation to prepare the skeletal birth canal for pregnancy and future delivery of a baby"),
        ("Onset of menstruation (menarche)", "the cyclical monthly shedding of the vascularized uterine endometrium lining when pregnancy has not occurred"),
        ("Growth of pubic and underarm hair", "maturation of adrenal and ovarian androgen pathways during adolescent development"),
    ]
    trait_name, bio_explanation = rng.choice(traits)
    prompt = (
        f"During female puberty, estrogen and progesterone trigger key physical milestones. "
        f"What is the biological significance of '{trait_name}' in adolescent girls?"
    )
    correct = bio_explanation
    options = [bio_explanation] + [t[1] for t in traits if t[1] != bio_explanation]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review female secondary sexual characteristics:\n"
        f"- Breast development (mammary duct proliferation and fat deposition).\n"
        f"- Pelvic widening (adaptation for childbearing).\n"
        f"- Menarche (first menstrual period; onset of reproductive capability).\n"
        f"- Pubic and axillary hair.\n\n"
        f"**Step 2:** For '{trait_name}', the significance is: **{bio_explanation}**."
    )
    return {
        "id": f"ns7_sr_29_{rng.randint(100000, 999999)}",
        "subskill": "29_female_secondary_sexual_characteristics",
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
            "tier_1": "Match the female physical trait to its biological purpose.",
            "tier_2": "Hips widen for childbearing; breasts develop for nursing; menstruation signals reproductive cycling.",
            "tier_3": f"The answer is: {bio_explanation}.",
        },
        "misconception_tags": ["female_puberty_trait_confusion"],
    }


# 30. Growth spurt curve graph interpretation
def arch_30_growth_spurt_curve_graph_interpretation(rng: random.Random) -> Dict[str, Any]:
    girl_peak_age = rng.choice([11, 12])
    boy_peak_age = rng.choice([14, 15])
    girl_rate = rng.randint(8, 10)
    boy_rate = rng.randint(9, 12)

    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 460 220' width='100%' height='220'>"
        f"<rect width='460' height='220' fill='#F8FAFC' rx='8'/>"
        f"<line x1='50' y1='180' x2='420' y2='180' stroke='#334155' stroke-width='2'/>"
        f"<line x1='50' y1='180' x2='50' y2='20' stroke='#334155' stroke-width='2'/>"
        f"<text x='235' y='210' fill='#1E293B' font-size='11' font-weight='bold' text-anchor='middle'>Age (Years)</text>"
        f"<text x='15' y='100' fill='#1E293B' font-size='10' font-weight='bold' transform='rotate(-90 15,100)' text-anchor='middle'>Growth Rate (cm/yr)</text>"
        f"<path d='M 50 140 Q 150 120, {50 + (girl_peak_age-8)*25} {180 - girl_rate*12} Q 250 140, 400 170' fill='none' stroke='#DB2777' stroke-width='3'/>"
        f"<text x='{50 + (girl_peak_age-8)*25}' y='{170 - girl_rate*12}' fill='#BE185D' font-size='10' font-weight='bold'>Girls Peak ({girl_peak_age} yrs, {girl_rate} cm/yr)</text>"
        f"<path d='M 50 150 Q 180 130, {50 + (boy_peak_age-8)*25} {180 - boy_rate*12} Q 350 150, 400 175' fill='none' stroke='#2563EB' stroke-width='3'/>"
        f"<text x='{50 + (boy_peak_age-8)*25}' y='{170 - boy_rate*12}' fill='#1D4ED8' font-size='10' font-weight='bold'>Boys Peak ({boy_peak_age} yrs, {boy_rate} cm/yr)</text>"
        f"</svg>"
    )
    prompt = (
        f"In human development, adolescent growth spurt velocity graphs track annual height increase against age. "
        f"According to standard human biological growth curves, girls reach their peak growth velocity earlier (around age {girl_peak_age}) "
        f"while boys reach their peak later (around age {boy_peak_age}). "
        f"What valid conclusion can be drawn regarding adolescent growth timing between sexes?"
    )
    correct = f"Girls typically initiate and peak their adolescent growth spurt approximately 2 to 3 years earlier than boys, although boys maintain a higher peak growth velocity ({boy_rate} cm/yr) and grow for a longer overall duration into late adolescence."
    options = [
        correct,
        "Boys complete their entire growth spurt before age 8, while girls continue growing until age 45.",
        "Both boys and girls grow at the exact identical growth rate on every single day of their lives.",
        "Adolescent growth spurts only happen when individuals drink pure sugar syrup daily.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze adolescent growth spurt curves:\n"
        f"- Girls peak earlier (~age {girl_peak_age}), driven by earlier onset of puberty.\n"
        f"- Boys peak later (~age {boy_peak_age}) with a slightly higher peak velocity ({boy_rate} cm/yr) and longer growth duration, resulting in greater average adult height.\n\n"
        f"**Step 2:** The valid conclusion is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_30_{rng.randint(100000, 999999)}",
        "subskill": "30_growth_spurt_curve_graph_interpretation",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "hints": {
            "tier_1": "Look at the ages on the graph: girls peak around 11-12, boys around 14-15.",
            "tier_2": "Girls begin their growth spurt earlier; boys start later and grow for longer.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["growth_spurt_timing_inversion"],
    }


# 31. Emotional and psychological changes during puberty
def arch_31_emotional_and_psychological_changes_during_puberty(rng: random.Random) -> Dict[str, Any]:
    changes = [
        ("Intense mood fluctuations and emotional sensitivity", "rapidly fluctuating concentrations of sex hormones (testosterone, estrogen) interacting with neurotransmitters in the developing adolescent brain"),
        ("Heightened self-consciousness and body image awareness", "rapid physical bodily changes (acne, height spurts, body shape) leading teenagers to compare themselves against peers and media standards"),
        ("Seeking greater independence and peer group acceptance", "normal psychological maturation transitioning from parental dependence toward developing an individual self-identity and social autonomy"),
    ]
    phenomenon, cause = rng.choice(changes)
    prompt = (
        f"Puberty involves major psychological and emotional development alongside physical maturation. "
        f"Why is '{phenomenon}' considered a completely normal aspect of adolescent development?"
    )
    correct = f"Because {cause.lower()}."
    distractors = [
        "Because it is a dangerous mental illness that requires lifelong hospitalization.",
        "Because human teenagers are possessed by magical spirits during puberty.",
        "Because the brain temporarily shuts down all thinking until age 25.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review psychological changes during puberty:\n"
        f"- Hormonal surges affect limbic brain centers, causing emotional intensity.\n"
        f"- Physical changes trigger self-reflection and peer-orientation.\n"
        f"- These transitions are completely normal developmental milestones.\n\n"
        f"**Step 2:** For '{phenomenon}', the cause is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_31_{rng.randint(100000, 999999)}",
        "subskill": "31_emotional_and_psychological_changes_during_puberty",
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
            "tier_1": "Remember that emotional changes during puberty are normal biological reactions.",
            "tier_2": "Hormone fluctuations and brain development explain mood swings and independence seeking.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["adolescent_emotional_pathologizing"],
    }


# 32. Male reproductive organs testes and scrotum
def arch_32_male_reproductive_organs_testes_and_scrotum(rng: random.Random) -> Dict[str, Any]:
    temp_diff = rng.choice([2, 3])
    prompt = (
        f"In human males, the testes are suspended outside the abdominal pelvic cavity within a sac of skin called the scrotum. "
        f"Why is it biologically vital that the testes are maintained at approximately {temp_diff}°C to 3°C BELOW core body temperature (37°C)?"
    )
    correct = "Because normal spermatogenesis (production of healthy, motile sperm cells) cannot take place at normal internal core body temperature; excessive heat damages developing sperm."
    options = [
        correct,
        "Because lower temperatures freeze sperm cells into solid ice cubes so they do not swim away.",
        "Because the scrotum absorbs sunlight through skin to photosynthesise carbohydrates.",
        "Because warm temperatures cause testosterone to turn into poisonous hydrochloric acid.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand scrotal thermoregulation:\n"
        f"- Spermatogenesis in seminiferous tubules is heat-sensitive.\n"
        f"- Core body temperature (37°C) inhibits viable sperm production.\n"
        f"- The scrotum keeps the testes ~{temp_diff}°C cooler, contracting closer to the body in cold and relaxing away in heat.\n\n"
        f"**Step 2:** The biological reason is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_32_{rng.randint(100000, 999999)}",
        "subskill": "32_male_reproductive_organs_testes_and_scrotum",
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
            "tier_1": "Why are testes outside the body? Think about temperature.",
            "tier_2": "Sperm cannot develop properly at normal 37°C body temperature; they need cooler conditions.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["scrotal_thermoregulation_misconception"],
    }


# 33. Male reproductive organs epididymis and vas deferens
def arch_33_male_reproductive_organs_epididymis_and_vas_deferens(rng: random.Random) -> Dict[str, Any]:
    structures = [
        ("Epididymis", "a tightly coiled crescent-shaped tube capping the posterior testis where immature sperm are stored for several weeks to mature, gain motility, and acquire fertilising capacity"),
        ("Vas deferens (sperm duct)", "a muscular muscular tube that propels mature sperm by peristaltic contractions from the epididymis up into the pelvic cavity toward the urethra during ejaculation"),
    ]
    target, function = rng.choice(structures)
    alt = structures[1] if target == structures[0] else structures[0]
    prompt = (
        f"In the male reproductive tract, what is the specific anatomical role of the '{target[0]}'?"
    )
    correct = function
    options = [
        function,
        alt[1],
        "Produces estrogen and progesterone to trigger the onset of female menstruation.",
        "Filters urea out of blood to produce acidic urine.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace the sperm pathway:\n"
        f"- Seminiferous tubules (testes) -> Epididymis (maturation/storage) -> Vas deferens (transport during ejaculation) -> Urethra.\n\n"
        f"**Step 2:** For '{target[0]}', the role is: **{function}**."
    )
    return {
        "id": f"ns7_sr_33_{rng.randint(100000, 999999)}",
        "subskill": "33_male_reproductive_organs_epididymis_and_vas_deferens",
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
            "tier_1": "Epididymis stores and matures sperm; Vas deferens transports sperm to the urethra.",
            "tier_2": "Match the organ to storage vs conduit/duct.",
            "tier_3": f"The answer is: {function}.",
        },
        "misconception_tags": ["epididymis_vas_deferens_confusion"],
    }


# 34. Male reproductive organs accessory glands and semen
def arch_34_male_reproductive_organs_accessory_glands_and_semen(rng: random.Random) -> Dict[str, Any]:
    glands = [
        ("Seminal vesicles", "secrete a thick alkaline fluid rich in fructose sugar (providing energy for sperm motility) and prostaglandins"),
        ("Prostate gland", "secretes a milky slightly alkaline fluid containing enzymes that activate sperm motility and neutralize the natural acidity of the female vagina"),
    ]
    target_gland, secretion_role = rng.choice(glands)
    prompt = (
        f"Semen is not merely sperm; sperm cells make up only about 5% of ejaculate volume, while the remaining 95% is seminal fluid. "
        f"What is the functional contribution of the '{target_gland}' to semen?"
    )
    correct = secretion_role
    options = [secretion_role] + [g[1] for g in glands if g[1] != secretion_role] + [
        "Produces red blood cells to carry oxygen directly to swimming sperm cells.",
        "Absorbs all sperm into the bladder to be eliminated during urination.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review male accessory glands:\n"
        f"- Seminal vesicles: fructose (energy for flagella) + alkaline buffer.\n"
        f"- Prostate gland: milky alkaline fluid neutralizing vaginal acidity and activating motility.\n\n"
        f"**Step 2:** For '{target_gland}', the contribution is: **{secretion_role}**."
    )
    return {
        "id": f"ns7_sr_34_{rng.randint(100000, 999999)}",
        "subskill": "34_male_reproductive_organs_accessory_glands_and_semen",
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
            "tier_1": "Accessory glands produce fluids that feed sperm (fructose) and protect them from acid.",
            "tier_2": "Seminal vesicles provide fructose fuel; the prostate neutralizes acid.",
            "tier_3": f"The answer is: {secretion_role}.",
        },
        "misconception_tags": ["semen_vs_sperm_composition_confusion"],
    }


# 35. Male reproductive organs penis and urethra
def arch_35_male_reproductive_organs_penis_and_urethra(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In human males, the urethra passes through the penis and serves as a dual-purpose duct. "
        f"Which statement scientifically describes how the male urethra operates?"
    )
    correct = "It acts as a shared conduit that transports urine from the urinary bladder during excretion, and semen from reproductive ducts during ejaculation (a sphincter muscle prevents both fluids from passing simultaneously)."
    options = [
        correct,
        "It continuously mixes urine and semen together so they always leave the body as a single fluid.",
        "It acts strictly as an organ of digestion that absorbs vitamins directly from bath water.",
        "It connects directly to the heart to pump oxygenated arterial blood out of the body.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the dual role of the male urethra:\n"
        f"- Excretory: carries urine from bladder.\n"
        f"- Reproductive: carries semen during ejaculation.\n"
        f"- Internal urethral sphincter closes during sexual excitement to prevent urine mixing with semen.\n\n"
        f"**Step 2:** The correct statement is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_35_{rng.randint(100000, 999999)}",
        "subskill": "35_male_reproductive_organs_penis_and_urethra",
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
            "tier_1": "Does the male urethra carry urine, semen, or both at different times?",
            "tier_2": "It carries urine during urination and semen during ejaculation, but never both at once.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["male_urethra_dual_function_confusion"],
    }


# 36. Female reproductive organs ovaries and ova
def arch_36_female_reproductive_organs_ovaries_and_ova(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The two ovaries are the primary female reproductive organs (gonads). "
        f"What are the two foundational biological functions of the ovaries in a mature human female?"
    )
    correct = "Producing female haploid gametes (egg cells / ova via oogenesis) and synthesizing the steroid hormones estrogen and progesterone."
    options = [
        correct,
        "Filtering urine from the blood and pumping oxygenated red blood cells to the brain.",
        "Producing millions of motile sperm cells and secreting male testosterone.",
        "Digesting food carbohydrates and absorbing water into the large intestine.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review ovarian functions:\n"
        f"1. Gamete production: releasing one mature ovum (egg cell) each month (ovulation).\n"
        f"2. Endocrine secretion: producing estrogen and progesterone to govern the menstrual cycle and secondary sex traits.\n\n"
        f"**Step 2:** The two functions are: **{correct}**."
    )
    return {
        "id": f"ns7_sr_36_{rng.randint(100000, 999999)}",
        "subskill": "36_female_reproductive_organs_ovaries_and_ova",
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
            "tier_1": "Ovaries do two things: make egg cells (ova) and make female hormones (estrogen/progesterone).",
            "tier_2": "They produce eggs and secrete reproductive hormones.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ovary_function_misunderstanding"],
    }


# 37. Female reproductive organs fallopian tubes site of fertilisation
def arch_37_female_reproductive_organs_fallopian_tubes_site_of_fertilisation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The Fallopian tubes (oviducts) connect each ovary to the uterus. "
        f"Where in the female reproductive tract does **fertilisation** (fusion of sperm and ovum) normally occur?"
    )
    correct = "In the upper third (ampulla) of the Fallopian tube (oviduct)."
    options = [
        correct,
        "Inside the muscular cervix at the entrance to the vagina.",
        "Directly on the exterior surface of the urinary bladder.",
        "Deep inside the amniotic fluid after the baby is already born.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify the anatomical site of fertilisation:\n"
        f"- Ovulation releases an ovum into the abdominal funnel (fimbriae) of the Fallopian tube.\n"
        f"- Cilia and peristalsis sweep the egg along the tube.\n"
        f"- Swimming sperm meet and fertilise the egg in the Fallopian tube.\n"
        f"- The resulting zygote divides as it travels to the uterus for implantation.\n\n"
        f"**Step 2:** Normal fertilisation occurs: **{correct}**."
    )
    return {
        "id": f"ns7_sr_37_{rng.randint(100000, 999999)}",
        "subskill": "37_female_reproductive_organs_fallopian_tubes_site_of_fertilisation",
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
            "tier_1": "Sperm meets egg in the Fallopian tube (oviduct), not in the uterus or vagina.",
            "tier_2": "Fertilisation happens in the Fallopian tube; implantation happens in the uterus.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fertilisation_site_misplaced_in_uterus"],
    }


# 38. Female reproductive organs uterus and endometrium
def arch_38_female_reproductive_organs_uterus_and_endometrium(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The uterus (womb) is a hollow, pear-shaped muscular organ lined by a specialized mucous membrane called the endometrium. "
        f"What is the biological role of the endometrium during the reproductive cycle?"
    )
    correct = "It thickens and becomes richly vascularized each month under progesterone to receive and nourish an implanting blastocyst/embryo; if no pregnancy occurs, it breaks down and is shed during menstruation."
    options = [
        correct,
        "It acts as a filter that turns incoming sperm cells into urine to be flushed out.",
        "It generates electrical shocks that prevent any cells from undergoing mitosis.",
        "It converts into a hard bone skeleton to support the female ribs during sleep.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the role of the endometrium:\n"
        f"- The endometrium prepares every month to support pregnancy.\n"
        f"- It builds up thick blood vessel networks to supply oxygen and nutrients to an early embryo.\n"
        f"- If no fertilisation happens, hormone levels drop and the lining sheds (menstruation).\n\n"
        f"**Step 2:** The biological role is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_38_{rng.randint(100000, 999999)}",
        "subskill": "38_female_reproductive_organs_uterus_and_endometrium",
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
            "tier_1": "The endometrium is the inner lining of the womb.",
            "tier_2": "It thickens with blood vessels to feed an embryo or sheds as a period if not pregnant.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["endometrium_function_misunderstanding"],
    }


# 39. Female reproductive organs cervix and vagina
def arch_39_female_reproductive_organs_cervix_and_vagina(rng: random.Random) -> Dict[str, Any]:
    structures = [
        ("Cervix", "the narrow lower muscular neck of the uterus that dilates up to 10 cm during childbirth and produces mucus that changes in consistency across the menstrual cycle"),
        ("Vagina", "an elastic muscular canal extending from the cervix to the exterior vulva, functioning as the receptacle for the penis during copulation and the birth canal during delivery"),
    ]
    target, desc = rng.choice(structures)
    alt = structures[1] if target == structures[0] else structures[0]
    prompt = (
        f"In the female reproductive anatomy, what is the anatomical definition and function of the '{target[0]}'?"
    )
    correct = desc
    options = [
        desc,
        alt[1],
        "The tube connecting the kidneys to the urinary bladder.",
        "The endocrine gland that secretes digestive insulin into the stomach.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish cervix and vagina:\n"
        f"- Cervix = narrow muscular opening at base of uterus (dilates during labour).\n"
        f"- Vagina = muscular birth canal connecting cervix to outside.\n\n"
        f"**Step 2:** For '{target[0]}', the definition is: **{desc}**."
    )
    return {
        "id": f"ns7_sr_39_{rng.randint(100000, 999999)}",
        "subskill": "39_female_reproductive_organs_cervix_and_vagina",
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
            "tier_1": "Cervix is the doorway/neck of the uterus; vagina is the birth canal.",
            "tier_2": "The cervix dilates during labour; the vagina connects to the outside.",
            "tier_3": f"The answer is: {desc}.",
        },
        "misconception_tags": ["cervix_vagina_confusion"],
    }


# 40. Menstrual cycle four phases timeline
def arch_40_menstrual_cycle_four_phases_timeline(rng: random.Random) -> Dict[str, Any]:
    phases = [
        ("Menstruation phase", "Days 1 to 5", "the vascular endometrium lining breaks down and is discharged through the vagina as menstrual flow because progesterone levels have dropped"),
        ("Follicular (proliferative) phase", "Days 6 to 13", "FSH stimulates an ovarian follicle to mature while rising estrogen causes the uterine endometrium to regenerate and thicken"),
        ("Ovulation", "Day 14", "a surge in luteinizing hormone (LH) triggers the mature Graafian follicle to rupture, releasing a secondary oocyte (egg) into the Fallopian tube"),
        ("Luteal (secretory) phase", "Days 15 to 28", "the ruptured follicle transforms into the corpus luteum, which secretes high progesterone to maintain a spongy, vascular uterine lining ready for implantation"),
    ]
    target_phase, days, mechanism = rng.choice(phases)
    cycle_days = rng.choice([28, 29, 30])
    target_stroke = rng.choice(["#E11D48", "#2563EB", "#059669", "#7C3AED"])

    svg = (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 440 220' width='100%' height='220'>"
        f"<rect width='440' height='220' fill='#FAFAFA' rx='8'/>"
        f"<circle cx='220' cy='110' r='80' fill='none' stroke='#CBD5E1' stroke-width='24'/>"
        f"<path d='M 220 30 A 80 80 0 0 1 290 60' fill='none' stroke='#EF4444' stroke-width='24'/>"
        f"<text x='260' y='30' fill='#DC2626' font-size='10' font-weight='bold'>Days 1-5: Menses</text>"
        f"<path d='M 290 60 A 80 80 0 0 1 220 190' fill='none' stroke='#3B82F6' stroke-width='24'/>"
        f"<text x='310' y='120' fill='#1D4ED8' font-size='10' font-weight='bold'>Days 6-13: Follicular</text>"
        f"<circle cx='220' cy='190' r='14' fill='#F59E0B'/>"
        f"<text x='220' y='215' fill='#D97706' font-size='11' font-weight='bold' text-anchor='middle'>Day 14: Ovulation</text>"
        f"<path d='M 220 190 A 80 80 0 0 1 220 30' fill='none' stroke='#10B981' stroke-width='24'/>"
        f"<text x='110' y='120' fill='#047857' font-size='10' font-weight='bold'>Days 15-{cycle_days}: Luteal</text>"
        f"<circle cx='220' cy='110' r='45' fill='none' stroke='{target_stroke}' stroke-width='3' stroke-dasharray='4,4'/>"
        f"<text x='220' y='105' fill='{target_stroke}' font-size='11' font-weight='bold' text-anchor='middle'>{target_phase}</text>"
        f"<text x='220' y='125' fill='#64748B' font-size='10' text-anchor='middle'>{days} ({cycle_days}d cycle)</text>"
        f"</svg>"
    )
    prompt = (
        f"In a human menstrual cycle of {cycle_days} days, a health diagram highlights the '{target_phase}' occurring during {days}. "
        f"Which physiological events occur during this specific phase?"
    )
    correct = mechanism
    options = [mechanism] + [p[2] for p in phases if p[2] != mechanism]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review the 4 phases of the 28-day menstrual cycle:\n"
        f"- Days 1-5 (Menstruation): Shedding of endometrium.\n"
        f"- Days 6-13 (Follicular): Follicle matures, estrogen thickens endometrium.\n"
        f"- Day 14 (Ovulation): LH surge releases mature egg.\n"
        f"- Days 15-28 (Luteal): Corpus luteum produces progesterone to maintain lining.\n\n"
        f"**Step 2:** For '{target_phase}' ({days}), the event is: **{mechanism}**."
    )
    return {
        "id": f"ns7_sr_40_{rng.randint(100000, 999999)}",
        "subskill": "40_menstrual_cycle_four_phases_timeline",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context",
        },
        "hints": {
            "tier_1": "Day 14 is ovulation; Days 1-5 is menstruation; Days 15-28 is the luteal phase.",
            "tier_2": f"Find what occurs during {target_phase} ({days}).",
            "tier_3": f"The answer is: {mechanism}.",
        },
        "misconception_tags": ["menstrual_cycle_phase_timeline_confusion"],
    }


# 41. Human fertilisation sperm egg fusion in oviduct
def arch_41_human_fertilisation_sperm_egg_fusion_in_oviduct(rng: random.Random) -> Dict[str, Any]:
    sperm_millions = rng.choice([200, 300, 400])
    prompt = (
        f"During human copulation, approximately {sperm_millions} million sperm cells are deposited into the vagina. "
        f"However, how many sperm cells actually penetrate and fertilise the single ovum?"
    )
    correct = "Exactly ONE sperm cell penetrates the ovum's outer membrane (zona pellucida); a rapid cortical reaction instantly hardens the membrane, permanently blocking all other sperm (preventing polyspermy)."
    options = [
        correct,
        f"All {sperm_millions} million sperm enter the egg simultaneously to build the baby's limbs.",
        "Exactly twenty-three sperm enter, each providing one chromosome.",
        "Zero sperm enter; the baby is formed by water molecules condensing inside the uterus.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand the mechanics of fertilisation:\n"
        f"- While millions of sperm swim toward the egg, only a few thousand reach the Fallopian tube.\n"
        f"- The first sperm to bind triggers the acrosome reaction, penetrating the zona pellucida.\n"
        f"- Immediately upon fusion, a cortical reaction releases enzymes that harden the egg membrane, blocking polyspermy.\n\n"
        f"**Step 2:** Exactly ONE sperm fertilises the ovum: **{correct}**."
    )
    return {
        "id": f"ns7_sr_41_{rng.randint(100000, 999999)}",
        "subskill": "41_human_fertilisation_sperm_egg_fusion_in_oviduct",
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
            "tier_1": "How many sperm fertilise one egg cell? Only one.",
            "tier_2": "The egg hardens its outer coat immediately after one sperm enters to block others.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["polyspermy_misconception"],
    }


# 42. Embryo implantation in uterine lining
def arch_42_embryo_implantation_in_uterine_lining(rng: random.Random) -> Dict[str, Any]:
    days_post = rng.choice([6, 7, 8])
    prompt = (
        f"Following fertilisation in the Fallopian tube, the single-celled zygote undergoes repeated mitotic divisions (cleavage) "
        f"as it travels down the oviduct. Approximately {days_post} days after fertilisation, the developing ball of cells (blastocyst) "
        f"reaches the uterus. What critical event occurs at this stage?"
    )
    correct = "Implantation: the blastocyst embeds into the nutrient-rich, vascularized endometrium lining of the uterus to establish pregnancy and begin forming the placenta."
    options = [
        correct,
        "Ovulation: the blastocyst explodes and releases a new egg back into the ovary.",
        "Menstruation: the blastocyst is immediately destroyed and washed out of the body.",
        "Childbirth: the fully formed baby is born into the world 7 days after fertilisation.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace early embryonic development:\n"
        f"- Day 0: Fertilisation in Fallopian tube -> Zygote.\n"
        f"- Days 1-5: Cleavage divisions form a morula and then a blastocyst.\n"
        f"- Days 6-8: Blastocyst implants into the vascular uterine endometrium.\n\n"
        f"**Step 2:** This critical event is **Implantation**: **{correct}**."
    )
    return {
        "id": f"ns7_sr_42_{rng.randint(100000, 999999)}",
        "subskill": "42_embryo_implantation_in_uterine_lining",
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
            "tier_1": "What is it called when the early embryo burrows into the womb wall? Implantation.",
            "tier_2": "The embryo embeds in the endometrium to begin receiving nutrients from the mother.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["implantation_timing_confusion"],
    }


# 43. Gestation placenta and umbilical cord functions
def arch_43_gestation_placenta_and_umbilical_cord_functions(rng: random.Random) -> Dict[str, Any]:
    structures = [
        ("The Placenta", "acts as a selective exchange organ where oxygen, glucose, amino acids, and antibodies diffuse from maternal blood into foetal blood, and metabolic wastes (CO2, urea) diffuse in reverse, WITHOUT maternal and foetal blood ever directly mixing"),
        ("The Umbilical Cord", "contains two umbilical arteries carrying deoxygenated blood and wastes from the foetus to the placenta, and one umbilical vein carrying oxygenated nutrient-rich blood from the placenta to the foetus"),
    ]
    target, details = rng.choice(structures)
    prompt = (
        f"During gestation, the foetus relies completely on maternal physiological support. "
        f"What is the biological function of '{target[0]}'?"
    )
    correct = details
    options = [details] + [s[1] for s in structures if s[1] != details] + [
        "Acts as a solid bone that connects the baby's skull directly to the mother's spine.",
        "Produces digestive stomach acid that breaks down raw meat inside the uterus.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review foetal support structures:\n"
        f"- Placenta: exchange barrier between maternal and foetal circulations (diffusion without blood mixing).\n"
        f"- Umbilical cord: lifeline conduit containing 2 arteries (wastes out) and 1 vein (nutrients in).\n\n"
        f"**Step 2:** For '{target[0]}', the function is: **{details}**."
    )
    return {
        "id": f"ns7_sr_43_{rng.randint(100000, 999999)}",
        "subskill": "43_gestation_placenta_and_umbilical_cord_functions",
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
            "tier_1": "Do maternal and baby blood mix directly? No, substances diffuse across the placenta.",
            "tier_2": "The umbilical cord carries blood vessels between the baby and the placenta.",
            "tier_3": f"The answer is: {details}.",
        },
        "misconception_tags": ["maternal_foetal_blood_mixing_misconception"],
    }


# 44. Gestation amniotic sac and fluid protection
def arch_44_gestation_amniotic_sac_and_fluid_protection(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Throughout pregnancy, the developing human foetus floats inside a fluid-filled membrane called the amniotic sac. "
        f"What are the three essential protective functions provided by the **amniotic fluid**?"
    )
    correct = "1. Absorbing mechanical shocks and physical jolts; 2. Maintaining a constant warm temperature; 3. Allowing free movement for musculoskeletal development while preventing embryonic adhesion to surrounding membranes."
    options = [
        correct,
        "1. Supplying high-voltage electricity; 2. Freezing the baby into a solid state; 3. Digesting rocks inside the uterus.",
        "1. Replacing oxygen breathing; 2. Pumping maternal blood through the skin; 3. Creating red blood cells.",
        "1. Acting as pure drinking milk; 2. Preventing any cell division; 3. Turning hair into scales.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review functions of amniotic fluid:\n"
        f"- Shock absorber: protects foetus against external knocks and pressure.\n"
        f"- Thermoregulation: keeps the foetus in a stable, warm thermal environment.\n"
        f"- Movement/support: allows muscles and bones to develop freely and prevents foetal skin sticking to the amnion.\n\n"
        f"**Step 2:** The protective functions are: **{correct}**."
    )
    return {
        "id": f"ns7_sr_44_{rng.randint(100000, 999999)}",
        "subskill": "44_gestation_amniotic_sac_and_fluid_protection",
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
            "tier_1": "Think about floating in a swimming pool: it cushions falls and keeps temperature steady.",
            "tier_2": "Shock absorption, temperature regulation, and freedom of movement.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["amniotic_fluid_function_confusion"],
    }


# 45. Childbirth stages labour dilation and delivery
def arch_45_childbirth_stages_labour_dilation_and_delivery(rng: random.Random) -> Dict[str, Any]:
    weeks = rng.choice([38, 40])
    prompt = (
        f"Full-term human gestation lasts approximately {weeks} weeks. "
        f"Which option lists the three progressive stages of childbirth (labour) in the correct chronological order?"
    )
    correct = "1. Dilation stage (uterine contractions widen the cervix to 10 cm and amniotic sac ruptures) -> 2. Expulsion stage (mother pushes and the baby is delivered through the vagina) -> 3. Placental stage (the placenta and foetal membranes are expelled as the afterbirth)"
    options = [
        correct,
        "1. Placental expulsion -> 2. Ovulation of a new egg -> 3. Dilation of cervix -> 4. Baby delivery",
        "1. Baby delivery -> 2. Uterine contractions begin -> 3. Amniotic sac forms",
        "1. Implantation of embryo -> 2. Delivery of placenta -> 3. Cervix closes permanently",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Sequence the 3 stages of childbirth:\n"
        f"Stage 1: Dilation of cervix (contractions thin and widen cervix to ~10 cm; waters break).\n"
        f"Stage 2: Delivery of the baby (expulsion through birth canal).\n"
        f"Stage 3: Delivery of the afterbirth (placenta and umbilical cord).\n\n"
        f"**Step 2:** The correct chronological order is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_45_{rng.randint(100000, 999999)}",
        "subskill": "45_childbirth_stages_labour_dilation_and_delivery",
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
            "tier_1": "Contractions open the cervix first, then the baby is born, then the placenta comes out.",
            "tier_2": "Dilation -> Baby delivery -> Afterbirth (placenta).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["childbirth_stages_sequence_error"],
    }


# 46. Contraception barrier methods condoms
def arch_46_contraception_barrier_methods_condoms(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Various contraceptive methods exist to prevent unintended pregnancy. "
        f"Why are barrier methods (specifically male and female latex condoms) uniquely critical in public health?"
    )
    correct = "Because condoms are the ONLY contraceptive method that simultaneously prevents unintended pregnancy AND protects against the transmission of Sexually Transmitted Infections (STIs), including HIV."
    options = [
        correct,
        "Because condoms permanently sterilize both sexual partners forever after one use.",
        "Because condoms are oral hormonal tablets that prevent ovaries from releasing eggs.",
        "Because condoms change a person's blood group to prevent pregnancy.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Evaluate contraceptive methods in public health:\n"
        f"- Hormonal contraceptives (the pill, injections, implants) prevent ovulation but offer ZERO protection against STIs/HIV.\n"
        f"- Barrier methods (male and female condoms) block physical exchange of bodily fluids and sperm.\n"
        f"- Therefore, condoms are the ONLY method providing dual protection against pregnancy AND STIs/HIV.\n\n"
        f"**Step 2:** The critical public health distinction is: **{correct}**."
    )
    return {
        "id": f"ns7_sr_46_{rng.randint(100000, 999999)}",
        "subskill": "46_contraception_barrier_methods_condoms",
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
            "tier_1": "Think about dual protection: pregnancy AND sexually transmitted infections like HIV.",
            "tier_2": "Hormone pills do not protect against STIs; only barrier condoms protect against both.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["contraception_dual_protection_confusion"],
    }


# 47. Contraception hormonal and permanent methods
def arch_47_contraception_hormonal_and_permanent_methods(rng: random.Random) -> Dict[str, Any]:
    methods = [
        ("The oral contraceptive pill (taken daily)", "contains synthetic estrogen and progesterone that suppress pituitary FSH and LH, preventing ovulation and thickening cervical mucus to impede sperm"),
        ("The contraceptive injection (e.g. Depo-Provera, given every 2 to 3 months)", "releases slow-release progestin into muscle to suppress ovulation for 8 to 12 weeks"),
        ("Vasectomy (male surgical sterilization)", "a minor surgical procedure where the vas deferens (sperm ducts) are cut and sealed, preventing sperm from entering ejaculated semen"),
        ("Tubal ligation (female surgical sterilization)", "a surgical procedure where the Fallopian tubes (oviducts) are severed and tied, permanently preventing ova from meeting sperm"),
    ]
    method_name, mechanism = rng.choice(methods)
    prompt = (
        f"Contraceptive technologies utilize different biological mechanisms to prevent conception. "
        f"How does '{method_name}' prevent pregnancy?"
    )
    correct = mechanism
    options = [mechanism] + [m[1] for m in methods if m[1] != mechanism]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review contraceptive classifications:\n"
        f"- Hormonal (pill, injection): prevents ovulation by mimicking luteal hormone levels.\n"
        f"- Surgical / permanent (vasectomy, tubal ligation): physically severs gamete conduits (vas deferens or fallopian tubes).\n\n"
        f"**Step 2:** For '{method_name}', the mechanism is: **{mechanism}**."
    )
    return {
        "id": f"ns7_sr_47_{rng.randint(100000, 999999)}",
        "subskill": "47_contraception_hormonal_and_permanent_methods",
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
            "tier_1": "Is it a hormone pill/shot that stops ovulation, or a surgery that cuts a tube?",
            "tier_2": "Vasectomy cuts sperm ducts; tubal ligation cuts fallopian tubes; pills stop ovulation.",
            "tier_3": f"The answer is: {mechanism}.",
        },
        "misconception_tags": ["contraceptive_mechanism_confusion"],
    }


# 48. Sexually transmitted infections pathogens and symptoms
def arch_48_sexually_transmitted_infections_pathogens_and_symptoms(rng: random.Random) -> Dict[str, Any]:
    stis = [
        ("Human Immunodeficiency Virus (HIV)", "a viral pathogen transmitted via blood and sexual fluids that attacks CD4+ helper T-cells, progressively crippling the immune system and leading to AIDS if untreated"),
        ("Gonorrhoea (caused by Neisseria gonorrhoeae)", "a bacterial infection causing burning painful urination, thick yellowish genital discharge, and potential pelvic inflammatory disease (PID) causing infertility"),
        ("Syphilis (caused by Treponema pallidum)", "a bacterial infection characterized by a painless genital ulcer (chancre) in early stages, progressing to skin rashes and systemic organ damage if untreated"),
    ]
    sti_name, profile = rng.choice(stis)
    prompt = (
        f"Sexually Transmitted Infections (STIs) are major public health priorities in South Africa. "
        f"Which clinical and biological profile correctly describes '{sti_name}'?"
    )
    correct = profile
    options = [profile] + [s[1] for s in stis if s[1] != profile]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review major STIs and pathogens:\n"
        f"- HIV: virus attacking CD4 immune cells.\n"
        f"- Gonorrhoea: bacterium causing burning urination and pus discharge.\n"
        f"- Syphilis: bacterium causing painless chancre sores and organ damage.\n\n"
        f"**Step 2:** For '{sti_name}', the profile is: **{profile}**."
    )
    return {
        "id": f"ns7_sr_48_{rng.randint(100000, 999999)}",
        "subskill": "48_sexually_transmitted_infections_pathogens_and_symptoms",
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
            "tier_1": "Identify whether the STI is viral (HIV) or bacterial (gonorrhoea, syphilis).",
            "tier_2": "HIV destroys immune cells; gonorrhoea causes painful discharge; syphilis causes ulcers.",
            "tier_3": f"The answer is: {profile}.",
        },
        "misconception_tags": ["sti_pathogen_type_confusion"],
    }


# 49. Addressing menstruation and pregnancy myths
def arch_49_addressing_menstruation_and_pregnancy_myths(rng: random.Random) -> Dict[str, Any]:
    myths = [
        ("Myth: 'A girl cannot fall pregnant the very first time she engages in sexual intercourse.'", "Fact: A female can fall pregnant whenever ovulation occurs, even during her very first sexual encounter if unprotected."),
        ("Myth: 'Swimming or exercising during menstruation is harmful and dangerous for a woman's health.'", "Fact: Menstruation is a normal healthy biological process; gentle exercise and swimming (with proper sanitary products) are safe and can relieve menstrual cramps."),
        ("Myth: 'Douching or taking a hot shower immediately after intercourse washes away sperm and prevents pregnancy.'", "Fact: Sperm swim into the cervical canal within seconds of ejaculation; showering or douching cannot wash away sperm and provides zero contraceptive protection."),
    ]
    myth_statement, scientific_fact = rng.choice(myths)
    prompt = (
        f"Harmful social myths often surround menstruation and human reproduction. "
        f"Analyze the following widespread belief:\n"
        f"\"{myth_statement}\"\n\n"
        f"Which statement provides the accurate scientific medical fact?"
    )
    correct = scientific_fact
    distractors = [
        "The myth is completely true because scientific laws only apply to adults over 30 years old.",
        "The myth is true because water has magical properties that destroy all living cells.",
        "The myth is true because pregnancy only occurs in cold winter months.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Address reproductive myths using CAPS curriculum guidance:\n"
        f"- Pregnancy can happen on the very first sexual encounter if ovulation has occurred.\n"
        f"- Menstruation is normal and healthy; exercise is beneficial.\n"
        f"- Showering after intercourse does not prevent sperm from reaching the Fallopian tubes.\n\n"
        f"**Step 2:** The scientific fact is: **{scientific_fact}**."
    )
    return {
        "id": f"ns7_sr_49_{rng.randint(100000, 999999)}",
        "subskill": "49_addressing_menstruation_and_pregnancy_myths",
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
            "tier_1": "Common myths about pregnancy and periods are scientifically false.",
            "tier_2": "Look for the evidence-based medical fact debunking the myth.",
            "tier_3": f"The answer is: {scientific_fact}.",
        },
        "misconception_tags": ["reproductive_myth_debunking"],
    }


# 50. Synthetic case study teenage reproductive health counselling
def arch_50_synthetic_case_study_teenage_reproductive_health_counselling(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        (
            "Two 14-year-old learners feel peer pressure to engage in sexual activity before they feel emotionally ready.",
            "Abstinence: choosing to delay sexual activity until one is emotionally, physically, and socially mature is the safest and 100% effective method to prevent teenage pregnancy and STIs",
        ),
        (
            "An adolescent wants to know how to access confidential adolescent-friendly healthcare services in South Africa.",
            "Under South African law and health policy, public primary healthcare clinics provide free, confidential reproductive counselling, contraceptives, and STI screening to adolescents without parental consent required from age 12",
        ),
    ]
    dilemma, advice = rng.choice(scenarios)
    prompt = (
        f"In life orientation and natural sciences education, adolescent reproductive health counselling empowers informed decisions. "
        f"Consider this scenario:\n"
        f"\"{dilemma}\"\n\n"
        f"Which guidance aligns with South African health policy and adolescent well-being?"
    )
    correct = advice
    options = [advice] + [s[1] for s in scenarios if s[1] != advice] + [
        "Adolescents should avoid asking doctors any questions and rely strictly on rumours from classmates.",
        "Healthcare clinics charge teenagers thousands of rands and arrest anyone asking about biology.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review South African adolescent reproductive health principles:\n"
        f"- Abstinence is the only 100% effective strategy for preventing pregnancy and STIs for teenagers.\n"
        f"- Public clinics offer confidential, free reproductive healthcare services to youth.\n\n"
        f"**Step 2:** The correct guidance is: **{advice}**."
    )
    return {
        "id": f"ns7_sr_50_{rng.randint(100000, 999999)}",
        "subskill": "50_synthetic_case_study_teenage_reproductive_health_counselling",
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
            "tier_1": "Think about adolescent rights and the benefits of delaying sexual activity until mature.",
            "tier_2": "Abstinence is 100% effective, and public clinics provide free confidential guidance.",
            "tier_3": f"The answer is: {advice}.",
        },
        "misconception_tags": ["adolescent_health_policy_misunderstanding"],
    }
