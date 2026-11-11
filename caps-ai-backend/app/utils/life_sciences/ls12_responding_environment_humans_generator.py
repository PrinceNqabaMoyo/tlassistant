"""Life Sciences Grade 12 Term 2: Human Responses to the Environment Generator.

Fully grounded in:
- curriculum_docs_auto/LifeSciences_Gr12/Term 2/01. Human responses to the environment.md

Subskills:
1. human_eye: Longitudinal anatomy, accommodation mechanism, pupillary reflex, optical defects.
2. human_ear: Coronal anatomy, hearing transduction pathway, dynamic/static balance, ear defects.
3. reflex_arc: Stimulus, sensory neuron, synapse/interneuron in spinal cord, motor neuron, effector.
4. cns_and_pns: Brain anatomy (cerebrum, cerebellum, medulla oblongata), autonomic vs somatic divisions.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.sensory_reproductive_builders import (
    build_eye_question,
    build_ear_question,
)


SUBSKILLS = [
    "human_eye",
    "human_ear",
    "reflex_arc",
    "brain_functions",
    "nervous_divisions",
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

    # Check for direct diagram or sensory modality
    if chosen_subskill in ("human_eye", "eye", "human_eye_structure", "eye_anatomy", "accommodation", "pupillary_reflex", "eye_defects"):
        sub = None if chosen_subskill in ("human_eye", "eye", "human_eye_structure", "eye_anatomy") else chosen_subskill
        return build_eye_question(actual_seed, grade=12, mode=mode, subskill=sub)

    if chosen_subskill in ("human_ear", "ear", "human_ear_structure", "ear_anatomy", "hearing_pathway", "balance_mechanism", "ear_defects"):
        sub = None if chosen_subskill in ("human_ear", "ear", "human_ear_structure", "ear_anatomy") else chosen_subskill
        return build_ear_question(actual_seed, grade=12, mode=mode, subskill=sub)

    # Conceptual Subskills: reflex_arc, brain_functions, nervous_divisions
    subskills_pool = ["reflex_arc", "brain_functions", "nervous_divisions"]
    if chosen_subskill not in subskills_pool:
        chosen_subskill = subskills_pool[actual_seed % len(subskills_pool)]

    if chosen_subskill == "reflex_arc":
        scenarios = [
            (
                "A person accidentally steps barefoot on a sharp drawing pin and instantly jerks their foot away. "
                "Which option correctly traces the physiological reflex arc from receptor to effector?",
                "Receptor in skin → Sensory neuron → Interneuron (in grey matter of spinal cord) → Motor neuron → Effector muscle",
                [
                    "Receptor in skin → Motor neuron → Spinal cord → Sensory neuron → Brain",
                    "Sensory neuron → Brain (cerebrum) → Effector muscle → Interneuron",
                    "Receptor → Effector muscle → Sensory neuron → Motor neuron → Spinal cord",
                ],
                "A reflex arc is an automatic, involuntary response that bypasses conscious brain processing to prevent injury.",
                ["reflex_arc_pathway_inversion", "sensory_motor_neuron_confusion"],
            ),
            (
                "What is the evolutionary and physiological significance of a reflex arc being coordinated "
                "at the level of the spinal cord without requiring prior conscious processing by the brain?",
                "It drastically shortens response latency to prevent or minimize severe tissue trauma",
                [
                    "It prevents neurotransmitters from exhausting cerebral ATP stores",
                    "It allows motor neurons to regenerate myelin sheaths faster",
                    "It bypasses the autonomic nervous system to stimulate smooth muscles directly",
                ],
                "Speed of response is paramount in avoiding severe physical damage from noxious stimuli.",
                ["reflex_function_misunderstanding", "spinal_cord_significance_error"],
            ),
        ]
    elif chosen_subskill == "brain_functions":
        scenarios = [
            (
                "A cyclist suffers a traumatic head injury and subsequently displays loss of voluntary muscular coordination, "
                "stumbling gait, and inability to judge balance. Which part of the brain has most likely sustained damage?",
                "Cerebellum",
                [
                    "Cerebrum",
                    "Medulla oblongata",
                    "Corpus callosum",
                ],
                "The cerebellum coordinates voluntary muscular movements and maintains balance and muscle tone.",
                ["cerebellum_vs_cerebrum_confusion", "brain_region_localization_error"],
            ),
            (
                "Which part of the human brain contains vital autonomic reflex centers that regulate heart rate, "
                "blood pressure, breathing rhythm, and peristalsis?",
                "Medulla oblongata",
                [
                    "Hypothalamus",
                    "Cerebellum",
                    "Cerebrum",
                ],
                "The medulla oblongata controls involuntary vital autonomic functions essential for life.",
                ["medulla_oblongata_function_confusion", "autonomic_center_misidentification"],
            ),
        ]
    else:  # nervous_divisions
        scenarios = [
            (
                "During a sudden encounter with a dangerous animal, the body undergoes a rapid 'fight-or-flight' reaction. "
                "Which division of the autonomic nervous system mediates pupillary dilation, bronchiolar dilation, "
                "and acceleration of heartbeat?",
                "Sympathetic nervous system",
                [
                    "Parasympathetic nervous system",
                    "Somatic sensory system",
                    "Central motor cortex",
                ],
                "The sympathetic nervous system prepares the body for emergency energy expenditure (fight or flight).",
                ["sympathetic_vs_parasympathetic_inversion", "autonomic_division_confusion"],
            ),
            (
                "Following the resolution of a stressful crisis, which division of the autonomic nervous system acts "
                "to decelerate heart rate, constrict pupils, and stimulate digestive glandular secretions ('rest and digest')?",
                "Parasympathetic nervous system",
                [
                    "Sympathetic nervous system",
                    "Somatic nervous system",
                    "Peripheral spinal plexus",
                ],
                "The parasympathetic system promotes energy conservation and restores homeostatic resting states.",
                ["parasympathetic_action_misconception", "autonomic_antagonism_error"],
            ),
        ]

    prompt, correct_ans, distractors, explanation, tags = r.choice(scenarios)
    options = [correct_ans] + distractors
    r.shuffle(options)

    return {
        "id": f"ls12_env_{actual_seed}_{chosen_subskill}",
        "archetype": "human_responses_environment",
        "topic": "Human responses to the environment",
        "subject": "Life Sciences",
        "grade": 12,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 3,
        "subskill": chosen_subskill,
        "question_text": prompt,
        "correct_answer": correct_ans,
        "options": options,
        "misconception_tags": tags,
        "hints": [
            "Consider whether this physiological response is voluntary or autonomic.",
            explanation,
            f"The correct answer is: {correct_ans}.",
        ],
        "solution_steps": [
            "Step 1: Analyze the physiological stimulus and neural structures involved.",
            f"Step 2: Recall curriculum principle: {explanation}",
            f"Step 3: Confirm correct response: {correct_ans}.",
        ],
    }
