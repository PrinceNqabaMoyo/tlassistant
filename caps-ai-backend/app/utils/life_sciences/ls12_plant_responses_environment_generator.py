"""Life Sciences Grade 12 Term 2: Plant Responses to the Environment Generator.

Covers:
- Plant hormones and growth regulators:
  - Auxins (IAA): Phototropism (unilateral light), Geotropism/Gravitropism (gravity response), and apical dominance.
  - Gibberellins: Stem elongation, seed germination (breaking dormancy), and fruit development.
  - Abscisic acid (ABA): Dormancy, drought stress response, and stomatal closure.
- Commercial applications of plant hormones: Synthetic weedkillers (2,4-D), rooting powders, and seedless fruit (parthenocarpy).
- Classical experimental investigations: Clinostat rotation vs stationary, tip decapitation, opaque foil caps, and mica sheet barrier experiments.
- Plant defence mechanisms: Mechanical (thorns, spines, thick cuticle) vs Chemical (tannins, toxic alkaloids).

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


def _generate_phototropism_investigation(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Auxin distribution, unilateral light, and phototropism experiments."""
    plant = r.choice(["oat (*Avena*) coleoptile", "maize seedling shoot", "sunflower hypocotyl", "bean seedling stem"])
    qid = _make_id("ls12_phototropism", seed, idx)

    # Treatment condition for the tip
    treatment = r.choice(["intact tip with unilateral light", "opaque tin foil cap over tip", "tip decapitated", "impermeable mica sheet inserted on shaded side"])

    if mode == "elementary_auxin_roles":
        prompt = (
            "Plant growth responses to external directional stimuli are regulated by biochemical plant hormones.\n\n"
            "1. Name the primary plant growth hormone synthesized in the apical meristem of the shoot tip.\n"
            "2. Distinguish between the effect of a high concentration of auxins on cell elongation in the **stem** versus in the **root**."
        )
        ans_str = "1. Auxin (IAA); 2. In stems: High auxin stimulates cell elongation; In roots: High auxin inhibits cell elongation."
        memo = (
            "1. Primary growth hormone: **Auxin** (Indole-3-acetic acid / IAA). [1]\n"
            "2. Differential response to auxin [2]:\n"
            "   - In stems / shoots: High auxin concentration **stimulates** cell elongation [1].\n"
            "   - In roots: High auxin concentration **inhibits** cell elongation [1]."
        )
        hints = {
            "tier_1": "Auxins have opposite effects on cell elongation in shoots versus roots.",
            "tier_2": "Shoots require high auxin to grow faster; roots are much more sensitive, so high auxin slows down root cell elongation.",
            "tier_3": "1. Auxin / IAA. 2. Stems: stimulates elongation; Roots: inhibits elongation.",
        }
        marks = 3
        misconceptions = ["auxin_root_shoot_effect_inversion", "confused_auxin_with_gibberellin"]
    else:
        # Full compound question on phototropism experiment
        prompt = (
            f"Grade 12 Life Sciences learners investigated phototropism using four {plant} seedlings exposed to unilateral light from the right:\n"
            f"- Seedling A: Intact tip (unmodified).\n"
            f"- Seedling B: Tip removed (decapitated).\n"
            f"- Seedling C: Tip covered with an opaque aluminium foil cap.\n"
            f"- Seedling D: Tip covered with a transparent plastic cap.\n\n"
            f"1. Name the hormone responsible for the growth movement observed in Seedling A.\n"
            f"2. Explain why Seedling A bends towards the light while Seedling C continues to grow straight upwards.\n"
            f"3. Explain the expected result in Seedling B.\n"
            f"4. State the purpose of including Seedling D in this investigation."
        )
        ans_str = (
            "1. Auxin (IAA); "
            "2. In Seedling A, auxins migrate away from unilateral light to shaded (left) side, stimulating cell elongation so shoot curves towards light; Seedling C cap blocks light from tip so auxins remain evenly distributed; "
            "3. Seedling B stops growing / does not bend because tip which synthesizes auxins was excised; "
            "4. Seedling D acts as a control to prove that physical touch/weight of cap does not cause the lack of bending."
        )
        memo = (
            "1. Hormone: **Auxin** / Indole-3-acetic acid (IAA). [1]\n"
            "2. Bending mechanism explanation [4]:\n"
            "   - In Seedling A: Unilateral light strikes from the right, causing auxins to migrate to the shaded (left) side of the shoot [1].\n"
            "   - The higher auxin concentration on the shaded side stimulates greater cell elongation compared to the illuminated side [1],\n"
            "   - causing the shoot to bend towards the light source (positive phototropism) [1].\n"
            "   - In Seedling C: The opaque foil cap prevents photoreceptors in the tip from detecting unilateral light; auxins remain evenly distributed, causing equal elongation and straight upward growth [1].\n"
            "3. Seedling B outcome [2]: Growth halts or no bending occurs [1] because the apical meristem producing auxins was removed [1].\n"
            "4. Seedling D purpose [1]: Serves as an experimental control to prove that the presence of a cap itself does not impede phototropic response, confirming that light perception is the decisive variable [1]."
        )
        hints = {
            "tier_1": "Auxins move to the dark side. Shoot cells with more auxin grow faster. Decapitation removes the auxin source.",
            "tier_2": "Shaded side has more auxin and grows faster, bending shoot to light. Seedling C gets no light at tip. D controls for the cap.",
            "tier_3": "1. Auxin. 2. Shaded side gets more auxin and elongates faster; C tip cannot perceive light so grows straight. 3. No growth/bending (tip removed). 4. Control for cap weight.",
        }
        marks = 8
        misconceptions = ["auxin_light_side_accumulation_error", "omitted_cell_elongation_mechanism", "control_variable_confusion"]

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
                {"id": "mp_1", "desc": "Hormone identification", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Auxin lateral migration and unequal cell elongation mechanism", "marks": 4, "editable": True},
                {"id": "mp_3", "desc": "Decapitation physiological deduction", "marks": 2, "editable": True},
                {"id": "mp_4", "desc": "Transparent cap experimental control rationale", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_geotropism_and_hormones(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Geotropism / clinostat experiments, ABA, gibberellins, and weedkiller applications."""
    topic = r.choice(["clinostat_geotropism", "hormone_functions_and_weedkillers", "apical_dominance"])
    qid = _make_id("ls12_plant_hormones", seed, idx)

    if topic == "clinostat_geotropism":
        prompt = (
            "A potted bean seedling was placed horizontally on a motorized clinostat apparatus in a dark room.\n"
            "- Clinostat 1: Rotates slowly and continuously at 1 revolution per hour.\n"
            "- Clinostat 2: Remains stationary (switched off) in the horizontal position.\n\n"
            "1. Predict the direction of growth of the shoot and root in **Clinostat 1**.\n"
            "2. Explain why the shoot in **Clinostat 2** bends upwards (negative geotropism) while the root bends downwards (positive geotropism).\n"
            "3. State the purpose of conducting this investigation in complete darkness."
        )
        ans_str = (
            "1. Shoot and root continue to grow straight horizontally; "
            "2. In stationary Clinostat 2, gravity causes auxins to accumulate on lower sides of both shoot and root; In shoot, high auxin stimulates cell elongation so lower side grows faster and bends up; In root, high auxin inhibits cell elongation so upper side grows faster and bends down; "
            "3. Eliminates light as an independent variable so phototropism does not interfere with the gravity response."
        )
        memo = (
            "1. Clinostat 1 prediction [2]: Both the shoot and the root will continue to grow straight horizontally [1] "
            "because continuous rotation distributes the gravitational pull equally on all sides of the organs [1].\n"
            "2. Clinostat 2 differential geotropic mechanism [4]:\n"
            "   - Gravity pulls auxins towards the lower side of both horizontally oriented organs [1].\n"
            "   - In the shoot: High auxin concentration on the lower side **stimulates** cell elongation, causing the lower side to elongate faster and curve upwards (negative geotropism) [1.5].\n"
            "   - In the root: High auxin concentration on the lower side **inhibits** cell elongation, allowing the upper side to elongate faster and curve downwards (positive geotropism) [1.5].\n"
            "3. Darkness rationale [1]: Placing the seedlings in darkness eliminates light as an external stimulus, ensuring any observed bending is solely a response to gravity (geotropism) and not phototropism [1]."
        )
        hints = {
            "tier_1": "Rotating distributes gravity evenly. In a horizontal seedling, auxin accumulates on the bottom side.",
            "tier_2": "Rotation = grows straight. High auxin on bottom of shoot speeds growth (bends up). High auxin on bottom of root slows growth (bends down).",
            "tier_3": "1. Grows straight. 2. Auxin accumulates on lower side; stimulates shoot elongation (curves up), inhibits root elongation (curves down). 3. Prevents phototropism.",
        }
        marks = 7
        misconceptions = ["clinostat_rotation_effect_misunderstood", "root_geotropism_inversion", "forgot_darkness_control_purpose"]
    elif topic == "hormone_functions_and_weedkillers":
        prompt = (
            "Horticultural farmers frequently utilize synthetic plant hormones to manage crop production.\n\n"
            "1. Name the plant hormone that triggers rapid closure of stomata during severe drought stress.\n"
            "2. State TWO functions of **gibberellins** in plants.\n"
            "3. Explain how synthetic auxins (such as 2,4-D) act as selective weedkillers in wheat or maize fields."
        )
        ans_str = (
            "1. Abscisic acid (ABA); "
            "2. Promotes stem elongation / internode lengthening, and breaks seed dormancy to stimulate germination; "
            "3. Synthetic auxins are absorbed selectively by broad-leaved dicot weeds, causing rapid uncontrollable runaway growth that exhausts food reserves and kills the weed, while narrow-leaved monocot crops are unharmed."
        )
        memo = (
            "1. Drought stress hormone: **Abscisic acid (ABA)**. [1]\n"
            "2. Gibberellin functions (any 2) [2]:\n"
            "   - Promotes internode and stem elongation [1].\n"
            "   - Breaks seed dormancy and initiates seed germination by mobilizing amylase enzymes [1].\n"
            "   - Promotes the development of larger seedless fruits (parthenocarpy) [1].\n"
            "3. Selective weedkiller action [3]: Synthetic auxins (e.g. 2,4-D) are selectively absorbed at lethal concentrations by broadleaf dicotyledonous weeds [1]. "
            "The unnaturally high auxin levels cause rapid, unregulated cell elongation and metabolic exhaustion [1], "
            "causing the weeds to warp, wither, and die while monocot crops (maize, wheat) metabolize or resist the chemical [1]."
        )
        hints = {
            "tier_1": "ABA is the stress hormone. Gibberellins make plants grow tall and wake up seeds. 2,4-D kills broadleaf weeds by causing runaway growth.",
            "tier_2": "ABA closes stomata. Gibberellins lengthen stems and break dormancy. 2,4-D overstimulates dicot weed growth until they collapse.",
            "tier_3": "1. Abscisic acid (ABA). 2. Stem elongation; breaks seed dormancy. 3. Causes rapid uncontrolled growth in broadleaf weeds which kills them.",
        }
        marks = 6
        misconceptions = ["confused_aba_with_auxin", "gibberellin_function_confusion", "weedkiller_mode_of_action_misconception"]
    else:  # apical_dominance
        prompt = (
            "A tea plantation farmer prunes (cuts off) the apical terminal buds of young tea bushes to increase leaf harvest.\n\n"
            "1. Name the physiological phenomenon where the terminal bud suppresses the growth of lateral buds.\n"
            "2. Explain the hormonal mechanism behind apical dominance.\n"
            "3. Explain why pruning the terminal bud causes the tea bushes to become bushier with more leaves."
        )
        ans_str = (
            "1. Apical dominance; "
            "2. Terminal bud synthesizes high concentrations of auxin which diffuse downward and inhibit lateral axillary buds; "
            "3. Removing terminal bud removes auxin source, allowing lateral buds to grow into branches."
        )
        memo = (
            "1. Phenomenon: **Apical dominance**. [1]\n"
            "2. Hormonal mechanism [2]: The growing terminal apical bud synthesizes high concentrations of auxins [1], "
            "which diffuse downwards through the stem and actively inhibit the elongation and division of cells in lateral (axillary) buds [1].\n"
            "3. Pruning explanation [2]: Removing (decapitating) the apical bud eliminates the primary source of downward-flowing auxins [1]. "
            "The low auxin concentration releases the lateral buds from inhibition, allowing them to develop into lateral branches, producing a bushier plant [1]."
        )
        hints = {
            "tier_1": "The top bud stops the side buds from growing. Cutting the top bud lets the side buds grow.",
            "tier_2": "Apical dominance is caused by auxin from the terminal bud inhibiting lateral buds. Removing it releases them.",
            "tier_3": "1. Apical dominance. 2. Auxins from apical bud inhibit lateral buds. 3. Removing tip removes auxin, releasing lateral branches.",
        }
        marks = 5
        misconceptions = ["confused_apical_dominance_with_phototropism", "pruning_mechanism_misunderstood"]

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
                {"id": "mp_1", "desc": "Hormone identification or phenomenon name", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Physiological explanation or differential mechanism", "marks": 3, "editable": True},
                {"id": "mp_3", "desc": "Experimental deduction or commercial application", "marks": marks - 4, "editable": True},
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
    """Master entry point for Grade 12 Plant Responses to the Environment."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("phototropism", "auxin_experiments") or mode == "elementary_auxin_roles":
            q = _generate_phototropism_investigation(sub_r, sub_seed, i, mode)
        elif subskill in ("geotropism", "clinostat", "weedkillers", "apical_dominance"):
            q = _generate_geotropism_and_hormones(sub_r, sub_seed, i, mode)
        else:
            # Alternating between phototropism experiments and geotropism/hormone questions
            if i % 2 == 0:
                q = _generate_phototropism_investigation(sub_r, sub_seed, i, mode)
            else:
                q = _generate_geotropism_and_hormones(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions


def generate_variant(seed: int, mode: str = "practice", **kwargs: Any) -> List[Dict[str, Any]]:
    return generate(count=1, seed=seed, mode=mode, **kwargs)
