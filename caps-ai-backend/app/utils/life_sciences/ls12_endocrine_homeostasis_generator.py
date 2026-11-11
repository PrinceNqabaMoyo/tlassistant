"""Life Sciences Grade 12 Term 2: Endocrine System & Homeostasis Generator.

Fully grounded in:
- curriculum_docs_auto/LifeSciences_Gr12/Term 2/04. The human endocrine system and homeostasis.md

Subskills:
1. endocrine_system_map: Anatomical location of major glands, target organs, and primary secretions.
2. glucose_homeostasis: Antagonistic control by insulin (beta cells) and glucagon (alpha cells).
3. thyroxine_feedback: Negative feedback loop between TSH (pituitary) and thyroxine (thyroid).
4. osmoregulation: Water balance mediated by ADH (hypothalamus/posterior pituitary) on renal tubules.
5. thermoregulation: Sweating, vasodilation, and vasoconstriction in response to ambient temperature.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.sensory_reproductive_builders import build_endocrine_question


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "compound",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    # Check for direct diagram or glandular subskill
    if subskill in ("endocrine_system", "endocrine_glands", "human_endocrine_system", "endocrine_system_map", "gland_identification", "glucose_homeostasis", "thyroxine_feedback", "osmoregulation_adh"):
        sub = None if subskill in ("endocrine_system", "endocrine_glands", "human_endocrine_system", "endocrine_system_map") else subskill
        return build_endocrine_question(actual_seed, grade=12, mode=mode, subskill=sub)

    # Deterministic 5-subskill progression across topic subskills
    ALL_SUBSKILLS = [
        "endocrine_system_map",
        "glucose_homeostasis",
        "osmoregulation_adh",
        "thermoregulation",
        "diabetes_mellitus",
        "general_negative_feedback",
    ]
    chosen_subskill = subskill if subskill in ALL_SUBSKILLS else ALL_SUBSKILLS[actual_seed % len(ALL_SUBSKILLS)]

    if chosen_subskill in ("endocrine_system_map", "glucose_homeostasis", "osmoregulation_adh"):
        sub = None if chosen_subskill == "endocrine_system_map" else chosen_subskill
        return build_endocrine_question(actual_seed, grade=12, mode=mode, subskill=sub)

    if chosen_subskill == "thermoregulation":
        temp_state = r.choice(["hot", "cold"])
        if temp_state == "hot":
            prompt = (
                "When ambient environmental temperature rises on a hot summer day, which physiological changes "
                "occur in the skin to increase radiant heat loss and maintain body core temperature at ~37°C?"
            )
            correct_ans = "Arterioles vasodilate to increase dermal blood flow, and sweat glands secrete sweat for evaporative cooling"
            distractors = [
                "Arterioles vasoconstrict to divert blood to deep organs, and erector muscles contract",
                "Sweat glands stop secreting sweat, and skeletal muscles undergo involuntary shivering",
                "Arterioles constrict completely, and thyroxine secretion increases basal metabolism",
            ]
            explanation = "Vasodilation increases blood flow near the skin surface to radiate heat, while sweat evaporation absorbs latent heat."
            tags = ["vasodilation_vasoconstriction_inversion", "thermoregulation_cooling_error"]
        else:
            prompt = (
                "When exposed to severe freezing temperatures, how does the body minimise heat loss through the skin?"
            )
            correct_ans = "Arterioles vasoconstrict to reduce blood flow near skin surface, and erector pili muscles contract to trap an insulating air layer"
            distractors = [
                "Arterioles vasodilate to flood skin capillaries with warm blood, and sweat glands dilate",
                "Sweat secretion increases rapidly to form an insulating fluid film over the epidermis",
                "Arterioles remain dilated while metabolic rate drops to zero to prevent caloric loss",
            ]
            explanation = "Vasoconstriction keeps warm blood routed into deep core organs, minimizing convective and radiant heat loss."
            tags = ["vasoconstriction_misunderstanding", "heat_conservation_inversion"]
    elif chosen_subskill == "diabetes_mellitus":
        scenarios_dm = [
            (
                "A person with untreated Type 1 Diabetes Mellitus experiences persistent thirst, frequent urination, "
                "and glucose in their urine (glucosuria). What is the underlying endocrine failure in this condition?",
                "Autoimmune destruction of pancreatic beta cells resulting in absolute deficiency of insulin",
                [
                    "Hypersecretion of glucagon by alpha cells leading to complete exhaustion of liver glycogen",
                    "Inability of kidney collecting ducts to reabsorb ADH from the blood",
                    "Hyperactive thyroid gland overproducing thyroxine that converts all fat into glucose",
                ],
                "Type 1 diabetes is characterized by lack of insulin secretion from beta cells, leaving glucose stranded in the blood.",
                ["diabetes_type1_etiology_error", "insulin_deficiency_confusion"],
            ),
            (
                "How does the underlying cellular pathophysiology of **Type 2 Diabetes Mellitus** differ from Type 1 Diabetes?",
                "Pancreatic beta cells produce insulin, but target body cells show reduced insulin receptor sensitivity (insulin resistance)",
                [
                    "Target cells absorb all insulin and convert it immediately into glucagon",
                    "Beta cells are completely destroyed at birth so no insulin is ever synthesized",
                    "The liver converts excess glucose into glucagon rather than glycogen",
                ],
                "Type 2 diabetes typically features insulin resistance where target cells fail to respond to circulating insulin.",
                ["type2_insulin_resistance_misunderstanding", "diabetes_type1_vs_type2_confusion"],
            ),
            (
                "Why do untreated diabetes mellitus patients frequently suffer from extreme thirst (polydipsia) and excessive urination (polyuria)?",
                "High blood glucose exceeds renal reabsorption threshold, causing osmotic diuresis that draws water into urine",
                [
                    "Glucose permanently blocks the synthesis of aldosterone in the adrenal cortex",
                    "Insulin breaks down all water molecules inside kidney glomeruli",
                    "Excess glucagon stimulates the hypothalamus to dump water into the urinary bladder",
                ],
                "Unreabsorbed glucose in the kidney tubules exerts an osmotic pull, preventing water reabsorption and causing dehydration.",
                ["osmotic_diuresis_misunderstanding", "glucosuria_mechanism_error"],
            ),
        ]
        prompt, correct_ans, distractors, explanation, tags = r.choice(scenarios_dm)
    else:  # general_negative_feedback
        scenarios_nf = [
            (
                "What fundamental characteristic distinguishes a **negative feedback control system** "
                "in human homeostatic regulation from positive feedback?",
                "The effector's response opposes and reverses the original deviation from the homeostatic set point",
                [
                    "The effector accelerates and amplifies the original deviation to reach an extreme state",
                    "Hormones are eliminated from circulation without producing any cellular changes",
                    "Nervous impulses permanently suppress endocrine glandular secretions",
                ],
                "Negative feedback detects a deviation from a setpoint and initiates corrective actions to reverse that change.",
                ["negative_vs_positive_feedback_inversion", "homeostasis_setpoint_misconception"],
            ),
            (
                "In the negative feedback regulation of **thyroxine**, what corrective action occurs when blood thyroxine concentration rises above the normal homeostatic set point?",
                "The pituitary gland decreases secretion of TSH, reducing thyroid gland stimulation and lowering thyroxine release",
                [
                    "The pituitary increases TSH secretion to rapidly burn off the excess thyroxine",
                    "The thyroid gland secretes insulin to break down thyroxine molecules",
                    "The hypothalamus permanently shuts down all blood supply to the thyroid gland",
                ],
                "High thyroxine levels exert negative feedback on the anterior pituitary (and hypothalamus) to decrease TSH secretion.",
                ["thyroxine_tsh_feedback_inversion", "pituitary_negative_feedback_error"],
            ),
            (
                "When blood carbon dioxide ($CO_2$) concentration rises during strenuous exercise, how does negative feedback restore normal blood pH?",
                "Chemoreceptors signal the respiratory centre in the medulla oblongata to increase breathing rate and depth, expelling excess CO2",
                [
                    "The pancreas secretes glucagon to neutralize carbonic acid in the bloodstream",
                    "The lungs slow down breathing to conserve carbon dioxide in muscle tissues",
                    "The kidneys instantly halt all filtration to trap acid in the urinary bladder",
                ],
                "Elevated CO2 forms carbonic acid; the medulla oblongata stimulates hyperventilation to restore homeostatic acid-base balance.",
                ["carbon_dioxide_chemoreceptor_error", "respiratory_homeostasis_misconception"],
            ),
        ]
        prompt, correct_ans, distractors, explanation, tags = r.choice(scenarios_nf)

    options = [correct_ans] + distractors
    r.shuffle(options)

    return {
        "id": f"ls12_endo_{actual_seed}_{chosen_subskill}",
        "archetype": "endocrine_homeostasis",
        "topic": "The human endocrine system and homeostasis",
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
            "Homeostasis operates to keep the internal environment constant within narrow physiological limits.",
            explanation,
            f"The correct answer is: {correct_ans}.",
        ],
        "solution_steps": [
            "Step 1: Identify the homeostatic parameter (temperature, glucose, water).",
            f"Step 2: Recall regulatory feedback mechanism: {explanation}",
            f"Step 3: Confirm correct response: {correct_ans}.",
        ],
    }
