"""Plant Anatomy & Physiology Diagram Subskill Builders.

Provides deterministic, 3-layer subskill builders for:
1. Dicotyledonous Leaf Transverse Section (plant_leaf)

Implements:
- 6-pillar contract (term, caps_weight_percent, duration, misconception_tags, 3-tier hints).
- Anti-leak security: client receives opaque randomized `ref` tokens; zero structure names in DOM.
- Multi-grade support (Grade 10 Support & Transport in Plants vs Grade 11 Photosynthesis & Bioenergetics).
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


PLANT_LEAF_DATA = _load_anchors("plant_leaf")


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_leaf_salt"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


# ============================================================================
# 1. PLANT LEAF BUILDER
# ============================================================================

def build_plant_leaf_question(
    seed: int,
    grade: int = 10,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = PLANT_LEAF_DATA["anchors"]
    grade_str = f"g{grade}"
    # Exclude empty-space anchors from Role L pin targets and distractors (Rule R8)
    empty_space_keys = {"intercellular_air_space", "sub_stomatal_cavity", "stomatal_pore"}
    allowed_keys = [
        k for k, v in anchors.items()
        if grade_str in v.get("grades", ["g10", "g11"]) and k not in empty_space_keys
    ]
    if len(allowed_keys) < 4:
        allowed_keys = [k for k in anchors.keys() if k not in empty_space_keys]

    if subskill is None:
        if grade >= 11:
            subskill = r.choice(["photosynthesis_adaptation", "stomatal_mechanism", "vascular_transport"])
        else:
            subskill = r.choice(["tissue_identification", "transpiration_adaptation", "vascular_transport", "stomatal_mechanism"])

    # Match target_key to subskill semantics so target_pin always points to a structure relevant to the prompt
    if subskill == "stomatal_mechanism":
        candidates = [k for k in ("guard_cells", "lower_epidermis") if k in allowed_keys]
        target_key = r.choice(candidates) if candidates else r.choice(allowed_keys)
    elif subskill == "vascular_transport":
        candidates = [k for k in ("xylem_vessels", "phloem_sieve_tubes") if k in allowed_keys]
        target_key = r.choice(candidates) if candidates else r.choice(allowed_keys)
    elif subskill == "transpiration_adaptation":
        candidates = [k for k in ("waxy_cuticle", "lower_epidermis", "guard_cells") if k in allowed_keys]
        target_key = r.choice(candidates) if candidates else r.choice(allowed_keys)
    elif subskill == "photosynthesis_adaptation":
        candidates = [k for k in ("palisade_mesophyll", "spongy_mesophyll", "upper_epidermis", "waxy_cuticle", "xylem_vessels") if k in allowed_keys]
        target_key = r.choice(candidates) if candidates else r.choice(allowed_keys)
    else:
        target_key = r.choice(allowed_keys)

    target = anchors[target_key]

    other_keys = [k for k in allowed_keys if k != target_key]
    r.shuffle(other_keys)
    distractor_keys = other_keys[:3]
    active_keys = [target_key] + distractor_keys
    r.shuffle(active_keys)

    pin_letters = ["A", "B", "C", "D"]
    client_pins: List[Dict[str, Any]] = []
    server_solution_map: Dict[str, str] = {}
    target_pin_letter = ""

    for idx, key in enumerate(active_keys):
        letter = pin_letters[idx]
        ref = _make_ref(seed, key, idx)
        if key == target_key:
            target_pin_letter = letter

        server_solution_map[letter] = anchors[key]["name"]
        client_pins.append({
            "pin": letter,
            "ref": ref,
            "anchor": anchors[key]["anchor"],
            "default_box": anchors[key]["default_box"],
            "side": anchors[key]["side"],
        })

    landmarks = [
        {
            "id": p["ref"],
            "label": f"Structure {p['pin']}",
            "x": p["anchor"][0],
            "y": p["anchor"][1],
        }
        for p in client_pins
    ]
    view_mode = "textbook"

    qid = f"ls{grade}_leaf_{seed}_{subskill[:4]}"
    options = None
    qtype = "diagram_short_answer"

    if subskill in ("tissue_identification", "plant_leaf", "plant_leaf_cross_section"):
        qtype = "mcq"
        if grade >= 11:
            prompt = (
                f"Study the transverse cross-section of the dicotyledonous leaf. "
                f"Identify the photosynthetic or vascular tissue indicated by **Pin {target_pin_letter}** and explain how its structural features adapt the leaf for efficient photosynthesis."
            )
            correct_ans = f"{target['name']} — {target['description']}"
            distractor_names = [f"{anchors[k]['name']} — {anchors[k]['description']}" for k in distractor_keys]
        else:
            prompt = (
                f"Study the transverse cross-section schematic of the dicotyledonous leaf. "
                f"Identify the tissue/structure indicated by **Pin {target_pin_letter}**."
            )
            correct_ans = target["name"]
            distractor_names = [anchors[k]["name"] for k in distractor_keys]
        options = [correct_ans] + distractor_names
        r.shuffle(options)
        memo = (
            f"Pin {target_pin_letter} indicates the **{target['name']}**. [1]\n"
            f"Function: {target['description']} [1]"
        )
        hints = {
            "tier_1": f"Observe whether Pin {target_pin_letter} points to the upper boundary, internal mesophyll, or vascular bundle.",
            "tier_2": f"Structure {target_pin_letter} is {target['name'].lower()}, characterized by its specific anatomical location.",
            "tier_3": f"The correct structure indicated by Pin {target_pin_letter} is {target['name']}.",
        }
        marks = 3 if grade >= 11 else 2
        misconceptions = ["confused_palisade_with_spongy", "xylem_phloem_inversion", "cuticle_epidermis_confusion"]

    elif subskill == "photosynthesis_adaptation":
        qtype = "mcq"
        prompt = (
            f"Refer to the transverse section of the dicotyledonous leaf. "
            f"Identify the leaf tissue indicated by **Pin {target_pin_letter}** and explain its structural adaptation for maximizing the rate of photosynthesis."
        )
        correct_ans = f"{target['name']} — {target['description']}"
        distractor_names = [f"{anchors[k]['name']} — {anchors[k]['description']}" for k in distractor_keys]
        options = [correct_ans] + distractor_names
        r.shuffle(options)
        memo = (
            f"1. Tissue {target_pin_letter}: **{target['name']}** [1]\n"
            f"2. Photosynthetic adaptation: {target['description']} [2]"
        )
        hints = {
            "tier_1": f"Examine the cellular arrangement and chloroplast density of tissue {target_pin_letter}.",
            "tier_2": f"Tissue {target_pin_letter} is the {target['name']}.",
            "tier_3": f"The correct response is: {correct_ans}.",
        }
        marks = 3
        misconceptions = ["confused_palisade_with_spongy", "epidermal_chloroplast_misconception"]

    elif subskill == "transpiration_adaptation":
        prompt = (
            f"A Grade {grade} learner analyzes the rate of water loss from a plant leaf.\n\n"
            f"1. Identify structure **{target_pin_letter}** on the diagram.\n"
            f"2. Explain TWO structural adaptations of the leaf that reduce excessive water loss through transpiration."
        )
        correct_ans = (
            f"1. {target['name']}; "
            f"2. Thick waxy cuticle reduces evaporation; Stomata concentrated on shaded lower epidermis / sunken stomata."
        )
        memo = (
            f"1. Structure {target_pin_letter}: **{target['name']}** [1]\n"
            f"2. Adaptations to reduce transpiration (any 2) [4]:\n"
            f"   - Thick waxy cuticle on the upper surface prevents cuticular water loss.\n"
            f"   - Stomata located primarily on the cooler, shaded lower (abaxial) epidermis.\n"
            f"   - Presence of epidermal trichomes (hairs) trapping a humid boundary layer.\n"
            f"   - Sunken stomata creating humid microclimates that reduce the water potential gradient."
        )
        hints = {
            "tier_1": "Think about how xerophytes and mesophytes conserve water while continuing photosynthesis.",
            "tier_2": "Cuticle thickness, stomatal distribution on the lower surface, and hairiness all reduce the water potential gradient.",
            "tier_3": f"1. {target['name']}. 2. Thick waxy cuticle; stomata located on shaded lower surface.",
        }
        marks = 5
        misconceptions = ["confused_transpiration_with_guttation", "assumed_stomata_on_upper_surface"]

    elif subskill == "vascular_transport":
        prompt = (
            f"The vein in the leaf section contains specialized vascular conducting tissues.\n\n"
            f"1. State whether the xylem vessels are located towards the upper (adaxial) or lower (abaxial) surface of the leaf.\n"
            f"2. Explain how the structural composition of xylem vessels allows them to withstand negative suction pressures during transpiration pull.\n"
            f"3. Name the organic solute translocated through the phloem sieve tubes."
        )
        correct_ans = "1. Upper (adaxial) surface; 2. Thickened cell walls impregnated with lignin prevent collapse; 3. Sucrose (sugar)"
        memo = (
            "1. Xylem vessels are located on the upper (adaxial) side of the vascular bundle. [1]\n"
            "2. Xylem adaptation [2]: Cell walls are heavily thickened and impregnated with lignin [1], "
            "which prevents the vessels from collapsing inward under extreme negative tension/suction forces generated by transpiration pull [1].\n"
            "3. Phloem translocates sucrose (dissolved sugars/assimilates). [1]"
        )
        hints = {
            "tier_1": "In a leaf cross-section, xylem is always toward the top (upper surface) and phloem is toward the bottom.",
            "tier_2": "Lignin provides immense mechanical tensile strength. Phloem transports sucrose made during photosynthesis.",
            "tier_3": "1. Upper (adaxial). 2. Lignified cell walls prevent collapse under tension. 3. Sucrose.",
        }
        marks = 4
        misconceptions = ["xylem_phloem_inversion", "confused_glucose_with_sucrose_translocation", "omitted_lignin_rigidity"]

    else:  # stomatal_mechanism
        prompt = (
            f"Structure **{target_pin_letter}** plays a critical role in regulating gas exchange and transpiration.\n\n"
            f"1. Identify structure **{target_pin_letter}**.\n"
            f"2. Describe the physiological mechanism that causes stomata to open during daylight hours.\n"
            f"3. Explain why the stomatal pore closes when a plant experiences severe water stress (drought)."
        )
        correct_ans = (
            f"1. {target['name']}; "
            f"2. Active uptake of potassium ions lowers guard cell water potential; water enters by osmosis; turgid cells bow outward due to thick inner walls; "
            f"3. Guard cells lose water, lose turgor (become flaccid), and close pore to prevent lethal desiccation."
        )
        memo = (
            f"1. Structure {target_pin_letter}: **{target['name']}** [1]\n"
            f"2. Stomatal opening mechanism [3]:\n"
            f"   - In daylight, active transport pumps potassium ions ($K^+$) into guard cells [1].\n"
            f"   - This lowers the water potential of guard cells, causing water to enter by osmosis [1].\n"
            f"   - Guard cells become turgid; their thinner outer walls stretch more than the thickened inner walls, causing the cells to curve outward and open the pore [1].\n"
            f"3. Under drought/water stress [2]: Abscisic acid (ABA) triggers $K^+$ and water efflux from guard cells [1]. "
            f"The guard cells lose turgor, become flaccid, and the pore closes to prevent dehydration [1]."
        )
        hints = {
            "tier_1": "Stomatal movements depend on turgor pressure changes in the paired guard cells.",
            "tier_2": "Potassium ion influx leads to water entry by osmosis. Thicker inner walls cause the guard cells to bow apart.",
            "tier_3": f"1. {target['name']}. 2. Osmotic entry of water makes guard cells turgid; thick inner walls cause bowing. 3. Water loss causes flaccidity.",
        }
        marks = 6
        misconceptions = ["inverted_turgid_flaccid_state", "omitted_differential_wall_thickness", "forgot_osmotic_potential_concept"]

    diag_payload = {
        "diagram_role": "identify" if locals().get("target_pin") else "context",
        "image_type": "plant_leaf",
        "master": "plant_leaf",
        "view": view_mode,
        "viewBox": "0 0 600 480",
        "grade_mask": grade_str,
        "locked_view": True,
        "pins": client_pins,
        "landmarks": landmarks,
        "target_pin": target_pin_letter,
        "target_key": target_key,
    }

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 9,
        "mode": mode,
        "subskill": subskill,
        "question_type": qtype,
        "options": options,
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": misconceptions,
        "modality": "bio_diagram",
        "diagram": {
            "master": "plant_leaf",
            "view": view_mode,
            "component": "PlantLeafSvg",
            "viewBox": "0 0 600 480",
            "grade_mask": grade_str,
            "locked_view": True,
            "pins": client_pins,
            "landmarks": landmarks,
        },
        "diagram_spec": diag_payload,
        "diagram_meta": diag_payload,
        "_server_solution": {
            "target_key": target_key,
            "target_pin": target_pin_letter,
            "pin_map": server_solution_map,
        },
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": f"Anatomical identification of pin {target_pin_letter}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Physiological explanation or structural adaptation", "marks": marks - 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }
