"""Grade 9 Natural Sciences - Reactions of Acids and Bases: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/PDF - Reactions of Acids and bases.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _fmt_num(val: float, decimals: int = 1) -> str:
    """Format a decimal using South African comma notation."""
    return f"{val:.{decimals}f}".replace(".", ",")


def _q(
    rng: random.Random,
    code: str,
    subskill: str,
    prompt: str,
    correct: str,
    sol: str,
    marks: int,
    qtype: str,
    tags: List[str],
    tier1: str,
    tier2: str,
    tier3: str,
    options: Optional[List[str]] = None,
    diagram_spec: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    guide = f"Marking Guide ({marks} marks): Award credit for each verified scientific step shown in the solution."
    item: Dict[str, Any] = {
        "id": f"ns9_rab_{code}_{rng.randint(100000, 999999)}",
        "subskill": subskill,
        "question_type": qtype,
        "prompt": prompt,
        "question": prompt,
        "question_text": prompt,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": marks,
        "marking_schema": guide,
        "marking_guide": guide,
        "term": 2,
        "caps_weight_percent": 15,
        "suggested_duration_mins": max(3, marks + 1),
        "hints": {"tier_1": tier1, "tier_2": tier2, "tier_3": tier3},
        "misconception_tags": tags,
    }
    if options is not None:
        item["options"] = options
    if diagram_spec is not None:
        item["diagram_spec"] = diagram_spec
    return item


def _svg_ph_curve_beaker(rng: random.Random, start_ph: float, drops_mid: int, end_ph: float, base_name: str) -> Dict[str, Any]:
    """Parameterized pH change curve during acid-base neutralisation."""
    y_start = int(175 - (start_ph / 14.0) * 140)
    y_mid = int(175 - (7.0 / 14.0) * 140)
    y_end = int(175 - (end_ph / 14.0) * 140)
    x_mid = 110 + drops_mid * 8
    svg = (
        f'<svg viewBox="0 0 420 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="210" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<line x1="55" y1="25" x2="55" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="55" y1="175" x2="395" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="55" y1="{y_mid}" x2="390" y2="{y_mid}" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="5,4"/>'
        f'<text x="394" y="{y_mid + 4}" font-size="11" fill="#15803d" text-anchor="end">pH 7 (Neutral)</text>'
        f'<text x="48" y="39" font-size="11" fill="#334155" text-anchor="end">14</text>'
        f'<text x="48" y="{y_mid + 4}" font-size="11" fill="#334155" text-anchor="end">7</text>'
        f'<text x="48" y="178" font-size="11" fill="#334155" text-anchor="end">0</text>'
        f'<text x="20" y="105" font-size="12" fill="#0f172a" transform="rotate(-90 20 105)" text-anchor="middle">pH</text>'
        f'<text x="225" y="198" font-size="11" fill="#0f172a" text-anchor="middle">Vinegar added to {base_name} (drops)</text>'
        f'<path d="M 65 {y_start} Q {x_mid - 20} {y_start + 8}, {x_mid} {y_mid} T 370 {y_end}" fill="none" stroke="#2563eb" stroke-width="3"/>'
        f'<circle cx="65" cy="{y_start}" r="4" fill="#1d4ed8"/>'
        f'<circle cx="{x_mid}" cy="{y_mid}" r="4.5" fill="#16a34a"/>'
        f'<circle cx="370" cy="{y_end}" r="4" fill="#dc2626"/>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_co2_straw_test(rng: random.Random, indicator: str, colour_before: str, colour_after: str) -> Dict[str, Any]:
    """Parameterized flask/beaker setup with learner exhaling through straw."""
    tube_x = rng.choice([190, 200, 210])
    liq_fill = "#bfdbfe" if "lime" in indicator.lower() else "#bbf7d0"
    svg = (
        f'<svg viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="400" height="210" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<rect x="145" y="70" width="110" height="115" rx="6" fill="none" stroke="#0f172a" stroke-width="2.5"/>'
        f'<rect x="148" y="125" width="104" height="58" rx="3" fill="{liq_fill}" opacity="0.8"/>'
        f'<line x1="{tube_x + 45}" y1="25" x2="{tube_x}" y2="160" stroke="#475569" stroke-width="5" stroke-linecap="round"/>'
        f'<circle cx="{tube_x - 8}" cy="148" r="4" fill="#ffffff" stroke="#334155"/>'
        f'<circle cx="{tube_x + 12}" cy="138" r="3" fill="#ffffff" stroke="#334155"/>'
        f'<text x="270" y="38" font-size="12" fill="#0f172a">Exhaled air (CO2)</text>'
        f'<text x="200" y="200" font-size="11" fill="#334155" text-anchor="middle">{indicator}: {colour_before} -> {colour_after}</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_evaporation_setup(rng: random.Random, salt_name: str, formula: str) -> Dict[str, Any]:
    """Parameterized evaporating basin over Bunsen burner / tripod setup."""
    flame_h = rng.choice([34, 38, 42])
    svg = (
        f'<svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="400" height="220" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<path d="M 145 72 Q 200 105 255 72 Z" fill="#f1f5f9" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="135" y="95" width="130" height="5" fill="#64748b"/>'
        f'<line x1="145" y1="100" x2="128" y2="185" stroke="#334155" stroke-width="3"/>'
        f'<line x1="255" y1="100" x2="272" y2="185" stroke="#334155" stroke-width="3"/>'
        f'<rect x="192" y="{150 - flame_h + 30}" width="16" height="45" fill="#475569"/>'
        f'<polygon points="200,{145 - flame_h} 191,150 209,150" fill="#3b82f6" opacity="0.85"/>'
        f'<path d="M 178 62 Q 173 46 181 34" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="3,3"/>'
        f'<path d="M 222 62 Q 227 46 219 34" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="3,3"/>'
        f'<text x="275" y="65" font-size="11" fill="#0f172a">Evaporating dish</text>'
        f'<text x="275" y="42" font-size="11" fill="#64748b">Steam escaping</text>'
        f'<text x="200" y="206" font-size="11" fill="#0f172a" text-anchor="middle">Recovering {salt_name} ({formula}) crystals</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_01_neutralisation_definition_and_ph_shift(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("hydrochloric acid", "sodium hydroxide", "decreases towards 7", "increases towards 7"),
        ("ethanoic acid (vinegar)", "sodium bicarbonate", "decreases towards 7", "increases towards 7"),
        ("sulfuric acid", "potassium hydroxide", "decreases towards 7", "increases towards 7"),
    ])
    acid, base, base_shift, acid_shift = pair
    mode_dir = rng.choice(["acid_to_base", "base_to_acid"])
    if mode_dir == "acid_to_base":
        prompt = (
            f"A learner measures the pH of a solution of **{base}** and slowly adds small portions of **{acid}** while stirring.\n\n"
            "1. Define a **neutralisation reaction** [2].\n"
            f"2. Describe what happens to the pH of the {base} solution as the {acid} is added [1].\n"
            "3. State the pH value of a completely neutral mixture [1]."
        )
        correct = f"A chemical reaction where an acid and base react so acidity and basicity cancel out forming salt and water; pH {base_shift}; Neutral pH = 7"
        sol = (
            "**Step 1:** A **neutralisation reaction** occurs when an acid and a base react with one another in the correct proportions so that the acid loses its acidity and the base loses its basicity, forming a salt and water [2].\n\n"
            f"**Step 2:** Because the {base} starts above pH 7 and an acid is added, the pH **{base_shift}** [1].\n\n"
            "**Step 3:** A completely neutral aqueous mixture has **pH = 7** [1]."
        )
    else:
        prompt = (
            f"A learner measures the pH of dilute **{acid}** in a beaker and slowly adds small amounts of **{base}**.\n\n"
            "1. Define a **neutralisation reaction** [2].\n"
            f"2. State how the pH of the {acid} changes as {base} is added [1].\n"
            "3. Identify the pH value at the exact point of neutralisation [1]."
        )
        correct = f"Reaction between an acid and a base forming a salt and water while cancelling acidity and basicity; pH {acid_shift}; pH = 7"
        sol = (
            "**Step 1:** **Neutralisation** is a chemical reaction in which an acid and a base react so that their acidic and basic properties cancel each other out, producing a salt and water [2].\n\n"
            f"**Step 2:** Adding basic {base} to acidic {acid} causes the pH to **{acid_shift}** [1].\n\n"
            "**Step 3:** Exact neutralisation occurs at **pH = 7** [1]."
        )
    return _q(
        rng, "01", "01_neutralisation_definition_and_ph_shift", prompt, correct, sol, 4, "structured",
        ["neutralisation_always_makes_ph_0_error"],
        "Mixing an acid and a base moves the pH towards the middle of the pH scale.",
        f"Remember acids have pH < 7, bases have pH > 7, and neutral mixtures sit at pH 7.",
        correct,
    )


def arch_02_acidic_basic_neutral_ph_boundaries(rng: random.Random) -> Dict[str, Any]:
    cases = [
        (_fmt_num(rng.choice([2.4, 3.1, 4.8])), "Acidic", "lower than 7 (more strongly acidic as pH drops toward 0)"),
        (_fmt_num(rng.choice([8.5, 9.6, 11.2])), "Basic (alkaline)", "greater than 7 (more strongly basic as pH rises toward 14)"),
        ("7,0", "Neutral", "equal to 7 (neither acidic nor basic)"),
    ]
    ph_str, category, rule = rng.choice(cases)
    prompt = (
        f"A Grade 9 chemistry test tube contains a clear aqueous sample tested with a pH meter, reading **pH {ph_str}**.\n\n"
        f"1. Classify the sample as **acidic**, **basic (alkaline)**, or **neutral** [1].\n"
        "2. Explain the pH boundary rule used to make this classification [2]."
    )
    correct = f"{category}; {rule}"
    sol = (
        f"**Step 1:** At pH {ph_str}, the solution is **{category}** [1].\n\n"
        f"**Step 2:** On the pH scale (0–14), solutions with pH < 7 are acidic, pH = 7 are neutral, and pH > 7 are basic; here it is {rule} [2]."
    )
    return _q(
        rng, "02", "02_acidic_basic_neutral_ph_boundaries", prompt, correct, sol, 3, "short_answer",
        ["higher_ph_means_stronger_acid_myth"],
        "Compare the measured pH directly against 7, the neutral midpoint.",
        "Below 7 = acid, equal to 7 = neutral, above 7 = base.",
        correct,
    )


def arch_03_exchange_reaction_ion_swap_concept(rng: random.Random) -> Dict[str, Any]:
    acid, base, salt = rng.choice([
        ("hydrochloric acid (HCl)", "sodium hydroxide (NaOH)", "sodium chloride (NaCl)"),
        ("hydrochloric acid (HCl)", "potassium hydroxide (KOH)", "potassium chloride (KCl)"),
        ("nitric acid (HNO3)", "sodium hydroxide (NaOH)", "sodium nitrate (NaNO3)"),
    ])
    prompt = (
        f"When **{acid}** reacts with **{base}**, hydrogen ions from the acid pair with hydroxide ions from the base to make water, while the metal cation pairs with the acid's anion to form **{salt}**.\n\n"
        "Why is this reaction classified as an **exchange reaction**?"
    )
    correct = "Reactants swap chemical partners: hydrogen from the acid combines with hydroxide/oxide from the base to make water, while the metal combines with the non-metal part of the acid to form a salt."
    distractors = [
        "Only heat is exchanged with the beaker walls without any bonds breaking or new substances forming.",
        "One metal atom turns directly into a non-metal gas inside the nucleus.",
        "Oxygen gas leaves the liquid and is replaced by nitrogen bubbles from the room air.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** In neutralisation, chemical partners are **exchanged** between the acid and base.\n"
        f"**Step 2:** Specifically, $H^+$ from {acid} swaps with the metal ion in {base} to produce water ($H_2O$) and the salt **{salt}** [2]."
    )
    return _q(
        rng, "03", "03_exchange_reaction_ion_swap_concept", prompt, correct, sol, 2, "multiple_choice",
        ["neutralisation_is_physical_dilution_myth"],
        "Notice how parts of the two reactants trade places to create two new compounds.",
        "Acid's hydrogen + base's oxygen/hydroxide -> water; Base's metal + acid's non-metal part -> salt.",
        correct, options=options,
    )


def arch_04_universal_indicator_colour_transition_sequence(rng: random.Random) -> Dict[str, Any]:
    start_state = rng.choice([
        ("strong base (pH 13)", "purple / violet", "strong acid (pH 1)", "violet -> blue -> green -> yellow -> orange -> red"),
        ("strong acid (pH 2)", "red / orange", "strong base (pH 12)", "red -> orange -> yellow -> green -> blue -> violet"),
    ])
    s_desc, s_col, target, seq = start_state
    prompt = (
        f"Universal indicator is added to a beaker containing a **{s_desc}** (initial colour: **{s_col}**). Another reagent is added drop by drop until the mixture reaches a **{target}**.\n\n"
        "1. State the colour of universal indicator at the exact **neutral point (pH 7)** [1].\n"
        "2. List the sequence of colours observed from start to finish [2]."
    )
    correct = f"Green at pH 7; Colour sequence: {seq}"
    sol = (
        "**Step 1:** Universal indicator turns **green** at pH 7 (neutral) [1].\n\n"
        f"**Step 2:** Following the universal indicator spectrum across pH 0–14 gives: **{seq}** [2]."
    )
    return _q(
        rng, "04", "04_universal_indicator_colour_transition_sequence", prompt, correct, sol, 3, "short_answer",
        ["universal_indicator_green_is_acid_error"],
        "Recall the rainbow order ROYGBV along the pH scale (0 red to 14 violet).",
        "Neutral sits in the middle of the rainbow at green (pH 7).",
        correct,
    )


def arch_05_indicator_drop_transfer_laboratory_technique(rng: random.Random) -> Dict[str, Any]:
    beaker_count = rng.choice([3, 4, 5])
    tool = rng.choice(["clean glass rod", "clean plastic drinking straw", "dropper pipette"])
    prompt = (
        f"Before adding acid portions across {beaker_count} trials, a learner arranges 1 cm strips of dry universal indicator paper on white paper and transfers **one drop** using a **{tool}** instead of dipping the strip directly into the test beaker.\n\n"
        "Explain **two scientific reasons** for using this drop-transfer method rather than dipping indicator paper directly into the whole solution [2]."
    )
    correct = "Prevents contaminating or colouring the main test solution with dissolved indicator dye, and keeps previous drops separated on labelled white paper for accurate side-by-side colour comparison."
    sol = (
        "**Step 1:** Dipping paper directly into the beaker leaches indicator dyes into the reaction mixture, **contaminating** future pH readings [1].\n\n"
        "**Step 2:** Placing single drops onto separate 1 cm strips on white paper preserves a clear **chronological colour record** and provides a uniform white background for colour matching [1]."
    )
    return _q(
        rng, "05", "05_indicator_drop_transfer_laboratory_technique", prompt, correct, sol, 2, "short_answer",
        ["dipping_indicator_paper_contaminates_sample"],
        "Think about keeping the bulk test mixture clean and keeping each time-point visible.",
        "One avoids polluting the beaker with dye; the other preserves each pH strip on white paper for comparison.",
        correct,
    )


def arch_06_vinegar_baking_soda_investigative_question_hypothesis(rng: random.Random) -> Dict[str, Any]:
    step_focus = rng.choice(["investigative_question", "hypothesis"])
    teaspoons_water = rng.choice([8, 10, 12])
    if step_focus == "investigative_question":
        prompt = (
            f"A class prepares a baking soda solution by dissolving one teaspoon of baking soda in {teaspoons_water} teaspoons of water, then plans to add vinegar in small equal portions while measuring pH.\n\n"
            "Write a clear, testable **investigative question** identifying both the independent and dependent variables [2]."
        )
        correct = "How does adding increasing portions (volume) of vinegar to a baking soda solution affect the pH of the mixture?"
        sol = (
            "**Step 1:** A valid investigative question asks about a relationship without a simple 'yes/no' answer and names both variables [1].\n\n"
            "**Step 2:** Question: *\"How does the volume (number of portions) of vinegar added to a baking soda solution affect the pH of the resulting mixture?\"* [1]."
        )
    else:
        prompt = (
            f"A learner tests 1 teaspoon of baking soda dissolved in {teaspoons_water} teaspoons of water (starting pH approx 8,5) and predicts what will happen as small portions of vinegar (pH approx 3) are stirred in.\n\n"
            "Formulate a scientifically valid **hypothesis** describing the expected trend in pH [2]."
        )
        correct = "If small portions of acidic vinegar are added to the basic baking soda solution, the pH of the mixture will decrease towards 7 (and below 7 if excess vinegar is added)."
        sol = (
            "**Step 1:** Vinegar is acidic (pH < 7) while baking soda solution is weakly basic (pH > 7) [1].\n\n"
            "**Step 2:** Hypothesis: *\"As more portions of vinegar are added to the baking soda solution, the pH will steadily decrease from basic towards neutral (pH 7), eventually becoming acidic below 7 when excess vinegar is added.\"* [1]."
        )
    return _q(
        rng, "06", "06_vinegar_baking_soda_investigative_question_hypothesis", prompt, correct, sol, 2, "short_answer",
        ["investigative_question_yes_no_error"],
        "Mention both what is changed (portions/volume of vinegar) and what is measured (pH).",
        "Use the pattern: 'How does [independent variable] affect [dependent variable]?' or 'As ... increases, ... decreases'.",
        correct,
    )


def arch_07_vinegar_baking_soda_effervescence_and_ph_graph(rng: random.Random) -> Dict[str, Any]:
    start_ph = rng.choice([8.5, 9.0, 9.5])
    drops_mid = rng.choice([12, 16, 20])
    end_ph = rng.choice([3.5, 4.0, 4.5])
    prompt = (
        f"Study the pH titration plot for a dilute baking soda solution as vinegar drops are added until the mixture reaches **pH {_fmt_num(end_ph)}**.\n\n"
        f"1. State the starting pH of the baking soda solution and classify it [2].\n"
        f"2. How many drops of vinegar were needed to reach the exact neutralisation point? [1]\n"
        "3. Identify the gas responsible for the bubbling (effervescence) seen as vinegar reacts with baking soda [1]."
    )
    svg = (
        f'<svg viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="220" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<line x1="60" y1="25" x2="60" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="60" y1="175" x2="395" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="60" y1="100" x2="390" y2="100" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="5,4"/>'
        f'<line x1="220" y1="100" x2="220" y2="175" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>'
        f'<text x="52" y="34" font-size="11" fill="#334155" text-anchor="end">14</text>'
        f'<text x="52" y="104" font-size="11" fill="#15803d" text-anchor="end">7</text>'
        f'<text x="52" y="178" font-size="11" fill="#334155" text-anchor="end">0</text>'
        f'<text x="65" y="191" font-size="11" fill="#334155" text-anchor="middle">0</text>'
        f'<text x="220" y="191" font-size="11" fill="#15803d" font-weight="bold" text-anchor="middle">{drops_mid}</text>'
        f'<text x="375" y="191" font-size="11" fill="#334155" text-anchor="middle">{drops_mid * 2}</text>'
        f'<text x="225" y="210" font-size="11" fill="#0f172a" text-anchor="middle">Vinegar added (drops)</text>'
        f'<text x="72" y="{int(175 - (start_ph / 14.0) * 140) - 8}" font-size="11" fill="#1d4ed8">pH {_fmt_num(start_ph)}</text>'
        f'<path d="M 65 {int(175 - (start_ph / 14.0) * 140)} Q 160 {int(175 - (start_ph / 14.0) * 140) + 12}, 220 100 T 375 {int(175 - (end_ph / 14.0) * 140)}" fill="none" stroke="#2563eb" stroke-width="3"/>'
        f'<circle cx="65" cy="{int(175 - (start_ph / 14.0) * 140)}" r="4" fill="#1d4ed8"/>'
        f'<circle cx="220" cy="100" r="5" fill="#16a34a"/>'
        f'<circle cx="375" cy="{int(175 - (end_ph / 14.0) * 140)}" r="4" fill="#dc2626"/>'
        f'</svg>'
    )
    spec = {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}
    correct = f"pH {_fmt_num(start_ph)} (weakly basic); {drops_mid} drops; Carbon dioxide (CO2)"
    sol = (
        f"**Step 1:** At 0 drops, the baking soda solution begins at **pH {_fmt_num(start_ph)}**, which is **basic** (pH > 7) [2].\n\n"
        f"**Step 2:** The curve crosses the dashed green neutral line (pH = 7) at **{drops_mid} drops** of vinegar [1].\n\n"
        "**Step 3:** Baking soda is a hydrogen carbonate/bicarbonate, so reacting with ethanoic acid releases bubbles of **carbon dioxide ($\\text{CO}_2$)** gas [1]."
    )
    return _q(
        rng, "07", "07_vinegar_baking_soda_effervescence_and_ph_graph", prompt, correct, sol, 4, "structured",
        ["baking_soda_bubbles_are_oxygen_myth"],
        "Read the start point at 0 drops and trace across from pH 7 to find the neutralisation volume.",
        "Carbonates and bicarbonates produce CO2 bubbles when treated with acids.",
        correct, diagram_spec=spec,
    )


def arch_08_baking_soda_sodium_bicarbonate_basic_character(rng: random.Random) -> Dict[str, Any]:
    common_name, chem_name, formula = rng.choice([
        ("baking soda", "sodium hydrogen carbonate", "NaHCO3"),
        ("bicarbonate of soda", "sodium bicarbonate", "NaHCO3"),
    ])
    col = rng.choice(["blue-green", "blue", "teal-blue"])
    prompt = (
        f"A learner dissolves **{common_name}** (chemical name: **{chem_name}**, formula $\\text{{{formula}}}$) in water and obtains a **{col}** colour on universal indicator paper (pH approx 8,5).\n\n"
        "1. Explain why baking soda solution neutralises acids such as vinegar or citric acid [2].\n"
        "2. State what three products form when ethanoic acid reacts with sodium bicarbonate [2]."
    )
    correct = "Baking soda is basic (pH > 7) so it accepts H+ and neutralises acids; Products: sodium ethanoate (a salt), water, and carbon dioxide gas"
    sol = (
        "**Step 1:** Dissolved baking soda produces a **basic solution (pH > 7)** that reacts chemically with acids, decreasing acidity until neutralisation [2].\n\n"
        "**Step 2:** Because it is a hydrogen carbonate, the products are a **salt** (sodium ethanoate), **water**, and **carbon dioxide** gas [2]."
    )
    return _q(
        rng, "08", "08_baking_soda_sodium_bicarbonate_basic_character", prompt, correct, sol, 4, "structured",
        ["baking_soda_is_acidic_myth"],
        "Compare its pH (~8,5) to 7 and recall the carbonate/bicarbonate + acid products.",
        "Carbonate + acid -> salt + water + carbon dioxide.",
        correct,
    )


def arch_09_stoichiometric_excess_acid_vs_excess_base_final_ph(rng: random.Random) -> Dict[str, Any]:
    vol_hcl = rng.choice([20, 25, 30])
    vol_naoh = rng.choice([10, 15, 35, 45])
    while vol_naoh == vol_hcl:
        vol_naoh = rng.choice([10, 15, 35, 45])
    if vol_hcl > vol_naoh:
        excess = "hydrochloric acid (HCl)"
        ph_range = "below 7 (acidic)"
        ind_col = "red / orange"
    else:
        excess = "sodium hydroxide (NaOH)"
        ph_range = "above 7 (basic / alkaline)"
        ind_col = "blue / violet"
    prompt = (
        "Hydrochloric acid and sodium hydroxide of **equal concentration (strength)** neutralise each other in a 1 : 1 volume ratio.\n"
        f"Suppose **{vol_hcl} ml** of $\\text{{HCl}}$ is mixed with **{vol_naoh} ml** of $\\text{{NaOH}}$.\n\n"
        "1. Does neutralisation ALWAYS result in a final mixture with pH = 7? Explain using this mixture [2].\n"
        "2. State the expected universal indicator colour of the final mixture [1]."
    )
    correct = f"No; {excess} is in excess, so the final pH will be {ph_range}; Universal indicator colour: {ind_col}"
    sol = (
        f"**Step 1:** **No** — mixing equal strengths only reaches pH 7 when balanced quantities react completely. Here, **{excess}** is in excess, leaving unreacted particles so the final pH is **{ph_range}** [2].\n\n"
        f"**Step 2:** Universal indicator therefore turns **{ind_col}** [1]."
    )
    return _q(
        rng, "09", "09_stoichiometric_excess_acid_vs_excess_base_final_ph", prompt, correct, sol, 3, "structured",
        ["mixing_acid_and_base_always_gives_ph_7_myth"],
        "Compare the volumes of equal-strength HCl and NaOH added.",
        "Whichever reactant is in excess determines whether the final mixture remains acidic (<7) or basic (>7).",
        correct,
    )


def arch_10_strength_potency_vs_volume_in_neutralisation(rng: random.Random) -> Dict[str, Any]:
    vol_base = rng.choice([50, 100])
    drops_weak = rng.choice([40, 50])
    drops_strong = rng.choice([8, 10])
    prompt = (
        f"Two learners neutralise identical **{vol_base} ml** samples of potassium hydroxide solution. "
        f"Learner A uses dilute lemon juice (needs **{drops_weak} drops**), whereas Learner B uses concentrated hydrochloric acid (needs only **{drops_strong} drops**).\n\n"
        "Identify **two key factors** (apart from temperature) that determine the final pH when mixing an acid and a base."
    )
    correct = "The relative strengths/concentrations (potency) of the acid and base solutions, and the exact volume/amount of each reactant mixed."
    distractors = [
        "Only the shape of the glass beaker and the colour of the wooden laboratory bench.",
        "Only the boiling point of water and the mass of the universal indicator strip.",
        "Only whether the base was poured before the acid without considering concentration or volume.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Final pH depends on both **concentration/strength (potency)** of the acid and base and the **amounts (volumes)** mixed.\n"
        f"**Step 2:** Concentrated HCl delivers far more reacting acid particles per drop ({drops_strong} drops vs {drops_weak} drops of weak lemon juice) [2]."
    )
    return _q(
        rng, "10", "10_strength_potency_vs_volume_in_neutralisation", prompt, correct, sol, 2, "multiple_choice",
        ["volume_alone_determines_neutralisation_myth"],
        "Think about why concentrated HCl needed fewer drops than weak lemon juice.",
        "Both concentration (strength) and volume added control whether H+ matches OH-.",
        correct, options=options,
    )


def arch_11_non_metal_oxides_form_acidic_solutions(rng: random.Random) -> Dict[str, Any]:
    nonmetal, oxide_name, oxide_f, acid_name, acid_f = rng.choice([
        ("carbon", "carbon dioxide", "CO2", "carbonic acid", "H2CO3"),
        ("sulfur", "sulfur dioxide", "SO2", "sulfurous acid", "H2SO3"),
        ("nitrogen", "nitrogen dioxide", "NO2", "nitric acid", "HNO3"),
    ])
    prompt = (
        f"When the non-metal **{nonmetal}** burns in oxygen, it produces the non-metal oxide **{oxide_name}** ($\\text{{{oxide_f}}}$), which then dissolves in pure water.\n\n"
        "1. Predict whether the resulting aqueous solution is **acidic** (pH < 7) or **basic** (pH > 7) [1].\n"
        f"2. Name the acid formed when {oxide_name} reacts with water [1].\n"
        "3. State the general rule linking non-metal oxides with pH [1]."
    )
    correct = f"Acidic (pH < 7); {acid_name} ({acid_f}); Non-metal oxides dissolve in water to form acidic solutions"
    sol = (
        f"**Step 1:** Dissolved {oxide_name} lowers the water's pH below 7, making it **acidic** [1].\n\n"
        f"**Step 2:** The product formed is **{acid_name}** ($\\text{{{acid_f}}}$) [1].\n\n"
        "**Step 3:** General rule: **Non-metal oxides form acidic solutions** in water (pH < 7) [1]."
    )
    return _q(
        rng, "11", "11_non_metal_oxides_form_acidic_solutions", prompt, correct, sol, 3, "structured",
        ["nonmetal_oxides_form_bases_myth"],
        "Group 14–16 non-metals on the right of the Periodic Table form acidic oxides in water.",
        f"{oxide_name} dissolves in water to form {acid_name}, lowering pH below 7.",
        correct,
    )


def arch_12_carbon_dioxide_straw_exhalation_limewater_and_universal_indicator(rng: random.Random) -> Dict[str, Any]:
    colour_before = "green"
    colour_after = rng.choice(["yellow", "yellow-orange"])
    spec = _svg_co2_straw_test(rng, "Universal indicator water", colour_before, colour_after)
    prompt = (
        f"As illustrated in the diagram, a learner uses a drinking straw to blow gently through neutral tap water containing green universal indicator. After one minute, the solution changes to **{colour_after}**.\n\n"
        "1. Name the non-metal oxide gas in exhaled breath responsible for this colour change [1].\n"
        "2. Explain why the universal indicator shifted from green to yellow/orange [2]."
    )
    correct = f"Carbon dioxide (CO2); Exhaled CO2 dissolved in water to form carbonic acid (H2CO3), lowering the pH below 7"
    sol = (
        "**Step 1:** Exhaled human breath contains **carbon dioxide ($\\text{CO}_2$)** [1].\n\n"
        "**Step 2:** $\\text{CO}_2$ dissolves in water to form weak **carbonic acid** ($\\text{H}_2\\text{CO}_3$), dropping the pH below 7 and shifting universal indicator from green to yellow-orange [2]."
    )
    return _q(
        rng, "12", "12_carbon_dioxide_straw_exhalation_limewater_and_universal_indicator", prompt, correct, sol, 3, "short_answer",
        ["exhaled_air_makes_water_basic_myth"],
        "Identify the gas humans breathe out and remember what happens when it dissolves in water.",
        "CO2 + H2O -> H2CO3 lowers pH below 7 -> yellow/orange universal indicator.",
        correct, diagram_spec=spec,
    )


def arch_13_carbonic_acid_formation_and_fizzy_drinks(rng: random.Random) -> Dict[str, Any]:
    drink = rng.choice(["sparkling water", "fizzy soda", "soda stream water"])
    prompt = (
        f"During bottling, carbon dioxide gas is forced under pressure into pure water to create **{drink}**.\n\n"
        "1. Write the **word equation** and **balanced chemical equation** for $\\text{CO}_2$ dissolving in water [2].\n"
        "2. Would fresh sparkling water turn universal indicator red/yellow or blue? Give a reason [2]."
    )
    correct = "Carbon dioxide + Water -> Carbonic acid; CO2 + H2O -> H2CO3; Yellow/orange (acidic, pH < 7) because carbonic acid forms"
    sol = (
        "**Step 1:** Word equation: **Carbon dioxide + Water $\\rightarrow$ Carbonic acid**. Balanced equation: **$\\text{CO}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{H}_2\\text{CO}_3$** [2].\n\n"
        f"**Step 2:** {drink.capitalize()} contains dissolved carbonic acid ($\\text{{pH}} \\approx 4$), turning universal indicator **yellow/orange** (acidic) [2]."
    )
    return _q(
        rng, "13", "13_carbonic_acid_formation_and_fizzy_drinks", prompt, correct, sol, 4, "structured",
        ["carbonic_acid_formula_error"],
        "Combine the atoms of 1 CO2 molecule and 1 H2O molecule together.",
        "H2 + C + O3 = H2CO3 (carbonic acid).",
        correct,
    )


def arch_14_industrial_emissions_and_acid_rain_formation(rng: random.Random) -> Dict[str, Any]:
    source = rng.choice(["Mpumalanga coal-fired power stations", "metal smelting furnaces", "heavy diesel vehicle exhaust"])
    prompt = (
        f"Smoke plumes from **{source}** release non-metal oxide gases such as **sulfur dioxide ($\\text{{SO}}_2$)** and **nitrogen oxides ($\\text{{NO}}_2$)** into the atmosphere.\n\n"
        "1. Explain step-by-step how these gases cause **acid rain** [2].\n"
        "2. Name **two strong acids** commonly formed inside rain droplets from these emissions [2]."
    )
    correct = "Non-metal oxides dissolve and react with atmospheric water vapour/oxygen in clouds to form acidic solutions that fall as precipitation (pH < 5,6); Sulfuric acid (H2SO4) and Nitric acid (HNO3)"
    sol = (
        f"**Step 1:** Non-metal oxides ($\\text{{SO}}_2$ and $\\text{{NO}}_2$) from {source} rise into clouds, dissolve and react with water vapour and oxygen to form acidic solutions, falling as **acid rain** [2].\n\n"
        "**Step 2:** The principal mineral acids formed are **sulfuric acid ($\\text{H}_2\\text{SO}_4$)** and **nitric acid ($\\text{HNO}_3$)** [2]."
    )
    return _q(
        rng, "14", "14_industrial_emissions_and_acid_rain_formation", prompt, correct, sol, 4, "structured",
        ["acid_rain_caused_by_hcl_only_myth"],
        "Remember that sulfur and nitrogen are non-metals whose oxides react with cloud moisture.",
        "SO2 -> sulfuric acid (H2SO4); NO2 -> nitric acid (HNO3).",
        correct,
    )


def arch_15_acid_rain_environmental_and_limestone_building_damage(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice([
        ("historic marble and sandstone monuments", "reacting chemically with calcium carbonate in the stone, eroding sculptures and facades"),
        ("Highveld freshwater dams and streams", "lowering river pH below healthy tolerances, killing fish eggs and aquatic invertebrates"),
        ("natural forest soils", "leaching essential mineral nutrients and damaging tree root hairs and leaves"),
    ])
    site, effect = target
    prompt = (
        f"Regions downwind of industrial emissions frequently experience **acid rain** (pH 3,5–4,8).\n\n"
        f"Explain clearly how acid rain damages **{site}**, naming the chemical reaction type when stone or lime-rich structures are attacked [3]."
    )
    correct = f"Acid rain harms {site} by {effect}; Acid-carbonate neutralisation reaction"
    sol = (
        f"**Step 1:** Acid rain harms {site} by **{effect}** [2].\n\n"
        "**Step 2:** Specifically on limestone/marble ($\\text{CaCO}_3$), sulfuric or nitric acid undergoes an **acid-carbonate neutralisation reaction**, dissolving the rock into soluble salts and $\\text{CO}_2$ gas [1]."
    )
    return _q(
        rng, "15", "15_acid_rain_environmental_and_limestone_building_damage", prompt, correct, sol, 3, "short_answer",
        ["acid_rain_only_melts_plastic_myth"],
        "Focus on chemical weathering of carbonates (CaCO3) and acidification of ecosystems.",
        f"Explain the concrete impact on {site} and link stone corrosion to carbonate + acid reaction.",
        correct,
    )


def arch_16_metal_oxides_basic_character_magnesium_oxide_in_water(rng: random.Random) -> Dict[str, Any]:
    metal_ox, formula, ph_val = rng.choice([
        ("Magnesium oxide", "MgO", "9,5"),
        ("Calcium oxide", "CaO", "12,0"),
        ("Sodium oxide", "Na2O", "13,0"),
    ])
    prompt = (
        f"A small spatula of white **{metal_ox}** ($\\text{{{formula}}}$) powder is stirred into distilled water in a test tube and tested with universal indicator, giving **pH {ph_val}**.\n\n"
        "1. State whether metal oxides form **acidic** or **basic** solutions in water [1].\n"
        "2. State the universal indicator colour expected at pH " + ph_val + " [1].\n"
        "3. Contrast metal oxides with non-metal oxides on the Periodic Table [1]."
    )
    correct = "Basic (alkaline) solutions; Blue / violet-blue; Metal oxides are basic whereas non-metal oxides are acidic"
    sol = (
        f"**Step 1:** **Metal oxides** (such as {metal_ox}) form **basic** solutions when dissolved in water (pH > 7) [1].\n\n"
        f"**Step 2:** At pH {ph_val}, universal indicator turns **blue to purple/violet** [1].\n\n"
        "**Step 3:** Elements on the left of the Periodic Table (metals) yield **basic oxides**, while non-metals on the right yield **acidic oxides** [1]."
    )
    return _q(
        rng, "16", "16_metal_oxides_basic_character_magnesium_oxide_in_water", prompt, correct, sol, 3, "structured",
        ["metal_oxides_are_acidic_myth"],
        "Metals sit on the left of the Periodic Table and form basic hydroxides/oxides in water.",
        f"pH {ph_val} > 7 -> basic -> blue/violet indicator.",
        correct,
    )


def arch_17_acid_plus_metal_oxide_general_word_equation(rng: random.Random) -> Dict[str, Any]:
    acid, ox, salt = rng.choice([
        ("Hydrochloric acid", "zinc oxide", "zinc chloride"),
        ("Hydrochloric acid", "iron(III) oxide", "iron(III) chloride"),
        ("Sulfuric acid", "copper(II) oxide", "copper(II) sulfate"),
        ("Nitric acid", "magnesium oxide", "magnesium nitrate"),
    ])
    prompt = (
        f"When any **acid** reacts with a **metal oxide**, a neutralisation exchange reaction occurs.\n\n"
        "1. Write the **general word equation** for any acid reacting with a metal oxide [2].\n"
        f"2. Write the **specific word equation** for **{acid.lower()}** reacting with **{ox}** [2]."
    )
    correct = f"Acid + Metal oxide -> Salt + Water; {acid} + {ox} -> {salt} + Water"
    sol = (
        "**Step 1:** General word equation: **Acid + Metal oxide $\\rightarrow$ Salt + Water** (notice NO carbon dioxide and NO hydrogen gas is produced) [2].\n\n"
        f"**Step 2:** Specific word equation: **{acid} + {ox} $\\rightarrow$ {salt} + Water** [2]."
    )
    return _q(
        rng, "17", "17_acid_plus_metal_oxide_general_word_equation", prompt, correct, sol, 4, "structured",
        ["metal_oxide_acid_releases_hydrogen_myth"],
        "The oxygen in the metal oxide pairs with hydrogen from the acid to form water.",
        "Acid + Metal oxide -> Salt + Water (only two products!).",
        correct,
    )


def arch_18_hydrochloric_acid_plus_magnesium_oxide_equation(rng: random.Random) -> Dict[str, Any]:
    mass_desc = rng.choice(["0,4 g", "0,5 g", "1,0 g"])
    prompt = (
        f"A white magnesium ribbon is burned in air to form {mass_desc} of magnesium oxide ($\\text{{MgO}}$), which is then dissolved completely in excess dilute hydrochloric acid ($\\text{{HCl}}$).\n\n"
        "1. Write the **word equation** for this neutralisation reaction [1].\n"
        "2. Write the **balanced chemical equation** using formulas [3]."
    )
    correct = "Hydrochloric acid + Magnesium oxide -> Magnesium chloride + Water; 2HCl + MgO -> MgCl2 + H2O"
    sol = (
        "**Step 1:** Word equation: **Hydrochloric acid + Magnesium oxide $\\rightarrow$ Magnesium chloride + Water** [1].\n\n"
        "**Step 2:** Formulas: $\\text{HCl}$ and $\\text{MgO}$ yield $\\text{MgCl}_2$ + $\\text{H}_2\\text{O}$.\n"
        "Balancing Cl and H atoms requires coefficient 2 in front of $\\text{HCl}$:\n"
        "**$$2\\text{HCl} + \\text{MgO} \\rightarrow \\text{MgCl}_2 + \\text{H}_2\\text{O}$$** [3]."
    )
    return _q(
        rng, "18", "18_hydrochloric_acid_plus_magnesium_oxide_equation", prompt, correct, sol, 4, "structured",
        ["unbalanced_mgcl2_missing_2hcl_error"],
        "Magnesium has valency 2 (Mg2+), so magnesium chloride needs two Cl- ions: MgCl2.",
        "Balance 2 Cl atoms and 2 H atoms on the left using 2HCl + MgO -> MgCl2 + H2O.",
        correct,
    )


def arch_19_hydrochloric_acid_plus_calcium_and_copper_oxide_equations(rng: random.Random) -> Dict[str, Any]:
    case = rng.choice([
        ("calcium oxide", "CaO", "calcium chloride", "CaCl2", "2HCl + CaO -> CaCl2 + H2O", "clear colourless solution"),
        ("copper(II) oxide", "CuO", "copper(II) chloride", "CuCl2", "2HCl + CuO -> CuCl2 + H2O", "characteristic blue-green solution"),
    ])
    ox_name, ox_f, salt_name, salt_f, eq, obs = case
    prompt = (
        f"Warm hydrochloric acid ($\\text{{HCl}}$) reacts completely with solid **{ox_name}** ($\\text{{{ox_f}}}$), producing a {obs}.\n\n"
        f"Write the **balanced chemical equation** for this reaction and identify the **salt** formed [3]."
    )
    correct = f"{eq}; Salt: {salt_name} ({salt_f})"
    sol = (
        f"**Step 1:** Acid + metal oxide forms a salt and water: {salt_name} ($\\text{{{salt_f}}}$) and $\\text{{H}}_2\\text{{O}}$ [1].\n\n"
        f"**Step 2:** Balanced chemical equation: **$${eq}$$** [2]."
    )
    return _q(
        rng, "19", "19_hydrochloric_acid_plus_calcium_and_copper_oxide_equations", prompt, correct, sol, 3, "short_answer",
        ["salt_formula_omits_subscript_2_error"],
        "Both Ca2+ and Cu2+ carry a +2 charge, so the chloride salt formula has two Cl atoms.",
        f"2HCl supplies 2 H for H2O and 2 Cl for {salt_f}.",
        correct,
    )


def arch_20_alkali_soluble_metal_hydroxide_definition_and_examples(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("Sodium hydroxide (NaOH)", "Copper(II) oxide (CuO) — insoluble in water"),
        ("Potassium hydroxide (KOH)", "Calcium carbonate (CaCO3) — practically insoluble in water"),
    ])
    alk, insol = pair
    prompt = (
        "All **alkalis** are bases, yet not every base is classified as an alkali.\n\n"
        "1. Explain precisely what distinguishes an **alkali** from a general base [1].\n"
        f"2. Which substance is a true laboratory alkali: **{alk}** or **{insol}**? [1]"
    )
    correct = f"An alkali is a base that dissolves readily in water (typically soluble metal hydroxides like NaOH/KOH); {alk}"
    sol = (
        "**Step 1:** An **alkali** is a base that **dissolves in water** to form an alkaline solution (pH > 7) [1].\n\n"
        f"**Step 2:** **{alk}** dissolves readily in water and is a classic alkali, whereas {insol.lower()} [1]."
    )
    return _q(
        rng, "20", "20_alkali_soluble_metal_hydroxide_definition_and_examples", prompt, correct, sol, 2, "short_answer",
        ["all_bases_are_insoluble_or_alkali_myth"],
        "Remember: Alkalis = water-soluble bases (e.g. NaOH, KOH).",
        f"Soluble metal hydroxides like {alk.split()[0]} hydroxide dissolve completely in water -> alkali.",
        correct,
    )


def arch_21_acid_plus_metal_hydroxide_general_word_equation(rng: random.Random) -> Dict[str, Any]:
    hydroxide, acid, salt = rng.choice([
        ("lithium hydroxide", "hydrochloric acid", "lithium chloride"),
        ("potassium hydroxide", "nitric acid", "potassium nitrate"),
        ("sodium hydroxide", "sulfuric acid", "sodium sulfate"),
    ])
    prompt = (
        "Laboratory alkalis such as metal hydroxides react smoothly with aqueous acids without producing bubbles.\n\n"
        "1. State the **general word equation** for an acid reacting with a metal hydroxide [1].\n"
        f"2. Apply this rule to write the word equation for **{acid}** reacting with **{hydroxide}** [2]."
    )
    correct = f"Acid + Metal hydroxide -> Salt + Water; {acid.capitalize()} + {hydroxide} -> {salt.capitalize()} + Water"
    sol = (
        "**Step 1:** General word equation: **Acid + Metal hydroxide $\\rightarrow$ Salt + Water** [1].\n\n"
        f"**Step 2:** Specific word equation: **{acid.capitalize()} + {hydroxide} $\\rightarrow$ {salt.capitalize()} + Water** [2]."
    )
    return _q(
        rng, "21", "21_acid_plus_metal_hydroxide_general_word_equation", prompt, correct, sol, 3, "structured",
        ["hydroxide_neutralisation_produces_gas_error"],
        "Hydrogen ions from the acid join hydroxide (OH-) from the base to make H2O.",
        "Products are only salt + water (no gas bubbles evolve).",
        correct,
    )


def arch_22_hydrochloric_acid_plus_sodium_hydroxide_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    salt_common = rng.choice(["table salt", "common culinary salt", "halite salt"])
    prompt = (
        f"When equal molar amounts of **hydrochloric acid ($\\text{{HCl}}$)** and **sodium hydroxide ($\\text{{NaOH}}$)** react in a beaker, a neutral solution of {salt_common} ($\\text{{pH}} = 7$) forms.\n\n"
        "1. Write the **word equation** [1].\n"
        "2. Write the **balanced chemical equation** [2].\n"
        "3. Explain why the two toxic, corrosive chemicals produce an edible neutral salt [1]."
    )
    correct = "Hydrochloric acid + Sodium hydroxide -> Sodium chloride + Water; HCl + NaOH -> NaCl + H2O; New compounds with completely different chemical properties are formed during chemical exchange"
    sol = (
        "**Step 1:** Word equation: **Hydrochloric acid + Sodium hydroxide $\\rightarrow$ Sodium chloride + Water** [1].\n\n"
        "**Step 2:** Balanced formula equation (already 1 : 1 : 1 : 1): **$$\\text{HCl} + \\text{NaOH} \\rightarrow \\text{NaCl} + \\text{H}_2\\text{O}$$** [2].\n\n"
        "**Step 3:** In a chemical reaction, atoms rearrange into new compounds ($\\text{NaCl}$ and $\\text{H}_2\\text{O}$) whose properties differ entirely from the corrosive reactants [1]."
    )
    return _q(
        rng, "22", "22_hydrochloric_acid_plus_sodium_hydroxide_balanced_equation", prompt, correct, sol, 4, "structured",
        ["reactant_toxicity_persists_in_salt_myth"],
        "Check atomic counts: H (1+1=2), Cl (1), Na (1), O (1) -> already balanced 1:1!",
        "HCl + NaOH -> NaCl + H2O forms safe table salt + water.",
        correct,
    )


def arch_23_crystallisation_of_table_salt_via_evaporation(rng: random.Random) -> Dict[str, Any]:
    salt_name, formula = rng.choice([
        ("sodium chloride", "NaCl"),
        ("potassium chloride", "KCl"),
    ])
    spec = _svg_evaporation_setup(rng, salt_name, formula)
    prompt = (
        f"After neutrally reacting dilute hydrochloric acid with an exact volume of alkali until pH = 7 (tested via indicator), a learner heats the clear aqueous **{salt_name}** solution gently in the apparatus shown.\n\n"
        "1. Name the laboratory separation process shown [1].\n"
        f"2. Describe what remains behind in the porcelain dish once heating finishes, and explain why universal indicator should NOT be left in the batch you want pure crystals from [2]."
    )
    correct = f"Evaporation / crystallisation; Pure white solid {salt_name} ({formula}) crystals remain because water boils off as vapour; indicator dye would stain/contaminate the recovered crystals"
    sol = (
        "**Step 1:** The technique is **evaporation** (followed by **crystallisation**) [1].\n\n"
        f"**Step 2:** Water vaporises into steam, leaving behind dry white **{salt_name} ($\\text{{{formula}}}$) crystals**. You perform the heating on a fresh neutralised batch without indicator so dye does not contaminate the pure white crystals [2]."
    )
    return _q(
        rng, "23", "23_crystallisation_of_table_salt_via_evaporation", prompt, correct, sol, 3, "structured",
        ["salt_evaporates_with_water_myth"],
        "Compare the boiling point of water (100 °C) with the very high melting/boiling point of ionic salt.",
        "Only water escapes as steam; solid salt crystals crystallise in the dish.",
        correct, diagram_spec=spec,
    )


def arch_24_acid_plus_potassium_hydroxide_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    acid_choice = rng.choice([
        ("hydrochloric acid", "HCl", "potassium chloride", "KCl", "HCl + KOH -> KCl + H2O"),
        ("nitric acid", "HNO3", "potassium nitrate", "KNO3", "HNO3 + KOH -> KNO3 + H2O"),
    ])
    a_name, a_f, s_name, s_f, eq = acid_choice
    prompt = (
        f"Aqueous **potassium hydroxide ($\\text{{KOH}}$)** is completely neutralised by **{a_name} ($\\text{{{a_f}}}$)**.\n\n"
        "Which balanced equation correctly represents this neutralisation reaction?"
    )
    correct = eq
    distractors = [
        f"{a_f} + KOH -> {s_f} + H2",
        f"2{a_f} + KOH -> {s_f} + CO2 + H2O",
        f"{a_f} + KOH -> {s_f}2 + 2H2O",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Potassium forms a $+1$ ion ($K^+$), combining 1:1 with the acid anion to produce **{s_name} ($\\text{{{s_f}}}$)** and water ($\\text{{H}}_2\\text{{O}}$).\n"
        f"**Step 2:** Every atom balances at 1:1 -> **$${eq}$$** [2]."
    )
    return _q(
        rng, "24", "24_acid_plus_potassium_hydroxide_balanced_equation", prompt, correct, sol, 2, "multiple_choice",
        ["hydroxide_neutralisation_makes_h2_error"],
        "Acid + metal hydroxide ALWAYS makes salt + water (never H2 or CO2 gas).",
        f"Check charge of potassium (Group 1, +1) -> {s_f} + H2O.",
        correct, options=options,
    )


def arch_25_acid_plus_magnesium_hydroxide_stoichiometric_balancing(rng: random.Random) -> Dict[str, Any]:
    base_name, base_f, salt_name, salt_f, eq = rng.choice([
        ("magnesium hydroxide", "Mg(OH)2", "magnesium chloride", "MgCl2", "2HCl + Mg(OH)2 -> MgCl2 + 2H2O"),
        ("calcium hydroxide", "Ca(OH)2", "calcium chloride", "CaCl2", "2HCl + Ca(OH)2 -> CaCl2 + 2H2O"),
    ])
    prompt = (
        f"**{base_name.capitalize()} ($\\text{{{base_f}}}$)** neutralises hydrochloric acid ($\\text{{HCl}}$).\n\n"
        f"Write the **balanced chemical equation** for this reaction, carefully counting the oxygen and hydrogen atoms inside the bracketed $(OH)_2$ group [3]."
    )
    correct = eq
    sol = (
        f"**Step 1:** Unbalanced skeleton: $\\text{{HCl}} + \\text{{{base_f}}} \\rightarrow \\text{{{salt_f}}} + \\text{{H}}_2\\text{{O}}$ [1].\n\n"
        f"**Step 2:** Notice $\\text{{{salt_f}}}$ needs **2 Cl** atoms, so place coefficient **2** before $\\text{{HCl}}$ [1].\n\n"
        "**Step 3:** Now the left side has $2 + 2 = 4$ H atoms and $2$ O atoms (from $(OH)_2$), which forms **2 $\\text{H}_2\\text{O}$** molecules:\n"
        f"**$${eq}$$** [1]."
    )
    return _q(
        rng, "25", "25_acid_plus_magnesium_hydroxide_stoichiometric_balancing", prompt, correct, sol, 3, "short_answer",
        ["forgetting_2h2o_with_group2_hydroxide_error"],
        "Remember the subscript 2 outside (OH)2 doubles BOTH oxygen and hydrogen.",
        "2 H from 2HCl + 2 OH from Mg(OH)2 = 2 H2O molecules.",
        correct,
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_neutralisation_definition_and_ph_shift": arch_01_neutralisation_definition_and_ph_shift,
    "02_acidic_basic_neutral_ph_boundaries": arch_02_acidic_basic_neutral_ph_boundaries,
    "03_exchange_reaction_ion_swap_concept": arch_03_exchange_reaction_ion_swap_concept,
    "04_universal_indicator_colour_transition_sequence": arch_04_universal_indicator_colour_transition_sequence,
    "05_indicator_drop_transfer_laboratory_technique": arch_05_indicator_drop_transfer_laboratory_technique,
    "06_vinegar_baking_soda_investigative_question_hypothesis": arch_06_vinegar_baking_soda_investigative_question_hypothesis,
    "07_vinegar_baking_soda_effervescence_and_ph_graph": arch_07_vinegar_baking_soda_effervescence_and_ph_graph,
    "08_baking_soda_sodium_bicarbonate_basic_character": arch_08_baking_soda_sodium_bicarbonate_basic_character,
    "09_stoichiometric_excess_acid_vs_excess_base_final_ph": arch_09_stoichiometric_excess_acid_vs_excess_base_final_ph,
    "10_strength_potency_vs_volume_in_neutralisation": arch_10_strength_potency_vs_volume_in_neutralisation,
    "11_non_metal_oxides_form_acidic_solutions": arch_11_non_metal_oxides_form_acidic_solutions,
    "12_carbon_dioxide_straw_exhalation_limewater_and_universal_indicator": arch_12_carbon_dioxide_straw_exhalation_limewater_and_universal_indicator,
    "13_carbonic_acid_formation_and_fizzy_drinks": arch_13_carbonic_acid_formation_and_fizzy_drinks,
    "14_industrial_emissions_and_acid_rain_formation": arch_14_industrial_emissions_and_acid_rain_formation,
    "15_acid_rain_environmental_and_limestone_building_damage": arch_15_acid_rain_environmental_and_limestone_building_damage,
    "16_metal_oxides_basic_character_magnesium_oxide_in_water": arch_16_metal_oxides_basic_character_magnesium_oxide_in_water,
    "17_acid_plus_metal_oxide_general_word_equation": arch_17_acid_plus_metal_oxide_general_word_equation,
    "18_hydrochloric_acid_plus_magnesium_oxide_equation": arch_18_hydrochloric_acid_plus_magnesium_oxide_equation,
    "19_hydrochloric_acid_plus_calcium_and_copper_oxide_equations": arch_19_hydrochloric_acid_plus_calcium_and_copper_oxide_equations,
    "20_alkali_soluble_metal_hydroxide_definition_and_examples": arch_20_alkali_soluble_metal_hydroxide_definition_and_examples,
    "21_acid_plus_metal_hydroxide_general_word_equation": arch_21_acid_plus_metal_hydroxide_general_word_equation,
    "22_hydrochloric_acid_plus_sodium_hydroxide_balanced_equation": arch_22_hydrochloric_acid_plus_sodium_hydroxide_balanced_equation,
    "23_crystallisation_of_table_salt_via_evaporation": arch_23_crystallisation_of_table_salt_via_evaporation,
    "24_acid_plus_potassium_hydroxide_balanced_equation": arch_24_acid_plus_potassium_hydroxide_balanced_equation,
    "25_acid_plus_magnesium_hydroxide_stoichiometric_balancing": arch_25_acid_plus_magnesium_hydroxide_stoichiometric_balancing,
}
