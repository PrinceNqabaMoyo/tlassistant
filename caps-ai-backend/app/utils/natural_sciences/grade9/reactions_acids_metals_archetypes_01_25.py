"""Grade 9 Natural Sciences - Reactions of Acids with a Metal: Archetypes 01 to 25.
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


def _svg_soap_bubble_h2_rig(rng: random.Random, metal_sym: str, acid_f: str, soap_shift: int) -> Dict[str, Any]:
    """Parameterized test tube + stopper + delivery tube into soapy water dish with rising H2 bubbles."""
    bx = 305 + soap_shift
    svg = (
        f'<svg viewBox="0 0 430 220" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="220" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<rect x="75" y="75" width="44" height="115" rx="8" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="78" y="132" width="38" height="55" rx="4" fill="#e0f2fe" opacity="0.85"/>'
        f'<rect x="86" y="172" width="22" height="7" fill="#64748b"/>'
        f'<polygon points="78,75 116,75 112,88 82,88" fill="#334155"/>'
        f'<path d="M 97 75 L 97 38 L 285 38 L 285 162" fill="none" stroke="#475569" stroke-width="3"/>'
        f'<rect x="240" y="145" width="135" height="45" rx="6" fill="#f1f5f9" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="243" y="155" width="129" height="32" rx="4" fill="#bae6fd" opacity="0.85"/>'
        f'<circle cx="{bx}" cy="128" r="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>'
        f'<circle cx="{bx + 18}" cy="96" r="9" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>'
        f'<circle cx="{bx - 10}" cy="62" r="10" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>'
        f'<text x="97" y="206" font-size="11" fill="#0f172a" text-anchor="middle">{metal_sym} + {acid_f}</text>'
        f'<text x="307" y="206" font-size="11" fill="#0f172a" text-anchor="middle">Dish with soapy water</text>'
        f'<text x="{bx + 30}" y="66" font-size="11" fill="#0369a1">Rising bubbles</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def _svg_labeled_apparatus_abcd(rng: random.Random, labels: Dict[str, str]) -> Dict[str, Any]:
    """Parameterized lettered (A-D) Mg + HCl delivery-tube apparatus diagram."""
    dx = rng.randint(-6, 6)
    svg = (
        f'<svg viewBox="0 0 430 225" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="430" height="225" fill="#ffffff" stroke="#e2e8f0"/>'
        f'<rect x="75" y="75" width="44" height="115" rx="8" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>'
        f'<rect x="78" y="135" width="38" height="52" rx="4" fill="#e0f2fe"/>'
        f'<rect x="86" y="175" width="22" height="6" fill="#64748b"/>'
        f'<polygon points="78,75 116,75 112,88 82,88" fill="#334155"/>'
        f'<path d="M 97 75 L 97 42 L {280 + dx} 42 L {280 + dx} 162" fill="none" stroke="#475569" stroke-width="3"/>'
        f'<rect x="235" y="145" width="130" height="45" rx="6" fill="#f1f5f9" stroke="#0f172a" stroke-width="2"/>'
        f'<circle cx="{292 + dx}" cy="112" r="9" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>'
        f'<text x="42" y="84" font-size="12" font-weight="bold" fill="#dc2626">A</text>'
        f'<line x1="53" y1="81" x2="77" y2="81" stroke="#dc2626" stroke-width="1.5"/>'
        f'<text x="188" y="30" font-size="12" font-weight="bold" fill="#dc2626">B</text>'
        f'<line x1="188" y1="33" x2="188" y2="41" stroke="#dc2626" stroke-width="1.5"/>'
        f'<text x="42" y="179" font-size="12" font-weight="bold" fill="#dc2626">C</text>'
        f'<line x1="53" y1="176" x2="86" y2="176" stroke="#dc2626" stroke-width="1.5"/>'
        f'<text x="382" y="174" font-size="12" font-weight="bold" fill="#dc2626">D</text>'
        f'<line x1="365" y1="170" x2="380" y2="170" stroke="#dc2626" stroke-width="1.5"/>'
        f'<text x="215" y="212" font-size="10.5" fill="#475569" text-anchor="middle">Acid-Metal Gas Generation Apparatus (trial shift {dx})</text>'
        f'</svg>'
    )
    return {"kind": "inline_svg", "svg": svg, "diagram_role": "context"}


def arch_01_hydrogen_chemical_formula_h2_diatomic_meaning(rng: random.Random) -> Dict[str, Any]:
    other_diatomics = rng.choice([("O2", "oxygen"), ("N2", "nitrogen"), ("Cl2", "chlorine")])
    other_f, other_n = other_diatomics
    prompt = (
        f"Like {other_n} ($\\text{{{other_f}}}$), pure **hydrogen gas** always travels around as pairs of chemically bonded atoms rather than isolated single atoms.\n\n"
        "1. Write the correct chemical formula for hydrogen gas [1].\n"
        "2. Explain what the scientific term **diatomic** means [1]."
    )
    correct = "H2; Diatomic means each molecule consists of two atoms of the same element covalently bonded together"
    sol = (
        "**Step 1:** Chemical formula of hydrogen gas: **$\\text{H}_2$** [1].\n\n"
        "**Step 2:** **Diatomic** ('two atoms') means two hydrogen atoms bond together chemically to form each stable molecule ($\\text{H}_2$) [1]."
    )
    return _q(
        rng, "01", "01_hydrogen_chemical_formula_h2_diatomic_meaning", prompt, correct, sol, 2, "short_answer",
        ["writing_hydrogen_gas_as_monatomic_H_error"],
        "Remember hydrogen sits among the 7 natural diatomic elements.",
        "H2 has subscript 2 because two atoms pair up into one molecule.",
        correct,
    )


def arch_02_hydrogen_etymology_water_generator_definition(rng: random.Random) -> Dict[str, Any]:
    prefix_pair = rng.choice([("'hydro' + 'gen'", "water + generator"), ("Greek 'hydro-' + '-genes'", "water + producer/creator")])
    words, meaning = prefix_pair
    prompt = (
        f"The element name **hydrogen** is derived from the classical roots {words} (literally *'{meaning}'*).\n\n"
        "Explain the chemical reaction behind this historical name [2]."
    )
    correct = "When hydrogen burns/reacts with oxygen in the air, the product formed is pure water (2H2 + O2 -> 2H2O), literally 'generating water'."
    sol = (
        "**Step 1:** When hydrogen ignites with oxygen in air, it forms **water ($\\text{H}_2\\text{O}$)** as its sole oxide product [1].\n\n"
        "**Step 2:** Hence *hydro-gen* means **'water generator'**, reflecting the reaction $2\\text{H}_2 + \\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O}$ [1]."
    )
    return _q(
        rng, "02", "02_hydrogen_etymology_water_generator_definition", prompt, correct, sol, 2, "short_answer",
        ["hydrogen_burns_to_make_carbon_dioxide_myth"],
        "Think about the product formed when hydrogen reacts with oxygen.",
        "H2 + O2 -> H2O ('water generator').",
        correct,
    )


def arch_03_hydrogen_periodic_table_position_and_lowest_density(rng: random.Random) -> Dict[str, Any]:
    mass_approx = rng.choice(["approx 1 u per atom (2 u per H2 molecule)", "atomic number 1, atomic mass 1"])
    prompt = (
        f"Hydrogen sits at the very top of the Periodic Table ({mass_approx}), making it the **lightest element** in the universe.\n\n"
        "1. Define **density** [1].\n"
        "2. Predict what happens when a balloon or soap bubble filled with $\\text{H}_2$ gas is released into ordinary room air, giving a physical reason [2]."
    )
    correct = "Density is mass per unit volume (D = m/V); Hydrogen bubbles rise/float upwards rapidly because hydrogen gas has a much lower density than surrounding air"
    sol = (
        "**Step 1:** **Density** is the amount of mass packed per unit volume of a substance ($D = m/V$) [1].\n\n"
        "**Step 2:** Because hydrogen molecules have the smallest mass and **lower density than air**, hydrogen soap bubbles and weather balloons **rise and float upwards** rapidly [2]."
    )
    return _q(
        rng, "03", "03_hydrogen_periodic_table_position_and_lowest_density", prompt, correct, sol, 3, "structured",
        ["hydrogen_sinks_because_density_confused_with_co2_myth"],
        "Recall D = mass/volume and compare atomic mass 1 vs nitrogen (14) and oxygen (16) in air.",
        "Much lighter molecules -> much lower density than air -> floats upwards.",
        correct,
    )


def arch_04_hydrogen_buoyancy_soap_bubbles_and_weather_balloons(rng: random.Random) -> Dict[str, Any]:
    metal_s, acid_f = rng.choice([("Mg", "HCl"), ("Zn", "HCl"), ("Mg", "H2SO4")])
    shift = rng.randint(-12, 12)
    spec = _svg_soap_bubble_h2_rig(rng, metal_s, acid_f, shift)
    prompt = (
        "Examine the experimental setup shown, in which a delivery tube channels gas from a metal + acid reaction beneath soapy water.\n\n"
        "1. Describe what happens to the soap bubbles once they detach from the dish surface [1].\n"
        "2. State what additional equipment a teacher needs to ignite the floating bubbles safely and what sound is heard [2]."
    )
    correct = "The hydrogen-filled soap bubbles float upwards into the air; A burning candle or glowing/burning wooden splint at arm's length produces a characteristic 'pop' sound"
    sol = (
        "**Step 1:** Filled with low-density $\\text{H}_2$, the soap bubbles **float upwards** away from the dish [1].\n\n"
        "**Step 2:** Touching a **burning candle/splint** to a rising bubble away from the tube ignites the trapped $\\text{H}_2$ in air with a **characteristic sharp 'pop' sound** [2]."
    )
    return _q(
        rng, "04", "04_hydrogen_buoyancy_soap_bubbles_and_weather_balloons", prompt, correct, sol, 3, "structured",
        ["bubbles_stay_on_dish_like_co2_myth"],
        "Watch where the text indicates bubbles move in the diagram: they rise into air.",
        "H2 rises upwards; small flames ignite rising bubbles with a pop sound.",
        correct, diagram_spec=spec,
    )


def arch_05_density_comparison_hydrogen_air_and_carbon_dioxide(rng: random.Random) -> Dict[str, Any]:
    rows = rng.choice([
        ("Hydrogen (0,09 kg/m³)", "Air (1,29 kg/m³)", "Carbon dioxide (1,98 kg/m³)"),
        ("Helium/Hydrogen (very low density)", "Room air (medium density)", "Carbon dioxide (high density)"),
    ])
    g1, g2, g3 = rows
    prompt = (
        f"Compare the room-temperature densities of three gases: **{g1}**, **{g2}**, and **{g3}**.\n\n"
        "Which gas will stay pooled at the bottom of an open upright flask, and which gas immediately escapes from the top?"
    )
    correct = "Carbon dioxide sinks/pools at the bottom (densest); Hydrogen immediately rises and escapes out of the top (least dense)."
    distractors = [
        "Hydrogen sinks to the bottom while carbon dioxide shoots straight upward into the ceiling.",
        "Both hydrogen and carbon dioxide sink beneath room air at identical speeds.",
        "Air sinks beneath carbon dioxide because nitrogen is heavier than CO2.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Gases denser than air (**CO2**) sink and pool inside upright glassware.\n"
        "**Step 2:** Gases far less dense than air (**H2**) rise buoyantly out of any open mouth [2]."
    )
    return _q(
        rng, "05", "05_density_comparison_hydrogen_air_and_carbon_dioxide", prompt, correct, sol, 2, "multiple_choice",
        ["confusing_co2_sinking_with_h2_rising"],
        "Dense sinks; light rises!",
        "1,98 > 1,29 (CO2 sinks); 0,09 < 1,29 (H2 rises).",
        correct, options=options,
    )


def arch_06_burning_splint_characteristic_pop_test_for_hydrogen(rng: random.Random) -> Dict[str, Any]:
    acid_choice = rng.choice(["hydrochloric acid", "dilute sulfuric acid"])
    metal_choice = rng.choice(["zinc granules", "magnesium ribbon", "iron filings"])
    prompt = (
        f"A learner reacts **{metal_choice}** with **{acid_choice}** in a test tube and collects the escaping colourless gas by holding an inverted tube over it.\n\n"
        "1. Describe the exact laboratory test used to confirm the gas is **hydrogen** [2].\n"
        "2. State the positive observation confirming hydrogen's presence [1]."
    )
    correct = "Hold a burning/lit wooden splint (or small flame) at the mouth of the test tube containing the collected gas; It extinguishes the splint while igniting the gas with a sharp 'pop' sound"
    sol = (
        "**Step 1:** Bring a **burning/lit wooden splint** to the mouth of the inverted test tube holding the gas [2].\n\n"
        "**Step 2:** Hydrogen mixes with atmospheric oxygen and burns rapidly with a **characteristic sharp 'pop' (barking) sound** [1]."
    )
    return _q(
        rng, "06", "06_burning_splint_characteristic_pop_test_for_hydrogen", prompt, correct, sol, 3, "structured",
        ["using_limewater_or_relight_splint_for_hydrogen_error"],
        "Remember the three gas tests: O2 relights glowing splint, CO2 turns limewater milky, H2 goes 'pop' with a flame!",
        "Lit/burning splint at tube mouth -> characteristic 'pop' sound.",
        correct,
    )


def arch_07_hydrogen_plus_oxygen_combustion_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    context = rng.choice(["the 'pop' test inside a test tube", "a hydrogen weather balloon igniting", "hydrogen rocket fuel combustion"])
    prompt = (
        f"During **{context}**, hydrogen gas combines rapidly with atmospheric oxygen gas, releasing energy.\n\n"
        "1. Write the **word equation** for this combustion reaction [1].\n"
        "2. Write the **balanced chemical equation** [2]."
    )
    correct = "Hydrogen + Oxygen -> Water; 2H2 + O2 -> 2H2O"
    sol = (
        "**Step 1:** Word equation: **Hydrogen + Oxygen $\\rightarrow$ Water** [1].\n\n"
        "**Step 2:** Since both gases are diatomic ($\\text{H}_2$ and $\\text{O}_2$), balance the two oxygen atoms by forming two water molecules:\n"
        "**$$2\\text{H}_2 + \\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O}$$** [2]."
    )
    return _q(
        rng, "07", "07_hydrogen_plus_oxygen_combustion_balanced_equation", prompt, correct, sol, 3, "short_answer",
        ["writing_h2_plus_o_gives_h2o_error"],
        "Remember both hydrogen (H2) and oxygen (O2) are diatomic!",
        "2 H2 + O2 -> 2 H2O balances 4 H and 2 O on each side.",
        correct,
    )


def arch_08_large_hydrogen_air_explosion_vs_small_pop_sound(rng: random.Random) -> Dict[str, Any]:
    vessel = rng.choice(["a 2-litre balloon filled with hydrogen-air mix", "a 5 ml test tube containing tiny H2 bubbles"])
    is_big = "2-litre" in vessel
    prompt = (
        "A tiny amount of hydrogen in oxygen makes a harmless tiny 'pop' sound, whereas a large tank or balloon full of hydrogen burns as a massive orange fireball and deafening boom.\n\n"
        f"Compare the energy release and risk if you ignite **{vessel}** and state why both involve the exact same chemical equation [2]."
    )
    if is_big:
        correct = "Igniting a 2-litre volume releases a huge amount of exothermic thermal energy almost instantaneously, causing a dangerous blast/fireball; chemically both convert H2 + O2 into H2O."
    else:
        correct = "Igniting only 5 ml releases very little total thermal energy (just a crisp audible pop safely contained in soap film or test tube); chemically both react via 2H2 + O2 -> 2H2O."
    sol = (
        "**Step 1:** The exact **same chemical reaction ($2\\text{H}_2 + \\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O}$)** occurs in every ignition [1].\n\n"
        "**Step 2:** Because energy released is proportional to reactant quantity, large mixed volumes create explosive shockwaves and fireballs, whereas tiny laboratory soap bubbles give a safe, quiet pop [1]."
    )
    return _q(
        rng, "08", "08_large_hydrogen_air_explosion_vs_small_pop_sound", prompt, correct, sol, 2, "short_answer",
        ["small_pop_and_fireball_are_different_reactions_myth"],
        "Think about amount of fuel reactant vs the chemical equation itself.",
        "Same 2H2 + O2 -> 2H2O reaction; total energy scales with the amount of hydrogen burned.",
        correct,
    )


def arch_09_safety_distance_flame_away_from_delivery_tube_reason(rng: random.Random) -> Dict[str, Any]:
    step_num = rng.choice([4, 5])
    prompt = (
        f"In Step {step_num} of the textbook practical (*Reaction between magnesium and hydrochloric acid*), learners are warned: "
        "***\"Hold the burning candle ONLY to the soap bubbles floating upwards — NEVER hold the flame directly against the end of the rubber delivery tube or test-tube stopper.\"***\n\n"
        "Explain the serious laboratory hazard that this safety instruction prevents [2]."
    )
    correct = "Holding a flame to the delivery tube could ignite gas streaming back into the generator test tube mixed with residual air/oxygen, causing an explosion and shattering hot glass with acid spray."
    sol = (
        "**Step 1:** Inside the reaction flask/delivery tube there is still a mixture of pressurized $\\text{H}_2$ gas and some air ($\text{O}_2$) [1].\n\n"
        "**Step 2:** Bringing a flame to the tube tip causes **flashback ignition** down into the stoppered test tube, which can **shatter glassware and spray corrosive HCl acid** [1]."
    )
    return _q(
        rng, "09", "09_safety_distance_flame_away_from_delivery_tube_reason", prompt, correct, sol, 2, "short_answer",
        ["testing_delivery_tube_nozzle_directly_is_safe_myth"],
        "Think about what is inside the delivery tube and stoppered flask containing HCl!",
        "Flame flashback could detonate H2/air inside the flask and shatter hot glass with acid.",
        correct,
    )


def arch_10_first_gas_bubbles_displaced_air_explanation(rng: random.Random) -> Dict[str, Any]:
    n_bubbles = rng.choice(["first 3–5", "very first few", "initial opening"])
    prompt = (
        f"Right after dropping magnesium into hydrochloric acid and sealing the stopper, the **{n_bubbles} gas bubbles** emerging from the delivery tube beneath soapy water do NOT pop when tested with a lit candle.\n\n"
        "Explain why those earliest bubbles fail to pop [2]."
    )
    correct = "The initial bubbles are mostly ordinary room air originally occupying the empty upper part of the test tube and delivery tube, pushed out ahead of the newly generated hydrogen gas."
    sol = (
        "**Step 1:** Before the stopper was fitted, the headspace above the acid and the inside of the delivery tube contained **room air** [1].\n\n"
        "**Step 2:** Expanding $\\text{H}_2$ pressure pushes that trapped **air** out first; only once the air is flushed away do pure $\\text{H}_2$ soap bubbles emerge and pop [1]."
    )
    return _q(
        rng, "10", "10_first_gas_bubbles_displaced_air_explanation", prompt, correct, sol, 2, "short_answer",
        ["first_bubbles_are_unreactive_hydrogen_myth"],
        "Ask yourself what filled the empty upper tube before reaction began.",
        "Displaced air exits the delivery tube before pure hydrogen fills it.",
        correct,
    )


def arch_11_test_tube_magnesium_hcl_delivery_tube_apparatus_parts(rng: random.Random) -> Dict[str, Any]:
    labels = {"A": "Rubber stopper", "B": "Gas delivery tube", "C": "Magnesium ribbon in dilute HCl", "D": "Soapy water dish"}
    ask_letter = rng.choice(["A", "B", "C", "D"])
    spec = _svg_labeled_apparatus_abcd(rng, labels)
    ans = labels[ask_letter]
    prompt = (
        "Inspect the acid–metal gas collection apparatus diagram showing four labelled features **A, B, C, and D**.\n\n"
        f"1. Identify feature **{ask_letter}** and explain its role in the practical investigation [2].\n"
        "2. State what happens to the pH reading inside the test tube before and after all magnesium reacts [1]."
    )
    correct = f"{ask_letter} = {ans}; Acid pH starts very low (~1) and increases as HCl is consumed during the reaction"
    sol = (
        f"**Step 1:** Label **{ask_letter}** identifies the **{ans}** (used either to seal gas escape, channel H2 safely, generate H2 from Mg + HCl, or trap floating bubbles in soap film) [2].\n\n"
        "**Step 2:** Because HCl acid is consumed while forming neutral $\\text{MgCl}_2$, the **pH rises/increases** from ~1 towards neutral (or becomes less acidic) [1]."
    )
    return _q(
        rng, "11", "11_test_tube_magnesium_hcl_delivery_tube_apparatus_parts", prompt, correct, sol, 3, "structured",
        ["stopper_and_delivery_tube_role_confusion"],
        "Trace the path from reactant tube (bottom left) -> seal (top) -> tubing -> bubble trap dish (right).",
        f"Letter {ask_letter} points to: {ans}.",
        correct, diagram_spec=spec,
    )


def arch_12_inverted_test_tube_upward_delivery_gas_collection(rng: random.Random) -> Dict[str, Any]:
    gas_target = rng.choice(["hydrogen gas (H2)", "gas X from zinc + HCl"])
    prompt = (
        f"When collecting **{gas_target}** dry without soap bubbles, a chemist holds an empty dry collecting test tube **upside-down (inverted)** over the gas outlet.\n\n"
        "Why must the test tube be held **mouth-downward (upward delivery)** rather than upright?"
    )
    correct = "Hydrogen is less dense than air and naturally rises upward, displacing heavier air downward out of the inverted tube."
    distractors = [
        "Hydrogen freezes inside the top of an upright tube.",
        "Holding the tube upside-down converts hydrogen into liquid hydrochloric acid.",
        "Hydrogen is denser than air so upside-down holding stops it overflowing onto the bench.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Hydrogen has the lowest gas density ($0{,}09\\text{ kg/m}^3$), far below air.\n"
        "**Step 2:** Holding the vessel **inverted** lets rising $\\text{H}_2$ accumulate at the closed top while heavier air escapes downward [2]."
    )
    return _q(
        rng, "12", "12_inverted_test_tube_upward_delivery_gas_collection", prompt, correct, sol, 2, "multiple_choice",
        ["collecting_hydrogen_in_upright_flask_error"],
        "Remember light gases rise up and trap in an inverted bell/tube.",
        "H2 rises into inverted top and pushes denser air out the bottom.",
        correct, options=options,
    )


def arch_13_general_word_equation_acid_plus_metal_salt_hydrogen(rng: random.Random) -> Dict[str, Any]:
    metal, acid, salt = rng.choice([
        ("Zinc", "hydrochloric acid", "zinc chloride"),
        ("Magnesium", "sulfuric acid", "magnesium sulfate"),
        ("Iron", "hydrochloric acid", "iron(II) chloride"),
    ])
    prompt = (
        "1. State the **general word equation** for the reaction between an acid and a reactive metal [2].\n"
        f"2. Apply this rule to predict the two products formed when **{metal}** reacts with **{acid}** [2]."
    )
    correct = f"Acid + Metal -> Salt + Hydrogen gas; Products: {salt} and hydrogen gas"
    sol = (
        "**Step 1:** General word equation: **Acid + Metal $\\rightarrow$ Salt + Hydrogen gas** (note: NO water and NO carbon dioxide form!) [2].\n\n"
        f"**Step 2:** Reacting {metal.lower()} with {acid} produces **{salt}** and **hydrogen gas** [2]."
    )
    return _q(
        rng, "13", "13_general_word_equation_acid_plus_metal_salt_hydrogen", prompt, correct, sol, 4, "structured",
        ["acid_plus_metal_produces_water_myth"],
        "Notice there is no oxygen/hydroxide base on the left — so where does hydrogen go? Straight out as H2 gas!",
        "Acid + Metal -> Salt + Hydrogen gas (no H2O!).",
        correct,
    )


def arch_14_investigative_question_and_hypothesis_mg_plus_hcl(rng: random.Random) -> Dict[str, Any]:
    part = rng.choice(["hypothesis", "investigative_question"])
    acid_conc = rng.choice(["1 M hydrochloric acid", "dilute 0,5 M HCl"])
    if part == "hypothesis":
        prompt = (
            f"Before dropping magnesium ribbon into **{acid_conc}**, a Grade 9 group wants to predict which gas will be produced and how solution pH will alter.\n\n"
            "Write a clear, testable **hypothesis** covering gas identity and pH change [2]."
        )
        correct = "When magnesium reacts with dilute HCl, hydrogen gas will be released (confirmed by a 'pop' with a lit flame) and the pH of the acid mixture will increase as acid reacts."
    else:
        prompt = (
            f"Design an experiment adding magnesium ribbon to **{acid_conc}** to determine reaction products and acidity change.\n\n"
            "Formulate **two scientific investigative questions** that cannot simply be answered with 'yes' or 'no' [2]."
        )
        correct = "1. What gaseous product is released when magnesium reacts with hydrochloric acid? 2. How does the pH of hydrochloric acid change during its reaction with magnesium?"
    sol = (
        "**Step 1:** Ground the statement clearly in observable evidence (bubbles / 'pop' test / pH colour change) [1].\n\n"
        f"**Step 2:** Model response: *{correct}* [1]."
    )
    return _q(
        rng, "14", "14_investigative_question_and_hypothesis_mg_plus_hcl", prompt, correct, sol, 2, "short_answer",
        ["hypothesis_unrelated_to_observations_error"],
        "Mention what happens to BOTH the gas product and the acid solution.",
        f"{correct}",
        correct,
    )


def arch_15_cleaning_magnesium_ribbon_oxide_layer_before_reaction(rng: random.Random) -> Dict[str, Any]:
    tool = rng.choice(["fine sandpaper", "emery cloth", "steel wool scourer"])
    prompt = (
        f"Before weighing 1 g of tarnished grey magnesium ribbon to react with HCl, a teacher rubs the strip briskly with **{tool}** until it shines silver.\n\n"
        "1. Name the dull chemical layer removed from the metal surface [1].\n"
        "2. Explain how failing to sand the ribbon changes the reaction observation [2]."
    )
    correct = "Magnesium oxide (MgO) tarnish layer; Acid reacts slowly first with the MgO coating without making hydrogen gas bubbles, delaying hydrogen effervescence until bare Mg is exposed"
    sol = (
        "**Step 1:** Exposure to air coats magnesium with dull **magnesium oxide ($\\text{MgO}$)** [1].\n\n"
        "**Step 2:** Because $\\text{MgO} + 2\\text{HCl} \\rightarrow \\text{MgCl}_2 + \\text{H}_2\\text{O}$ makes NO hydrogen gas, leaving the tarnish on delays bubbling and slows initial reaction rate until bare Mg metal is reached [2]."
    )
    return _q(
        rng, "15", "15_cleaning_magnesium_ribbon_oxide_layer_before_reaction", prompt, correct, sol, 3, "structured",
        ["magnesium_oxide_coating_releases_hydrogen_myth"],
        "Recall Chapter 2 (Metals with oxygen) + Chapter 6 (Acid + Metal oxide -> NO gas!).",
        "Sanding removes MgO crust so HCl touches bare Mg immediately -> instant H2 fizzing.",
        correct,
    )


def arch_16_macroscopic_observations_mg_in_hcl_effervescence_and_heat(rng: random.Random) -> Dict[str, Any]:
    mass = rng.choice(["1,0 g", "0,5 g"])
    prompt = (
        f"A learner drops **{mass}** of freshly cleaned magnesium ribbon into $40\\text{{ ml}}$ of $1\\text{{ M}}$ hydrochloric acid inside a glass test tube.\n\n"
        "List **three macroscopic observations** seen and felt directly at the test tube [3]."
    )
    correct = "Rapid fizzing/effervescence (colourless gas bubbles rise), the solid magnesium strip disappears/dissolves, and the bottom of the test tube feels noticeably warm (heat released)."
    sol = (
        "**Step 1:** Vigorous **bubbling / effervescence** of colourless hydrogen gas begins immediately [1].\n\n"
        "**Step 2:** The silver **magnesium ribbon shrinks and dissolves** leaving a clear solution of magnesium chloride [1].\n\n"
        "**Step 3:** The test tube glass becomes **warm** to the touch (exothermic reaction) [1]."
    )
    return _q(
        rng, "16", "16_macroscopic_observations_mg_in_hcl_effervescence_and_heat", prompt, correct, sol, 3, "short_answer",
        ["ignoring_heat_or_metal_dissolving_observations"],
        "Use three senses/observations: gas formed, solid metal fate, and temperature feel.",
        "Effervescence (bubbles), metal dissolves/disappears, test tube warms up.",
        correct,
    )


def arch_17_exothermic_temperature_rise_during_acid_metal_reaction(rng: random.Random) -> Dict[str, Any]:
    t_start = rng.choice([21, 22, 23])
    t_peak = t_start + rng.choice([14, 18, 22])
    prompt = (
        f"During an acid–metal practical, a thermometer recorded an initial hydrochloric acid temperature of **$T_1 = {t_start}\\,^\\circ\\text{{C}}$** and a peak reaction temperature of **$T_2 = {t_peak}\\,^\\circ\\text{{C}}$** after magnesium dissolved.\n\n"
        f"Calculate the temperature change $\\Delta T$ and classify the reaction energy profile [2]."
    )
    dt = t_peak - t_start
    correct = f"+{dt} °C; Exothermic reaction (thermal energy is released from the chemical system to the solution/surroundings)"
    sol = (
        f"**Step 1:** $\\Delta T = T_2 - T_1 = {t_peak} - {t_start} = +{dt}\\,^\\circ\\text{{C}}$ [1].\n\n"
        "**Step 2:** Because heat energy was released to raise solution temperature, it is **exothermic** [1]."
    )
    return _q(
        rng, "17", "17_exothermic_temperature_rise_during_acid_metal_reaction", prompt, correct, sol, 2, "short_answer",
        ["temperature_rise_means_endothermic_myth"],
        "Subtract initial from peak temperature; warming surroundings = energy exiting (exo-).",
        f"+{dt} °C temperature rise -> exothermic.",
        correct,
    )


def arch_18_solution_ph_increase_as_acid_is_consumed_by_metal(rng: random.Random) -> Dict[str, Any]:
    ph_before = rng.choice(["1,0", "1,2"])
    ph_after = rng.choice(["5,8", "6,5", "7,0"])
    prompt = (
        f"Before adding magnesium ribbon, a learner tests $1\\text{{ M}}$ hydrochloric acid with universal indicator paper and records **pH {ph_before}** (red). Once magnesium stops fizzing (with all acid reacted), the mixture reads **pH {ph_after}**.\n\n"
        "1. Did the pH increase, decrease, or remain constant? [1]\n"
        "2. Explain chemically why the solution became less acidic during the reaction [2]."
    )
    correct = f"pH increased (from {ph_before} to {ph_after}); Acid particles (HCl) were consumed reacting with magnesium to produce neutral magnesium chloride salt and escaping H2 gas, lowering H+ concentration"
    sol = (
        f"**Step 1:** The pH **increased** from **{ph_before}** to **{ph_after}** [1].\n\n"
        "**Step 2:** Higher pH means lower acidity: as magnesium reacted, hydrogen from HCl turned into escaping $\\text{H}_2$ gas while remaining solution formed dissolved neutral salt ($\\text{MgCl}_2$) [2]."
    )
    return _q(
        rng, "18", "18_solution_ph_increase_as_acid_is_consumed_by_metal", prompt, correct, sol, 3, "structured",
        ["thinking_higher_ph_means_more_acidic_myth"],
        "Remember moving up from pH 1 towards pH 7 means LESS acid remaining.",
        "HCl reacts -> less H+ remains in solution -> pH increases towards 7.",
        correct,
    )


def arch_19_limiting_reactant_complete_consumption_of_magnesium(rng: random.Random) -> Dict[str, Any]:
    scenario = rng.choice([
        ("All magnesium ribbon has completely vanished while universal indicator still turns bright red (pH ~1,5).", "Hydrochloric acid was in excess; magnesium was the limiting reactant that ran out first."),
        ("Fizzing stops completely while unreacted pieces of shiny magnesium ribbon sit at the bottom and universal indicator reads green (~pH 7).", "Magnesium metal was in excess; hydrochloric acid ran out completely first (limiting reactant)."),
    ])
    obs, conclusion = scenario
    prompt = (
        "After 5 minutes in a closed laboratory test tube, bubbling ceases completely.\n"
        f"**Observation:** {obs}\n\n"
        "Identify which reactant was **used up completely (limiting)** and which remained in **excess**, justifying from the observation [2]."
    )
    correct = conclusion
    sol = (
        "**Step 1:** A chemical reaction halts as soon as ONE reactant runs out.\n\n"
        f"**Step 2:** {conclusion} [2]."
    )
    return _q(
        rng, "19", "19_limiting_reactant_complete_consumption_of_magnesium", prompt, correct, sol, 2, "short_answer",
        ["reaction_stops_only_when_temperature_cools_myth"],
        "Check what visible substance or pH clue remains at the end of the reaction.",
        conclusion,
        correct,
    )


def arch_20_magnesium_plus_hydrochloric_acid_word_equation(rng: random.Random) -> Dict[str, Any]:
    prompt_form = rng.choice(["Write out the complete word equation", "Identify the salt and gas named in the word equation"])
    metal = rng.choice(["Magnesium", "magnesium ribbon"])
    prompt = (
        f"During the investigation reacting **{metal}** with **hydrochloric acid**, {prompt_form.lower()} representing the overall reaction [2]."
    )
    correct = "Magnesium + Hydrochloric acid -> Magnesium chloride + Hydrogen gas"
    sol = (
        "**Step 1:** Substitute specific reactants into Acid + Metal -> Salt + Hydrogen [1].\n\n"
        "**Step 2:** **Magnesium + Hydrochloric acid $\\rightarrow$ Magnesium chloride + Hydrogen gas** [1]."
    )
    return _q(
        rng, "20", "20_magnesium_plus_hydrochloric_acid_word_equation", prompt, correct, sol, 2, "short_answer",
        ["magnesium_oxide_or_hydroxide_in_word_equation_error"],
        "Hydrochloric acid always gives '-chloride' salts; acid + metal gives hydrogen gas.",
        "Magnesium + Hydrochloric acid -> Magnesium chloride + Hydrogen gas.",
        correct,
    )


def arch_21_magnesium_plus_hydrochloric_acid_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    phase_note = rng.choice(["Show all reactants on the left and products on the right.", "Include correct subscripts and stoichiometric coefficients."])
    prompt = (
        f"Write the **balanced chemical equation** using chemical formulas for the reaction between **magnesium metal ($\\text{{Mg}}$)** and **hydrochloric acid ($\\text{{HCl}}$)**. {phase_note} [3]"
    )
    correct = "Mg + 2HCl -> MgCl2 + H2"
    sol = (
        "**Step 1:** Reactants: $\\text{Mg}$ and $\\text{HCl}$. Products: $\\text{MgCl}_2$ + $\\text{H}_2$ [1].\n\n"
        "**Step 2:** Notice two H atoms make one $\\text{H}_2$ molecule and two Cl atoms bond with one $Mg^{2+}$ ion, so place coefficient **2** before $\\text{HCl}$:\n"
        "**$$\\text{Mg} + 2\\text{HCl} \\rightarrow \\text{MgCl}_2 + \\text{H}_2$$** [2]."
    )
    return _q(
        rng, "21", "21_magnesium_plus_hydrochloric_acid_balanced_equation", prompt, correct, sol, 3, "short_answer",
        ["mg_plus_hcl_gives_mgcl_plus_h_error"],
        "Remember hydrogen gas is H2 and magnesium ions carry +2 charge (MgCl2).",
        "Need 2 HCl per Mg to make 1 MgCl2 + 1 H2.",
        correct,
    )


def arch_22_deriving_mgcl2_formula_after_removing_h2_from_2hcl(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([("magnesium", "Mg", "MgCl2"), ("zinc", "Zn", "ZnCl2"), ("calcium", "Ca", "CaCl2")])
    name, sym, salt = pair
    prompt = (
        f"A Grade 9 guide explains formula construction step-by-step for **{name} ($\\text{{{sym}}}$) + hydrochloric acid ($\\text{{HCl}}$)**:\n"
        "1. Forming **one $\\text{H}_2$** molecule removes **two H** atoms from HCl, forcing us to take **two $\\text{HCl}$** units.\n"
        "2. How many chlorine atoms remain available after removing the two H atoms, and what is the formula of the resulting ionic chloride salt? [2]"
    )
    correct = f"2 Cl atoms remain; they combine with one {sym}2+ atom/ion to form {salt}"
    sol = (
        "**Step 1:** Starting from $2\\text{HCl}$ and removing $\\text{H}_2$ leaves **2 Cl atoms** ($2\\,Cl^-$) [1].\n\n"
        f"**Step 2:** Pairing those 2 Cl atoms with 1 {name} atom gives **{salt}** [1]."
    )
    return _q(
        rng, "22", "22_deriving_mgcl2_formula_after_removing_h2_from_2hcl", prompt, correct, sol, 2, "short_answer",
        ["salt_chloride_subscript_missing_error"],
        "Look at what stays behind when H2 is taken out of 2HCl: two Cl particles!",
        f"1 {sym} + 2 Cl -> {salt}.",
        correct,
    )


def arch_23_atomic_conservation_count_mg_2hcl_equation(rng: random.Random) -> Dict[str, Any]:
    coeff = rng.choice([1, 2, 3])
    mg_n = coeff
    hcl_n = 2 * coeff
    prompt = (
        f"Check conservation of atoms in the scaled reaction:\n"
        f"$$ {mg_n if mg_n > 1 else ''}\\text{{Mg}} + {hcl_n}\\text{{HCl}} \\rightarrow {mg_n if mg_n > 1 else ''}\\text{{MgCl}}_2 + {mg_n if mg_n > 1 else ''}\\text{{H}}_2 $$\n\n"
        "Count the exact total number of **H**, **Cl**, and **Mg** atoms on BOTH sides of the arrow [3]."
    )
    correct = f"Left = Right: {mg_n} Mg atom(s), {hcl_n} H atoms, and {hcl_n} Cl atoms on both sides"
    sol = (
        f"**Step 1 (Left):** {mg_n} Mg + {hcl_n} H + {hcl_n} Cl [1].\n\n"
        f"**Step 2 (Right):** {mg_n} Mg + {hcl_n} Cl (inside {mg_n} MgCl2) + {hcl_n} H (inside {mg_n} H2) [2]."
    )
    return _q(
        rng, "23", "23_atomic_conservation_count_mg_2hcl_equation", prompt, correct, sol, 3, "short_answer",
        ["hydrogen_subscript_multiplied_wrongly_error"],
        "Multiply each front coefficient by each subscript inside the molecule.",
        f"{mg_n} Mg, {hcl_n} H, {hcl_n} Cl on both sides.",
        correct,
    )


def arch_24_comparing_acid_metal_vs_acid_carbonate_gas_products(rng: random.Random) -> Dict[str, Any]:
    tube_a, tube_b = rng.choice([("magnesium strip", "calcium carbonate powder"), ("zinc strip", "baking soda (NaHCO3)")])
    prompt = (
        f"A learner adds dilute HCl to Test Tube 1 (**{tube_a}**) and Test Tube 2 (**{tube_b}**). Both tubes fizz vigorously releasing colourless gases.\n\n"
        "Compare the **gas identities** and the **confirming diagnostic test + positive result** for each tube [4]."
    )
    correct = "Test Tube 1 releases Hydrogen (H2) -> burns with sharp 'pop' using lit splint; Test Tube 2 releases Carbon dioxide (CO2) -> turns clear limewater milky/cloudy"
    sol = (
        f"**Step 1 (Tube 1, metal {tube_a}):** Produces **hydrogen ($\\text{{H}}_2$)** gas, confirmed by a **'pop' sound** when ignited with a burning splint [2].\n\n"
        f"**Step 2 (Tube 2, carbonate {tube_b}):** Produces **carbon dioxide ($\\text{{CO}}_2$)** gas, confirmed when bubbled into **clear limewater turning it milky white** [2]."
    )
    return _q(
        rng, "24", "24_comparing_acid_metal_vs_acid_carbonate_gas_products", prompt, correct, sol, 4, "structured",
        ["confusing_co2_limewater_test_with_h2_pop_test"],
        "Metals yield H2 (and NO water); carbonates yield CO2 + H2O.",
        "Metal -> H2 (pop test); Carbonate -> CO2 (milky limewater).",
        correct,
    )


def arch_25_comparing_acid_metal_vs_acid_hydroxide_products(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([("magnesium ribbon (Mg)", "magnesium hydroxide (Mg(OH)2)"), ("sodium hydroxide (NaOH)", "zinc granules (Zn)")])
    item1, item2 = pair
    prompt = (
        f"When **{item1}** vs **{item2}** react separately with dilute hydrochloric acid, one produces gas bubbles while the other remains bubble-free while releasing water.\n\n"
        "State which general product distinguishes an **acid + metal** reaction from an **acid + metal hydroxide** reaction."
    )
    correct = "Acid + metal produces hydrogen gas (H2) plus salt, whereas acid + metal hydroxide produces water (H2O) plus salt with no gas bubbles."
    distractors = [
        "Acid + metal produces carbon dioxide whereas metal hydroxide produces hydrogen gas.",
        "Both reactions produce identical hydrogen gas bubbles and pure oxygen.",
        "Acid + metal produces liquid water and no dissolved salt.",
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "**Step 1:** Metal + acid -> Salt + **$\\text{H}_2$ gas** (bubbles).\n"
        "**Step 2:** Metal hydroxide + acid -> Salt + **$\\text{H}_2\\text{O}$ water** (no gas) [2]."
    )
    return _q(
        rng, "25", "25_comparing_acid_metal_vs_acid_hydroxide_products", prompt, correct, sol, 2, "multiple_choice",
        ["claiming_acid_plus_metal_forms_water_myth"],
        "Check where oxygen atoms come from! Pure metals have no oxygen/hydroxide.",
        "Pure metal -> H2 gas; Metal hydroxide -> H2O.",
        correct, options=options,
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_hydrogen_chemical_formula_h2_diatomic_meaning": arch_01_hydrogen_chemical_formula_h2_diatomic_meaning,
    "02_hydrogen_etymology_water_generator_definition": arch_02_hydrogen_etymology_water_generator_definition,
    "03_hydrogen_periodic_table_position_and_lowest_density": arch_03_hydrogen_periodic_table_position_and_lowest_density,
    "04_hydrogen_buoyancy_soap_bubbles_and_weather_balloons": arch_04_hydrogen_buoyancy_soap_bubbles_and_weather_balloons,
    "05_density_comparison_hydrogen_air_and_carbon_dioxide": arch_05_density_comparison_hydrogen_air_and_carbon_dioxide,
    "06_burning_splint_characteristic_pop_test_for_hydrogen": arch_06_burning_splint_characteristic_pop_test_for_hydrogen,
    "07_hydrogen_plus_oxygen_combustion_balanced_equation": arch_07_hydrogen_plus_oxygen_combustion_balanced_equation,
    "08_large_hydrogen_air_explosion_vs_small_pop_sound": arch_08_large_hydrogen_air_explosion_vs_small_pop_sound,
    "09_safety_distance_flame_away_from_delivery_tube_reason": arch_09_safety_distance_flame_away_from_delivery_tube_reason,
    "10_first_gas_bubbles_displaced_air_explanation": arch_10_first_gas_bubbles_displaced_air_explanation,
    "11_test_tube_magnesium_hcl_delivery_tube_apparatus_parts": arch_11_test_tube_magnesium_hcl_delivery_tube_apparatus_parts,
    "12_inverted_test_tube_upward_delivery_gas_collection": arch_12_inverted_test_tube_upward_delivery_gas_collection,
    "13_general_word_equation_acid_plus_metal_salt_hydrogen": arch_13_general_word_equation_acid_plus_metal_salt_hydrogen,
    "14_investigative_question_and_hypothesis_mg_plus_hcl": arch_14_investigative_question_and_hypothesis_mg_plus_hcl,
    "15_cleaning_magnesium_ribbon_oxide_layer_before_reaction": arch_15_cleaning_magnesium_ribbon_oxide_layer_before_reaction,
    "16_macroscopic_observations_mg_in_hcl_effervescence_and_heat": arch_16_macroscopic_observations_mg_in_hcl_effervescence_and_heat,
    "17_exothermic_temperature_rise_during_acid_metal_reaction": arch_17_exothermic_temperature_rise_during_acid_metal_reaction,
    "18_solution_ph_increase_as_acid_is_consumed_by_metal": arch_18_solution_ph_increase_as_acid_is_consumed_by_metal,
    "19_limiting_reactant_complete_consumption_of_magnesium": arch_19_limiting_reactant_complete_consumption_of_magnesium,
    "20_magnesium_plus_hydrochloric_acid_word_equation": arch_20_magnesium_plus_hydrochloric_acid_word_equation,
    "21_magnesium_plus_hydrochloric_acid_balanced_equation": arch_21_magnesium_plus_hydrochloric_acid_balanced_equation,
    "22_deriving_mgcl2_formula_after_removing_h2_from_2hcl": arch_22_deriving_mgcl2_formula_after_removing_h2_from_2hcl,
    "23_atomic_conservation_count_mg_2hcl_equation": arch_23_atomic_conservation_count_mg_2hcl_equation,
    "24_comparing_acid_metal_vs_acid_carbonate_gas_products": arch_24_comparing_acid_metal_vs_acid_carbonate_gas_products,
    "25_comparing_acid_metal_vs_acid_hydroxide_products": arch_25_comparing_acid_metal_vs_acid_hydroxide_products,
}
