"""Grade 9 Natural Sciences - Reactions of Metals with Oxygen: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/02. Reactions of metals with oxygen.md.
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
    guide = f"Marking Guide ({marks} marks): Award credit for each verified scientific step shown in the solution."
    item: Dict[str, Any] = {
        "id": f"ns9_rmo_{code}_{rng.randint(100000, 999999)}",
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


def arch_01_metal_oxidation_general_word_equation(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Magnesium", "Magnesium oxide"),
        ("Zinc", "Zinc oxide"),
        ("Calcium", "Calcium oxide"),
        ("Iron", "Iron oxide"),
        ("Copper", "Copper oxide"),
        ("Aluminium", "Aluminium oxide"),
    ]
    m, ox = rng.choice(metals)
    group_note = rng.choice(["Oxygen belongs to Group 16 on the Periodic Table.", "Metals lie to the left of the stepped line on the Periodic Table."])
    prompt = (
        f"When any reactive metal burns or heats in air, it undergoes oxidation. {group_note}\n\n"
        f"1. State the **general word equation** for the reaction between a metal and oxygen [1].\n"
        f"2. Apply this rule to write the **specific word equation** for **{m}** reacting with oxygen [1].\n"
        f"3. State the general chemical family name given to products like {ox} [1]."
    )
    correct = f"Metal + Oxygen -> Metal oxide; {m} + Oxygen -> {ox}; Family: Metal oxides"
    sol = (
        f"**Step 1:** General word equation: **Metal + Oxygen $\\rightarrow$ Metal oxide** [1].\n\n"
        f"**Step 2:** Specific word equation: **{m} + Oxygen $\\rightarrow$ {ox}** [1].\n\n"
        f"**Step 3:** Products of metal oxidation belong to the family of **metal oxides** [1]."
    )
    return _q(
        rng, "01", "01_metal_oxidation_general_word_equation", prompt, correct, sol, 3, "structured",
        ["oxidation_general_equation_error"],
        "Replace the non-metal placeholder: a metal combines directly with oxygen.",
        f"Think: Metal + Oxygen -> Metal oxide, so {m} forms {ox}.",
        correct,
    )


def arch_02_metal_oxide_definition_and_fixed_ratio(rng: random.Random) -> Dict[str, Any]:
    oxide, formula, ratio_desc = rng.choice([
        ("Magnesium oxide", "MgO", "1 magnesium atom to 1 oxygen atom (1 : 1)"),
        ("Sodium oxide", "Na2O", "2 sodium atoms to 1 oxygen atom (2 : 1)"),
        ("Calcium oxide", "CaO", "1 calcium atom to 1 oxygen atom (1 : 1)"),
        ("Aluminium oxide", "Al2O3", "2 aluminium atoms to 3 oxygen atoms (2 : 3)"),
    ])
    prompt = (
        f"Consider the compound **{oxide}** ($\\text{{{formula}}}$) formed when a pure metal reacts with oxygen.\n\n"
        "Which statement accurately defines a **metal oxide**?"
    )
    correct = f"A pure compound in which metal atoms are chemically bonded with oxygen atoms in a fixed ratio (here {ratio_desc})."
    distractors = [
        f"A physical mixture of metal filings shaken loosely with oxygen bubbles that separates on standing.",
        f"An acidic gas formed when oxygen molecules melt inside a heated beaker.",
        f"Any metal element whose atoms gain extra protons during combustion to turn into oxygen.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"**Step 1:** A **metal oxide** is a chemical compound formed when a metal bonds chemically with oxygen in a **fixed atomic ratio**.\n"
        f"**Step 2:** In {oxide} ({formula}), the atoms are chemically joined in a {ratio_desc} ratio, forming a new substance with distinct properties [2]."
    )
    return _q(
        rng, "02", "02_metal_oxide_definition_and_fixed_ratio", prompt, correct, sol, 2, "multiple_choice",
        ["compound_vs_mixture_oxide_myth"],
        "Is a metal oxide a physical mixture or a chemically bonded compound?",
        f"In {formula}, the subscript numbers reflect a fixed chemical ratio.",
        correct, options=options,
    )


def arch_03_three_levels_of_interpretation_macroscopic_submicroscopic_symbolic(rng: random.Random) -> Dict[str, Any]:
    task = rng.choice([
        ("Macroscopic", "Describing the blinding white flame and flaky white MgO powder seen in the classroom", "direct sensory observations without instruments seeing atoms"),
        ("Submicroscopic", "Visualising oxygen molecules splitting and bonding one-to-one with magnesium spheres", "imaginary mental or drawn particle models of atoms and molecules"),
        ("Symbolic", "Writing the balanced formula equation 2Mg + O2 -> 2MgO", "chemical symbols, formulas, subscripts, and balancing coefficients"),
    ])
    lvl, example, rationale = task
    prompt = (
        "Chemists interpret every metal oxidation reaction across three complementary levels.\n\n"
        f"In an experiment burning magnesium ribbon, a learner records: *\"{example}.\"*\n\n"
        f"1. Identify which of the three levels (**macroscopic**, **submicroscopic**, or **symbolic**) this represents [1].\n"
        f"2. Define what is focused on at that level [1]."
    )
    correct = f"{lvl} level; focuses on {rationale}."
    sol = (
        f"**Step 1:** This belongs to the **{lvl} level** [1].\n\n"
        f"**Step 2:** It focuses on {rationale}, connecting laboratory behaviour to chemical theory [1]."
    )
    return _q(
        rng, "03", "03_three_levels_of_interpretation_macroscopic_submicroscopic_symbolic", prompt, correct, sol, 2, "short_answer",
        ["macroscopic_submicroscopic_confusion"],
        "The three levels are Macroscopic (seen/felt), Submicroscopic (particles), and Symbolic (formulas).",
        f"Look closely at whether '{example[:42]}...' describes senses, particles, or formulas.",
        correct,
    )


def arch_04_iron_oxygen_rapid_steel_wool_combustion(rng: random.Random) -> Dict[str, Any]:
    flame_desc = rng.choice(["blue Bunsen flame", "pure oxygen gas jar", "tongs over a spirit burner"])
    prompt = (
        f"A small ball of fine steel wool is fluffed out with tongs and held in a **{flame_desc}**.\n\n"
        "1. State **two clear visual observations** during this combustion [2].\n"
        "2. Classify whether energy is absorbed overall or released to the surroundings [1].\n"
        "3. State the chemical name of the dark solid product formed [1]."
    )
    correct = "Orange/gold bright sparks shoot off and iron wool glows bright orange; Energy is released (exothermic reaction); Product: Iron oxide"
    sol = (
        "**Step 1:** Observations: **bright orange/golden sparks** shower outward and the wool glows intensely without a smoky yellow flame, cooling into a brittle dark grey-black/reddish solid [2].\n\n"
        "**Step 2:** Heat and light are given off, meaning it is an **exothermic combustion reaction** [1].\n\n"
        "**Step 3:** Product: **Iron oxide** (principally iron(III) oxide / triiron tetraoxide) [1]."
    )
    return _q(
        rng, "04", "04_iron_oxygen_rapid_steel_wool_combustion", prompt, correct, sol, 4, "structured",
        ["steel_wool_combustion_observation_error"],
        "Remember sparks and glowing fibres when iron strands burn in oxygen.",
        "Rapid oxidation gives off thermal and light energy (exothermic) forming iron oxide.",
        correct,
    )


def arch_05_steel_as_an_iron_alloy_identity(rng: random.Random) -> Dict[str, Any]:
    pct_c = rng.choice(["0,2%", "0,5%", "1,1%", "1,5%"])
    prompt = (
        f"In Grade 9 laboratories, steel wool containing approximately **98%–99% iron** mixed with **{pct_c} carbon** is burned to demonstrate the reaction of iron with oxygen.\n\n"
        "1. What scientific term describes a solid material like steel made by mixing a base metal with small amounts of other elements? [1]\n"
        "2. Why does burning steel wool serve as a valid laboratory model for the reaction of iron with oxygen? [1]"
    )
    correct = "An alloy; Because steel consists predominantly of iron atoms reacting with oxygen when heated."
    sol = (
        "**Step 1:** Steel is classified as a metal **alloy** [1].\n\n"
        f"**Step 2:** Steel consists overwhelmingly of **iron** (with only {pct_c} carbon added for strength), so its vigorous sparking in oxygen represents iron reacting with oxygen [1]."
    )
    return _q(
        rng, "05", "05_steel_as_an_iron_alloy_identity", prompt, correct, sol, 2, "short_answer",
        ["steel_is_pure_element_myth"],
        "A mixture of a metal with small percentages of carbon or other metals has a specific name.",
        "Steel = alloy mainly of Fe; the iron content drives the rapid oxidation.",
        correct,
    )


def arch_06_iron_filings_bunsen_flame_sparking(rng: random.Random) -> Dict[str, Any]:
    item_pair = rng.choice([
        ("iron filings sprinkled into a Bunsen flame", "solid iron block held in the same flame"),
        ("fluffed steel wool threads", "thick solid iron nail"),
    ])
    fast_obj, slow_obj = item_pair
    prompt = (
        f"When **{fast_obj}** react in air they produce bright showering sparks immediately, whereas a **{slow_obj}** merely heats up on the outside.\n\n"
        "Which factor explains this dramatic difference in reaction rate?"
    )
    correct = "Far greater exposed surface area of fine iron particles in contact with atmospheric oxygen molecules per second."
    options = [
        correct,
        "Fine iron filings contain more oxygen gas trapped inside each atom's nucleus than an iron nail.",
        "Large solid iron objects are completely non-reactive with Group 16 elements at all temperatures.",
        "Smaller pieces have lower density so gravity pushes them out of the oxygen zone faster.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Chemical reactions between a solid metal and oxygen gas only happen at the outer **contact surface**.\n"
        f"**Step 2:** {fast_obj.capitalize()} expose orders of magnitude more iron atoms to colliding $O_2$ molecules simultaneously, causing rapid visible sparking [2]."
    )
    return _q(
        rng, "06", "06_iron_filings_bunsen_flame_sparking", prompt, correct, sol, 2, "multiple_choice",
        ["surface_area_combustion_confusion"],
        "Think about how many iron atoms can touch oxygen molecules at once.",
        "Powders and thin threads expose a huge surface area to air.",
        correct, options=options,
    )


def arch_07_iron_rusting_word_and_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    metal_obj = rng.choice(["garden gate hinge", "iron railway spike", "mild steel chain", "unpainted burglar bar"])
    prompt = (
        f"An exposed **{metal_obj}** turns reddish-brown after several wet weeks outdoors.\n\n"
        "1. Write the **word equation** for iron rusting in oxygen [1].\n"
        "2. Write the **balanced chemical equation** for the formation of iron(III) oxide [2].\n"
        "3. Explain how this chemical change differs in speed from steel wool combustion [1]."
    )
    correct = "Iron + Oxygen -> Iron oxide; 4Fe + 3O2 -> 2Fe2O3; Rusting is slow ambient corrosion while steel wool combustion is rapid high-temperature oxidation"
    sol = (
        "**Step 1:** Word equation: **Iron + Oxygen $\\rightarrow$ Iron oxide** (forming hydrated iron(III) oxide) [1].\n\n"
        "**Step 2:** Balanced symbol equation: **$$4\\text{Fe} + 3\\text{O}_2 \\rightarrow 2\\text{Fe}_2\\text{O}_3$$** (4 Fe and 6 O atoms on each side) [2].\n\n"
        "**Step 3:** Rusting is **slow corrosion** occurring over days/weeks at ambient temperature in moisture, unlike rapid combustion with sparks [1]."
    )
    return _q(
        rng, "07", "07_iron_rusting_word_and_balanced_equation", prompt, correct, sol, 4, "structured",
        ["iron_oxide_balancing_error"],
        "Iron(III) oxide has formula Fe2O3; count oxygen atoms on both sides (LCM of 2 and 3 is 6).",
        "Need 3 O2 (= 6 O) and 2 Fe2O3 (= 6 O and 4 Fe) -> 4Fe + 3O2 -> 2Fe2O3.",
        correct,
    )


def arch_08_magnesium_combustion_observations_and_equation(rng: random.Random) -> Dict[str, Any]:
    length_cm = rng.choice([4, 5, 6, 8])
    prompt = (
        f"A **{length_cm} cm strip** of silvery magnesium ribbon is held with metal tongs in a roaring burner flame.\n\n"
        "1. Describe **two macroscopic observations** produced by the reaction [2].\n"
        "2. Write the **balanced chemical equation** (with state symbols) for magnesium burning in oxygen [2]."
    )
    correct = "1. Dazzling/blinding white flame and formation of crumbly white powder/ash (MgO); 2. 2Mg(s) + O2(g) -> 2MgO(s)"
    sol = (
        "**Step 1:** Observations: burns fiercely with an **intensely bright/blinding white flame**, leaving behind a **crumbly white solid ash (magnesium oxide)** [2].\n\n"
        "**Step 2:** Balanced chemical equation: **$$2\\text{Mg}(s) + \\text{O}_2(g) \\rightarrow 2\\text{MgO}(s)$$** [2]."
    )
    return _q(
        rng, "08", "08_magnesium_combustion_observations_and_equation", prompt, correct, sol, 4, "structured",
        ["magnesium_oxide_mgo2_subscript_error"],
        "Remember magnesium ribbon burns brightly and leaves white ash, not a dark solid.",
        "MgO has 1 Mg to 1 O, so balance 2Mg + O2 -> 2MgO.",
        correct,
    )


def arch_09_magnesium_combustion_eye_safety_ultraviolet(rng: random.Random) -> Dict[str, Any]:
    precaution = rng.choice([
        "Why must learners avoid looking directly at burning magnesium ribbon without protective tinted eye shields?",
        "What essential safety rule applies to onlookers during a teacher demonstration of magnesium combustion?",
    ])
    prompt = (
        "During a physical science demonstration, magnesium ribbon is ignited in a laboratory fume hood.\n\n"
        f"{precaution}"
    )
    correct = "The flame emits high-intensity visible and ultraviolet light that can injure retinas and cause temporary or permanent eye damage; look slightly away or wear UV-filtering safety goggles."
    options = [
        correct,
        "Looking directly at magnesium extinguishes the flame by absorbing heat through the eyes.",
        "Magnesium vapor freezes eye lenses instantly at temperatures below 0 °C.",
        "The white ash turns bright green only if someone looks straight at the crucible.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Magnesium combustion releases intense white light rich in **ultraviolet (UV) radiation**.\n"
        "**Step 2:** Staring directly at the flame risks **retinal burns or temporary blindness**, so learners look slightly aside or wear protective shaded goggles [2]."
    )
    return _q(
        rng, "09", "09_magnesium_combustion_eye_safety_ultraviolet", prompt, correct, sol, 2, "multiple_choice",
        ["magnesium_combustion_safety_omission"],
        "Think about the kind of radiation a blinding white light gives off.",
        "Intense UV/white light can harm the retina of the eye.",
        correct, options=options,
    )


def arch_10_magnesium_historical_camera_flash_powder(rng: random.Random) -> Dict[str, Any]:
    era = rng.choice(["late 1800s", "early 1900s", "pioneering studio photography"])
    prompt = (
        f"Before electronic xenon strobes existed in **{era}**, photographers used magnesium flash powder trays to light dark rooms.\n\n"
        "1. Which physical and chemical property of magnesium combustion made it suitable for photography? [2]\n"
        "2. Name the fine white smoke compound produced in the studio air immediately after the flash [1]."
    )
    correct = "Extremely rapid reaction with oxygen emitting an intensely bright white flash of light over a fraction of a second; Magnesium oxide (MgO)"
    sol = (
        "**Step 1:** Finely powdered magnesium oxidises almost instantaneously when ignited, releasing a burst of **intense white illumination** bright enough to expose film in milliseconds [2].\n\n"
        "**Step 2:** The white smoke settled as fine **magnesium oxide ($\\text{MgO}$)** ash [1]."
    )
    return _q(
        rng, "10", "10_magnesium_historical_camera_flash_powder", prompt, correct, sol, 3, "short_answer",
        ["historical_combustion_application"],
        "Photography needs intense white illumination in a very short burst.",
        "Rapid oxidation produces bright white light + solid MgO dust.",
        correct,
    )


def arch_11_particle_diagram_magnesium_oxidation(rng: random.Random) -> Dict[str, Any]:
    mg_col = rng.choice(["#7c3aed", "#6366f1", "#4f46e5"])
    o_col = rng.choice(["#dc2626", "#ef4444", "#b91c1c"])
    svg = (
        f'<svg viewBox="0 0 380 155" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="380" height="155" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="190" y="20" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Submicroscopic Oxidation of Magnesium</text>'
        f'<rect x="14" y="34" width="150" height="92" rx="6" fill="#ffffff" stroke="#94a3b8"/>'
        f'<text x="89" y="48" font-family="sans-serif" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Reactants</text>'
        f'<circle cx="46" cy="76" r="13" fill="{mg_col}" stroke="#1e293b"/><text x="46" y="80" font-size="9" fill="#fff" text-anchor="middle">Mg</text>'
        f'<circle cx="46" cy="108" r="13" fill="{mg_col}" stroke="#1e293b"/><text x="46" y="112" font-size="9" fill="#fff" text-anchor="middle">Mg</text>'
        f'<circle cx="116" cy="92" r="11" fill="{o_col}" stroke="#1e293b"/><text x="116" y="96" font-size="8" fill="#fff" text-anchor="middle">O</text>'
        f'<circle cx="138" cy="92" r="11" fill="{o_col}" stroke="#1e293b"/><text x="138" y="96" font-size="8" fill="#fff" text-anchor="middle">O</text>'
        f'<path d="M 173,80 L 203,80 M 198,75 L 205,80 L 198,85" fill="none" stroke="#0284c7" stroke-width="2.5"/>'
        f'<rect x="214" y="34" width="152" height="92" rx="6" fill="#ffffff" stroke="#94a3b8"/>'
        f'<text x="290" y="48" font-family="sans-serif" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Products (Paired Units)</text>'
        f'<circle cx="268" cy="76" r="13" fill="{mg_col}" stroke="#1e293b"/><text x="268" y="80" font-size="9" fill="#fff" text-anchor="middle">Mg</text>'
        f'<circle cx="292" cy="76" r="11" fill="{o_col}" stroke="#1e293b"/><text x="292" y="80" font-size="8" fill="#fff" text-anchor="middle">O</text>'
        f'<circle cx="268" cy="108" r="13" fill="{mg_col}" stroke="#1e293b"/><text x="268" y="112" font-size="9" fill="#fff" text-anchor="middle">Mg</text>'
        f'<circle cx="292" cy="108" r="11" fill="{o_col}" stroke="#1e293b"/><text x="292" y="112" font-size="8" fill="#fff" text-anchor="middle">O</text>'
        f'<text x="190" y="143" font-family="sans-serif" font-size="9" fill="#475569" text-anchor="middle">Total atoms: 2 Mg, 2 O before = 2 Mg, 2 O after</text>'
        f'</svg>'
    )
    prompt = (
        "Inspect the particle model diagram illustrating magnesium reacting with oxygen.\n\n"
        "1. How many magnesium atoms and oxygen molecules are shown on the reactant side? [1]\n"
        "2. Write the chemical formula of **one product formula unit** formed on the right [1].\n"
        "3. Why must **two** product units form from one $O_2$ molecule? [1]"
    )
    correct = "2 magnesium atoms and 1 diatomic oxygen molecule (2 O atoms); Formula of one unit: MgO; Because the 2 separated O atoms each bond with one Mg atom, conserving atoms"
    sol = (
        "**Step 1:** Reactants contain **2 single Mg atoms** and **1 bonded $O_2$ molecule (2 O atoms)** [1].\n\n"
        "**Step 2:** Each paired unit has 1 Mg joined to 1 O, giving formula **$\\text{MgO}$** [1].\n\n"
        "**Step 3:** Breaking the $O_2$ molecule releases 2 separate oxygen atoms; each bonds with a magnesium atom to produce **2 units of MgO**, conserving total atoms [1]."
    )
    return _q(
        rng, "11", "11_particle_diagram_magnesium_oxidation", prompt, correct, sol, 3, "structured",
        ["particle_model_coefficient_vs_formula"],
        "Look at one single bonded pair in the Products box: 1 purple Mg + 1 red O.",
        "One pair = MgO, and there are 2 separate pairs so 2Mg + O2 -> 2MgO.",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_12_group1_alkali_metal_oxide_formula_m2o(rng: random.Random) -> Dict[str, Any]:
    elem, sym, oxide, form, bal = rng.choice([
        ("Lithium", "Li", "Lithium oxide", "Li2O", "4Li + O2 -> 2Li2O"),
        ("Sodium", "Na", "Sodium oxide", "Na2O", "4Na + O2 -> 2Na2O"),
        ("Potassium", "K", "Potassium oxide", "K2O", "4K + O2 -> 2K2O"),
    ])
    prompt = (
        f"Metals in **Group 1** of the Periodic Table follow the general oxide formula pattern **$\\text{{M}}_2\\text{{O}}$**.\n\n"
        f"1. Predict the **name** and **chemical formula** of the oxide formed when **{elem} ({sym})** reacts with oxygen [2].\n"
        f"2. Write the **balanced chemical equation** for this oxidation reaction [2]."
    )
    correct = f"Name: {oxide}, Formula: {form}; Balanced equation: {bal}"
    sol = (
        f"**Step 1:** Group 1 element {elem} ({sym}) matches $\\text{{M}}_2\\text{{O}}$, giving **{oxide} ($\\text{{{form}}}$)** [2].\n\n"
        f"**Step 2:** Balancing with diatomic $O_2$: **$$\\text{{{bal}}}$$** [2]."
    )
    return _q(
        rng, "12", "12_group1_alkali_metal_oxide_formula_m2o", prompt, correct, sol, 4, "structured",
        ["group1_oxide_mo_error"],
        f"Substitute {sym} in place of M in the pattern M2O.",
        f"If product is {form}, you need 2 formula units per O2 molecule -> 4 {sym} atoms.",
        correct,
    )


def arch_13_group2_alkaline_earth_oxide_formula_mo(rng: random.Random) -> Dict[str, Any]:
    elem, sym, oxide, form, bal = rng.choice([
        ("Calcium", "Ca", "Calcium oxide", "CaO", "2Ca + O2 -> 2CaO"),
        ("Beryllium", "Be", "Beryllium oxide", "BeO", "2Be + O2 -> 2BeO"),
        ("Strontium", "Sr", "Strontium oxide", "SrO", "2Sr + O2 -> 2SrO"),
        ("Barium", "Ba", "Barium oxide", "BaO", "2Ba + O2 -> 2BaO"),
    ])
    prompt = (
        f"Just like magnesium, **Group 2** metals form oxides following the general formula **$\\text{{MO}}$**.\n\n"
        f"What are the **chemical formula** and **balanced reaction equation** when **{elem} ({sym})** burns completely in oxygen?"
    )
    correct = f"Formula: {form} ({oxide}); Equation: {bal}"
    options = [
        correct,
        f"Formula: {sym}2O ({oxide}); Equation: 4{sym} + O2 -> 2{sym}2O",
        f"Formula: {sym}O2 ({elem} dioxide); Equation: {sym} + O2 -> {sym}O2",
        f"Formula: {sym}2O3 ({oxide}); Equation: 4{sym} + 3O2 -> 2{sym}2O3",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** Substituting Group 2 {sym} into $\\text{{MO}}$ yields **{form}** ({oxide}).\n"
        f"**Step 2:** Two {form} units use 2 {sym} atoms and 1 $O_2$ molecule: **$$\\text{{{bal}}}$$** [2]."
    )
    return _q(
        rng, "13", "13_group2_alkaline_earth_oxide_formula_mo", prompt, correct, sol, 2, "multiple_choice",
        ["group2_oxide_subscript_error"],
        "Group 2 metals bond 1:1 with oxygen (MO).",
        f"Use {form} and put a coefficient 2 in front of {sym} and {form}.",
        correct, options=options,
    )


def arch_14_group13_aluminium_oxide_formula_m2o3(rng: random.Random) -> Dict[str, Any]:
    metal, sym, ox, form, bal = rng.choice([
        ("Aluminium", "Al", "Aluminium oxide", "Al2O3", "4Al + 3O2 -> 2Al2O3"),
        ("Gallium", "Ga", "Gallium oxide", "Ga2O3", "4Ga + 3O2 -> 2Ga2O3"),
    ])
    prompt = (
        f"Elements in Group 13 (valency 3) combine with oxygen (valency 2) using the formula ratio **$\\text{{M}}_2\\text{{O}}_3$**.\n\n"
        f"1. Write the formula of **{ox}** formed by **{metal} ({sym})** [1].\n"
        f"2. Write the **balanced chemical equation** for {metal} reacting with oxygen gas [2]."
    )
    correct = f"Formula: {form}; Balanced equation: {bal}"
    sol = (
        f"**Step 1:** Cross-valency gives 2 {sym} to 3 O: **$\\text{{{form}}}$** [1].\n\n"
        f"**Step 2:** To balance oxygen atoms ($O_2$ vs $O_3$), use 6 O atoms on each side: **$$\\text{{{bal}}}$$** [2]."
    )
    return _q(
        rng, "14", "14_group13_aluminium_oxide_formula_m2o3", prompt, correct, sol, 3, "structured",
        ["group13_oxide_balancing_error"],
        "Find the lowest common multiple of 2 oxygen atoms (O2) and 3 oxygen atoms (M2O3), which is 6.",
        f"2 {form} provides 6 O atoms, requiring 3 O2 and 4 {sym}.",
        correct,
    )


def arch_15_copper_oxidation_surface_blackening_observations(rng: random.Random) -> Dict[str, Any]:
    shape = rng.choice(["copper turning", "cleaned copper strip", "coiled copper wire", "copper coin"])
    prompt = (
        f"A shiny reddish-brown **{shape}** is heated steadily in the hot part of a Bunsen burner flame for three minutes.\n\n"
        "1. State the visible colour change observed on the surface of the metal [1].\n"
        "2. State the chemical name and formula of the new surface layer formed [2]."
    )
    correct = "Shiny reddish-brown copper turns dull black on the outer surface; Copper(II) oxide (CuO)"
    sol = (
        "**Step 1:** The shiny reddish-brown metal surface gradually becomes covered by a **dull black coating** (no bright sparks or vigorous flame occur) [1].\n\n"
        "**Step 2:** That black coating is **copper(II) oxide** with chemical formula **$\\text{CuO}$** [2]."
    )
    return _q(
        rng, "15", "15_copper_oxidation_surface_blackening_observations", prompt, correct, sol, 3, "short_answer",
        ["copper_oxide_color_confusion"],
        "Copper is much less reactive than magnesium; heating merely coats its outside black.",
        "Reddish-brown copper + oxygen -> black copper(II) oxide (CuO).",
        correct,
    )


def arch_16_copper_oxide_balanced_chemical_equation(rng: random.Random) -> Dict[str, Any]:
    context = rng.choice(["electrical wiring scrap heated in air", "a copper sheet roasted inside a kiln", "copper turnings heated over a flame"])
    prompt = (
        f"Consider **{context}**, where solid copper forms black copper(II) oxide ($\\text{{CuO}}$).\n\n"
        "1. Write the **word equation** for this reaction [1].\n"
        "2. Write the **balanced symbol equation** including state symbols [2]."
    )
    correct = "Copper + Oxygen -> Copper(II) oxide; 2Cu(s) + O2(g) -> 2CuO(s)"
    sol = (
        "**Step 1:** Word equation: **Copper + Oxygen $\\rightarrow$ Copper(II) oxide** [1].\n\n"
        "**Step 2:** Balanced equation: **$$2\\text{Cu}(s) + \\text{O}_2(g) \\rightarrow 2\\text{CuO}(s)$$** [2]."
    )
    return _q(
        rng, "16", "16_copper_oxide_balanced_chemical_equation", prompt, correct, sol, 3, "structured",
        ["copper_oxide_balancing_error"],
        "Oxygen enters as O2 gas; CuO contains only 1 O atom per unit.",
        "Put a 2 in front of Cu and 2 in front of CuO.",
        correct,
    )


def arch_17_copper_oxide_vs_magnesium_reactivity_contrast(rng: random.Random) -> Dict[str, Any]:
    pair_ctx = rng.choice(["magnesium vs copper", "iron wool vs copper sheet"])
    prompt = (
        f"When comparing the oxidation of **{pair_ctx}** in a burner flame, magnesium ignites into a dazzling white flame, whereas copper darkens slowly on its surface without ever catching fire.\n\n"
        "What does this difference prove chemically about copper compared to magnesium?"
    )
    correct = "Copper is far less reactive toward oxygen than magnesium, so it oxidises slowly at high heat without sustaining self-ignition or a bright flame."
    options = [
        correct,
        "Copper is a non-metal that cannot form metal oxides under any conditions.",
        "Copper has no oxygen-binding capacity and only accumulates black soot from the air.",
        "Magnesium is much heavier than copper, forcing it to attract more oxygen gas.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Metals differ markedly in chemical **reactivity**.\n"
        "**Step 2:** Magnesium sits high on the reactivity scale and oxidises vigorously; copper sits low on the scale and reacts slowly at high temperature only on the surface to yield black $\\text{CuO}$ [2]."
    )
    return _q(
        rng, "17", "17_copper_oxide_vs_magnesium_reactivity_contrast", prompt, correct, sol, 2, "multiple_choice",
        ["copper_unreactive_myth"],
        "Think about the reactivity series of metals.",
        "Copper DOES react when strongly heated, just slowly and calmly because of low reactivity.",
        correct, options=options,
    )


def arch_18_copper_oxide_color_and_hardness_property_change(rng: random.Random) -> Dict[str, Any]:
    aspect = rng.choice(["scraping off the black powder with a spatula", "comparing conductivity and lustre of the coating vs core metal"])
    prompt = (
        f"After heating a copper strip in air, a learner tests the product by **{aspect}**.\n\n"
        "State **two distinct property changes** between unreacted copper and the black product that prove a **chemical reaction** occurred (rather than merely a soot stain) [2]."
    )
    correct = "Shiny reddish-brown colour changed permanently to dull black powder; malleable metallic wire turned into brittle non-conducting solid powder (new substance CuO formed)."
    sol = (
        "**Step 1:** Property change 1: Colour permanently shifts from **lustrous reddish-brown** to **dull black** (and cannot be washed off with water like surface dust) [1].\n\n"
        "**Step 2:** Property change 2: Malleable, flexible, electrically conductive metal turns into a **brittle, flaky oxide powder** ($\\text{CuO}$) with different chemical/electrical properties [1]."
    )
    return _q(
        rng, "18", "18_copper_oxide_color_and_hardness_property_change", prompt, correct, sol, 2, "short_answer",
        ["copper_oxide_soot_misconception"],
        "Chemical reactions produce new substances with new physical and chemical properties.",
        "Compare appearance (shiny brown vs dull black) and mechanics/conductivity (malleable metal vs brittle oxide powder).",
        correct,
    )


def arch_19_metal_oxides_basic_alkaline_nature_universal_indicator(rng: random.Random) -> Dict[str, Any]:
    oxide_name, hydroxide = rng.choice([
        ("Magnesium oxide (MgO)", "magnesium hydroxide"),
        ("Calcium oxide (CaO)", "calcium hydroxide"),
        ("Sodium oxide (Na2O)", "sodium hydroxide"),
    ])
    prompt = (
        f"White ash of **{oxide_name}** is stirred into a beaker of pure distilled water (initially green pH 7 with Universal Indicator).\n\n"
        "1. State the colour change observed in Universal Indicator [1].\n"
        "2. State whether the resulting aqueous solution is **acidic, neutral, or basic (alkaline)** and give a plausible pH value [2]."
    )
    correct = f"Universal Indicator turns blue or purple/violet; Solution is basic (alkaline) with pH > 7 (around pH 9–13 depending on concentration, forming {hydroxide})."
    sol = (
        f"**Step 1:** Metal oxides react with water to form basic metal hydroxides (here {hydroxide}), turning green Universal Indicator **blue or purple** [1].\n\n"
        "**Step 2:** The solution is **basic (alkaline)** with **$\\text{pH} > 7$** (typically pH 9 to 13) [2]."
    )
    return _q(
        rng, "19", "19_metal_oxides_basic_alkaline_nature_universal_indicator", prompt, correct, sol, 3, "structured",
        ["metal_oxide_is_acidic_myth"],
        "Remember: Metal oxides dissolved in water are BASES.",
        "Bases turn Universal Indicator blue/violet and red litmus blue (pH > 7).",
        correct,
    )


def arch_20_metal_vs_nonmetal_oxide_ph_contrast(rng: random.Random) -> Dict[str, Any]:
    m_ox, nm_ox = rng.choice([
        ("Magnesium oxide", "Sulfur dioxide"),
        ("Calcium oxide", "Carbon dioxide"),
        ("Potassium oxide", "Phosphorus pentoxide"),
    ])
    prompt = (
        f"Equal small samples of **{m_ox}** (Solution X) and **{nm_ox}** (Solution Y) are bubbled or stirred into two separate jars of red/blue litmus water.\n\n"
        "Predict the pH classification (**above 7** or **below 7**) and red/blue litmus results for Solution X and Solution Y [4]."
    )
    correct = f"Solution X ({m_ox}, metal oxide): basic, pH > 7, turns red litmus blue; Solution Y ({nm_ox}, non-metal oxide): acidic, pH < 7, turns blue litmus red."
    sol = (
        f"**Step 1:** **{m_ox}** is a metal oxide -> dissolves to make a **basic** solution (**$\\text{{pH}} > 7$**), turning **red litmus blue** (blue litmus stays blue) [2].\n\n"
        f"**Step 2:** **{nm_ox}** is a non-metal oxide -> dissolves to make an **acidic** solution (**$\\text{{pH}} < 7$**), turning **blue litmus red** (red litmus stays red) [2]."
    )
    return _q(
        rng, "20", "20_metal_vs_nonmetal_oxide_ph_contrast", prompt, correct, sol, 4, "structured",
        ["litmus_color_inversion", "oxide_ph_inversion"],
        "Classify each compound first: metal oxide or non-metal oxide?",
        "Metal oxides -> Base (pH > 7, Red -> Blue). Non-metal oxides -> Acid (pH < 7, Blue -> Red).",
        correct,
    )


def arch_21_balancing_metal_oxygen_equations_coefficients_vs_subscripts(rng: random.Random) -> Dict[str, Any]:
    bad_eq, good_eq, ox_name = rng.choice([
        ("Mg + O2 -> MgO2", "2Mg + O2 -> 2MgO", "magnesium oxide"),
        ("Na + O2 -> NaO2", "4Na + O2 -> 2Na2O", "sodium oxide"),
        ("Fe + O2 -> FeO2", "4Fe + 3O2 -> 2Fe2O3", "iron(III) oxide"),
    ])
    prompt = (
        f"A learner tries to balance the combustion of a metal by writing: `$\\text{{{bad_eq}}}$`.\n\n"
        "1. Explain why changing the subscript inside the product formula is scientifically invalid [1].\n"
        f"2. Write the properly balanced chemical equation using the true fixed formula of **{ox_name}** [2]."
    )
    correct = f"Altering subscripts changes the compound's fixed chemical identity into a different/impossible substance; Correct balanced equation: {good_eq}"
    sol = (
        f"**Step 1:** Subscripts represent the fixed atomic bonding ratio defining the substance ({ox_name}); changing subscripts invents a completely different compound rather than balancing atoms [1].\n\n"
        f"**Step 2:** We must only adjust coefficients in front of authentic formulas: **$$\\text{{{good_eq}}}$$** [2]."
    )
    return _q(
        rng, "21", "21_balancing_metal_oxygen_equations_coefficients_vs_subscripts", prompt, correct, sol, 3, "structured",
        ["balancing_by_changing_subscripts_error"],
        "Only numbers in front (coefficients) may be altered when balancing.",
        f"Keep the true formula of {ox_name} and balance with leading coefficients: {good_eq}.",
        correct,
    )


def arch_22_mass_increase_when_metal_burns_in_open_crucible(rng: random.Random) -> Dict[str, Any]:
    m_start = rng.choice([2.4, 3.6, 4.8, 6.0])
    m_o = round(m_start * (16.0 / 24.0), 1)
    m_end = round(m_start + m_o, 1)
    m_start_str = str(m_start).replace(".", ",")
    m_end_str = str(m_end).replace(".", ",")
    m_o_str = str(m_o).replace(".", ",")
    prompt = (
        f"A cleaned strip of magnesium ribbon of mass **{m_start_str} g** is heated inside a loosely lidded crucible until completely converted to white magnesium oxide ash.\n"
        f"After cooling, the final ash has a mass of **{m_end_str} g**.\n\n"
        "1. Explain why the solid mass inside the crucible increased instead of staying constant [2].\n"
        "2. Calculate the mass of oxygen gas that chemically combined with the magnesium [1]."
    )
    correct = f"Atmospheric oxygen (O2) entered from outside the crucible and bonded chemically into solid MgO; Mass of oxygen combined = {m_o_str} g"
    sol = (
        "**Step 1:** In an open/loosely covered crucible, oxygen gas from the air entered the system and bonded with magnesium to become part of the solid $\\text{MgO}$ product; total mass of (Mg + $\\text{O}_2$) was still conserved [2].\n\n"
        f"**Step 2:** Mass of oxygen combined $= {m_end_str}\\text{{ g}} - {m_start_str}\\text{{ g}} = {m_o_str}\\text{{ g}}$ [1]."
    )
    return _q(
        rng, "22", "22_mass_increase_when_metal_burns_in_open_crucible", prompt, correct, sol, 3, "calculation",
        ["apparent_mass_violation_open_crucible"],
        "Did any gas from the surrounding air join the magnesium inside the crucible?",
        f"Subtract initial metal mass from final oxide mass: {m_end_str} - {m_start_str}.",
        correct,
    )


def arch_23_iron_rusting_dual_requirement_water_and_oxygen(rng: random.Random) -> Dict[str, Any]:
    target_tube = rng.choice([
        ("Tube A (Dry Air + CaCl2)", "will NOT rust", "anhydrous calcium chloride absorbs all water vapour so moisture is absent"),
        ("Tube B (Boiled Water + Oil Seal)", "will NOT rust", "boiling drives out dissolved O2 gas and the oil layer blocks new oxygen from entering"),
        ("Tube C (Tap Water + Open Air)", "WILL rust", "both atmospheric oxygen and liquid water are simultaneously present"),
        ("Tube D (Salt Water + Open Air)", "WILL rust fastest", "both water and O2 are present plus dissolved salt ions speed corrosion"),
    ])
    t_name, outcome, reason = target_tube
    c_oil = rng.choice(["#f59e0b", "#eab308"])
    svg = (
        f'<svg viewBox="0 0 400 155" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="400" height="155" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="200" y="18" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Iron Nail Corrosion Investigation (4 Test Tubes)</text>'
        # Tube A
        f'<rect x="26" y="34" width="60" height="92" rx="8" fill="#fff" stroke="#475569" stroke-width="1.5"/>'
        f'<rect x="28" y="102" width="56" height="22" fill="#e2e8f0"/><text x="56" y="116" font-size="7" fill="#334155" text-anchor="middle">CaCl2 dry</text>'
        f'<line x1="56" y1="54" x2="56" y2="96" stroke="#64748b" stroke-width="4"/><text x="56" y="142" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Tube A</text>'
        # Tube B
        f'<rect x="116" y="34" width="60" height="92" rx="8" fill="#fff" stroke="#475569" stroke-width="1.5"/>'
        f'<rect x="118" y="64" width="56" height="10" fill="{c_oil}"/><text x="146" y="60" font-size="7" fill="#92400e" text-anchor="middle">Oil seal</text>'
        f'<rect x="118" y="74" width="56" height="50" fill="#e0f2fe"/><text x="146" y="116" font-size="7" fill="#0369a1" text-anchor="middle">Boiled H2O</text>'
        f'<line x1="146" y1="80" x2="146" y2="112" stroke="#64748b" stroke-width="4"/><text x="146" y="142" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Tube B</text>'
        # Tube C
        f'<rect x="206" y="34" width="60" height="92" rx="8" fill="#fff" stroke="#475569" stroke-width="1.5"/>'
        f'<rect x="208" y="74" width="56" height="50" fill="#bae6fd"/><text x="236" y="60" font-size="7" fill="#334155" text-anchor="middle">Open air</text>'
        f'<line x1="236" y1="64" x2="236" y2="112" stroke="#b45309" stroke-width="4"/><text x="236" y="142" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Tube C</text>'
        # Tube D
        f'<rect x="296" y="34" width="60" height="92" rx="8" fill="#fff" stroke="#475569" stroke-width="1.5"/>'
        f'<rect x="298" y="74" width="56" height="50" fill="#93c5fd"/><text x="326" y="116" font-size="7" fill="#1e3a8a" text-anchor="middle">Salt water</text>'
        f'<line x1="326" y1="64" x2="326" y2="112" stroke="#9a3412" stroke-width="5"/><text x="326" y="142" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Tube D</text>'
        f'</svg>'
    )
    prompt = (
        "Examine the controlled rusting investigation diagram containing four identical clean iron nails.\n\n"
        f"1. Predict whether the iron nail in **{t_name}** will rust after two weeks [1].\n"
        "2. Explain your prediction in terms of the two environmental substances required for rusting [2]."
    )
    correct = f"{t_name} {outcome}; Because rusting requires BOTH oxygen AND water simultaneously, and in this tube {reason}."
    sol = (
        f"**Step 1:** Prediction for {t_name}: the nail **{outcome}** [1].\n\n"
        f"**Step 2:** Rusting requires both **oxygen ($O_2$)** and **water ($H_2O$)** simultaneously; in {t_name}, {reason} [2]."
    )
    return _q(
        rng, "23", "23_iron_rusting_dual_requirement_water_and_oxygen", prompt, correct, sol, 3, "structured",
        ["water_alone_causes_rust_myth"],
        "Rusting needs BOTH water AND oxygen at the same time.",
        f"Check which of oxygen or water is missing or enhanced in {t_name}.",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_24_rust_chemical_identity_flaky_iron_oxide(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice(["old steel bridge beam", "corroded coastal railway track", "unpainted corrugated fencing"])
    prompt = (
        f"Unlike shiny metallic iron, rust peeling off an **{scenario}** crumbles easily into brown dust.\n\n"
        "Why does iron continue corroding deeper once a first layer of rust forms on the surface?"
    )
    correct = "Rust (iron oxide) is flaky, porous, and expands outward so it cracks and flakes off, constantly exposing fresh deeper iron metal to air and water."
    options = [
        correct,
        "Rust is a living fungus that reproduces inward by digesting iron atoms.",
        "Iron oxide forms an airtight glass shield that pumps pure oxygen deep into the iron.",
        "Rust turns metallic iron into liquid mercury that evaporates away overnight.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Hydrated iron(III) oxide occupies more volume than iron and forms a **brittle, porous, flaky crust**.\n"
        "**Step 2:** As flakes detach, underlying iron reacts repeatedly with $O_2$ and $H_2O$ until structural failure occurs [2]."
    )
    return _q(
        rng, "24", "24_rust_chemical_identity_flaky_iron_oxide", prompt, correct, sol, 2, "multiple_choice",
        ["rust_protects_iron_like_aluminium_myth"],
        "Think about the texture of rust flakes: are they airtight or crumbly?",
        "Crumbly flakes fall away and expose fresh metal below.",
        correct, options=options,
    )


def arch_25_coastal_kzn_western_cape_accelerated_rusting(rng: random.Random) -> Dict[str, Any]:
    coast, inland = rng.choice([
        ("Durban (KwaZulu-Natal coast)", "Polokwane (inland Limpopo)"),
        ("Gqeberha (Eastern Cape coast)", "Bloemfontein (Free State Highveld)"),
        ("Cape Town / False Bay coast", "Kimberley (Northern Cape)"),
    ])
    prompt = (
        f"Motor vehicles and steel balcony railings in **{coast}** develop severe rust years sooner than identical vehicles kept in **{inland}**.\n\n"
        "Give **two climatic or chemical reasons** why coastal conditions accelerate iron corrosion so dramatically [2]."
    )
    correct = "1. Consistently high atmospheric humidity/moisture provides continuous water; 2. Airborne sea-salt spray (NaCl ions) acts as an electrolyte speeding up electron transfer during oxidation."
    sol = (
        f"**Step 1:** {coast} has continuously **high relative humidity and ocean mist**, keeping steel surfaces damp far longer than dry {inland} [1].\n\n"
        "**Step 2:** **Dissolved sea salt (sodium chloride)** in coastal mist increases electrical conductivity on wet metal, strongly accelerating electrochemical corrosion [1]."
    )
    return _q(
        rng, "25", "25_coastal_kzn_western_cape_accelerated_rusting", prompt, correct, sol, 2, "short_answer",
        ["salt_water_rust_acceleration_error"],
        "Compare coastal sea air vs dry inland air: think moisture and dissolved sea salt.",
        "High humidity + NaCl salt ions (electrolyte) accelerate rust formation.",
        correct,
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_metal_oxidation_general_word_equation": arch_01_metal_oxidation_general_word_equation,
    "02_metal_oxide_definition_and_fixed_ratio": arch_02_metal_oxide_definition_and_fixed_ratio,
    "03_three_levels_of_interpretation_macroscopic_submicroscopic_symbolic": arch_03_three_levels_of_interpretation_macroscopic_submicroscopic_symbolic,
    "04_iron_oxygen_rapid_steel_wool_combustion": arch_04_iron_oxygen_rapid_steel_wool_combustion,
    "05_steel_as_an_iron_alloy_identity": arch_05_steel_as_an_iron_alloy_identity,
    "06_iron_filings_bunsen_flame_sparking": arch_06_iron_filings_bunsen_flame_sparking,
    "07_iron_rusting_word_and_balanced_equation": arch_07_iron_rusting_word_and_balanced_equation,
    "08_magnesium_combustion_observations_and_equation": arch_08_magnesium_combustion_observations_and_equation,
    "09_magnesium_combustion_eye_safety_ultraviolet": arch_09_magnesium_combustion_eye_safety_ultraviolet,
    "10_magnesium_historical_camera_flash_powder": arch_10_magnesium_historical_camera_flash_powder,
    "11_particle_diagram_magnesium_oxidation": arch_11_particle_diagram_magnesium_oxidation,
    "12_group1_alkali_metal_oxide_formula_m2o": arch_12_group1_alkali_metal_oxide_formula_m2o,
    "13_group2_alkaline_earth_oxide_formula_mo": arch_13_group2_alkaline_earth_oxide_formula_mo,
    "14_group13_aluminium_oxide_formula_m2o3": arch_14_group13_aluminium_oxide_formula_m2o3,
    "15_copper_oxidation_surface_blackening_observations": arch_15_copper_oxidation_surface_blackening_observations,
    "16_copper_oxide_balanced_chemical_equation": arch_16_copper_oxide_balanced_chemical_equation,
    "17_copper_oxide_vs_magnesium_reactivity_contrast": arch_17_copper_oxide_vs_magnesium_reactivity_contrast,
    "18_copper_oxide_color_and_hardness_property_change": arch_18_copper_oxide_color_and_hardness_property_change,
    "19_metal_oxides_basic_alkaline_nature_universal_indicator": arch_19_metal_oxides_basic_alkaline_nature_universal_indicator,
    "20_metal_vs_nonmetal_oxide_ph_contrast": arch_20_metal_vs_nonmetal_oxide_ph_contrast,
    "21_balancing_metal_oxygen_equations_coefficients_vs_subscripts": arch_21_balancing_metal_oxygen_equations_coefficients_vs_subscripts,
    "22_mass_increase_when_metal_burns_in_open_crucible": arch_22_mass_increase_when_metal_burns_in_open_crucible,
    "23_iron_rusting_dual_requirement_water_and_oxygen": arch_23_iron_rusting_dual_requirement_water_and_oxygen,
    "24_rust_chemical_identity_flaky_iron_oxide": arch_24_rust_chemical_identity_flaky_iron_oxide,
    "25_coastal_kzn_western_cape_accelerated_rusting": arch_25_coastal_kzn_western_cape_accelerated_rusting,
}
