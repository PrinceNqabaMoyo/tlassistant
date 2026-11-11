"""Life Sciences Grade 11 Term 2: Photosynthesis Generator.

Covers:
- Chloroplast ultrastructure: Double membrane, thylakoids/grana, and stroma.
- Light-dependent phase: Photolysis of water, production of ATP and NADPH, release of oxygen.
- Light-independent phase (Calvin cycle): Fixation of carbon dioxide, utilization of ATP and NADPH, glucose synthesis.
- Limiting factors: Carbon dioxide concentration, light intensity, and temperature (enzyme denaturation).
- Practical investigations: Starch test, destarching, verifying requirements (light, chlorophyll, CO2).
- Greenhouse crop optimization and atmospheric carbon balance.
- Leaf transverse section integration via 3-layer anti-leak diagram plate.

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from app.utils.life_sciences.plant_physiology_builders import build_plant_leaf_question


def _fmt_sa(val: float | int, decimals: int = 1) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_photosynthesis_phases(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Biochemical pathways of light-dependent vs light-independent phases."""
    temp_c = r.choice([20, 25, 30, 35, 45, 52])
    co2_ppm = r.choice([250, 350, 420, 800, 1000])
    light_percent = r.choice([25, 50, 75, 100])
    qid = _make_id("ls11_photo_phases", seed, idx)

    if mode == "elementary_chloroplast_sites":
        prompt = (
            "Photosynthesis takes place within the chloroplast in two sequential biochemical phases.\n\n"
            "1. Name the exact internal site in the chloroplast where the light-dependent phase occurs.\n"
            "2. Name the site where the light-independent phase (Calvin cycle) takes place.\n"
            "3. State the two energy-rich carrier molecules produced during the light phase that are required by the Calvin cycle."
        )
        ans_str = "1. Thylakoid membranes / Grana; 2. Stroma; 3. ATP and NADPH"
        memo = (
            "1. Light-dependent phase site: Thylakoid membranes / Grana. [1]\n"
            "2. Light-independent phase site: Liquid stroma. [1]\n"
            "3. Energy-rich molecules: ATP and NADPH (reduced NADP). [2]"
        )
        hints = {
            "tier_1": "Recall the disc stacks (grana) and the fluid matrix (stroma) inside chloroplasts.",
            "tier_2": "Chlorophyll pigments are in grana. Photolysis yields ATP and NADPH. Carbon fixation occurs in the stroma.",
            "tier_3": "1. Grana/Thylakoids. 2. Stroma. 3. ATP and NADPH.",
        }
        marks = 4
        misconceptions = ["confused_grana_with_stroma", "atp_nadph_identity_error"]
    else:
        # Full compound question on phases, equations, and limiting factor dynamics
        prompt = (
            f"An investigation was set up in an agricultural research station to maximize tomato crop yield in a controlled greenhouse.\n"
            f"The environmental temperature was set to ${temp_c}^\\circ\\text{{C}}$, $\\text{{CO}}_2$ concentration to "
            f"${co2_ppm}\\text{{ ppm}}$, and supplemental light intensity to ${light_percent}\\%$.\n\n"
            f"1. Write down the balanced chemical equation for photosynthesis.\n"
            f"2. Tabulate two differences between the light-dependent phase and the light-independent phase regarding their exact cellular location and primary inputs.\n"
            f"3. Explain what happens to the rate of photosynthesis if the greenhouse temperature reaches $50^\\circ\\text{{C}}$ while $\\text{{CO}}_2$ and light remain optimal."
        )
        ans_str = (
            "1. 6CO2 + 6H2O -> C6H12O6 + 6O2; "
            "2. Comparative table: Light phase (Grana, inputs Light + H2O) vs Calvin cycle (Stroma, inputs CO2 + ATP + NADPH); "
            "3. Rate drops towards zero because high temperature denatures photosynthetic enzymes (e.g. RuBisCO)."
        )
        memo = (
            "1. Balanced chemical equation [3]:\n"
            "   $$6\\text{CO}_2 + 6\\text{H}_2\\text{O} \\xrightarrow{\\text{Light, Chlorophyll}} \\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2$$\n"
            "   (1 mark for correct reactants, 1 mark for correct products, 1 mark for balancing).\n"
            "2. Comparison Table [4]:\n"
            "   - Light-dependent phase: Occurs in Thylakoids / Grana [1]; Requires Radiant energy and Water [1].\n"
            "   - Light-independent phase: Occurs in the Stroma [1]; Requires Carbon dioxide, ATP, and NADPH [1].\n"
            "3. High temperature effect [2]: At 50°C, extreme thermal kinetic energy denatures the enzymes (such as RuBisCO) [1], "
            "altering the shape of their active sites so that substrates can no longer bind and the Calvin cycle stops [1]."
        )
        hints = {
            "tier_1": "Ensure the formula is balanced: 6 carbons, 12 hydrogens, 18 oxygens on each side. High temperatures affect enzymes.",
            "tier_2": "Light phase = Grana (H2O + light). Dark phase = Stroma (CO2 + ATP + NADPH). Enzymes denature above 40-45°C.",
            "tier_3": "1. 6CO2 + 6H2O -> C6H12O6 + 6O2. 2. Grana vs Stroma; H2O+Light vs CO2+ATP+NADPH. 3. Enzyme denaturation.",
        }
        marks = 9
        misconceptions = ["unbalanced_photosynthesis_equation", "confused_grana_with_stroma", "forgot_temperature_enzyme_denaturation"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 10,
        "subskill": "chloroplast_phases",
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "question_text": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Balanced chemical equation for photosynthesis", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": "Tabulation of light vs dark phases", "marks": 4, "editable": True},
                {"id": "mp_3", "desc": "Thermal enzyme denaturation explanation", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "unbalanced_formula", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_starch_investigation(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Experimental investigations: Starch testing and verifying photosynthetic requirements."""
    plant = r.choice(["variegated Coleus", "Geranium", "Impatiens plant", "bean plant"])
    requirement = r.choice(["radiant light energy", "chlorophyll pigment", "carbon dioxide"])
    qid = _make_id("ls11_starch_test", seed, idx)

    if requirement == "radiant light energy":
        investigation_desc = "One leaf was partially covered on both upper and lower surfaces with an opaque strip of black cardboard."
        covered_result = "remains yellowish-brown (no starch produced)"
        uncovered_result = "turns dark blue-black (starch produced)"
        control_explanation = "The uncovered green part of the leaf served as the experimental control."
    elif requirement == "chlorophyll pigment":
        investigation_desc = "A variegated leaf with white outer margins and a green central zone was tested for starch."
        covered_result = "white margins remain yellowish-brown"
        uncovered_result = "green central zone turns dark blue-black"
        control_explanation = "The green pigmented zone with chlorophyll acted as the control."
    else:  # carbon dioxide
        investigation_desc = "The plant was enclosed inside a clear bell jar containing sodium hydroxide pellets (which absorb CO2)."
        covered_result = "remains yellowish-brown throughout"
        uncovered_result = "turns blue-black only in a control bell jar with sodium bicarbonate"
        control_explanation = "A second plant exposed to normal atmospheric CO2 served as the positive control."

    if mode == "elementary_destarching":
        prompt = (
            f"Before starting any photosynthesis experiment using a potted {plant}, the plant must be placed in a dark cupboard for 48 hours.\n\n"
            "1. State the biological term for this procedure.\n"
            "2. Explain why this step is essential for ensuring experimental validity."
        )
        ans_str = "1. Destarching; 2. Ensures all pre-existing starch is metabolised so any starch detected is produced solely during the experiment."
        memo = (
            "1. Procedure: Destarching the plant. [1]\n"
            "2. Validity rationale [2]: Keeping the plant in darkness forces it to metabolise and transport away all pre-existing starch stored in its leaves [1]. "
            "This ensures that any starch detected at the end of the experiment was synthesized solely during the experimental light exposure period [1]."
        )
        hints = {
            "tier_1": "What happens to stored food when a plant has no light to make new sugars?",
            "tier_2": "The plant hydrolyses starch into glucose for cellular respiration. This is called destarching.",
            "tier_3": "1. Destarching. 2. Ensures any starch found was synthesized solely during the experiment.",
        }
        marks = 3
        misconceptions = ["forgot_destarching_rationale", "confused_destarching_with_dehydration"]
    else:
        prompt = (
            f"Life Sciences learners investigated whether **{requirement}** is necessary for photosynthesis using a {plant}.\n"
            f"The plant was first destarched for 48 hours. {investigation_desc}\n"
            f"After 6 hours of sunlight exposure, the leaf was boiled in water, boiled in an ethanol water bath, rinsed in warm water, "
            f"and tested with iodine solution.\n\n"
            f"1. Explain why the leaf was boiled in ethanol (alcohol).\n"
            f"2. Predict the colour change observed in the tested areas.\n"
            f"3. Explain how the results prove that {requirement} is essential for photosynthesis.\n"
            f"4. State the safety precaution that must be observed when heating ethanol."
        )
        ans_str = (
            f"1. Dissolves and extracts green chlorophyll pigment; "
            f"2. Tested area without requirement: {covered_result}; Area with requirement: {uncovered_result}; "
            f"3. Starch was synthesized only where {requirement} was present; "
            f"4. Heat ethanol in a water bath using a hot plate; never expose to an open naked flame because ethanol is highly flammable."
        )
        memo = (
            "1. Ethanol extraction [2]: Boiling in ethanol dissolves and removes the green chlorophyll pigment [1], "
            "decolorizing the leaf so that subsequent iodine colour changes can be clearly seen [1].\n"
            f"2. Colour prediction [2]: Area lacking {requirement}: {covered_result} [1]; Area with {requirement}: {uncovered_result} [1].\n"
            f"3. Conclusion [2]: Starch (photosynthetic product) was detected solely in regions where {requirement} was available, "
            f"demonstrating that {requirement} is mandatory for carbohydrate synthesis [2].\n"
            "4. Safety precaution [1]: Ethanol is highly flammable; it must be heated in a hot water bath and never over a direct open flame. [1]"
        )
        hints = {
            "tier_1": "Chlorophyll masks iodine's colour change. Ethanol is flammable. Iodine turns blue-black with starch.",
            "tier_2": "Boiling in ethanol removes chlorophyll. Ethanol must be heated in a water bath. Without the factor, no starch forms (brown).",
            "tier_3": f"1. Extract chlorophyll. 2. Without factor: brown; with factor: blue-black. 3. Starch produced only with {requirement}. 4. Use water bath (flammable).",
        }
        marks = 7
        misconceptions = ["iodine_colour_inversion", "open_flame_alcohol_safety_error", "chlorophyll_removal_misunderstood"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 9,
        "subskill": "starch_test",
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "question_text": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Ethanol decolorization rationale", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Comparative iodine test colour predictions", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Experimental deduction linking product to requirement", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Flammability laboratory safety precaution", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master entry point for Grade 11 Photosynthesis."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = (seed + i) if seed is not None else r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("leaf_transverse_section", "palisade_photosynthesis", "plant_leaf", "leaf_adaptations_photosynthesis"):
            q = build_plant_leaf_question(sub_seed, grade=11, mode=mode, subskill="tissue_identification")
        elif subskill in ("chloroplast_phases", "limiting_factors") or mode == "elementary_chloroplast_sites":
            q = _generate_photosynthesis_phases(sub_r, sub_seed, i, mode)
        elif subskill in ("starch_test", "destarching") or mode == "elementary_destarching":
            q = _generate_starch_investigation(sub_r, sub_seed, i, mode)
        else:
            # Alternating between phases, starch experiments, and leaf cross-section
            picker = (sub_seed + i) % 3
            if picker == 0:
                q = _generate_photosynthesis_phases(sub_r, sub_seed, i, mode)
            elif picker == 1:
                q = _generate_starch_investigation(sub_r, sub_seed, i, mode)
            else:
                q = build_plant_leaf_question(sub_seed, grade=11, mode=mode)

        questions.append(q)

    return questions


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)
