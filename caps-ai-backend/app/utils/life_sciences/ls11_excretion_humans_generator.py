"""Life Sciences Grade 11 Term 3: Excretion in Humans Topic Generator.

Fully grounded in:
- curriculum_docs_auto/LifeSciences_Gr11/Term 3/02. Excretion in humans.md
- curriculum_docs/LifeSciences_Gr11/Term 3/Excretion_in_humans.md

Subskills:
1. nephron_microstructure_anatomy: Microscopic renal nephron and Malpighian body (diagram questions).
2. excretory_organs_and_kidney_anatomy: Excretory organs and gross coronal kidney anatomy.
3. ultrafiltration_mechanisms: Glomerular hydrostatic pressure, podocytes, glomerular filtrate.
4. tubular_reabsorption_secretion: PCT active reabsorption, Loop of Henle, DCT tubular secretion.
5. osmoregulation_and_adh_homeostasis: Hypothalamic osmoreceptors, posterior pituitary ADH, negative feedback.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.organ_diagram_builders import build_nephron_question


SUBSKILLS = [
    "nephron_microstructure_anatomy",
    "excretory_organs_and_kidney_anatomy",
    "ultrafiltration_mechanisms",
    "tubular_reabsorption_secretion",
    "osmoregulation_and_adh_homeostasis",
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

    if chosen_subskill in ("nephron_microstructure_anatomy", "human_nephron", "diagram", "nephron", "anatomy"):
        return build_nephron_question(actual_seed, grade=11, mode=mode, subskill=chosen_subskill)

    subskills_pool = [
        "excretory_organs_and_kidney_anatomy",
        "ultrafiltration_mechanisms",
        "tubular_reabsorption_secretion",
        "osmoregulation_and_adh_homeostasis",
    ]
    if chosen_subskill not in subskills_pool:
        chosen_subskill = subskills_pool[actual_seed % len(subskills_pool)]

    if chosen_subskill == "excretory_organs_and_kidney_anatomy":
        scenarios = [
            (
                "Why is the physiological process of **egestion (defecation)** distinctly separated from **excretion** in biological science?",
                "Egestion is the expulsion of undigested, unabsorbed food residue from the gut, whereas excretion is the removal of metabolic waste products produced inside cellular reactions",
                [
                    "Egestion removes nitrogenous urea, whereas excretion only eliminates excess carbon dioxide",
                    "Egestion occurs exclusively in the kidneys, whereas excretion occurs exclusively in the lungs",
                    "Egestion requires active ATP transport across podocytes, whereas excretion is purely passive",
                ],
                "Excretion strictly refers to removing wastes of cellular metabolism (urea, uric acid, CO2, bile pigments); egestion removes non-metabolic dietary fiber and intestinal waste.",
            ),
            (
                "In a macroscopic longitudinal cross-section of the human kidney, where are the renal **Malpighian bodies (Bowman's capsules and glomeruli)** situated?",
                "Exclusively in the outer Renal Cortex",
                [
                    "Deep within the central Renal Pelvis",
                    "Exclusively inside the conical Renal Pyramids of the Medulla",
                    "Inside the muscular walls of the Ureter",
                ],
                "The outer renal cortex houses all Malpighian bodies, proximal convoluted tubules, and distal convoluted tubules, giving it a granular appearance.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ls11_excretion_organs_anatomy",
            q[0],
            q[1],
            q[2],
            q[3],
            "excretion_vs_egestion_confusion",
        )

    elif chosen_subskill == "ultrafiltration_mechanisms":
        scenarios = [
            (
                "What structural hemodynamic factor generates the high **hydrostatic blood pressure** inside the glomerulus necessary for non-selective ultrafiltration?",
                "The afferent arteriole entering the glomerulus has a significantly wider diameter than the efferent arteriole leaving it",
                [
                    "The efferent arteriole is connected directly to the high-pressure abdominal aorta",
                    "Rhythmic peristalsis of the Bowman's capsule pumps blood through the capillaries",
                    "The renal vein possesses one-way venous pocket valves that double blood velocity",
                ],
                "Because blood enters through a wider afferent arteriole and exits through a narrower efferent arteriole, resistance increases, creating elevated glomerular hydrostatic pressure.",
            ),
            (
                "Which component of normal blood plasma is **prevented** from passing into the Bowman's capsule during glomerular ultrafiltration under healthy conditions?",
                "Large plasma proteins (e.g. albumin, fibrinogen) and blood cells (erythrocytes, leukocytes)",
                [
                    "Urea and uric acid",
                    "Glucose and amino acids",
                    "Sodium, potassium, and chloride ions",
                ],
                "The basement membrane and podocyte filtration slits act as physical molecular sieves, blocking cells and large plasma proteins; their presence in urine indicates renal glomerulus damage.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ls11_excretion_ultrafiltration",
            q[0],
            q[1],
            q[2],
            q[3],
            "glomerular_filtration_diameter_inversion",
        )

    elif chosen_subskill == "tubular_reabsorption_secretion":
        scenarios = [
            (
                "Under healthy physiological conditions, what percentage of **glucose and amino acids** present in the glomerular filtrate is reabsorbed in the Proximal Convoluted Tubule (PCT)?",
                "100% (completely reabsorbed via active carrier transport against concentration gradients)",
                [
                    "~50% (the remainder is excreted to sweeten urine)",
                    "0% (glucose cannot cross tubular epithelial membranes)",
                    "Only absorbed if insulin binds to the collecting duct aquaporins",
                ],
                "Healthy kidneys reabsorb 100% of filtered glucose and amino acids in the PCT; glucose appearing in urine (glycosuria) is a classic indicator of diabetes mellitus.",
            ),
            (
                "What is the primary physiological function of the hairpin-shaped **Loop of Henle** extending down into the renal medulla?",
                "Establishes a high osmotic solute gradient in the interstitial fluid of the medulla, enabling water conservation",
                [
                    "Synthesizes erythropoietin to stimulate red blood cell production in bone marrow",
                    "Excretes solid cholesterol stones directly into the bladder",
                    "Filters uncoagulated fibrinogen out of the renal pelvis",
                ],
                "The countercurrent multiplier system of the Loop of Henle creates a hypertonic medullary gradient that draws water out of the collecting duct by osmosis.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ls11_excretion_reabsorption",
            q[0],
            q[1],
            q[2],
            q[3],
            "pct_complete_glucose_reabsorption_misconception",
        )

    else:  # osmoregulation_and_adh_homeostasis
        scenarios = [
            (
                "When a person is dehydrated on a hot day, blood plasma becomes hypertonic (low water potential). What hormonal homeostatic corrective response occurs?",
                "Hypothalamus osmoreceptors stimulate the posterior pituitary gland to secrete more ADH (antidiuretic hormone), making collecting duct walls more permeable to water, producing concentrated urine",
                [
                    "Anterior pituitary secretes glucagon, which pumps water into the bladder",
                    "Adrenal cortex stops secreting aldosterone, causing massive water loss in urine",
                    "Thyroid gland secretes thyroxine, diluting blood plasma with cellular fluid",
                ],
                "ADH increases aquaporin water channels in distal tubules and collecting ducts, maximizing water reabsorption back into blood capillaries and conserving body fluid.",
            ),
            (
                "If a person consumes large volumes of pure water on a cold day, what is the resulting negative feedback adjustment?",
                "Pituitary gland secretes less ADH; collecting ducts become less permeable to water; less water is reabsorbed, resulting in large volumes of dilute urine",
                [
                    "Pituitary secretes excess ADH; collecting ducts absorb all water, stopping urination completely",
                    "Liver secretes excess bile to neutralize dilute blood",
                    "Kidney podocytes close completely, halting glomerular filtration",
                ],
                "In overhydration, low ADH secretion reduces collecting duct permeability, allowing excess water to pass into urine, maintaining normal blood osmolality.",
            ),
        ]
        q = r.choice(scenarios)
        return _format_mcq(
            actual_seed,
            "ls11_excretion_adh_osmoregulation",
            q[0],
            q[1],
            q[2],
            q[3],
            "adh_secretion_hydration_inversion",
        )


def _format_mcq(
    seed: int,
    lo_id: str,
    prompt: str,
    correct: str,
    distractors: List[str],
    explanation: str,
    misconception: str,
) -> Dict[str, Any]:
    options = [correct] + distractors
    random.Random(seed).shuffle(options)
    return {
        "id": f"{lo_id}_{seed}",
        "term": 3,
        "caps_weight_percent": 16,
        "suggested_duration_mins": 3,
        "learning_objective_id": lo_id,
        "misconception_tags": [misconception],
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct,
        "hints": [
            "Review the functional processes of excretion and osmoregulation in the human kidney.",
            f"Key physiological rule: {explanation[:80]}...",
            f"The correct biological answer is: {correct}.",
        ],
        "worked_solution": f"Correct Answer: {correct}. Explanation: {explanation}",
    }
