"""Sensory, Endocrine, and Reproductive Diagram Subskill Builders.

Provides deterministic, 3-layer subskill builders for:
1. Human Eye (human_eye) - Role L / P
2. Human Ear (human_ear) - Role P (hearing & balance pathways, zero A-D pins)
3. Human Endocrine System (endocrine_system) - Role P (homeostatic negative feedback, zero A-D pins)
4. Male Reproductive System (male_reproductive) - Role L / P
5. Female Reproductive System (female_reproductive) - Role L / P

Implements:
- 6-pillar contract (term, caps_weight_percent, duration, misconception_tags, 3-tier hints, marking_schema).
- Anti-leak security: client receives opaque randomized `ref` tokens for Role L; zero structure names in DOM.
- Multi-grade support (Grade 9 Natural Sciences macroscopic vs Grade 12 Life Sciences biochemical mechanisms).
- Locked single-view presentation in question cards.
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


EYE_DATA = _load_anchors("human_eye")
EAR_DATA = _load_anchors("human_ear")
ENDOCRINE_DATA = _load_anchors("endocrine_system")
MALE_REPRO_DATA = _load_anchors("male_reproductive")
FEMALE_REPRO_DATA = _load_anchors("female_reproductive")


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_sensory_salt"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


# ============================================================================
# 1. HUMAN EYE BUILDER (Role L)
# ============================================================================

def build_eye_question(
    seed: int,
    grade: int = 12,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = EYE_DATA["anchors"]
    grade_str = f"g{grade}"
    allowed_keys = [k for k, v in anchors.items() if grade_str in v.get("grades", ["g8", "g9", "g12"])]
    if not allowed_keys:
        allowed_keys = list(anchors.keys())

    if subskill is None:
        if grade < 12:
            subskill = "anatomy_identification"
        else:
            subskill_choices = ["anatomy_identification", "accommodation", "pupillary_reflex", "eye_defects"]
            subskill = subskill_choices[seed % len(subskill_choices)]

    target_key = allowed_keys[seed % len(allowed_keys)]
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
            "role": "target" if k == target_key else "distractor",
        })
        if k == target_key:
            target_pin = letter

    if subskill == "accommodation":
        dist = r.choice(["near", "distant"])
        if dist == "near":
            question_text = (
                f"A person shifts their gaze to read text held 30 cm from their eyes (< 6 m). "
                f"Refer to the eye diagram. Which sequence of physiological changes in the ciliary muscles, "
                f"suspensory ligaments, and lens brings the image into sharp focus, and what structure is labeled Pin {target_pin}?"
            )
            correct_answer = f"Pin {target_pin}: {target['name']}; Ciliary muscles contract, suspensory ligaments slacken, lens becomes more convex (bulges)"
            distractors = [
                f"Pin {target_pin}: {target['name']}; Ciliary muscles relax, suspensory ligaments tighten, lens becomes flatter",
                f"Pin {target_pin}: {anchors[other_keys[0]]['name']}; Ciliary muscles contract, suspensory ligaments tighten, lens becomes flatter",
                f"Pin {target_pin}: {anchors[other_keys[1]]['name']}; Ciliary muscles relax, suspensory ligaments slacken, lens becomes more convex",
            ]
        else:
            question_text = (
                f"A person looks at a distant mountain peak (> 6 m). "
                f"Refer to the eye diagram. Identify Pin {target_pin} and state the sequence of physiological changes in the ciliary muscles, "
                f"suspensory ligaments, and lens that brings the distant image into focus."
            )
            correct_answer = f"Pin {target_pin}: {target['name']}; Ciliary muscles relax, suspensory ligaments tighten (taut), lens becomes less convex (flatter)"
            distractors = [
                f"Pin {target_pin}: {target['name']}; Ciliary muscles contract, suspensory ligaments slacken, lens becomes more convex",
                f"Pin {target_pin}: {anchors[other_keys[0]]['name']}; Ciliary muscles relax, suspensory ligaments slacken, lens becomes flatter",
                f"Pin {target_pin}: {anchors[other_keys[1]]['name']}; Ciliary muscles contract, suspensory ligaments tighten, lens becomes more convex",
            ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["ciliary_suspensory_antagonism_error", "lens_curvature_inversion"]
        hints = [
            "Remember that contraction of the circular ciliary ring moves the ciliary body closer to the lens.",
            "Near vision (< 6 m) requires greater light refraction, so the lens must be thick/convex (ciliary muscles contracted, ligaments slack).",
            f"The correct response is: '{correct_answer}'.",
        ]
    elif subskill == "pupillary_reflex":
        light_state = r.choice(["bright", "dim"])
        if light_state == "bright":
            question_text = (
                f"A learner steps from a dark room into bright midday sunlight. "
                f"Identify Pin {target_pin} on the eye diagram and describe the antagonistic muscle reaction in the iris "
                f"that protects photoreceptors from damage."
            )
            correct_answer = f"Pin {target_pin}: {target['name']}; Circular muscles contract, radial muscles relax, pupil constricts"
            distractors = [
                f"Pin {target_pin}: {target['name']}; Radial muscles contract, circular muscles relax, pupil dilates",
                f"Pin {target_pin}: {anchors[other_keys[0]]['name']}; Circular muscles relax, radial muscles contract, pupil constricts",
                f"Pin {target_pin}: {anchors[other_keys[1]]['name']}; Both circular and radial muscles contract simultaneously",
            ]
        else:
            question_text = (
                f"A learner enters a dimly lit theater. "
                f"Identify Pin {target_pin} on the eye diagram and describe the antagonistic muscle action in the iris "
                f"to maximize light entry onto the retina."
            )
            correct_answer = f"Pin {target_pin}: {target['name']}; Radial muscles contract, circular muscles relax, pupil dilates"
            distractors = [
                f"Pin {target_pin}: {target['name']}; Circular muscles contract, radial muscles relax, pupil constricts",
                f"Pin {target_pin}: {anchors[other_keys[0]]['name']}; Radial muscles relax, circular muscles contract, pupil dilates",
                f"Pin {target_pin}: {anchors[other_keys[1]]['name']}; Both circular and radial muscles relax completely",
            ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["iris_muscle_antagonism_confusion", "pupil_aperture_inversion"]
        hints = [
            "In bright light, less light must enter the eye to avoid bleaching photoreceptors.",
            "Circular muscles act like a drawstring (constriction) while radial muscles radiate outward (dilation).",
            f"The correct response is: '{correct_answer}'.",
        ]
    elif subskill == "eye_defects":
        defect = r.choice(["myopia", "hypermetropia"])
        if defect == "myopia":
            question_text = (
                f"Refer to the longitudinal cross-section of the human eye. Identify Pin {target_pin}, and state the visual defect "
                f"and corrective lens required when the eyeball is elongated so light focuses in front of the retina."
            )
            correct_answer = f"Pin {target_pin}: {target['name']}; Short-sightedness (myopia), corrected using biconcave lenses"
            distractors = [
                f"Pin {target_pin}: {target['name']}; Long-sightedness (hypermetropia), corrected using biconvex lenses",
                f"Pin {target_pin}: {anchors[other_keys[0]]['name']}; Astigmatism, corrected using cylindrical lenses",
                f"Pin {target_pin}: {anchors[other_keys[1]]['name']}; Cataracts, corrected by surgical lens replacement",
            ]
        else:
            question_text = (
                f"Refer to the longitudinal cross-section of the human eye. Identify Pin {target_pin}, and state the visual defect "
                f"and corrective lens required when light rays from near objects converge behind the retina."
            )
            correct_answer = f"Pin {target_pin}: {target['name']}; Long-sightedness (hypermetropia), corrected using biconvex lenses"
            distractors = [
                f"Pin {target_pin}: {target['name']}; Short-sightedness (myopia), corrected using biconcave lenses",
                f"Pin {target_pin}: {anchors[other_keys[0]]['name']}; Astigmatism, corrected using cylindrical lenses",
                f"Pin {target_pin}: {anchors[other_keys[1]]['name']}; Presbyopia, corrected using tinted lenses",
            ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["myopia_hypermetropia_confusion", "lens_correction_inversion"]
        hints = [
            "Consider whether the focal point is in front of or behind the retina.",
            "Myopia (in front) requires diverging biconcave lenses; hypermetropia (behind) requires converging biconvex lenses.",
            f"The correct response is: '{correct_answer}'.",
        ]
    else:  # anatomy_identification
        question_text = (
            f"Study the longitudinal cross-section of the human eye. "
            f"Identify the anatomical structure indicated by Pin {target_pin} and its primary function."
        )
        correct_answer = f"{target['name']} — {target['description']}"
        distractor_names = [f"{anchors[k]['name']} — {anchors[k]['description']}" for k in other_keys[:3]]
        options = [correct_answer] + distractor_names
        r.shuffle(options)
        misconception_tags = ["sclera_choroid_retina_layer_confusion", "fovea_blind_spot_inversion"]
        hints = [
            f"Look at the position of Pin {target_pin} relative to the anterior and posterior chambers.",
            f"{target['description'][:80]}...",
            f"The structure indicated by Pin {target_pin} is {target['name']}.",
        ]

    diag_payload = {
        "diagram_role": "identify" if locals().get("target_pin") else "context",
        "master": "human_eye",
        "image_type": "human_eye",
        "view": "longitudinal_cross_section",
        "viewBox": "0 0 600 480",
        "grade_mask": grade_str,
        "pins": pins_payload,
        "state": "static",
        "target_pin": target_pin,
        "target_key": target_key,
    }

    sol_str = (
        f"Step 1: Locate Pin {target_pin} on the eye cross-section ({target['name']}).\n"
        f"Step 2: Physiological role: {target['description']}\n"
        f"Step 3: Correct answer: {correct_answer}"
    )

    return {
        "id": f"eye_{grade}_{seed}_{subskill}",
        "archetype": "human_eye_anatomy",
        "topic": "Human responses to the environment",
        "subject": "Life Sciences" if grade == 12 else "Natural Sciences",
        "grade": grade,
        "term": 1 if grade == 9 else 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 3,
        "subskill": subskill,
        "modality": "bio_diagram",
        "question_type": "mcq",
        "prompt": question_text,
        "question_text": question_text,
        "correct_answer": correct_answer,
        "sample_answer": sol_str,
        "worked_solution": sol_str,
        "options": options,
        "marks": 3,
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Identification of Pin {target_pin}: {target['name']}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct physiological mechanism / function: {correct_answer}", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "diagram_meta": diag_payload,
        "diagram_spec": diag_payload,
        "misconception_tags": misconception_tags,
        "hints": hints,
        "solution_steps": [
            f"Step 1: Locate Pin {target_pin} on the eye canvas.",
            f"Step 2: Recall anatomical and functional characteristics: {target['description']}",
            f"Step 3: Conclude that the correct answer is {correct_answer}.",
        ],
    }


# ============================================================================
# 2. HUMAN EAR BUILDER (Role P: Hearing & Balance Pathways, Zero A-D Pins)
# ============================================================================

def build_ear_question(
    seed: int,
    grade: int = 12,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = EAR_DATA["anchors"]
    grade_str = f"g{grade}"

    subskill_choices = ["hearing_pathway", "balance_mechanism", "ear_defects"]
    if subskill is None or subskill not in subskill_choices:
        subskill = subskill_choices[seed % len(subskill_choices)]

    landmark_keys = ["pinna", "tympanic_membrane", "eustachian_tube", "auditory_ossicles", "semicircular_canals", "cochlea", "auditory_nerve"]
    landmarks = []
    for k in landmark_keys:
        if k in anchors:
            cfg = anchors[k]
            landmarks.append({
                "name": cfg["name"],
                "text": cfg["name"],
                "anchor": cfg["anchor"],
                "default_box": cfg["default_box"],
                "side": cfg["side"],
                "role": "landmark",
            })

    if subskill == "hearing_pathway":
        question_text = (
            "Refer to the coronal cross-section of the human ear showing the Outer Ear, Middle Ear, and Inner Ear.\n\n"
            "1. Trace the complete mechanical and fluid pathway of sound transmission from the Pinna to the Organ of Corti in the Cochlea. (2)\n"
            "2. Explain why the Auditory Ossicles (Malleus, Incus, Stapes) and the small area of the Oval Window are essential for amplifying vibrations before they enter the fluid-filled Cochlea. (2)"
        )
        correct_answer = (
            "1. Airborne sound waves are collected by the Pinna, travel down the External Auditory Canal, and cause the Tympanic Membrane (eardrum) to vibrate. "
            "The Auditory Ossicles (Malleus, Incus, Stapes) transmit vibrations across the middle ear to the Oval Window, generating pressure waves in the perilymph and endolymph of the Cochlea that stimulate hair cells in the Organ of Corti.\n"
            "2. Because inner ear fluid (perilymph/endolymph) has much higher inertia/density than air, the lever action of the ossicles and the much smaller surface area of the Oval Window relative to the Tympanic Membrane concentrate and amplify pressure so fluid waves are strong enough to bend hair cells."
        )
        marking_points = [
            {"id": "mp_1", "desc": "1. Pathway: Pinna -> Auditory canal -> Tympanic membrane -> Ossicles (Malleus, Incus, Stapes) -> Oval window -> Cochlea (Organ of Corti)", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "2. Amplification explanation: lever action of ossicles and smaller surface area of oval window overcome higher density/inertia of cochlear fluid", "marks": 2, "editable": True},
        ]
        misconception_tags = ["hearing_pathway_sequence_error", "oval_vs_round_window_inversion"]
        hints = [
            "Sound begins as airborne waves in the outer ear, becomes mechanical bone vibration in the middle ear, and fluid waves in the inner ear.",
            "Moving liquid in the cochlea requires more force than moving air; compare the size of the Tympanic Membrane to the Oval Window.",
            correct_answer,
        ]
    elif subskill == "balance_mechanism":
        question_text = (
            "Refer to the inner ear vestibular apparatus (Semicircular Canals, Utricle, and Saccule) shown in the ear diagram.\n\n"
            "1. Describe how the Semicircular Canals detect rotational (dynamic) changes in speed and direction of the head. (2)\n"
            "2. Distinguish between the sensory receptors and stimuli for dynamic balance in the Semicircular Canals versus static (gravitational) balance in the Utricle and Saccule. (2)"
        )
        correct_answer = (
            "1. Movement of the head in any of three perpendicular planes causes endolymph fluid inside the Semicircular Canals to lag behind, bending the gelatinous cupula and stimulating the sensory hair cells of the cristae in the ampullae to generate nerve impulses along the vestibular branch of the Auditory Nerve.\n"
            "2. Dynamic balance uses cristae (with cupulae) in the ampullae of the Semicircular Canals to detect rotational acceleration, whereas static balance uses maculae (with calcium carbonate otoliths) in the Utricle and Saccule to detect head position relative to gravity."
        )
        marking_points = [
            {"id": "mp_1", "desc": "1. Endolymph movement bends cupula and stimulates cristae in ampullae of semicircular canals", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "2. Cristae in semicircular canals detect rotation vs maculae (with otoliths) in utricle/saccule detect gravity/head position", "marks": 2, "editable": True},
        ]
        misconception_tags = ["dynamic_vs_static_balance_confusion", "cochlea_balance_misconception"]
        hints = [
            "Remember: Semicircular canals = rotation/dynamic balance; Utricle & Saccule = gravity/head tilt/static balance.",
            "Sensory receptors in ampullae are cristae; sensory receptors in utricle and saccule are maculae.",
            correct_answer,
        ]
    else:  # ear_defects
        variant = r.choice(["otitis_media_grommets", "conductive_vs_sensorineural", "altitude_barotrauma"])
        if variant == "otitis_media_grommets":
            question_text = (
                "Refer to the middle ear cavity and Eustachian Tube in the human ear diagram.\n\n"
                "1. Explain the physiological function of the Eustachian Tube during rapid changes in altitude (such as flying or diving), and explain how blockage of this tube leads to middle ear infection (otitis media). (2)\n"
                "2. State how insertion of a tympanostomy tube (grommet) into the Tympanic Membrane restores normal hearing in a child with chronic middle ear fluid accumulation. (2)"
            )
            correct_answer = (
                "1. The Eustachian Tube connects the middle ear cavity to the pharynx to equalize air pressure on both sides of the Tympanic Membrane so it can vibrate freely. When blocked by mucus or inflammation during a throat infection, bacteria and fluid accumulate in the middle ear cavity (otitis media), increasing pressure and dampening eardrum vibration.\n"
                "2. A grommet provides an open ventilation channel through the Tympanic Membrane, allowing trapped fluid to drain and equalizing air pressure in the middle ear so the Tympanic Membrane and Auditory Ossicles can vibrate normally."
            )
            marking_points = [
                {"id": "mp_1", "desc": "1. Eustachian tube equalizes pressure across tympanic membrane; blockage traps fluid/bacteria in middle ear (otitis media)", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "2. Grommet ventilates middle ear / drains fluid and equalizes pressure so tympanic membrane vibrates freely", "marks": 2, "editable": True},
            ]
            misconception_tags = ["eustachian_tube_misattribution", "middle_vs_outer_ear_infection"]
            hints = [
                "The Eustachian tube connects the middle ear cavity to the back of the throat (nasopharynx).",
                "Fluid trapped behind the eardrum prevents it from vibrating; a grommet equalizes pressure and allows drainage.",
                correct_answer,
            ]
        elif variant == "conductive_vs_sensorineural":
            question_text = (
                "Hearing impairment may be classified as either conductive hearing loss or sensorineural (nerve) deafness.\n\n"
                "1. Distinguish between conductive hearing loss (e.g. otosclerosis/ossicle fusion) and sensorineural hearing loss (e.g. cochlear hair cell or auditory nerve damage). (2)\n"
                "2. Explain why a conventional sound-amplifying hearing aid is effective for conductive hearing loss but ineffective if the auditory nerve is severed. (2)"
            )
            correct_answer = (
                "1. Conductive hearing loss results from physical obstruction or mechanical failure transmitting sound vibrations through the outer or middle ear (ossicles/tympanic membrane); sensorineural deafness results from damage to the receptor hair cells in the cochlea (Organ of Corti) or the auditory nerve fibers.\n"
                "2. A conventional hearing aid amplifies acoustic sound waves so they can still reach the inner ear; however, if the auditory nerve is damaged or severed, electrical nerve impulses cannot be transmitted to the cerebral cortex for perception regardless of how loud the amplified sound is."
            )
            marking_points = [
                {"id": "mp_1", "desc": "1. Distinguishes physical vibration transmission failure (conductive) from receptor/nerve damage (sensorineural)", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "2. Explains hearing aid amplifies acoustic vibration but cannot restore lost impulse transmission along a damaged nerve", "marks": 2, "editable": True},
            ]
            misconception_tags = ["conductive_vs_sensorineural_confusion", "hearing_aid_nerve_fallacy"]
            hints = [
                "Conductive involves mechanics (eardrum, bones); sensorineural involves receptors and nerves (cochlea, auditory nerve).",
                "Amplifying sound helps if the problem is transmission, but impulses still need a functional nerve to reach the brain.",
                correct_answer,
            ]
        else:
            question_text = (
                "During rapid descent in an unpressurized aircraft or while scuba diving, an individual fails to 'pop' their ears.\n\n"
                "1. Explain why ambient external pressure changes cause intense pain and inward bulging of the Tympanic Membrane if the Eustachian Tube fails to open. (2)\n"
                "2. Describe how swallowing, chewing, or yawning facilitates middle ear pressure equalization. (2)"
            )
            correct_answer = (
                "1. Higher atmospheric pressure in the external auditory canal presses inward against the Tympanic Membrane because air pressure in the closed middle ear cavity remains lower; this inward deformation stretches nociceptive pain fibres in the eardrum.\n"
                "2. Actions like swallowing or yawning contract tensor veli palatini muscles connected to the pharyngeal orifice of the Eustachian Tube, momentarily pulling it open and allowing air to rush into the middle ear to restore pressure equilibrium."
            )
            marking_points = [
                {"id": "mp_1", "desc": "1. Explains higher external pressure relative to closed middle ear forces eardrum inward causing mechanical tension/pain", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "2. Explains muscular contraction during swallowing/yawning pulls open Eustachian orifice to equalize pressure", "marks": 2, "editable": True},
            ]
            misconception_tags = ["tympanic_pressure_differential_error", "eustachian_muscular_opening_mechanism"]
            hints = [
                "Compare the air pressure outside the eardrum with the air pressure trapped inside the middle ear.",
                "Swallowing pulls the opening of the Eustachian tube open in the nasopharynx.",
                correct_answer,
            ]

    diag_payload = {
        "diagram_role": "identify" if locals().get("target_pin") else "context",
        "master": "human_ear",
        "image_type": "human_ear",
        "view": "coronal_auditory_section",
        "viewBox": "0 0 600 480",
        "grade_mask": grade_str,
        "pins": [],
        "landmarks": landmarks,
        "state": "static",
    }

    return {
        "id": f"ear_{grade}_{seed}_{subskill}",
        "archetype": "human_ear_anatomy",
        "topic": "Human responses to the environment",
        "subject": "Life Sciences" if grade == 12 else "Natural Sciences",
        "grade": grade,
        "term": 1 if grade == 9 else 2,
        "caps_weight_percent": 16,
        "suggested_duration_mins": 5,
        "subskill": subskill,
        "modality": "bio_diagram",
        "question_type": "diagram_short_answer",
        "prompt": question_text,
        "question_text": question_text,
        "correct_answer": correct_answer,
        "sample_answer": correct_answer,
        "worked_solution": correct_answer,
        "marks": 4,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "diagram_meta": diag_payload,
        "diagram_spec": diag_payload,
        "misconception_tags": misconception_tags,
        "hints": {
            "tier_1": hints[0],
            "tier_2": hints[1],
            "tier_3": hints[2],
        },
    }


# ============================================================================
# 3. ENDOCRINE SYSTEM BUILDER (Role P: Homeostatic Negative Feedback, Zero A-D Pins)
# ============================================================================

def build_endocrine_question(
    seed: int,
    grade: int = 12,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    anchors = ENDOCRINE_DATA["anchors"]
    grade_str = f"g{grade}"

    subskill_choices = ["glucose_homeostasis", "thyroxine_feedback", "osmoregulation_adh"]
    if subskill is None or subskill not in subskill_choices:
        subskill = subskill_choices[seed % len(subskill_choices)]

    landmark_keys = ["hypothalamus", "pituitary_gland", "thyroid_gland", "adrenal_glands", "pancreas", "ovaries", "testes"]
    landmarks = []
    for k in landmark_keys:
        if k in anchors:
            cfg = anchors[k]
            landmarks.append({
                "name": cfg["name"],
                "text": cfg["name"],
                "anchor": cfg["anchor"],
                "default_box": cfg["default_box"],
                "side": cfg["side"],
                "role": "landmark",
            })

    if subskill == "glucose_homeostasis":
        question_text = (
            "Refer to the Human Endocrine System diagram showing the Pancreas (Islets of Langerhans) and Adrenal Glands.\n\n"
            "1. Describe the negative feedback mechanism mediated by the Pancreas when blood glucose levels rise above the normal setpoint after a carbohydrate-rich meal. (2)\n"
            "2. Explain how the antagonistic hormone glucagon restores blood glucose levels during fasting, and state how adrenaline from the Adrenal Glands reinforces this effect during an emergency. (2)"
        )
        correct_answer = (
            "1. Beta cells in the Islets of Langerhans of the Pancreas detect high blood glucose and secrete insulin into the bloodstream. "
            "Insulin increases cell membrane permeability to glucose and stimulates liver and muscle cells to convert excess glucose into stored glycogen, lowering blood glucose back to normal.\n"
            "2. When blood glucose drops, alpha cells in the Pancreas secrete glucagon, which stimulates the liver to hydrolyse stored glycogen back into glucose. "
            "During an emergency, adrenaline from the Adrenal Glands also stimulates glycogenolysis in the liver to rapidly increase blood glucose for cellular respiration in skeletal muscles."
        )
        marking_points = [
            {"id": "mp_1", "desc": "1. Beta cells of Pancreas secrete insulin -> liver/muscle cells convert glucose to glycogen and increase glucose uptake", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "2. Alpha cells secrete glucagon (glycogen -> glucose in liver); adrenaline enhances glycogenolysis for emergency energy", "marks": 2, "editable": True},
        ]
        misconception_tags = ["insulin_glucagon_inversion", "alpha_beta_cell_confusion"]
        hints = [
            "Insulin lowers blood glucose ('IN-sulin puts glucose INto cells' and stores it as glycogen).",
            "Glucagon from alpha cells and adrenaline from the adrenal medulla both promote conversion of glycogen to glucose.",
            correct_answer,
        ]
    elif subskill == "thyroxine_feedback":
        question_text = (
            "Refer to the Human Endocrine System diagram showing the Pituitary Gland (Hypophysis) and the Thyroid Gland.\n\n"
            "1. Describe the negative feedback loop between the Pituitary Gland and the Thyroid Gland when blood thyroxine levels fall below normal. (2)\n"
            "2. State two physiological effects of chronic hypothyroidism (undersecretion of thyroxine) on basal metabolic rate and body mass in adults. (2)"
        )
        correct_answer = (
            "1. Low blood thyroxine levels are detected by the Hypothalamus and Pituitary Gland. The anterior Pituitary Gland secretes more Thyroid Stimulating Hormone (TSH) into the blood, which stimulates the Thyroid Gland to synthesize and secrete more thyroxine until normal blood thyroxine levels are restored (which then inhibit further TSH release).\n"
            "2. Undersecretion of thyroxine lowers the basal metabolic rate (rate of cellular respiration), leading to lethargy/fatigue, decreased heat production (cold intolerance), and weight gain."
        )
        marking_points = [
            {"id": "mp_1", "desc": "1. Pituitary secretes more TSH -> stimulates Thyroid gland to secrete more thyroxine -> normal levels inhibit TSH", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "2. Decreased basal metabolic rate / cellular respiration, lethargy, and weight gain", "marks": 2, "editable": True},
        ]
        misconception_tags = ["negative_feedback_inversion", "tsh_thyroxine_regulatory_error"]
        hints = [
            "Low thyroxine stimulates the anterior pituitary to release Thyroid Stimulating Hormone (TSH).",
            "Thyroxine regulates the basal metabolic rate (rate of cellular respiration in body cells).",
            correct_answer,
        ]
    else:  # osmoregulation_adh
        question_text = (
            "Refer to the Human Endocrine System diagram showing the Hypothalamus, Pituitary Gland, and Adrenal Glands.\n\n"
            "1. Describe the homeostatic osmoregulation pathway involving the Hypothalamus and Pituitary Gland on a hot day when a marathon runner loses water through heavy sweating (low blood water potential). (2)\n"
            "2. Explain how aldosterone secreted by the Adrenal Glands regulates blood sodium ion (Na⁺) concentration when blood sodium levels drop. (2)"
        )
        correct_answer = (
            "1. Osmoreceptors in the Hypothalamus detect the low water potential (hypertonic blood) and stimulate the posterior Pituitary Gland to secrete more Antidiuretic Hormone (ADH). "
            "ADH increases the permeability of the distal convoluted tubules and collecting ducts in the kidneys so more water is reabsorbed into the blood, producing a small volume of concentrated urine.\n"
            "2. When blood sodium levels drop, the adrenal cortex of the Adrenal Glands secretes more aldosterone, which stimulates active reabsorption of Na⁺ ions from the renal filtrate back into the blood capillaries."
        )
        marking_points = [
            {"id": "mp_1", "desc": "1. Hypothalamus osmoreceptors -> Pituitary secretes more ADH -> collecting ducts more permeable -> more water reabsorbed into blood", "marks": 2, "editable": True},
            {"id": "mp_2", "desc": "2. Adrenal cortex secretes more aldosterone -> increases active reabsorption of Na+ ions in kidney tubules", "marks": 2, "editable": True},
        ]
        misconception_tags = ["adh_osmoregulation_inversion", "pituitary_lobe_confusion"]
        hints = [
            "Anti-Diuretic Hormone (ADH) conserves body water by increasing collecting duct permeability in the kidneys.",
            "Aldosterone from the adrenal cortex regulates salt (Na⁺) reabsorption in the nephron tubules.",
            correct_answer,
        ]

    diag_payload = {
        "diagram_role": "identify" if locals().get("target_pin") else "context",
        "master": "endocrine_system",
        "image_type": "endocrine_system",
        "view": "glandular_anatomic_map",
        "viewBox": "0 0 600 480",
        "grade_mask": grade_str,
        "pins": [],
        "landmarks": landmarks,
        "state": "static",
    }

    return {
        "id": f"endocrine_{grade}_{seed}_{subskill}",
        "archetype": "endocrine_system_map",
        "topic": "The human endocrine system and homeostasis",
        "subject": "Life Sciences" if grade == 12 else "Natural Sciences",
        "grade": grade,
        "term": 1 if grade == 9 else 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "subskill": subskill,
        "modality": "bio_diagram",
        "question_type": "diagram_short_answer",
        "prompt": question_text,
        "question_text": question_text,
        "correct_answer": correct_answer,
        "sample_answer": correct_answer,
        "worked_solution": correct_answer,
        "marks": 4,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": marking_points,
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "diagram_meta": diag_payload,
        "diagram_spec": diag_payload,
        "misconception_tags": misconception_tags,
        "hints": {
            "tier_1": hints[0],
            "tier_2": hints[1],
            "tier_3": hints[2],
        },
    }


# ============================================================================
# 4. MALE REPRODUCTIVE SYSTEM BUILDER (Role L)
# ============================================================================

def build_male_reproductive_question(
    seed: int,
    grade: int = 12,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = MALE_REPRO_DATA["anchors"]
    grade_str = f"g{grade}"
    allowed_keys = [k for k, v in anchors.items() if grade_str in v.get("grades", ["g7", "g9", "g12"])]
    if not allowed_keys:
        allowed_keys = list(anchors.keys())

    if subskill is None:
        if grade < 12:
            subskill = "anatomy_identification"
        else:
            subskill = r.choice(["spermatogenesis_temperature", "semen_accessory_glands"])

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

    if subskill == "spermatogenesis_temperature":
        question_text = (
            f"Refer to the sagittal cross-section of the human male reproductive system. "
            f"Identify the structure indicated by Pin {target_pin}, and explain why the testes are housed externally within the scrotum."
        )
        correct_answer = f"Pin {target_pin}: {target['name']}; Scrotum maintains testes at 2°C to 3°C below core body temperature for viable sperm production"
        distractors = [
            f"Pin {target_pin}: {anchors[other_keys[0]]['name']}; To allow testes to secrete testosterone directly into urine",
            f"Pin {target_pin}: {anchors[other_keys[1]]['name']}; To ensure the vas deferens does not constrict",
            f"Pin {target_pin}: {anchors[other_keys[2]]['name']}; To keep mature sperm isolated from blood",
        ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["scrotal_temperature_misconception", "spermatogenesis_thermal_limits"]
        hints = [
            "Enzymes involved in spermatogenesis are temperature sensitive.",
            "Normal body core temperature (37°C) inhibits viable sperm production.",
            f"The correct response is: {correct_answer}.",
        ]
    elif subskill == "semen_accessory_glands":
        question_text = (
            f"Refer to the sagittal cross-section of the male reproductive system. "
            f"Identify Pin {target_pin}, and state which accessory gland secretes an alkaline fluid rich in fructose to energize spermatozoa."
        )
        correct_answer = f"Pin {target_pin}: {target['name']}; Seminal Vesicle secretes fructose-rich fluid"
        distractors = [
            f"Pin {target_pin}: {anchors[other_keys[0]]['name']}; Epididymis secretes fructose-rich fluid",
            f"Pin {target_pin}: {anchors[other_keys[1]]['name']}; Scrotum secretes fructose-rich fluid",
            f"Pin {target_pin}: {anchors[other_keys[2]]['name']}; Ureter secretes fructose-rich fluid",
        ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["accessory_gland_function_confusion", "semen_component_error"]
        hints = [
            "Seminal vesicles contribute ~60% of semen volume, including fructose.",
            "Prostate fluid is alkaline to neutralize acidity; Cowper's gland secretes lubricant.",
            f"The correct answer is: {correct_answer}.",
        ]
    else:  # anatomy_identification
        question_text = (
            f"Study the sagittal cross-section of the human male reproductive system. "
            f"Identify the structure indicated by Pin {target_pin} and its reproductive role."
        )
        correct_answer = f"{target['name']} — {target['description']}"
        distractor_names = [f"{anchors[k]['name']} — {anchors[k]['description']}" for k in other_keys[:3]]
        options = [correct_answer] + distractor_names
        r.shuffle(options)
        misconception_tags = ["male_anatomy_misidentification", "vas_deferens_urethra_confusion"]
        hints = [
            f"Observe Pin {target_pin} along the sperm pathway from testis to penis.",
            f"{target['description'][:80]}...",
            f"The structure indicated by Pin {target_pin} is {target['name']}.",
        ]

    diag_payload = {
        "diagram_role": "identify" if locals().get("target_pin") else "context",
        "master": "male_reproductive",
        "image_type": "male_reproductive",
        "view": "textbook",
        "viewBox": "0 0 600 480",
        "grade_mask": f"g{grade}",
        "pins": pins_payload,
        "state": "static",
        "target_pin": target_pin,
        "target_key": target_key,
    }

    sol_str = (
        f"Step 1: Locate Pin {target_pin} on the male reproductive system ({target['name']}).\n"
        f"Step 2: Physiological role: {target['description']}\n"
        f"Step 3: Correct answer: {correct_answer}"
    )

    return {
        "id": f"male_repro_{grade}_{seed}_{subskill}",
        "archetype": "male_reproductive_anatomy",
        "topic": "Human Reproduction" if grade == 12 else "Human reproduction",
        "subject": "Life Sciences" if grade == 12 else "Natural Sciences",
        "grade": grade,
        "term": 1,
        "caps_weight_percent": 14,
        "suggested_duration_mins": 3,
        "subskill": subskill,
        "modality": "bio_diagram",
        "question_type": "mcq",
        "prompt": question_text,
        "question_text": question_text,
        "correct_answer": correct_answer,
        "sample_answer": sol_str,
        "worked_solution": sol_str,
        "options": options,
        "marks": 3,
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Identification of Pin {target_pin}: {target['name']}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Reproductive function / explanation: {correct_answer}", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "diagram_meta": diag_payload,
        "diagram_spec": diag_payload,
        "misconception_tags": misconception_tags,
        "hints": hints,
        "solution_steps": [
            f"Step 1: Locate Pin {target_pin} on the male reproductive system.",
            f"Step 2: Note its anatomical relation: {target['description']}",
            f"Step 3: The correct answer is {correct_answer}.",
        ],
    }


# ============================================================================
# 5. FEMALE REPRODUCTIVE SYSTEM BUILDER (Role L)
# ============================================================================

def build_female_reproductive_question(
    seed: int,
    grade: int = 12,
    mode: str = "practice",
    subskill: Optional[str] = None,
) -> Dict[str, Any]:
    r = random.Random(seed)
    anchors = FEMALE_REPRO_DATA["anchors"]
    grade_str = f"g{grade}"
    allowed_keys = [k for k, v in anchors.items() if grade_str in v.get("grades", ["g7", "g9", "g12"])]
    if not allowed_keys:
        allowed_keys = list(anchors.keys())

    if subskill is None:
        if grade < 12:
            subskill = "anatomy_identification"
        else:
            subskill = r.choice(["hormonal_menstrual_cycle", "fertilization_implantation"])

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

    if subskill == "hormonal_menstrual_cycle":
        phase = r.choice(["follicular", "luteal"])
        if phase == "follicular":
            question_text = (
                f"Refer to the coronal view of the female reproductive system. Identify Pin {target_pin}, and state which hormone "
                f"is secreted by developing Graafian follicles during days 1 to 14 to thicken the endometrium."
            )
            correct_answer = f"Pin {target_pin}: {target['name']}; Estrogen (Oestrogen) thickens the endometrium"
            distractors = [
                f"Pin {target_pin}: {anchors[other_keys[0]]['name']}; Oxytocin thickens the endometrium",
                f"Pin {target_pin}: {anchors[other_keys[1]]['name']}; Prolactin thickens the endometrium",
                f"Pin {target_pin}: {anchors[other_keys[2]]['name']}; Testosterone thickens the endometrium",
            ]
        else:
            question_text = (
                f"Refer to the coronal view of the female reproductive system. Identify Pin {target_pin}, and state which hormone "
                f"is secreted in large quantities by the corpus luteum after ovulation to maintain the endometrium for implantation."
            )
            correct_answer = f"Pin {target_pin}: {target['name']}; Progesterone maintains the endometrium"
            distractors = [
                f"Pin {target_pin}: {anchors[other_keys[0]]['name']}; Follicle Stimulating Hormone (FSH) alone",
                f"Pin {target_pin}: {anchors[other_keys[1]]['name']}; Prolactin maintains the endometrium",
                f"Pin {target_pin}: {anchors[other_keys[2]]['name']}; Adrenaline maintains the endometrium",
            ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["estrogen_progesterone_cycle_confusion", "follicular_luteal_phase_inversion"]
        hints = [
            "Estrogen repairs and thickens the endometrium before ovulation.",
            "Progesterone maintains the thickened vascular endometrium after ovulation.",
            f"The correct response is: {correct_answer}.",
        ]
    elif subskill == "fertilization_implantation":
        question_text = (
            f"Study the coronal view of the female reproductive system. Identify Pin {target_pin}, and state where fertilisation "
            f"and blastocyst implantation normally occur."
        )
        correct_answer = f"Pin {target_pin}: {target['name']}; Fertilisation occurs in the Fallopian tube (oviduct) and implantation in the endometrium"
        distractors = [
            f"Pin {target_pin}: {anchors[other_keys[0]]['name']}; Fertilisation occurs in the ovary and implantation in the Fallopian tube",
            f"Pin {target_pin}: {anchors[other_keys[1]]['name']}; Fertilisation occurs in the uterus and implantation in the cervix",
            f"Pin {target_pin}: {anchors[other_keys[2]]['name']}; Fertilisation occurs in the vagina and implantation in the myometrium",
        ]
        options = [correct_answer] + distractors
        r.shuffle(options)
        misconception_tags = ["fertilization_site_misidentification", "implantation_tissue_confusion"]
        hints = [
            "Fertilisation occurs high in the oviduct within 24 hours of ovulation.",
            "Implantation of the multicellular blastocyst occurs in the vascular uterine endometrium.",
            f"The correct answer is: {correct_answer}.",
        ]
    else:  # anatomy_identification
        question_text = (
            f"Study the coronal cross-section of the human female reproductive system. "
            f"Identify the structure indicated by Pin {target_pin} and its reproductive role."
        )
        correct_answer = f"{target['name']} — {target['description']}"
        distractor_names = [f"{anchors[k]['name']} — {anchors[k]['description']}" for k in other_keys[:3]]
        options = [correct_answer] + distractor_names
        r.shuffle(options)
        misconception_tags = ["female_anatomy_misidentification", "fallopian_ovary_relation_error"]
        hints = [
            f"Observe Pin {target_pin} on the female reproductive tract.",
            f"{target['description'][:80]}...",
            f"The structure indicated by Pin {target_pin} is {target['name']}.",
        ]

    diag_payload = {
        "diagram_role": "identify" if locals().get("target_pin") else "context",
        "master": "female_reproductive",
        "image_type": "female_reproductive",
        "view": "textbook",
        "viewBox": "0 0 600 480",
        "grade_mask": f"g{grade}",
        "pins": pins_payload,
        "state": "static",
        "target_pin": target_pin,
        "target_key": target_key,
    }

    sol_str = (
        f"Step 1: Locate Pin {target_pin} on the female reproductive tract ({target['name']}).\n"
        f"Step 2: Physiological role: {target['description']}\n"
        f"Step 3: Correct answer: {correct_answer}"
    )

    return {
        "id": f"female_repro_{grade}_{seed}_{subskill}",
        "archetype": "female_reproductive_anatomy",
        "topic": "Human Reproduction" if grade == 12 else "Human reproduction",
        "subject": "Life Sciences" if grade == 12 else "Natural Sciences",
        "grade": grade,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 3,
        "subskill": subskill,
        "modality": "bio_diagram",
        "question_type": "mcq",
        "prompt": question_text,
        "question_text": question_text,
        "correct_answer": correct_answer,
        "sample_answer": sol_str,
        "worked_solution": sol_str,
        "options": options,
        "marks": 3,
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp_1", "desc": f"Identification of Pin {target_pin}: {target['name']}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Reproductive function / explanation: {correct_answer}", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "diagram_meta": diag_payload,
        "diagram_spec": diag_payload,
        "misconception_tags": misconception_tags,
        "hints": hints,
        "solution_steps": [
            f"Step 1: Locate Pin {target_pin} on the female reproductive tract.",
            f"Step 2: Recall functional significance: {target['description']}",
            f"Step 3: The correct answer is {correct_answer}.",
        ],
    }
