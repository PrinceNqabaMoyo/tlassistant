"""Natural Sciences Grade 9 Term 1: Systems in the Human Body Topic Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 1/02. Systems in the human body.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. human_system_purposes: Comprehensive functional matching across all major organ systems.
2. nervous_system_reflex_arc: Stepwise neural impulse conduction pathway and reflex arc.
3. excretory_system_filtration: Excretory tract structures, nephron filtration, and fluid balance.
4. musculoskeletal_mechanics: Antagonistic muscle pairs, skeletal support, tendons vs ligaments.
5. pathology_and_lifestyle: Systemic disorders (rickets, osteoporosis, kidney stones, alcohol/drug impact).
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.organ_diagram_builders import build_nephron_question

TOPIC_NAME = "Systems in the human body"
ORDERED_SUBSKILLS = [
    "human_system_purposes",
    "nervous_system_reflex_arc",
    "excretory_system_filtration",
    "musculoskeletal_mechanics",
    "pathology_and_lifestyle",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_sys"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any]) -> Dict[str, Any]:
    if "title" not in res or not res["title"]:
        res["title"] = "Excretory System & Kidney Nephron Anatomy"
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
    elif subskill in ("excretory", "nephron", "kidney_nephron"):
        return _normalize_res(build_nephron_question(actual_seed, grade=9, mode=mode))
    elif subskill in ORDERED_SUBSKILLS:
        chosen_subskill = subskill
    else:
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]

    # Subskill 1: Human System Purposes
    if chosen_subskill == "human_system_purposes":
        systems = [
            (
                "Nervous System",
                "Receives sensory stimuli, transmits electrochemical impulses, and coordinates rapid bodily responses",
                "Brain, spinal cord, sensory organs, peripheral nerves",
                "nervous_system_function_confusion",
            ),
            (
                "Excretory System",
                "Filters metabolic wastes from blood and regulates water, salt, and pH fluid balance",
                "Kidneys, ureters, urinary bladder, urethra",
                "excretory_digestive_conflation",
            ),
            (
                "Musculoskeletal System",
                "Provides internal structural support, protects delicate organs, and enables locomotion via antagonistic muscle pairs",
                "Bones, skeletal muscles, cartilage, tendons, ligaments",
                "musculoskeletal_structure_confusion",
            ),
            (
                "Respiratory System",
                "Supplies oxygen to the bloodstream for cellular respiration and removes carbon dioxide via diffusion across alveoli",
                "Trachea, bronchi, bronchioles, lungs, alveoli, diaphragm",
                "respiratory_circulatory_conflation",
            ),
            (
                "Digestive System",
                "Breaks down ingested food mechanically and chemically into dissolved nutrients for systemic absorption",
                "Mouth, oesophagus, stomach, small intestine, large intestine, pancreas, liver",
                "digestive_absorption_confusion",
            ),
        ]
        target = systems[actual_seed % len(systems)]
        question_text = (
            "The human body functions through integrated organ systems.\n\n"
            f"1. State the **primary physiological purpose** of the **{target[0]}**.\n"
            f"2. List **three major organs or components** belonging to the {target[0]}.\n"
            "3. Explain briefly how this system cooperates with the circulatory system to maintain life."
        )
        sample = (
            f"1. **Primary Purpose:** {target[1]};\n"
            f"2. **Components:** {target[2]};\n"
            f"3. The circulatory system transports the required substances (e.g. oxygen, nutrients, hormones, or metabolic wastes) to and from the organs of the {target[0]} via blood vessels."
        )
        marking = (
            f"• 1 mark: Accurate purpose stated ({target[1]}) [1]\n"
            f"• 2 marks: Two or more correct organs/components ({target[2]}) [2]\n"
            "• 1 mark: Clear explanation of interaction with blood circulation [1]\n"
            "**Total: 4 marks**"
        )
        return {
            "title": f"System Purpose: {target[0]}",
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
                f"What is the main role of the {target[0]} in keeping a person alive and responsive?",
                f"Recall which organs make up this system: {target[2]}.",
                f"Purpose: {target[1]}. Components include {target[2]}.",
            ],
            "misconception_tags": [target[3], "system_interdependence_misconception"],
            "learning_objective_id": "NS9.LL.02.01",
        }

    # Subskill 2: Nervous System Reflex Arc
    if chosen_subskill == "nervous_system_reflex_arc":
        stimuli = [
            ("accidentally touches a boiling kettle", "pain/heat receptors in the fingertip skin", "biceps muscle contracts to jerk the hand away"),
            ("steps barefoot on a sharp thorn", "pain receptors in the sole of the foot", "hamstring/leg muscles contract to withdraw the foot"),
            ("suddenly perceives a blinding flash of light", "photoreceptors in the retina of the eye", "pupil sphincter muscle contracts to constrict the pupil"),
        ]
        st = stimuli[actual_seed % len(stimuli)]
        question_text = (
            f"A learner {st[0]}.\n\n"
            "1. Sequence the **5 structural components of a neural reflex arc** in the exact order an impulse travels:\n"
            "   *Effector, Sensory Neuron, Central Nervous System (Spinal Cord), Receptor, Motor Neuron*\n"
            f"2. Identify the specific **receptor** and **effector** in this scenario.\n"
            "3. Explain why this response occurs automatically before the brain registers conscious pain perception."
        )
        sample = (
            "1. **Reflex Arc Sequence:**\n"
            "   $$\\text{Stimulus} \\to \\text{Receptor} \\to \\text{Sensory Neuron} \\to \\text{CNS (Spinal Cord)} \\to \\text{Motor Neuron} \\to \\text{Effector}$$\n"
            f"2. **Receptor:** {st[1]}; **Effector:** {st[2]};\n"
            "3. Reflex arcs bypass conscious brain processing and are coordinated directly through spinal synapses, ensuring an immediate, rapid withdrawal that minimizes tissue damage."
        )
        marking = (
            "• 2 marks: Exact 5-stage sequence in correct order [2]\n"
            f"• 2 marks: Correct receptor ({st[1]}) [1] and effector ({st[2]}) [1]\n"
            "• 1 mark: Biological rationale: rapid spinal bypass prevents severe tissue damage [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Neural Reflex Arc & Conduction Pathway",
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
                "The message starts at the sense organ (receptor) and ends at the working muscle or gland (effector).",
                "Sensory neuron carries information in; motor neuron carries the command out.",
                "Sequence: Receptor → Sensory Neuron → CNS (Spinal Cord) → Motor Neuron → Effector.",
            ],
            "misconception_tags": ["reflex_arc_sequence_inversion", "brain_required_for_reflex_misconception"],
            "learning_objective_id": "NS9.LL.02.02",
        }

    # Subskill 3: Excretory System & Nephron Filtration
    if chosen_subskill == "excretory_system_filtration":
        if actual_seed % 2 == 0:
            return _normalize_res(build_nephron_question(actual_seed, grade=9, mode=mode))
        question_text = (
            "The human urinary system continuously purifies blood and maintains osmotic fluid balance.\n\n"
            "1. Distinguish between the functions of the **ureters** and the **urethra**.\n"
            "2. Name the microscopic functional filtering units located inside the renal cortex and medulla of the kidneys.\n"
            "3. State **two main metabolic waste substances** removed from blood plasma to form urine.\n"
            "4. What medical technology is used when a patient experiences acute kidney failure?"
        )
        sample = (
            "1. **Ureters:** Muscular tubes that transport urine from each kidney to the urinary bladder; "
            "**Urethra:** Single tube that carries urine from the bladder to the exterior of the body during urination;\n"
            "2. **Nephrons** (each kidney contains approximately 1 million nephrons);\n"
            "3. **Metabolic Wastes:** Urea (from nitrogenous protein breakdown), excess salts, and excess water (or creatinine/uric acid);\n"
            "4. **Renal Dialysis** (haemodialysis machine / artificial kidney)."
        )
        marking = (
            "• 2 marks: Difference between ureter (kidney to bladder) [1] and urethra (bladder to outside) [1]\n"
            "• 1 mark: Nephrons [1]\n"
            "• 1 mark: Two waste products (urea, excess salts, water, creatinine) [1]\n"
            "• 1 mark: Kidney dialysis / haemodialysis [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Excretory System & Kidney Function",
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
                "Ureters connect kidneys to bladder; the urethra leads out of the body.",
                "The filtering units in the kidney are called nephrons, which filter out urea and excess salts.",
                "Ureters lead to bladder; urethra leads out. Filtering units: nephrons. Treatment: dialysis.",
            ],
            "misconception_tags": ["ureter_urethra_confusion", "excretion_egestion_conflation"],
            "learning_objective_id": "NS9.LL.02.03",
        }

    # Subskill 4: Musculoskeletal Mechanics
    if chosen_subskill == "musculoskeletal_mechanics":
        question_text = (
            "Skeletal muscles can only contract (pull); they cannot actively push.\n\n"
            "1. Explain what is meant by an **antagonistic muscle pair**, using the **biceps and triceps** of the upper arm as an example.\n"
            "2. Distinguish between the structural functions of **tendons** and **ligaments**.\n"
            "3. Describe the role of **cartilage** at synovial joints."
        )
        sample = (
            "1. **Antagonistic Muscle Pair:** A pair of muscles that work in opposition to each other to produce movement around a joint. "
            "To bend (flex) the elbow, the biceps contracts while the triceps relaxes; to straighten (extend) the arm, the triceps contracts while the biceps relaxes;\n"
            "2. **Tendons:** Inelastic, tough connective tissue that joins skeletal muscle to bone; "
            "**Ligaments:** Elastic, strong connective tissue that joins bone to bone across a joint to stabilize it;\n"
            "3. **Cartilage:** Smooth, tough protective tissue covering the ends of bones, preventing friction and absorbing mechanical shock during movement."
        )
        marking = (
            "• 2 marks: Antagonistic definition [1] with biceps/triceps flexion/extension mechanism [1]\n"
            "• 2 marks: Tendons (muscle to bone) [1] vs Ligaments (bone to bone) [1]\n"
            "• 1 mark: Cartilage prevents bone-on-bone friction and absorbs shock [1]\n"
            "**Total: 5 marks**"
        )
        return {
            "title": "Musculoskeletal Mechanics & Connective Tissues",
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
                "Remember: muscles can only pull, never push. When one flexes, its partner must relax.",
                "Tendons connect muscle to bone. Ligaments connect bone to bone.",
                "Antagonistic pair: biceps contracts to flex, triceps contracts to extend. Tendons: muscle-bone; Ligaments: bone-bone.",
            ],
            "misconception_tags": ["tendon_ligament_interchange", "muscle_push_misconception"],
            "learning_objective_id": "NS9.LL.02.04",
        }

    # Subskill 5: Pathology and Lifestyle
    disorders = [
        (
            "Osteoporosis",
            "Skeletal System",
            "Bones lose calcium mineral density, becoming porous, brittle, and highly susceptible to fractures",
            "Ensure adequate dietary calcium and vitamin D intake, and perform weight-bearing exercise",
            "osteoporosis_calcium_misconception",
        ),
        (
            "Rickets",
            "Skeletal System",
            "Softening and bowing of leg bones in children caused by severe deficiency of Vitamin D or calcium",
            "Sunlight exposure for endogenous Vitamin D synthesis, fortified milk/dietary calcium",
            "rickets_etiology_confusion",
        ),
        (
            "Kidney Stones (Renal Calculi)",
            "Excretory System",
            "Hard mineral deposits of calcium oxalate or uric acid crystalizing in renal pelvis, obstructing urine flow",
            "Adequate daily water hydration and balanced dietary salt/oxalate intake",
            "kidney_stone_mechanism_error",
        ),
        (
            "Effects of Alcohol and Sedative Drugs on the Nervous System",
            "Nervous System",
            "Depresses central nervous system synaptic transmission, slows reaction times, impairs motor coordination, and blunts cognitive judgment",
            "Avoid alcohol/drug abuse, never drive under the influence of CNS depressants",
            "alcohol_stimulant_misconception",
        ),
    ]
    dis = disorders[actual_seed % len(disorders)]
    question_text = (
        f"Pathological disorders and lifestyle factors can severely impair human body systems.\n\n"
        f"1. Identify the body system primarily afflicted by **{dis[0]}**.\n"
        f"2. Describe the **biological cause and physiological manifestation** of this condition.\n"
        f"3. State **two lifestyle, dietary, or medical precautions** to prevent or manage this disorder."
    )
    sample = (
        f"1. **Affected System:** {dis[1]};\n"
        f"2. **Cause & Manifestation:** {dis[2]};\n"
        f"3. **Prevention / Management:** {dis[3]}."
    )
    marking = (
        f"• 1 mark: Correct organ system identified ({dis[1]}) [1]\n"
        f"• 2 marks: Biological explanation of cause and manifestation ({dis[2]}) [2]\n"
        f"• 1 mark: Preventive/therapeutic lifestyle measures ({dis[3]}) [1]\n"
        "**Total: 4 marks**"
    )
    return {
        "title": f"System Pathology: {dis[0]}",
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
            f"Think about which organs are damaged by {dis[0]}.",
            f"What nutrient deficiency or substance abuse triggers {dis[0]}?",
            f"System: {dis[1]}. Manifestation: {dis[2]}. Prevention: {dis[3]}.",
        ],
        "misconception_tags": [dis[4], "lifestyle_disease_etiology_error"],
        "learning_objective_id": "NS9.LL.02.05",
    }
