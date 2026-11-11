"""Grade 10 Life Sciences — Term 2: Transport Systems in Animals Topic Generator.

Strictly grounded in:
- curriculum_docs_auto/LifeSciences_Gr10/Term 2/05. Transport systems in animals.md
- curriculum_docs_auto/LifeSciences_Gr10/Syllabus.md

Topic-First Architecture:
- Owns the ordered curriculum subskills for Grade 10 Transport Systems in Animals:
  1. heart_external_and_internal_anatomy (calls reusable heart_generator with grade_mask='g10', view='textbook')
  2. cardiac_cycle_and_electrical_control (calls reusable heart_generator with grade_mask='g10', view='flow')
  3. open_closed_single_double_circulation (open vs. closed, pulmonary vs. systemic, hepatic portal & coronary vessels)
  4. blood_vessel_histology_and_function (tunica intima/media/externa, lumen, pressure, valves)
  5. electrical_pacemaker_and_ecg (calls reusable heart_generator with grade_mask='g10', view='exam')
  6. lymphatic_system_and_cardiovascular_diseases (lymphatic return, immunity, hypertension, stents, bypass, pacemakers)
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.heart_generator import generate_heart_question

TOPIC_NAME = "Transport systems in animals"

ORDERED_SUBSKILLS = [
    "heart_external_and_internal_anatomy",
    "cardiac_cycle_and_electrical_control",
    "open_closed_single_double_circulation",
    "blood_vessel_histology_and_function",
    "electrical_pacemaker_and_ecg",
    "lymphatic_system_and_cardiovascular_diseases",
]


def _gen_open_closed_double_circulation(seed: int, mode: str = "assessment") -> Dict[str, Any]:
    r = random.Random(seed)
    variant = r.choice(["double_vs_single", "organ_vessels"])
    if variant == "double_vs_single":
        question_text = (
            "Animals exhibit either open or closed circulatory systems, and vertebrate closed systems may follow "
            "single or double circulation pathways.\n\n"
            "1. Distinguish between an open circulatory system (e.g., insects/crabs) and a closed circulatory system (e.g., mammals).\n"
            "2. Explain why the mammalian circulatory system is described as a 'double' circulatory system, naming its two circuits.\n"
            "3. State one major physiological advantage of a four-chambered double circulatory system over a two-chambered single circulatory system."
        )
        ans_str = (
            "1. In an open circulatory system blood is pumped into a body cavity (haemocoel) where it bathes organs directly at low speed; in a closed circulatory system blood remains entirely enclosed within blood vessels; "
            "2. Blood passes through the heart twice during one complete circuit of the body: the pulmonary circuit (heart -> lungs -> heart) and the systemic circuit (heart -> body tissues -> heart); "
            "3. Oxygenated and deoxygenated blood are completely separated by the septum and oxygenated blood is re-pressurised by the left ventricle for rapid delivery to metabolically active tissues."
        )
        memo = (
            "1. Open: blood enters body cavity bathing organs directly; Closed: blood remains confined inside blood vessels [1].\n"
            "2. Pulmonary circulation and systemic circulation (passes through heart twice per full cycle) [2].\n"
            "3. No mixing of oxygenated and deoxygenated blood / maintains high systemic blood pressure [1]."
        )
        points = [
            {"point": 1, "desc": "Distinguishes open (body cavity) vs. closed (confined to vessels) circulation"},
            {"point": 2, "desc": "Names pulmonary and systemic circuits of double circulation"},
            {"point": 3, "desc": "Explains prevention of oxygenated/deoxygenated mixing and high systemic pressure"},
        ]
    else:
        question_text = (
            "In the human systemic circulatory system, specialised arteries and veins supply and drain major organs.\n\n"
            "1. Name the blood vessel that transports nutrient-rich blood directly from the small intestine to the liver before returning to the heart.\n"
            "2. Name the arteries that supply the heart muscle (myocardium) itself with oxygenated blood.\n"
            "3. Name the artery that supplies blood containing metabolic waste to the kidney and the vein that drains filtered blood from the kidney."
        )
        ans_str = (
            "1. Hepatic portal vein; "
            "2. Coronary arteries; "
            "3. Renal artery (supplies kidney) and renal vein (drains kidney)."
        )
        memo = (
            "1. Hepatic portal vein [1].\n"
            "2. Coronary arteries [1].\n"
            "3. Renal artery [1] and renal vein [1]."
        )
        points = [
            {"point": 1, "desc": "Identifies the hepatic portal vein"},
            {"point": 2, "desc": "Identifies the coronary arteries supplying the myocardium"},
            {"point": 3, "desc": "Identifies renal artery and renal vein"},
        ]

    return {
        "id": f"ls10_tsa_circ_{seed}",
        "question_id": f"ls10_tsa_circ_{seed}",
        "subject": "Life Sciences",
        "grade": 10,
        "term": 2,
        "topic": TOPIC_NAME,
        "subskill": "open_closed_single_double_circulation",
        "learning_objective_id": "LS10.T2.TSA.CIRCULATION_PATHWAYS",
        "question_text": question_text,
        "question": question_text,
        "prompt": question_text,
        "prompt_latex": question_text,
        "final_answer": ans_str,
        "answer_latex": ans_str,
        "sample_answer": ans_str,
        "ideal_answer": ans_str,
        "expected_answer_type": "text",
        "marking_memo": memo,
        "marking_points": points,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": f"mp{p['point']}", "desc": p["desc"], "marks": 1, "editable": True}
                for p in points
            ],
        },
        "hints": {
            "tier_1": "Compare how blood travels to the lungs for oxygenation versus to the rest of the body's organs.",
            "tier_2": "'Hepatic' refers to the liver, 'renal' refers to the kidneys, and 'coronary' refers to the heart muscle itself.",
            "tier_3": ans_str,
        },
        "misconception_tags": ["pulmonary_vs_systemic_circuit_inversion", "hepatic_vein_vs_portal_vein_confusion"],
        "keywords": ["pulmonary", "systemic", "double circulation", "hepatic portal vein", "coronary artery", "renal artery"],
        "caps_weight_percent": 20,
        "suggested_duration_mins": 4,
        "marks": 4,
        "mode": mode,
    }


def _gen_blood_vessel_histology(seed: int, mode: str = "assessment") -> Dict[str, Any]:
    r = random.Random(seed)
    variant = r.choice(["layers_and_valves", "artery_vs_vein_mechanics", "capillary_specialization"])
    if variant == "layers_and_valves":
        question_text = (
            "The walls of mammalian arteries and veins are composed of three distinct tissue layers surrounding the central lumen.\n\n"
            "1. Name the innermost epithelial lining of a blood vessel and state how this single layer is structurally suited to form blood capillaries.\n"
            "2. Compare the middle muscular and elastic layer (tunica media) and lumen size of an artery with that of a vein.\n"
            "3. Explain how skeletal muscle contraction and semilunar valves work together to return blood in veins from the legs to the heart against gravity."
        )
        ans_str = (
            "1. Squamous endothelium (single layer of flat squamous epithelial cells); its one-cell-thick barrier provides a very short diffusion distance for rapid exchange of oxygen, nutrients, and wastes in capillaries; "
            "2. An artery has a much thicker middle layer of smooth muscle and elastic fibres and a narrower lumen than a vein to withstand and recoil under high systolic blood pressure; "
            "3. Contracting skeletal muscles squeeze adjacent thin-walled veins to push blood upwards, while internal semilunar valves close whenever blood tries to flow backwards."
        )
        memo = (
            "1. Squamous endothelium [1]; one-cell-thick layer reduces diffusion distance in capillaries [1].\n"
            "2. Artery has thicker smooth muscle/elastic layer and narrower lumen than a vein [1].\n"
            "3. Skeletal muscles compress veins to propel blood forward while semilunar valves prevent backflow [1]."
        )
        points = [
            {"point": 1, "desc": "Identifies squamous endothelium and explains short diffusion distance"},
            {"point": 2, "desc": "Compares thicker muscular/elastic wall and narrower lumen of artery vs. vein"},
            {"point": 3, "desc": "Explains skeletal muscle pump and one-way semilunar valves in veins"},
        ]
    elif variant == "artery_vs_vein_mechanics":
        question_text = (
            "Blood pressure varies significantly between the arterial and venous systems of mammals.\n\n"
            "1. Explain why arteries require a thick layer of elastic fibres in the tunica media.\n"
            "2. Why do veins have a wider lumen and thinner walls than arteries of corresponding diameter?\n"
            "3. Explain why veins possess internal valves while healthy systemic arteries do not."
        )
        ans_str = (
            "1. Elastic fibres allow arteries to stretch under high systolic pressure and recoil during diastole to maintain continuous blood flow; "
            "2. Blood in veins flows under low hydrostatic pressure, so wide lumens offer low resistance to returning blood; "
            "3. Venous pressure is insufficient to overcome gravity and prevent retrograde flow, requiring one-way valves, whereas arterial flow is driven forward by high ventricular pressure."
        )
        memo = (
            "1. Elastic recoil maintains continuous flow and withstands systolic surges [1].\n"
            "2. Wide lumen reduces vascular resistance under low pressure [1].\n"
            "3. Low pressure requires one-way valves to prevent pooling, unlike arterial high pressure [2]."
        )
        points = [
            {"point": 1, "desc": "Explains elastic recoil and high systolic pressure absorption"},
            {"point": 2, "desc": "Relates wide venous lumen to low vascular resistance"},
            {"point": 3, "desc": "Contrasts one-way venous valves with high-pressure arterial pumping"},
        ]
    else:
        question_text = (
            "Capillaries are the microscopic site of internal exchange between blood and tissue fluid.\n\n"
            "1. Describe the histological structure of a capillary wall.\n"
            "2. Explain how the total cross-sectional area of the capillary bed affects the velocity of blood flow.\n"
            "3. What physiological advantage is gained from slow blood flow through capillary networks?"
        )
        ans_str = (
            "1. A single layer of flattened squamous endothelial cells resting on a basal lamina with intercellular clefts; "
            "2. The immense branching of millions of capillaries creates an enormous total cross-sectional area, causing blood flow velocity to drop dramatically; "
            "3. Slow velocity maximizes contact time for diffusion of respiratory gases (O2, CO2), glucose, and metabolic wastes across the endothelium."
        )
        memo = (
            "1. Single layer of flat endothelial cells on basal lamina [1].\n"
            "2. Large total cross-sectional area drastically decreases blood velocity [1].\n"
            "3. Maximizes contact time for efficient diffusion of gases and nutrients [2]."
        )
        points = [
            {"point": 1, "desc": "Describes one-cell-thick endothelial wall"},
            {"point": 2, "desc": "Explains inverse relationship between total cross-sectional area and blood velocity"},
            {"point": 3, "desc": "States physiological advantage of slow transit time for diffusion"},
        ]

    return {
        "id": f"ls10_tsa_vessels_{seed}",
        "question_id": f"ls10_tsa_vessels_{seed}",
        "subject": "Life Sciences",
        "grade": 10,
        "term": 2,
        "topic": TOPIC_NAME,
        "subskill": "blood_vessel_histology_and_function",
        "learning_objective_id": "LS10.T2.TSA.BLOOD_VESSELS",
        "question_text": question_text,
        "question": question_text,
        "prompt": question_text,
        "prompt_latex": question_text,
        "final_answer": ans_str,
        "answer_latex": ans_str,
        "sample_answer": ans_str,
        "ideal_answer": ans_str,
        "expected_answer_type": "text",
        "marking_memo": memo,
        "marking_points": points,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": f"mp{p['point']}", "desc": p["desc"], "marks": 1, "editable": True}
                for p in points
            ],
        },
        "hints": {
            "tier_1": "Capillaries lack the outer fibrous and middle muscular coats, retaining only the innermost lining.",
            "tier_2": "Arteries receive high-pressure surges from ventricular systole; veins return blood under low pressure.",
            "tier_3": ans_str,
        },
        "misconception_tags": ["lumen_size_artery_vs_vein_inversion", "endothelium_vs_epidermis_confusion"],
        "keywords": ["squamous endothelium", "lumen", "smooth muscle", "elastic fibres", "semilunar valves", "capillaries"],
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "marks": 4,
        "mode": mode,
    }


def _gen_lymphatic_and_diseases(seed: int, mode: str = "assessment") -> Dict[str, Any]:
    r = random.Random(seed)
    focus = r.choice(["lymphatic", "cardiovascular_disease"])
    if focus == "lymphatic":
        question_text = (
            "The lymphatic circulatory system operates alongside the blood cardiovascular system.\n\n"
            "1. Explain how tissue fluid is formed at arterial capillary beds and how excess fluid is returned to the blood circulatory system as lymph.\n"
            "2. Name the main lymphatic duct that drains lymph from the lower body and left side into the left subclavian vein.\n"
            "3. State two vital physiological roles of the lymphatic system in the human body."
        )
        ans_str = (
            "1. High hydrostatic blood pressure forces plasma (minus large plasma proteins and red blood cells) out through capillary pores to bathe cells as tissue fluid; excess fluid drains into blind-ending lymph capillaries as lymph; "
            "2. Thoracic duct; "
            "3. Returns excess interstitial fluid/proteins to the bloodstream (preventing oedema) and defends the body against pathogens by producing/filtering lymphocytes in lymph nodes (plus absorbing digested fats via lacteals)."
        )
        memo = (
            "1. High capillary pressure filters plasma out as tissue fluid; excess drains into blind lymph vessels [1].\n"
            "2. Thoracic duct [1].\n"
            "3. Returns excess tissue fluid to blood AND immunity / lymphocyte production / fat transport [2]."
        )
        points = [
            {"point": 1, "desc": "Explains pressure filtration of plasma to tissue fluid and drainage into lymph vessels"},
            {"point": 2, "desc": "Identifies the thoracic duct"},
            {"point": 3, "desc": "States fluid return (preventing oedema) and immune defence / lipid transport"},
        ]
    else:
        question_text = (
            "Cardiovascular diseases are a major cause of morbidity globally and in South Africa.\n\n"
            "1. Explain the sequence of events by which atherosclerosis (cholesterol plaque build-up) in a coronary artery leads to a myocardial infarction (heart attack).\n"
            "2. Distinguish between a coronary stent and coronary bypass surgery as medical treatments for blocked coronary arteries.\n"
            "3. State the medical condition treated by implanting an artificial pacemaker."
        )
        ans_str = (
            "1. Fatty cholesterol plaques narrow or thrombose (clot) a coronary artery, cutting off oxygenated blood and glucose to a region of the cardiac muscle (myocardium), causing those heart muscle cells to die from oxygen starvation; "
            "2. A stent is a small expandable mesh tube inserted inside the narrowed coronary artery to hold it open, whereas bypass surgery grafts a healthy blood vessel from another part of the body to route blood around the blockage; "
            "3. Arrhythmia / bradycardia (failure or abnormality of the sinoatrial node pacemaker rhythm)."
        )
        memo = (
            "1. Plaque/clot blocks coronary artery -> deprives myocardium of oxygen/nutrients -> cardiac muscle tissue dies [2].\n"
            "2. Stent: mesh tube expanding blocked lumen; Bypass: grafted vessel routing blood around blockage [1].\n"
            "3. Arrhythmia / abnormal heart rhythm / SA node failure [1]."
        )
        points = [
            {"point": 1, "desc": "Explains coronary artery occlusion leading to myocardial hypoxia and cell death"},
            {"point": 2, "desc": "Distinguishes internal mesh stent from surgical vessel bypass graft"},
            {"point": 3, "desc": "Identifies arrhythmia / faulty SA node pacemaker"},
        ]

    return {
        "id": f"ls10_tsa_lymph_{seed}",
        "question_id": f"ls10_tsa_lymph_{seed}",
        "subject": "Life Sciences",
        "grade": 10,
        "term": 2,
        "topic": TOPIC_NAME,
        "subskill": "lymphatic_system_and_cardiovascular_diseases",
        "learning_objective_id": "LS10.T2.TSA.LYMPHATIC_DISEASES",
        "question_text": question_text,
        "question": question_text,
        "prompt": question_text,
        "prompt_latex": question_text,
        "final_answer": ans_str,
        "answer_latex": ans_str,
        "sample_answer": ans_str,
        "ideal_answer": ans_str,
        "expected_answer_type": "text",
        "marking_memo": memo,
        "marking_points": points,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": f"mp{p['point']}", "desc": p["desc"], "marks": 1, "editable": True}
                for p in points
            ],
        },
        "hints": {
            "tier_1": "Consider how blood plasma leaves capillaries and what happens if a coronary artery supplying the heart wall is blocked.",
            "tier_2": "Lymph vessels have blind ends and return fluid via the thoracic duct; coronary arteries feed the myocardium itself.",
            "tier_3": ans_str,
        },
        "misconception_tags": ["pulmonary_vs_coronary_occlusion_confusion", "lymph_pumped_by_heart_fallacy"],
        "keywords": ["lymph", "tissue fluid", "thoracic duct", "coronary artery", "myocardium", "stent", "pacemaker"],
        "caps_weight_percent": 15,
        "suggested_duration_mins": 4,
        "marks": 4,
        "mode": mode,
    }


def generate_topic_question(
    seed: int,
    mode: str = "assessment",
    subskill: Optional[str] = None,
    view: Optional[str] = None,
) -> Dict[str, Any]:
    """Generate a single question from the ordered Grade 10 Transport Systems in Animals subskills."""
    norm_sub = (subskill or "").strip().lower()

    if not norm_sub:
        idx = abs(int(seed) - 1001) if int(seed) < 100000 else abs(int(seed))
        norm_sub = ORDERED_SUBSKILLS[idx % len(ORDERED_SUBSKILLS)]

    if "valve" in norm_sub or norm_sub in ("heart_external_and_internal_anatomy", "chambers", "identification_adaptation"):
        return generate_heart_question(seed=seed, grade=10, mode=mode, subskill="valves", view=view or "textbook")
    if "cardiac" in norm_sub or "cycle" in norm_sub:
        return generate_heart_question(seed=seed, grade=10, mode=mode, subskill="cardiac_cycle", view=view or "flow")
    if "node" in norm_sub or "pacemaker" in norm_sub or "ecg" in norm_sub:
        return generate_heart_question(seed=seed, grade=10, mode=mode, subskill="nodes", view=view or "exam")
    if "circulat" in norm_sub or "open_closed" in norm_sub:
        return _gen_open_closed_double_circulation(seed=seed, mode=mode)
    if "blood_vessel" in norm_sub or "histology" in norm_sub:
        return _gen_blood_vessel_histology(seed=seed, mode=mode)
    if "lymph" in norm_sub or "disease" in norm_sub:
        return _gen_lymphatic_and_diseases(seed=seed, mode=mode)

    return generate_heart_question(seed=seed, grade=10, mode=mode, subskill="valves", view=view or "textbook")


def generate(
    seed: Optional[int] = None,
    count: int = 1,
    grade: Any = 10,
    mode: str = "assessment",
    subskill: Optional[str] = None,
    view: Optional[str] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    """Universal topic generator entry point for Grade 10 Transport Systems in Animals."""
    base_seed = int(seed) if seed is not None else 1001
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = base_seed * 1000 + i
        if subskill:
            chosen_subskill = subskill
        else:
            start_offset = abs(base_seed - 1001) % len(ORDERED_SUBSKILLS)
            chosen_subskill = ORDERED_SUBSKILLS[(start_offset + i) % len(ORDERED_SUBSKILLS)]

        questions.append(
            generate_topic_question(
                seed=sub_seed,
                mode=mode,
                subskill=chosen_subskill,
                view=view,
            )
        )
    return questions
