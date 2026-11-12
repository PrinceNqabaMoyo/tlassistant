"""Grade 9 Natural Sciences - Reactions of Acids with a Metal: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/05. Reactions of acids with a metal.md.
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
        "id": f"ns9_ram_{code}_{rng.randint(100000, 999999)}",
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


def _svg_reactivity_tubes(rng: random.Random, labels: List[str], rates: List[int]) -> Dict[str, Any]:
    """Parameterized 4-tube bubble comparison for Mg, Zn, Fe, Cu reactivity in dilute HCl."""
    tubes = []
    for i, (lbl, n_bubbles) in enumerate(zip(labels, rates)):
        x = 45 + i * 92
        bubbles = "".join(
            f'<circle cx="{x + 14 + (b % 3) * 8}" cy="{158 - b * 9}" r="2.8" fill="#ffffff" stroke="#0284c7"/>'
            for b in range(n_bubbles)
        )
        tubes.append(
            f'<rect x="{x}" y="48" width="44" height="126" rx="8" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
            f'<rect x="{x + 3}" y="102" width="38" height="68" rx="4" fill="#e0f2fe" opacity="0.85"/>'
            f'<rect x="{x + 12}" y="160" width="20" height="7" fill="#64748b"/>'
            f'{bubbles}'
            f'<text x="{x + 22}" y="195" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{lbl}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 420 212" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="212" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="210" y="24" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Equal strips in 1 M HCl at 25 °C</text>'
        f'{"".join(tubes)}'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_metal_acid_particle_model(rng: random.Random, metal_sym: str, eq_scale: int) -> Dict[str, Any]:
    """Parameterized submicroscopic particle equation model for M + 2HCl -> MCl2 + H2."""
    y_off = rng.randint(-5, 5)
    m_x = 58
    hcl_x = 128
    salt_x = 295
    h2_x = 378
    svg = (
        f'<svg viewBox="0 0 430 190" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="190" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<text x="215" y="24" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Particle Conservation ({eq_scale}x scale): {metal_sym} + 2HCl -&gt; {metal_sym}Cl2 + H2</text>'
        f'<circle cx="{m_x}" cy="{100 + y_off}" r="18" fill="#94a3b8" stroke="#334155" stroke-width="2"/>'
        f'<text x="{m_x}" y="{104 + y_off}" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{metal_sym}</text>'
        f'<circle cx="{hcl_x}" cy="{76 + y_off}" r="10" fill="#ef4444" stroke="#7f1d1d"/>'
        f'<text x="{hcl_x}" y="{80 + y_off}" font-size="9" fill="#ffffff" text-anchor="middle">H</text>'
        f'<circle cx="{hcl_x + 25}" cy="{76 + y_off}" r="14" fill="#22c55e" stroke="#14532d"/>'
        f'<text x="{hcl_x + 25}" y="{80 + y_off}" font-size="10" fill="#ffffff" text-anchor="middle">Cl</text>'
        f'<circle cx="{hcl_x}" cy="{124 + y_off}" r="10" fill="#ef4444" stroke="#7f1d1d"/>'
        f'<text x="{hcl_x}" y="{128 + y_off}" font-size="9" fill="#ffffff" text-anchor="middle">H</text>'
        f'<circle cx="{hcl_x + 25}" cy="{124 + y_off}" r="14" fill="#22c55e" stroke="#14532d"/>'
        f'<text x="{hcl_x + 25}" y="{128 + y_off}" font-size="10" fill="#ffffff" text-anchor="middle">Cl</text>'
        f'<line x1="202" y1="100" x2="236" y2="100" stroke="#0f172a" stroke-width="2.5"/>'
        f'<polygon points="236,100 227,95 227,105" fill="#0f172a"/>'
        f'<circle cx="{salt_x - 24}" cy="{100 + y_off}" r="13" fill="#22c55e" stroke="#14532d"/>'
        f'<circle cx="{salt_x}" cy="{100 + y_off}" r="17" fill="#94a3b8" stroke="#334155"/>'
        f'<circle cx="{salt_x + 24}" cy="{100 + y_off}" r="13" fill="#22c55e" stroke="#14532d"/>'
        f'<text x="{salt_x}" y="{104 + y_off}" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">{metal_sym}Cl2</text>'
        f'<circle cx="{h2_x - 10}" cy="{100 + y_off}" r="10" fill="#ef4444" stroke="#7f1d1d"/>'
        f'<circle cx="{h2_x + 8}" cy="{100 + y_off}" r="10" fill="#ef4444" stroke="#7f1d1d"/>'
        f'<text x="{h2_x}" y="{126 + y_off}" font-size="10" fill="#991b1b" text-anchor="middle">H2 molecule</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_h2_volume_time_graph(rng: random.Random, v_max: int, t_end: int) -> Dict[str, Any]:
    """Parameterized hydrogen volume (cm^3) vs time (s) curve levelling off at t_end."""
    x_stop = 180 + t_end * 2
    y_top = 175 - int((v_max / 80.0) * 130)
    svg = (
        f'<svg viewBox="0 0 420 215" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="420" height="215" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<line x1="60" y1="25" x2="60" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="60" y1="175" x2="395" y2="175" stroke="#0f172a" stroke-width="2"/>'
        f'<line x1="60" y1="{y_top}" x2="385" y2="{y_top}" stroke="#cbd5e1" stroke-dasharray="4,4"/>'
        f'<line x1="{x_stop}" y1="{y_top}" x2="{x_stop}" y2="175" stroke="#94a3b8" stroke-dasharray="4,4"/>'
        f'<text x="52" y="{y_top + 4}" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="end">{v_max}</text>'
        f'<text x="52" y="178" font-size="11" fill="#334155" text-anchor="end">0</text>'
        f'<text x="{x_stop}" y="190" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{t_end} s</text>'
        f'<text x="225" y="207" font-size="11" fill="#0f172a" text-anchor="middle">Time (s)</text>'
        f'<text x="20" y="100" font-size="11" fill="#0f172a" transform="rotate(-90 20 100)" text-anchor="middle">H2 volume (cm³)</text>'
        f'<path d="M 60 175 Q 110 {y_top + 15}, {x_stop} {y_top} L 385 {y_top}" fill="none" stroke="#2563eb" stroke-width="3"/>'
        f'<circle cx="{x_stop}" cy="{y_top}" r="4.5" fill="#16a34a"/>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_26_zinc_plus_hydrochloric_acid_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    form = rng.choice(["zinc granules", "granulated zinc shot", "clean zinc foil"])
    prompt = (
        f"A small sample of **{form}** ($\\text{{Zn}}$) is placed into dilute hydrochloric acid ($\\text{{HCl}}$) inside a gas syringe generator.\n\n"
        "1. Write the **word equation** [1].\n"
        "2. Write the **balanced chemical equation** ($\\text{{Zn}}$ forms $Zn^{2+}$ ions) [2]."
    )
    correct = "Zinc + Hydrochloric acid -> Zinc chloride + Hydrogen gas; Zn + 2HCl -> ZnCl2 + H2"
    sol = (
        "**Step 1:** Word equation: **Zinc + Hydrochloric acid $\\rightarrow$ Zinc chloride + Hydrogen gas** [1].\n\n"
        "**Step 2:** Balancing with $ZnCl_2$ and $H_2$: **$$\\text{Zn} + 2\\text{HCl} \\rightarrow \\text{ZnCl}_2 + \\text{H}_2$$** [2]."
    )
    return _q(
        rng, "26", "26_zinc_plus_hydrochloric_acid_balanced_equation", prompt, correct, sol, 3, "structured",
        ["zinc_chloride_written_as_zncl_error"],
        "Zinc acts with +2 valency just like magnesium.",
        "Zn + 2HCl -> ZnCl2 + H2.",
        correct,
    )


def arch_27_iron_plus_hydrochloric_acid_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    obs = rng.choice(["slow streams of bubbles turning solution pale light green", "gradual bubbling leaving pale green aqueous iron(II) chloride"])
    prompt = (
        f"Clean **iron filings ($\\text{{Fe}}$)** react steadily in warm dilute hydrochloric acid ($\\text{{HCl}}$), showing **{obs}**.\n\n"
        "Write the **balanced chemical equation** forming iron(II) chloride ($\\text{FeCl}_2$) and hydrogen gas [3]."
    )
    correct = "Fe + 2HCl -> FeCl2 + H2"
    sol = (
        "**Step 1:** Iron(II) has charge $+2$, pairing with two $Cl^-$ ions to form **$\\text{FeCl}_2$** [1].\n\n"
        "**Step 2:** Place coefficient 2 before HCl to conserve both Cl and H atoms:\n"
        "**$$\\text{Fe} + 2\\text{HCl} \\rightarrow \\text{FeCl}_2 + \\text{H}_2$$** [2]."
    )
    return _q(
        rng, "27", "27_iron_plus_hydrochloric_acid_balanced_equation", prompt, correct, sol, 3, "short_answer",
        ["iron_hcl_omits_2_coefficient_error"],
        "Iron(II) chloride is explicitly FeCl2, so 2 HCl molecules are needed.",
        "Fe + 2HCl -> FeCl2 + H2.",
        correct,
    )


def arch_28_calcium_plus_hydrochloric_acid_vigorous_reaction(rng: random.Random) -> Dict[str, Any]:
    mass = rng.choice(["0,2 g", "0,5 g"])
    prompt = (
        f"Dropping **{mass}** of reactive Group 2 **calcium metal ($\\text{{Ca}}$)** into dilute hydrochloric acid triggers instant furious fizzing and strong warming.\n\n"
        "1. Write the **balanced chemical equation** for calcium reacting with hydrochloric acid [2].\n"
        "2. Explain why Group 2 calcium fizzes even more rapidly than zinc or iron in the same acid [1]."
    )
    correct = "Ca + 2HCl -> CaCl2 + H2; Calcium sits higher up in the metal reactivity series than zinc and iron"
    sol = (
        "**Step 1:** Calcium forms $Ca^{2+}$, yielding **$$\\text{Ca} + 2\\text{HCl} \\rightarrow \\text{CaCl}_2 + \\text{H}_2$$** [2].\n\n"
        "**Step 2:** Calcium loses valence electrons much more readily (higher **metal reactivity**), causing far faster effervescence [1]."
    )
    return _q(
        rng, "28", "28_calcium_plus_hydrochloric_acid_vigorous_reaction", prompt, correct, sol, 3, "structured",
        ["all_metals_react_at_same_rate_myth"],
        "Group 2 calcium behaves stoichiometrically like magnesium; compare metal reactivity.",
        "Ca + 2HCl -> CaCl2 + H2; higher reactivity -> faster bubbling.",
        correct,
    )


def arch_29_sodium_or_potassium_explosive_hazard_with_acids(rng: random.Random) -> Dict[str, Any]:
    alkali_metal = rng.choice(["sodium (Na)", "potassium (K)"])
    prompt = (
        f"Why must school science laboratories **NEVER** react Group 1 alkali metals such as **{alkali_metal}** directly with hydrochloric or sulfuric acid in an open test tube?"
    )
    correct = f"{alkali_metal.capitalize()} is dangerously hyper-reactive, generating hydrogen and heat explosively fast and splattering corrosive boiling acid glass."
    distractors = [
        f"{alkali_metal.capitalize()} is unreactive like gold so nothing happens at all.",
        "Alkali metals absorb all sound so the pop test stops working permanently.",
        "Potassium turns dilute hydrochloric acid into frozen water instantly.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Group 1 alkali metals (Na, K) react violently even with cold water.\n"
        f"**Step 2:** With strong acid, **{alkali_metal}** releases hydrogen gas and heat so violently that instant explosion/acid splatter occurs [2]."
    )
    return _q(
        rng, "29", "29_sodium_or_potassium_explosive_hazard_with_acids", prompt, correct, sol, 2, "multiple_choice",
        ["group1_metals_safe_in_school_acid_experiments_myth"],
        "Recall Group 1 alkali metals react violently even with pure water!",
        "Explosive exothermic H2 release splatters corrosive acid.",
        correct, options=options,
    )


def arch_30_magnesium_plus_sulfuric_acid_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    use_case = rng.choice(["Epsom salts (magnesium sulfate)", "soluble MgSO4 fertiliser solution"])
    prompt = (
        f"Magnesium ribbon reacts completely with dilute **sulfuric acid ($\\text{{H}}_2\\text{{SO}}_4$)** to form **{use_case}** and hydrogen gas.\n\n"
        "1. Write the **word equation** [1].\n"
        "2. Write the **balanced chemical equation** [2]."
    )
    correct = "Magnesium + Sulfuric acid -> Magnesium sulfate + Hydrogen gas; Mg + H2SO4 -> MgSO4 + H2"
    sol = (
        "**Step 1:** Word equation: **Magnesium + Sulfuric acid $\\rightarrow$ Magnesium sulfate + Hydrogen gas** [1].\n\n"
        "**Step 2:** Because $Mg^{2+}$ balances $SO_4^{2-}$ in a 1 : 1 ratio and sulfuric acid already provides 2 H atoms, it is balanced directly:\n"
        "**$$\\text{Mg} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{MgSO}_4 + \\text{H}_2$$** [2]."
    )
    return _q(
        rng, "30", "30_magnesium_plus_sulfuric_acid_balanced_equation", prompt, correct, sol, 3, "structured",
        ["sulfuric_acid_makes_magnesium_sulfide_error"],
        "Remember H2SO4 carries 2 H atoms AND an SO4 sulfate unit (valency -2).",
        "Mg + H2SO4 -> MgSO4 + H2 (balanced 1:1!).",
        correct,
    )


def arch_31_zinc_plus_sulfuric_acid_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    catalyst_note = rng.choice(["in a conical flask", "to fill a hydrogen balloon", "in a classroom gas generator"])
    prompt = (
        f"Zinc granules react with dilute **sulfuric acid ($\\text{{H}}_2\\text{{SO}}_4$)** {catalyst_note}.\n\n"
        "Which balanced equation correctly models this reaction?"
    )
    correct = "Zn + H2SO4 -> ZnSO4 + H2"
    distractors = [
        "Zn + H2SO4 -> ZnSO4 + H2O",
        "Zn + 2H2SO4 -> Zn(SO4)2 + H2",
        "Zn + H2SO4 -> ZnS + O2 + H2",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Zinc ($Zn^{2+}$) combines 1:1 with sulfate ($SO_4^{2-}$) to form **$\\text{ZnSO}_4$**, freeing the two acid hydrogens as **$\\text{H}_2$**.\n"
        "**Step 2:** Balanced equation: **$$\\text{Zn} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{ZnSO}_4 + \\text{H}_2$$** [2]."
    )
    return _q(
        rng, "31", "31_zinc_plus_sulfuric_acid_balanced_equation", prompt, correct, sol, 2, "multiple_choice",
        ["zinc_sulfate_makes_water_error"],
        "Pure metal + acid NEVER creates water (H2O); it makes H2 gas!",
        "Zn + H2SO4 -> ZnSO4 + H2.",
        correct, options=options,
    )


def arch_32_iron_plus_sulfuric_acid_green_salt_equation(rng: random.Random) -> Dict[str, Any]:
    shape = rng.choice(["iron nail", "iron wool strands", "clean iron filings"])
    prompt = (
        f"An unrusted **{shape}** ($\\text{{Fe}}$) dissolves slowly in dilute sulfuric acid ($\\text{{H}}_2\\text{{SO}}_4$), forming a pale green solution of iron(II) sulfate.\n\n"
        "Write the **word equation** and **balanced chemical equation** for this reaction [3]."
    )
    correct = "Iron + Sulfuric acid -> Iron(II) sulfate + Hydrogen gas; Fe + H2SO4 -> FeSO4 + H2"
    sol = (
        "**Step 1:** Word equation: **Iron + Sulfuric acid $\\rightarrow$ Iron(II) sulfate + Hydrogen gas** [1].\n\n"
        "**Step 2:** Balanced equation: **$$\\text{Fe} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{FeSO}_4 + \\text{H}_2$$** [2]."
    )
    return _q(
        rng, "32", "32_iron_plus_sulfuric_acid_green_salt_equation", prompt, correct, sol, 3, "short_answer",
        ["iron_sulfuric_acid_wrong_salt_formula_error"],
        "Iron(II) has +2 charge matching sulfate's -2 charge (1:1).",
        "Fe + H2SO4 -> FeSO4 + H2.",
        correct,
    )


def arch_33_salt_naming_chlorides_vs_sulfates_from_metal_acid_pairs(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Aluminium", "hydrochloric acid", "aluminium chloride"),
        ("Magnesium", "nitric acid", "magnesium nitrate"),
        ("Zinc", "sulfuric acid", "zinc sulfate"),
        ("Calcium", "sulfuric acid", "calcium sulfate"),
    ]
    m, a, s = rng.choice(cases)
    prompt = (
        f"Without needing a balanced formula equation, state the exact chemical name of the **salt** formed when **{m}** reacts with **{a}**, and name the other product [2]."
    )
    correct = f"{s.capitalize()} and hydrogen gas (H2)"
    sol = (
        f"**Step 1:** Combine the metal name (**{m.lower()}**) with the acid salt root ({a} -> **-{s.split()[-1]}**) = **{s.capitalize()}** [1].\n\n"
        "**Step 2:** The second product of acid + metal is always **hydrogen gas ($\\text{H}_2$)** [1]."
    )
    return _q(
        rng, "33", "33_salt_naming_chlorides_vs_sulfates_from_metal_acid_pairs", prompt, correct, sol, 2, "short_answer",
        ["misnaming_salt_anion_from_acid_error"],
        "Hydrochloric -> -chloride; Sulfuric -> -sulfate; Nitric -> -nitrate.",
        f"{s.capitalize()} + hydrogen gas.",
        correct,
    )


def arch_34_copper_gold_silver_unreactive_in_dilute_acids(rng: random.Random) -> Dict[str, Any]:
    noble_m = rng.choice(["copper (Cu)", "silver (Ag)", "gold (Au)"])
    active_m = rng.choice(["zinc (Zn)", "magnesium (Mg)"])
    prompt = (
        f"Two clean shiny metal strips — **{active_m}** and **{noble_m}** — are placed into separate test tubes of $1\\text{{ M}}$ hydrochloric acid. Bubbles race off {active_m}, while **{noble_m}** shows **no change and zero bubbles**.\n\n"
        f"Explain scientifically why **{noble_m}** fails to react with dilute hydrochloric acid [2]."
    )
    correct = f"{noble_m.capitalize()} lies below hydrogen in the metal reactivity series, so it is too unreactive to displace hydrogen gas from dilute HCl."
    sol = (
        f"**Step 1:** Metals vary widely in reactivity; **{noble_m}** is a low-reactivity (coinage/precious) metal placed **below hydrogen** in the reactivity series [1].\n\n"
        "**Step 2:** Therefore it cannot displace hydrogen ($H^+$) ions from dilute acids to release $\\text{H}_2$ gas (which is also why copper piping resists dilute vinegar/weak acids) [1]."
    )
    return _q(
        rng, "34", "34_copper_gold_silver_unreactive_in_dilute_acids", prompt, correct, sol, 2, "short_answer",
        ["claiming_copper_dissolves_violently_in_dilute_hcl_myth"],
        "Think about where gold, silver, and copper rank relative to hydrogen in chemical reactivity.",
        f"{noble_m.capitalize()} sits below hydrogen -> no reaction with dilute acids.",
        correct,
    )


def arch_35_ranking_metal_reactivity_from_bubble_rate_observations(rng: random.Random) -> Dict[str, Any]:
    order_pairs = rng.choice([
        (["Cu", "Mg", "Fe", "Zn"], [0, 8, 2, 5], "Mg > Zn > Fe > Cu"),
        (["Zn", "Fe", "Cu", "Mg"], [5, 2, 0, 8], "Mg > Zn > Fe > Cu"),
        (["Fe", "Cu", "Mg", "Zn"], [2, 0, 8, 5], "Mg > Zn > Fe > Cu"),
    ])
    labels, rates, ranking = order_pairs
    spec = _svg_reactivity_tubes(rng, labels, rates)
    prompt = (
        "Equal-sized strips of **Mg, Zn, Fe, and Cu** are dropped simultaneously into identical test tubes containing $1\\text{{ M}}$ HCl at $25\\,^\\circ\\text{{C}}$, shown in the diagram.\n\n"
        "1. Rank the four metals from **most reactive to least reactive** using the hydrogen bubble rates visible [2].\n"
        "2. Identify which tube produces ZERO bubbles [1]."
    )
    correct = f"{ranking}; Tube with Copper (Cu) produces zero bubbles"
    sol = (
        "**Step 1:** Faster $\\text{H}_2$ gas evolution corresponds directly to higher metal reactivity: magnesium bubbles furiously, zinc briskly, iron slowly, and copper none [2].\n\n"
        f"**Step 2:** Reactivity descending order: **{ranking}**, with **Cu** unreactive (0 bubbles) [1]."
    )
    return _q(
        rng, "35", "35_ranking_metal_reactivity_from_bubble_rate_observations", prompt, correct, sol, 3, "structured",
        ["ranking_copper_above_iron_error"],
        "Count the density of hydrogen bubbles rising in each labelled test tube.",
        f"Most bubbles -> fewest bubbles gives {ranking}.",
        correct, diagram_spec=spec,
    )


def arch_36_effect_of_metal_surface_area_powder_vs_ribbon_rate(rng: random.Random) -> Dict[str, Any]:
    mass = rng.choice(["1,0 g", "2,0 g"])
    prompt = (
        f"A learner reacts **{mass} of coarse zinc chunks** with $50\\text{{ ml}}$ of $1\\text{{ M}}$ HCl in Beaker A, and **{mass} of fine zinc powder** with identical HCl in Beaker B.\n\n"
        "Compare the **initial rate of hydrogen bubbling** AND the **final total volume of hydrogen produced** between Beaker A and Beaker B [3]."
    )
    correct = "Beaker B (zinc powder) bubbles much faster initially due to larger exposed surface area; Both beakers ultimately produce the exact same total volume of H2 because equal mass (moles) of zinc reacted"
    sol = (
        "**Step 1 (Rate):** Powdered zinc in **Beaker B exposes far greater surface area**, allowing many more acid–metal particle collisions per second -> faster initial H2 evolution [2].\n\n"
        f"**Step 2 (Total volume):** Since both beakers used the exact same mass (**{mass}**) of Zn and excess acid, the **final total volume of H2 gas is equal** [1]."
    )
    return _q(
        rng, "36", "36_effect_of_metal_surface_area_powder_vs_ribbon_rate", prompt, correct, sol, 3, "structured",
        ["powder_makes_twice_as_much_total_gas_myth"],
        "Distinguish how FAST gas forms (surface area) from HOW MUCH gas forms in total (mass of reactant).",
        "Greater surface area = faster rate; equal limiting mass = equal total H2 volume.",
        correct,
    )


def arch_37_effect_of_acid_concentration_and_temperature_on_h2_rate(rng: random.Random) -> Dict[str, Any]:
    factor = rng.choice([
        ("warming the HCl from 20 °C to 45 °C", "particles move faster with higher kinetic energy and collide more frequently and forcefully"),
        ("doubling HCl concentration from 0,5 M to 1,0 M", "twice as many acid particles occupy the same volume, doubling collision frequency per second"),
    ])
    change, reason = factor
    prompt = (
        f"While repeating the zinc + HCl practical, a group tries **{change}** while keeping metal strip size constant.\n\n"
        "State how the rate of hydrogen gas evolution changes and explain this in terms of **particle collisions** [2]."
    )
    correct = f"The reaction rate increases significantly; {reason}."
    sol = (
        "**Step 1:** The rate of hydrogen bubbling **increases** [1].\n\n"
        f"**Step 2:** Collision theory explanation: {reason} [1]."
    )
    return _q(
        rng, "37", "37_effect_of_acid_concentration_and_temperature_on_h2_rate", prompt, correct, sol, 2, "short_answer",
        ["temperature_slows_acid_metal_reactions_myth"],
        "Higher temperature or concentration means more effective collisions per second.",
        reason,
        correct,
    )


def arch_38_recovering_soluble_salt_crystals_via_filtration_and_evaporation(rng: random.Random) -> Dict[str, Any]:
    salt = rng.choice(["zinc sulfate (ZnSO4)", "magnesium chloride (MgCl2)"])
    prompt = (
        f"A learner reacts excess metal with acid until fizzing stops completely, intending to harvest pure dry crystals of **{salt}**.\n\n"
        "Outline the **two laboratory separation steps** needed after bubbling stops to obtain clean, dry salt crystals [2]."
    )
    correct = f"1. Filter the mixture to remove unreacted excess solid metal; 2. Gently heat/evaporate the clear filtrate solution (then let cool) so water leaves behind pure dry {salt} crystals."
    sol = (
        "**Step 1 (Filtration):** Filter off any excess solid metal granules sitting at the bottom to keep a clear aqueous solution of the salt [1].\n\n"
        f"**Step 2 (Evaporation/crystallisation):** Heat the clear filtrate gently to evaporate water, letting dry **{salt}** crystals form [1]."
    )
    return _q(
        rng, "38", "38_recovering_soluble_salt_crystals_via_filtration_and_evaporation", prompt, correct, sol, 2, "short_answer",
        ["evaporating_unfiltered_excess_metal_error"],
        "First remove leftover solid metal chunks, then separate dissolved salt from water.",
        "Step 1: Filtration; Step 2: Evaporation / crystallisation.",
        correct,
    )


def arch_39_writing_submicroscopic_particle_model_metal_acid_reaction(rng: random.Random) -> Dict[str, Any]:
    metal_sym = rng.choice(["Mg", "Zn", "Fe"])
    eq_scale = rng.choice([1, 2, 3])
    spec = _svg_metal_acid_particle_model(rng, metal_sym, eq_scale)
    prompt = (
        f"Study the submicroscopic particle model illustrating **{metal_sym}** reacting with hydrochloric acid at the atomic scale.\n\n"
        f"1. State the exact **chemical equation** represented by this model [1].\n"
        f"2. Identify which product particle on the right is **diatomic** and explain how chlorine atoms rearrange [2]."
    )
    correct = f"{metal_sym} + 2HCl -> {metal_sym}Cl2 + H2; H2 is the diatomic molecule while both Cl atoms transfer onto one {metal_sym} atom to form {metal_sym}Cl2"
    sol = (
        f"**Step 1:** Symbol equation represented: **${metal_sym} + 2\\text{{HCl}} \\rightarrow {metal_sym}\\text{{Cl}}_2 + \\text{{H}}_2$** [1].\n\n"
        f"**Step 2:** **$\\text{{H}}_2$** is the newly formed **diatomic** molecule (two bonded red H spheres), while two Cl spheres attach to one {metal_sym} sphere making **${metal_sym}\\text{{Cl}}_2$** [2]."
    )
    return _q(
        rng, "39", "39_writing_submicroscopic_particle_model_metal_acid_reaction", prompt, correct, sol, 3, "structured",
        ["breaking_molecules_creates_new_elements_myth"],
        "Count reactant and product particles across the arrow.",
        f"{metal_sym} + 2HCl -> {metal_sym}Cl2 + H2; H2 = diatomic gas.",
        correct, diagram_spec=spec,
    )


def arch_40_mass_conservation_open_beaker_vs_closed_flask_acid_metal(rng: random.Random) -> Dict[str, Any]:
    init_m = rng.choice([125.0, 140.0, 155.0])
    drop_m = rng.choice([0.4, 0.6, 0.8])
    rem_m = init_m - drop_m
    prompt = (
        f"A learner sets an open conical flask containing HCl and magnesium on an electronic scale reading **{_fmt_num(init_m)} g** at $t = 0$. "
        f"After bubbling ends, the open flask reads **{_fmt_num(rem_m)} g** ({_fmt_num(drop_m)} g less).\n\n"
        "Explain why this open-beaker mass drop does **NOT** violate the Law of Conservation of Mass [2]."
    )
    correct = f"Mass was conserved strictly: the missing {_fmt_num(drop_m)} g escaped into the room as invisible buoyant hydrogen gas (H2); inside a sealed balloon-capped flask total mass stays {_fmt_num(init_m)} g."
    sol = (
        f"**Step 1:** The **Law of Conservation of Mass** holds for closed systems [1].\n\n"
        f"**Step 2:** Because the flask was open, **{_fmt_num(drop_m)} g of hydrogen gas ($\\text{{H}}_2$)** floated upward out into the air, making the scale reading fall from {_fmt_num(init_m)} g to {_fmt_num(rem_m)} g [1]."
    )
    return _q(
        rng, "40", "40_mass_conservation_open_beaker_vs_closed_flask_acid_metal", prompt, correct, sol, 2, "short_answer",
        ["mass_is_destroyed_when_gas_escapes_myth"],
        "Remember hydrogen gas has real physical mass even though it is invisible and buoyant.",
        f"The {_fmt_num(drop_m)} g mass loss equals the mass of H2 gas that escaped out of the open flask.",
        correct,
    )


def arch_41_galvanised_iron_roofing_and_acid_rain_corrosion(rng: random.Random) -> Dict[str, Any]:
    region = rng.choice(["Highveld industrial towns", "Secunda and Witbank corridors", "coastal industrial estates"])
    prompt = (
        f"Zinc-coated (galvanised) corrugated iron roofs in **{region}** gradually wear thinner when exposed repeatedly to **acid rain** (containing dilute sulfuric acid, $\\text{{H}}_2\\text{{SO}}_4$).\n\n"
        "Explain chemically how acid rain attacks the zinc roofing layer, naming the two chemical products formed [3]."
    )
    correct = "Sulfuric acid in acid rain reacts chemically with the reactive zinc metal coating (Zn + H2SO4 -> ZnSO4 + H2), slowly dissolving the protective zinc into soluble zinc sulfate salt and hydrogen gas."
    sol = (
        "**Step 1:** Zinc is an active metal that reacts directly with dilute sulfuric acid in acid rain [1].\n\n"
        "**Step 2:** Reaction: **$\\text{Zn} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{ZnSO}_4 + \\text{H}_2$**, gradually stripping away the protective zinc coat as soluble **zinc sulfate** and **hydrogen gas** [2]."
    )
    return _q(
        rng, "41", "41_galvanised_iron_roofing_and_acid_rain_corrosion", prompt, correct, sol, 3, "short_answer",
        ["acid_rain_only_dissolves_rock_not_metal_myth"],
        "Apply acid + reactive metal rules to zinc roofing and rainwater containing H2SO4.",
        "Zn + H2SO4 -> zinc sulfate + hydrogen gas, eating away the galvanised coating.",
        correct,
    )


def arch_42_aluminium_citrus_food_pots_and_acid_leaching(rng: random.Random) -> Dict[str, Any]:
    food = rng.choice(["lemon pickle", "acidic tomato bredie", "rhubarb chutney", "vinegar-marinated achar"])
    prompt = (
        f"Chemists and chefs advise against storing strongly acidic **{food}** overnight inside bare, unlined **aluminium** or **galvanised zinc** cooking pots.\n\n"
        "Give the chemical reason for this kitchen rule [2]."
    )
    correct = f"Organic acids (like citric/ethanoic acid) in {food} slowly react with bare reactive aluminium or zinc metal, forming hydrogen gas and leaching dissolved metal salts into the food."
    sol = (
        f"**Step 1:** **{food.capitalize()}** contains dissolved acids (citric/ethanoic acid, pH ~2,5–3,8) [1].\n\n"
        "**Step 2:** Reactive pot metals slowly undergo **acid + metal reactions**, pitting the metal and contaminating the food with **dissolved aluminium/zinc salts** [1]."
    )
    return _q(
        rng, "42", "42_aluminium_citrus_food_pots_and_acid_leaching", prompt, correct, sol, 2, "short_answer",
        ["kitchen_acids_cannot_react_with_metals_myth"],
        "Apply acid + metal -> salt + hydrogen to reactive metal cookware.",
        "Food acids react with Al/Zn, pitting the pot and dissolving unwanted metal salts into the food.",
        correct,
    )


def arch_43_car_battery_sulfuric_acid_corroding_terminal_clamps(rng: random.Random) -> Dict[str, Any]:
    vehicle = rng.choice(["taxi minibus", "farm bakkie", "family sedan"])
    prompt = (
        f"A mechanic servicing a **{vehicle}** notices green-white powdery corrosion crust around brass/steel terminal clamps near a leaking 12 V lead-acid battery containing **sulfuric acid ($\\text{{H}}_2\\text{{SO}}_4$)**.\n\n"
        "1. Explain why leaking battery acid corrodes metal clamps and sparks an ignition risk [2].\n"
        "2. Suggest a safe household base paste to clean and neutralise the acid spill before scrubbing [1]."
    )
    correct = "Sulfuric acid reacts with metal clamps producing metal sulfate salts and flammable hydrogen gas (which can ignite from battery sparks); Dilute baking soda (sodium bicarbonate) solution"
    sol = (
        "**Step 1:** Sulfuric acid undergoes **acid + metal corrosion**, eating metal clamps into sulfate salts and liberating explosive **$\\text{H}_2$ gas** near electric sparks [2].\n\n"
        "**Step 2:** Applying mild alkaline **baking soda solution ($\\text{NaHCO}_3$)** safely neutralises spilled battery acid [1]."
    )
    return _q(
        rng, "43", "43_car_battery_sulfuric_acid_corroding_terminal_clamps", prompt, correct, sol, 3, "structured",
        ["cleaning_battery_acid_with_water_only_neutralises_myth"],
        "Think about flammable gas from acid + metal AND what weak household carbonate neutralises H2SO4.",
        "Acid + metal generates flammable H2; neutralise battery acid safely with baking soda (NaHCO3).",
        correct,
    )


def arch_44_vinegar_cleaning_tarnished_metal_oxide_vs_bare_copper(rng: random.Random) -> Dict[str, Any]:
    coin = rng.choice(["tarnished copper pot bottom", "dull dark-brown copper coin", "oxidised bronze plaque"])
    prompt = (
        f"Remember from an earlier question that bare copper does NOT react with dilute acid. Yet dipping a **{coin}** (coated in dark copper oxide, $\\text{{CuO}}$) into vinegar–salt solution restores bright shiny orange copper **without any fizzing**!\n\n"
        "Explain this clever chemical paradox [2]."
    )
    correct = "Ethanoic acid in vinegar reacts cleanly with the dark metal oxide coating (CuO + acid -> copper salt + water, no bubbles) exposing the clean bare copper beneath, which does not react with weak acid."
    sol = (
        "**Step 1:** Vinegar reacts with the **copper(II) oxide ($\\text{CuO}$) tarnish** via an acid + metal oxide neutralisation forming soluble copper salt + water (hence zero gas bubbles) [1].\n\n"
        "**Step 2:** Once bright pure copper is uncovered, copper lies below hydrogen in reactivity, so acid stops attacking the clean metal itself [1]."
    )
    return _q(
        rng, "44", "44_vinegar_cleaning_tarnished_metal_oxide_vs_bare_copper", prompt, correct, sol, 2, "short_answer",
        ["vinegar_cleans_by_dissolving_copper_metal_with_hydrogen_myth"],
        "Contrast Acid + Copper(II) Oxide (Ch. 6) vs Acid + Pure Copper Metal (Ch. 7).",
        "Vinegar removes the CuO oxide tarnish cleanly and stops at bare unreactive Cu.",
        correct,
    )


def arch_45_hydrogen_fuel_clean_combustion_and_climate_context(rng: random.Random) -> Dict[str, Any]:
    vehicle = rng.choice(["fuel-cell buses in Johannesburg", "clean aviation prototypes", "green hydrogen mining trucks in Limpopo"])
    prompt = (
        f"Engineers designing **{vehicle}** burn or react green **hydrogen gas ($\\text{{H}}_2$)** instead of fossil diesel because hydrogen's exhaust causes zero greenhouse warming directly.\n\n"
        "Write the combustion equation for hydrogen in oxygen and state the sole chemical exhaust product emitted [2]."
    )
    correct = "2H2 + O2 -> 2H2O; Pure water (steam/water vapour) only — zero CO2 greenhouse gas"
    sol = (
        "**Step 1:** Combustion equation: **$$2\\text{H}_2 + \\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O}$$** [1].\n\n"
        "**Step 2:** The only chemical product is pure **water ($\\text{H}_2\\text{O}$)** — releasing zero carbon dioxide ($\\text{CO}_2$) or soot [1]."
    )
    return _q(
        rng, "45", "45_hydrogen_fuel_clean_combustion_and_climate_context", prompt, correct, sol, 2, "short_answer",
        ["burning_hydrogen_emits_carbon_dioxide_myth"],
        "Notice there is NO carbon (C) atom anywhere on the reactant side of H2 + O2!",
        "2H2 + O2 -> 2H2O (only pure water vapour!).",
        correct,
    )


def arch_46_scientist_distinction_chemist_vs_pharmacist_in_south_africa(rng: random.Random) -> Dict[str, Any]:
    context = rng.choice(["a South African town high street vs an industrial analytical laboratory", "choosing Grade 10–12 Science career pathways"])
    prompt = (
        f"While discussing {context}, learners note that in some countries people casually call a corner shop dispenser a 'chemist'. In South Africa, however, **chemist** and **pharmacist** refer to two distinct regulated professions.\n\n"
        "Distinguish clearly between the work of a **chemist** and a **pharmacist** [2]."
    )
    correct = "A chemist researches matter, chemical reactions, composition, and synthesis/analysis in laboratories or industry; a pharmacist prepares, dispenses, and advises patients safely on medical prescriptions and medicines."
    sol = (
        "**Step 1:** A **chemist** investigates chemical properties, develops new materials/products, or runs quality/forensic analyses in labs and industry [1].\n\n"
        "**Step 2:** A **pharmacist** specialises in medicine formulation, dispensing doctor prescriptions, dosage safety, and patient healthcare counselling [1]."
    )
    return _q(
        rng, "46", "46_scientist_distinction_chemist_vs_pharmacist_in_south_africa", prompt, correct, sol, 2, "short_answer",
        ["chemist_and_pharmacist_mean_exact_same_career_in_sa_myth"],
        "Think: laboratory research/chemical analysis vs healthcare medicine dispensing.",
        "Chemist = chemical research & reactions; Pharmacist = medical dispensing & patient drug safety.",
        correct,
    )


def arch_47_chemistry_careers_geochemistry_mining_and_materials_science_sa(rng: random.Random) -> Dict[str, Any]:
    career, desc = rng.choice([
        ("Geochemist", "analyses the chemical composition of rocks, ores, and groundwater around South African mineral belts (e.g. Bushveld Complex)"),
        ("Forensic chemist", "analyses trace chemical evidence, toxins, and unknown powders from crime scenes"),
        ("Environmental chemist", "monitors river acidity (e.g. acid mine drainage), air pollutants, and industrial waste treatment"),
        ("Materials scientist", "engineers corrosion-resistant alloys, battery electrolytes, and lightweight composites"),
    ])
    prompt = (
        "Reactions between acids, bases, and metals underpin several vital South African STEM careers.\n\n"
        f"Describe the primary scientific role of a **{career}** and give one example of chemistry used in their daily work [2]."
    )
    correct = f"A {career.lower()} {desc}, applying laboratory analysis and chemical reaction principles."
    sol = (
        f"**Step 1:** **Role of a {career}:** {desc.capitalize()} [1].\n\n"
        "**Step 2:** This relies directly on understanding chemical elements, reactivity, and acid–metal/base reactions [1]."
    )
    return _q(
        rng, "47", "47_chemistry_careers_geochemistry_mining_and_materials_science_sa", prompt, correct, sol, 2, "short_answer",
        ["chemistry_only_applies_in_schools_myth"],
        f"Connect the prefix/focus of '{career}' to real South African industry or environmental applications.",
        f"{career}: {desc}.",
        correct,
    )


def arch_48_graphing_hydrogen_volume_over_time_reaction_progress(rng: random.Random) -> Dict[str, Any]:
    v_max = rng.choice([48, 60, 72])
    t_end = rng.choice([45, 60, 75])
    spec = _svg_h2_volume_time_graph(rng, v_max, t_end)
    prompt = (
        "Examine the plotted gas-collection curve recording the cumulative volume of hydrogen gas ($\\text{cm}^3$) collected every 15 s when magnesium ribbon reacts in hydrochloric acid.\n\n"
        f"1. State the maximum total volume of hydrogen gas produced [1].\n"
        f"2. At what exact time did the reaction finish, and how can this be read from the shape of the plotted curve? [2]"
    )
    correct = f"{v_max} cm³; Finished at {t_end} s where the curve becomes completely flat/horizontal (gradient = 0, no further gas evolved)"
    sol = (
        f"**Step 1:** Reading the plateau value gives **{v_max} cm³** of $\\text{{H}}_2$ gas [1].\n\n"
        f"**Step 2:** The curve becomes horizontal (zero slope / constant volume) at **$t = {t_end}\\text{{ s}}$**, showing all limiting reactant was consumed [2]."
    )
    return _q(
        rng, "48", "48_graphing_hydrogen_volume_over_time_reaction_progress", prompt, correct, sol, 3, "structured",
        ["flat_graph_means_gas_disappeared_myth"],
        "Read where the blue curve stops rising and turns horizontal!",
        f"Plateau = {v_max} cm³ reached at t = {t_end} s.",
        correct, diagram_spec=spec,
    )


def arch_49_identifying_unknown_gas_pop_test_vs_glowing_splint_vs_limewater(rng: random.Random) -> Dict[str, Any]:
    gas_case = rng.choice([
        ("Gas P", "extinguishes a burning splint with a sharp squeaky 'pop' sound", "Hydrogen (H2) — from Acid + Metal"),
        ("Gas Q", "turns clear limewater milky white when bubbled through", "Carbon dioxide (CO2) — from Acid + Metal carbonate"),
        ("Gas R", "causes a glowing wooden splint (with no flame) to burst brightly back into flame", "Oxygen (O2)"),
    ])
    g_lbl, obs, ans = gas_case
    prompt = (
        f"During an unlabelled laboratory gas bench check, a test on **{g_lbl}** shows that it **{obs}**.\n\n"
        f"Identify **{g_lbl}** and (if generated by an acid reaction) state the matching reactant class [2]."
    )
    correct = ans
    sol = (
        "**Step 1:** Match diagnostic signature:\n"
        "- Burning splint 'pop' -> Hydrogen ($\\text{H}_2$)\n"
        "- Cloudy limewater -> Carbon dioxide ($\\text{CO}_2$)\n"
        "- Relights glowing splint -> Oxygen ($\\text{O}_2$) [1].\n\n"
        f"**Step 2:** Result for {g_lbl}: **{ans}** [1]."
    )
    return _q(
        rng, "49", "49_identifying_unknown_gas_pop_test_vs_glowing_splint_vs_limewater", prompt, correct, sol, 2, "short_answer",
        ["mixing_glowing_splint_o2_test_with_burning_splint_h2_pop_test"],
        "Carefully distinguish GLOWING splint (relights O2) vs BURNING/LIT splint (pop for H2) vs LIMEWATER (CO2).",
        f"{g_lbl} -> {ans}.",
        correct,
    )


def arch_50_acid_reactions_term2_synthesis_metal_oxide_hydroxide_carbonate(rng: random.Random) -> Dict[str, Any]:
    row = rng.choice([
        ("Mg", "Mg + 2HCl -> MgCl2 + H2", "hydrogen gas (H2) only"),
        ("MgO", "MgO + 2HCl -> MgCl2 + H2O", "water (H2O) only, zero gas"),
        ("Mg(OH)2", "Mg(OH)2 + 2HCl -> MgCl2 + 2H2O", "water (H2O) only, zero gas"),
        ("MgCO3", "MgCO3 + 2HCl -> MgCl2 + H2O + CO2", "water (H2O) AND carbon dioxide gas (CO2)"),
    ])
    reactant, eq, extra = row
    prompt = (
        "Complete this Term 2 Chemical Reactions synthesis table task for hydrochloric acid reacting with four magnesium-family solids: **Mg, MgO, Mg(OH)2, and MgCO3**.\n\n"
        f"For **{reactant} + HCl**:\n"
        "1. Write the **balanced chemical equation** [2].\n"
        "2. Specify the non-salt by-product(s) formed and state whether effervescence occurs [2]."
    )
    correct = f"{eq}; By-product(s): {extra}"
    sol = (
        f"**Step 1:** Notice every member forms magnesium chloride ($\\text{{MgCl}}_2$): **$${eq}$$** [2].\n\n"
        f"**Step 2:** Non-salt product(s): **{extra}** [2]."
    )
    return _q(
        rng, "50", "50_acid_reactions_term2_synthesis_metal_oxide_hydroxide_carbonate", prompt, correct, sol, 4, "structured",
        ["confusing_term2_four_acid_reaction_families"],
        "Pure metal -> H2 gas; Oxide/Hydroxide -> H2O only; Carbonate -> H2O + CO2.",
        f"{eq} -> {extra}.",
        correct,
    )


BUILDERS_26_50: Dict[str, Any] = {
    "26_zinc_plus_hydrochloric_acid_balanced_equation": arch_26_zinc_plus_hydrochloric_acid_balanced_equation,
    "27_iron_plus_hydrochloric_acid_balanced_equation": arch_27_iron_plus_hydrochloric_acid_balanced_equation,
    "28_calcium_plus_hydrochloric_acid_vigorous_reaction": arch_28_calcium_plus_hydrochloric_acid_vigorous_reaction,
    "29_sodium_or_potassium_explosive_hazard_with_acids": arch_29_sodium_or_potassium_explosive_hazard_with_acids,
    "30_magnesium_plus_sulfuric_acid_balanced_equation": arch_30_magnesium_plus_sulfuric_acid_balanced_equation,
    "31_zinc_plus_sulfuric_acid_balanced_equation": arch_31_zinc_plus_sulfuric_acid_balanced_equation,
    "32_iron_plus_sulfuric_acid_green_salt_equation": arch_32_iron_plus_sulfuric_acid_green_salt_equation,
    "33_salt_naming_chlorides_vs_sulfates_from_metal_acid_pairs": arch_33_salt_naming_chlorides_vs_sulfates_from_metal_acid_pairs,
    "34_copper_gold_silver_unreactive_in_dilute_acids": arch_34_copper_gold_silver_unreactive_in_dilute_acids,
    "35_ranking_metal_reactivity_from_bubble_rate_observations": arch_35_ranking_metal_reactivity_from_bubble_rate_observations,
    "36_effect_of_metal_surface_area_powder_vs_ribbon_rate": arch_36_effect_of_metal_surface_area_powder_vs_ribbon_rate,
    "37_effect_of_acid_concentration_and_temperature_on_h2_rate": arch_37_effect_of_acid_concentration_and_temperature_on_h2_rate,
    "38_recovering_soluble_salt_crystals_via_filtration_and_evaporation": arch_38_recovering_soluble_salt_crystals_via_filtration_and_evaporation,
    "39_writing_submicroscopic_particle_model_metal_acid_reaction": arch_39_writing_submicroscopic_particle_model_metal_acid_reaction,
    "40_mass_conservation_open_beaker_vs_closed_flask_acid_metal": arch_40_mass_conservation_open_beaker_vs_closed_flask_acid_metal,
    "41_galvanised_iron_roofing_and_acid_rain_corrosion": arch_41_galvanised_iron_roofing_and_acid_rain_corrosion,
    "42_aluminium_citrus_food_pots_and_acid_leaching": arch_42_aluminium_citrus_food_pots_and_acid_leaching,
    "43_car_battery_sulfuric_acid_corroding_terminal_clamps": arch_43_car_battery_sulfuric_acid_corroding_terminal_clamps,
    "44_vinegar_cleaning_tarnished_metal_oxide_vs_bare_copper": arch_44_vinegar_cleaning_tarnished_metal_oxide_vs_bare_copper,
    "45_hydrogen_fuel_clean_combustion_and_climate_context": arch_45_hydrogen_fuel_clean_combustion_and_climate_context,
    "46_scientist_distinction_chemist_vs_pharmacist_in_south_africa": arch_46_scientist_distinction_chemist_vs_pharmacist_in_south_africa,
    "47_chemistry_careers_geochemistry_mining_and_materials_science_sa": arch_47_chemistry_careers_geochemistry_mining_and_materials_science_sa,
    "48_graphing_hydrogen_volume_over_time_reaction_progress": arch_48_graphing_hydrogen_volume_over_time_reaction_progress,
    "49_identifying_unknown_gas_pop_test_vs_glowing_splint_vs_limewater": arch_49_identifying_unknown_gas_pop_test_vs_glowing_splint_vs_limewater,
    "50_acid_reactions_term2_synthesis_metal_oxide_hydroxide_carbonate": arch_50_acid_reactions_term2_synthesis_metal_oxide_hydroxide_carbonate,
}
