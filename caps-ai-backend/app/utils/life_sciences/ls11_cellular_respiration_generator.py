"""Life Sciences Grade 11 Term 2: Cellular Respiration Generator.

Covers:
- Aerobic cellular respiration:
  - Glycolysis (cytosol/cytoplasm, anaerobic breakdown of glucose to pyruvate, net 2 ATP).
  - Krebs cycle (mitochondrial matrix, decarboxylation, release of CO2, high-energy H-carriers NADH/FADH2).
  - Oxidative phosphorylation (mitochondrial cristae, electron transport system, ATP synthase, oxygen as terminal electron acceptor forming water, 32-34 ATP).
- Anaerobic respiration (Fermentation):
  - Lactic acid fermentation in human skeletal muscle under oxygen debt.
  - Alcoholic fermentation in yeast (brewing and bread baking industries).
- Respirometer experiments: Germinating seeds, lime water CO2 tests, thermoflask heat release.

Strictly complies with the 6-Pillar Generator Contract.
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


def _generate_respiration_stages(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Aerobic stages, ATP yield, and organelle locations."""
    qid = _make_id("ls11_aerobic_resp", seed, idx)

    if mode == "elementary_atp_yield":
        prompt = (
            "Aerobic cellular respiration occurs in three distinct sequential stages inside eukaryotic cells.\n\n"
            "1. State the net number of ATP molecules produced per molecule of glucose during glycolysis.\n"
            "2. State the final terminal electron acceptor in the electron transport chain of oxidative phosphorylation.\n"
            "3. State the approximate total net ATP yield of complete aerobic cellular respiration per molecule of glucose."
        )
        ans_str = "1. 2 ATP; 2. Oxygen (O2); 3. 36 to 38 ATP"
        memo = (
            "1. Glycolysis net yield: 2 ATP molecules (4 synthesized, 2 consumed during activation). [1]\n"
            "2. Terminal electron acceptor: Oxygen ($O_2$), which combines with electrons and $H^+$ ions to form water ($H_2O$). [1]\n"
            "3. Total net ATP yield: Approximately 36 to 38 ATP molecules per molecule of glucose. [1]"
        )
        hints = {
            "tier_1": "Glycolysis gives a small net gain of 2. Aerobic respiration produces much more energy.",
            "tier_2": "Oxygen accepts electrons at the end of the electron transport chain. Total ATP is 36-38.",
            "tier_3": "1. 2 ATP. 2. Oxygen. 3. 36 to 38 ATP.",
        }
        marks = 3
        misconceptions = ["confused_gross_vs_net_atp", "forgot_oxygen_terminal_acceptor"]
    else:
        # Full compound aerobic respiration question
        tissue = r.choice(["human skeletal muscle cells during moderate aerobic exertion", "active liver hepatocytes metabolizing glucose", "germinating sunflower seedlings with high metabolic rates"])
        prompt = (
            f"A biochemical diagram illustrates the catabolism of glucose inside {tissue}.\n\n"
            "1. Name the THREE sequential stages of aerobic respiration and state the exact cellular site of each stage.\n"
            "2. Write down the complete balanced chemical equation for aerobic cellular respiration.\n"
            "3. Explain why the inner mitochondrial membrane (cristae) is extensively folded into finger-like projections."
        )
        ans_str = (
            "1. Glycolysis (cytoplasm), Krebs cycle (mitochondrial matrix), Oxidative phosphorylation (mitochondrial cristae); "
            "2. C6H12O6 + 6O2 -> 6CO2 + 6H2O + 36-38 ATP; "
            "3. Folds (cristae) provide an extensive surface area for electron transport carrier enzymes and ATP synthase complexes."
        )
        memo = (
            "1. Stages and locations [3]:\n"
            "   - Glycolysis: Cytoplasm / Cytosol [1]\n"
            "   - Krebs cycle (Citric acid cycle): Mitochondrial matrix [1]\n"
            "   - Oxidative phosphorylation: Inner mitochondrial membrane / Cristae [1]\n"
            "2. Balanced chemical equation [3]:\n"
            "   $$\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\xrightarrow{\\text{enzymes}} 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{--}38\\text{ ATP}$$\n"
            "   (1 mark for reactants, 1 mark for products, 1 mark for balancing).\n"
            "3. Cristae folding adaptation [2]: The folds (cristae) vastly increase the surface area [1] for packing "
            "electron transport chain cytochromes and ATP synthase enzyme complexes, maximizing ATP synthesis [1]."
        )
        hints = {
            "tier_1": "One stage occurs outside the mitochondrion; two occur inside. Cristae provide surface area.",
            "tier_2": "Cytoplasm = Glycolysis. Matrix = Krebs. Cristae = Oxidative phosphorylation. Folds increase surface area for ATP synthase.",
            "tier_3": "1. Glycolysis (cytoplasm), Krebs (matrix), Oxidative phosphorylation (cristae). 2. C6H12O6 + 6O2 -> 6CO2 + 6H2O + ATP. 3. Increase surface area for enzymes.",
        }
        marks = 8
        misconceptions = ["confused_matrix_with_cristae", "unbalanced_respiration_equation", "omitted_surface_area_adaptation"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 9,
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
                {"id": "mp_1", "desc": "3 stages and their precise cellular locations", "marks": 3, "editable": True},
                {"id": "mp_2", "desc": "Balanced chemical equation for aerobic respiration", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Cristae surface area structural adaptation", "marks": 2, "editable": True},
            ],
            "deductions": [{"rule": "unbalanced_formula", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_anaerobic_and_experiments(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Anaerobic fermentation in humans vs yeast and respirometer investigations."""
    context = r.choice(["athletic_sprint", "yeast_fermentation", "germinating_seeds"])
    qid = _make_id("ls11_anaerobic_exp", seed, idx)

    if context == "athletic_sprint":
        sport = r.choice(["100m Olympic sprint", "400m high-intensity hurdles event", "explosive rugby scrum drive"])
        prompt = (
            f"During a {sport}, an athlete's skeletal muscles expend energy at an exceptionally rapid rate, exceeding the rate at which "
            f"oxygen can be delivered by the cardiovascular system.\n\n"
            f"1. Name the pathway of cellular respiration that occurs under this condition.\n"
            f"2. Name the toxic metabolic byproduct that accumulates in muscle cells and explain its physiological effect.\n"
            f"3. Explain what 'oxygen debt' means and describe how it is repaid after the athlete stops running."
        )
        ans_str = (
            "1. Anaerobic respiration / Lactic acid fermentation; "
            "2. Lactic acid (lactate); causes muscle fatigue, stiffness, and cramping; "
            "3. Oxygen debt is the extra oxygen required post-exercise to transport lactic acid to the liver and convert it back to pyruvic acid / glucose."
        )
        memo = (
            "1. Pathway: Anaerobic respiration / Lactic acid fermentation. [1]\n"
            "2. Toxic byproduct and effect [2]: Lactic acid (lactate) [1]. Its accumulation lowers intracellular pH, inhibiting glycolytic enzymes and causing muscle fatigue/cramps [1].\n"
            "3. Oxygen debt repayment [3]: Oxygen debt is the volume of oxygen required after strenuous exercise to metabolize accumulated lactic acid [1]. "
            "The athlete breathes heavily post-exercise to supply oxygen [1], allowing lactic acid to be transported via the bloodstream to the liver where it is oxidised back into pyruvate and glucose [1]."
        )
        hints = {
            "tier_1": "Without oxygen, pyruvate cannot enter the mitochondrion. What builds up in human muscle?",
            "tier_2": "Lactic acid forms. Rapid deep breathing after exercise supplies oxygen to clear it in the liver.",
            "tier_3": "1. Lactic acid fermentation. 2. Lactic acid causes fatigue/cramps. 3. Extra oxygen taken in after exercise to convert lactic acid back to glucose in the liver.",
        }
        marks = 6
        misconceptions = ["lactic_acid_vs_alcohol_confusion", "misunderstood_oxygen_debt_repayment"]
    elif context == "yeast_fermentation":
        product_app = r.choice(["commercial beer brewing", "traditional sorghum beer fermentation", "commercial bread baking"])
        prompt = (
            f"Yeast (*Saccharomyces cerevisiae*) is widely utilized in {product_app} because of its metabolic capabilities under anaerobic conditions.\n\n"
            f"1. Write down the word equation for anaerobic respiration (fermentation) in yeast.\n"
            f"2. State which product of yeast fermentation is essential in bread dough rising and explain why.\n"
            f"3. Compare the net ATP yield of alcoholic fermentation in yeast to that of complete aerobic respiration in human liver cells."
        )
        ans_str = (
            "1. Glucose -> Ethanol + Carbon dioxide + 2 ATP; "
            "2. Carbon dioxide (CO2); gas bubbles expand dough, creating porous, spongy bread; "
            "3. Fermentation yields only 2 ATP per glucose, whereas aerobic respiration yields 36-38 ATP (18 times more energy)."
        )
        memo = (
            "1. Word equation for alcoholic fermentation [2]:\n"
            "   $$\\text{Glucose} \\xrightarrow{\\text{yeast enzymes}} \\text{Ethanol} + \\text{Carbon dioxide} + \\text{Energy (2 ATP)}$$ [2]\n"
            "2. Bread rising role [2]: Carbon dioxide gas ($CO_2$) is released and trapped in the gluten dough matrix [1], "
            "expanding during baking to create a light, porous, spongy texture (the alcohol evaporates during baking) [1].\n"
            "3. ATP comparison [2]: Alcoholic fermentation yields only a net of 2 ATP per glucose molecule [1], "
            "whereas aerobic cellular respiration yields 36 to 38 ATP per glucose molecule (approximately 18 to 19 times more energy) [1]."
        )
        hints = {
            "tier_1": "Yeast produces alcohol, gas, and a tiny amount of ATP. Think about which gas causes dough to rise.",
            "tier_2": "Equation: Glucose -> Ethanol + CO2 + 2 ATP. CO2 gas expands the dough. Aerobic produces 36-38 ATP vs 2 in fermentation.",
            "tier_3": "1. Glucose -> Ethanol + CO2 + ATP. 2. CO2 gas expands dough. 3. 2 ATP (anaerobic) vs 36-38 ATP (aerobic).",
        }
        marks = 6
        misconceptions = ["forgot_ethanol_product_in_plants", "fermentation_atp_exaggeration"]
    else:  # germinating_seeds
        seeds = r.choice(["germinating bean seeds", "germinating pea seeds", "germinating sunflower seeds"])
        prompt = (
            f"An investigation was set up using {seeds} placed in a thermos flask connected via delivery tube to a test tube of clear limewater.\n"
            f"A second thermos flask containing boiled, sterilized seeds with disinfectant served as the experimental control.\n\n"
            f"1. Predict the observation in the limewater test tube connected to the live germinating seeds.\n"
            f"2. Explain why the seeds in the control flask were boiled and soaked in disinfectant.\n"
            f"3. A thermometer inserted into the flask with live germinating seeds recorded a temperature increase from 20°C to 26°C. "
            f"Explain the source of this thermal energy."
        )
        ans_str = (
            "1. Limewater turns milky/cloudy; "
            "2. Boiling kills seeds to stop respiration; disinfectant kills bacteria/fungi so their respiration does not skew results; "
            "3. Respiration is an exothermic catabolic reaction; energy not trapped as ATP is lost as metabolic heat."
        )
        memo = (
            "1. Observation [1]: Clear limewater (calcium hydroxide) turns milky / cloudy / chalky white due to carbon dioxide production. [1]\n"
            "2. Control sterilization rationale [2]: Boiling kills the plant embryos to halt living seed respiration [1], "
            "and disinfectant destroys bacteria and fungal spores on the seed coat so that microbial respiration does not produce false CO2/heat [1].\n"
            "3. Temperature rise explanation [2]: Cellular respiration is an exothermic catabolic process [1]. "
            "Approximately 60% of the chemical energy liberated during glucose breakdown is not conserved as ATP but is dissipated as metabolic heat [1]."
        )
        hints = {
            "tier_1": "Limewater tests for carbon dioxide. Why do we sterilize seeds in experiments on respiration?",
            "tier_2": "CO2 turns limewater milky. Boiled seeds + disinfectant ensure no living organisms or microbes respire. Respiration releases heat.",
            "tier_3": "1. Turns milky. 2. Kills seeds and microbes to prove live seeds caused the effect. 3. Heat energy dissipated from exothermic respiration.",
        }
        marks = 5
        misconceptions = ["confused_limewater_with_iodine", "forgot_microbial_respiration_control"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 9,
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
                {"id": "mp_1", "desc": "Biochemical pathway or experimental prediction", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Physiological rationale or validity condition", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Energy budget or post-exercise debt recovery", "marks": marks - 4, "editable": True},
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
    """Master entry point for Grade 11 Cellular Respiration."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("aerobic_stages", "atp_yield") or mode == "elementary_atp_yield":
            q = _generate_respiration_stages(sub_r, sub_seed, i, mode)
        elif subskill in ("anaerobic_fermentation", "respirometer"):
            q = _generate_anaerobic_and_experiments(sub_r, sub_seed, i, mode)
        else:
            # Alternating between aerobic pathways and anaerobic/experimental questions
            if i % 2 == 0:
                q = _generate_respiration_stages(sub_r, sub_seed, i, mode)
            else:
                q = _generate_anaerobic_and_experiments(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)
