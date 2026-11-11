"""Organ Diagram Subskill Builders for Natural Sciences & Life Sciences.

Provides deterministic, 3-layer subskill builders for:
1. Alveolus Gas Exchange (alveolus_gas_exchange)
2. Human Digestive System (digestive_system)
3. Intestinal Villus Anatomy (intestinal_villus)
4. Human Nephron Ultrastructure (human_nephron)

Implements:
- 6-pillar contract (term, caps_weight_percent, duration, misconception_tags, 3-tier hints).
- Anti-leak security: client receives opaque randomized `ref` tokens; zero structure names in DOM.
- Progressive depth staging (Grade 9 macroscopic vs Grade 11 microscopic/biochemical mechanisms).
- Single locked view mode in question cards.
"""

from __future__ import annotations

import json
import os
import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

ANCHORS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "data",
    "diagram_anchors",
)


def _load_anchors(master_name: str) -> Dict[str, Any]:
    path = os.path.join(ANCHORS_DIR, f"{master_name}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


ALVEOLUS_DATA = _load_anchors("alveolus_gas_exchange")
DIGESTIVE_DATA = _load_anchors("digestive_system")
VILLUS_DATA = _load_anchors("intestinal_villus")
NEPHRON_DATA = _load_anchors("human_nephron")


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_organ_salt"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


# ============================================================================
# 1. ALVEOLUS GAS EXCHANGE
# ============================================================================

def build_alveolus_question(
    seed: int,
    grade: int = 11,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = ALVEOLUS_DATA["anchors"]
    grade_str = f"g{grade}"
    allowed_keys = [k for k, v in anchors.items() if grade_str in v.get("grades", ["g9", "g11"])]

    target_key = r.choice(allowed_keys)
    target = anchors[target_key]

    # Generate 4 pins (1 target + 3 distractors)
    other_keys = [k for k in allowed_keys if k != target_key]
    r.shuffle(other_keys)
    selected_keys = [target_key] + other_keys[:3]
    r.shuffle(selected_keys)

    pin_letters = ["A", "B", "C", "D"]
    pins_payload = []
    target_pin = "A"

    for idx, k in enumerate(selected_keys):
        letter = pin_letters[idx]
        ref = _make_ref(seed, k, idx)
        pins_payload.append({
            "pin": letter,
            "anchor": anchors[k]["anchor"],
            "default_box": anchors[k]["default_box"],
            "side": anchors[k]["side"],
            "ref": ref,
        })
        if k == target_key:
            target_pin = letter

    if grade >= 11:
        correct_ans = f"{target['name']} — {target['description']}"
        distractor_names = [f"{anchors[k]['name']} — {anchors[k]['description']}" for k in other_keys[:3]]
        options = [correct_ans] + distractor_names
        r.shuffle(options)
        prompt = (
            f"Study the microscopic cross-section of the pulmonary alveolus and adjacent capillary. "
            f"Identify the histological structure indicated by **Pin {target_pin}** and explain its adaptation for rapid gaseous exchange."
        )
        marks = 3
    else:
        correct_ans = target["name"]
        distractor_names = [anchors[k]["name"] for k in other_keys[:3]]
        options = [correct_ans] + distractor_names
        r.shuffle(options)
        prompt = (
            f"Look at the diagram showing gas exchange in the human lungs. "
            f"Identify the part labelled by **Pin {target_pin}**."
        )
        marks = 2

    hints = [
        f"Pin {target_pin} is located on the {target['side']} side of the diffusion interface.",
        f"This structure plays a vital role in {target['description']}",
        f"The correct biological structure indicated by Pin {target_pin} is {target['name']}.",
    ]
    sol_str = f"Pin {target_pin} points to {target['name']}. {target['description']}"

    return {
        "id": f"alveolus_{seed}_{target_key}",
        "term": 3 if grade == 11 else 1,
        "caps_weight_percent": 12,
        "suggested_duration_mins": 3,
        "learning_objective_id": f"ls{grade}_gaseous_exchange_alveolus",
        "misconception_tags": [
            "erythrocyte_endothelium_confusion",
            "diffusion_gradient_direction_error",
            "alveolar_capillary_membrane_thickness",
        ],
        "modality": "bio_diagram",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "sample_answer": sol_str,
        "target_pin": target_pin,
        "target_key": target_key,
        "synonyms": target["synonyms"],
        "hints": hints,
        "marks": marks,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Identification of Pin {target_pin}: {target['name']}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Histological adaptation / function: {target['description']}", "marks": marks - 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "worked_solution": sol_str,
        "diagram_spec": {
            "diagram_role": "identify" if locals().get("target_pin") else "context",
            "image_type": "alveolus_gas_exchange",
            "view": "microscopic_diffusion_section",
            "viewBox": ALVEOLUS_DATA["viewBox"],
            "grade_mask": grade_str,
            "pins": pins_payload,
            "state": "static",
        },
    }


# ============================================================================
# 2. HUMAN DIGESTIVE SYSTEM
# ============================================================================

def build_digestive_question(
    seed: int,
    grade: int = 9,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = DIGESTIVE_DATA["anchors"]
    grade_str = f"g{grade}"
    allowed_keys = [k for k, v in anchors.items() if grade_str in v.get("grades", ["g9", "g11"])]

    target_key = r.choice(allowed_keys)
    target = anchors[target_key]

    other_keys = [k for k in allowed_keys if k != target_key]
    r.shuffle(other_keys)
    selected_keys = [target_key] + other_keys[:3]
    r.shuffle(selected_keys)

    pin_letters = ["A", "B", "C", "D"]
    pins_payload = []
    target_pin = "A"

    for idx, k in enumerate(selected_keys):
        letter = pin_letters[idx]
        ref = _make_ref(seed, k, idx)
        pins_payload.append({
            "pin": letter,
            "anchor": anchors[k]["anchor"],
            "default_box": anchors[k]["default_box"],
            "side": anchors[k]["side"],
            "ref": ref,
        })
        if k == target_key:
            target_pin = letter

    if grade >= 11:
        correct_ans = f"{target['name']} — {target['description']}"
        distractor_names = [f"{anchors[k]['name']} — {anchors[k]['description']}" for k in other_keys[:3]]
        options = [correct_ans] + distractor_names
        r.shuffle(options)
        prompt = (
            f"Refer to the coronal anatomical overview of the human alimentary canal and accessory glands. "
            f"Identify the organ designated by **Pin {target_pin}** and state its specific digestive or homeostatic function."
        )
        marks = 3
    else:
        correct_ans = target["name"]
        distractor_names = [anchors[k]["name"] for k in other_keys[:3]]
        options = [correct_ans] + distractor_names
        r.shuffle(options)
        prompt = (
            f"Refer to the human digestive system diagram. "
            f"Identify the organ marked by **Pin {target_pin}**."
        )
        marks = 2

    hints = [
        f"Pin {target_pin} is located on the {target['side']} side of the digestive tract.",
        f"Function clue: {target['description']}",
        f"The organ designated by Pin {target_pin} is the {target['name']}.",
    ]
    sol_str = f"Pin {target_pin} identifies the {target['name']}. {target['description']}"

    return {
        "id": f"digestive_{seed}_{target_key}",
        "term": 1 if grade == 9 else 2,
        "caps_weight_percent": 14,
        "suggested_duration_mins": 3,
        "learning_objective_id": f"ns{grade}_digestive_system_organs",
        "misconception_tags": [
            "liver_pancreas_inversion",
            "peristalsis_site_confusion",
            "digestion_vs_absorption_organ",
        ],
        "modality": "bio_diagram",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "sample_answer": sol_str,
        "target_pin": target_pin,
        "target_key": target_key,
        "synonyms": target["synonyms"],
        "hints": hints,
        "marks": marks,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Identification of Pin {target_pin}: {target['name']}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Digestive / enzymatic role: {target['description']}", "marks": marks - 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "worked_solution": sol_str,
        "diagram_spec": {
            "diagram_role": "identify" if locals().get("target_pin") else "context",
            "image_type": "human_digestive_system",
            "view": "coronal_alimentary_canal",
            "viewBox": DIGESTIVE_DATA["viewBox"],
            "grade_mask": grade_str,
            "pins": pins_payload,
            "state": "static",
        },
    }


# ============================================================================
# 3. INTESTINAL VILLUS ANATOMY
# ============================================================================

def build_villus_question(
    seed: int,
    grade: int = 11,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = VILLUS_DATA["anchors"]
    allowed_keys = list(anchors.keys())

    target_key = r.choice(allowed_keys)
    target = anchors[target_key]

    other_keys = [k for k in allowed_keys if k != target_key]
    r.shuffle(other_keys)
    selected_keys = [target_key] + other_keys[:3]
    r.shuffle(selected_keys)

    pin_letters = ["A", "B", "C", "D"]
    pins_payload = []
    target_pin = "A"

    for idx, k in enumerate(selected_keys):
        letter = pin_letters[idx]
        ref = _make_ref(seed, k, idx)
        pins_payload.append({
            "pin": letter,
            "anchor": anchors[k]["anchor"],
            "default_box": anchors[k]["default_box"],
            "side": anchors[k]["side"],
            "ref": ref,
        })
        if k == target_key:
            target_pin = letter

    correct_ans = f"{target['name']} — {target['description']}"
    distractor_names = [f"{anchors[k]['name']} — {anchors[k]['description']}" for k in other_keys[:3]]
    options = [correct_ans] + distractor_names
    r.shuffle(options)

    prompt = (
        f"Study the longitudinal cross-section of an intestinal villus from the small intestine (ileum). "
        f"Identify the histological component labelled by **Pin {target_pin}** and explain how it facilitates nutrient absorption."
    )

    hints = [
        f"Pin {target_pin} is located on the {target['side']} side of the villus cross-section.",
        f"Structural adaptation: {target['description']}",
        f"The correct anatomical structure is {target['name']}.",
    ]
    sol_str = f"Pin {target_pin} indicates the {target['name']}. {target['description']}"

    return {
        "id": f"villus_{seed}_{target_key}",
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "learning_objective_id": "ls11_animal_nutrition_villus_absorption",
        "misconception_tags": [
            "lacteal_vs_blood_capillary_absorption",
            "goblet_cell_mucus_function",
            "microvilli_vs_villi_scale_confusion",
        ],
        "modality": "bio_diagram",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "sample_answer": sol_str,
        "target_pin": target_pin,
        "target_key": target_key,
        "synonyms": target["synonyms"],
        "hints": hints,
        "marks": 3,
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Identification of Pin {target_pin}: {target['name']}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Absorption adaptation: {target['description']}", "marks": 2, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "worked_solution": sol_str,
        "diagram_spec": {
            "diagram_role": "identify" if locals().get("target_pin") else "context",
            "image_type": "intestinal_villus",
            "view": "longitudinal_cross_section",
            "viewBox": VILLUS_DATA["viewBox"],
            "grade_mask": "g11",
            "pins": pins_payload,
            "state": "static",
        },
    }


# ============================================================================
# 4. HUMAN NEPHRON ULTRASTRUCTURE
# ============================================================================

def build_nephron_question(
    seed: int,
    grade: int = 11,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = NEPHRON_DATA["anchors"]
    grade_str = f"g{grade}"
    allowed_keys = [k for k, v in anchors.items() if grade_str in v.get("grades", ["g9", "g11"])]
    if not allowed_keys:
        allowed_keys = list(anchors.keys())

    target_key = r.choice(allowed_keys)
    target = anchors[target_key]

    other_keys = [k for k in allowed_keys if k != target_key]
    r.shuffle(other_keys)
    selected_keys = [target_key] + other_keys[:3]
    r.shuffle(selected_keys)

    pin_letters = ["A", "B", "C", "D"]
    pins_payload = []
    target_pin = "A"

    for idx, k in enumerate(selected_keys):
        letter = pin_letters[idx]
        ref = _make_ref(seed, k, idx)
        pins_payload.append({
            "pin": letter,
            "anchor": anchors[k]["anchor"],
            "default_box": anchors[k]["default_box"],
            "side": anchors[k]["side"],
            "ref": ref,
        })
        if k == target_key:
            target_pin = letter

    if grade >= 11:
        correct_ans = f"{target['name']} — {target['description']}"
        distractor_names = [f"{anchors[k]['name']} — {anchors[k]['description']}" for k in other_keys[:3]]
        options = [correct_ans] + distractor_names
        r.shuffle(options)
        prompt = (
            f"Examine the functional schematic of a microscopic renal nephron and associated vascular knot. "
            f"Identify the region labelled by **Pin {target_pin}** and describe the specific physiological process (ultrafiltration, selective reabsorption, or osmoregulation) occurring there."
        )
        marks = 3
    else:
        correct_ans = target["name"]
        distractor_names = [anchors[k]["name"] for k in other_keys[:3]]
        options = [correct_ans] + distractor_names
        r.shuffle(options)
        prompt = (
            f"Refer to the diagram of a kidney nephron (filtration unit of the excretory system). "
            f"Identify the part labelled by **Pin {target_pin}**."
        )
        marks = 2

    hints = [
        f"Pin {target_pin} is situated on the {target['side']} side of the nephron schematic.",
        f"Renal process: {target['description']}",
        f"The indicated nephron region is {target['name']}.",
    ]
    sol_str = f"Pin {target_pin} corresponds to {target['name']}. {target['description']}"

    return {
        "id": f"nephron_{seed}_{target_key}",
        "term": 3 if grade >= 11 else 1,
        "caps_weight_percent": 16,
        "suggested_duration_mins": 3,
        "learning_objective_id": f"ls{grade}_excretion_nephron_filtration",
        "misconception_tags": [
            "afferent_efferent_lumen_confusion",
            "ultrafiltration_vs_reabsorption_site",
            "pct_vs_dct_hormonal_sensitivity",
        ],
        "modality": "bio_diagram",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_ans,
        "sample_answer": sol_str,
        "target_pin": target_pin,
        "target_key": target_key,
        "synonyms": target["synonyms"],
        "hints": hints,
        "marks": marks,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Identification of Pin {target_pin}: {target['name']}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Renal mechanism: {target['description']}", "marks": marks - 1, "editable": True},
            ],
            "carry_forward_rule": "consequential_accuracy",
        },
        "worked_solution": sol_str,
        "diagram_spec": {
            "diagram_role": "identify" if locals().get("target_pin") else "context",
            "image_type": "human_nephron",
            "view": "renal_microstructure_section",
            "viewBox": NEPHRON_DATA["viewBox"],
            "grade_mask": grade_str,
            "pins": pins_payload,
            "state": "static",
        },
    }
