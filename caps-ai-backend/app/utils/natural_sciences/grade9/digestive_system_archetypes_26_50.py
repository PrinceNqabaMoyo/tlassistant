"""Grade 9 Natural Sciences: Term 1 - Digestive System (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 1/02. Systems in the human body.md & digestive curriculum requirements.
Focus: Laboratory food tests (Iodine, Benedict's, Biuret, Ethanol emulsion), balanced diet, deficiency diseases (Kwashiorkor, Marasmus, Scurvy, Rickets, Anemia, Goiter), eating disorders, gastrointestinal pathologies, enzyme kinetics, and dialysis tubing model.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Food test iodine test for starch blue black coloration
def arch_26_food_test_iodine_test_for_starch_blue_black_coloration(rng: random.Random) -> Dict[str, Any]:
    samples = [
        ("Milled maize meal suspension", True, "blue-black / dark blue", "contains abundant complex starch polysaccharides that react with iodine"),
        ("Boiled egg white solution", False, "yellow-brown / amber", "contains pure albumin protein and lacks starch"),
        ("Dilute sucrose solution", False, "yellow-brown / amber", "contains simple disaccharide sugar and lacks starch"),
        ("Pure sunflower cooking oil", False, "yellow-brown / amber", "contains pure triglycerides and lacks starch"),
    ]
    food, has_starch, color, reason = rng.choice(samples)
    prompt = (
        f"A learner adds a few drops of yellowish-brown dilute iodine solution to a test tube containing **{food}**.\n\n"
        f"What color change is observed, and what biological conclusion is drawn?"
    )
    correct = f"Color observed: {color}; Conclusion: {reason}."
    wrong_color = "yellow-brown / amber" if has_starch else "blue-black / dark blue"
    wrong_reason = "indicates absence of starch" if has_starch else "indicates high concentration of starch"
    options = [
        correct,
        f"Color observed: {wrong_color}; Conclusion: {wrong_reason}.",
        "Color observed: bright magenta; Conclusion: indicates presence of radioactive iodine gas.",
        "Color observed: milky white; Conclusion: indicates complete absence of water.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze chemical test for starch:\n"
        f"- Reagent: Iodine solution (yellow-brown).\n"
        f"- Positive result: Color changes to blue-black.\n"
        f"- Negative result: Remains yellow-brown.\n"
        f"**Step 2:** Sample: {food} -> Starch present = {has_starch}.\n\n"
        f"**Step 3:** The correct observation and conclusion is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_26_{rng.randint(100000, 999999)}",
        "subskill": "26_food_test_iodine_test_for_starch_blue_black_coloration",
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
            "tier_1": f"Does {food} contain starch? What color does iodine turn in the presence of starch?",
            "tier_2": "Iodine turns blue-black with starch; it stays yellow-brown if starch is absent.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["food_test_iodine_starch_blue_black_misconception"],
    }


# 27. Food test benedicts test for reducing sugars color gradient
def arch_27_food_test_benedicts_test_for_reducing_sugars_color_gradient(rng: random.Random) -> Dict[str, Any]:
    levels = [
        ("high concentration of glucose", "brick-red precipitate", "Large quantity of copper(II) ions reduced to insoluble copper(I) oxide precipitate"),
        ("moderate concentration of maltose", "orange to yellow precipitate", "Moderate reduction of cupric ions by reducing sugar aldehyde/ketone groups"),
        ("low trace concentration of glucose", "green precipitate", "Slight reduction of cupric ions forming a trace precipitate"),
        ("zero reducing sugars (distilled water control)", "remains clear blue", "Zero reduction occurs; cupric ions remain in copper(II) sulfate state"),
    ]
    conc, color, chemistry = rng.choice(levels)
    prompt = (
        f"Benedict's test requires heating a food mixture with bright blue Benedict's reagent in a boiling water bath for 3 to 5 minutes.\n\n"
        f"If the tested solution contains **{conc}**, what color change occurs, and what chemical event causes it?"
    )
    correct = f"Color result: {color}; Explanation: {chemistry}."
    alt = [l for l in levels if l[0] != conc][0]
    options = [
        correct,
        f"Color result: {alt[1]}; Explanation: {alt[2]}.",
        "Color result: pitch black; Explanation: Complete combustion of glucose into charcoal.",
        "Color result: fluorescent purple; Explanation: Precipitation of pure protein crystals.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review Benedict's semi-quantitative color scale:\n"
        f"- Blue (none) -> Green (trace) -> Yellow/Orange (moderate) -> Brick-red (high).\n"
        f"**Step 2:** Match {conc}:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The correct result is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_27_{rng.randint(100000, 999999)}",
        "subskill": "27_food_test_benedicts_test_for_reducing_sugars_color_gradient",
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
            "tier_1": f"Recall the color scale of Benedict's test for: {conc}.",
            "tier_2": "Blue = 0; Green = trace; Yellow/Orange = moderate; Brick-red = high reducing sugars.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["food_test_benedicts_reducing_sugars_gradient_misconception"],
    }


# 28. Food test biuret test for proteins violet purple coloration
def arch_28_food_test_biuret_test_for_proteins_violet_purple_coloration(rng: random.Random) -> Dict[str, Any]:
    samples = [
        ("Dilute fresh milk suspension", True, "violet / purple", "Cu2+ ions form coordination complexes with peptide bonds (-CO-NH-) linking amino acids"),
        ("Dilute egg albumin solution", True, "violet / purple", "High concentration of polypeptide chains complex with copper(II) ions in alkaline solution"),
        ("Pure cornstarch solution", False, "remains pale blue", "Contains glycosidic carbohydrate bonds and lacks peptide bonds"),
        ("Refined cane sugar syrup", False, "remains pale blue", "Contains disaccharide sugar molecules and lacks peptide bonds"),
    ]
    sample, has_protein, color, chemistry = rng.choice(samples)
    prompt = (
        f"To test for protein, a student adds dilute sodium hydroxide (NaOH) followed by a few drops of 1% copper(II) sulfate (CuSO4) to **{sample}**.\n\n"
        f"What color is observed, and what chemical bond does the Biuret test detect?"
    )
    correct = f"Color: {color}; Chemical basis: {chemistry}."
    wrong_color = "remains pale blue" if has_protein else "violet / purple"
    wrong_chem = "lacks peptide bonds" if has_protein else "detects abundant peptide bonds"
    options = [
        correct,
        f"Color: {wrong_color}; Chemical basis: {wrong_chem}.",
        "Color: bright orange; Chemical basis: detects fatty acid ester bonds.",
        "Color: deep emerald green; Chemical basis: detects chlorophyll molecules.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze Biuret test for proteins:\n"
        f"- Reagents: Alkaline NaOH + dilute CuSO4.\n"
        f"- Detects: Peptide bonds in polypeptide chains.\n"
        f"- Positive: Violet / purple coloration.\n"
        f"- Negative: Pale blue.\n"
        f"**Step 2:** Sample: {sample} -> Protein present = {has_protein}.\n\n"
        f"**Step 3:** The correct observation is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_28_{rng.randint(100000, 999999)}",
        "subskill": "28_food_test_biuret_test_for_proteins_violet_purple_coloration",
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
            "tier_1": f"Does {sample} contain protein? What color does the Biuret test turn for proteins?",
            "tier_2": "Biuret test turns violet/purple in the presence of peptide bonds in proteins.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["food_test_biuret_protein_peptide_bonds_misconception"],
    }


# 29. Food test ethanol emulsion test for lipids cloudy white
def arch_29_food_test_ethanol_emulsion_test_for_lipids_cloudy_white(rng: random.Random) -> Dict[str, Any]:
    samples = [
        ("Crushed roasted peanut extract", True, "a cloudy-white milky emulsion forms", "Lipids dissolve in absolute ethanol but are insoluble in water, precipitating as microscopic suspended fat droplets"),
        ("Pure sunflower oil", True, "a cloudy-white milky emulsion forms", "Hydrophobic triglycerides dissolve in alcohol and precipitate out when mixed with water"),
        ("Apple juice extract", False, "solution remains completely clear and transparent", "Soluble sugars dissolve in both alcohol and water without forming an emulsion"),
        ("Egg white solution", False, "solution remains clear or forms coarse white protein flakes without a milky emulsion", "Water-soluble albumin lacks lipid content"),
    ]
    food, has_lipid, observation, mechanism = rng.choice(samples)
    prompt = (
        f"In the ethanol emulsion test, a chopped food sample is shaken with absolute ethanol to dissolve lipids, "
        f"and the clear liquid is then poured into a test tube containing cold distilled water.\n\n"
        f"If the tested sample is **{food}**, what physical observation occurs and why?"
    )
    correct = f"Observation: {observation}.\nMechanism: {mechanism}."
    wrong_obs = "solution remains completely clear and transparent" if has_lipid else "a cloudy-white milky emulsion forms"
    wrong_mech = "lipids are absent" if has_lipid else "lipids precipitate out into a milky emulsion"
    options = [
        correct,
        f"Observation: {wrong_obs}.\nMechanism: {wrong_mech}.",
        "Observation: test tube catches fire immediately.\nMechanism: Lipids undergo spontaneous combustion with water.",
        "Observation: turns solid neon green.\nMechanism: Ethanol reacts with starch to make paint.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze ethanol emulsion test protocol:\n"
        f"- Lipids are soluble in ethanol, but insoluble in water.\n"
        f"- Adding water precipitates dissolved lipids into a cloudy-white emulsion.\n"
        f"**Step 2:** Sample: {food} -> Lipids present = {has_lipid}.\n\n"
        f"**Step 3:** The correct result is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_29_{rng.randint(100000, 999999)}",
        "subskill": "29_food_test_ethanol_emulsion_test_for_lipids_cloudy_white",
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
            "tier_1": f"Does {food} contain fats/lipids? What indicates a positive emulsion test?",
            "tier_2": "A positive ethanol emulsion test forms a cloudy-white milky emulsion when poured into water.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["food_test_ethanol_emulsion_lipids_milky_misconception"],
    }


# 30. Food test translucent grease spot test filter paper
def arch_30_food_test_translucent_grease_spot_test_filter_paper(rng: random.Random) -> Dict[str, Any]:
    samples = [
        ("A drop of cooking oil", True, "Permanent translucent spot that allows light to pass through even after thorough drying", "Lipid molecules penetrate between paper cellulose fibers and do not evaporate"),
        ("A drop of water", False, "Temporary wet mark that dries completely, leaving opaque white paper", "Water evaporates completely into the atmosphere without leaving non-volatile lipid residues"),
        ("A drop of pure honey syrup", False, "Sticky residue that dries without creating a translucent lipid grease stain", "High sugar content without hydrophobic triglycerides"),
    ]
    name, is_lipid, result, reason = rng.choice(samples)
    prompt = (
        f"A learner rubs **{name}** onto a piece of unglazed brown paper or white filter paper and allows it to dry in the air for 15 minutes.\n\n"
        f"What is observed when holding the paper up to a light source, and what does this test verify?"
    )
    correct = f"Result: {result} ({reason})."
    alt = [s for s in samples if s[1] != is_lipid][0]
    options = [
        correct,
        f"Result: {alt[2]} ({alt[3]}).",
        "Result: Paper dissolves into thin air leaving behind pure copper wire.",
        "Result: Paper turns bright fluorescent purple due to protein crystallization.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the grease spot test for fats:\n"
        f"- Lipids leave a permanent translucent spot on paper that does not evaporate.\n"
        f"- Water and watery solutions dry completely leaving normal opaque paper.\n"
        f"**Step 2:** Sample: {name} -> Lipid = {is_lipid}.\n\n"
        f"**Step 3:** The correct observation is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_30_{rng.randint(100000, 999999)}",
        "subskill": "30_food_test_translucent_grease_spot_test_filter_paper",
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
            "tier_1": f"Does {name} leave a permanent see-through grease spot after drying?",
            "tier_2": "Fats leave a permanent translucent mark; water dries and leaves opaque paper.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["grease_spot_test_lipids_translucent_mark_misconception"],
    }


# 31. Evaluating food test investigation unknown foodstuff analysis
def arch_31_evaluating_food_test_investigation_unknown_foodstuff_analysis(rng: random.Random) -> Dict[str, Any]:
    combinations = [
        (
            "Food Sample X",
            "Iodine: Blue-black | Benedict's: Blue | Biuret: Violet | Ethanol emulsion: Clear",
            "Contains starch and protein; lacks reducing sugars and lipids",
        ),
        (
            "Food Sample Y",
            "Iodine: Yellow-brown | Benedict's: Brick-red | Biuret: Blue | Ethanol emulsion: Cloudy-white",
            "Contains reducing sugars and lipids; lacks starch and protein",
        ),
        (
            "Food Sample Z",
            "Iodine: Blue-black | Benedict's: Orange | Biuret: Pale blue | Ethanol emulsion: Cloudy-white",
            "Contains starch, reducing sugars, and lipids; lacks protein",
        ),
    ]
    name, data, conclusion = rng.choice(combinations)
    prompt = (
        f"A laboratory technician analyzes an unknown food sample ({name}) and records the following qualitative biochemical test results:\n"
        f"**{data}**\n\n"
        f"Which nutritional composition conclusion is supported by these laboratory results?"
    )
    correct = conclusion
    distractors = [c[2] for c in combinations if c[0] != name]
    distractors.append("Contains zero organic nutrients and is composed entirely of pure sand.")
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Decode biochemical food tests:\n"
        f"- Iodine blue-black = Starch present; Yellow-brown = Starch absent.\n"
        f"- Benedict's brick-red/orange = Reducing sugar present; Blue = Absent.\n"
        f"- Biuret violet = Protein present; Pale blue = Absent.\n"
        f"- Ethanol cloudy-white = Lipid present; Clear = Absent.\n"
        f"**Step 2:** Match data: {data}\n"
        f"- Conclusion: {correct}\n\n"
        f"**Step 3:** The correct deduction is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_31_{rng.randint(100000, 999999)}",
        "subskill": "31_evaluating_food_test_investigation_unknown_foodstuff_analysis",
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
            "tier_1": "Match each test: Iodine = starch; Benedict's = sugar; Biuret = protein; Ethanol = lipid.",
            "tier_2": "Check which tests are positive (blue-black, orange/red, violet, cloudy) and which are negative.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["food_test_matrix_data_analysis_deduction_misconception"],
    }


# 32. Balanced diet seven essential components energy and growth
def arch_32_balanced_diet_seven_essential_components_energy_and_growth(rng: random.Random) -> Dict[str, Any]:
    components = [
        ("Carbohydrates", "Primary rapid energy substrate providing ~17 kJ/g via cellular respiration"),
        ("Proteins", "Supplying essential amino acids for growth, structural cellular repair, and synthesis of enzymes and antibodies"),
        ("Lipids (Fats & Oils)", "Concentrated long-term energy storage (~38 kJ/g), thermal insulation, and cellular membrane synthesis"),
        ("Dietary Fiber (Roughage)", "Indigestible plant cellulose adding bulk to feces, stimulating intestinal peristalsis, and preventing constipation"),
        ("Water", "Universal biochemical solvent, transport medium for nutrients and wastes, and thermoregulatory fluid for sweating"),
    ]
    name, role = rng.choice(components)
    prompt = (
        f"A balanced diet provides all seven essential nutrient classes in appropriate physiological proportions.\n\n"
        f"What is the primary nutritional and physiological role of **{name}** in human metabolism?"
    )
    correct = role
    distractors = [c[1] for c in components if c[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze components of a balanced diet.\n"
        f"**Step 2:** Relate {name} to metabolic role:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct nutritional role is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_32_{rng.randint(100000, 999999)}",
        "subskill": "32_balanced_diet_seven_essential_components_energy_and_growth",
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
            "tier_1": f"Recall what {name} is used for: energy, building tissue, fiber bulk, or solvent?",
            "tier_2": "Carbs = quick energy; Proteins = repair/growth; Fats = storage/insulation; Fiber = peristalsis bulk.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["balanced_diet_seven_nutrient_classes_roles_misconception"],
    }


# 33. Dietary deficiency kwashiorkor protein deficiency edema
def arch_33_dietary_deficiency_kwashiorkor_protein_deficiency_edema(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Kwashiorkor is a form of severe acute malnutrition predominantly affecting young children weaned onto carbohydrate-rich, protein-deficient diets.\n\n"
        f"What is the primary nutritional cause, clinical hallmark, and pathophysiological mechanism of **Kwashiorkor**?"
    )
    correct = (
        "Severe dietary protein deficiency despite adequate carbohydrate calories; characterized by a swollen, distended abdomen (edema/ascites), "
        "enlarged fatty liver, reddish-orange thinning hair, and apathy; caused by low plasma albumin reducing oncotic pressure, leaking fluid into peritoneal tissues."
    )
    wrong1 = (
        "Severe vitamin C deficiency causing teeth to fall out within 2 hours of eating rice."
    )
    wrong2 = (
        "Excess protein intake causing muscles to grow three times larger than the skeleton."
    )
    wrong3 = (
        "Lack of dietary table salt causing red blood cells to dissolve in the stomach."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze Kwashiorkor pathology:\n"
        f"- Cause: Protein deficiency (adequate calories from maize/cassava).\n"
        f"- Hallmarks: Swollen belly (edema), fatty liver, reddish depigmented hair.\n"
        f"- Mechanism: Low blood albumin -> fluid extravasation into abdominal cavity.\n\n"
        f"**Step 2:** The correct clinical profile is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_33_{rng.randint(100000, 999999)}",
        "subskill": "33_dietary_deficiency_kwashiorkor_protein_deficiency_edema",
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
            "tier_1": "What nutrient is lacking in Kwashiorkor, and why is the child's belly swollen?",
            "tier_2": "Protein deficiency causes low blood albumin, leaking fluid into the abdomen (edema).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["kwashiorkor_protein_deficiency_edema_distended_belly_misconception"],
    }


# 34. Dietary deficiency marasmus severe calorie starvation wasting
def arch_34_dietary_deficiency_marasmus_severe_calorie_starvation_wasting(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Marasmus is a severe form of protein-energy malnutrition distinct from Kwashiorkor.\n\n"
        f"What is the dietary etiology and clinical presentation of a child suffering from **Marasmus**?"
    )
    correct = (
        "Generalized, severe deficiency of both protein and total caloric energy (starvation); "
        "presents with extreme skeletal wasting of muscle and subcutaneous adipose tissue, sunken 'old person' facial appearance, "
        "prominent ribs, and absence of edema (no swollen abdomen)."
    )
    wrong1 = (
        "Excess consumption of sugary sweets causing the body to grow three times faster than normal."
    )
    wrong2 = (
        "Vitamin A overdose causing green skin and severe bone hardening."
    )
    wrong3 = (
        "Lack of dietary fiber causing food to turn into kidney stones inside the lungs."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare Marasmus vs Kwashiorkor:\n"
        f"- Kwashiorkor: Protein deficiency WITH calories -> Edema (swollen belly).\n"
        f"- Marasmus: Total starvation (both protein AND calories lacking) -> Severe wasting, NO edema.\n\n"
        f"**Step 2:** The correct clinical presentation is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_34_{rng.randint(100000, 999999)}",
        "subskill": "34_dietary_deficiency_marasmus_severe_calorie_starvation_wasting",
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
            "tier_1": "Is Marasmus just protein deficiency, or total calorie starvation? Is there edema?",
            "tier_2": "Marasmus is total starvation (calories + protein), causing severe skeletal wasting without edema.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["marasmus_vs_kwashiorkor_starvation_wasting_no_edema_misconception"],
    }


# 35. Dietary deficiency vitamin c scurvy bleeding gums collagen
def arch_35_dietary_deficiency_vitamin_c_scurvy_bleeding_gums_collagen(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Vitamin C (ascorbic acid) is an essential water-soluble micronutrient found in fresh citrus fruits and green vegetables.\n\n"
        f"Which clinical condition results from chronic vitamin C deficiency, and what biochemical defect causes it?"
    )
    correct = (
        "Scurvy; Vitamin C is an essential co-factor for prolyl hydroxylase in collagen triple-helix synthesis; "
        "defective collagen weakens capillaries and connective tissues, causing spongy bleeding gums, subperiosteal hemorrhages, poor wound healing, and opening of healed scars."
    )
    wrong1 = (
        "Night blindness; Vitamin C is needed to synthesize visual purple in retinal rod cells."
    )
    wrong2 = (
        "Rickets; Vitamin C failure prevents calcium absorption in the small intestine."
    )
    wrong3 = (
        "Goiter; Vitamin C is the direct building block for thyroid thyroxine hormones."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze Vitamin C deficiency (Scurvy):\n"
        f"- Required for: Collagen synthesis (structural protein of capillaries, bone, skin).\n"
        f"- Symptoms: Bleeding gums, loose teeth, capillary fragility, delayed wound healing.\n\n"
        f"**Step 2:** The correct clinical condition is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_35_{rng.randint(100000, 999999)}",
        "subskill": "35_dietary_deficiency_vitamin_c_scurvy_bleeding_gums_collagen",
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
            "tier_1": "What disease did sailors get when lacking fresh citrus fruits?",
            "tier_2": "Scurvy is caused by Vitamin C deficiency, disrupting collagen and causing bleeding gums.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["vitamin_c_deficiency_scurvy_collagen_synthesis_misconception"],
    }


# 36. Dietary deficiency vitamin d calcium rickets osteomalacia
def arch_36_dietary_deficiency_vitamin_d_calcium_rickets_osteomalacia(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Vitamin D (cholecalciferol) and calcium are vital for normal mineral homeostasis and bone ossification.\n\n"
        f"Which clinical condition develops in growing children who lack vitamin D or adequate safe sunlight exposure, and what skeletal deformity occurs?"
    )
    correct = (
        "Rickets; lack of vitamin D impairs active calcium absorption in the intestine; "
        "growing bone matrix fails to mineralize with calcium phosphate, remaining soft and pliable so that leg bones bend under body weight, causing bowed legs and pigeon chest."
    )
    wrong1 = (
        "Anemia; bones become brittle because bone marrow turns into pure calcium metal."
    )
    wrong2 = (
        "Scurvy; teeth turn completely black and dissolve within 24 hours."
    )
    wrong3 = (
        "Kwashiorkor; legs swell with water because skin absorbs sunlight as glucose."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze Vitamin D / Calcium deficiency:\n"
        f"- Disease in children: Rickets (Osteomalacia in adults).\n"
        f"- Mechanism: Poor calcium absorption -> unmineralized soft bone matrix.\n"
        f"- Deformity: Bowed legs under body weight.\n\n"
        f"**Step 2:** The correct condition is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_36_{rng.randint(100000, 999999)}",
        "subskill": "36_dietary_deficiency_vitamin_d_calcium_rickets_osteomalacia",
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
            "tier_1": "What bone disease in children causes bowed legs due to lack of Vitamin D?",
            "tier_2": "Rickets causes soft, unmineralized bones that bow under body weight.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["vitamin_d_calcium_rickets_bowed_legs_misconception"],
    }


# 37. Dietary deficiency iron anemia fatigue hemoglobin
def arch_37_dietary_deficiency_iron_anemia_fatigue_hemoglobin(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Iron is an essential mineral component of the heme group within hemoglobin.\n\n"
        f"Which deficiency disorder is caused by inadequate dietary iron intake, and what physiological symptoms emerge?"
    )
    correct = (
        "Iron-deficiency Anemia; insufficient iron limits hemoglobin synthesis, reducing the oxygen-carrying capacity of red blood cells; "
        "symptoms include chronic fatigue, pallor (pale conjunctiva and skin), shortness of breath (dyspnea) on mild exertion, and dizziness."
    )
    wrong1 = (
        "Osteoporosis; lack of iron causes bones to turn into fragile porous glass."
    )
    wrong2 = (
        "Goiter; iron deficiency causes the thyroid gland in the neck to swell."
    )
    wrong3 = (
        "Kwashiorkor; lack of iron causes the stomach to fill with pure hydrochloric acid."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze iron deficiency pathophysiology:\n"
        f"- Role of iron: Central atom in hemoglobin molecule that binds O2.\n"
        f"- Defect: Inability to manufacture sufficient hemoglobin -> Anemia.\n"
        f"- Symptoms: Fatigue, pallor, weakness, dyspnea due to tissue hypoxia.\n\n"
        f"**Step 2:** The correct disorder is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_37_{rng.randint(100000, 999999)}",
        "subskill": "37_dietary_deficiency_iron_anemia_fatigue_hemoglobin",
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
            "tier_1": "What condition results from low iron and leads to pale skin and fatigue?",
            "tier_2": "Iron deficiency anemia impairs hemoglobin synthesis, causing fatigue and shortness of breath.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["iron_deficiency_anemia_hemoglobin_fatigue_misconception"],
    }


# 38. Dietary deficiency vitamin a night blindness rhodopsin
def arch_38_dietary_deficiency_vitamin_a_night_blindness_rhodopsin(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Vitamin A (retinol) is a fat-soluble vitamin found in liver, carrots, pumpkin, and leafy greens.\n\n"
        f"Which clinical manifestation is the earliest symptom of vitamin A deficiency, and what biochemical mechanism accounts for it?"
    )
    correct = (
        "Night blindness (nyctalopia); Vitamin A is the precursor for retinal, which combines with opsin to synthesize rhodopsin "
        "(the light-sensitive pigment in retinal rod cells required for vision in dim light); severe prolonged deficiency leads to xerophthalmia and irreversible blindness."
    )
    wrong1 = (
        "Scurvy; inability to synthesize collagen in the teeth."
    )
    wrong2 = (
        "Rickets; loss of calcium from the enamel of the teeth."
    )
    wrong3 = (
        "Goiter; sudden enlargement of the pituitary gland behind the eyes."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze Vitamin A deficiency:\n"
        f"- Required for: Rhodopsin visual purple pigment in retinal rods.\n"
        f"- Early symptom: Night blindness (poor adaptation to dim light).\n"
        f"- Advanced condition: Xerophthalmia (dry cornea) and blindness.\n\n"
        f"**Step 2:** The correct manifestation is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_38_{rng.randint(100000, 999999)}",
        "subskill": "38_dietary_deficiency_vitamin_a_night_blindness_rhodopsin",
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
            "tier_1": "What visual problem occurs when a person lacks Vitamin A?",
            "tier_2": "Vitamin A deficiency causes night blindness because rhodopsin cannot be synthesized.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["vitamin_a_deficiency_night_blindness_rhodopsin_misconception"],
    }


# 39. Dietary deficiency iodine goiter thyroid enlargement
def arch_39_dietary_deficiency_iodine_goiter_thyroid_enlargement(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Iodine is a trace element found in seafood and iodized table salt.\n\n"
        f"What disorder results from chronic dietary iodine deficiency, and what physiological feedback mechanism causes the visible symptom?"
    )
    correct = (
        "Goiter; iodine is an essential component of thyroxine (T4/T3); lack of iodine causes low thyroxine levels, triggering "
        "the anterior pituitary to secrete excess Thyroid Stimulating Hormone (TSH) in an attempt to stimulate the gland, causing massive hypertrophy and swelling of the thyroid gland in the neck."
    )
    wrong1 = (
        "Anemia; red blood cells turn white and shrink into platelets."
    )
    wrong2 = (
        "Scurvy; connective tissues around the lips bleed continuously."
    )
    wrong3 = (
        "Marasmus; muscle fibers turn into pure fat deposits in the lungs."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze iodine deficiency pathology (Goiter):\n"
        f"- Role of iodine: Synthesize thyroxine in thyroid gland.\n"
        f"- Feedback loop: Low thyroxine -> High TSH from pituitary.\n"
        f"- Outcome: Hypertrophy and swelling of thyroid gland in neck (Goiter).\n\n"
        f"**Step 2:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_39_{rng.randint(100000, 999999)}",
        "subskill": "39_dietary_deficiency_iodine_goiter_thyroid_enlargement",
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
            "tier_1": "What neck swelling occurs when a person lacks iodine?",
            "tier_2": "Goiter: low thyroxine causes high TSH, swelling the thyroid gland in the neck.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["iodine_deficiency_goiter_tsh_thyroid_swelling_misconception"],
    }


# 40. Eating disorders anorexia nervosa psychological wasting
def arch_40_eating_disorders_anorexia_nervosa_psychological_wasting(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Anorexia nervosa is a complex psychological eating disorder characterized by an intense fear of gaining weight and a distorted body image.\n\n"
        f"Which clinical features and physiological consequences characterize **Anorexia Nervosa**?"
    )
    correct = (
        "Severe voluntary caloric restriction, compulsive excessive exercising, and refusal to maintain minimal healthy body weight; "
        "leads to severe emaciation, amenorrhea (cessation of menstrual periods), hypothermia, cardiac arrhythmias (bradycardia), bone loss (osteopenia), and fine body hair growth (lanugo)."
    )
    wrong1 = (
        "Compulsive overeating of 50 loaves of bread every morning followed by sleeping for 20 hours."
    )
    wrong2 = (
        "Bacterial infection of the tongue causing food to taste like solid coal."
    )
    wrong3 = (
        "Complete loss of all salivary glands caused by drinking cold water."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze anorexia nervosa clinical criteria:\n"
        f"- Psychological: Distorted body image, morbid fear of weight gain.\n"
        f"- Behavioral: Severe self-starvation, excessive exercise.\n"
        f"- Medical: Amenorrhea, bradycardia, muscle wasting, lanugo hair.\n\n"
        f"**Step 2:** The correct clinical profile is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_40_{rng.randint(100000, 999999)}",
        "subskill": "40_eating_disorders_anorexia_nervosa_psychological_wasting",
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
            "tier_1": "Recall the features of Anorexia: self-starvation, fear of weight gain, amenorrhea.",
            "tier_2": "Anorexia involves severe self-starvation, distorted body image, and medical complications like amenorrhea.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["anorexia_nervosa_eating_disorder_amenorrhea_misconception"],
    }


# 41. Eating disorders bulimia nervosa binge purge tooth erosion
def arch_41_eating_disorders_bulimia_nervosa_binge_purge_tooth_erosion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Bulimia nervosa is characterized by recurrent episodes of binge eating followed by compensatory purging behaviors.\n\n"
        f"Which clinical hallmark and dental/medical complication defines **Bulimia Nervosa**?"
    )
    correct = (
        "Cycles of rapid, uncontrollable consumption of large quantities of high-calorie food (bingeing) followed by self-induced vomiting, "
        "laxative abuse, or extreme fasting (purging); recurrent exposure of teeth to acidic gastric juices causes severe enamel erosion, salivary gland enlargement, and electrolyte imbalances (hypokalemia)."
    )
    wrong1 = (
        "Refusal to ever eat solid food from birth, surviving strictly on filtered seawater."
    )
    wrong2 = (
        "Genetic mutation causing teeth to turn into iron nails inside the gums."
    )
    wrong3 = (
        "Inability to absorb water in the stomach causing permanent swelling of the toes."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze bulimia nervosa hallmarks:\n"
        f"- Binge eating followed by compensatory purging (vomiting, laxatives).\n"
        f"- Stomach acid from vomiting erodes dental enamel.\n"
        f"- Electrolyte loss (potassium/chloride) causes cardiac arrhythmias.\n\n"
        f"**Step 2:** The correct clinical hallmark is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_41_{rng.randint(100000, 999999)}",
        "subskill": "41_eating_disorders_bulimia_nervosa_binge_purge_tooth_erosion",
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
            "tier_1": "What eating disorder involves bingeing followed by purging (vomiting), causing tooth erosion?",
            "tier_2": "Bulimia nervosa features binge-purge cycles; gastric acid from vomiting erodes tooth enamel.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["bulimia_nervosa_binge_purge_dental_erosion_misconception"],
    }


# 42. Lifestyle conditions obesity type2 diabetes atherosclerosis
def arch_42_lifestyle_conditions_obesity_type2_diabetes_atherosclerosis(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Obesity is defined by a Body Mass Index (BMI) >= 30 kg/m², resulting from chronic positive energy balance (caloric intake exceeding metabolic expenditure).\n\n"
        f"What pathophysiological cascade links obesity to **Type 2 Diabetes** and **cardiovascular disease**?"
    )
    correct = (
        "Excess visceral adipose tissue releases pro-inflammatory cytokines and free fatty acids, inducing peripheral insulin resistance; "
        "pancreatic beta cells become exhausted leading to chronic hyperglycemia (Type 2 Diabetes), while dyslipidemia and hypertension accelerate arterial atherosclerosis."
    )
    wrong1 = (
        "Obesity causes all bones to soften into cartilage within 48 hours."
    )
    wrong2 = (
        "Fat cells turn into bacteria that consume white blood cells in the liver."
    )
    wrong3 = (
        "Excess calories turn into pure iron that clogs the bronchial tubes of the lungs."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze obesity pathophysiology:\n"
        f"- Visceral adiposity -> Insulin resistance.\n"
        f"- Beta cell exhaustion -> Type 2 Diabetes.\n"
        f"- Dyslipidemia + inflammation -> Atherosclerosis and hypertension.\n\n"
        f"**Step 2:** The correct physiological cascade is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_42_{rng.randint(100000, 999999)}",
        "subskill": "42_lifestyle_conditions_obesity_type2_diabetes_atherosclerosis",
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
            "tier_1": "How does excess body fat lead to insulin resistance and clogged arteries?",
            "tier_2": "Visceral fat causes insulin resistance leading to Type 2 diabetes and accelerates atherosclerosis.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["obesity_type_2_diabetes_insulin_resistance_misconception"],
    }


# 43. Gastrointestinal pathology peptic ulcers helicobacter pylori
def arch_43_gastrointestinal_pathology_peptic_ulcers_helicobacter_pylori(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Peptic ulcers are painful sores that erode the mucosal lining of the stomach (gastric ulcer) or duodenum (duodenal ulcer).\n\n"
        f"What is the primary microbiological cause and treatment of most **peptic ulcers**?"
    )
    correct = (
        "Infection by the bacterium *Helicobacter pylori*; it produces urease to neutralize local acid, burrows into mucosal lining, "
        "and induces chronic inflammation that weakens the protective mucus barrier, allowing gastric acid and pepsin to erode underlying tissue; "
        "treated with 'triple therapy' (two antibiotics plus a proton pump inhibitor acid suppressor)."
    )
    wrong1 = (
        "Eating spicy curry; spicy food directly burns a physical hole through the stomach in 10 minutes."
    )
    wrong2 = (
        "Viral infection of red blood cells that turns saliva into hydrochloric acid."
    )
    wrong3 = (
        "Drinking cold milk that curdles and turns into sharp stones cutting the stomach wall."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze peptic ulcer etiology:\n"
        f"- Primary cause: *Helicobacter pylori* bacterial infection (plus NSAID overuse).\n"
        f"- Mechanism: Weakens mucosal barrier, exposing epithelium to acid/pepsin digestion.\n"
        f"- Treatment: Antibiotics + Proton pump inhibitors (PPIs).\n\n"
        f"**Step 2:** The accurate medical explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_43_{rng.randint(100000, 999999)}",
        "subskill": "43_gastrointestinal_pathology_peptic_ulcers_helicobacter_pylori",
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
            "tier_1": "What bacterium causes most stomach ulcers, and how is it treated?",
            "tier_2": "*Helicobacter pylori* bacteria cause ulcers by weakening the mucus barrier; treated with antibiotics.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["peptic_ulcers_helicobacter_pylori_acid_erosion_misconception"],
    }


# 44. Gastrointestinal pathology diarrhea cholera dehydration ors
def arch_44_gastrointestinal_pathology_diarrhea_cholera_dehydration_ors(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Diarrheal diseases, including cholera (caused by *Vibrio cholerae*), cause rapid, severe dehydration in children and adults.\n\n"
        f"What is the pathophysiological mechanism of cholera toxin, and how does **Oral Rehydration Salts (ORS)** save lives?"
    )
    correct = (
        "Cholera toxin locks intestinal epithelial adenylate cyclase in active state, causing massive chloride and water secretion into intestinal lumen (rice-water stools); "
        "ORS solution (water, glucose, sodium chloride) utilizes intact sodium-glucose cotransporters (SGLT-1) in enterocytes to pull water back into blood by osmosis, reversing dehydration."
    )
    wrong1 = (
        "Cholera stops all bowel movements, causing the stomach to fill with solid salt; treated by giving pure alcohol."
    )
    wrong2 = (
        "Cholera turns red blood cells into liquid bile; treated by applying ice to the chest."
    )
    wrong3 = (
        "Cholera is treated by complete fluid restriction, withholding all water for 5 days."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze cholera mechanism and ORS physiology:\n"
        f"- Toxin triggers massive water/electrolyte secretion -> severe dehydration and hypovolemic shock.\n"
        f"- ORS mechanism: Sodium-glucose cotransport (SGLT-1) absorbs sodium and water even during cholera diarrhea.\n\n"
        f"**Step 2:** The correct physiological explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_44_{rng.randint(100000, 999999)}",
        "subskill": "44_gastrointestinal_pathology_diarrhea_cholera_dehydration_ors",
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
            "tier_1": "How does cholera cause water loss, and why does ORS use glucose with salt?",
            "tier_2": "Cholera causes massive water secretion; ORS uses sodium-glucose cotransporters to pull water back into blood.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["diarrhea_cholera_toxin_ors_sodium_glucose_cotransport_misconception"],
    }


# 45. Gastrointestinal pathology constipation dietary roughage fiber
def arch_45_gastrointestinal_pathology_constipation_dietary_roughage_fiber(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Constipation is characterized by infrequent, difficult, or painful evacuation of hard, dry feces.\n\n"
        f"How does adequate intake of **dietary fiber (roughage)** and **water** prevent constipation?"
    )
    correct = (
        "Insoluble dietary fiber (cellulose) cannot be digested by human enzymes; it absorbs water and expands, "
        "adding soft bulk to the fecal mass; this physical stretch stimulates mechanoreceptors in the intestinal wall, triggering strong peristaltic waves that shorten colon transit time."
    )
    wrong1 = (
        "Fiber dissolves into pure glucose that provides instant energy to abdominal muscles."
    )
    wrong2 = (
        "Fiber kills all gut bacteria, preventing any fecal material from ever forming."
    )
    wrong3 = (
        "Fiber chemically binds all water so that feces become rock-hard and cannot move."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze role of fiber (roughage) in colon motility:\n"
        f"- Insoluble fiber retains water and adds fecal bulk.\n"
        f"- Fecal bulk stretches colon wall -> triggers peristaltic contractions.\n"
        f"- Speeds up transit time, keeping stools soft and easy to pass.\n\n"
        f"**Step 2:** The correct physiological mechanism is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_45_{rng.randint(100000, 999999)}",
        "subskill": "45_gastrointestinal_pathology_constipation_dietary_roughage_fiber",
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
            "tier_1": "How does fiber help food move through the large intestine?",
            "tier_2": "Fiber holds water and adds bulk to stools, stimulating peristalsis and preventing hard, dry feces.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["constipation_dietary_fiber_peristalsis_bulk_misconception"],
    }


# 46. Gastrointestinal pathology liver cirrhosis alcohol fibrosis
def arch_46_gastrointestinal_pathology_liver_cirrhosis_alcohol_fibrosis(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Cirrhosis is the end-stage progressive destruction of normal hepatic architecture, commonly caused by chronic alcohol abuse or hepatitis B/C.\n\n"
        f"What histological changes occur in **liver cirrhosis**, and what vital functions are compromised?"
    )
    correct = (
        "Chronic toxicity causes progressive necrosis of functional hepatocytes; destroyed liver tissue is replaced by diffuse fibrous scar tissue "
        "and regenerative nodules; hepatic blood flow is obstructed (portal hypertension), leading to failure of bile production, deamination, and detoxification."
    )
    wrong1 = (
        "The liver doubles in size and turns into a second heart pumping bile to the brain."
    )
    wrong2 = (
        "The liver completely converts into an extra lung that exhales alcohol fumes."
    )
    wrong3 = (
        "Liver cells turn into skeletal muscle fibers, making the abdomen rock hard."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze cirrhosis histology and pathology:\n"
        f"- Hepatocyte necrosis + replacement with non-functional fibrous scar tissue.\n"
        f"- Loss of metabolic functions: Bile synthesis, detoxification, urea synthesis, clotting factors.\n"
        f"- Portal hypertension from vascular distortion.\n\n"
        f"**Step 2:** The correct description is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_46_{rng.randint(100000, 999999)}",
        "subskill": "46_gastrointestinal_pathology_liver_cirrhosis_alcohol_fibrosis",
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
            "tier_1": "What happens to functional liver cells when damaged by chronic alcohol abuse?",
            "tier_2": "Healthy hepatocytes are replaced by irreversible fibrous scar tissue, compromising liver function.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["liver_cirrhosis_alcohol_hepatocyte_fibrosis_misconception"],
    }


# 47. Evaluating enzyme activity temperature optimum denaturation
def arch_47_evaluating_enzyme_activity_temperature_optimum_denaturation(rng: random.Random) -> Dict[str, Any]:
    temp = rng.choice([55, 60, 65, 70])
    prompt = (
        f"In an experiment testing salivary amylase on starch at various temperatures, "
        f"reaction rate peaks at approximately **37°C** (optimum temperature).\n"
        f"When the temperature is elevated to **{temp}°C**, the enzyme activity drops to zero and cannot be restored even after cooling back down.\n\n"
        f"What biophysical event occurs at {temp}°C to permanently inactivate the enzyme?"
    )
    correct = (
        f"Thermal denaturation: excessive kinetic energy breaks hydrogen and ionic bonds stabilizing the enzyme's specific 3D tertiary protein conformation; "
        f"the active site permanently loses its complementary shape ('lock'), so it can no longer bind starch substrates."
    )
    wrong1 = (
        "The enzyme enters hibernation and falls asleep until next winter."
    )
    wrong2 = (
        "The starch molecules turn into iron crystals that crush the enzyme."
    )
    wrong3 = (
        "The water in the test tube breaks down into explosive hydrogen gas."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze temperature effects on enzyme kinetics:\n"
        f"- Below optimum (~37°C): Low kinetic energy -> few collisions.\n"
        f"- At optimum: Maximum enzyme-substrate collision frequency.\n"
        f"- Above optimum (>50°C): Thermal denaturation breaks tertiary bonds -> irreversible active site deformation.\n\n"
        f"**Step 2:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_47_{rng.randint(100000, 999999)}",
        "subskill": "47_evaluating_enzyme_activity_temperature_optimum_denaturation",
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
            "tier_1": f"What happens to the 3D shape of an enzyme at {temp}°C?",
            "tier_2": "Thermal denaturation destroys the tertiary structure and active site shape, inactivating the enzyme permanently.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["enzyme_temperature_optimum_denaturation_active_site_misconception"],
    }


# 48. Evaluating enzyme activity ph optimum pepsin vs amylase
def arch_48_evaluating_enzyme_activity_ph_optimum_pepsin_vs_amylase(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Salivary amylase operates optimally at **pH ~6.8 - 7.0** in the mouth, whereas stomach pepsin operates optimally at **pH ~1.5 - 2.0**.\n\n"
        f"What happens to the catalytic activity of salivary amylase when it is swallowed and enters the strongly acidic stomach lumen, and why?"
    )
    correct = (
        "Amylase activity drops to zero and the enzyme is permanently denatured; the high H+ ion concentration alters ionic charges on active site "
        "amino acid residues, disrupting tertiary folding and destroying substrate binding capability."
    )
    wrong1 = (
        "Amylase becomes ten times more active and digests all stomach walls in 5 seconds."
    )
    wrong2 = (
        "Amylase converts into stomach pepsin by absorbing acid ions."
    )
    wrong3 = (
        "Amylase begins to digest water into pure oxygen bubbles."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze pH sensitivity of digestive enzymes:\n"
        f"- Mouth: Amylase optimum pH ~7.0.\n"
        f"- Stomach: Acidic environment (pH ~2.0) provided by HCl.\n"
        f"- Outcome: Swallowed amylase is rapidly and irreversibly denatured by extreme acidity.\n\n"
        f"**Step 2:** The correct statement is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_48_{rng.randint(100000, 999999)}",
        "subskill": "48_evaluating_enzyme_activity_ph_optimum_pepsin_vs_amylase",
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
            "tier_1": "Can salivary amylase work in stomach acid (pH 2)?",
            "tier_2": "Extreme stomach acid denatures salivary amylase, stopping starch digestion in the stomach.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["enzyme_ph_optimum_amylase_vs_pepsin_denaturation_misconception"],
    }


# 49. Evaluating dialysis tubing visking model of small intestine
def arch_49_evaluating_dialysis_tubing_visking_model_of_small_intestine(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A laboratory model of the small intestine is set up: a sealed piece of dialysis (Visking) tubing containing a mixture of starch and glucose "
        f"is immersed in a beaker of pure distilled water for 60 minutes.\n\n"
        f"Subsequent testing reveals that glucose is present in the surrounding beaker water, but starch is absent.\n"
        f"Which biophysical principle explains this observation?"
    )
    correct = (
        "The dialysis tubing acts as a selectively permeable membrane with microscopic pores; small, soluble glucose monosaccharide molecules "
        "diffuse freely through the pores into the water, while large, insoluble starch polymers are too large to pass through."
    )
    wrong1 = (
        "Starch actively eats the dialysis tubing from the inside, preventing itself from leaving."
    )
    wrong2 = (
        "Glucose turns into a gas that evaporates through the glass beaker."
    )
    wrong3 = (
        "Water in the beaker actively repels starch using magnetic force."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze Visking dialysis tubing model:\n"
        f"- Pores allow small molecules (< molecular weight cutoff) to diffuse.\n"
        f"- Glucose (monosaccharide, small) passes through pores into beaker.\n"
        f"- Starch (polysaccharide, huge polymer) is blocked by pore size.\n\n"
        f"**Step 2:** The correct biophysical principle is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_49_{rng.randint(100000, 999999)}",
        "subskill": "49_evaluating_dialysis_tubing_visking_model_of_small_intestine",
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
            "tier_1": "Why can glucose pass through dialysis tubing pores while starch cannot?",
            "tier_2": "Dialysis membrane pores allow small glucose molecules to diffuse through, but block large starch polymers.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["visking_dialysis_tubing_model_selective_permeability_misconception"],
    }


# 50. Synthetic case study acute malnutrition refeeding triage
def arch_50_synthetic_case_study_acute_malnutrition_refeeding_triage(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        (
            "A 3-year-old child presents to a rural clinic with generalized pitting edema (swollen feet and distended belly), sparse reddish-orange hair, flaky paint dermatosis, and severe lethargy",
            "Severe Acute Malnutrition (Kwashiorkor)",
            "Begin careful therapeutic refeeding with low-lactose, high-protein formula (F-75/F-100), monitor potassium/electrolyte balance to prevent refeeding syndrome, and provide micronutrient supplementation",
        ),
        (
            "A 14-month-old infant presents severely emaciated with 'skin and bone' appearance, prominent ribcage, loss of buccal fat pads giving a wizened 'old man' face, but with zero edema",
            "Severe Acute Malnutrition (Marasmus)",
            "Initiate gradual stabilized caloric rehydration and refeeding with starter therapeutic milk (F-75) before transitioning to ready-to-use therapeutic food (RUTF), monitoring blood glucose",
        ),
    ]
    presentation, diagnosis, triage_plan = rng.choice(scenarios)
    prompt = (
        f"**Clinical Triage Case Study:**\n\n"
        f"Patient presentation: {presentation}.\n\n"
        f"What is the clinical diagnosis and the evidence-based medical triage intervention?"
    )
    correct = f"Diagnosis: {diagnosis}.\nTriage plan: {triage_plan}."
    alt = [s for s in scenarios if s[1] != diagnosis][0]
    options = [
        correct,
        f"Diagnosis: {alt[1]}.\nTriage plan: {alt[2]}.",
        "Diagnosis: Acute allergic reaction to fruit.\nTriage plan: Administer high-dose antibiotics and withhold all food for 7 days.",
        "Diagnosis: Healthy athletic build.\nTriage plan: Encourage intense running and give two cups of black coffee.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze clinical signs: {presentation}.\n"
        f"**Step 2:** Formulate diagnosis and triage response:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The correct clinical response is: **{correct}**."
    )
    return {
        "id": f"ns9_dig_50_{rng.randint(100000, 999999)}",
        "subskill": "50_synthetic_case_study_acute_malnutrition_refeeding_triage",
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
            "tier_1": f"Is this child presenting with edema (Kwashiorkor) or severe wasting without edema (Marasmus)?",
            "tier_2": "Edema + distended belly = Kwashiorkor; severe skin-and-bone wasting without edema = Marasmus.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["acute_malnutrition_triage_kwashiorkor_vs_marasmus_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "26_food_test_iodine_test_for_starch_blue_black_coloration": arch_26_food_test_iodine_test_for_starch_blue_black_coloration,
    "27_food_test_benedicts_test_for_reducing_sugars_color_gradient": arch_27_food_test_benedicts_test_for_reducing_sugars_color_gradient,
    "28_food_test_biuret_test_for_proteins_violet_purple_coloration": arch_28_food_test_biuret_test_for_proteins_violet_purple_coloration,
    "29_food_test_ethanol_emulsion_test_for_lipids_cloudy_white": arch_29_food_test_ethanol_emulsion_test_for_lipids_cloudy_white,
    "30_food_test_translucent_grease_spot_test_filter_paper": arch_30_food_test_translucent_grease_spot_test_filter_paper,
    "31_evaluating_food_test_investigation_unknown_foodstuff_analysis": arch_31_evaluating_food_test_investigation_unknown_foodstuff_analysis,
    "32_balanced_diet_seven_essential_components_energy_and_growth": arch_32_balanced_diet_seven_essential_components_energy_and_growth,
    "33_dietary_deficiency_kwashiorkor_protein_deficiency_edema": arch_33_dietary_deficiency_kwashiorkor_protein_deficiency_edema,
    "34_dietary_deficiency_marasmus_severe_calorie_starvation_wasting": arch_34_dietary_deficiency_marasmus_severe_calorie_starvation_wasting,
    "35_dietary_deficiency_vitamin_c_scurvy_bleeding_gums_collagen": arch_35_dietary_deficiency_vitamin_c_scurvy_bleeding_gums_collagen,
    "36_dietary_deficiency_vitamin_d_calcium_rickets_osteomalacia": arch_36_dietary_deficiency_vitamin_d_calcium_rickets_osteomalacia,
    "37_dietary_deficiency_iron_anemia_fatigue_hemoglobin": arch_37_dietary_deficiency_iron_anemia_fatigue_hemoglobin,
    "38_dietary_deficiency_vitamin_a_night_blindness_rhodopsin": arch_38_dietary_deficiency_vitamin_a_night_blindness_rhodopsin,
    "39_dietary_deficiency_iodine_goiter_thyroid_enlargement": arch_39_dietary_deficiency_iodine_goiter_thyroid_enlargement,
    "40_eating_disorders_anorexia_nervosa_psychological_wasting": arch_40_eating_disorders_anorexia_nervosa_psychological_wasting,
    "41_eating_disorders_bulimia_nervosa_binge_purge_tooth_erosion": arch_41_eating_disorders_bulimia_nervosa_binge_purge_tooth_erosion,
    "42_lifestyle_conditions_obesity_type2_diabetes_atherosclerosis": arch_42_lifestyle_conditions_obesity_type2_diabetes_atherosclerosis,
    "43_gastrointestinal_pathology_peptic_ulcers_helicobacter_pylori": arch_43_gastrointestinal_pathology_peptic_ulcers_helicobacter_pylori,
    "44_gastrointestinal_pathology_diarrhea_cholera_dehydration_ors": arch_44_gastrointestinal_pathology_diarrhea_cholera_dehydration_ors,
    "45_gastrointestinal_pathology_constipation_dietary_roughage_fiber": arch_45_gastrointestinal_pathology_constipation_dietary_roughage_fiber,
    "46_gastrointestinal_pathology_liver_cirrhosis_alcohol_fibrosis": arch_46_gastrointestinal_pathology_liver_cirrhosis_alcohol_fibrosis,
    "47_evaluating_enzyme_activity_temperature_optimum_denaturation": arch_47_evaluating_enzyme_activity_temperature_optimum_denaturation,
    "48_evaluating_enzyme_activity_ph_optimum_pepsin_vs_amylase": arch_48_evaluating_enzyme_activity_ph_optimum_pepsin_vs_amylase,
    "49_evaluating_dialysis_tubing_visking_model_of_small_intestine": arch_49_evaluating_dialysis_tubing_visking_model_of_small_intestine,
    "50_synthetic_case_study_acute_malnutrition_refeeding_triage": arch_50_synthetic_case_study_acute_malnutrition_refeeding_triage,
}
