"""Life Sciences & Senior Phase Natural Sciences — Photosynthesis & Cellular Respiration.
Covers the biochemical pathways of radiant energy conversion, ATP yield, limiting factors, and cellular metabolism.
Strictly complies with the 6-Pillar Generator Contract:
- Multi-grade vertical strand (Gr8 NS, Gr11 LS)
- Procedural seeded PRNG determinism (random.Random(seed))
- Atomic elementary sub-drills (mode="compound" | "elementary_*")
- Standardized misconception taxonomy
- Teacher-editable marking schema with [M] and [A] marks
- Deterministic 3-tier pre-baked hints
- South African comma decimal convention (",")
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_sa(val: float | int, decimals: int = 1) -> str:
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_gr8_photosynthesis(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 8 Natural Sciences: Basic concepts, word equation, and starch test experiment."""
    plant_name = r.choice(["Geranium", "Variegated Hibiscus", "Elodea (Pondweed)", "Bean seedling"])
    hours_dark = r.choice([24, 48, 72])
    test_reagent = "iodine solution"

    qid = _make_id("ns8_photosynthesis", seed, idx)

    if mode == "elementary_starch_test":
        prompt = (
            f"A Grade 8 learner sets up an experiment to test a leaf from a {plant_name} plant for the presence of starch.\n"
            f"The leaf is boiled in water for 5 minutes, then boiled in a water bath with alcohol, rinsed in warm water, "
            f"and placed on a white tile. A few drops of {test_reagent} are added.\n\n"
            f"1. Explain why the leaf was boiled in alcohol.\n"
            f"2. State the expected colour change of {test_reagent} if starch is present in the leaf."
        )
        ans_str = "1. To extract/remove the green chlorophyll; 2. Brown to blue-black"
        memo = (
            "1. Boiling in alcohol removes the green chlorophyll pigment so that the color change can be clearly observed. [2]\n"
            "2. Positive starch test: Yellowish-brown turns blue-black. [2]"
        )
        hints = {
            "tier_1": "Think about how the green colour of the leaf might affect seeing the reagent's colour change.",
            "tier_2": "Alcohol dissolves and removes chlorophyll; iodine solution turns dark blue-black in the presence of starch.",
            "tier_3": "Answer: 1. Extract chlorophyll; 2. Changes from brown to blue-black.",
        }
        marks = 4
    else:
        # Full compound Gr8 question
        prompt = (
            f"A potted {plant_name} was placed in a dark cupboard for {hours_dark} hours before an investigation.\n"
            f"One leaf was partially covered with a strip of black cardboard on both sides and exposed to sunlight for 6 hours.\n\n"
            f"1. What is the purpose of placing the plant in a dark cupboard for {hours_dark} hours?\n"
            f"2. Write down the complete word equation for photosynthesis.\n"
            f"3. Predict the colour of the covered part versus the uncovered part of the leaf after performing the starch test with {test_reagent}."
        )
        ans_str = (
            f"1. Destarch the plant; "
            f"2. Carbon dioxide + Water + Light -> Glucose + Oxygen; "
            f"3. Covered part remains brown/yellow, uncovered part turns blue-black"
        )
        memo = (
            f"1. To destarch the leaf / ensure any starch detected was produced solely during the 6 hours of light exposure. [2]\n"
            f"2. Carbon dioxide + Water + (radiant energy / sunlight) -> Glucose + Oxygen [3]\n"
            f"3. Covered part: Remains yellowish-brown (no starch produced without light); Uncovered part: Turns blue-black (starch produced). [2]"
        )
        hints = {
            "tier_1": "Destarching ensures prior starch is metabolized. Photosynthesis requires light, carbon dioxide, and water.",
            "tier_2": "The word equation is: Carbon dioxide + Water -> Glucose + Oxygen. Covered regions cannot photosynthesize.",
            "tier_3": "1. Destarch the plant. 2. Carbon dioxide + Water -> Glucose + Oxygen. 3. Covered = brown; Uncovered = blue-black.",
        }
        marks = 7

    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 15,
        "suggested_duration_mins": 8,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["forgot_destarching_rationale", "iodine_positive_colour_inversion", "confused_reactants_and_products"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Destarching explanation", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Photosynthesis word equation", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Starch test comparative prediction", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "omitted_radiant_energy", "penalty": 0}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr11_photosynthesis_phases(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 11 Life Sciences: Light and dark phases, chloroplast anatomy, and chemical equation."""
    temp_c = r.choice([20, 25, 30, 35, 45, 50])
    co2_ppm = r.choice([200, 300, 400, 800])
    light_percent = r.choice([30, 50, 75, 100])

    qid = _make_id("ls11_photosynthesis", seed, idx)

    if mode == "elementary_light_phase_sites":
        prompt = (
            "Photosynthesis in green plants occurs in two distinct, sequential phases inside the chloroplast.\n\n"
            "1. Name the exact site in the chloroplast where the light-dependent phase takes place.\n"
            "2. State the two essential high-energy energy-carrier molecules produced during the light-dependent phase that are utilized in the Calvin cycle (light-independent phase)."
        )
        ans_str = "1. Thylakoids / Grana; 2. ATP and NADPH"
        memo = (
            "1. Light-dependent phase takes place in the thylakoids / grana. [1]\n"
            "2. High-energy molecules: ATP and NADPH (reduced NADP). [2]"
        )
        hints = {
            "tier_1": "Recall the two main internal structures of the chloroplast: the disc stacks and the surrounding liquid matrix.",
            "tier_2": "The chlorophyll pigments are embedded in the thylakoid membranes of grana. Photolysis produces ATP and NADPH.",
            "tier_3": "1. Thylakoids/Grana. 2. ATP and NADPH.",
        }
        marks = 3
    elif mode == "elementary_limiting_factor_graph":
        prompt = (
            f"A greenhouse farmer measures the rate of photosynthesis in tomato plants at different temperatures.\n"
            f"The rate increases steadily from $15^\\circ\\text{{C}}$ up to $35^\\circ\\text{{C}}$, but drops sharply towards zero at ${temp_c}^\\circ\\text{{C}}$.\n\n"
            f"Explain, in terms of biochemical enzyme activity, why the rate of photosynthesis decreases drastically when the temperature exceeds $40^\\circ\\text{{C}}$."
        )
        ans_str = "Enzymes controlling the Calvin cycle (e.g. RuBisCO) denature at high temperatures, changing active site shape."
        memo = (
            "At temperatures above 40°C, the enzymes that catalyze photosynthesis (such as RuBisCO in the Calvin cycle) "
            "denature [1]. The shape of the active site is altered [1], so substrate molecules can no longer bind and catalytic function is lost [1]."
        )
        hints = {
            "tier_1": "Photosynthetic reactions in the stroma are catalyzed by proteins called enzymes.",
            "tier_2": "High thermal kinetic energy disrupts weak hydrogen bonds in enzyme tertiary structure, causing denaturation.",
            "tier_3": "High temperature denatures the photosynthetic enzymes, altering active site shape and stopping glucose synthesis.",
        }
        marks = 3
    else:
        # Full compound Gr11 question
        prompt = (
            f"An investigation was conducted to study the rate of photosynthesis under controlled conditions.\n"
            f"The environmental temperature was maintained at ${temp_c}^\\circ\\text{{C}}$, $\\text{{CO}}_2$ concentration at "
            f"${co2_ppm}\\text{{ ppm}}$, and light intensity at ${light_percent}\\%$.\n\n"
            f"1. Write down the balanced chemical equation for photosynthesis.\n"
            f"2. Tabulate two differences between the light-dependent phase and the light-independent phase regarding their exact location and primary input requirements.\n"
            f"3. Explain what will happen to the rate of photosynthesis if the temperature is increased to $50^\\circ\\text{{C}}$ while light and $\\text{{CO}}_2$ remain optimal."
        )
        ans_str = (
            "1. 6CO2 + 6H2O -> C6H12O6 + 6O2; "
            "2. Table: Light phase (Grana/Thylakoids, requires Light + H2O) vs Dark phase (Stroma, requires CO2 + ATP + NADPH); "
            "3. Drops to zero due to enzyme denaturation."
        )
        memo = (
            "1. Balanced chemical equation: $6\\text{CO}_2 + 6\\text{H}_2\\text{O} \\xrightarrow{\\text{Light, Chlorophyll}} \\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2$ [3]\n"
            "2. Comparison Table [4]:\n"
            "   - Light-dependent phase: Occurs in Grana/Thylakoids; Requires Radiant light energy and Water (H2O).\n"
            "   - Light-independent phase (Calvin cycle): Occurs in Stroma; Requires CO2, ATP, and NADPH.\n"
            "3. At 50°C, enzymes (e.g. RuBisCO) are denatured, changing their active site shape and halting glucose synthesis. [2]"
        )
        hints = {
            "tier_1": "Make sure your chemical equation is balanced: 6 carbons on both sides.",
            "tier_2": "Light phase = Grana (needs H2O and light). Dark phase = Stroma (needs CO2, ATP, NADPH). Enzymes denature above 40°C.",
            "tier_3": "1. 6CO2 + 6H2O -> C6H12O6 + 6O2. 2. Grana vs Stroma; Light+Water vs CO2+ATP. 3. Enzymes denature at 50°C.",
        }
        marks = 9

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 10,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["confused_grana_with_stroma", "unbalanced_photosynthesis_equation", "forgot_temperature_enzyme_denaturation"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Balanced chemical equation", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": "Comparative table of light vs dark phases", "marks": 4, "editable": True},
                {"id": "mp_3", "desc": "Enzyme denaturation at extreme temperature", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "unbalanced_formula", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_gr11_cellular_respiration(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Grade 11 Life Sciences: Aerobic vs anaerobic respiration, glycolysis, Krebs cycle, and ATP yield."""
    exercise_type = r.choice(["sprinting 100m", "long-distance marathon running", "vigorous weightlifting"])
    qid = _make_id("ls11_respiration", seed, idx)

    if mode == "elementary_atp_yield":
        prompt = (
            "Cellular respiration is the biochemical catabolic pathway by which glucose is broken down to release energy in the form of ATP.\n\n"
            "1. State the net number of ATP molecules generated per glucose molecule during glycolysis.\n"
            "2. State the approximate total net ATP yield of complete aerobic respiration per molecule of glucose."
        )
        ans_str = "1. 2 ATP; 2. 36 to 38 ATP"
        memo = (
            "1. Glycolysis produces a net yield of 2 ATP molecules (4 produced, 2 consumed). [1]\n"
            "2. Complete aerobic respiration produces approximately 36 to 38 ATP molecules per molecule of glucose. [2]"
        )
        hints = {
            "tier_1": "Glycolysis is the anaerobic initial breakdown in the cytoplasm.",
            "tier_2": "Glycolysis yields 2 net ATP. The Krebs cycle and oxidative phosphorylation in mitochondria add 34–36 ATP.",
            "tier_3": "1. 2 net ATP. 2. 36 to 38 ATP.",
        }
        marks = 3
    else:
        # Full compound Gr11 cellular respiration question
        prompt = (
            f"An athlete is {exercise_type}.\n"
            f"During the initial phase, oxygen delivery to the skeletal muscle cells is sufficient, but during peak exertion, "
            f"an oxygen deficit develops.\n\n"
            f"1. Name the three sequential stages of aerobic cellular respiration and state where each takes place in the cell.\n"
            f"2. Write down the chemical equation for aerobic cellular respiration.\n"
            f"3. Explain what happens in the athlete's muscle cells when oxygen becomes depleted (anaerobic respiration) and name the metabolic byproduct that accumulates."
        )
        ans_str = (
            "1. Glycolysis (cytoplasm), Krebs cycle (mitochondrial matrix), Oxidative phosphorylation (mitochondrial cristae); "
            "2. C6H12O6 + 6O2 -> 6CO2 + 6H2O + 36-38 ATP; "
            "3. Anaerobic fermentation occurs; pyruvate is converted to lactic acid which accumulates causing muscle fatigue."
        )
        memo = (
            "1. Stages of aerobic respiration [3]:\n"
            "   - Glycolysis: Cytoplasm / Cytosol\n"
            "   - Krebs cycle (Citric acid cycle): Mitochondrial matrix\n"
            "   - Oxidative phosphorylation: Inner mitochondrial membrane / Cristae\n"
            "2. Chemical equation: $\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\xrightarrow{} 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + \\text{ATP}$ [3]\n"
            "3. Under oxygen deficit, anaerobic respiration (lactic acid fermentation) takes place [1]. "
            "Pyruvate is reduced to lactic acid [1], which accumulates and leads to muscle fatigue/cramping [1]."
        )
        hints = {
            "tier_1": "Identify the 3 stages: cytoplasm first, then two stages in different parts of the mitochondrion.",
            "tier_2": "When oxygen runs out in human muscle, lactic acid fermentation occurs. In yeast, it is alcohol and CO2.",
            "tier_3": "1. Glycolysis (cytoplasm), Krebs (matrix), Oxidative phosphorylation (cristae). 2. C6H12O6 + 6O2 -> 6CO2 + 6H2O + ATP. 3. Lactic acid fermentation.",
        }
        marks = 9

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 10,
        "mode": mode,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": ["aerobic_anaerobic_atp_confusion", "mitochondria_structure_confusion", "lactic_acid_vs_ethanol_confusion"],
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "3 stages and their cellular locations", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": "Aerobic respiration chemical equation", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Anaerobic lactic acid explanation", "marks": 3, "editable": True},
            ],
            "deductions": [{"rule": "unbalanced_formula", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    grade: str = "11",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator for Photosynthesis and Cellular Respiration."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    grade_num = "".join(ch for ch in str(grade) if ch.isdigit()) or "11"

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if grade_num == "8" or subskill == "photosynthesis_gr8" or mode == "elementary_starch_test":
            q = _generate_gr8_photosynthesis(sub_r, sub_seed, i, mode)
        elif subskill == "cellular_respiration" or mode == "elementary_atp_yield":
            q = _generate_gr11_cellular_respiration(sub_r, sub_seed, i, mode)
        elif subskill == "photosynthesis" or mode in ("elementary_light_phase_sites", "elementary_limiting_factor_graph"):
            q = _generate_gr11_photosynthesis_phases(sub_r, sub_seed, i, mode)
        else:
            # Default mixed mode for Grade 11 Life Sciences
            chosen = sub_r.choice(["photo", "resp"])
            if chosen == "photo":
                q = _generate_gr11_photosynthesis_phases(sub_r, sub_seed, i, mode)
            else:
                q = _generate_gr11_cellular_respiration(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions
