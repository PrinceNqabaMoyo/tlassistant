"""Grade 9 Natural Sciences: Term 1 - Circulatory and Respiratory Systems (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 1/04. Circulatory and respiratory systems.md.
Focus: Cellular respiration link, exercise investigations, bell jar model, lung volumes, pathologies (asthma/TB/smoking/hypertension/heart attack), CPR/first aid, and blood groups.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Cellular respiration link glucose oxygen atp carbon dioxide water
def arch_26_cellular_respiration_link_glucose_oxygen_atp_carbon_dioxide_water(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The respiratory and circulatory systems work synergistically to sustain internal cellular respiration in body tissues.\n\n"
        f"Which biochemical equation and physiological role represents **aerobic cellular respiration**?"
    )
    correct = (
        "Glucose + Oxygen -> Carbon Dioxide + Water + ATP Energy (C6H12O6 + 6O2 -> 6CO2 + 6H2O + ATP); "
        "circulatory system delivers glucose (from digestive system) and O2 (from respiratory system) to mitochondria, and carries away waste CO2."
    )
    wrong1 = (
        "Carbon Dioxide + Water + Light -> Glucose + Oxygen; "
        "respiratory system synthesizes glucose from sunlight inside mitochondria."
    )
    wrong2 = (
        "Glucose -> Lactic Acid + Alcohol; "
        "circulatory system converts all cells into yeast cultures to produce bread inside muscles."
    )
    wrong3 = (
        "Oxygen + Water -> Nitrogen Gas + Urea; "
        "respiratory system burns pure water to manufacture body heat."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Write the chemical equation for aerobic cellular respiration:\n"
        f"- C6H12O6 + 6O2 -> 6CO2 + 6H2O + 36-38 ATP.\n"
        f"**Step 2:** Relate to organ systems:\n"
        f"- Respiratory system: supplies O2 and removes CO2.\n"
        f"- Digestive system: absorbs glucose.\n"
        f"- Circulatory system: transports substrates to working cells.\n\n"
        f"**Step 3:** The accurate statement is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_26_{rng.randint(100000, 999999)}",
        "subskill": "26_cellular_respiration_link_glucose_oxygen_atp_carbon_dioxide_water",
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
            "tier_1": "Recall: Cellular respiration breaks down glucose with oxygen to yield energy (ATP), water, and CO2.",
            "tier_2": "C6H12O6 + 6O2 -> 6CO2 + 6H2O + Energy.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cellular_respiration_vs_gas_exchange_equation_misconception"],
    }


# 27. Aerobic vs anaerobic respiration lactic acid oxygen debt
def arch_27_aerobic_vs_anaerobic_respiration_lactic_acid_oxygen_debt(rng: random.Random) -> Dict[str, Any]:
    states = [
        (
            "Aerobic respiration",
            "Requires oxygen; completely oxidizes glucose into CO2 and H2O; yields maximum energy (~36 ATP per glucose); occurs in mitochondria during resting and moderate activity",
        ),
        (
            "Anaerobic respiration in human skeletal muscle",
            "Occurs during intense sprinting when oxygen supply cannot meet rapid ATP demand; incomplete breakdown of glucose produces lactic acid and only 2 ATP per glucose",
        ),
        (
            "Oxygen debt (EPOC)",
            "The additional volume of oxygen consumed post-exercise to metabolize accumulated lactic acid in the liver (converting it back to glycogen) and re-oxygenate myoglobin",
        ),
    ]
    name, mechanism = rng.choice(states)
    prompt = (
        f"During vigorous physical exertion, muscular energy demands outstrip immediate cardiovascular oxygen delivery.\n\n"
        f"Which statement accurately explains **{name}**?"
    )
    correct = mechanism
    distractors = [s[1] for s in states if s[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare aerobic and anaerobic metabolic pathways.\n"
        f"**Step 2:** Relate to {name}:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_27_{rng.randint(100000, 999999)}",
        "subskill": "27_aerobic_vs_anaerobic_respiration_lactic_acid_oxygen_debt",
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
            "tier_1": f"Think about whether {name} requires oxygen, produces lactic acid, or repays metabolic debt.",
            "tier_2": "Aerobic yields 36 ATP with O2; Anaerobic yields 2 ATP + lactic acid; Oxygen debt repays liver oxidation post-exercise.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["anaerobic_respiration_lactic_acid_oxygen_debt_misconception"],
    }


# 28. Investigating breathing rate physical exercise fair test
def arch_28_investigating_breathing_rate_physical_exercise_fair_test(rng: random.Random) -> Dict[str, Any]:
    variables = [
        (
            "Independent variable",
            "The level or duration of physical exercise (e.g. at rest, 2 minutes of step-ups, 5 minutes of sprinting)",
        ),
        (
            "Dependent variable",
            "The breathing rate (measured in breaths per minute by counting thoracic chest rises)",
        ),
        (
            "Fixed / Controlled variables",
            "Same participant, same ambient room temperature, identical exercise type and cadence, and consistent rest interval before baseline testing",
        ),
        (
            "Physiological reason for increased breathing rate",
            "Working skeletal muscles produce excess CO2, lowering blood pH; respiratory centers in the medulla oblongata detect acidosis and accelerate ventilation to expel CO2",
        ),
    ]
    var_name, role = rng.choice(variables)
    prompt = (
        f"Learners conduct a scientific investigation to determine how physical exercise affects breathing rate in humans.\n\n"
        f"Which experimental parameter or physiological rationale correctly identifies the **{var_name}** in this investigation?"
    )
    correct = role
    distractors = [v[1] for v in variables if v[0] != var_name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze experimental design for breathing rate investigation.\n"
        f"**Step 2:** Identify {var_name}:\n"
        f"- {var_name}: {correct}\n\n"
        f"**Step 3:** The correct identification is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_28_{rng.randint(100000, 999999)}",
        "subskill": "28_investigating_breathing_rate_physical_exercise_fair_test",
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
            "tier_1": f"Identify what is manipulated, measured, or held constant: {var_name}.",
            "tier_2": "Independent = exercise intensity; Dependent = breathing rate; Controlled = participant, temperature, duration.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["breathing_rate_exercise_fair_test_variables_misconception"],
    }


# 29. Investigating pulse rate radial carotid artery beats per minute
def arch_29_investigating_pulse_rate_radial_carotid_artery_beats_per_minute(rng: random.Random) -> Dict[str, Any]:
    beats_15s = rng.choice([18, 20, 22, 24])
    resting_bpm = beats_15s * 4
    ex_beats_15s = beats_15s + rng.choice([10, 12, 14])
    exercise_bpm = ex_beats_15s * 4
    diff = exercise_bpm - resting_bpm
    prompt = (
        f"A learner measures their resting pulse rate at the radial artery on the wrist, counting **{beats_15s} beats in 15 seconds**.\n"
        f"Immediately after 3 minutes of vigorous star jumps, they count **{ex_beats_15s} beats in 15 seconds**.\n\n"
        f"What is their resting pulse rate, their post-exercise pulse rate (in beats per minute), and the overall increase in pulse rate?"
    )
    correct = f"Resting: {resting_bpm} bpm; Post-exercise: {exercise_bpm} bpm; Overall increase: {diff} bpm."
    wrong1 = f"Resting: {beats_15s} bpm; Post-exercise: {ex_beats_15s} bpm; Overall increase: {ex_beats_15s - beats_15s} bpm."
    wrong2 = f"Resting: {resting_bpm // 2} bpm; Post-exercise: {exercise_bpm // 2} bpm; Overall increase: {diff // 2} bpm."
    wrong3 = f"Resting: {resting_bpm + 20} bpm; Post-exercise: {exercise_bpm + 20} bpm; Overall increase: {diff} bpm."
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Convert 15-second beat counts to beats per minute (multiply by 4):\n"
        f"- Resting: {beats_15s} x 4 = {resting_bpm} bpm.\n"
        f"- Post-exercise: {ex_beats_15s} x 4 = {exercise_bpm} bpm.\n"
        f"**Step 2:** Calculate net difference:\n"
        f"- {exercise_bpm} - {resting_bpm} = {diff} bpm.\n\n"
        f"**Step 3:** The correct values are: **{correct}**."
    )
    return {
        "id": f"ns9_crs_29_{rng.randint(100000, 999999)}",
        "subskill": "29_investigating_pulse_rate_radial_carotid_artery_beats_per_minute",
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
            "tier_1": "How many 15-second periods make up one full minute (60 seconds)?",
            "tier_2": "Multiply each 15-second count by 4, then subtract resting from post-exercise.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["pulse_rate_calculation_bpm_radial_artery_misconception"],
    }


# 30. Investigating exhaled air limewater calcium carbonate cloudiness
def arch_30_investigating_exhaled_air_limewater_calcium_carbonate_cloudiness(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a classic biology practical, a student uses a drinking straw to gently bubble exhaled air through a test tube containing clear limewater [aqueous Ca(OH)2].\n\n"
        f"What chemical observation occurs, and which balanced chemical reaction explains why limewater serves as an indicator for carbon dioxide?"
    )
    correct = (
        "The clear limewater turns milky/cloudy; carbon dioxide reacts with calcium hydroxide to form an insoluble white precipitate of calcium carbonate "
        "[Ca(OH)2 + CO2 -> CaCO3(s) + H2O]."
    )
    wrong1 = (
        "The limewater turns bright purple because inhaled oxygen oxidizes calcium into metallic calcium gas."
    )
    wrong2 = (
        "The limewater remains crystal clear; exhaled air contains zero carbon dioxide because all carbon is converted to pure sugar in lungs."
    )
    wrong3 = (
        "The test tube violently boils and forms solid gold crystals from nitrogen gas."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze chemical test for carbon dioxide:\n"
        f"- Reagent: Clear limewater [calcium hydroxide solution, Ca(OH)2(aq)].\n"
        f"- Reaction: Ca(OH)2(aq) + CO2(g) -> CaCO3(s) + H2O(l).\n"
        f"**Step 2:** Physical observation: The insoluble CaCO3 precipitate turns the solution milky/cloudy.\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_30_{rng.randint(100000, 999999)}",
        "subskill": "30_investigating_exhaled_air_limewater_calcium_carbonate_cloudiness",
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
            "tier_1": "What happens to clear limewater when carbon dioxide is bubbled through it?",
            "tier_2": "Limewater turns milky/cloudy due to insoluble calcium carbonate precipitate (CaCO3).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["limewater_carbon_dioxide_calcium_carbonate_milky_misconception"],
    }


# 31. Bell jar model balloons rubber sheet analogy limitations
def arch_31_bell_jar_model_balloons_rubber_sheet_analogy_limitations(rng: random.Random) -> Dict[str, Any]:
    analogies = [
        ("Glass bell jar", "Rigid thoracic cage / ribcage and chest cavity"),
        ("Rubber sheet at base", "Muscular diaphragm"),
        ("Y-shaped glass tube", "Trachea and two primary bronchi"),
        ("Two balloons inside jar", "Left and right lungs"),
    ]
    parts_map = "\n".join(f"- {a[0]}: represents the {a[1]}" for a in analogies)
    limitations = [
        "In the model, the glass jar is rigid and cannot move, whereas in the human body, the ribs actively move upwards and outwards via intercostal muscles",
        "The balloons expand passively by air rushing in, but real lungs contain millions of microscopic alveoli rather than a hollow elastic balloon",
        "The model lacks pleural membranes and fluid that reduce friction between lungs and thoracic wall",
    ]
    lim = rng.choice(limitations)
    prompt = (
        f"A bell jar apparatus is constructed to demonstrate the mechanics of human breathing:\n"
        f"{parts_map}\n\n"
        f"Pulling the rubber sheet downwards causes the balloons to inflate.\n"
        f"What is a major biological **limitation** of this physical model compared to the human respiratory system?"
    )
    correct = lim
    distractors = [
        "The human lungs contain pure vacuum with zero pressure at all times.",
        "The human diaphragm is made of solid bone that cannot move up or down.",
        "The human trachea carries solid food directly into both lungs during inhalation.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze bell jar model components and analogy to human thorax.\n"
        f"**Step 2:** Evaluate model limitations:\n"
        f"- In the body: Ribs move up and out via external intercostals, expanding the chest in 3 dimensions.\n"
        f"- In the model: Glass walls are completely rigid and stationary.\n\n"
        f"**Step 3:** The accurate limitation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_31_{rng.randint(100000, 999999)}",
        "subskill": "31_bell_jar_model_balloons_rubber_sheet_analogy_limitations",
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
            "tier_1": "Can the glass walls of the bell jar move like real ribs do?",
            "tier_2": "The glass bell jar is rigid and cannot move, unlike human ribs that swing upwards and outwards.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["bell_jar_lung_model_analogies_and_limitations_misconception"],
    }


# 32. Lung volumes tidal volume vital capacity residual volume
def arch_32_lung_volumes_tidal_volume_vital_capacity_residual_volume(rng: random.Random) -> Dict[str, Any]:
    volumes = [
        (
            "Tidal Volume (TV, ~500 mL)",
            "The volume of air inspired or expired with each normal, effortless resting breath",
        ),
        (
            "Vital Capacity (VC, ~4000-5000 mL)",
            "The maximum volume of air that can be forcibly exhaled after a maximum inspiration (TV + IRV + ERV)",
        ),
        (
            "Residual Volume (RV, ~1200 mL)",
            "The volume of air remaining in the lungs even after the most forceful exhalation; keeps alveoli continuously inflated and prevents lung collapse (atelectasis)",
        ),
    ]
    name, definition = rng.choice(volumes)
    prompt = (
        f"Spirometry measures dynamic respiratory volumes and capacities during pulmonary function testing.\n\n"
        f"What is the medical definition and physiological significance of **{name}**?"
    )
    correct = definition
    distractors = [v[1] for v in volumes if v[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review standard pulmonary volumes and capacities.\n"
        f"**Step 2:** Match {name} to definition:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct definition is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_32_{rng.randint(100000, 999999)}",
        "subskill": "32_lung_volumes_tidal_volume_vital_capacity_residual_volume",
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
            "tier_1": f"Is {name} a normal resting breath, maximum breath, or leftover air?",
            "tier_2": "Tidal = normal quiet breath; Vital capacity = max breath in to max out; Residual = air that never leaves lungs.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["spirometry_lung_volumes_vital_capacity_residual_misconception"],
    }


# 33. Respiratory disorders asthma bronchospasm inflammation inhalers
def arch_33_respiratory_disorders_asthma_bronchospasm_inflammation_inhalers(rng: random.Random) -> Dict[str, Any]:
    elements = [
        (
            "Pathophysiological triad of an acute asthma attack",
            "Bronchospasm (constriction of smooth muscle around bronchioles), chronic mucosal inflammation with edema, and excessive secretion of thick viscous mucus narrowing airways",
        ),
        (
            "Bronchodilator rescue inhaler (e.g. Salbutamol / Ventolin)",
            "Beta-2 adrenergic agonist that rapidly relaxes smooth muscle around constricted bronchioles to immediately widen the airway lumen during wheezing and dyspnea",
        ),
        (
            "Steroid preventer inhaler (Corticosteroids)",
            "Anti-inflammatory medication taken daily to reduce chronic baseline inflammation, swelling, and hypersensitivity of the bronchial lining",
        ),
    ]
    name, mechanism = rng.choice(elements)
    prompt = (
        f"Asthma is a common chronic inflammatory disease of the airways affecting millions of South Africans.\n\n"
        f"Which statement accurately explains the **{name}**?"
    )
    correct = mechanism
    distractors = [e[1] for e in elements if e[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze asthma pathophysiology and pharmacological management.\n"
        f"**Step 2:** Relate {name} to mechanism:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_33_{rng.randint(100000, 999999)}",
        "subskill": "33_respiratory_disorders_asthma_bronchospasm_inflammation_inhalers",
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
            "tier_1": f"Recall how asthma affects bronchioles and how {name} works.",
            "tier_2": "Asthma causes bronchiole constriction, swelling, and mucus; bronchodilators relax muscle, steroids reduce inflammation.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["asthma_pathophysiology_bronchospasm_inhalers_misconception"],
    }


# 34. Respiratory disorders chronic bronchitis mucus airway obstruction
def arch_34_respiratory_disorders_chronic_bronchitis_mucus_airway_obstruction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Chronic bronchitis is a component of Chronic Obstructive Pulmonary Disease (COPD), commonly triggered by long-term tobacco smoking or industrial airborne dust.\n\n"
        f"Which clinical pathology and anatomical change defines **chronic bronchitis**?"
    )
    correct = (
        "Persistent chronic inflammation of the bronchial lining leading to hypertrophy of goblet cells, hypersecretion of mucus, "
        "destruction of respiratory cilia, and persistent productive cough for at least 3 months in two consecutive years."
    )
    wrong1 = (
        "Complete calcification of the vocal cords causing complete inability to swallow solid food."
    )
    wrong2 = (
        "Bacterial infection of the kidney causing blood to enter the bronchial tree during sleep."
    )
    wrong3 = (
        "Temporary sneezing caused by walking past freshly cut grass that resolves within 10 seconds."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze chronic bronchitis pathology:\n"
        f"- Chronic bronchial mucosal inflammation.\n"
        f"- Goblet cell hyperplasia -> excessive thick mucus.\n"
        f"- Ciliary loss -> inability to clear mucus -> persistent productive cough.\n\n"
        f"**Step 2:** The correct clinical definition is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_34_{rng.randint(100000, 999999)}",
        "subskill": "34_respiratory_disorders_chronic_bronchitis_mucus_airway_obstruction",
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
            "tier_1": "What happens to the bronchial lining and mucus production in chronic bronchitis?",
            "tier_2": "Bronchial inflammation, swollen goblet cells producing excessive mucus, and paralyzed cilia causing smoker's cough.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["chronic_bronchitis_copd_mucus_hypersecretion_misconception"],
    }


# 35. Respiratory disorders emphysema alveolar wall destruction surface loss
def arch_35_respiratory_disorders_emphysema_alveolar_wall_destruction_surface_loss(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Emphysema is an irreversible degenerative respiratory disease primarily caused by chronic cigarette smoking.\n\n"
        f"Which histological mechanism explains the devastating loss of respiratory function in **emphysema**?"
    )
    correct = (
        "Cigarette smoke toxins stimulate macrophage elastase release that breaks down elastic fibers and destroys delicate alveolar septal walls; "
        "clusters of tiny alveoli coalesce into large, stiff, irregular air pockets, drastically reducing the surface area available for gas exchange and causing severe breathlessness."
    )
    wrong1 = (
        "Alveoli fill with liquid nitrogen from air, causing the lungs to turn into brittle ice crystals."
    )
    wrong2 = (
        "The trachea expands until it fills the entire abdominal cavity, crushing the liver and kidneys."
    )
    wrong3 = (
        "The lungs double their surface area by growing extra ciliated cells on the outside of the ribs."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze emphysema histology and biophysics:\n"
        f"- Destruction of alveolar septal walls and elastin fibers.\n"
        f"- Loss of total surface area for diffusion (from 90 m² down to <20 m²).\n"
        f"- Loss of elastic recoil -> air trapping and severe dyspnea.\n\n"
        f"**Step 2:** The correct histological mechanism is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_35_{rng.randint(100000, 999999)}",
        "subskill": "35_respiratory_disorders_emphysema_alveolar_wall_destruction_surface_loss",
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
            "tier_1": "What happens to the alveolar walls and gas exchange surface area in emphysema?",
            "tier_2": "Alveolar walls are broken down, merging into fewer, larger spaces, drastically reducing surface area for diffusion.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["emphysema_alveolar_destruction_surface_area_reduction_misconception"],
    }


# 36. Respiratory infections tuberculosis mycobacterium granulomas dots
def arch_36_respiratory_infections_tuberculosis_mycobacterium_granulomas_dots(rng: random.Random) -> Dict[str, Any]:
    aspects = [
        (
            "Causative pathogen and transmission",
            "Caused by the acid-fast bacterium *Mycobacterium tuberculosis*; transmitted via infectious droplet nuclei expelled through coughing, sneezing, or spitting by a person with active pulmonary TB",
        ),
        (
            "Pathological hallmark in lung tissue",
            "Formation of granulomas (tubercles) where macrophages wall off the bacilli; necrosis leads to caseous ('cheese-like') center and cavitation destroying lung parenchyma",
        ),
        (
            "Directly Observed Treatment, Short-course (DOTS)",
            "A standardized 6-month combination antibiotic regimen (rifampicin, isoniazid, pyrazinamide, ethambutol) observed by a healthcare worker to prevent default and drug resistance (MDR-TB)",
        ),
    ]
    topic, detail = rng.choice(aspects)
    prompt = (
        f"Tuberculosis (TB) is a major communicable infectious disease and a leading cause of mortality in South Africa.\n\n"
        f"Which clinical statement accurately describes **{topic}** in tuberculosis management?"
    )
    correct = detail
    distractors = [a[1] for a in aspects if a[0] != topic]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review tuberculosis microbiology, pathology, and public health protocol.\n"
        f"**Step 2:** Relate to {topic}:\n"
        f"- {topic}: {correct}\n\n"
        f"**Step 3:** The correct statement is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_36_{rng.randint(100000, 999999)}",
        "subskill": "36_respiratory_infections_tuberculosis_mycobacterium_granulomas_dots",
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
            "tier_1": f"Recall the bacteria, lung tubercles, or 6-month DOTS treatment for: {topic}.",
            "tier_2": "TB is caused by *M. tuberculosis*, forms lung tubercles, and requires strict 6-month DOTS antibiotics.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["tuberculosis_mycobacterium_dots_granuloma_misconception"],
    }


# 37. Respiratory infections pneumonia alveolar fluid consolidation
def arch_37_respiratory_infections_pneumonia_alveolar_fluid_consolidation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Pneumonia is an acute inflammatory infection of one or both lungs caused by bacteria (e.g. *Streptococcus pneumoniae*), viruses, or fungi.\n\n"
        f"What is the pathophysiological mechanism that leads to impaired gas exchange during **pneumonia**?"
    )
    correct = (
        "Inflammatory exudate, pus, and fluid accumulate inside the alveolar air sacs (consolidation), "
        "dramatically thickening the diffusion barrier and blocking inhaled air from contacting the capillary endothelium, causing severe hypoxia."
    )
    wrong1 = (
        "The trachea turns into a solid muscle block that swallows the entire esophagus."
    )
    wrong2 = (
        "Pneumonia causes all alveoli to double their oxygen absorption, turning venous blood completely blue."
    )
    wrong3 = (
        "White blood cells leave the body completely and turn into external chest hair."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze pneumonia pathophysiology:\n"
        f"- Pathogen triggers acute inflammatory response in terminal bronchioles and alveoli.\n"
        f"- Capillaries leak protein-rich fluid, neutrophils, and cellular debris into alveoli (consolidation).\n"
        f"- Fluid-filled alveoli cannot exchange gases, causing hypoxemia.\n\n"
        f"**Step 2:** The correct physiological mechanism is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_37_{rng.randint(100000, 999999)}",
        "subskill": "37_respiratory_infections_pneumonia_alveolar_fluid_consolidation",
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
            "tier_1": "What fills the alveoli during pneumonia?",
            "tier_2": "Alveoli fill with inflammatory fluid and pus (consolidation), preventing oxygen from diffusing into blood.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["pneumonia_alveolar_exudate_consolidation_misconception"],
    }


# 38. Smoking pathology tar carcinogens nicotine carbon monoxide
def arch_38_smoking_pathology_tar_carcinogens_nicotine_carbon_monoxide(rng: random.Random) -> Dict[str, Any]:
    components = [
        (
            "Tar",
            "Sticky black particulate residue that settles in airways, paralyzes and destroys cilia, and contains over 60 known chemical carcinogens that trigger lung, mouth, and throat cancer",
        ),
        (
            "Nicotine",
            "Highly addictive neuroactive stimulant that triggers adrenaline release, constricts peripheral blood vessels, elevates heart rate and blood pressure, and damages vascular endothelium",
        ),
        (
            "Carbon Monoxide (CO)",
            "Colorless, odorless toxic gas that binds to hemoglobin 200 times more tightly than oxygen (forming carboxyhemoglobin), chronically depriving vital tissues and the heart of oxygen",
        ),
    ]
    name, pathology = rng.choice(components)
    prompt = (
        f"Cigarette smoke contains thousands of noxious chemical compounds harmful to the cardiovascular and respiratory systems.\n\n"
        f"Which clinical pathology is directly caused by **{name}**?"
    )
    correct = pathology
    distractors = [c[1] for c in components if c[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify tobacco smoke component: {name}.\n"
        f"**Step 2:** Relate to biological damage:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct pathology is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_38_{rng.randint(100000, 999999)}",
        "subskill": "38_smoking_pathology_tar_carcinogens_nicotine_carbon_monoxide",
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
            "tier_1": f"Think about whether {name} causes cancer/ciliary paralysis, vascular constriction, or oxygen deprivation.",
            "tier_2": "Tar = carcinogens and paralyzed cilia; Nicotine = addiction and high BP; Carbon monoxide = binds hemoglobin.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["tobacco_smoke_tar_nicotine_carbon_monoxide_pathology_misconception"],
    }


# 39. Cardiovascular disorders hypertension high blood pressure risks
def arch_39_cardiovascular_disorders_hypertension_high_blood_pressure_risks(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Hypertension (high blood pressure) is often referred to as the 'silent killer' because it typically causes no overt symptoms until severe organ damage occurs.\n\n"
        f"What clinical threshold defines hypertension in adults, and what long-term pathophysiological complications does it cause?"
    )
    correct = (
        "Persistently elevated resting blood pressure >= 140/90 mmHg; causes strain and micro-tears in arterial walls, accelerating atherosclerosis, "
        "left ventricular hypertrophy, heart failure, renal damage, and ischemic or hemorrhagic stroke."
    )
    wrong1 = (
        "Resting blood pressure below 80/50 mmHg; causes bones to turn soft and flexible like rubber."
    )
    wrong2 = (
        "Blood pressure fluctuating between 110/70 and 120/80 mmHg; requires immediate surgical amputation of the toes."
    )
    wrong3 = (
        "Zero pulse in the wrists with complete absence of heart contractions for over 10 days."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review clinical parameters of hypertension:\n"
        f"- Diagnostic threshold: Systolic >= 140 mmHg and/or Diastolic >= 90 mmHg.\n"
        f"- Target organ damage: Heart (hypertrophy, CAD), Brain (stroke), Kidneys (renal failure).\n\n"
        f"**Step 2:** The correct definition and risk profile is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_39_{rng.randint(100000, 999999)}",
        "subskill": "39_cardiovascular_disorders_hypertension_high_blood_pressure_risks",
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
            "tier_1": "What reading defines hypertension, and which organs are damaged?",
            "tier_2": "Hypertension is >= 140/90 mmHg; causes heart attacks, strokes, and kidney damage.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["hypertension_clinical_threshold_and_target_organ_damage_misconception"],
    }


# 40. Cardiovascular disorders atherosclerosis plaque coronary artery disease
def arch_40_cardiovascular_disorders_atherosclerosis_plaque_coronary_artery_disease(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Coronary Artery Disease (CAD) is predominantly caused by the progressive development of atherosclerosis.\n\n"
        f"Which histological sequence describes the formation of an **atherosclerotic plaque (atheroma)** inside an artery?"
    )
    correct = (
        "Endothelial damage (from hypertension or smoking) -> LDL cholesterol infiltrates the arterial wall -> macrophages engulf oxidized LDL forming foam cells -> "
        "fibrous cap and smooth muscle proliferation form an atheroma plaque, narrowing the lumen and restricting arterial blood flow."
    )
    wrong1 = (
        "Arterial smooth muscles absorb stomach acid and turn into bone plates that fall out through the fingertips."
    )
    wrong2 = (
        "Red blood cells dissolve their nuclei and form pure water droplets that burst the capillary walls."
    )
    wrong3 = (
        "Blood vessels widen into enormous sacs that hold 50 liters of extra liquid inside the lungs."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze atherogenesis sequence:\n"
        f"1. Endothelial injury.\n"
        f"2. Infiltration and oxidation of LDL lipids.\n"
        f"3. Macrophages consume lipids -> foam cells.\n"
        f"4. Fibrous plaque narrows arterial lumen (ischemia).\n\n"
        f"**Step 2:** The correct histological sequence is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_40_{rng.randint(100000, 999999)}",
        "subskill": "40_cardiovascular_disorders_atherosclerosis_plaque_coronary_artery_disease",
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
            "tier_1": "How does cholesterol and macrophage accumulation build a plaque in arteries?",
            "tier_2": "Endothelial damage -> LDL oxidation -> foam cell accumulation -> fibrous cap narrows lumen.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["atherosclerosis_pathogenesis_foam_cells_plaque_misconception"],
    }


# 41. Cardiovascular disorders myocardial infarction heart attack ischemia
def arch_41_cardiovascular_disorders_myocardial_infarction_heart_attack_ischemia(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A myocardial infarction (commonly called a heart attack) is an acute medical emergency.\n\n"
        f"What is the precise pathophysiological cause of a **heart attack**?"
    )
    correct = (
        "A coronary artery branch becomes acutely occluded (typically by a thrombus forming on a ruptured atherosclerotic plaque), "
        "depriving downstream cardiac muscle (myocardium) of oxygen and nutrients; the resulting ischemia causes irreversible necrosis (infarction) of heart tissue."
    )
    wrong1 = (
        "The lungs stop producing carbon dioxide, causing the heart to explode from excessive oxygen."
    )
    wrong2 = (
        "The digestive stomach acid leaks through the diaphragm and dissolves the tricuspid valve."
    )
    wrong3 = (
        "The pacemaker in the right atrium runs out of battery and needs to be replaced with a solar panel."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze myocardial infarction pathology:\n"
        f"- Coronary artery carries oxygenated blood to heart muscle itself.\n"
        f"- Plaque rupture + thrombosis -> acute blockage.\n"
        f"- Ischemia (lack of blood/O2) -> cell death (infarction) of myocardium.\n\n"
        f"**Step 2:** The correct pathophysiological explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_41_{rng.randint(100000, 999999)}",
        "subskill": "41_cardiovascular_disorders_myocardial_infarction_heart_attack_ischemia",
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
            "tier_1": "Which blood vessels supply the heart muscle itself?",
            "tier_2": "Blockage of a coronary artery deprives heart muscle of oxygen, causing tissue death (infarction).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["myocardial_infarction_coronary_thrombosis_ischemia_misconception"],
    }


# 42. Cardiovascular disorders stroke cerebrovascular accident ischemic vs hemorrhagic
def arch_42_cardiovascular_disorders_stroke_cerebrovascular_accident_ischemic_vs_hemorrhagic(rng: random.Random) -> Dict[str, Any]:
    types = [
        (
            "Ischemic Stroke (~85% of cases)",
            "A blood clot (thrombus or embolus) blocks a cerebral artery supplying brain tissue, cutting off oxygen and glucose and causing rapid neuronal death",
        ),
        (
            "Hemorrhagic Stroke (~15% of cases)",
            "A weakened cerebral blood vessel ruptures (often due to chronic untreated hypertension or an aneurysm), bleeding into brain tissue and increasing intracranial pressure",
        ),
    ]
    name, mechanism = rng.choice(types)
    prompt = (
        f"A stroke (cerebrovascular accident) occurs when blood flow to part of the brain is interrupted.\n\n"
        f"What is the neurological mechanism and clinical hallmark of an **{name}**?"
    )
    correct = mechanism
    alt = [t for t in types if t[0] != name][0]
    options = [
        correct,
        alt[1],
        "Brain cells disconnect from the skull and migrate into the stomach to help with digestion.",
        "Cerebral spinal fluid turns into pure nitrogen, freezing the spinal cord instantly.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare ischemic vs hemorrhagic stroke mechanisms:\n"
        f"- Ischemic: Blockage by a blood clot -> lack of perfusion.\n"
        f"- Hemorrhagic: Blood vessel ruptures -> bleeding into brain parenchyma.\n\n"
        f"**Step 2:** Match {name}:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_42_{rng.randint(100000, 999999)}",
        "subskill": "42_cardiovascular_disorders_stroke_cerebrovascular_accident_ischemic_vs_hemorrhagic",
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
            "tier_1": f"Is {name.split()[0]} caused by a blood clot blockage or a ruptured bleeding vessel?",
            "tier_2": "Ischemic = blood clot blockage; Hemorrhagic = blood vessel rupture/bleed.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["stroke_cerebrovascular_accident_ischemic_vs_hemorrhagic_misconception"],
    }


# 43. Healthy lifestyle aerobic exercise cardiac output stroke volume
def arch_43_healthy_lifestyle_aerobic_exercise_cardiac_output_stroke_volume(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Regular aerobic cardiovascular training induces long-term physiological adaptations in the heart muscle.\n\n"
        f"How does aerobic conditioning affect **stroke volume (SV)**, **resting heart rate (HR)**, and **cardiac output (CO)**?"
    )
    correct = (
        "Myocardial hypertrophy of the left ventricle increases stroke volume (more blood pumped per beat); "
        "consequently, resting heart rate decreases (resting bradycardia) while maintaining adequate resting cardiac output (CO = HR x SV)."
    )
    wrong1 = (
        "The heart shrinks in size, stroke volume drops to zero, and the person must breathe 500 times per minute to survive."
    )
    wrong2 = (
        "Heart muscle turns into cartilage, preventing any contractions from occurring during sleep."
    )
    wrong3 = (
        "Blood pressure rises permanently above 250 mmHg and resting heart rate increases to 200 bpm."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze formula: Cardiac Output (CO) = Heart Rate (HR) x Stroke Volume (SV).\n"
        f"**Step 2:** Training effect:\n"
        f"- Stronger myocardium -> higher SV.\n"
        f"- To maintain normal CO at rest, resting HR decreases (athlete's bradycardia, ~45-60 bpm).\n\n"
        f"**Step 3:** The correct physiological adaptation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_43_{rng.randint(100000, 999999)}",
        "subskill": "43_healthy_lifestyle_aerobic_exercise_cardiac_output_stroke_volume",
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
            "tier_1": "Recall: Cardiac output = Heart rate x Stroke volume.",
            "tier_2": "Conditioned hearts pump MORE blood per beat (higher stroke volume), allowing a SLOWER resting heart rate.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cardiac_output_stroke_volume_exercise_adaptation_misconception"],
    }


# 44. Healthy lifestyle low salt low saturated fat diet cholesterol
def arch_44_healthy_lifestyle_low_salt_low_saturated_fat_diet_cholesterol(rng: random.Random) -> Dict[str, Any]:
    dietary_factors = [
        (
            "Excess dietary salt (Sodium chloride / NaCl)",
            "Promotes osmotic water retention in the bloodstream, increasing circulating plasma volume and elevating arterial blood pressure (hypertension)",
        ),
        (
            "High saturated and trans-fat intake",
            "Elevates circulating Low-Density Lipoprotein (LDL) cholesterol, accelerating arterial atheroma plaque deposition and narrowing coronary vessels",
        ),
        (
            "High dietary fiber and unsaturated fats (Omega-3)",
            "Helps lower blood cholesterol levels, stabilizes endothelial function, and reduces platelet aggregation and thrombosis risk",
        ),
    ]
    name, mechanism = rng.choice(dietary_factors)
    prompt = (
        f"Dietary choices directly influence cardiovascular morbidity and mortality.\n\n"
        f"Which physiological mechanism explains the health impact of **{name}**?"
    )
    correct = mechanism
    distractors = [d[1] for d in dietary_factors if d[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze nutritional cardiovascular physiology.\n"
        f"**Step 2:** Relate {name} to hemodynamic/metabolic effect:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_44_{rng.randint(100000, 999999)}",
        "subskill": "44_healthy_lifestyle_low_salt_low_saturated_fat_diet_cholesterol",
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
            "tier_1": f"How does {name} affect blood volume, blood pressure, or cholesterol?",
            "tier_2": "Salt retains water and raises blood pressure; saturated fats raise LDL cholesterol and cause plaque.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cardiovascular_diet_salt_hypertension_ldl_cholesterol_misconception"],
    }


# 45. First aid cpr cardiopulmonary resuscitation chest compressions aed
def arch_45_first_aid_cpr_cardiopulmonary_resuscitation_chest_compressions_aed(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When an individual suffers cardiac arrest, immediate cardiopulmonary resuscitation (CPR) can double or triple survival chances.\n\n"
        f"What is the standard ratio of chest compressions to rescue breaths in adult CPR, and what is the mechanical purpose of chest compressions?"
    )
    correct = (
        "30 chest compressions followed by 2 rescue breaths (rate of 100-120 compressions/min, depth of 5-6 cm in center of chest); "
        "compressions physically squeeze the heart between sternum and spine to maintain artificial blood circulation to the brain and vital organs until an Automated External Defibrillator (AED) arrives."
    )
    wrong1 = (
        "10 rescue breaths followed by 1 chest compression; compressions are designed to crack ribs so excess air can escape."
    )
    wrong2 = (
        "100 compressions and 50 rescue breaths; the rescuer must pour warm water down the airway to jump-start heart cells."
    )
    wrong3 = (
        "Zero compressions; the rescuer simply waits quietly for 30 minutes without touching the patient."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review CPR guidelines:\n"
        f"- Standard adult ratio: 30 compressions to 2 breaths.\n"
        f"- Rate: 100-120 compressions per minute.\n"
        f"- Depth: 5-6 cm on lower half of sternum.\n"
        f"**Step 2:** Mechanical objective: Artificially pump oxygenated blood to the brain.\n\n"
        f"**Step 3:** The correct protocol is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_45_{rng.randint(100000, 999999)}",
        "subskill": "45_first_aid_cpr_cardiopulmonary_resuscitation_chest_compressions_aed",
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
            "tier_1": "Recall the universal CPR compression-to-breath ratio: 30:2.",
            "tier_2": "30 compressions at 100-120 bpm, followed by 2 breaths, maintaining blood flow to the brain.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cardiopulmonary_resuscitation_cpr_ratio_and_technique_misconception"],
    }


# 46. First aid choking heimlich maneuver foreign body airway obstruction
def arch_46_first_aid_choking_heimlich_maneuver_foreign_body_airway_obstruction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A person choking on food exhibits severe foreign body airway obstruction (cannot speak, cough, or breathe, clutching their throat with both hands).\n\n"
        f"Which first aid intervention should be performed, and what mechanical principle makes it effective?"
    )
    correct = (
        "Perform abdominal thrusts (the Heimlich maneuver): stand behind the victim, place a fist just above the navel, and deliver quick inward and upward thrusts; "
        "this forcefully pushes the diaphragm upwards, compressing residual air inside the lungs to create an artificial cough that pops the obstruction out."
    )
    wrong1 = (
        "Give the victim a large glass of water to wash the food down into the bronchial tree."
    )
    wrong2 = (
        "Have the person lie flat on their back and jump forcefully on their knees."
    )
    wrong3 = (
        "Wait 10 minutes to see if the foreign object dissolves on its own."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Identify severe foreign body airway obstruction signs (universal choking sign).\n"
        f"**Step 2:** Technique: Abdominal thrusts (Heimlich maneuver).\n"
        f"- Mechanism: Quick inward/upward thrust elevates diaphragm -> compresses residual lung air -> expels foreign object.\n\n"
        f"**Step 3:** The correct intervention is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_46_{rng.randint(100000, 999999)}",
        "subskill": "46_first_aid_choking_heimlich_maneuver_foreign_body_airway_obstruction",
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
            "tier_1": "What first aid procedure uses quick upward thrusts below the ribcage to expel choking objects?",
            "tier_2": "Heimlich maneuver (abdominal thrusts) pushes diaphragm up to create an artificial cough.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["first_aid_choking_heimlich_maneuver_airway_clearing_misconception"],
    }


# 47. Blood transfusions abo blood groups antigens antibodies agglutination
def arch_47_blood_transfusions_abo_blood_groups_antigens_antibodies_agglutination(rng: random.Random) -> Dict[str, Any]:
    groups = [
        (
            "Type A",
            "Has A antigens on erythrocytes; produces anti-B antibodies in plasma; can receive blood from Type A and Type O",
        ),
        (
            "Type B",
            "Has B antigens on erythrocytes; produces anti-A antibodies in plasma; can receive blood from Type B and Type O",
        ),
        (
            "Type AB",
            "Has both A and B antigens on erythrocytes; produces neither anti-A nor anti-B antibodies in plasma; universal recipient",
        ),
        (
            "Type O",
            "Has neither A nor B antigens on erythrocytes; produces both anti-A and anti-B antibodies in plasma; universal donor (O negative)",
        ),
    ]
    name, profile = rng.choice(groups)
    prompt = (
        f"The ABO blood grouping system is determined by glycoprotein antigens on red blood cell membranes and matching antibodies in plasma.\n\n"
        f"Which clinical profile accurately characterizes blood **{name}** in transfusion compatibility?"
    )
    correct = profile
    distractors = [g[1] for g in groups if g[0] != name]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review ABO antigen-antibody matrix.\n"
        f"**Step 2:** Match {name}:\n"
        f"- {name}: {correct}\n\n"
        f"**Step 3:** The correct profile is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_47_{rng.randint(100000, 999999)}",
        "subskill": "47_blood_transfusions_abo_blood_groups_antigens_antibodies_agglutination",
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
            "tier_1": f"What antigens are on {name} RBCs, and what antibodies are in the plasma?",
            "tier_2": "Type A has A antigen (anti-B); Type B has B antigen (anti-A); Type AB has both (neither); Type O has neither (both antibodies).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["abo_blood_group_antigens_antibodies_agglutination_misconception"],
    }


# 48. Blood transfusions rhesus factor rh incompatibility erythroblastosis fetalis
def arch_48_blood_transfusions_rhesus_factor_rh_incompatibility_erythroblastosis_fetalis(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Rhesus incompatibility can arise during pregnancy between a mother and her developing fetus.\n\n"
        f"Under which specific maternal-fetal blood combination can **erythroblastosis fetalis (hemolytic disease of the newborn)** develop, and how is it prevented?"
    )
    correct = (
        "An Rh-negative mother carrying an Rh-positive fetus: fetal Rh+ red blood cells leak into maternal blood during first delivery, sensitizing mother to produce anti-Rh antibodies; "
        "in subsequent Rh+ pregnancies, maternal anti-Rh IgG antibodies cross the placenta and destroy fetal red blood cells; prevented by administering anti-D immunoglobulin (RhoGAM) within 72 hours of delivery."
    )
    wrong1 = (
        "An Rh-positive mother carrying an Rh-negative fetus: the mother turns Rh-negative and rejects her own liver."
    )
    wrong2 = (
        "Both mother and baby are Rh-negative: the baby's blood turns into plasma without red cells."
    )
    wrong3 = (
        "Both mother and baby are Rh-positive: excessive antibodies cause the placenta to become solid bone."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze Rh incompatibility etiology:\n"
        f"- Mother: Rh-negative (lacks D antigen).\n"
        f"- Fetus: Rh-positive (inherits D antigen from father).\n"
        f"**Step 2:** Sensitization occurs during birth of 1st child -> anti-Rh antibodies formed.\n"
        f"**Step 3:** 2nd pregnancy: Maternal anti-Rh IgG antibodies cross placenta -> destroy fetal erythrocytes.\n"
        f"- Prevention: Inject anti-D immunoglobulin (RhoGAM).\n\n"
        f"**Step 4:** The correct clinical scenario is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_48_{rng.randint(100000, 999999)}",
        "subskill": "48_blood_transfusions_rhesus_factor_rh_incompatibility_erythroblastosis_fetalis",
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
            "tier_1": "Which blood combination causes hemolytic disease: Rh- mother with Rh+ baby, or Rh+ mother with Rh- baby?",
            "tier_2": "Rh-negative mother carrying an Rh-positive baby; prevented with anti-D immunoglobulin (RhoGAM).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["rhesus_incompatibility_rh_negative_mother_rh_positive_fetus_misconception"],
    }


# 49. Evaluating experimental data breathing rate exercise recovery curves
def arch_49_evaluating_experimental_data_breathing_rate_exercise_recovery_curves(rng: random.Random) -> Dict[str, Any]:
    fit_time = rng.choice([2, 3])
    unfit_time = fit_time + rng.choice([4, 5])
    prompt = (
        f"Two learners (Learner A: competitive cross-country runner; Learner B: sedentary student) perform an identical 5-minute step-test.\n"
        f"Their breathing rates and heart rates are recorded every minute during exercise and during recovery.\n\n"
        f"Results show that Learner A returns to resting baseline in **{fit_time} minutes**, while Learner B takes **{unfit_time} minutes** to recover.\n"
        f"Which physiological evaluation explains this disparity in cardiovascular recovery time?"
    )
    correct = (
        f"Learner A has higher cardiovascular efficiency, greater stroke volume, and superior capillarization of muscles; "
        f"their oxygen debt is repaid rapidly ({fit_time} mins vs {unfit_time} mins) and metabolic lactic acid is cleared efficiently."
    )
    wrong1 = (
        "Learner A did not perform the exercise and cheated by holding their breath the entire time."
    )
    wrong2 = (
        "Learner B has twice as many lungs as Learner A, meaning they take longer to exhaust all extra air."
    )
    wrong3 = (
        "Learner A's blood does not contain any carbon dioxide, preventing the brain from receiving nervous impulses."
    )
    options = [correct, wrong1, wrong2, wrong3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze exercise physiology and recovery curves.\n"
        f"**Step 2:** Athletic conditioning features:\n"
        f"- Higher stroke volume, greater cardiac output reserve, denser capillary networks in skeletal muscle.\n"
        f"- Rapid lactic acid clearance and faster oxygen debt repayment.\n\n"
        f"**Step 3:** The correct evaluation is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_49_{rng.randint(100000, 999999)}",
        "subskill": "49_evaluating_experimental_data_breathing_rate_exercise_recovery_curves",
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
            "tier_1": "Why does a physically fit athlete recover their normal breathing and heart rate faster?",
            "tier_2": "Fitter individuals have higher stroke volume and faster oxygen debt repayment, leading to shorter recovery times.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["exercise_recovery_time_cardiovascular_fitness_misconception"],
    }


# 50. Synthetic case study cardiorespiratory failure emergency triage
def arch_50_synthetic_case_study_cardiorespiratory_failure_emergency_triage(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        (
            "A 58-year-old individual collapses clutching their chest with crushing retrosternal pain radiating to the left arm and jaw, sweating profusely and pale",
            "Acute Myocardial Infarction (Heart Attack)",
            "Call emergency services immediately, keep patient calm and seated upright, chew an aspirin (300 mg) to prevent clot expansion, and prepare AED/CPR if consciousness is lost",
        ),
        (
            "A 14-year-old student during a sports match experiences sudden severe wheezing, tight chest, blue-tinged lips (cyanosis), and inability to speak in complete sentences",
            "Severe Acute Asthma Attack",
            "Sit the student upright, administer 4-10 puffs of a Salbutamol (blue) bronchodilator rescue inhaler via spacer, repeat after 4 minutes, and call emergency medical services",
        ),
    ]
    presentation, diagnosis, emergency_action = rng.choice(scenarios)
    prompt = (
        f"**Emergency Clinical Triage Case Study:**\n\n"
        f"Patient presentation: {presentation}.\n\n"
        f"What is the most probable clinical diagnosis and the vital immediate first aid intervention?"
    )
    correct = f"Diagnosis: {diagnosis}.\nAction: {emergency_action}."
    alt = [s for s in scenarios if s[1] != diagnosis][0]
    options = [
        correct,
        f"Diagnosis: {alt[1]}.\nAction: {alt[2]}.",
        "Diagnosis: Normal muscle cramp.\nAction: Give the person two large energy drinks and make them run 5 kilometers.",
        "Diagnosis: Food poisoning.\nAction: Induce vomiting using raw seawater and apply warm mud to the chest.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze clinical signs: {presentation}.\n"
        f"**Step 2:** Formulate diagnosis and emergency protocol:\n"
        f"- {correct}\n\n"
        f"**Step 3:** The correct diagnosis and triage response is: **{correct}**."
    )
    return {
        "id": f"ns9_crs_50_{rng.randint(100000, 999999)}",
        "subskill": "50_synthetic_case_study_cardiorespiratory_failure_emergency_triage",
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
            "tier_1": f"Look at the symptom pattern: {presentation[:60]}...",
            "tier_2": "Match chest pain radiating to arm = heart attack; wheezing/cyanosis = severe asthma.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cardiorespiratory_emergency_triage_diagnosis_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "26_cellular_respiration_link_glucose_oxygen_atp_carbon_dioxide_water": arch_26_cellular_respiration_link_glucose_oxygen_atp_carbon_dioxide_water,
    "27_aerobic_vs_anaerobic_respiration_lactic_acid_oxygen_debt": arch_27_aerobic_vs_anaerobic_respiration_lactic_acid_oxygen_debt,
    "28_investigating_breathing_rate_physical_exercise_fair_test": arch_28_investigating_breathing_rate_physical_exercise_fair_test,
    "29_investigating_pulse_rate_radial_carotid_artery_beats_per_minute": arch_29_investigating_pulse_rate_radial_carotid_artery_beats_per_minute,
    "30_investigating_exhaled_air_limewater_calcium_carbonate_cloudiness": arch_30_investigating_exhaled_air_limewater_calcium_carbonate_cloudiness,
    "31_bell_jar_model_balloons_rubber_sheet_analogy_limitations": arch_31_bell_jar_model_balloons_rubber_sheet_analogy_limitations,
    "32_lung_volumes_tidal_volume_vital_capacity_residual_volume": arch_32_lung_volumes_tidal_volume_vital_capacity_residual_volume,
    "33_respiratory_disorders_asthma_bronchospasm_inflammation_inhalers": arch_33_respiratory_disorders_asthma_bronchospasm_inflammation_inhalers,
    "34_respiratory_disorders_chronic_bronchitis_mucus_airway_obstruction": arch_34_respiratory_disorders_chronic_bronchitis_mucus_airway_obstruction,
    "35_respiratory_disorders_emphysema_alveolar_wall_destruction_surface_loss": arch_35_respiratory_disorders_emphysema_alveolar_wall_destruction_surface_loss,
    "36_respiratory_infections_tuberculosis_mycobacterium_granulomas_dots": arch_36_respiratory_infections_tuberculosis_mycobacterium_granulomas_dots,
    "37_respiratory_infections_pneumonia_alveolar_fluid_consolidation": arch_37_respiratory_infections_pneumonia_alveolar_fluid_consolidation,
    "38_smoking_pathology_tar_carcinogens_nicotine_carbon_monoxide": arch_38_smoking_pathology_tar_carcinogens_nicotine_carbon_monoxide,
    "39_cardiovascular_disorders_hypertension_high_blood_pressure_risks": arch_39_cardiovascular_disorders_hypertension_high_blood_pressure_risks,
    "40_cardiovascular_disorders_atherosclerosis_plaque_coronary_artery_disease": arch_40_cardiovascular_disorders_atherosclerosis_plaque_coronary_artery_disease,
    "41_cardiovascular_disorders_myocardial_infarction_heart_attack_ischemia": arch_41_cardiovascular_disorders_myocardial_infarction_heart_attack_ischemia,
    "42_cardiovascular_disorders_stroke_cerebrovascular_accident_ischemic_vs_hemorrhagic": arch_42_cardiovascular_disorders_stroke_cerebrovascular_accident_ischemic_vs_hemorrhagic,
    "43_healthy_lifestyle_aerobic_exercise_cardiac_output_stroke_volume": arch_43_healthy_lifestyle_aerobic_exercise_cardiac_output_stroke_volume,
    "44_healthy_lifestyle_low_salt_low_saturated_fat_diet_cholesterol": arch_44_healthy_lifestyle_low_salt_low_saturated_fat_diet_cholesterol,
    "45_first_aid_cpr_cardiopulmonary_resuscitation_chest_compressions_aed": arch_45_first_aid_cpr_cardiopulmonary_resuscitation_chest_compressions_aed,
    "46_first_aid_choking_heimlich_maneuver_foreign_body_airway_obstruction": arch_46_first_aid_choking_heimlich_maneuver_foreign_body_airway_obstruction,
    "47_blood_transfusions_abo_blood_groups_antigens_antibodies_agglutination": arch_47_blood_transfusions_abo_blood_groups_antigens_antibodies_agglutination,
    "48_blood_transfusions_rhesus_factor_rh_incompatibility_erythroblastosis_fetalis": arch_48_blood_transfusions_rhesus_factor_rh_incompatibility_erythroblastosis_fetalis,
    "49_evaluating_experimental_data_breathing_rate_exercise_recovery_curves": arch_49_evaluating_experimental_data_breathing_rate_exercise_recovery_curves,
    "50_synthetic_case_study_cardiorespiratory_failure_emergency_triage": arch_50_synthetic_case_study_cardiorespiratory_failure_emergency_triage,
}
