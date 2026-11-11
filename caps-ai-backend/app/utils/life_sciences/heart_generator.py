"""Human Heart Reusable Subskill Builder & Question Generator (Grades 9 & 10).

Fully grounded in:
- NaturalSciences_Gr9/Term 1/04. Circulatory and respiratory systems.md
- LifeSciences_Gr10/Term 2/05. Transport systems in animals.md

Implements:
1. 6-pillar contract (term, caps_weight_percent, duration, misconception_tags, 3-tier hints, learning_objective_id).
2. Anti-leak assessment contract: client payload contains ZERO structure names or canonical keys for Role L targets.
3. Role P compliance for `cardiac_cycle_phase` and `electrical_pacemaker`: zero A-D pins, real anatomical landmark labels, process/duration/pathway questions.
4. Progressive depth staging (g9 macroscopic vs g10 ultrastructure & cardiac cycle).
5. Deterministic single-view selection ('textbook', 'flow', or 'exam') per question archetype/mode.
"""

from __future__ import annotations

import json
import os
import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

ANCHORS_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "data",
    "diagram_anchors",
    "heart.json",
)

with open(ANCHORS_FILE, "r", encoding="utf-8") as f:
    HEART_DATA = json.load(f)

ANCHORS = HEART_DATA["anchors"]
PHASES = HEART_DATA["phases"]


def _make_ref(seed: int, key: str, index: int) -> str:
    """Generate an unpredictable per-instance reference token for server-side verification."""
    raw = f"{seed}_{key}_{index}_fundile_salt"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _build_cardiac_cycle_simulearn_script(target_a_name: str, target_b_name: Optional[str]) -> Dict[str, Any]:
    """Build a canonical 3-phase SimuLearn visual walkthrough script for the human heart."""
    return {
        "title": "Human Heart & 3-Phase Cardiac Cycle Walkthrough",
        "steps": [
            {
                "step": 1,
                "phase": "atrial_systole",
                "title": "Phase 1: Atrial Systole (0,1 s)",
                "narration": (
                    "Deoxygenated blood from the venae cavae and oxygenated blood from the pulmonary veins "
                    "fill the right and left atria. Both atria contract simultaneously for 0,1 s, forcing blood "
                    "through the open tricuspid and bicuspid (mitral) valves into the ventricles."
                ),
                "highlight_pins": ["A"],
            },
            {
                "step": 2,
                "phase": "ventricular_systole",
                "title": "Phase 2: Ventricular Systole — 'Lubb' Sound (0,3 s)",
                "narration": (
                    "The muscular ventricles contract forcefully from the apex upward for 0,3 s. Rising ventricular "
                    "hydrostatic pressure snaps the tricuspid and bicuspid valves shut (producing the loud 'lubb' heart sound), "
                    "while chordae tendineae prevent valve eversion. Blood is ejected through the open semilunar valves "
                    "into the pulmonary artery and aorta."
                ),
                "highlight_pins": ["A", "B"] if target_b_name else ["A"],
            },
            {
                "step": 3,
                "phase": "general_diastole",
                "title": "Phase 3: General Diastole — 'Dubb' Sound (0,4 s)",
                "narration": (
                    f"Both atria and ventricles relax for 0,4 s. As ventricular pressure drops below arterial pressure, "
                    f"blood recoils against the aortic and pulmonary semilunar valves, snapping them shut (producing the 'dubb' sound). "
                    f"Verified structures: {target_a_name}"
                    + (f", {target_b_name}." if target_b_name else ".")
                ),
                "highlight_pins": ["B"] if target_b_name else ["A"],
            },
        ],
    }


def generate_heart_question(
    seed: int,
    grade: int = 9,
    mode: str = "assessment",
    subskill: Optional[str] = None,
    view: Optional[str] = None,
) -> Dict[str, Any]:
    """Generate a deterministic, syllabus-grounded human heart question."""
    r = random.Random(seed)
    grade_str = f"g{grade}"
    allowed_keys = [k for k, v in ANCHORS.items() if grade_str in v["grades"]]

    # Question archetype selection based on grade and subskill
    if grade >= 10:
        archetype_pool = ["cardiac_cycle_phase", "valve_mechanics", "identification_adaptation", "electrical_pacemaker"]
        if subskill in ("cardiac_cycle", "cardiac_cycle_and_electrical_control"):
            archetype = "cardiac_cycle_phase"
        elif subskill in ("valves", "heart_external_and_internal_anatomy"):
            archetype = "valve_mechanics"
        elif subskill == "nodes":
            archetype = "electrical_pacemaker"
        elif subskill == "vessels":
            archetype = "blood_vessel_direction"
        elif subskill == "chambers":
            archetype = "identification_adaptation"
        else:
            archetype = r.choice(archetype_pool)
    else:
        archetype_pool = ["identification_adaptation", "blood_vessel_direction", "chamber_differentiation"]
        if subskill == "vessels":
            archetype = "blood_vessel_direction"
        elif subskill in ("chambers", "heart_structure_and_double_circulation"):
            archetype = "chamber_differentiation"
        else:
            archetype = r.choice(archetype_pool)

    # Role P vs Role L separation:
    # Role P archetypes: cardiac_cycle_phase, electrical_pacemaker -> zero A-D pins, real landmark labels
    is_role_p = archetype in ("cardiac_cycle_phase", "electrical_pacemaker")

    if archetype == "cardiac_cycle_phase":
        phase_key = r.choice(["atrial_systole", "ventricular_systole", "general_diastole"])
        target_keys = ["tricuspid_valve", "bicuspid_valve"] if grade >= 10 else ["right_ventricle", "left_ventricle"]
        active_state = phase_key
        landmark_keys = ["right_atrium", "tricuspid_valve", "right_ventricle", "aorta", "pulmonary_artery", "bicuspid_valve", "left_ventricle"]
    elif archetype == "electrical_pacemaker":
        target_keys = ["sa_node", "av_node"]
        active_state = "static"
        landmark_keys = ["sa_node", "right_atrium", "av_node", "interventricular_septum", "right_ventricle", "left_ventricle"]
    elif archetype == "valve_mechanics":
        target_keys = r.sample(["tricuspid_valve", "bicuspid_valve", "semilunar_valves", "tendinous_cords"], k=2)
        active_state = "static"
        remaining_keys = [k for k in allowed_keys if k not in target_keys]
        landmark_keys = r.sample(remaining_keys, k=min(2, len(remaining_keys)))
    elif archetype == "blood_vessel_direction":
        vessels = ["superior_vena_cava", "pulmonary_artery", "aorta", "pulmonary_veins"]
        target_keys = r.sample(vessels, k=2)
        active_state = "static"
        remaining_keys = [k for k in allowed_keys if k not in target_keys]
        landmark_keys = r.sample(remaining_keys, k=min(2, len(remaining_keys)))
    else:
        chambers = ["right_atrium", "right_ventricle", "left_atrium", "left_ventricle"]
        target_keys = r.sample(chambers, k=2)
        active_state = "static"
        remaining_keys = [k for k in allowed_keys if k not in target_keys]
        landmark_keys = r.sample(remaining_keys, k=min(2, len(remaining_keys)))

    letters = ["A", "B", "C", "D", "E"]
    client_pins = []
    server_target_refs = {}

    for i, k in enumerate(target_keys):
        letter = letters[i]
        ref = _make_ref(seed, k, i)
        cfg = ANCHORS[k]
        if not is_role_p:
            client_pins.append({
                "pin": letter,
                "ref": ref,
                "anchor": cfg["anchor"],
                "default_box": cfg["default_box"],
                "side": cfg["side"],
                "role": "target",
            })
        server_target_refs[letter] = {
            "key": k,
            "ref": ref,
            "name": cfg["name"],
            "synonyms": cfg["synonyms"],
            "description": cfg["description"],
            "side": cfg["side"],
        }

    client_landmarks = []
    for k in landmark_keys:
        cfg = ANCHORS[k]
        client_landmarks.append({
            "name": cfg["name"],
            "text": cfg["name"],
            "anchor": cfg["anchor"],
            "default_box": cfg["default_box"],
            "side": cfg["side"],
            "role": "landmark",
        })

    target_a = server_target_refs["A"]
    target_b = server_target_refs["B"] if "B" in server_target_refs else None

    if archetype == "cardiac_cycle_phase":
        phase_data = PHASES[active_state]
        dur_str = str(phase_data["duration_sec"]).replace(".", ",")
        sound_str = f"'{phase_data['sound']}' sound" if phase_data["sound"] else "No heart sound (neither 'lubb' nor 'dubb')"
        question_text = (
            f"Refer to the directional blood-flow diagram of the human heart during a single heartbeat (total cardiac cycle = 0,8 s).\n\n"
            f"Consider the phase in which the atria are {phase_data['atria'].replace('_', ' ')} and the ventricles are {phase_data['ventricles'].replace('_', ' ')} (duration = {dur_str} s):\n"
            f"1. Name this phase of the cardiac cycle.\n"
            f"2. State whether the atrioventricular valves (Tricuspid Valve and Bicuspid Valve) and the Semi-lunar Valves are open or closed during this phase.\n"
            f"3. Identify the heart sound produced during this phase and explain the valve action that causes it."
        )
        ans_str = (
            f"1. {phase_data['name']} ({dur_str} s)\n"
            f"2. Atrioventricular (Tricuspid and Bicuspid) valves are {phase_data['av_valves']}; Semi-lunar valves are {phase_data['semilunar_valves']}.\n"
            f"3. {sound_str}. {phase_data['narrative']}"
        )
        memo = ans_str
        marking_points = [
            {"point": 1, "desc": f"1. Identifies phase: {phase_data['name']} ({dur_str} s)"},
            {"point": 2, "desc": f"2. AV valves {phase_data['av_valves']} and Semi-lunar valves {phase_data['semilunar_valves']}"},
            {"point": 3, "desc": f"3. Heart sound ({sound_str}) and valve mechanism: {phase_data['narrative']}"},
        ]
        tier_1 = "Recall the three phases of the 0,8 s cardiac cycle: Atrial Systole (0,1 s), Ventricular Systole (0,3 s), and General Diastole (0,4 s)."
        tier_2 = f"During {phase_data['name']}, AV valves are {phase_data['av_valves']} and semi-lunar valves are {phase_data['semilunar_valves']}."
        tier_3 = ans_str
        misconceptions = ["valve_sound_inversion", "semilunar_vs_av_confusion"]
        marks = 4
        default_view = "flow"
        lo_id = "LS10.T2.TSA.CARDIAC_CYCLE"

    elif archetype == "valve_mechanics":
        case_id = (abs(int(seed)) % 97) + 1 if seed is not None else 1
        orientation = "anterior longitudinal cross-section" if case_id % 2 == 0 else "coronal sectional view"
        question_text = (
            f"Refer to the {orientation} diagram of the human heart (Case #{case_id}).\n\n"
            f"1. Identify the anatomical structure indicated by Pin A.\n"
            f"2. Identify the anatomical structure indicated by Pin B.\n"
            f"3. Explain the primary mechanical function of structure A during ventricular systole."
        )
        ans_str = f"1. {target_a['name']}\n2. {target_b['name']}\n3. {target_a['description']}"
        memo = ans_str
        marking_points = [
            {"point": 1, "desc": f"1. Identifies Pin A as {target_a['name']}"},
            {"point": 2, "desc": f"2. Identifies Pin B as {target_b['name']}"},
            {"point": 3, "desc": f"3. Function of structure A: {target_a['description']}"},
        ]
        tier_1 = "Remember that anatomical right is on the left side of the diagram."
        tier_2 = f"Pin A is located on the {'anatomical right' if target_a['side'] == 'left' else 'anatomical left'} side."
        tier_3 = f"A: {target_a['name']}. B: {target_b['name']}. Function: {target_a['description']}."
        misconceptions = ["left_right_orientation_flip", "atria_ventricle_swap"]
        marks = 4
        default_view = "textbook"
        lo_id = "LS10.T2.TSA.HEART_ANATOMY"

    elif archetype == "electrical_pacemaker":
        pacemaker_scenarios = [
            {
                "context": "resting physiological state (heart rate = 72 beats per minute)",
                "q1": "1. Explain why the Sinoatrial Node (SA node) in the upper right atrium wall is described as the natural myogenic pacemaker of the heart.",
                "q2": "2. Trace the pathway of the electrical impulse from the Atrioventricular Node (AV node) through the Interventricular Septum to the ventricular myocardium.",
                "q3": "3. Explain the physiological importance of the brief 0,1 s delay at the Atrioventricular Node before the ventricles contract.",
                "a1": "1. The Sinoatrial Node (SA node) initiates rhythmic electrical impulses spontaneously (myogenically) without external nervous stimulation, setting the pace of the heartbeat and causing both atria to contract simultaneously.",
                "a2": "2. From the Atrioventricular Node (AV node), the electrical impulse travels down the Bundle of His (atrioventricular bundle) along the Interventricular Septum, divides into right and left bundle branches, and spreads upward through the Purkinje fibres in the ventricular walls.",
                "a3": "3. The brief delay at the AV node allows the atria to finish contracting and empty blood completely into the ventricles before ventricular systole begins from the apex upward.",
                "mp1": "1. SA node initiates spontaneous myogenic impulses causing simultaneous atrial contraction",
                "mp2": "2. Conduction pathway: AV node -> Bundle of His in interventricular septum -> bundle branches -> Purkinje fibres",
                "mp3": "3. AV node delay ensures complete atrial emptying / ventricular filling before ventricular contraction",
            },
            {
                "context": "sympathetic stimulation during vigorous physical exercise (heart rate = 140 beats per minute)",
                "q1": "1. Identify the intrinsic pacemaker node located in the upper wall of the right atrium and state how sympathetic nerve impulses plus adrenaline alter its firing rate during exercise.",
                "q2": "2. Describe the sequence of specialized conducting structures that transmit the impulse from the Atrioventricular Node (AV node) through the Interventricular Septum to the apex of the ventricles.",
                "q3": "3. Explain why ventricular contraction must begin at the apex of the heart and spread upward toward the semilunar valves.",
                "a1": "1. The Sinoatrial Node (SA node); sympathetic nerve stimulation and adrenaline increase the frequency of spontaneous depolarization at the SA node, accelerating heart rate and cardiac output to supply more oxygenated blood to active muscles.",
                "a2": "2. The impulse passes from the Atrioventricular Node (AV node) into the Bundle of His (atrioventricular bundle) inside the Interventricular Septum, splits into left and right bundle branches toward the apex, and radiates through the Purkinje fibres.",
                "a3": "3. Contracting from the apex upward squeezes blood efficiently toward the superiorly located pulmonary artery and aorta (through the semilunar valves) rather than trapping blood at the bottom of the ventricles.",
                "mp1": "1. Sinoatrial Node (SA node); sympathetic stimulation / adrenaline increases impulse firing rate",
                "mp2": "2. Pathway: AV node -> Bundle of His in interventricular septum -> bundle branches -> Purkinje fibres",
                "mp3": "3. Bottom-up (apex to base) ventricular contraction forces blood upward into the aorta and pulmonary artery",
            },
            {
                "context": "clinical cardiology assessment of intrinsic conduction vs artificial pacemaker placement",
                "q1": "1. Distinguish between the anatomical location and physiological role of the Sinoatrial Node (SA node) versus the Atrioventricular Node (AV node).",
                "q2": "2. If the Bundle of His in the Interventricular Septum is blocked, explain how the coordination between atrial systole and ventricular systole is disrupted.",
                "q3": "3. Name the specialized conducting fibres that distribute the electrical impulse throughout the thick muscular walls of the left and right ventricles.",
                "a1": "1. The Sinoatrial Node (SA node) is in the upper right atrial wall and initiates each heartbeat (primary pacemaker), whereas the Atrioventricular Node (AV node) is at the inferior junction of the atria/interatrial septum and delays then relays the impulse to the ventricles.",
                "a2": "2. Electrical impulses from the atria cannot cross the fibrous ring into the ventricles via the Interventricular Septum, so the atria and ventricles beat independently (atrioventricular heart block) with reduced ventricular rate.",
                "a3": "3. Purkinje fibres (arising from the left and right bundle branches of the Bundle of His).",
                "mp1": "1. SA node (upper right atrium, initiates impulse) vs AV node (atrioventricular junction, delays and relays impulse)",
                "mp2": "2. Impulses blocked from reaching ventricles through septum; atria and ventricles contract asynchronously",
                "mp3": "3. Purkinje fibres distribute the impulse through the ventricular myocardium",
            },
        ]
        sc = pacemaker_scenarios[seed % len(pacemaker_scenarios)]
        question_text = (
            f"Refer to the coronal cross-section of the human heart showing the intrinsic cardiac conduction system "
            f"during a {sc['context']} "
            f"(Sinoatrial Node, Atrioventricular Node, and Interventricular Septum).\n\n"
            f"{sc['q1']}\n"
            f"{sc['q2']}\n"
            f"{sc['q3']}"
        )
        ans_str = f"{sc['a1']}\n{sc['a2']}\n{sc['a3']}"
        memo = ans_str
        marking_points = [
            {"point": 1, "desc": sc["mp1"]},
            {"point": 2, "desc": sc["mp2"]},
            {"point": 3, "desc": sc["mp3"]},
        ]
        tier_1 = "The SA node initiates the wave across the atria; the AV node relays it into the interventricular septum."
        tier_2 = "After the AV node, specialized fibres (Bundle of His and Purkinje fibres) conduct the impulse to the apex of the ventricles."
        tier_3 = ans_str
        misconceptions = ["atria_ventricle_swap"]
        marks = 4
        default_view = "textbook"
        lo_id = "LS10.T2.TSA.CARDIAC_CYCLE"

    elif archetype == "blood_vessel_direction":
        oxy_state = "Deoxygenated" if ("pulmonary_artery" in target_a["key"] or "vena_cava" in target_a["key"]) else "Oxygenated"
        specimen_num = (seed % 97) + 1
        question_text = (
            f"In anatomical cardiac investigation #{specimen_num}:\n"
            f"1. Name the major blood vessel indicated by Pin A.\n"
            f"2. State whether blood inside vessel A is oxygenated or deoxygenated.\n"
            f"3. Name the blood vessel indicated by Pin B and state its function."
        )
        ans_str = (
            f"1. {target_a['name']}\n"
            f"2. {oxy_state} blood\n"
            f"3. {target_b['name']}: {target_b['description']}"
        )
        memo = ans_str
        marking_points = [
            {"point": 1, "desc": f"1. Identifies Pin A: {target_a['name']}"},
            {"point": 2, "desc": f"2. Identifies oxygenation state: {oxy_state} blood"},
            {"point": 3, "desc": f"3. Identifies Pin B ({target_b['name']}) and its function: {target_b['description']}"},
        ]
        tier_1 = "Vessels exiting the ventricles are arteries; vessels entering atria are veins."
        tier_2 = "Pulmonary artery is the exception carrying deoxygenated blood to the lungs; aorta carries oxygenated blood to the body."
        tier_3 = ans_str
        misconceptions = ["pulmonary_artery_carries_oxygenated", "left_right_orientation_flip"]
        marks = 3
        default_view = "flow"
        lo_id = "NS9.T1.CRS.HEART_CIRCULATION" if grade == 9 else "LS10.T2.TSA.HEART_ANATOMY"

    else:  # chamber_differentiation / identification_adaptation
        specimen_num = (seed % 97) + 1
        question_text = (
            f"In anatomical cardiac investigation #{specimen_num}:\n"
            f"1. Identify the cardiac chamber indicated by Pin A.\n"
            f"2. Identify the cardiac chamber indicated by Pin B.\n"
            f"3. Account for the difference in muscular wall thickness between the left and right ventricles."
        )
        ans_str = (
            f"1. {target_a['name']}\n"
            f"2. {target_b['name']}\n"
            f"3. The left ventricle has a much thicker muscular myocardium wall because it must pump blood under high hydrostatic pressure through the systemic circulation to the entire body, whereas the right ventricle only pumps blood a short distance to the lungs under lower pressure."
        )
        memo = ans_str
        marking_points = [
            {"point": 1, "desc": f"1. Identifies Pin A: {target_a['name']}"},
            {"point": 2, "desc": f"2. Identifies Pin B: {target_b['name']}"},
            {"point": 3, "desc": "3. Left ventricle wall is thicker to generate high pressure for systemic circulation vs low-pressure pulmonary circuit"},
        ]
        tier_1 = "View the diagram as if facing a patient: the patient's right is on your left."
        tier_2 = "The left ventricle forms the apex and has a wall 3 times thicker than the right ventricle."
        tier_3 = ans_str
        misconceptions = ["left_right_orientation_flip", "atria_ventricle_swap"]
        marks = 4
        default_view = "textbook"
        lo_id = "NS9.T1.CRS.HEART_CIRCULATION" if grade == 9 else "LS10.T2.TSA.HEART_ANATOMY"

    resolved_view = view or ("exam" if str(mode).lower() == "exam" else default_view)

    diagram_spec = {
        "diagram_role": "identify" if client_pins else "context",
        "kind": "bio_diagram",
        "image_type": "human_heart",
        "master": "heart",
        "view": resolved_view,
        "grade_mask": grade_str,
        "state": active_state,
        "pins": client_pins,
        "landmarks": client_landmarks,
        "viewBox": HEART_DATA["viewBox"],
    }

    return {
        "id": f"ns{grade}_heart_{seed}",
        "question_id": f"ns{grade}_heart_{seed}",
        "subject": "Natural Sciences" if grade == 9 else "Life Sciences",
        "grade": grade,
        "term": 1 if grade == 9 else 2,
        "topic": "Circulatory and respiratory systems" if grade == 9 else "Transport systems in animals",
        "subskill": archetype,
        "learning_objective_id": lo_id,
        "question_text": question_text,
        "question": question_text,
        "prompt": question_text,
        "prompt_latex": question_text,
        "correct_answer": ans_str,
        "final_answer": ans_str,
        "answer_latex": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "ideal_answer": ans_str,
        "expected_answer_type": "text",
        "marking_memo": memo,
        "marking_points": marking_points,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": f"mp{p['point']}", "desc": p["desc"], "marks": 1, "editable": True}
                for p in marking_points
            ],
        },
        "hints": {
            "tier_1": tier_1,
            "tier_2": tier_2,
            "tier_3": tier_3,
        },
        "misconception_tags": misconceptions,
        "keywords": ["heart", "atrium", "ventricle", "aorta", "pulmonary", "valve", "septum"],
        "caps_weight_percent": 20,
        "suggested_duration_mins": 4,
        "marks": marks,
        "modality": "bio_diagram",
        "diagram_spec": diagram_spec,
        "simulearn_script": _build_cardiac_cycle_simulearn_script(
            target_a["name"],
            target_b["name"] if target_b else None,
        ),
        "_server_verification": server_target_refs,
    }


def generate(
    seed: Optional[int] = None,
    count: int = 1,
    grade: Any = 9,
    mode: str = "assessment",
    subskill: Optional[str] = None,
    view: Optional[str] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    """Universal generator interface returning a list of questions."""
    grade_num = int("".join(ch for ch in str(grade) if ch.isdigit()) or "9")
    questions = []
    base_seed = int(seed) if seed is not None else 1001
    for i in range(count):
        sub_seed = base_seed * 1000 + i
        questions.append(
            generate_heart_question(
                seed=sub_seed,
                grade=grade_num,
                mode=mode,
                subskill=subskill,
                view=view,
            )
        )
    return questions


def mark_heart_answer(user_answer: str, target_ref_entry: Dict[str, Any]) -> Dict[str, Any]:
    """Server-side verification against accepted South African curriculum synonym lexicon."""
    cleaned = user_answer.strip().lower()
    synonyms = [s.lower() for s in target_ref_entry.get("synonyms", [])]
    is_correct = any(syn in cleaned for syn in synonyms)
    return {
        "is_correct": is_correct,
        "canonical_name": target_ref_entry.get("name"),
        "matched": is_correct,
    }
