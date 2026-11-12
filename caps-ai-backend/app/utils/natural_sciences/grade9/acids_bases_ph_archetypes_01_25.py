"""Grade 9 Natural Sciences - Acids, Bases and the pH Value: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/04. Acids bases and the pH value.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


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
    guide = f"Marking Guide ({marks} marks): Award marks per verified concept, indicator rule, and scientific reasoning."
    item: Dict[str, Any] = {
        "id": f"ns9_ph_{code}_{rng.randint(100000, 999999)}",
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


def arch_01_ph_scale_range_and_meaning_power_of_hydrogen(rng: random.Random) -> Dict[str, Any]:
    focus = rng.choice(["0 (or 1) to 14", "1 to 14 standard laboratory range"])
    prompt = (
        f"In 1909, Danish chemist Søren Sørensen introduced the **pH scale** (operating across **{focus}**).\n\n"
        "1. What does the letter **'H'** in pH stand for chemically? [1]\n"
        "2. Explain concisely what the pH scale quantifies in any aqueous solution [2]."
    )
    correct = "Hydrogen (specifically hydrogen ions / power of hydrogen); Quantifies how acidic or basic (alkaline) an aqueous solution is based on hydrogen ion concentration."
    sol = (
        "**Step 1:** **'H'** represents **hydrogen** (reflecting hydrogen ion concentration, $H^+$ — \"power of hydrogen\") [1].\n\n"
        "**Step 2:** The pH scale numerically quantifies the relative **acidity or basicity (alkalinity)** of an aqueous liquid across values 0/1 to 14 [2]."
    )
    return _q(
        rng, "01", "01_ph_scale_range_and_meaning_power_of_hydrogen", prompt, correct, sol, 3, "structured",
        ["ph_acronym_meaning_error"],
        "Remember pH literally stands for 'power of hydrogen'.",
        "H = hydrogen element/ions; measures relative acidity vs basicity.",
        correct,
    )


def arch_02_ph_zones_acidic_neutral_basic_boundaries(rng: random.Random) -> Dict[str, Any]:
    ph_val, cls_name, ions = rng.choice([
        ("2,4", "Acidic", "pH < 7 (excess hydrogen ions)"),
        ("7,0", "Neutral", "pH = 7 (balanced H+ and OH-)"),
        ("11,2", "Basic (alkaline)", "pH > 7 (excess hydroxide ions)"),
        ("5,5", "Weakly acidic", "pH < 7 (mildly below 7)"),
        ("8,6", "Weakly basic (alkaline)", "pH > 7 (just above 7)"),
    ])
    prompt = (
        f"An unlabelled aqueous sample tests cleanly at **pH {ph_val}** at 25 °C.\n\n"
        f"Classify this sample as **acidic**, **neutral**, or **basic (alkaline)** and justify using the standard pH boundaries [2]."
    )
    correct = f"{cls_name}; Justification: {ions}."
    sol = (
        "**Step 1:** Reference boundaries at 25 °C: Acids have **$\\text{pH} < 7$**, exact neutral is **$\\text{pH} = 7$**, and bases have **$\\text{pH} > 7$** [1].\n\n"
        f"**Step 2:** Because pH = {ph_val}, the solution is **{cls_name}** ({ions}) [1]."
    )
    return _q(
        rng, "02", "02_ph_zones_acidic_neutral_basic_boundaries", prompt, correct, sol, 2, "short_answer",
        ["ph_boundary_classification_error"],
        "Compare the given pH directly against 7,0.",
        f"{ph_val} -> {cls_name} ({ions}).",
        correct,
    )


def arch_03_acid_strength_trend_toward_ph_zero_or_one(rng: random.Random) -> Dict[str, Any]:
    a1, a2 = rng.choice([("pH 1,5", "pH 5,5"), ("pH 2,0", "pH 6,0"), ("pH 1,0", "pH 4,5")])
    prompt = (
        f"Two clear colourless acid solutions measure **{a1}** (Acid P) and **{a2}** (Acid Q).\n\n"
        "Which acid is **stronger / more strongly acidic**, and what general rule links pH number to acid strength?"
    )
    correct = f"Acid P ({a1}) is more strongly acidic; Lower pH values closer to 0–1 indicate higher acidity and stronger acid character."
    options = [
        correct,
        f"Acid Q ({a2}) is stronger because larger pH numbers always mean stronger acidity.",
        "Both acids have identical strength since both sit below pH 7.",
        f"Acid Q ({a2}) is neutral while Acid P ({a1}) is weakly basic.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** On the acid side (pH < 7), acidity strengthens **as pH drops toward 0–1**.\n"
        f"**Step 2:** Therefore Acid P (**{a1}**) is much more strongly acidic than Acid Q ({a2}) [2]."
    )
    return _q(
        rng, "03", "03_acid_strength_trend_toward_ph_zero_or_one", prompt, correct, sol, 2, "multiple_choice",
        ["lower_ph_means_weaker_acid_myth"],
        "Careful: smaller numbers mean MORE acidic!",
        f"{a1} < {a2}, so Acid P is stronger.",
        correct, options=options,
    )


def arch_04_base_strength_trend_toward_ph_fourteen(rng: random.Random) -> Dict[str, Any]:
    b1, b2 = rng.choice([("baking soda (pH 8,4)", "drain unblocker NaOH (pH 13,6)"), ("toothpaste (pH 8,0)", "oven cleaner (pH 13,2)")])
    prompt = (
        f"Compare two alkaline cleaners: **{b1}** vs **{b2}**.\n\n"
        "1. State which cleaner is **more strongly basic (caustic)** [1].\n"
        "2. State the direction pH moves as base strength increases [1]."
    )
    correct = f"{b2} is more strongly basic; Basicity increases as pH rises above 7 toward 14."
    sol = (
        f"**Step 1:** **{b2}** has a much higher pH closer to 14 and is far more caustic/basic [1].\n\n"
        "**Step 2:** For bases (pH > 7), alkaline strength **increases as pH moves higher toward 14** [1]."
    )
    return _q(
        rng, "04", "04_base_strength_trend_toward_ph_fourteen", prompt, correct, sol, 2, "short_answer",
        ["base_strength_ph_direction_error"],
        "For bases above 7, higher pH means stronger alkalinity.",
        f"{b2} sits closer to 14, so it is stronger.",
        correct,
    )


def arch_05_logarithmic_tenfold_acidity_jump_per_ph_unit(rng: random.Random) -> Dict[str, Any]:
    ph_low = rng.choice([1, 2, 3])
    steps = rng.choice([2, 3])
    ph_high = ph_low + steps
    factor = 10 ** steps
    prompt = (
        f"The pH scale is **logarithmic** (base 10): each step of **1 pH unit** changes hydrogen-ion acidity by a factor of **10**.\n\n"
        f"How many times more acidic ($H^+$ concentration) is a citrus solution at **pH {ph_low}** compared with one at **pH {ph_high}**?"
    )
    correct = f"{factor} times more acidic (10^{steps} = {factor})."
    options = [
        correct,
        f"{steps} times more acidic.",
        f"{steps * 10} times more acidic.",
        f"{factor // 10} times more acidic.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** pH drops by ${ph_high} - {ph_low} = {steps}$ whole pH units.\n"
        f"**Step 2:** Each unit multiplies acidity by 10 -> $10^{{{steps}}} = {factor}$ times more acidic [2]."
    )
    return _q(
        rng, "05", "05_logarithmic_tenfold_acidity_jump_per_ph_unit", prompt, correct, sol, 2, "multiple_choice",
        ["linear_ph_difference_myth"],
        "Multiply by 10 for every 1 pH step—do NOT simply multiply by 10 once.",
        f"{steps} pH steps -> 10^{steps} = {factor}x.",
        correct, options=options,
    )


def arch_06_neutral_solution_ion_balance_h_equals_oh(rng: random.Random) -> Dict[str, Any]:
    liq = rng.choice(["pure distilled water", "clean aqueous sodium chloride (NaCl) salt solution", "sucrose sugar dissolved in pure water"])
    prompt = (
        f"A calibrated probe measures **{liq}** at **pH 7,0**.\n\n"
        "1. State the pH classification of this liquid [1].\n"
        "2. Explain chemically in terms of hydrogen ($H^+$) and hydroxide ($OH^-$) ions why it is neither acidic nor basic [2]."
    )
    correct = "Neutral; Contains exactly balanced concentrations of hydrogen ions (H+) and hydroxide ions (OH-) so neither acidic nor basic properties dominate."
    sol = (
        "**Step 1:** A reading of pH 7,0 is classified as **neutral** [1].\n\n"
        "**Step 2:** Pure water and neutral salt solutions contain **equal concentrations of $H^+$ and $OH^-$ ions**, creating complete acid-base balance [2]."
    )
    return _q(
        rng, "06", "06_neutral_solution_ion_balance_h_equals_oh", prompt, correct, sol, 3, "structured",
        ["neutral_has_zero_ions_myth"],
        "Does neutral water have zero ions, or an equal balance of H+ and OH-?",
        "Neutral (pH 7) -> equal H+ and OH- balance.",
        correct,
    )


def arch_07_what_is_an_acid_base_indicator_definition(rng: random.Random) -> Dict[str, Any]:
    ctx = rng.choice(["clear laboratory glassware", "a Grade 9 water quality test kit"])
    prompt = (
        f"Because colourless acids and bases often look identical in **{ctx}**, chemists rely on **acid-base indicators**.\n\n"
        "Define what an **acid-base indicator** is and state the physical cue learners observe when using one [2]."
    )
    correct = "A chemical dye substance whose molecules change colour distinctly and reversibly depending on whether it is in an acidic, neutral, or basic (alkaline) environment."
    sol = (
        "**Step 1:** An **acid-base indicator** is a sensitive dye compound that exhibits **distinct colour changes** when exposed to acids versus bases [1].\n\n"
        "**Step 2:** Chemists inspect the reversible **colour shift** safely instead of tasting or touching hazardous liquids [1]."
    )
    return _q(
        rng, "07", "07_what_is_an_acid_base_indicator_definition", prompt, correct, sol, 2, "short_answer",
        ["indicator_neutralises_acid_myth"],
        "Think about the root word 'indicate': what observable property changes?",
        "Reversible colour-changing dye reacting to pH / H+ vs OH- levels.",
        correct,
    )


def arch_08_universal_indicator_full_rainbow_spectrum_ph(rng: random.Random) -> Dict[str, Any]:
    target = rng.choice([
        ("Dark Red (pH 1)", "Strong acid (e.g. battery / stomach acid)", 0, "#dc2626"),
        ("Bright Orange (pH 3)", "Moderate acid (e.g. vinegar / citrus juice)", 1, "#f97316"),
        ("Canary Yellow (pH 5)", "Weak acid (e.g. black coffee / rainwater)", 2, "#eab308"),
        ("Pure Green (pH 7)", "Neutral solution (e.g. pure water)", 3, "#16a34a"),
        ("Turquoise Blue (pH 9)", "Weak base (e.g. baking soda / soap)", 4, "#0284c7"),
        ("Deep Violet/Purple (pH 13)", "Strong base / alkali (e.g. drain cleaner NaOH)", 6, "#7e22ce"),
    ])
    sample_name = rng.choice(["Sample W", "Sample X", "Sample Y", "Sample Z"])
    sample_desc, verdict, idx_hi, hi_col = target
    sample_lbl = f"{sample_name}: {sample_desc}"
    swatch = [
        ("1", "#dc2626"), ("3", "#f97316"), ("5", "#eab308"), ("7", "#16a34a"),
        ("9", "#0284c7"), ("11", "#2563eb"), ("13", "#7e22ce"),
    ]
    rects = "".join(
        f'<rect x="{30 + i*46}" y="42" width="42" height="46" rx="4" fill="{col}" '
        f'stroke="{"#0f172a" if i == idx_hi else "none"}" stroke-width="{"3" if i == idx_hi else "0"}"/>'
        f'<text x="{51 + i*46}" y="104" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">pH {ph}</text>'
        for i, (ph, col) in enumerate(swatch)
    )
    svg = (
        f'<svg viewBox="0 0 380 144" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="380" height="144" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="190" y="20" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Universal Indicator Chart ({sample_name} Match)</text>'
        f'{rects}'
        f'<circle cx="{51 + idx_hi*46}" cy="33" r="4" fill="{hi_col}" stroke="#0f172a"/>'
        f'<text x="72" y="126" font-size="8" font-weight="bold" fill="#dc2626" text-anchor="middle">Acidic (&lt;7)</text>'
        f'<text x="189" y="126" font-size="8" font-weight="bold" fill="#16a34a" text-anchor="middle">Neutral (=7)</text>'
        f'<text x="306" y="126" font-size="8" font-weight="bold" fill="#7e22ce" text-anchor="middle">Basic (&gt;7)</text>'
        f'</svg>'
    )
    prompt = (
        "Examine the Universal Indicator reference colour chart (with the tested band outlined).\n\n"
        f"A learner adds three drops of Universal Indicator to a mystery liquid and records: **{sample_lbl}**.\n"
        "Classify its exact chemical strength and give a plausible household/laboratory example [2]."
    )
    correct = verdict
    sol = (
        "**Step 1:** Locate the colour band on the Universal Indicator spectrum (red/orange/yellow < 7 -> green 7 -> blue/purple > 7) [1].\n\n"
        f"**Step 2:** {sample_lbl} matches **{verdict}** [1]."
    )
    return _q(
        rng, "08", "08_universal_indicator_full_rainbow_spectrum_ph", prompt, correct, sol, 2, "short_answer",
        ["universal_indicator_is_always_green_myth", "blue_means_cold_not_base_myth"],
        "Remember ROY-G-BIV: Red/Orange/Yellow = Acid, Green = Neutral, Blue/Violet = Base.",
        f"{sample_lbl} -> {verdict}.",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_09_universal_indicator_advantage_over_litmus(rng: random.Random) -> Dict[str, Any]:
    pair_str = rng.choice(["lemon juice (pH 2,2) vs rainwater (pH 5,6)", "handwash (pH 9) vs drain cleaner (pH 13,8)"])
    prompt = (
        f"A learner wants to compare **{pair_str}** to find out which sample is stronger.\n\n"
        "Explain why **Universal Indicator** succeeds at this task whereas standard **litmus paper** fails to distinguish them [2]."
    )
    correct = "Litmus only shows a binary acid-vs-base shift (all acids look red; all bases look blue), whereas Universal Indicator displays a graduated rainbow spectrum indicating approximate pH strength (e.g. red vs yellow, or blue vs deep purple)."
    sol = (
        "**Step 1:** Simple **litmus** has only two colours—turning identically red in both pH 2 and pH 5,6 (or identically blue in both pH 9 and pH 13,8) [1].\n\n"
        "**Step 2:** **Universal Indicator** is a blended multi-dye mixture giving distinct rainbow shades across pH 1–14, allowing strength estimation [1]."
    )
    return _q(
        rng, "09", "09_universal_indicator_advantage_over_litmus", prompt, correct, sol, 2, "short_answer",
        ["litmus_can_measure_strength_myth"],
        "Can blue litmus paper tell pH 2 from pH 5? Compare with Universal Indicator.",
        "Litmus = binary only; Universal Indicator = graduated pH strength.",
        correct,
    )


def arch_10_red_and_blue_litmus_two_paper_testing_protocol(rng: random.Random) -> Dict[str, Any]:
    sol_type, red_obs, blue_obs = rng.choice([
        ("Dilute nitric acid (pH 1,5)", "Remains red", "Turns red"),
        ("Aqueous ammonia base (pH 11,5)", "Turns blue", "Remains blue"),
        ("Distilled water (pH 7,0)", "Remains red", "Remains blue"),
    ])
    prompt = (
        f"An unlabelled beaker contains **{sol_type}**. A student dips fresh **red litmus paper** AND fresh **blue litmus paper** into separate drops of it.\n\n"
        "State the exact final colour of:\n"
        "1. Red litmus paper [1]\n"
        "2. Blue litmus paper [1]"
    )
    correct = f"Red litmus: {red_obs}; Blue litmus: {blue_obs}"
    sol = (
        f"**Step 1:** For **{sol_type}**, Red litmus **{red_obs.lower()}** [1].\n\n"
        f"**Step 2:** Blue litmus **{blue_obs.lower()}** [1]."
    )
    return _q(
        rng, "10", "10_red_and_blue_litmus_two_paper_testing_protocol", prompt, correct, sol, 2, "short_answer",
        ["acids_turn_red_litmus_blue_confusion"],
        "Rule: Acids turn BOTH litmus strips red; Bases turn BOTH blue; Neutral changes NEITHER.",
        f"Red -> {red_obs}; Blue -> {blue_obs}.",
        correct,
    )


def arch_11_neutral_solution_dual_litmus_invariance(rng: random.Random) -> Dict[str, Any]:
    sample = rng.choice(["clear liquid X", "unknown bottle Y"])
    prompt = (
        f"A student dips ONLY **red litmus paper** into **{sample}**. The red strip stays red, so the student concludes: *\"{sample} must be an acid!\"*\n\n"
        "Explain the logical flaw in this conclusion and state how to test **{sample}** properly with litmus [2]."
    )
    correct = "Both acids AND neutral solutions leave red litmus paper red! One must also dip blue litmus paper: if blue stays blue it is neutral (pH 7); only if blue turns red is it acidic."
    sol = (
        "**Step 1:** Red litmus remaining red is ambiguous—both **acids** and **neutral solutions (like pure water)** leave red litmus unchanged [1].\n\n"
        "**Step 2:** Always test with **both red and blue strips** (blue turning red confirms acid; neither changing confirms neutral) [1]."
    )
    return _q(
        rng, "11", "11_neutral_solution_dual_litmus_invariance", prompt, correct, sol, 2, "short_answer",
        ["single_litmus_strip_fallacy"],
        "What happens to red litmus paper in pure water (pH 7)?",
        "Neutral ALSO keeps red litmus red; test blue litmus as well to eliminate neutral.",
        correct,
    )


def arch_12_bromothymol_blue_colour_transitions(rng: random.Random) -> Dict[str, Any]:
    medium, col = rng.choice([
        ("lemon juice (acidic, pH 2,3)", "Yellow"),
        ("pure distilled water (neutral, pH 7,0)", "Green"),
        ("sodium hydroxide (basic, pH 13,0)", "Blue"),
    ])
    prompt = (
        "Chemists frequently use liquid **bromothymol blue** indicator during titration investigations.\n\n"
        f"What exact colour does bromothymol blue display in **{medium}**?"
    )
    correct = col
    options = ["Yellow", "Green", "Blue", "Bright pink / magenta"]
    sol = (
        "**Step 1:** Bromothymol blue colour map: Acidic (< pH 6) = **Yellow**; Neutral (~ pH 7) = **Green**; Basic (> pH 7,6) = **Blue**.\n"
        f"**Step 2:** Therefore in {medium} it appears **{col}** [2]."
    )
    return _q(
        rng, "12", "12_bromothymol_blue_colour_transitions", prompt, correct, sol, 2, "multiple_choice",
        ["bromothymol_blue_acid_base_swap"],
        "Bromothymol blue: Yellow in acid, Green neutral, Blue in base.",
        f"{medium} -> {col}.",
        correct, options=options,
    )


def arch_13_phenolphthalein_colour_transitions_titration(rng: random.Random) -> Dict[str, Any]:
    medium, col = rng.choice([
        ("sodium hydroxide alkali (pH 13)", "Bright pink / magenta"),
        ("hydrochloric acid (pH 1,5)", "Colourless (clear)"),
        ("distilled water (pH 7,0)", "Colourless (clear)"),
    ])
    prompt = (
        "Drops of liquid **phenolphthalein** indicator are added to a flask of **{medium}**.\n\n"
        f"State the colour observed in **{medium}** and recall the full acid / neutral / base pattern of phenolphthalein [2]."
    )
    correct = f"{col}; Phenolphthalein is colourless in acid and neutral solutions, turning bright pink/magenta only in bases (pH > 8,2)."
    sol = (
        "**Step 1:** Phenolphthalein stays **colourless** across both acidic (< 7) and neutral (7) conditions, shifting sharply to **bright pink/magenta** in basic solutions (> 8,2) [1].\n\n"
        f"**Step 2:** In {medium}, it appears **{col}** [1]."
    )
    return _q(
        rng, "13", "13_phenolphthalein_colour_transitions_titration", prompt, correct, sol, 2, "short_answer",
        ["phenolphthalein_turns_blue_myth"],
        "Phenolphthalein acts like an alkaline switch: clear below ~8,2 and bright pink in bases.",
        f"{medium} -> {col}.",
        correct,
    )


def arch_14_phenolphthalein_acid_vs_neutral_limitation(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([("vinegar and distilled water", "acidic vinegar vs neutral water"), ("dilute HCl and NaCl brine", "acidic HCl vs neutral brine")])
    sub_pair, desc = pair
    prompt = (
        f"Two unlabelled beakers hold **{sub_pair}**. Adding phenolphthalein leaves BOTH beakers completely **colourless**.\n\n"
        f"Why cannot phenolphthalein alone tell **{desc}** apart, and which simple indicator would immediately separate them? [2]"
    )
    correct = "Phenolphthalein stays colourless in ALL solutions with pH <= 8,2 (both acidic and neutral); Blue litmus paper, bromothymol blue, or Universal Indicator immediately turns red/yellow in acid while staying blue/green in neutral."
    sol = (
        "**Step 1:** Because phenolphthalein's colour change begins only above **pH 8,2**, both acidic and neutral liquids remain identically colourless [1].\n\n"
        "**Step 2:** Switching to **Universal Indicator**, **bromothymol blue** (yellow vs green), or **blue litmus paper** (turns red vs stays blue) separates acid from neutral instantly [1]."
    )
    return _q(
        rng, "14", "14_phenolphthalein_acid_vs_neutral_limitation", prompt, correct, sol, 2, "short_answer",
        ["phenolphthalein_detects_acid_myth"],
        "Check phenolphthalein's colour at pH 3 AND at pH 7.",
        "Colourless in both; use blue litmus / bromothymol blue / Universal Indicator instead.",
        correct,
    )


def arch_15_red_cabbage_natural_anthocyanin_indicator_preparation(rng: random.Random) -> Dict[str, Any]:
    step_focus = rng.choice(["boiling water extraction and filtration", "straining out solid purple leaves"])
    prompt = (
        f"Learners prepare a homemade natural acid-base indicator from shredded fresh **red cabbage** leaves using **{step_focus}**.\n\n"
        "Outline the **three practical laboratory steps** to prepare clean purple cabbage indicator liquid ready for pH testing [3]."
    )
    correct = "1. Chop/shred red cabbage leaves finely and soak or simmer gently in hot/boiling water until the pigment turns the water deep purple. 2. Allow the beaker to cool safely. 3. Filter or strain out solid leaf pieces to collect pure purple pigment juice."
    sol = (
        "**Step 1:** Chop red cabbage finely to break cell walls and heat/simmer gently in water for ~10 minutes so water-soluble **anthocyanin pigment** dissolves into a deep purple extract [1].\n\n"
        "**Step 2:** Let the mixture cool safely [1].\n\n"
        "**Step 3:** **Filter or strain** through a sieve/filter paper to obtain clear purple indicator extract free of pulp [1]."
    )
    return _q(
        rng, "15", "15_red_cabbage_natural_anthocyanin_indicator_preparation", prompt, correct, sol, 3, "structured",
        ["natural_indicator_extraction_steps"],
        "Think like extracting tea: chop -> steep/boil pigment into water -> cool -> strain/filter.",
        "Chop + simmer/soak in hot water -> cool -> filter purple solution.",
        correct,
    )


def arch_16_red_cabbage_colour_spectrum_red_violet_blue_green_yellow(rng: random.Random) -> Dict[str, Any]:
    test_case = rng.choice([
        ("Lemon juice / HCl (strong acid)", "Bright pinkish-red"),
        ("Distilled water (neutral pH 7)", "Purple / violet"),
        ("Baking soda solution (weak base)", "Blue / teal-turquoise"),
        ("Drain cleaner / NaOH (strong base)", "Green turning yellow"),
    ])
    subs, expected = test_case
    prompt = (
        "Purple **red cabbage indicator** displays a striking rainbow across acids, neutrals, and bases (red in acid -> purple neutral -> blue weak base -> green/yellow strong base).\n\n"
        f"Predict the colour obtained when purple red cabbage juice is mixed into **{subs}** [2]."
    )
    correct = expected
    options = ["Bright pinkish-red", "Purple / violet", "Blue / teal-turquoise", "Green turning yellow"]
    sol = (
        "**Step 1:** Anthocyanin colour order across pH: Strong Acid = **Bright pinkish-red**; Neutral = **Purple/violet**; Weak Base = **Blue/teal**; Strong Base = **Green/yellow**.\n"
        f"**Step 2:** Therefore **{subs}** produces **{expected}** [2]."
    )
    return _q(
        rng, "16", "16_red_cabbage_colour_spectrum_red_violet_blue_green_yellow", prompt, correct, sol, 2, "multiple_choice",
        ["red_cabbage_green_in_acid_myth"],
        "Remember red cabbage goes PINK-RED in acid and GREEN/YELLOW in strong base!",
        f"{subs} -> {expected}.",
        correct, options=options,
    )


def arch_17_other_plant_natural_indicators_turmeric_beetroot_hibiscus(rng: random.Random) -> Dict[str, Any]:
    plant, acid_c, base_c = rng.choice([
        ("Turmeric spice water", "Remains bright yellow", "Turns brick-red / reddish-brown"),
        ("Black rooibos/Ceylon tea", "Lightens pale amber-yellow (with lemon)", "Darkens deep brown"),
    ])
    prompt = (
        f"Besides red cabbage, kitchen plant extracts such as **{plant}** act as natural acid-base indicators.\n\n"
        f"State the colour shift seen when **{plant}** encounters acid versus an alkaline base [2]."
    )
    correct = f"In acid: {acid_c}; In base: {base_c}."
    sol = (
        f"**Step 1 & 2:** Natural pigments in **{plant}** shift reversibly: **{acid_c}** in acid versus **{base_c}** in basic solution [2]."
    )
    return _q(
        rng, "17", "17_other_plant_natural_indicators_turmeric_beetroot_hibiscus", prompt, correct, sol, 2, "short_answer",
        ["natural_indicator_colour_pairs"],
        "Think about turmeric curry stains turning reddish-brown when washed with alkaline bar soap!",
        f"Acid: {acid_c}; Base: {base_c}.",
        correct,
    )


def arch_18_digital_ph_meter_electrode_calibration_and_precision(rng: random.Random) -> Dict[str, Any]:
    reading = rng.choice(["4,38", "8,72", "6,85", "2,14"])
    prompt = (
        f"A field scientist dips a calibrated **electronic digital pH meter** probe into a water sample and records **pH {reading}**.\n\n"
        "State **two major scientific advantages** of using a digital pH meter over Universal Indicator paper strips [2]."
    )
    correct = "1. Delivers high numerical precision (e.g. two decimal places like 4,38 instead of subjective colour judgment); 2. Works reliably in dark, murky, or coloured liquids without optical colour interference."
    sol = (
        f"**Step 1:** An electronic probe gives **objective, high-precision decimal values** (like pH {reading}) without subjective eye-matching error [1].\n\n"
        "**Step 2:** It works accurately in **strongly coloured, cloudy, or dark liquids** (e.g. muddy river water, wine, coffee) where dye paper colours would be masked [1]."
    )
    return _q(
        rng, "18", "18_digital_ph_meter_electrode_calibration_and_precision", prompt, correct, sol, 2, "short_answer",
        ["ph_meter_vs_paper_precision"],
        "Consider decimal accuracy and coloured/muddy solutions.",
        "High decimal precision + works in dark/opaque samples.",
        correct,
    )


def arch_19_limitation_of_colour_indicators_in_dark_opaque_liquids(rng: random.Random) -> Dict[str, Any]:
    liquid = rng.choice(["dark red grape juice", "black filter coffee", "dark soy sauce", "deep purple beetroot soup"])
    prompt = (
        f"A student adds green liquid Universal Indicator into a test tube of **{liquid}** to test its pH, but cannot determine the reading.\n\n"
        "Explain why liquid indicator dyes fail here, and suggest which instrument resolves the issue cleanly [2]."
    )
    correct = f"The intense natural pigment of {liquid} hides and masks the indicator's subtle colour change; Use a calibrated digital pH meter probe instead."
    sol = (
        f"**Step 1:** Optical colour indicators depend on visibly reading dye hues; **{liquid}** masks red/orange/green shades [1].\n\n"
        "**Step 2:** Measuring electronically with a **digital pH meter** overcomes dark-liquid opacity completely [1]."
    )
    return _q(
        rng, "19", "19_limitation_of_colour_indicators_in_dark_opaque_liquids", prompt, correct, sol, 2, "short_answer",
        ["dark_sample_colour_indicator_limitation"],
        "Why can't you see red or orange dye inside a dark black or purple drink?",
        "Dark pigment masks dye colour -> use electronic pH meter.",
        correct,
    )


def arch_20_everyday_household_acids_citrus_vinegar_stomach(rng: random.Random) -> Dict[str, Any]:
    food, acid_chem, ph_r = rng.choice([
        ("Lemons and limes", "Citric acid", "pH ~2,0–2,4"),
        ("Household white spirit vinegar", "Ethanoic (acetic) acid", "pH ~2,8–3,2"),
        ("Human gastric stomach juice", "Hydrochloric acid (HCl)", "pH ~1,5–2,0"),
        ("Fizzy sparkling drinks", "Carbonic acid (H2CO3) / phosphoric acid", "pH ~2,5–3,8"),
    ])
    prompt = (
        f"**{food}** contain a familiar acidic compound.\n\n"
        "1. Name the **specific chemical acid** found inside it [1].\n"
        f"2. State whether its pH sits inside the **strongly acidic**, **weakly acidic**, or **basic** range (e.g. {ph_r}) [1]."
    )
    correct = f"Acid: {acid_chem}; Strongly/moderately acidic ({ph_r}, below 7)."
    sol = (
        f"**Step 1:** **{food}** naturally contain **{acid_chem}** [1].\n\n"
        f"**Step 2:** Its typical reading lies cleanly below 7 (**{ph_r}**) [1]."
    )
    return _q(
        rng, "20", "20_everyday_household_acids_citrus_vinegar_stomach", prompt, correct, sol, 2, "short_answer",
        ["household_acid_names_error"],
        "Match common foods/fluids: citrus -> citric, vinegar -> ethanoic, stomach -> HCl.",
        f"{food} -> {acid_chem} ({ph_r}).",
        correct,
    )


def arch_21_everyday_household_bases_soap_bleach_baking_soda(rng: random.Random) -> Dict[str, Any]:
    item, base_chem, ph_r = rng.choice([
        ("Bicarbonate of soda (baking soda) paste", "Sodium hydrogen carbonate (NaHCO3)", "pH ~8,5 (weak base)"),
        ("Window & kitchen ammonia cleaner (Handy Andy)", "Ammonia solution (NH3(aq))", "pH ~11,5 (stronger base)"),
        ("Caustic drain unblocker crystals", "Sodium hydroxide (NaOH)", "pH ~13,5–14,0 (very strong caustic base)"),
        ("Milk of Magnesia antacid", "Magnesium hydroxide (Mg(OH)2)", "pH ~10,0–10,5 (alkaline base)"),
    ])
    prompt = (
        f"Many household cleaning products and kitchen powders are chemically basic (alkaline): consider **{item}**.\n\n"
        "1. Identify its primary **active basic ingredient** [1].\n"
        f"2. State its approximate pH position ({ph_r}) and predicted litmus response [2]."
    )
    correct = f"Active base: {base_chem}; {ph_r}; Turns red litmus blue (blue litmus stays blue)."
    sol = (
        f"**Step 1:** Primary active base: **{base_chem}** [1].\n\n"
        f"**Step 2:** Measured range: **{ph_r}**, turning **red litmus paper blue** [2]."
    )
    return _q(
        rng, "21", "21_everyday_household_bases_soap_bleach_baking_soda", prompt, correct, sol, 3, "structured",
        ["all_chemicals_in_homes_are_acids_myth"],
        "Cleaning agents like ammonia, soap, baking soda, and drain unblocker sit ABOVE pH 7.",
        f"{item}: {base_chem}, {ph_r}, turns red litmus blue.",
        correct,
    )


def arch_22_physical_sensory_properties_acids_sour_corrosive(rng: random.Random) -> Dict[str, Any]:
    safe_item = rng.choice(["sour amasi / citrus fruit", "dilute vinegar on chips"])
    prompt = (
        f"Known food-grade weak acids like **{safe_item}** demonstrate characteristic everyday acid properties.\n\n"
        "State **two general physical/sensory properties** of aqueous acids AND explain why strong mineral acids (like lab $\\text{H}_2\\text{SO}_4$) are labelled **corrosive** [3]."
    )
    correct = "Taste sour (food acids only), feel rough/squeaky (not soapy), sting cuts, and turn blue litmus red; Strong acids are corrosive because high H+ reactivity eats away/destroys living skin proteins and metals."
    sol = (
        "**Step 1:** Aqueous acids typically **taste sour** (for known culinary acids only!), feel **rough/non-slippery**, and **sting cuts** [2].\n\n"
        "**Step 2:** Concentrated lab acids are **corrosive**—chemically attacking skin cells, clothing fabric, and reactive metals on contact [1]."
    )
    return _q(
        rng, "22", "22_physical_sensory_properties_acids_sour_corrosive", prompt, correct, sol, 3, "structured",
        ["acids_feel_slippery_myth"],
        "Contrast sour taste / rough skin feel with soapy alkaline feel; define corrosive.",
        "Acids taste sour (known foods only), feel rough, and strong ones corrode tissue/metals.",
        correct,
    )


def arch_23_physical_sensory_properties_bases_bitter_soapy_caustic(rng: random.Random) -> Dict[str, Any]:
    base_ex = rng.choice(["soapy washing-powder water", "weak baking-soda paste"])
    prompt = (
        f"Rubbing a tiny drop of **{base_ex}** between gloved or clean fingertips highlights typical alkaline behaviour.\n\n"
        "1. State the typical **tactile feel** and **taste category** associated with bases (never tasting chemicals directly!) [2].\n"
        "2. Explain what the warning hazard word **'caustic'** means for strong alkalis such as NaOH [1]."
    )
    correct = "Feel slippery / soapy (react with skin oils) and are generally bitter; Caustic means capable of severely burning, dissolving, or destroying organic tissue chemically."
    sol = (
        "**Step 1:** Bases feel noticeably **slippery / soapy** between fingers (saponifying skin oils) and possess a **bitter** character [2].\n\n"
        "**Step 2:** **Caustic** (e.g. caustic soda, NaOH) warns that concentrated alkalis severely burn and dissolve human tissue just as dangerously as strong acids [1]."
    )
    return _q(
        rng, "23", "23_physical_sensory_properties_bases_bitter_soapy_caustic", prompt, correct, sol, 3, "structured",
        ["strong_bases_harmless_myth"],
        "Acids = sour & rough; Bases = bitter & slippery/soapy (strong ones = caustic!).",
        "Slippery/soapy feel, bitter; Caustic = burns/destroys living tissue.",
        correct,
    )


def arch_24_ranking_household_substances_ascending_or_descending_ph(rng: random.Random) -> Dict[str, Any]:
    pool = [
        ("Stomach acid", 1.5),
        ("Lemon juice", 2.2),
        ("White vinegar", 3.0),
        ("Black coffee", 5.0),
        ("Distilled water", 7.0),
        ("Baking soda", 8.5),
        ("Ammonia cleaner", 11.5),
        ("Drain cleaner", 13.8),
    ]
    sample5 = rng.sample(pool, 5)
    shuffled = list(sample5)
    rng.shuffle(shuffled)
    asc = rng.choice([True, False])
    direction = "INCREASING pH (lowest pH / most acidic -> highest pH / most basic)" if asc else "DECREASING pH (highest pH / most basic -> lowest pH / most acidic)"
    sorted_items = sorted(sample5, key=lambda x: x[1], reverse=not asc)
    list_str = ", ".join(name for name, _ in shuffled)
    ans_str = " -> ".join(f"{name} (~pH {str(ph).replace('.', ',')})" for name, ph in sorted_items)
    prompt = (
        f"Arrange these five everyday substances in order of **{direction}**:\n"
        f"**{list_str}** [3]."
    )
    sol = (
        "**Step 1:** Match approximate pH zones (strong acid ~1–3 -> weak acid ~5 -> neutral 7 -> weak base ~8,5 -> strong alkali 11–14) [1].\n\n"
        f"**Step 2:** Correct {direction}: **{ans_str}** [2]."
    )
    return _q(
        rng, "24", "24_ranking_household_substances_ascending_or_descending_ph", prompt, ans_str, sol, 3, "short_answer",
        ["household_ph_ordering_error"],
        "Anchor neutral water at 7 first, sort sour items below 7 and cleaners above 7.",
        ans_str,
        ans_str,
    )


def arch_25_swimming_pool_water_ph_testing_phenol_red_balance(rng: random.Random) -> Dict[str, Any]:
    fault = rng.choice([
        ("drops down to pH 6,2", "too acidic", "stings swimmers' eyes/nose, corrodes metal pump impellers/heaters, and breaks down chlorine rapidly", "add basic soda ash (sodium carbonate) to raise pH back to 7,2–7,6"),
        ("climbs up to pH 8,4", "too alkaline (basic)", "renders chlorine disinfectant sluggish/ineffective, turns water cloudy with scale, and dries skin", "carefully add dilute pool acid (hydrochloric/bisulfate) to lower pH back to 7,2–7,6"),
    ])
    meas, cond, problem, fix = fault
    prompt = (
        f"Ideal domestic swimming pool water is maintained tightly around **pH 7,2 to 7,6**. During summer rains, a pool test kit shows water **{meas}**.\n\n"
        f"1. State whether this pool water is **{cond}** relative to the ideal band [1].\n"
        "2. State ONE practical problem this causes for swimmers or pool hardware, and ONE chemical corrective action [2]."
    )
    correct = f"Water is {cond}; Problem: {problem}; Fix: {fix}."
    sol = (
        f"**Step 1:** Relative to ideal pH 7,2–7,6, **pH {meas.split()[-1]}** is **{cond}** [1].\n\n"
        f"**Step 2:** Effect: {problem}. Treatment: **{fix}** [2]."
    )
    return _q(
        rng, "25", "25_swimming_pool_water_ph_testing_phenol_red_balance", prompt, correct, sol, 3, "structured",
        ["pool_ph_remediation_inversion"],
        "Use neutralisation: acidic pool needs mild base (soda ash); alkaline pool needs pool acid.",
        f"{cond}: {fix}.",
        correct,
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_ph_scale_range_and_meaning_power_of_hydrogen": arch_01_ph_scale_range_and_meaning_power_of_hydrogen,
    "02_ph_zones_acidic_neutral_basic_boundaries": arch_02_ph_zones_acidic_neutral_basic_boundaries,
    "03_acid_strength_trend_toward_ph_zero_or_one": arch_03_acid_strength_trend_toward_ph_zero_or_one,
    "04_base_strength_trend_toward_ph_fourteen": arch_04_base_strength_trend_toward_ph_fourteen,
    "05_logarithmic_tenfold_acidity_jump_per_ph_unit": arch_05_logarithmic_tenfold_acidity_jump_per_ph_unit,
    "06_neutral_solution_ion_balance_h_equals_oh": arch_06_neutral_solution_ion_balance_h_equals_oh,
    "07_what_is_an_acid_base_indicator_definition": arch_07_what_is_an_acid_base_indicator_definition,
    "08_universal_indicator_full_rainbow_spectrum_ph": arch_08_universal_indicator_full_rainbow_spectrum_ph,
    "09_universal_indicator_advantage_over_litmus": arch_09_universal_indicator_advantage_over_litmus,
    "10_red_and_blue_litmus_two_paper_testing_protocol": arch_10_red_and_blue_litmus_two_paper_testing_protocol,
    "11_neutral_solution_dual_litmus_invariance": arch_11_neutral_solution_dual_litmus_invariance,
    "12_bromothymol_blue_colour_transitions": arch_12_bromothymol_blue_colour_transitions,
    "13_phenolphthalein_colour_transitions_titration": arch_13_phenolphthalein_colour_transitions_titration,
    "14_phenolphthalein_acid_vs_neutral_limitation": arch_14_phenolphthalein_acid_vs_neutral_limitation,
    "15_red_cabbage_natural_anthocyanin_indicator_preparation": arch_15_red_cabbage_natural_anthocyanin_indicator_preparation,
    "16_red_cabbage_colour_spectrum_red_violet_blue_green_yellow": arch_16_red_cabbage_colour_spectrum_red_violet_blue_green_yellow,
    "17_other_plant_natural_indicators_turmeric_beetroot_hibiscus": arch_17_other_plant_natural_indicators_turmeric_beetroot_hibiscus,
    "18_digital_ph_meter_electrode_calibration_and_precision": arch_18_digital_ph_meter_electrode_calibration_and_precision,
    "19_limitation_of_colour_indicators_in_dark_opaque_liquids": arch_19_limitation_of_colour_indicators_in_dark_opaque_liquids,
    "20_everyday_household_acids_citrus_vinegar_stomach": arch_20_everyday_household_acids_citrus_vinegar_stomach,
    "21_everyday_household_bases_soap_bleach_baking_soda": arch_21_everyday_household_bases_soap_bleach_baking_soda,
    "22_physical_sensory_properties_acids_sour_corrosive": arch_22_physical_sensory_properties_acids_sour_corrosive,
    "23_physical_sensory_properties_bases_bitter_soapy_caustic": arch_23_physical_sensory_properties_bases_bitter_soapy_caustic,
    "24_ranking_household_substances_ascending_or_descending_ph": arch_24_ranking_household_substances_ascending_or_descending_ph,
    "25_swimming_pool_water_ph_testing_phenol_red_balance": arch_25_swimming_pool_water_ph_testing_phenol_red_balance,
}
