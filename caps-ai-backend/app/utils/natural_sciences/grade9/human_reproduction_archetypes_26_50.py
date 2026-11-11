"""Grade 9 Natural Sciences: Term 1 - Human Reproduction (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 1/03. Human reproduction.md.
Focus: Implantation, placenta/umbilical cord, gestation, teratogens (FAS/nicotine/folic acid), labor/birth, contraception, STIs, infertility/IVF, and twins.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Implantation blastocyst trophoblast and endometrial embedding
def arch_26_implantation_blastocyst_trophoblast_and_endometrial_embedding(rng: random.Random) -> Dict[str, Any]:
    events = [
        (
            "Trophoblast outer cell layer",
            "Secretes proteolytic enzymes that digest into the thickened vascular endometrium, facilitating embedding and producing hCG",
        ),
        (
            "Inner cell mass (embryoblast)",
            "Pluripotent cluster of cells within the blastocyst that will differentiate into the embryo and all fetal tissues",
        ),
        (
            "Human Chorionic Gonadotropin (hCG)",
            "Embryonic hormone that rescues the corpus luteum from degenerating, maintaining high progesterone secretion to sustain the endometrium",
        ),
        (
            "Timing of implantation",
            "Occurs approximately 6 to 9 days after fertilization in the upper posterior wall of the uterine endometrium",
        ),
    ]
    name, role = rng.choice(events)
    prompt = (
        f"Following cleavage in the fallopian tube, the dividing ball of cells forms a blastocyst that reaches the uterus.\n\n"
        f"Which statement accurately explains the biological significance of: **{name}**?"
    )
    correct = role
    distractors = [e[1] for e in events if e[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze blastocyst implantation dynamics.\n"
        f"**Step 2:** Match feature to its physiological function:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_26_{rng.randint(100000, 999999)}",
        "subskill": "26_implantation_blastocyst_trophoblast_and_endometrial_embedding",
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
            "tier_1": f"Recall how {name} contributes to successful uterine implantation.",
            "tier_2": "Trophoblast invades endometrium; inner cell mass becomes embryo; hCG preserves corpus luteum.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["blastocyst_implantation_hcg_trophoblast_misconception"],
    }


# 27. Gestation and trimesters developmental milestones
def arch_27_gestation_and_trimesters_developmental_milestones(rng: random.Random) -> Dict[str, Any]:
    milestones = [
        (
            "First Trimester (Weeks 1-12)",
            "Organogenesis takes place: heart starts beating (~week 4), limbs and facial features form, and rudimentary nervous system develops; embryo is most vulnerable to teratogens",
        ),
        (
            "Second Trimester (Weeks 13-26)",
            "Rapid fetal growth and skeletal ossification occur; hair (lanugo) and eyelashes form; mother begins to feel fetal movements (quickening)",
        ),
        (
            "Third Trimester (Weeks 27-40)",
            "Extensive brain growth, lung maturation (pulmonary surfactant synthesis), and rapid deposition of insulating adipose tissue prepare fetus for independent life outside the womb",
        ),
    ]
    tri_name, desc = rng.choice(milestones)
    prompt = (
        f"Human gestation lasts approximately 40 weeks (280 days from the last menstrual period), divided into three trimesters.\n\n"
        f"Which developmental milestone and clinical profile characterizes the **{tri_name}**?"
    )
    correct = desc
    distractors = [m[1] for m in milestones if m[0] != tri_name]
    distractors.append("All organs disappear completely and the fetus turns back into an unfertilized ovum.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review gestational developmental stages.\n"
        f"**Step 2:** Match trimester to core developmental landmarks:\n"
        f"- {tri_name}: {correct}\n\n"
        f"**Step 3:** The accurate profile is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_27_{rng.randint(100000, 999999)}",
        "subskill": "27_gestation_and_trimesters_developmental_milestones",
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
            "tier_1": f"Think about what forms during the {tri_name}.",
            "tier_2": "1st trimester = organogenesis; 2nd = rapid growth and quickening; 3rd = fat storage and lung maturation.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["gestational_trimester_developmental_milestones_misconception"],
    }


# 28. Placenta structure and function barrier and nutrient gas exchange
def arch_28_placenta_structure_and_function_barrier_and_nutrient_gas_exchange(rng: random.Random) -> Dict[str, Any]:
    functions = [
        (
            "Nutrient and Gas Exchange",
            "Oxygen and dissolved nutrients (glucose, amino acids) diffuse from maternal blood sinuses into fetal capillaries, while fetal metabolic wastes (CO2, urea) diffuse in reverse",
        ),
        (
            "Placental Barrier Isolation",
            "Maternal and fetal blood never mix directly; separation by thin chorionic villi walls prevents maternal blood pressure from destroying fragile fetal vessels and prevents agglutination from incompatible ABO/Rh blood types",
        ),
        (
            "Endocrine Secretion",
            "Takes over from corpus luteum by month 3 to synthesize massive quantities of progesterone and estrogen, sustaining the pregnant endometrium until birth",
        ),
        (
            "Passive Immunity Transfer",
            "Selectively transports maternal immunoglobulin G (IgG) antibodies across chorionic villi to endow the newborn with temporary immune protection against pathogens",
        ),
    ]
    fn_name, mechanism = rng.choice(functions)
    prompt = (
        f"The placenta is a temporary disc-shaped organ formed jointly by embryonic chorionic tissue and maternal endometrium.\n\n"
        f"Which statement correctly describes the **{fn_name}** performed by the placenta?"
    )
    correct = mechanism
    distractors = [f[1] for f in functions if f[0] != fn_name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze placental physiology and adaptations.\n"
        f"**Step 2:** Relate {fn_name} to biological mechanism:\n"
        f"- {fn_name}: {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_28_{rng.randint(100000, 999999)}",
        "subskill": "28_placenta_structure_and_function_barrier_and_nutrient_gas_exchange",
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
            "tier_1": f"Recall how the placenta accomplishes: {fn_name}.",
            "tier_2": "Maternal and fetal blood do not mix directly; diffusion occurs across chorionic villi, and hormones like progesterone maintain pregnancy.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["placental_circulation_and_maternal_fetal_barrier_misconception"],
    }


# 29. Umbilical cord two arteries one vein circulation
def arch_29_umbilical_cord_two_arteries_one_vein_circulation(rng: random.Random) -> Dict[str, Any]:
    vessels = [
        (
            "Umbilical Vein (1 vessel)",
            "Carries oxygen-rich and nutrient-rich blood from the placenta to the fetal heart and liver",
            "Deoxygenated blood carrying waste from the fetus to the mother",
        ),
        (
            "Umbilical Arteries (2 vessels)",
            "Carry deoxygenated, waste-laden blood (containing urea and CO2) from the internal iliac arteries of the fetus back to the placenta",
            "Oxygen-rich blood pumped from the mother's aorta into the fetal brain",
        ),
    ]
    name, correct_fn, wrong_fn = rng.choice(vessels)
    prompt = (
        f"The umbilical cord connects the developing fetus to the placenta, embedded in protective gelatinous Wharton's jelly.\n\n"
        f"What is the number of vessels and physiological flow direction of the **{name.split()[0]} {name.split()[1]}**?"
    )
    alt = [v for v in vessels if v[0] != name][0]
    options = [
        f"{name}: {correct_fn}.",
        f"{name}: {wrong_fn}.",
        f"{alt[0]}: {alt[1]}.",
        "A single lymph tube carrying solid food particles directly to the fetal stomach.",
    ]
    correct = f"{name}: {correct_fn}."
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Note umbilical vessel counts and roles:\n"
        f"- 1 Umbilical Vein: carries oxygenated, nutrient-rich blood toward the fetus.\n"
        f"- 2 Umbilical Arteries: carry deoxygenated, waste-rich blood away from the fetus toward the placenta.\n\n"
        f"**Step 2:** Match {name}:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The accurate description is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_29_{rng.randint(100000, 999999)}",
        "subskill": "29_umbilical_cord_two_arteries_one_vein_circulation",
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
            "tier_1": "Notice: In fetal circulation, the umbilical VEIN brings oxygen TO the baby, while ARTERIES take waste AWAY.",
            "tier_2": "Cord has 2 arteries (deoxygenated waste to placenta) and 1 vein (oxygenated blood to fetus).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["umbilical_vessels_arteries_vs_vein_oxygenation_misconception"],
    }


# 30. Amniotic sac and fluid cushioning thermoregulation protection
def arch_30_amniotic_sac_and_fluid_cushioning_thermoregulation_protection(rng: random.Random) -> Dict[str, Any]:
    roles = [
        (
            "Mechanical shock absorption",
            "Acts as a fluid cushion absorbing external impacts and pressures against the mother's abdomen, preventing trauma to the delicate fetus",
        ),
        (
            "Thermal buffering and homeothermy",
            "Maintains a stable, warm body temperature around the fetus regardless of external environmental temperature fluctuations",
        ),
        (
            "Freedom of musculoskeletal movement",
            "Allows the fetus to move limbs freely in buoyant liquid, preventing fetal adhesions to membranes and promoting musculoskeletal development",
        ),
        (
            "Lung and digestive tract preparation",
            "Fetus inhales and swallows amniotic fluid, facilitating respiratory tract branching and gastrointestinal tract practice prior to birth",
        ),
    ]
    fn_name, explanation = rng.choice(roles)
    prompt = (
        f"Throughout gestation, the fetus floats weightlessly within the fluid-filled amniotic sac enclosed by the amnion membrane.\n\n"
        f"How does the amniotic fluid provide **{fn_name}**?"
    )
    correct = explanation
    distractors = [r[1] for r in roles if r[0] != fn_name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze amniotic fluid functions.\n"
        f"**Step 2:** Relate to {fn_name}:\n"
        f"- {fn_name}: {correct}\n\n"
        f"**Step 3:** The correct physiological role is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_30_{rng.randint(100000, 999999)}",
        "subskill": "30_amniotic_sac_and_fluid_cushioning_thermoregulation_protection",
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
            "tier_1": f"Think about how liquid surrounding the baby performs: {fn_name}.",
            "tier_2": "Amniotic fluid acts as a hydraulic shock absorber, temperature buffer, and prevents skin adhesions.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["amniotic_fluid_and_sac_protective_functions_misconception"],
    }


# 31. Maternal lifestyle teratogens alcohol fetal alcohol syndrome fas
def arch_31_maternal_lifestyle_teratogens_alcohol_fetal_alcohol_syndrome_fas(rng: random.Random) -> Dict[str, Any]:
    consequences = [
        (
            "Craniofacial dysmorphology",
            "Microcephaly (small head circumference), smooth philtrum, thin upper lip, and short palpebral fissures (small eye openings)",
        ),
        (
            "Central nervous system neurodevelopmental damage",
            "Severe irreversible cognitive deficit, impaired memory, intellectual disability, ADHD, and diminished executive brain function",
        ),
        (
            "Intrauterine and postnatal growth restriction",
            "Stunted height and low birth weight persisting throughout childhood and adulthood due to impaired cellular division",
        ),
    ]
    feature, desc = rng.choice(consequences)
    prompt = (
        f"Alcohol is a potent teratogen that freely crosses the placental barrier. Fetal alcohol dehydrogenase activity is negligible, causing alcohol to persist in fetal tissues at toxic concentrations.\n\n"
        f"Which clinical manifestation is a hallmark of **Fetal Alcohol Syndrome (FAS)** regarding **{feature}**?"
    )
    correct = desc
    distractors = [c[1] for c in consequences if c[0] != feature]
    distractors.append("Permanent genetic mutation turning fetal erythrocytes into plant chloroplasts.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review clinical features of Fetal Alcohol Syndrome (FAS).\n"
        f"**Step 2:** Identify manifestations of {feature}:\n"
        f"- {feature}: {correct}\n\n"
        f"**Step 3:** The correct clinical hallmark is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_31_{rng.randint(100000, 999999)}",
        "subskill": "31_maternal_lifestyle_teratogens_alcohol_fetal_alcohol_syndrome_fas",
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
            "tier_1": f"Recall how prenatal alcohol exposure impacts {feature}.",
            "tier_2": "FAS features: microcephaly, smooth philtrum, intellectual disability, and persistent growth restriction.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["fetal_alcohol_syndrome_fas_teratogen_misconception"],
    }


# 32. Maternal lifestyle smoking nicotine low birth weight prematurity
def arch_32_maternal_lifestyle_smoking_nicotine_low_birth_weight_prematurity(rng: random.Random) -> Dict[str, Any]:
    toxins = [
        (
            "Carbon Monoxide (CO)",
            "Binds tightly to maternal and fetal hemoglobin to form carboxyhemoglobin, drastically reducing oxygen-carrying capacity and causing chronic fetal hypoxia",
        ),
        (
            "Nicotine",
            "Causes severe vasoconstriction of placental and uterine blood vessels, diminishing blood flow and nutrient delivery, while accelerating fetal heart rate",
        ),
        (
            "Combined clinical outcome",
            "Significantly elevated risk of intrauterine growth restriction (IUGR), low birth weight (<2500 g), premature labor, and sudden infant death syndrome (SIDS)",
        ),
    ]
    name, mechanism = rng.choice(toxins)
    prompt = (
        f"Cigarette smoke contains thousands of chemicals that cross the placenta into fetal circulation.\n\n"
        f"What is the biological mechanism and pathophysiological consequence of **{name}** during pregnancy?"
    )
    correct = mechanism
    distractors = [t[1] for t in toxins if t[0] != name]
    distractors.append("Produces excess calcium causing the fetal skull to turn completely into solid enamel.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the pathophysiological effects of cigarette smoke components during pregnancy.\n"
        f"**Step 2:** Relate {name} to fetal compromise:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_32_{rng.randint(100000, 999999)}",
        "subskill": "32_maternal_lifestyle_smoking_nicotine_low_birth_weight_prematurity",
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
            "tier_1": f"What effect does {name} have on blood vessels or oxygen transport?",
            "tier_2": "CO displaces oxygen from hemoglobin; nicotine constricts placental blood vessels causing low birth weight.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["maternal_smoking_nicotine_placental_hypoxia_misconception"],
    }


# 33. Maternal lifestyle diet folic acid spina bifida prevention
def arch_33_maternal_lifestyle_diet_folic_acid_spina_bifida_prevention(rng: random.Random) -> Dict[str, Any]:
    nutrients = [
        (
            "Folic Acid (Vitamin B9)",
            "Essential for nucleotide synthesis and neural tube closure by Day 28 of embryonic development; prevents severe neural tube defects (spina bifida and anencephaly)",
            "Calcium",
        ),
        (
            "Iron",
            "Required for massive maternal and fetal hemoglobin synthesis and expansion of maternal blood volume, preventing severe gestational anemia and fetal fatigue",
            "Vitamin C",
        ),
        (
            "Calcium and Vitamin D",
            "Crucial for fetal skeletal mineralization and bone ossification without depleting maternal bone mineral density",
            "Vitamin K",
        ),
    ]
    name, role, distractor = rng.choice(nutrients)
    prompt = (
        f"Adequate maternal nutrition during the periconceptional period and pregnancy is critical for normal embryonic organogenesis.\n\n"
        f"What is the primary medical reason for recommending adequate dietary intake of **{name}**?"
    )
    correct = role
    distractors = [n[1] for n in nutrients if n[0] != name]
    distractors.append("Ensures the developing embryo produces excess saliva to dissolve digestive toxins.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review essential prenatal nutritional requirements.\n"
        f"**Step 2:** Relate {name} to embryonic developmental health:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct rationale is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_33_{rng.randint(100000, 999999)}",
        "subskill": "33_maternal_lifestyle_diet_folic_acid_spina_bifida_prevention",
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
            "tier_1": f"Why is {name} prescribed before and during early pregnancy?",
            "tier_2": "Folic acid prevents spina bifida/neural tube defects; iron prevents maternal-fetal anemia.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["prenatal_nutrition_folic_acid_spina_bifida_misconception"],
    }


# 34. Stages of labor and birth cervical dilation delivery afterbirth
def arch_34_stages_of_labor_and_birth_cervical_dilation_delivery_afterbirth(rng: random.Random) -> Dict[str, Any]:
    stages = [
        (
            "Stage 1: Dilation stage",
            "Regular uterine contractions widen and thin the cervix from 0 cm until it reaches full dilation at 10 cm; amniotic sac usually ruptures ('water breaks')",
            "Stage 1",
        ),
        (
            "Stage 2: Expulsion / Delivery stage",
            "Full cervical dilation to the birth of the baby; strong abdominal and myometrial contractions push the infant head-first ('crowning') through the birth canal",
            "Stage 2",
        ),
        (
            "Stage 3: Afterbirth / Placental stage",
            "Within 15-30 minutes after delivery, the uterus contracts strongly to detach and expel the placenta and umbilical membranes, closing maternal spiral arteries",
            "Stage 3",
        ),
    ]
    st_name, details, stage_num = rng.choice(stages)
    prompt = (
        f"Parturition (childbirth) proceeds through three distinct chronological stages.\n\n"
        f"Which clinical events define **{st_name}**?"
    )
    correct = details
    distractors = [s[1] for s in stages if s[0] != st_name]
    distractors.append("The fetus is reabsorbed back into the fallopian tubes for 6 more months.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the chronological progression of childbirth.\n"
        f"**Step 2:** Match {st_name} to its clinical milestones:\n"
        f"- {st_name}: {correct}\n\n"
        f"**Step 3:** The correct description is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_34_{rng.randint(100000, 999999)}",
        "subskill": "34_stages_of_labor_and_birth_cervical_dilation_delivery_afterbirth",
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
            "tier_1": f"Think about whether {st_name} is opening the cervix, pushing the baby out, or expelling the placenta.",
            "tier_2": "Stage 1: Cervical dilation to 10 cm; Stage 2: Fetal delivery; Stage 3: Expulsion of placenta/afterbirth.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["stages_of_labor_and_parturition_sequence_misconception"],
    }


# 35. Parturition hormones oxytocin prostaglandins positive feedback
def arch_35_parturition_hormones_oxytocin_prostaglandins_positive_feedback(rng: random.Random) -> Dict[str, Any]:
    mechanisms = [
        (
            "Oxytocin positive feedback loop (Ferguson reflex)",
            "Fetal head pushes against cervix -> stretch receptors send nerve signals to hypothalamus -> posterior pituitary releases more oxytocin -> oxytocin stimulates stronger uterine contractions -> stronger push on cervix -> repeats with escalating intensity until birth",
        ),
        (
            "Prostaglandins",
            "Synthesized locally by the placenta and uterine tissues in response to oxytocin, softening the cervix and coordinating smooth muscle contractility",
        ),
        (
            "Progesterone withdrawal",
            "Drop in circulating progesterone relative to estrogen removes the calming block on uterine muscle, enabling rhythmic myometrial contractions",
        ),
    ]
    name, mechanism = rng.choice(mechanisms)
    prompt = (
        f"Labor is initiated and intensified through a powerful neuroendocrine positive feedback loop.\n\n"
        f"Which statement describes the action of: **{name}**?"
    )
    correct = mechanism
    distractors = [m[1] for m in mechanisms if m[0] != name]
    distractors.append("Insulin and glucagon oscillate to digest the pelvic bones before contraction.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze endocrine regulation of labor.\n"
        f"**Step 2:** Relate {name} to hormonal actions:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_35_{rng.randint(100000, 999999)}",
        "subskill": "35_parturition_hormones_oxytocin_prostaglandins_positive_feedback",
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
            "tier_1": "Recall how oxytocin and cervical stretching form a positive feedback loop.",
            "tier_2": "Cervical stretch stimulates oxytocin release, which triggers stronger contractions, further stretching the cervix.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["parturition_hormones_oxytocin_positive_feedback_misconception"],
    }


# 36. Lactation and breastfeeding prolactin oxytocin let down colostrum
def arch_36_lactation_and_breastfeeding_prolactin_oxytocin_let_down_colostrum(rng: random.Random) -> Dict[str, Any]:
    elements = [
        (
            "Prolactin (Anterior Pituitary)",
            "Stimulates glandular alveolar cells in mammary glands to continuously synthesize and produce milk",
        ),
        (
            "Oxytocin (Posterior Pituitary)",
            "Stimulates contraction of myoepithelial cells surrounding mammary alveoli to eject milk into lactiferous ducts ('let-down / milk ejection reflex')",
        ),
        (
            "Colostrum",
            "Thick, yellowish fluid produced during the first 2-4 days postpartum; rich in proteins, minerals, and maternal secretory IgA antibodies establishing neonatal gut immunity",
        ),
    ]
    name, role = rng.choice(elements)
    prompt = (
        f"Lactation is regulated by infant suckling reflexes stimulating hormone release from the pituitary gland.\n\n"
        f"What is the specialized physiological role of **{name}**?"
    )
    correct = role
    distractors = [e[1] for e in elements if e[0] != name]
    distractors.append("Acts as a strong digestive enzyme that dissolves calcium in the baby's stomach.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze lactation physiology.\n"
        f"**Step 2:** Relate {name} to breast milk production or delivery:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct functional role is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_36_{rng.randint(100000, 999999)}",
        "subskill": "36_lactation_and_breastfeeding_prolactin_oxytocin_let_down_colostrum",
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
            "tier_1": f"Distinguish between milk PRODUCTION (prolactin) vs milk EJECTION (oxytocin).",
            "tier_2": "Prolactin produces milk; oxytocin ejects milk ('let-down'); colostrum provides first antibody immunity.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["lactation_prolactin_vs_oxytocin_colostrum_misconception"],
    }


# 37. Contraception barrier methods male female condoms sti prevention
def arch_37_contraception_barrier_methods_male_female_condoms_sti_prevention(rng: random.Random) -> Dict[str, Any]:
    methods = [
        (
            "Male Latex Condom",
            "Sheath unrolled over erect penis before intercourse; captures ejaculated semen and physically prevents sperm and genital pathogens from entering the vagina; prevents STIs",
        ),
        (
            "Female Condom (Femidom)",
            "Polyurethane sheath with flexible rings inserted into the vagina before intercourse; lines the vaginal walls and cervix to block semen entry and protect against STIs",
        ),
        (
            "Diaphragm / Cervical Cap with Spermicide",
            "Flexible dome-shaped silicone cup fitted over the cervix; blocks sperm entry into uterus but does NOT protect against viral sexually transmitted infections (STIs)",
        ),
    ]
    name, profile = rng.choice(methods)
    prompt = (
        f"Barrier methods of contraception physically prevent spermatozoa from reaching the ovum.\n\n"
        f"Which clinical profile accurately describes the mechanism and STI protection of the **{name}**?"
    )
    correct = profile
    distractors = [m[1] for m in methods if m[0] != name]
    distractors.append("Permanently alters chromosome number in sperm cells via electrical currents.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review barrier contraceptive mechanisms and dual-protection benefits.\n"
        f"**Step 2:** Match {name} to medical characteristics:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The accurate profile is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_37_{rng.randint(100000, 999999)}",
        "subskill": "37_contraception_barrier_methods_male_female_condoms_sti_prevention",
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
            "tier_1": f"Does the {name} provide protection against both pregnancy and STIs?",
            "tier_2": "Only male and female condoms offer dual protection against pregnancy AND sexually transmitted infections (STIs/HIV).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["contraceptive_barrier_methods_and_sti_protection_misconception"],
    }


# 38. Contraception hormonal methods pill injection implant mechanism
def arch_38_contraception_hormonal_methods_pill_injection_implant_mechanism(rng: random.Random) -> Dict[str, Any]:
    methods = [
        (
            "Combined Oral Contraceptive Pill (Estrogen + Progestin)",
            "Inhibits pituitary FSH and LH secretion to prevent ovulation; thickens cervical mucus to impede sperm entry; thins endometrium",
            "Taken orally once daily at the same time",
        ),
        (
            "Contraceptive Injection (e.g. Depo-Provera / Petogen)",
            "Long-acting progestin depot inhibiting the LH surge to suppress ovulation and creating hostile cervical mucus",
            "Administered intramuscularly every 2 to 3 months",
        ),
        (
            "Subdermal Hormone Implant (e.g. Implanon)",
            "Flexible rod releasing steady low-dose progestin to consistently suppress ovulation and thicken cervical mucus",
            "Inserted under skin of upper arm; effective for 3 to 5 years",
        ),
    ]
    name, mechanism, regimen = rng.choice(methods)
    prompt = (
        f"Hormonal contraceptives manipulate endocrine feedback loops to prevent unintended pregnancy.\n\n"
        f"What is the primary physiological mechanism and administration profile of the **{name}**?"
    )
    correct = f"Mechanism: {mechanism}.\nAdministration: {regimen}."
    alt = [m for m in methods if m[0] != name][0]
    options = [
        correct,
        f"Mechanism: {alt[1]}.\nAdministration: {alt[2]}.",
        "Mechanism: Physically severs the fallopian tubes using ultrasonic vibrations.\nAdministration: Weekly topical cream.",
        "Mechanism: Completely eliminates all white blood cells from the reproductive tract.\nAdministration: Inhaled aerosol.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze hormonal contraceptive mode of action.\n"
        f"**Step 2:** Threefold mechanism of hormonal methods:\n"
        f"1. Suppress ovulation by inhibiting pituitary FSH and LH surges.\n"
        f"2. Thicken cervical mucus barrier.\n"
        f"3. Thin endometrial lining to prevent implantation.\n\n"
        f"**Step 3:** The correct profile is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_38_{rng.randint(100000, 999999)}",
        "subskill": "38_contraception_hormonal_methods_pill_injection_implant_mechanism",
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
            "tier_1": f"How do synthetic hormones in {name} prevent pregnancy?",
            "tier_2": "Synthetic progesterone/estrogen inhibit FSH and LH to prevent ovulation, and thicken cervical mucus.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["hormonal_contraception_ovulation_inhibition_misconception"],
    }


# 39. Contraception intrauterine devices copper vs hormonal iud
def arch_39_contraception_intrauterine_devices_copper_vs_hormonal_iud(rng: random.Random) -> Dict[str, Any]:
    types = [
        (
            "Copper Intrauterine Device (Copper IUD / Loop)",
            "Releases copper ions into the uterine cavity, creating a sterile inflammatory response toxic to sperm (impairs motility and viability) and preventing fertilization without hormones",
            "Effective for 5 to 10 years; non-hormonal",
        ),
        (
            "Hormonal Intrauterine System (e.g. Mirena / Levonorgestrel IUD)",
            "Slowly releases progestin directly into the uterine cavity, dramatically thickening cervical mucus and thinning the endometrium to prevent fertilization and implantation",
            "Effective for 5 to 7 years; hormonal",
        ),
    ]
    name, mechanism, duration = rng.choice(types)
    prompt = (
        f"Intrauterine devices (IUDs) are small T-shaped devices placed inside the uterine cavity by a healthcare provider.\n\n"
        f"What is the contraceptive mechanism of the **{name}**?"
    )
    correct = f"Mechanism: {mechanism} ({duration})."
    alt = [t for t in types if t[0] != name][0]
    options = [
        correct,
        f"Mechanism: {alt[1]} ({alt[2]}).",
        "Mechanism: Clamps the vagina shut using a metal spring lock.\n(Effective for 2 weeks).",
        "Mechanism: Releases high doses of insulin that digest spermatozoa before ejaculation.\n(Effective for 1 month).",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Differentiate copper IUD from hormonal IUS.\n"
        f"**Step 2:** Match {name}:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The accurate statement is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_39_{rng.randint(100000, 999999)}",
        "subskill": "39_contraception_intrauterine_devices_copper_vs_hormonal_iud",
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
            "tier_1": f"Is {name} copper-based (spermicidal ions) or hormone-releasing?",
            "tier_2": "Copper IUD is non-hormonal and toxic to sperm; hormonal IUS releases progestin to thicken mucus and thin endometrium.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["intrauterine_device_copper_vs_hormonal_mechanism_misconception"],
    }


# 40. Contraception permanent surgical vasectomy and tubal ligation
def arch_40_contraception_permanent_surgical_vasectomy_and_tubal_ligation(rng: random.Random) -> Dict[str, Any]:
    procedures = [
        (
            "Vasectomy (Male Sterilization)",
            "The vas deferens (sperm ducts) are surgically cut, tied, or cauterized",
            "Sperm produced in the testes cannot travel to the ejaculatory ducts; semen is still ejaculated normally (secreted by seminal vesicles and prostate) but contains zero sperm",
            "testosterone production and erection remain completely unaffected",
        ),
        (
            "Tubal Ligation (Female Sterilization / 'Tubes Tied')",
            "Both fallopian tubes (oviducts) are surgically cut, clipped, or cauterized",
            "Secondary oocytes released from ovaries cannot travel down the tube to meet sperm, and sperm cannot reach the egg; fertilization is permanently prevented",
            "menstrual cycles and ovarian hormone secretion (estrogen and progesterone) continue normally",
        ),
    ]
    name, surgery, effect, hormone_fact = rng.choice(procedures)
    prompt = (
        f"Sterilization is a permanent surgical method of contraception chosen when an individual or couple desires no future children.\n\n"
        f"Which clinical explanation accurately describes **{name}**?"
    )
    correct = f"Procedure: {surgery}.\nPhysiological result: {effect};\nEndocrine status: {hormone_fact}."
    alt = [p for p in procedures if p[0] != name][0]
    options = [
        correct,
        f"Procedure: {alt[1]}.\nPhysiological result: {alt[2]};\nEndocrine status: {alt[3]}.",
        f"Procedure: Surgical removal of the entire urinary bladder.\nPhysiological result: Stops urine formation;\nEndocrine status: Causes instant menopause.",
        f"Procedure: Removal of the stomach.\nPhysiological result: Blocks food entry;\nEndocrine status: Shuts down all gonadotropins.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze surgical sterilization mechanics.\n"
        f"**Step 2:** Note key points for {name}:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The accurate clinical statement is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_40_{rng.randint(100000, 999999)}",
        "subskill": "40_contraception_permanent_surgical_vasectomy_and_tubal_ligation",
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
            "tier_1": f"Does {name} block gamete transport or remove hormone-producing glands?",
            "tier_2": "Vasectomy cuts vas deferens (semen still produced without sperm); tubal ligation cuts fallopian tubes; neither affects hormones.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["surgical_sterilization_vasectomy_tubal_ligation_misconception"],
    }


# 41. Contraception natural methods rhythm withdrawal efficacy limitations
def arch_41_contraception_natural_methods_rhythm_withdrawal_efficacy_limitations(rng: random.Random) -> Dict[str, Any]:
    methods = [
        (
            "Withdrawal method (Coitus interruptus)",
            "The male pulls the penis out of the vagina before ejaculation",
            "High failure rate (up to 20-25%): pre-ejaculatory fluid emitted by Cowper's glands often contains viable spermatozoa, and timing errors occur frequently; offers zero STI protection",
        ),
        (
            "Calendar / Rhythm method",
            "Tracking cycle lengths to estimate the fertile window (ovulation +/- days) and abstaining from intercourse during fertile days",
            "High failure rate (up to 25%): natural biological cycles vary due to stress, illness, or hormonal fluctuations, making exact ovulation timing unpredictable; zero STI protection",
        ),
        (
            "Basal Body Temperature (BBT) & Cervical Mucus method",
            "Daily recording of resting morning temperature (rises 0.3-0.5°C after ovulation under progesterone) and monitoring stretchy clear cervical mucus (spinnbarkeit)",
            "Moderate to high failure rate when used imperfectly: temperature rises only AFTER ovulation has already occurred; requires strict compliance; zero STI protection",
        ),
    ]
    name, mechanism, limitation = rng.choice(methods)
    prompt = (
        f"Natural / behavioral family planning methods do not use pharmaceutical drugs or barrier devices.\n\n"
        f"Which statement correctly evaluates the **{name}** and explains its high typical-use failure rate?"
    )
    correct = f"Technique: {mechanism}.\nLimitation: {limitation}."
    alt = [m for m in methods if m[0] != name][0]
    options = [
        correct,
        f"Technique: {alt[1]}.\nLimitation: {alt[2]}.",
        "Technique: Ingesting hot herbal water after sex.\nLimitation: 100% effective against HIV and all pathogens.",
        "Technique: Wearing heavy winter clothing during coitus.\nLimitation: Freezes sperm cells completely.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Evaluate natural family planning methods.\n"
        f"**Step 2:** Note high failure rate causes:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The accurate evaluation is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_41_{rng.randint(100000, 999999)}",
        "subskill": "41_contraception_natural_methods_rhythm_withdrawal_efficacy_limitations",
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
            "tier_1": f"Why is {name} unreliable for preventing pregnancy and STIs?",
            "tier_2": "Pre-ejaculatory fluid can contain viable sperm; cycle variation makes ovulation timing imprecise; zero STI defense.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["natural_family_planning_failure_rate_limitations_misconception"],
    }


# 42. Sexually transmitted infections hiv aids retrovirus cd4 lymphocytes
def arch_42_sexually_transmitted_infections_hiv_aids_retrovirus_cd4_lymphocytes(rng: random.Random) -> Dict[str, Any]:
    facts = [
        (
            "Mechanism of pathogenesis",
            "HIV is a retrovirus that binds to and infects CD4+ T-helper lymphocytes, replicating inside and destroying them, progressively collapsing cell-mediated immunity",
        ),
        (
            "Modes of transmission",
            "Transmitted through unprotected sexual intercourse, infected blood transfusions, shared hypodermic needles, and vertically from mother to child (during gestation, birth, or breastfeeding)",
        ),
        (
            "Progression to AIDS",
            "Diagnosed when CD4+ T-cell count falls below 200 cells/uL or when opportunistic infections (e.g. tuberculosis, Kaposi's sarcoma, pneumocystis pneumonia) emerge",
        ),
        (
            "Antiretroviral Therapy (ART)",
            "Combination medication suppressing viral replication to undetectable levels ('Undetectable = Untransmittable' or U=U), allowing CD4 count recovery and preventing transmission",
        ),
    ]
    feature, detail = rng.choice(facts)
    prompt = (
        f"Human Immunodeficiency Virus (HIV) remains a critical public health challenge in South Africa.\n\n"
        f"Which biological statement accurately describes HIV regarding: **{feature}**?"
    )
    correct = detail
    distractors = [f[1] for f in facts if f[0] != feature]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze HIV virology, immunology, and transmission dynamics.\n"
        f"**Step 2:** Match {feature} to medical facts:\n"
        f"- {feature}: {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_42_{rng.randint(100000, 999999)}",
        "subskill": "42_sexually_transmitted_infections_hiv_aids_retrovirus_cd4_lymphocytes",
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
            "tier_1": f"Recall how HIV infects and destroys CD4+ T-helper immune cells.",
            "tier_2": "HIV destroys CD4 cells leading to opportunistic infections (TB); ART suppresses viral load to undetectable levels.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["hiv_pathogenesis_cd4_t_cells_art_misconception"],
    }


# 43. Sexually transmitted infections syphilis treponema pallidum stages
def arch_43_sexually_transmitted_infections_syphilis_treponema_pallidum_stages(rng: random.Random) -> Dict[str, Any]:
    stages = [
        (
            "Primary stage",
            "Appearance of a single, painless, firm, ulcerated sore called a chancre at the initial infection site (genitals, anus, or mouth) that heals spontaneously after 3-6 weeks",
        ),
        (
            "Secondary stage",
            "Disseminated spirochetemia marked by non-itchy copper-red skin rashes on the palms of hands and soles of feet, fever, and mucous patches",
        ),
        (
            "Tertiary stage",
            "Develops years later if untreated: destructive gummas in skin/bones, cardiovascular syphilis (aortic aneurysm), and neurosyphilis causing dementia, paralysis, or blindness",
        ),
    ]
    name, symptoms = rng.choice(stages)
    prompt = (
        f"Syphilis is a complex sexually transmitted infection caused by the spirochete bacterium *Treponema pallidum*.\n\n"
        f"Which clinical manifestation defines the **{name}** of syphilis?"
    )
    correct = symptoms
    distractors = [s[1] for s in stages if s[0] != name]
    distractors.append("Immediate transformation of red blood cells into fungal spores within 5 minutes.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review stages of syphilis (*Treponema pallidum*).\n"
        f"**Step 2:** Match {name} to clinical presentation:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct clinical manifestation is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_43_{rng.randint(100000, 999999)}",
        "subskill": "43_sexually_transmitted_infections_syphilis_treponema_pallidum_stages",
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
            "tier_1": f"Think about whether {name} is the initial chancre, body rash, or organ-destroying tertiary damage.",
            "tier_2": "Primary = painless chancre; Secondary = rash on palms/soles; Tertiary = neurological/cardiovascular damage.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["syphilis_treponema_pallidum_stages_chancre_misconception"],
    }


# 44. Sexually transmitted infections gonorrhea chlamydia pelvic inflammatory disease
def arch_44_sexually_transmitted_infections_gonorrhea_chlamydia_pelvic_inflammatory_disease(rng: random.Random) -> Dict[str, Any]:
    stis = [
        (
            "Gonorrhea (*Neisseria gonorrhoeae*)",
            "Gram-negative diplococcus causing purulent urethral discharge (thick yellow/green pus) and painful urination (dysuria) in males; often asymptomatic in females but ascends to cause pelvic inflammatory disease (PID)",
        ),
        (
            "Chlamydia (*Chlamydia trachomatis*)",
            "Obligate intracellular bacterium; frequently asymptomatic ('silent infection') in up to 70% of women, but causes silent scarring and occlusion of fallopian tubes leading to tubal factor infertility and ectopic pregnancy",
        ),
        (
            "Pelvic Inflammatory Disease (PID)",
            "Polymicrobial upper genital tract infection caused by ascending untreated gonorrhea or chlamydia from cervix to uterus and fallopian tubes, causing permanent tubal scarring and chronic pelvic pain",
        ),
    ]
    name, pathology = rng.choice(stis)
    prompt = (
        f"Bacterial sexually transmitted infections of the urogenital tract can cause severe reproductive sequelae if left untreated.\n\n"
        f"What is the clinical presentation and reproductive complication associated with **{name}**?"
    )
    correct = pathology
    distractors = [s[1] for s in stis if s[0] != name]
    distractors.append("Causes the rapid growth of extra finger bones inside the pelvic cavity.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze bacterial STIs and complications.\n"
        f"**Step 2:** Relate {name} to clinical pathology:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct pathology profile is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_44_{rng.randint(100000, 999999)}",
        "subskill": "44_sexually_transmitted_infections_gonorrhea_chlamydia_pelvic_inflammatory_disease",
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
            "tier_1": f"Consider the causative bacterium and long-term risks of: {name}.",
            "tier_2": "Untreated gonorrhea and chlamydia ascend the tract causing PID, scarring fallopian tubes, and causing infertility.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["gonorrhea_chlamydia_pid_infertility_misconception"],
    }


# 45. STI prevention treatment condoms antibiotics arvs abstinence
def arch_45_sti_prevention_treatment_condoms_antibiotics_arvs_abstinence(rng: random.Random) -> Dict[str, Any]:
    interventions = [
        (
            "Bacterial STIs (Gonorrhea, Chlamydia, Syphilis)",
            "Can be fully cured with appropriate antibiotic regimens (e.g. penicillin for syphilis, ceftriaxone/azithromycin for gonorrhea/chlamydia); partners must be treated simultaneously",
            "Curable with antibiotics",
        ),
        (
            "Viral STIs (HIV, HPV, Herpes Simplex / HSV)",
            "Cannot be cured with antibiotics; managed and suppressed with antiviral medications (ARVs for HIV, acyclovir for HSV), and preventable via vaccination (HPV vaccine)",
            "Incurable by antibiotics; managed by antivirals/vaccines",
        ),
        (
            "Barrier Dual Protection",
            "Consistent and correct use of latex condoms during every sexual encounter provides effective dual protection against both unintended pregnancy and transmission of STIs/HIV",
            "Preventable via consistent condom use",
        ),
    ]
    name, explanation, key = rng.choice(interventions)
    prompt = (
        f"Public health approaches to sexually transmitted infections (STIs) combine primary prevention, screening, and pharmacological treatment.\n\n"
        f"Which clinical principle accurately distinguishes the treatment and prevention of **{name}**?"
    )
    correct = explanation
    distractors = [i[1] for i in interventions if i[0] != name]
    distractors.append("All STIs can be permanently eliminated from the body by drinking cold saltwater.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish bacterial from viral STI treatment paradigms.\n"
        f"**Step 2:** Match {name}:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct clinical principle is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_45_{rng.randint(100000, 999999)}",
        "subskill": "45_sti_prevention_treatment_condoms_antibiotics_arvs_abstinence",
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
            "tier_1": f"Are {name} caused by bacteria (curable with antibiotics) or viruses (managed with antivirals)?",
            "tier_2": "Bacteria = antibiotics cure (syphilis, gonorrhea); Viruses = antivirals manage, no antibiotic cure (HIV, herpes).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["sti_prevention_antibiotics_vs_antivirals_misconception"],
    }


# 46. Infertility male causes low sperm count motility varicocele
def arch_46_infertility_male_causes_low_sperm_count_motility_varicocele(rng: random.Random) -> Dict[str, Any]:
    causes = [
        (
            "Oligospermia / Azoospermia (Low/Zero sperm count)",
            "Semen contains fewer than 15 million sperm per mL (or no sperm), reducing the mathematical probability of a spermatozoon reaching the ovum",
        ),
        (
            "Asthenospermia (Poor sperm motility)",
            "Spermatozoa exhibit abnormal flagellar kinematics or defective mitochondrial ATP generation, preventing them from swimming through cervical mucus and up the fallopian tube",
        ),
        (
            "Varicocele",
            "Enlarged, varicose veins in the pampiniform plexus of the scrotum causing increased scrotal temperature that impairs testicular spermatogenesis",
        ),
        (
            "Testicular hyperthermia (e.g. tight clothing, prolonged fever)",
            "Disrupts the essential 2-3°C sub-core temperature differential required for optimal meiosis in seminiferous tubules, causing morphologically abnormal sperm",
        ),
    ]
    cause_name, pathology = rng.choice(causes)
    prompt = (
        f"Infertility is medically defined as the inability to conceive after 12 months of regular unprotected sexual intercourse.\n\n"
        f"Which biological mechanism explains how **{cause_name}** causes male infertility?"
    )
    correct = pathology
    distractors = [c[1] for c in causes if c[0] != cause_name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze male infertility etiologies.\n"
        f"**Step 2:** Relate {cause_name} to pathophysiological mechanism:\n"
        f"- {cause_name}: {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_46_{rng.randint(100000, 999999)}",
        "subskill": "46_infertility_male_causes_low_sperm_count_motility_varicocele",
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
            "tier_1": f"How does {cause_name} affect sperm count, movement, or production?",
            "tier_2": "Varicocele raises scrotal heat; asthenospermia impairs swimming; oligospermia means low sperm count.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["male_infertility_sperm_motility_varicocele_misconception"],
    }


# 47. Infertility female causes blocked fallopian tubes anovulation endometriosis
def arch_47_infertility_female_causes_blocked_fallopian_tubes_anovulation_endometriosis(rng: random.Random) -> Dict[str, Any]:
    causes = [
        (
            "Tubal occlusion (Blocked Fallopian Tubes)",
            "Scar tissue from untreated pelvic inflammatory disease (PID) or past infections creates a physical barrier blocking sperm passage and trapping the ovum",
        ),
        (
            "Anovulation / Polycystic Ovary Syndrome (PCOS)",
            "Hormonal imbalances (elevated androgens and LH/FSH dysregulation) prevent ovarian follicles from maturing and rupturing, meaning no ovum is released for fertilization",
        ),
        (
            "Endometriosis",
            "Endometrial tissue grows outside the uterus (on ovaries, oviducts, or pelvic peritoneum), bleeding cyclically, causing adhesions, chronic pelvic inflammation, and distorted pelvic anatomy",
        ),
    ]
    name, pathology = rng.choice(causes)
    prompt = (
        f"Female reproductive dysfunction accounts for approximately 40-50% of clinical infertility presentations.\n\n"
        f"Which biological mechanism explains how **{name}** impairs fertility?"
    )
    correct = pathology
    distractors = [c[1] for c in causes if c[0] != name]
    distractors.append("Causes direct transformation of the ovaries into extra liver lobes.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze female infertility etiologies.\n"
        f"**Step 2:** Relate {name} to physiological mechanism:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The accurate explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_47_{rng.randint(100000, 999999)}",
        "subskill": "47_infertility_female_causes_blocked_fallopian_tubes_anovulation_endometriosis",
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
            "tier_1": f"Recall how {name} disrupts ovulation, egg transport, or embryo implantation.",
            "tier_2": "Blocked tubes prevent gamete meeting; anovulation means no egg released; endometriosis causes ectopic endometrial scarring.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["female_infertility_tubal_blockage_pcos_endometriosis_misconception"],
    }


# 48. Assisted reproductive technology ivf in vitro fertilization steps
def arch_48_assisted_reproductive_technology_ivf_in_vitro_fertilization_steps(rng: random.Random) -> Dict[str, Any]:
    steps = [
        (
            "Step 1: Ovarian hyperstimulation",
            "Injectable gonadotropins (FSH) stimulate the ovaries to mature multiple Graafian follicles simultaneously rather than a single dominant follicle",
        ),
        (
            "Step 2: Egg retrieval (Oocyte aspiration)",
            "Under ultrasound guidance, mature oocytes are aspirated from ovarian follicles using a fine needle inserted through the vaginal wall",
        ),
        (
            "Step 3: In vitro fertilization & culture",
            "Sperm and harvested eggs are combined in a specialized culture dish (or via intracytoplasmic sperm injection / ICSI) in the laboratory to produce cleavage-stage embryos",
        ),
        (
            "Step 4: Embryo transfer",
            "One or two high-grade blastocysts are transferred into the uterine cavity via a thin catheter through the cervix for natural endometrial implantation",
        ),
    ]
    st_name, st_desc = rng.choice(steps)
    prompt = (
        f"In Vitro Fertilization (IVF) is an assisted reproductive technology used to treat severe tubal factor, male factor, or unexplained infertility.\n\n"
        f"Which clinical procedure describes **{st_name}** in the standard IVF protocol?"
    )
    correct = st_desc
    distractors = [s[1] for s in steps if s[0] != st_name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review chronological sequence of IVF protocol:\n"
        f"1. Ovarian hyperstimulation -> 2. Egg retrieval -> 3. In vitro fertilization -> 4. Embryo transfer.\n\n"
        f"**Step 2:** Match {st_name}:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The correct procedural description is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_48_{rng.randint(100000, 999999)}",
        "subskill": "48_assisted_reproductive_technology_ivf_in_vitro_fertilization_steps",
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
            "tier_1": f"Think about where {st_name} occurs in the IVF procedure.",
            "tier_2": "Stimulate ovaries -> retrieve eggs -> fertilize in lab culture -> transfer embryo into uterus.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["in_vitro_fertilization_ivf_procedure_steps_misconception"],
    }


# 49. Twins formation monozygotic identical vs dizygotic fraternal
def arch_49_twins_formation_monozygotic_identical_vs_dizygotic_fraternal(rng: random.Random) -> Dict[str, Any]:
    types = [
        (
            "Monozygotic (Identical) Twins",
            "A single ovum is fertilized by a single sperm cell to form one zygote, which subsequently splits into two separate embryos during early cleavage; twins share 100% identical DNA and are always the same biological sex",
            "Always same sex, genetically identical, from 1 egg and 1 sperm",
        ),
        (
            "Dizygotic (Fraternal / Non-identical) Twins",
            "Two distinct ova are released simultaneously during ovulation and fertilized by two distinct spermatozoa; twins share approximately 50% of their genes (like ordinary siblings) and can be of the same or different biological sexes",
            "Can be different sexes, genetically distinct, from 2 eggs and 2 sperm",
        ),
    ]
    t_name, explanation, summary = rng.choice(types)
    prompt = (
        f"Multiple pregnancies can arise through distinct biological mechanisms in the female reproductive tract.\n\n"
        f"Which statement correctly explains the biological origin and genetic relationship of **{t_name}**?"
    )
    correct = explanation
    alt = [t for t in types if t[0] != t_name][0]
    options = [
        correct,
        alt[1],
        "Two sperm cells penetrate the same single egg at the exact same millisecond, doubling the baby's limbs.",
        "A single unfertilized egg divides by binary fission and implants in the liver without any sperm.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare biological mechanisms of twin development:\n"
        f"- Monozygotic (Identical): 1 egg + 1 sperm -> single zygote splits -> 100% genetically identical.\n"
        f"- Dizygotic (Fraternal): 2 eggs + 2 sperm -> two separate zygotes -> ~50% genetically related.\n\n"
        f"**Step 2:** Match {t_name}:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The accurate explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_49_{rng.randint(100000, 999999)}",
        "subskill": "49_twins_formation_monozygotic_identical_vs_dizygotic_fraternal",
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
            "tier_1": f"How many eggs and sperm form {t_name.split()[0]} twins?",
            "tier_2": "Monozygotic = 1 egg + 1 sperm that splits (identical); Dizygotic = 2 eggs + 2 sperm (fraternal).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["twins_monozygotic_vs_dizygotic_origin_misconception"],
    }


# 50. Teenage pregnancy socioeconomic educational and health impacts
def arch_50_teenage_pregnancy_socioeconomic_educational_and_health_impacts(rng: random.Random) -> Dict[str, Any]:
    impacts = [
        (
            "Obstetric and biological health risks for adolescent mothers",
            "Elevated risks of pre-eclampsia (pregnancy-induced hypertension), obstructed labor due to an incompletely developed maternal pelvic girdle (cephalopelvic disproportion), and anemia",
        ),
        (
            "Neonatal health outcomes for the infant",
            "Significantly higher incidence of prematurity, low birth weight (<2500 g), infant respiratory distress, and early childhood developmental delays",
        ),
        (
            "Educational and socioeconomic consequences",
            "High rates of school dropout, disruption of academic progression, persistent economic vulnerability, and perpetuation of intergenerational poverty cycles",
        ),
        (
            "Comprehensive prevention and youth-friendly clinical support",
            "Empowering adolescents through evidence-based comprehensive sexuality education, accessible youth-friendly reproductive clinics, and dual-protection contraception",
        ),
    ]
    topic, analysis = rng.choice(impacts)
    prompt = (
        f"Adolescent pregnancy carries multifaceted biological, public health, and social consequences.\n\n"
        f"Which evidence-based finding accurately reflects the **{topic}**?"
    )
    correct = analysis
    distractors = [i[1] for i in impacts if i[0] != topic]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze multifaceted dimensions of adolescent pregnancy.\n"
        f"**Step 2:** Relate to {topic}:\n"
        f"- {topic}: {correct}\n\n"
        f"**Step 3:** The correct evidence-based finding is: **{correct}**."
    )
    return {
        "id": f"ns9_rep_50_{rng.randint(100000, 999999)}",
        "subskill": "50_teenage_pregnancy_socioeconomic_educational_and_health_impacts",
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
            "tier_1": f"Consider the biological, social, and medical evidence surrounding: {topic}.",
            "tier_2": "Adolescent pregnancy increases obstetric complications (obstructed labor, pre-eclampsia), prematurity, and school interruption.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["adolescent_pregnancy_biological_and_social_impacts_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "26_implantation_blastocyst_trophoblast_and_endometrial_embedding": arch_26_implantation_blastocyst_trophoblast_and_endometrial_embedding,
    "27_gestation_and_trimesters_developmental_milestones": arch_27_gestation_and_trimesters_developmental_milestones,
    "28_placenta_structure_and_function_barrier_and_nutrient_gas_exchange": arch_28_placenta_structure_and_function_barrier_and_nutrient_gas_exchange,
    "29_umbilical_cord_two_arteries_one_vein_circulation": arch_29_umbilical_cord_two_arteries_one_vein_circulation,
    "30_amniotic_sac_and_fluid_cushioning_thermoregulation_protection": arch_30_amniotic_sac_and_fluid_cushioning_thermoregulation_protection,
    "31_maternal_lifestyle_teratogens_alcohol_fetal_alcohol_syndrome_fas": arch_31_maternal_lifestyle_teratogens_alcohol_fetal_alcohol_syndrome_fas,
    "32_maternal_lifestyle_smoking_nicotine_low_birth_weight_prematurity": arch_32_maternal_lifestyle_smoking_nicotine_low_birth_weight_prematurity,
    "33_maternal_lifestyle_diet_folic_acid_spina_bifida_prevention": arch_33_maternal_lifestyle_diet_folic_acid_spina_bifida_prevention,
    "34_stages_of_labor_and_birth_cervical_dilation_delivery_afterbirth": arch_34_stages_of_labor_and_birth_cervical_dilation_delivery_afterbirth,
    "35_parturition_hormones_oxytocin_prostaglandins_positive_feedback": arch_35_parturition_hormones_oxytocin_prostaglandins_positive_feedback,
    "36_lactation_and_breastfeeding_prolactin_oxytocin_let_down_colostrum": arch_36_lactation_and_breastfeeding_prolactin_oxytocin_let_down_colostrum,
    "37_contraception_barrier_methods_male_female_condoms_sti_prevention": arch_37_contraception_barrier_methods_male_female_condoms_sti_prevention,
    "38_contraception_hormonal_methods_pill_injection_implant_mechanism": arch_38_contraception_hormonal_methods_pill_injection_implant_mechanism,
    "39_contraception_intrauterine_devices_copper_vs_hormonal_iud": arch_39_contraception_intrauterine_devices_copper_vs_hormonal_iud,
    "40_contraception_permanent_surgical_vasectomy_and_tubal_ligation": arch_40_contraception_permanent_surgical_vasectomy_and_tubal_ligation,
    "41_contraception_natural_methods_rhythm_withdrawal_efficacy_limitations": arch_41_contraception_natural_methods_rhythm_withdrawal_efficacy_limitations,
    "42_sexually_transmitted_infections_hiv_aids_retrovirus_cd4_lymphocytes": arch_42_sexually_transmitted_infections_hiv_aids_retrovirus_cd4_lymphocytes,
    "43_sexually_transmitted_infections_syphilis_treponema_pallidum_stages": arch_43_sexually_transmitted_infections_syphilis_treponema_pallidum_stages,
    "44_sexually_transmitted_infections_gonorrhea_chlamydia_pelvic_inflammatory_disease": arch_44_sexually_transmitted_infections_gonorrhea_chlamydia_pelvic_inflammatory_disease,
    "45_sti_prevention_treatment_condoms_antibiotics_arvs_abstinence": arch_45_sti_prevention_treatment_condoms_antibiotics_arvs_abstinence,
    "46_infertility_male_causes_low_sperm_count_motility_varicocele": arch_46_infertility_male_causes_low_sperm_count_motility_varicocele,
    "47_infertility_female_causes_blocked_fallopian_tubes_anovulation_endometriosis": arch_47_infertility_female_causes_blocked_fallopian_tubes_anovulation_endometriosis,
    "48_assisted_reproductive_technology_ivf_in_vitro_fertilization_steps": arch_48_assisted_reproductive_technology_ivf_in_vitro_fertilization_steps,
    "49_twins_formation_monozygotic_identical_vs_dizygotic_fraternal": arch_49_twins_formation_monozygotic_identical_vs_dizygotic_fraternal,
    "50_teenage_pregnancy_socioeconomic_educational_and_health_impacts": arch_50_teenage_pregnancy_socioeconomic_educational_and_health_impacts,
}
