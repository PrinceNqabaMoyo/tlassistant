"""Natural Sciences Grade 7 Term 2: Acids, Bases, and Neutral Substances Generator.

100% CAPS-aligned deterministic generator grounded in
curriculum_docs_auto/Natural Sciences_Gr7/Term 2/03. Acids, bases and neutrals.md.

Subskills:
1. ph_classification: Classification of substances across the pH scale (1 to 14)
2. litmus_indicators: Red and blue litmus paper color transitions and testing
3. universal_indicator: Full color spectrum and pH estimation using universal indicator
4. neutralization_applications: Acid-base neutralization reactions and practical applications (stings, antacids, soil lime)
5. acid_base_properties: Physical, sensory, and chemical properties of acids and bases

Strictly complies with the 6-Pillar Generator Contract.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "ph_classification",
    "litmus_indicators",
    "universal_indicator",
    "neutralization_applications",
    "acid_base_properties",
]


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _gen_ph_classification(r: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    acid_choices = [
        ("battery acid", 1, "strong acid"),
        ("lemon juice", 2, "strong acid"),
        ("vinegar", 3, "weak acid"),
        ("tomato juice", 4, "weak acid"),
        ("black coffee", 5, "weak acid"),
        ("fresh milk", 6, "weak acid"),
    ]
    base_choices = [
        ("seawater", 8, "weak base"),
        ("baking soda solution", 9, "weak base"),
        ("milk of magnesia", 10, "weak base"),
        ("household ammonia cleaner", 11, "strong base"),
        ("soapy washing powder", 12, "strong base"),
        ("caustic drain cleaner", 13, "strong base"),
    ]

    acid_item = r.choice(acid_choices)
    base_item = r.choice(base_choices)
    neutral_item = ("pure distilled water", 7, "neutral")

    items = [acid_item, neutral_item, base_item]
    r.shuffle(items)

    prompt = (
        f"A Grade 7 science learner tests three household substances on the pH scale:\n"
        f"- Substance A: {items[0][0]} (pH {items[0][1]})\n"
        f"- Substance B: {items[1][0]} (pH {items[1][1]})\n"
        f"- Substance C: {items[2][0]} (pH {items[2][1]})\n\n"
        f"1. Classify each substance as an **acid**, **base**, or **neutral** based on its pH value. (3)\n"
        f"2. State the pH range for acidic substances and basic (alkaline) substances. (2)\n"
        f"3. Which of the three substances is the most acidic? (1)"
    )

    most_acidic = min(items, key=lambda x: x[1])[0]

    memo = (
        f"Step 1: Classify based on pH:\n"
        f"- Substance A ({items[0][0]}, pH {items[0][1]}): **{('Acid' if items[0][1] < 7 else ('Neutral' if items[0][1] == 7 else 'Base'))}** [1]\n"
        f"- Substance B ({items[1][0]}, pH {items[1][1]}): **{('Acid' if items[1][1] < 7 else ('Neutral' if items[1][1] == 7 else 'Base'))}** [1]\n"
        f"- Substance C ({items[2][0]}, pH {items[2][1]}): **{('Acid' if items[2][1] < 7 else ('Neutral' if items[2][1] == 7 else 'Base'))}** [1]\n\n"
        f"Step 2: State pH ranges:\n"
        f"- Acids have a pH from **0 to less than 7** (0–6) [1]\n"
        f"- Bases have a pH from **greater than 7 to 14** (8–14) [1]\n\n"
        f"Step 3: Most acidic substance:\n"
        f"**{most_acidic}** (has the lowest pH number) [1]"
    )

    correct_ans = (
        f"A: {('Acid' if items[0][1] < 7 else ('Neutral' if items[0][1] == 7 else 'Base'))}; "
        f"B: {('Acid' if items[1][1] < 7 else ('Neutral' if items[1][1] == 7 else 'Base'))}; "
        f"C: {('Acid' if items[2][1] < 7 else ('Neutral' if items[2][1] == 7 else 'Base'))}; "
        f"Acids: pH < 7, Bases: pH > 7; Most acidic: {most_acidic}"
    )

    return {
        "id": _make_id("ns7_ph_class", seed, idx),
        "prompt": prompt,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 6,
        "subskill": "ph_classification",
        "question_type": "short_answer",
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "canonical_solution": memo,
        "explanation": memo,
        "marks": 6,
        "hints": {
            "tier_1": "Recall that pH 7 is neutral. Values below 7 are acidic, and values above 7 are basic.",
            "tier_2": "The lower the pH value (closer to 0), the stronger the acid. The higher the pH (closer to 14), the stronger the base.",
            "tier_3": f"Acids < 7, Neutral = 7, Bases > 7. Most acidic has lowest pH: {most_acidic}."
        },
        "misconception_tags": ["ph_scale_direction_inversion", "confused_neutral_with_acid"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_1", "desc": f"Correct classification of Substance A ({items[0][0]})", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Correct classification of Substance B ({items[1][0]})", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Correct classification of Substance C ({items[2][0]})", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Acid pH range: pH < 7 (or 0-6)", "marks": 1, "editable": True},
                {"id": "mp_5", "desc": "Base pH range: pH > 7 (or 8-14)", "marks": 1, "editable": True},
                {"id": "mp_6", "desc": f"Identification of most acidic: {most_acidic}", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


def _gen_litmus_indicators(r: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    scenarios = [
        ("clear vinegar (dilute ethanoic acid)", "acid", "remains red", "turns red"),
        ("limewater (calcium hydroxide solution)", "base", "turns blue", "remains blue"),
        ("table salt water (sodium chloride solution)", "neutral", "remains red", "remains blue"),
        ("hand washing soap solution", "base", "turns blue", "remains blue"),
        ("fizzy cold drink (carbonic acid)", "acid", "remains red", "turns red"),
    ]
    substance, s_type, red_res, blue_res = r.choice(scenarios)

    prompt = (
        f"A laboratory technician investigates a beaker containing **{substance}** using dry strips of red and blue litmus paper.\n\n"
        f"1. Predict the colour change observed on the **red litmus paper** strip. (1)\n"
        f"2. Predict the colour change observed on the **blue litmus paper** strip. (1)\n"
        f"3. Based on the litmus observations, determine whether {substance} is an acid, a base, or neutral. (1)\n"
        f"4. State one limitation of litmus paper compared to a digital pH meter. (1)"
    )

    memo = (
        f"Step 1: Red litmus reaction:\n"
        f"{red_res.capitalize()} [1]\n\n"
        f"Step 2: Blue litmus reaction:\n"
        f"{blue_res.capitalize()} [1]\n\n"
        f"Step 3: Classification:\n"
        f"**{s_type.capitalize()}** [1]\n\n"
        f"Step 4: Limitation of litmus paper:\n"
        f"Litmus paper only indicates whether a substance is an acid or a base; it does not measure the exact pH value or relative strength of the solution. [1]"
    )

    correct_ans = f"1. Red litmus: {red_res}; 2. Blue litmus: {blue_res}; 3. {s_type.capitalize()}; 4. Litmus does not indicate exact pH or strength."

    return {
        "id": _make_id("ns7_litmus", seed, idx),
        "prompt": prompt,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "subskill": "litmus_indicators",
        "question_type": "short_answer",
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "canonical_solution": memo,
        "explanation": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Bases turn red litmus Blue (B for Base, B for Blue). Acids turn blue litmus Red.",
            "tier_2": f"{substance.capitalize()} is an {s_type}. Think about how red and blue litmus behave in an {s_type}.",
            "tier_3": f"Red litmus: {red_res}. Blue litmus: {blue_res}. Classification: {s_type}."
        },
        "misconception_tags": ["litmus_colour_reversal", "confused_neutral_with_colourless"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": f"Red litmus: {red_res}", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Blue litmus: {blue_res}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Classification: {s_type}", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Limitation: cannot show exact numerical pH / strength", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


def _gen_universal_indicator(r: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    cases = [
        ("Sample P", 1, "red", "strong acid"),
        ("Sample Q", 5, "yellow/orange", "weak acid"),
        ("Sample R", 7, "green", "neutral"),
        ("Sample S", 9, "blue", "weak base"),
        ("Sample T", 13, "purple/violet", "strong base"),
    ]
    c1, c2 = r.sample(cases, 2)

    prompt = (
        f"Universal indicator solution produces a continuous spectrum of colours corresponding to different pH values.\n\n"
        f"A learner adds a few drops of universal indicator to two unknown solutions:\n"
        f"- Solution 1 turns **{c1[2]}** (pH {c1[1]})\n"
        f"- Solution 2 turns **{c2[2]}** (pH {c2[1]})\n\n"
        f"1. State the colour that Universal Indicator displays in a perfectly neutral solution (pH 7). (1)\n"
        f"2. Deduce whether Solution 1 is a strong acid, weak acid, neutral, weak base, or strong base. (1)\n"
        f"3. Deduce whether Solution 2 is a strong acid, weak acid, neutral, weak base, or strong base. (1)\n"
        f"4. Why is Universal Indicator more informative than litmus paper in a laboratory? (1)"
    )

    memo = (
        f"Step 1: Neutral colour of Universal Indicator:\n"
        f"**Green** [1]\n\n"
        f"Step 2: Solution 1 classification:\n"
        f"**{c1[3].capitalize()}** (pH {c1[1]} gives a {c1[2]} colour) [1]\n\n"
        f"Step 3: Solution 2 classification:\n"
        f"**{c2[3].capitalize()}** (pH {c2[1]} gives a {c2[2]} colour) [1]\n\n"
        f"Step 4: Scientific advantage:\n"
        f"Universal indicator provides a broad spectrum of colours that allows learners to estimate the exact pH value and relative strength of the acid or base, whereas litmus only provides a binary yes/no test. [1]"
    )

    correct_ans = f"1. Green; 2. {c1[3].capitalize()}; 3. {c2[3].capitalize()}; 4. Universal indicator shows the full range of pH and strength."

    return {
        "id": _make_id("ns7_univ_ind", seed, idx),
        "prompt": prompt,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "subskill": "universal_indicator",
        "question_type": "short_answer",
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "canonical_solution": memo,
        "explanation": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Think about the colors of the rainbow: red/orange is acid, green is neutral, blue/purple is base.",
            "tier_2": "Neutral pH 7 is green. Red indicates a strong acid, while purple/violet indicates a strong base.",
            "tier_3": f"Neutral: Green. Solution 1: {c1[3]}. Solution 2: {c2[3]}."
        },
        "misconception_tags": ["universal_indicator_colour_confusion", "confused_weak_with_strong_acid"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Neutral colour is green", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": f"Solution 1 deduced as {c1[3]}", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Solution 2 deduced as {c2[3]}", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Universal indicator advantage: estimates exact pH / strength across full spectrum", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


def _gen_neutralization_applications(r: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    scenarios = [
        {
            "context": "indigestion and heartburn",
            "cause": "excess hydrochloric acid produced in the stomach (pH ~1,5 to 2)",
            "remedy": "antacid tablet containing magnesium hydroxide or calcium carbonate (mild base)",
            "reaction": "The basic antacid reacts with the excess stomach acid to form a neutral salt and water, relieving burning discomfort."
        },
        {
            "context": "bee sting treatment",
            "cause": "acidic venom (methanoic / formic acid) injected into skin tissue",
            "remedy": "bicarbonate of soda paste (mild household base)",
            "reaction": "The mild base neutralizes the acidic venom into harmless salt and water, reducing swelling and pain."
        },
        {
            "context": "wasp sting treatment",
            "cause": "alkaline (basic) venom injected into skin tissue",
            "remedy": "dilute vinegar or lemon juice (mild household acid)",
            "reaction": "The mild acid neutralizes the alkaline venom, relieving pain and inflammation."
        },
        {
            "context": "agricultural acidic soil treatment",
            "cause": "soil acidified by acid rain or intensive fertilizer use (pH < 5,5)",
            "remedy": "agricultural lime (calcium carbonate / slaked lime, a base)",
            "reaction": "The lime base neutralizes soil acidity, restoring optimal nutrient absorption for crop roots."
        }
    ]
    scen = r.choice(scenarios)

    prompt = (
        f"A practical application of chemistry involves managing **{scen['context']}** caused by {scen['cause']}.\n\n"
        f"1. Complete the general word equation for a neutralization reaction:\n"
        f"   $$\\text{{Acid}} + \\text{{Base}} \\longrightarrow \\text{{[ ? ]}} + \\text{{[ ? ]}}$$\n"
        f"2. Suggest a suitable household or agricultural remedy to treat this condition.\n"
        f"3. Explain the scientific reason why this remedy is effective in terms of neutralization. (2)"
    )

    memo = (
        f"Step 1: Word equation for neutralization:\n"
        f"$$\\text{{Acid}} + \\text{{Base}} \\longrightarrow \\text{{Salt}} + \\text{{Water}}$$ [2]\n\n"
        f"Step 2: Recommended remedy:\n"
        f"{scen['remedy']} [1]\n\n"
        f"Step 3: Scientific mechanism:\n"
        f"{scen['reaction']} [2]"
    )

    correct_ans = f"1. Salt + Water; 2. {scen['remedy']}; 3. {scen['reaction']}"

    return {
        "id": _make_id("ns7_neutralize", seed, idx),
        "prompt": prompt,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 6,
        "subskill": "neutralization_applications",
        "question_type": "short_answer",
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "canonical_solution": memo,
        "explanation": memo,
        "marks": 5,
        "hints": {
            "tier_1": "When an acid and a base combine, they cancel each other out in a neutralization reaction.",
            "tier_2": "The products of neutralizing an acid and a base are always a salt and water.",
            "tier_3": f"Products: Salt and Water. Explanation: {scen['reaction']}"
        },
        "misconception_tags": ["treated_acid_sting_with_acid", "neutralization_products_misconception"],
        "marking_schema": {
            "total_marks": 5,
            "marking_points": [
                {"id": "mp_1", "desc": "Product 1: Salt", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Product 2: Water", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": f"Remedy identified: {scen['remedy']}", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": f"Neutralization explanation: {scen['reaction']}", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


def _gen_acid_base_properties(r: random.Random, seed: Optional[int], idx: int) -> Dict[str, Any]:
    examples = [
        ("fresh lemon juice", "hand washing soap"),
        ("dilute vinegar", "milk of magnesia"),
        ("grapefruit juice", "bicarbonate of soda paste"),
        ("sour dairy buttermilk", "washing powder solution"),
    ]
    acid_ex, base_ex = r.choice(examples)

    prompt = (
        f"Acids and bases have distinct physical, sensory, and chemical characteristics.\n"
        f"A learner investigates household examples such as {acid_ex} (an acid) and {base_ex} (a base).\n\n"
        f"1. Compare the **taste** of an acid versus a base (e.g. {acid_ex} vs {base_ex}). (2)\n"
        f"2. Describe the **texture/feel** of an alkaline base when rubbed between fingertips. (1)\n"
        f"3. State one critical laboratory safety rule regarding the identification of unknown chemicals. (1)"
    )

    memo = (
        f"Step 1: Taste comparison:\n"
        f"- Acids have a **sour** taste (e.g. citrus fruit, vinegar) [1]\n"
        f"- Bases have a **bitter** taste [1]\n\n"
        f"Step 2: Feel of a base:\n"
        f"Bases feel **slippery** or **soapy** to the touch [1]\n\n"
        f"Step 3: Laboratory safety rule:\n"
        f"Learners must **never taste, smell directly, or touch** unknown laboratory chemicals because many acids and bases are corrosive or toxic; always use chemical indicators or meters instead. [1]"
    )

    correct_ans = "1. Acids taste sour; Bases taste bitter. 2. Bases feel slippery/soapy. 3. Never taste or touch chemicals; use indicators."

    return {
        "id": _make_id("ns7_properties", seed, idx),
        "prompt": prompt,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 5,
        "subskill": "acid_base_properties",
        "question_type": "short_answer",
        "correct_answer": correct_ans,
        "sample_answer": correct_ans,
        "canonical_solution": memo,
        "explanation": memo,
        "marks": 4,
        "hints": {
            "tier_1": "Think about lemons (sour acid) and soap or tonic water (bitter base).",
            "tier_2": "Bases react with skin oils to create a slippery, soapy sensation. Acids taste sour.",
            "tier_3": "1. Sour vs bitter. 2. Slippery/soapy. 3. Never taste/touch unknown chemicals."
        },
        "misconception_tags": ["sensory_testing_safety_violation", "taste_reversal_acid_base"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp_1", "desc": "Acid taste: sour", "marks": 1, "editable": True},
                {"id": "mp_2", "desc": "Base taste: bitter", "marks": 1, "editable": True},
                {"id": "mp_3", "desc": "Base feel: slippery / soapy", "marks": 1, "editable": True},
                {"id": "mp_4", "desc": "Safety rule: never taste or touch unknown lab chemicals", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        }
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master entry point for Grade 7 Acids, Bases and Neutrals."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    target_sub = str(subskill or "").strip().lower()

    def _build_one(sub_name: str, idx: int) -> Dict[str, Any]:
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if "ph_class" in sub_name or sub_name == "ph_classification":
            return _gen_ph_classification(sub_r, sub_seed, idx)
        elif "litmus" in sub_name or sub_name == "litmus_indicators":
            return _gen_litmus_indicators(sub_r, sub_seed, idx)
        elif "universal" in sub_name or sub_name == "universal_indicator":
            return _gen_universal_indicator(sub_r, sub_seed, idx)
        elif "neutraliz" in sub_name or sub_name == "neutralization_applications":
            return _gen_neutralization_applications(sub_r, sub_seed, idx)
        elif "property" in sub_name or "properties" in sub_name or sub_name == "acid_base_properties":
            return _gen_acid_base_properties(sub_r, sub_seed, idx)
        else:
            return _gen_ph_classification(sub_r, sub_seed, idx)

    if target_sub and target_sub not in ("compound", "all", "mixed", "auto", "default", "none"):
        for i in range(count):
            questions.append(_build_one(target_sub, i))
        return questions

    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        questions.append(_build_one(sub, i))

    return questions
