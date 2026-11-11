"""Grade 9 Natural Sciences: Term 1 - Systems in the Human Body (Archetypes 26 to 50).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr9/Term 1/02. Systems in the human body.md.
Focus: Muscular mechanics, nervous control, reflex arcs, excretion, endocrine regulation, pathology, and health investigations.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


# 26. Antagonistic muscle pairs biceps and triceps arm movement
def arch_26_antagonistic_muscle_pairs_biceps_and_triceps_arm_movement(rng: random.Random) -> Dict[str, Any]:
    movements = [
        (
            "Flexion of the forearm (bending the elbow to raise the hand toward the shoulder)",
            "The biceps brachii muscle contracts (shortens and bulges) acting as the flexor agonist, while the triceps brachii muscle relaxes (lengthens) as the antagonist",
        ),
        (
            "Extension of the forearm (straightening the elbow to lower the arm)",
            "The triceps brachii muscle contracts (shortens) acting as the extensor agonist, while the biceps brachii muscle relaxes (lengthens) as the antagonist",
        ),
    ]
    target_action, muscle_roles = rng.choice(movements)
    prompt = (
        f"Skeletal muscles can only exert a pulling force when they contract; they cannot push.\n\n"
        f"How do the antagonistic muscle pair **biceps and triceps** coordinate during **{target_action}**?"
    )
    correct = muscle_roles
    other_m = [m[1] for m in movements if m[0] != target_action][0]
    options = [
        correct,
        other_m,
        "Both biceps and triceps muscles contract simultaneously with maximum force, snapping the elbow bone in half.",
        "Both muscles relax completely and turn into liquid fat, letting gravity swing the arm uncontrollably.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze antagonistic muscle mechanics:\n"
        f"- Muscles work in antagonistic pairs (as one contracts, the other relaxes).\n"
        f"- For {target_action}: {muscle_roles}.\n\n"
        f"**Step 2:** The correct coordination is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_26_{rng.randint(100000, 999999)}",
        "subskill": "26_antagonistic_muscle_pairs_biceps_and_triceps_arm_movement",
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
            "tier_1": f"To bend or straighten the arm, which muscle pulls and which one relaxes?",
            "tier_2": "Flexion: biceps contracts, triceps relaxes; Extension: triceps contracts, biceps relaxes.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["antagonistic_muscle_pairs_coordination_misconception"],
    }


# 27. Nervous system central vs peripheral organization
def arch_27_nervous_system_central_vs_peripheral_organization(rng: random.Random) -> Dict[str, Any]:
    divisions = [
        (
            "Central Nervous System (CNS)",
            "Comprises the brain and spinal cord; acts as the primary processing, integration, and command centre of the body",
        ),
        (
            "Peripheral Nervous System (PNS)",
            "Comprises all cranial and spinal nerves branching outside the brain and spinal cord; transmits sensory impulses toward the CNS and motor commands away to effectors",
        ),
    ]
    target_div, desc = rng.choice(divisions)
    prompt = (
        f"The human nervous system is anatomically divided into the Central Nervous System (CNS) and Peripheral Nervous System (PNS).\n\n"
        f"Which anatomical structures and primary physiological role define the **{target_div}**?"
    )
    correct = desc
    other_div = [d[1] for d in divisions if d[0] != target_div][0]
    options = [
        correct,
        other_div,
        "Comprises the fingernails and toenails; acts as electric light receptors that glow in the dark",
        "Comprises the kidneys and urinary bladder; coordinates conscious thought and memory",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review nervous system organization:\n"
        f"- CNS = brain + spinal cord (integration & decision making).\n"
        f"- PNS = peripheral nerves (sensory input & motor output communication lines).\n\n"
        f"**Step 2:** For {target_div}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_27_{rng.randint(100000, 999999)}",
        "subskill": "27_nervous_system_central_vs_peripheral_organization",
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
            "tier_1": f"Does {target_div} include the brain/spinal cord or the branching nerves?",
            "tier_2": "CNS consists of the brain and spinal cord; PNS consists of nerves extending throughout the body.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["cns_vs_pns_anatomical_distinction_misconception"],
    }


# 28. Neuron structure sensory relay interneuron and motor neurons
def arch_28_neuron_structure_sensory_relay_interneuron_and_motor_neurons(rng: random.Random) -> Dict[str, Any]:
    neurons = [
        ("Sensory neuron (afferent)", "Transmits electrical nerve impulses from sensory receptors (e.g. in skin or eyes) toward the central nervous system (spinal cord/brain)"),
        ("Interneuron / Relay neuron (connector)", "Located entirely within the grey matter of the spinal cord or brain; processes information and connects sensory neurons to motor neurons"),
        ("Motor neuron (efferent)", "Transmits nerve impulses away from the central nervous system to effectors (muscles or glands) to elicit a response"),
    ]
    target_n, function = rng.choice(neurons)
    prompt = (
        f"Neurons are specialized electro-conductive cells that transmit information throughout the nervous system.\n\n"
        f"What is the direction of impulse conduction and functional role of a **{target_n}**?"
    )
    correct = function
    alt = [n[1] for n in neurons if n[0] != target_n]
    options = [correct] + alt
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Classify functional neuron types:\n"
        f"- Sensory (afferent): receptor -> CNS.\n"
        f"- Interneuron/Relay: within CNS (bridges sensory and motor).\n"
        f"- Motor (efferent): CNS -> effector muscle/gland.\n\n"
        f"**Step 2:** For {target_n}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_28_{rng.randint(100000, 999999)}",
        "subskill": "28_neuron_structure_sensory_relay_interneuron_and_motor_neurons",
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
            "tier_1": f"Where does a {target_n.split()[0].lower()} neuron carry signals: toward the CNS, inside the CNS, or to an effector?",
            "tier_2": "Sensory brings input to CNS; interneuron links inside CNS; motor carries output to muscle.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["sensory_relay_motor_neuron_pathways_misconception"],
    }


# 29. Reflex arc neural pathway stimulus to effector response
def arch_29_reflex_arc_neural_pathway_stimulus_to_effector_response(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        ("accidentally touching a scorching hot metal stove plate with a fingertip", "pain thermoreceptors in fingertip skin", "biceps muscle contracts to rapidly withdraw the hand"),
        ("stepping barefoot on a sharp acacia thorn in the veld", "nociceptors (pain receptors) in sole of foot", "hamstring muscles contract to instantly flex knee and lift foot"),
    ]
    hazard, receptor, response = rng.choice(scenarios)
    prompt = (
        f"When a person reacts to **{hazard}**, an involuntary **reflex action** occurs before the sensation reaches the conscious brain.\n\n"
        f"What is the correct anatomical sequence of components in this **reflex arc**?"
    )
    correct = (
        f"Stimulus -> Receptor ({receptor}) -> Sensory neuron -> Interneuron (in spinal cord grey matter) -> "
        f"Motor neuron -> Effector (muscle) -> Response ({response})"
    )
    wrong_1 = (
        f"Stimulus -> Motor neuron -> Interneuron -> Sensory neuron -> Receptor -> Response"
    )
    wrong_2 = (
        f"Stimulus -> Brain cerebral cortex -> Stomach -> Lungs -> Effector -> Response"
    )
    wrong_3 = (
        f"Stimulus -> Effector -> Sensory neuron -> Motor neuron -> Receptor -> Response"
    )
    options = [correct, wrong_1, wrong_2, wrong_3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** State the canonical reflex arc sequence:\n"
        f"$$\\text{{Stimulus}} \\rightarrow \\text{{Receptor}} \\rightarrow \\text{{Sensory Neuron}} \\rightarrow \\text{{Spinal Interneuron}} \\rightarrow \\text{{Motor Neuron}} \\rightarrow \\text{{Effector}} \\rightarrow \\text{{Response}}$$\n\n"
        f"**Step 2:** Why is it rapid?\n"
        f"- The pathway bypasses the conscious cerebral cortex (synapsing directly in the spinal cord), protecting body tissues from severe burns or lacerations.\n\n"
        f"**Step 3:** The accurate reflex arc sequence is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_29_{rng.randint(100000, 999999)}",
        "subskill": "29_reflex_arc_neural_pathway_stimulus_to_effector_response",
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
            "tier_1": "What comes first: the receptor detecting the stimulus, or the motor neuron triggering the muscle?",
            "tier_2": "Stimulus -> Receptor -> Sensory neuron -> Spinal cord interneuron -> Motor neuron -> Effector -> Response.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["reflex_arc_sequence_misconception"],
    }


# 30. Autonomic reflexes pupillary light reflex and knee jerk
def arch_30_autonomic_reflexes_pupillary_light_reflex_and_knee_jerk(rng: random.Random) -> Dict[str, Any]:
    reflexes = [
        (
            "Pupillary light reflex (shining a bright penlight into a patient's eye)",
            "Photoreceptors in the retina detect bright light; impulses travel via the optic nerve to the midbrain; parasympathetic motor impulses stimulate circular iris sphincter muscles to contract, constricting the pupil to protect the retina from phototoxic damage",
        ),
        (
            "Patellar knee-jerk reflex (tapping the patellar tendon below the kneecap with a reflex hammer)",
            "Muscle spindle stretch receptors in the quadriceps detect sudden stretch; sensory impulses enter the lumbar spinal cord and synapse directly onto motor neurons; quadriceps muscle contracts, causing the lower leg to kick forward",
        ),
    ]
    target_r, mechanism = rng.choice(reflexes)
    prompt = (
        f"Reflex actions can be somatic or autonomic.\n\n"
        f"What is the biological mechanism and survival value of the **{target_r}**?"
    )
    correct = mechanism
    other_r = [r[1] for r in reflexes if r[0] != target_r][0]
    options = [
        correct,
        other_r,
        "The light or tap melts the skull bone, which cools down the ears during exercise.",
        "The stimulus forces the stomach to vomit all ingested proteins within three seconds.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze clinical reflex mechanisms:\n"
        f"- For {target_r}: {mechanism}.\n\n"
        f"**Step 2:** The accurate mechanism is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_30_{rng.randint(100000, 999999)}",
        "subskill": "30_autonomic_reflexes_pupillary_light_reflex_and_knee_jerk",
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
            "tier_1": f"How does the body protect the eye or maintain posture in {target_r.split()[0]}?",
            "tier_2": "The pupillary reflex constricts the iris in bright light; the patellar reflex maintains upright standing balance.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["autonomic_somatic_reflex_mechanisms_misconception"],
    }


# 31. Excretory system organs kidneys ureters bladder urethra
def arch_31_excretory_system_organs_kidneys_ureters_bladder_urethra(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The urinary system filters metabolic wastes and eliminates urine from the human body.\n\n"
        f"What is the correct anatomical pathway of urine from its site of formation to its exit from the body?"
    )
    correct = (
        "Kidneys (renal pyramids & pelvis) -> Ureters (narrow muscular ducts) -> "
        "Urinary Bladder (distensible storage reservoir) -> Urethra (terminal duct to external opening)"
    )
    wrong_1 = (
        "Kidneys -> Urethra -> Urinary Bladder -> Ureters"
    )
    wrong_2 = (
        "Urinary Bladder -> Kidneys -> Ureters -> Urethra"
    )
    wrong_3 = (
        "Kidneys -> Gallbladder -> Stomach -> Ureters"
    )
    options = [correct, wrong_1, wrong_2, wrong_3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace the urinary tract pathway:\n"
        f"- Kidneys form urine in nephrons.\n"
        f"- Urine drains into renal pelvis and down the **ureters** via peristalsis.\n"
        f"- Urine is temporarily stored in the **urinary bladder**.\n"
        f"- Micturition releases urine through the **urethra** to the exterior.\n\n"
        f"**Step 2:** The correct anatomical sequence is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_31_{rng.randint(100000, 999999)}",
        "subskill": "31_excretory_system_organs_kidneys_ureters_bladder_urethra",
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
            "tier_1": "Which tube connects kidney to bladder, and which tube exits the body?",
            "tier_2": "Ureter connects kidney to bladder; urethra carries urine from bladder to outside.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ureter_vs_urethra_anatomical_confusion_misconception"],
    }


# 32. Kidney nephron ultrafiltration reabsorption and urine formation
def arch_32_kidney_nephron_ultrafiltration_reabsorption_and_urine_formation(rng: random.Random) -> Dict[str, Any]:
    stages = [
        (
            "Ultrafiltration",
            "In the Bowman's capsule: high hydrostatic pressure in the glomerulus forces water, glucose, amino acids, urea, and salts through podocyte filtration slits to form glomerular filtrate, while large blood cells and proteins remain in the blood.",
        ),
        (
            "Selective reabsorption",
            "Along the proximal convoluted tubule and loop of Henle: 100% of valuable glucose and amino acids, plus water and essential ions, are actively and passively transported back into peritubular capillaries.",
        ),
        (
            "Tubular excretion / secretion",
            "In the distal convoluted tubule: excess potassium ions, hydrogen ions ($H^+$), and drug metabolites are actively transported from blood into the tubular fluid to form final urine.",
        ),
    ]
    target_s, details = rng.choice(stages)
    prompt = (
        f"Urine formation in each kidney nephron occurs through three fundamental stages: "
        f"ultrafiltration, selective reabsorption, and tubular secretion.\n\n"
        f"Which statement scientifically outlines **{target_s}**?"
    )
    correct = details
    alt = [s[1] for s in stages if s[0] != target_s]
    options = [correct] + alt + ["The kidney burns blood in flames to vaporise all liquid into steam"]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review nephron physiology:\n"
        f"- For {target_s}: {details}.\n\n"
        f"**Step 2:** The correct description is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_32_{rng.randint(100000, 999999)}",
        "subskill": "32_kidney_nephron_ultrafiltration_reabsorption_and_urine_formation",
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
            "tier_1": f"Where does {target_s.lower()} occur and what molecules move?",
            "tier_2": "Ultrafiltration occurs in Bowman's capsule; reabsorption reclaims glucose/water along tubules.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["ultrafiltration_vs_reabsorption_mechanisms_misconception"],
    }


# 33. Osmoregulation and water balance role of ADH
def arch_33_osmoregulation_and_water_balance_role_of_adh(rng: random.Random) -> Dict[str, Any]:
    states = [
        (
            "A person running in the hot Karoo sun without drinking water, becoming dehydrated with high blood osmolarity",
            "Hypothalamus osmoreceptors stimulate the pituitary gland to secrete MORE Antidiuretic Hormone (ADH); ADH increases permeability of kidney collecting ducts to water; more water is reabsorbed into blood; a small volume of concentrated, dark amber urine is excreted.",
        ),
        (
            "A person drinking 2 litres of water while resting in a cool room, causing low blood osmolarity",
            "Pituitary gland secretes LESS ADH; collecting ducts become less permeable to water; less water is reabsorbed; a large volume of dilute, pale straw-coloured urine is excreted.",
        ),
    ]
    scenario, response = rng.choice(states)
    prompt = (
        f"Osmoregulation maintains blood water balance via a negative feedback loop involving **Antidiuretic Hormone (ADH)**.\n\n"
        f"In the case of: **{scenario}**,\n\n"
        f"What is the endocrine and renal physiological response?"
    )
    correct = response
    other_r = [s[1] for s in states if s[0] != scenario][0]
    options = [
        correct,
        other_r,
        "The kidneys stop working permanently and must be removed surgically within two hours.",
        "The brain releases hydrochloric acid into the lungs to produce water molecules from oxygen.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze ADH negative feedback:\n"
        f"- High osmolarity (dehydration) -> MORE ADH -> collecting ducts permeable -> MORE water reabsorbed -> concentrated, low volume urine.\n"
        f"- Low osmolarity (overhydration) -> LESS ADH -> collecting ducts impermeable -> LESS water reabsorbed -> dilute, high volume urine.\n\n"
        f"**Step 2:** The correct physiological response is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_33_{rng.randint(100000, 999999)}",
        "subskill": "33_osmoregulation_and_water_balance_role_of_adh",
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
            "tier_1": "Does dehydration cause MORE or LESS ADH to be released?",
            "tier_2": "Dehydration triggers more ADH, causing kidneys to conserve water and produce concentrated urine.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["adh_osmoregulation_feedback_misconception"],
    }


# 34. Dialysis machine artificial filtration principle
def arch_34_dialysis_machine_artificial_filtration_principle(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Patients suffering from end-stage renal failure depend on regular hemodialysis treatment.\n\n"
        f"What is the biophysical principle of a **dialysis machine**, and how does it clean the patient's blood?"
    )
    correct = (
        "Blood is pumped through semi-permeable dialysis tubing bathed in sterile dialysate fluid; "
        "metabolic wastes (urea, excess salts, creatinine) diffuse down their concentration gradient into the dialysate, "
        "while valuable blood cells, platelets, and large plasma proteins are retained."
    )
    options = [
        correct,
        "The machine boils all of the patient's blood to 120 °C to vaporise all urea into nitrogen gas.",
        "The machine uses permanent magnets that pull white blood cells out through the patient's skin.",
        "The machine replaces all human blood with cold sea water every three days.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Understand hemodialysis mechanics:\n"
        f"- Uses a selectively permeable artificial membrane.\n"
        f"- Dialysate contains optimal concentrations of glucose and ions (no urea).\n"
        f"- Urea and toxins diffuse from blood into dialysate down concentration gradients.\n"
        f"- Blood cells and proteins are too large to pass through pores.\n\n"
        f"**Step 2:** The accurate principle is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_34_{rng.randint(100000, 999999)}",
        "subskill": "34_dialysis_machine_artificial_filtration_principle",
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
            "tier_1": "How do urea and waste molecules leave blood in a dialysis machine?",
            "tier_2": "Wastes diffuse through semi-permeable tubing into dialysate down their concentration gradient.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["dialysis_semipermeable_diffusion_misconception"],
    }


# 35. Endocrine system chemical messengers and bloodstream transport
def arch_35_endocrine_system_chemical_messengers_and_bloodstream_transport(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The endocrine system regulates bodily processes through **hormones**.\n\n"
        f"What defines an **endocrine gland**, and how do hormones reach their specific target organs?"
    )
    correct = (
        "Endocrine glands are ductless glands that secrete chemical hormones directly into surrounding blood capillaries; "
        "the bloodstream carries hormones throughout the body, but they only affect target cells that possess complementary receptor proteins."
    )
    options = [
        correct,
        "Endocrine glands are long plastic tubes that pump solid enzymes through the ear canal.",
        "Endocrine glands spray hot steam across the skin to conduct electrical nerve impulses.",
        "Hormones only travel through empty air when a person speaks loudly.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define endocrine glands and hormone action:\n"
        f"- Endocrine = ductless (secretes directly into circulatory bloodstream).\n"
        f"- Specificity = target cells have complementary surface or intracellular receptors (lock-and-key fit).\n\n"
        f"**Step 2:** The accurate scientific definition: **{correct}**."
    )
    return {
        "id": f"ns9_sys_35_{rng.randint(100000, 999999)}",
        "subskill": "35_endocrine_system_chemical_messengers_and_bloodstream_transport",
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
            "tier_1": "Do endocrine glands have ducts, or do they secrete directly into the bloodstream?",
            "tier_2": "Endocrine glands are ductless, secreting hormones into blood that bind to target receptors.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["endocrine_ductless_bloodstream_transport_misconception"],
    }


# 36. Glucose homeostasis insulin vs glucagon feedback loop
def arch_36_glucose_homeostasis_insulin_vs_glucagon_feedback_loop(rng: random.Random) -> Dict[str, Any]:
    situations = [
        (
            "Blood glucose level rises significantly above normal (e.g. after consuming a carbohydrate-rich meal)",
            "Beta cells in the islets of Langerhans (pancreas) secrete INSULIN; insulin stimulates liver and skeletal muscle cells to take up glucose and convert it into glycogen for storage, lowering blood glucose back to normal",
        ),
        (
            "Blood glucose level drops below normal (e.g. during prolonged fasting or strenuous exercise)",
            "Alpha cells in the islets of Langerhans (pancreas) secrete GLUCAGON; glucagon stimulates liver cells to break down stored glycogen into glucose (glycogenolysis) and release it into the blood, raising blood glucose back to normal",
        ),
    ]
    target_sit, mechanism = rng.choice(situations)
    prompt = (
        f"Blood glucose concentration is tightly regulated around 4.0 to 7.0 mmol/L by the pancreas.\n\n"
        f"When **{target_sit}**,\n\n"
        f"Which hormone is secreted, and what physiological change restores homeostasis?"
    )
    correct = mechanism
    other_s = [s[1] for s in situations if s[0] != target_sit][0]
    options = [
        correct,
        other_s,
        "The stomach secretes sulfuric acid to dissolve all blood cells within five minutes.",
        "The lungs release pure helium gas to lighten the bloodstream.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the glucose homeostatic feedback loop:\n"
        f"- High blood glucose -> INSULIN -> glucose uptake & glycogen storage -> level decreases.\n"
        f"- Low blood glucose -> GLUCAGON -> glycogen breakdown & glucose release -> level increases.\n\n"
        f"**Step 2:** For {target_sit}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_36_{rng.randint(100000, 999999)}",
        "subskill": "36_glucose_homeostasis_insulin_vs_glucagon_feedback_loop",
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
            "tier_1": "Which hormone lowers blood glucose, and which hormone raises it?",
            "tier_2": "Insulin lowers glucose by storing it as glycogen; glucagon raises glucose by breaking down glycogen.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["insulin_vs_glucagon_action_misconception"],
    }


# 37. Fight or flight response adrenaline physiological effects
def arch_37_fight_or_flight_response_adrenaline_physiological_effects(rng: random.Random) -> Dict[str, Any]:
    threats = [
        "suddenly encountering a venomous cape cobra while hiking in the veld",
        "facing an immediate collision with a speeding runaway motor vehicle",
    ]
    threat = rng.choice(threats)
    prompt = (
        f"In acute emergency situations like {threat}, the adrenal medulla releases **adrenaline**.\n\n"
        f"Which coordinated physiological responses prepare the body for immediate **fight or flight**?"
    )
    correct = (
        "Heart rate and cardiac output increase; bronchioles dilate to increase oxygen uptake; "
        "glycogen is rapidly broken down to glucose; blood vessels in skeletal muscles dilate while vessels to the digestive tract constrict."
    )
    options = [
        correct,
        "Heart rate stops; pupils constrict to total darkness; all skeletal muscles fall asleep.",
        "The digestive tract speeds up massive nutrient digestion while breathing completely halts.",
        "Body temperature drops to -20 °C, freezing the brain into solid ice.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze the physiological effects of adrenaline:\n"
        f"- Adrenaline prepares the organism for high-intensity physical action (fight or flight).\n"
        f"- Increased heart rate and breathing -> delivers $O_2$ and glucose to active skeletal muscles.\n"
        f"- Vasoconstriction to gut/skin -> diverts blood away from non-essential organs to muscles and brain.\n\n"
        f"**Step 2:** The coordinated responses are: **{correct}**."
    )
    return {
        "id": f"ns9_sys_37_{rng.randint(100000, 999999)}",
        "subskill": "37_fight_or_flight_response_adrenaline_physiological_effects",
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
            "tier_1": "What happens to heart rate, breathing, and blood flow during an emergency?",
            "tier_2": "Adrenaline increases heart rate, dilates airways, and diverts blood from gut to muscles.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["adrenaline_fight_or_flight_physiological_shifts_misconception"],
    }


# 38. Integumentary system skin thermoregulation sweating and vasodilation
def arch_38_integumentary_system_skin_thermoregulation_sweating_and_vasodilation(rng: random.Random) -> Dict[str, Any]:
    thermal_states = [
        (
            "Hot environment (body core temperature begins to exceed 37.0 °C)",
            "Precapillary arterioles in the skin dilate (vasodilation), increasing blood flow to surface capillaries to radiate heat; sweat glands secrete sweat, which evaporates and absorbs latent heat of vaporization from the skin.",
        ),
        (
            "Cold environment (body core temperature begins to drop below 37.0 °C)",
            "Precapillary arterioles in the skin constrict (vasoconstriction), reducing surface blood flow to conserve core heat; arrector pili muscles contract to raise hairs (trapping an insulating air layer); involuntary shivering generates metabolic heat.",
        ),
    ]
    state_desc, cooling_mech = rng.choice(thermal_states)
    prompt = (
        f"The human skin (integumentary system) plays a vital role in homeostatic **thermoregulation**.\n\n"
        f"In a **{state_desc}**,\n\n"
        f"What physiological mechanisms occur in the dermis and epidermis to maintain a constant 37 °C core temperature?"
    )
    correct = cooling_mech
    other_m = [s[1] for s in thermal_states if s[0] != state_desc][0]
    options = [
        correct,
        other_m,
        "The skin turns into solid iron armor that absorbs radio waves from cell towers.",
        "Skin cells explode to release cool water into the room atmosphere.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze thermoregulatory feedback:\n"
        f"- When hot: vasodilation (increases radiation) + sweating (evaporative cooling).\n"
        f"- When cold: vasoconstriction (conserves heat) + shivering (metabolic heat production) + piloerection.\n\n"
        f"**Step 2:** For {state_desc}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_38_{rng.randint(100000, 999999)}",
        "subskill": "38_integumentary_system_skin_thermoregulation_sweating_and_vasodilation",
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
            "tier_1": f"Do blood vessels in the skin widen (vasodilate) or narrow (vasoconstrict) when {state_desc.split()[0].lower()}?",
            "tier_2": "Heat triggers vasodilation and sweating; cold triggers vasoconstriction, piloerection, and shivering.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["vasodilation_vasoconstriction_thermoregulation_misconception"],
    }


# 39. Immune lymphatic system lymph nodes and pathogen defense
def arch_39_immune_lymphatic_system_lymph_nodes_and_pathogen_defense(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"The lymphatic system consists of lymphatic vessels, lymph fluid, and swollen bean-shaped **lymph nodes**.\n\n"
        f"Why do lymph nodes in the neck or groin swell and become tender during a bacterial or viral throat infection?"
    )
    correct = (
        "Lymph nodes act as biological filters containing dense populations of lymphocytes and macrophages; "
        "when pathogens are drained in lymph to the node, lymphocytes rapidly proliferate and synthesize antibodies, "
        "while macrophages engulf and digest foreign debris, causing the node to swell."
    )
    options = [
        correct,
        "The lymph nodes store heavy gold coins that the body creates when it detects bacteria.",
        "The lymph nodes fill with pure gasoline to burn the throat infection in fire.",
        "The swelling is caused by bone marrow breaking off and falling into the neck.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze lymph node immune function:\n"
        f"- Lymph nodes filter lymph fluid returning to the venous system.\n"
        f"- When pathogens enter, lymphocytes undergo clonal expansion and macrophages phagocytose debris.\n"
        f"- The rapid cellular multiplication causes lymphadenopathy (swollen, tender lymph nodes).\n\n"
        f"**Step 2:** The accurate explanation is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_39_{rng.randint(100000, 999999)}",
        "subskill": "39_immune_lymphatic_system_lymph_nodes_and_pathogen_defense",
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
            "tier_1": "What type of white blood cells multiply inside lymph nodes when fighting an infection?",
            "tier_2": "Lymphocytes multiply and macrophages engulf pathogens in lymph nodes, causing them to swell.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["lymph_node_swelling_immune_function_misconception"],
    }


# 40. Interdependence of circulatory respiratory and digestive systems
def arch_40_interdependence_of_circulatory_respiratory_and_digestive_systems(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Every cell in the human body requires energy produced by aerobic cellular respiration:\n"
        f"$$\\text{{Glucose}} + \\text{{Oxygen}} \\rightarrow \\text{{Carbon Dioxide}} + \\text{{Water}} + \\text{{Energy (ATP)}}$$\n\n"
        f"How do the **digestive, respiratory, and circulatory systems** cooperate to power cellular respiration in a leg muscle cell?"
    )
    correct = (
        "The digestive system breaks down food to absorb glucose into blood; the respiratory system ventilates lungs "
        "to diffuse oxygen into blood; the circulatory system pumps both glucose and oxygen to the leg muscle cell "
        "and transports carbon dioxide waste back to the lungs for exhalation."
    )
    options = [
        correct,
        "The respiratory system swallows bread, the digestive system breathes air, and the circulatory system does nothing.",
        "The digestive system produces pure electricity that flows directly down the nerves without blood.",
        "The three systems operate 100% independently with zero shared vessels or molecules.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Trace the inter-system cooperation:\n"
        f"- Digestive system: supplies glucose.\n"
        f"- Respiratory system: supplies oxygen, removes carbon dioxide.\n"
        f"- Circulatory system: vascular transport medium linking both systems to working cells.\n\n"
        f"**Step 2:** The accurate cooperation is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_40_{rng.randint(100000, 999999)}",
        "subskill": "40_interdependence_of_circulatory_respiratory_and_digestive_systems",
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
            "tier_1": "Which system provides glucose, which provides oxygen, and which transports them?",
            "tier_2": "Digestive supplies glucose, respiratory supplies O2, and circulatory transports both to cells.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["body_systems_interdependence_respiration_misconception"],
    }


# 41. Skeletal health disorders rickets osteoporosis and calcium
def arch_41_skeletal_health_disorders_rickets_osteoporosis_and_calcium(rng: random.Random) -> Dict[str, Any]:
    disorders = [
        (
            "Rickets (in children)",
            "Deficiency of vitamin D or calcium; bones fail to mineralize and remain soft and weak, bending under body weight to cause bowed legs and stunted growth",
            "Ensuring dietary intake of calcium/vitamin D and safe exposure to sunlight",
        ),
        (
            "Osteoporosis (typically in elderly individuals)",
            "Rate of bone resorption exceeds bone formation; bone mineral density severely decreases, making bones porous, brittle, and highly susceptible to pathological fractures (e.g. hip or vertebrae)",
            "Weight-bearing exercise, calcium and vitamin D supplementation, and hormone balance",
        ),
    ]
    dis_name, pathology, prevent = rng.choice(disorders)
    prompt = (
        f"Bone health depends on continuous remodeling and adequate dietary mineral intake.\n\n"
        f"Which clinical profile and prevention strategy defines **{dis_name}**?"
    )
    correct = f"Pathology: {pathology}.\nPrevention: {prevent}."
    alt = [d for d in disorders if d[0] != dis_name][0]
    options = [
        correct,
        f"Pathology: {alt[1]}.\nPrevention: {alt[2]}.",
        "Pathology: Bones turn into solid gold due to excessive fruit juice consumption.\nPrevention: Sleeping in ice.",
        "Pathology: Bones grow feathers and fly out of the arms.\nPrevention: Drinking table vinegar.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Distinguish skeletal disorders:\n"
        f"- Rickets: childhood softening and bowing of bones from vitamin D/calcium deficiency.\n"
        f"- Osteoporosis: porous, brittle bones with low density in adults/elderly.\n\n"
        f"**Step 2:** For {dis_name}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_41_{rng.randint(100000, 999999)}",
        "subskill": "41_skeletal_health_disorders_rickets_osteoporosis_and_calcium",
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
            "tier_1": f"Is {dis_name.split()[0]} soft bowed bones in children or brittle porous bones in elderly?",
            "tier_2": "Rickets affects children (soft bones); osteoporosis affects adults (brittle porous bones).",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["rickets_vs_osteoporosis_pathology_misconception"],
    }


# 42. Circulatory disorders hypertension atherosclerosis heart attack
def arch_42_circulatory_disorders_hypertension_atherosclerosis_heart_attack(rng: random.Random) -> Dict[str, Any]:
    conditions = [
        (
            "Atherosclerosis",
            "Deposition of fatty cholesterol plaques within arterial walls, narrowing the lumen and restricting arterial blood flow",
            "Can lead to myocardial infarction (heart attack) if coronary arteries become occluded",
        ),
        (
            "Hypertension (high blood pressure)",
            "Chronically elevated systolic and diastolic pressure (> 140/90 mmHg) against arterial walls",
            "Forces the heart to work harder, thickening cardiac muscle and increasing risk of stroke, aneurysms, and kidney damage",
        ),
    ]
    cond_name, path, risk = rng.choice(conditions)
    prompt = (
        f"Cardiovascular diseases represent a leading cause of non-communicable mortality.\n\n"
        f"Which clinical description and major health risk defines **{cond_name}**?"
    )
    correct = f"Description: {path}.\nHealth Risk: {risk}."
    alt = [c for c in conditions if c[0] != cond_name][0]
    options = [
        correct,
        f"Description: {alt[1]}.\nHealth Risk: {alt[2]}.",
        "Description: Blood transforms into solid diamonds inside brain veins.\nHealth Risk: Permanent freezing.",
        "Description: The heart grows to the size of a motor car.\nHealth Risk: Inability to fit through doors.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review cardiovascular pathologies:\n"
        f"- Atherosclerosis = plaque buildup narrowing coronary arteries.\n"
        f"- Hypertension = chronic high blood pressure damaging vessels and organs.\n\n"
        f"**Step 2:** For {cond_name}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_42_{rng.randint(100000, 999999)}",
        "subskill": "42_circulatory_disorders_hypertension_atherosclerosis_heart_attack",
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
            "tier_1": f"Is {cond_name} fatty plaque buildup in arteries or chronic high blood pressure?",
            "tier_2": "Atherosclerosis is plaque narrowing; hypertension is chronically high pressure.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["atherosclerosis_vs_hypertension_pathology_misconception"],
    }


# 43. Respiratory disorders asthma bronchitis and smoking impact
def arch_43_respiratory_disorders_asthma_bronchitis_and_smoking_impact(rng: random.Random) -> Dict[str, Any]:
    diseases = [
        (
            "Asthma",
            "Chronic allergic inflammatory disorder causing sudden spasms of smooth muscles around bronchioles, swelling of mucous membranes, and excessive mucus secretion, severely restricting airflow and causing wheezing",
            "Treated using bronchodilator inhalers that relax airway smooth muscles",
        ),
        (
            "Chronic Bronchitis (often exacerbated by tobacco smoking)",
            "Prolonged inflammation of bronchi with destruction of cilia and hypersecretion of mucus; trapped tar and bacteria cause persistent phlegm-producing cough and breathing difficulty",
            "Prevented by smoking cessation and avoiding environmental air pollutants",
        ),
    ]
    target_d, mechanism, management = rng.choice(diseases)
    prompt = (
        f"Respiratory pathologies severely impair gas exchange and air ventilation.\n\n"
        f"Which clinical profile accurately details **{target_d}**?"
    )
    correct = f"Pathology: {mechanism}.\nManagement: {management}."
    alt = [d for d in diseases if d[0] != target_d][0]
    options = [
        correct,
        f"Pathology: {alt[1]}.\nManagement: {alt[2]}.",
        "Pathology: The lungs turn into solid marble stone from eating ice cream.\nManagement: Drinking hot oil.",
        "Pathology: The trachea dissolves into water during rainstorms.\nManagement: Wearing an umbrella indoors.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare asthma vs bronchitis:\n"
        f"- Asthma: bronchiole bronchospasm triggered by allergies/exercise; relieved by bronchodilators.\n"
        f"- Bronchitis: inflammation of bronchi, loss of cilia, excess mucus from smoking/pollution.\n\n"
        f"**Step 2:** For {target_d}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_43_{rng.randint(100000, 999999)}",
        "subskill": "43_respiratory_disorders_asthma_bronchitis_and_smoking_impact",
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
            "tier_1": f"What causes airway narrowing in {target_d}?",
            "tier_2": "Asthma causes bronchiole muscle spasms; bronchitis causes chronic airway inflammation and mucus.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["asthma_vs_bronchitis_mechanisms_misconception"],
    }


# 44. Digestive disorders ulcers anorexia bulimia and obesity
def arch_44_digestive_disorders_ulcers_anorexia_bulimia_and_obesity(rng: random.Random) -> Dict[str, Any]:
    disorders = [
        (
            "Peptic stomach ulcers",
            "Erosion of the protective mucous stomach lining by hydrochloric acid and pepsin, often triggered by *Helicobacter pylori* bacterial infection, leading to painful open sores and bleeding",
        ),
        (
            "Anorexia nervosa",
            "Psychological eating disorder characterized by self-starvation, distorted body image, extreme fear of weight gain, severe malnutrition, and organ damage",
        ),
        (
            "Obesity",
            "Chronic state of excessive body fat accumulation resulting from prolonged energy intake exceeding energy expenditure; increases risk of type 2 diabetes, cardiovascular disease, and osteoarthritis",
        ),
    ]
    target_d, profile = rng.choice(disorders)
    prompt = (
        f"Disorders of the digestive and metabolic system can stem from infection, behavioral pathology, or dietary imbalance.\n\n"
        f"Which clinical definition correctly identifies **{target_d}**?"
    )
    correct = profile
    alt = [d[1] for d in disorders if d[0] != target_d]
    options = [correct] + alt
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review digestive health conditions:\n"
        f"- For {target_d}: {profile}.\n\n"
        f"**Step 2:** The accurate clinical description is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_44_{rng.randint(100000, 999999)}",
        "subskill": "44_digestive_disorders_ulcers_anorexia_bulimia_and_obesity",
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
            "tier_1": f"Is {target_d} related to stomach acid sores, self-starvation, or excess adipose accumulation?",
            "tier_2": f"Match {target_d} to its specific pathological profile.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["digestive_metabolic_disorders_misconception"],
    }


# 45. Excretory disorders kidney stones and renal failure
def arch_45_excretory_disorders_kidney_stones_and_renal_failure(rng: random.Random) -> Dict[str, Any]:
    conditions = [
        (
            "Kidney stones (renal calculi)",
            "Hard crystallized mineral deposits (typically calcium oxalate or uric acid) that precipitate in concentrated urine, causing severe flank pain and hematuria when obstructing the ureter",
            "Prevented by high daily water hydration and balanced dietary calcium/salt intake",
        ),
        (
            "Chronic kidney failure (renal failure)",
            "Progressive, irreversible loss of nephron filtration capacity leading to toxic buildup of urea in blood (uremia), dangerous potassium elevation, and fluid retention",
            "Requires ongoing hemodialysis or renal kidney transplantation for survival",
        ),
    ]
    target_c, pathology, treatment = rng.choice(conditions)
    prompt = (
        f"Renal pathologies impair metabolic waste clearance and fluid balance.\n\n"
        f"Which clinical description and management strategy defines **{target_c}**?"
    )
    correct = f"Pathology: {pathology}.\nManagement: {treatment}."
    alt = [c for c in conditions if c[0] != target_c][0]
    options = [
        correct,
        f"Pathology: {alt[1]}.\nManagement: {alt[2]}.",
        "Pathology: The kidneys turn into solid gold coins.\nManagement: Spending the coins in stores.",
        "Pathology: The bladder flies out of the body during sneezing.\nManagement: Tying it with string.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Compare renal disorders:\n"
        f"- Kidney stones = crystallized mineral precipitates blocking ureter; painful.\n"
        f"- Renal failure = loss of nephron function -> uremia; treated by dialysis or kidney transplant.\n\n"
        f"**Step 2:** For {target_c}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_45_{rng.randint(100000, 999999)}",
        "subskill": "45_excretory_disorders_kidney_stones_and_renal_failure",
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
            "tier_1": f"Is {target_c} mineral crystallization or total loss of filtration function?",
            "tier_2": "Kidney stones are mineral deposits; renal failure requires dialysis or kidney transplant.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["kidney_stones_vs_renal_failure_misconception"],
    }


# 46. Nervous disorders stroke and alcohol drug neuropathy
def arch_46_nervous_disorders_stroke_and_alcohol_drug_neuropathy(rng: random.Random) -> Dict[str, Any]:
    conditions = [
        (
            "Cerebrovascular accident (Stroke)",
            "A sudden interruption of blood supply to a region of the brain (caused by an arterial blockage/thrombus or cerebral hemorrhage), depriving brain neurons of oxygen and causing rapid cell death, paralysis, and speech loss",
        ),
        (
            "Peripheral neuropathy from chronic substance abuse",
            "Progressive chemical degradation of myelin sheaths and peripheral nerve fibres due to chronic alcohol or toxic drug exposure, causing numbness, burning pain, and loss of coordination in limbs",
        ),
    ]
    target_c, desc = rng.choice(conditions)
    prompt = (
        f"Neurological health can be catastrophically damaged by vascular events or chemical toxicity.\n\n"
        f"Which clinical definition correctly identifies **{target_c}**?"
    )
    correct = desc
    alt = [c[1] for c in conditions if c[0] != target_c][0]
    options = [
        correct,
        alt,
        "The brain turns into green leaves that photosynthesize during full daylight",
        "Nerves turn into hollow copper cables that conduct radio music into the teeth",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Review neurological pathologies:\n"
        f"- Stroke = cerebral ischemia or hemorrhage depriving brain neurons of oxygen.\n"
        f"- Neuropathy = toxic degeneration of peripheral nerve axons and myelin.\n\n"
        f"**Step 2:** For {target_c}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_46_{rng.randint(100000, 999999)}",
        "subskill": "46_nervous_disorders_stroke_and_alcohol_drug_neuropathy",
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
            "tier_1": f"What causes brain cell death in {target_c.split()[0]}?",
            "tier_2": "Stroke is interrupted brain blood flow; neuropathy is nerve damage from toxins or diabetes.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["stroke_vs_neuropathy_mechanisms_misconception"],
    }


# 47. Healthy lifestyle balanced diet hydration exercise rest
def arch_47_healthy_lifestyle_balanced_diet_hydration_exercise_rest(rng: random.Random) -> Dict[str, Any]:
    pillars = [
        ("Regular cardiovascular exercise (e.g. 30 minutes of jogging/swimming daily)", "strengthens cardiac muscle, increases lung vital capacity, lowers resting heart rate and blood pressure, and boosts insulin sensitivity"),
        ("Adequate daily hydration (1.5 to 2.5 litres of clean water)", "ensures optimal blood volume, assists renal excretion of urea, prevents kidney stones, and supports cellular metabolic reactions"),
        ("Quality restorative sleep (7 to 9 hours nightly)", "enables neural memory consolidation, release of growth hormone for tissue repair, and immune system rejuvenation"),
    ]
    target_p, benefit = rng.choice(pillars)
    prompt = (
        f"Maintaining human body system integrity requires a preventative, healthy lifestyle.\n\n"
        f"What is the direct physiological benefit of **{target_p}**?"
    )
    correct = f"It {benefit}."
    alt = [p[1] for p in pillars if p[0] != target_p]
    distractors = [f"It {b}." for b in alt]
    distractors.append("It turns all human bones into liquid oil.")
    options = [correct] + distractors[:3]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze physiological health maintenance:\n"
        f"- For {target_p}: {benefit}.\n\n"
        f"**Step 2:** The direct physiological benefit is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_47_{rng.randint(100000, 999999)}",
        "subskill": "47_healthy_lifestyle_balanced_diet_hydration_exercise_rest",
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
            "tier_1": f"What does {target_p.split()[0].lower()} do for body organs?",
            "tier_2": "Exercise strengthens the heart/lungs; hydration aids kidneys; sleep repairs tissues and brain.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["lifestyle_physiology_organ_benefits_misconception"],
    }


# 48. Substance abuse impact on liver cirrhosis and brain damage
def arch_48_substance_abuse_impact_on_liver_cirrhosis_and_brain_damage(rng: random.Random) -> Dict[str, Any]:
    toxins = [
        (
            "Chronic excessive alcohol consumption on the liver",
            "Causes alcoholic fatty liver disease, progressing to hepatitis and irreversible cirrhosis where healthy hepatocytes are replaced by non-functional fibrous scar tissue, leading to hepatic failure and jaundice",
        ),
        (
            "Chronic alcohol and methamphetamine abuse on the central nervous system",
            "Causes neurotoxic destruction of neurons in the frontal cortex and hippocampus, impairing judgment, memory consolidation, and emotional regulation",
        ),
    ]
    substance, organ_damage = rng.choice(toxins)
    prompt = (
        f"Substance abuse severely impairs vital human organs.\n\n"
        f"What is the progressive pathological outcome of **{substance}**?"
    )
    correct = organ_damage
    other_t = [t[1] for t in toxins if t[0] != substance][0]
    options = [
        correct,
        other_t,
        "It turns all body cells into photosynthetic chloroplasts that produce honey.",
        "It causes the liver to turn into a second beating heart with four chambers.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze toxicology of substance abuse:\n"
        f"- Liver: alcohol metabolism produces acetaldehyde, causing fatty infiltration, inflammation, and cirrhosis (scarring).\n"
        f"- Brain: chronic neurotoxicity causes neuronal atrophy, loss of synapses, and cognitive decline.\n\n"
        f"**Step 2:** For {substance}: **{correct}**."
    )
    return {
        "id": f"ns9_sys_48_{rng.randint(100000, 999999)}",
        "subskill": "48_substance_abuse_impact_on_liver_cirrhosis_and_brain_damage",
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
            "tier_1": "How does alcohol damage the liver or brain over time?",
            "tier_2": "Alcohol causes liver cirrhosis (scarring) and neural degeneration in the brain.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["substance_abuse_organ_pathology_misconception"],
    }


# 49. Evaluating fair test investigation human reaction time ruler drop
def arch_49_evaluating_fair_test_investigation_human_reaction_time_ruler_drop(rng: random.Random) -> Dict[str, Any]:
    trials = [
        ("distraction (normal quiet room vs texting on a mobile phone)", "presence of mobile phone distraction", "catch distance on the 30 cm ruler (in cm)", "same ruler, dropped from the same zero mark between fingers, same catcher"),
        ("fatigue (well-rested in the morning vs sleep-deprived at midnight)", "state of rest vs sleep deprivation", "reaction distance caught on the ruler (in cm)", "same person catching, same drop method, same room lighting"),
    ]
    investigation_desc, indep, dep, controlled = rng.choice(trials)
    prompt = (
        f"Grade 9 learners investigate factors affecting human reaction time using the **ruler drop method**.\n\n"
        f"They test the effect of **{investigation_desc}**.\n\n"
        f"Which option accurately identifies the **independent variable**, the **dependent variable**, and the **controlled variables**?"
    )
    correct = (
        f"Independent: {indep};\n"
        f"Dependent: {dep};\n"
        f"Controlled: {controlled}"
    )
    options = [
        correct,
        f"Independent: {dep};\nDependent: {indep};\nControlled: None required in biological investigations",
        f"Independent: {controlled};\nDependent: {dep};\nControlled: {indep}",
        "Independent: The weather outside;\nDependent: The colour of socks worn;\nControlled: Gravity",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Define investigation variables:\n"
        f"- Independent variable: the factor deliberately altered ({indep}).\n"
        f"- Dependent variable: the response measured ({dep}).\n"
        f"- Controlled variables: factors held constant to ensure experimental validity ({controlled}).\n\n"
        f"**Step 2:** The correct identification is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_49_{rng.randint(100000, 999999)}",
        "subskill": "49_evaluating_fair_test_investigation_human_reaction_time_ruler_drop",
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
            "tier_1": "Which factor did the learners change, and which factor did they measure in cm?",
            "tier_2": "The independent variable is the condition tested; the dependent variable is the catch distance.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["reaction_time_investigation_variables_misconception"],
    }


# 50. Synthetic case study multi organ system failure and emergency triage
def arch_50_synthetic_case_study_multi_organ_system_failure_and_emergency_triage(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (
            "An endurance marathon runner collapses in 36 °C heat: severe disorientation, cessation of sweating, core body temperature 40.5 °C, weak rapid pulse, dark brown urine",
            "Integumentary and excretory failure (Severe heat stroke with acute dehydration and rhabdomyolysis)",
            "Immediate rapid cooling (ice immersion/misting), intravenous fluid hydration, and emergency transport to intensive care",
        ),
        (
            "A patient presents with acute crushing chest pain radiating down the left arm, shortness of breath, pale clammy skin, and cyanosis (bluish lips)",
            "Circulatory and respiratory crisis (Myocardial infarction / acute coronary occlusion depriving cardiac muscle of oxygen)",
            "Administering supplemental oxygen, chewing aspirin to reduce platelet clotting, sublingual nitroglycerin, and urgent coronary angioplasty",
        ),
    ]
    presentation, diagnosis, intervention = rng.choice(cases)
    prompt = (
        f"A medical emergency response team assesses a critically ill patient.\n\n"
        f"Clinical findings: *\"{presentation}\"*\n\n"
        f"What is the primary organ system diagnosis and life-saving medical intervention?"
    )
    correct = f"Diagnosis: {diagnosis}.\nIntervention: {intervention}."
    alt = [c for c in cases if c[0] != presentation][0]
    options = [
        correct,
        f"Diagnosis: {alt[1]}.\nIntervention: {alt[2]}.",
        "Diagnosis: Excessive fingernail growth.\nIntervention: Trimming fingernails with scissors.",
        "Diagnosis: Lack of gravity in the bones.\nIntervention: Tying sandbags to the patient's ears.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Analyze clinical case findings:\n"
        f"- Patient presentation: {presentation}.\n"
        f"- Diagnosis: {diagnosis}.\n"
        f"- Emergency intervention: {intervention}.\n\n"
        f"**Step 2:** The correct medical triage is: **{correct}**."
    )
    return {
        "id": f"ns9_sys_50_{rng.randint(100000, 999999)}",
        "subskill": "50_synthetic_case_study_multi_organ_system_failure_and_emergency_triage",
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
            "tier_1": f"Look at the organs affected in: {presentation[:60]}...",
            "tier_2": "Match the clinical symptom constellation to the correct diagnosis and emergency intervention.",
            "tier_3": f"The answer is: {correct}.",
        },
        "misconception_tags": ["multi_organ_system_triage_diagnosis_misconception"],
    }


BUILDERS: Dict[str, Any] = {
    "26_antagonistic_muscle_pairs_biceps_and_triceps_arm_movement": arch_26_antagonistic_muscle_pairs_biceps_and_triceps_arm_movement,
    "27_nervous_system_central_vs_peripheral_organization": arch_27_nervous_system_central_vs_peripheral_organization,
    "28_neuron_structure_sensory_relay_interneuron_and_motor_neurons": arch_28_neuron_structure_sensory_relay_interneuron_and_motor_neurons,
    "29_reflex_arc_neural_pathway_stimulus_to_effector_response": arch_29_reflex_arc_neural_pathway_stimulus_to_effector_response,
    "30_autonomic_reflexes_pupillary_light_reflex_and_knee_jerk": arch_30_autonomic_reflexes_pupillary_light_reflex_and_knee_jerk,
    "31_excretory_system_organs_kidneys_ureters_bladder_urethra": arch_31_excretory_system_organs_kidneys_ureters_bladder_urethra,
    "32_kidney_nephron_ultrafiltration_reabsorption_and_urine_formation": arch_32_kidney_nephron_ultrafiltration_reabsorption_and_urine_formation,
    "33_osmoregulation_and_water_balance_role_of_adh": arch_33_osmoregulation_and_water_balance_role_of_adh,
    "34_dialysis_machine_artificial_filtration_principle": arch_34_dialysis_machine_artificial_filtration_principle,
    "35_endocrine_system_chemical_messengers_and_bloodstream_transport": arch_35_endocrine_system_chemical_messengers_and_bloodstream_transport,
    "36_glucose_homeostasis_insulin_vs_glucagon_feedback_loop": arch_36_glucose_homeostasis_insulin_vs_glucagon_feedback_loop,
    "37_fight_or_flight_response_adrenaline_physiological_effects": arch_37_fight_or_flight_response_adrenaline_physiological_effects,
    "38_integumentary_system_skin_thermoregulation_sweating_and_vasodilation": arch_38_integumentary_system_skin_thermoregulation_sweating_and_vasodilation,
    "39_immune_lymphatic_system_lymph_nodes_and_pathogen_defense": arch_39_immune_lymphatic_system_lymph_nodes_and_pathogen_defense,
    "40_interdependence_of_circulatory_respiratory_and_digestive_systems": arch_40_interdependence_of_circulatory_respiratory_and_digestive_systems,
    "41_skeletal_health_disorders_rickets_osteoporosis_and_calcium": arch_41_skeletal_health_disorders_rickets_osteoporosis_and_calcium,
    "42_circulatory_disorders_hypertension_atherosclerosis_heart_attack": arch_42_circulatory_disorders_hypertension_atherosclerosis_heart_attack,
    "43_respiratory_disorders_asthma_bronchitis_and_smoking_impact": arch_43_respiratory_disorders_asthma_bronchitis_and_smoking_impact,
    "44_digestive_disorders_ulcers_anorexia_bulimia_and_obesity": arch_44_digestive_disorders_ulcers_anorexia_bulimia_and_obesity,
    "45_excretory_disorders_kidney_stones_and_renal_failure": arch_45_excretory_disorders_kidney_stones_and_renal_failure,
    "46_nervous_disorders_stroke_and_alcohol_drug_neuropathy": arch_46_nervous_disorders_stroke_and_alcohol_drug_neuropathy,
    "47_healthy_lifestyle_balanced_diet_hydration_exercise_rest": arch_47_healthy_lifestyle_balanced_diet_hydration_exercise_rest,
    "48_substance_abuse_impact_on_liver_cirrhosis_and_brain_damage": arch_48_substance_abuse_impact_on_liver_cirrhosis_and_brain_damage,
    "49_evaluating_fair_test_investigation_human_reaction_time_ruler_drop": arch_49_evaluating_fair_test_investigation_human_reaction_time_ruler_drop,
    "50_synthetic_case_study_multi_organ_system_failure_and_emergency_triage": arch_50_synthetic_case_study_multi_organ_system_failure_and_emergency_triage,
}
