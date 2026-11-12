"""Grade 9 Natural Sciences - Reactions of Non-Metals with Oxygen: Archetypes 01 to 25.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/03. Reactions of non metals with oxygen.md.
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
    guide = f"Marking Guide ({marks} marks): Award marks per verified concept, formula, and explanation shown in the solution."
    item: Dict[str, Any] = {
        "id": f"ns9_rnmo_{code}_{rng.randint(100000, 999999)}",
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


def arch_01_nonmetal_oxidation_general_word_equation(rng: random.Random) -> Dict[str, Any]:
    pair = rng.choice([
        ("Carbon", "Carbon dioxide"),
        ("Sulfur", "Sulfur dioxide"),
        ("Phosphorus", "Diphosphorus pentoxide"),
        ("Nitrogen", "Nitrogen dioxide"),
    ])
    nm, ox = pair
    prompt = (
        "When non-metal elements combust in pure oxygen or air, they follow a general oxidation rule.\n\n"
        "1. State the **general word equation** for a non-metal reacting with oxygen [1].\n"
        f"2. Apply this rule to complete the word equation for **{nm}** burning completely in abundant oxygen [1].\n"
        "3. Explain how this general word equation compares with the metal + oxygen word equation [1]."
    )
    correct = f"Non-metal + Oxygen -> Non-metal oxide; {nm} + Oxygen -> {ox}; Same addition structure except metal is replaced by non-metal (products differ in acidity)"
    sol = (
        "**Step 1:** General word equation: **Non-metal + Oxygen $\\rightarrow$ Non-metal oxide** [1].\n\n"
        f"**Step 2:** **{nm} + Oxygen $\\rightarrow$ {ox}** [1].\n\n"
        "**Step 3:** Both share the synthesis word pattern `element + oxygen -> oxide`, but metal oxides are basic whereas non-metal oxides are generally acidic [1]."
    )
    return _q(
        rng, "01", "01_nonmetal_oxidation_general_word_equation", prompt, correct, sol, 3, "structured",
        ["nonmetal_oxidation_general_equation_error"],
        "Replace 'metal' with 'non-metal' in the synthesis oxide pattern.",
        f"{nm} + Oxygen -> {ox}.",
        correct,
    )


def arch_02_reactive_vs_inert_elements_definition(rng: random.Random) -> Dict[str, Any]:
    elem_pair = rng.choice([
        ("Oxygen (O2)", "Argon (Ar)"),
        ("Fluorine / Oxygen", "Helium (He)"),
        ("Sulfur (S)", "Neon (Ne)"),
    ])
    reactive_el, inert_el = elem_pair
    prompt = (
        f"In atmospheric air, **{reactive_el}** combines readily with metals and non-metals during combustion, whereas **{inert_el}** remains completely unreacted inside light bulbs and gas jars.\n\n"
        "Define the chemical terms **reactive** and **inert** using these elements as examples [2]."
    )
    correct = f"Reactive means readily undergoing chemical reactions with other substances ({reactive_el}); Inert means chemically unreactive / refusing to combine easily with other elements ({inert_el})."
    sol = (
        f"**Step 1:** **Reactive** describes a substance that readily breaks/forms bonds in chemical reactions (e.g., **{reactive_el}** combining vigorously during burning) [1].\n\n"
        f"**Step 2:** **Inert** describes an unreactive substance that resists chemical bonding even when heated (e.g., noble gas **{inert_el}**) [1]."
    )
    return _q(
        rng, "02", "02_reactive_vs_inert_elements_definition", prompt, correct, sol, 2, "short_answer",
        ["inert_vs_reactive_definition_confusion"],
        "Contrast an element that joins eagerly in combustion with a noble gas that refuses to react.",
        f"Reactive = readily reacts ({reactive_el}); Inert = unreactive ({inert_el}).",
        correct,
    )


def arch_03_periodic_table_nonmetal_region_location(rng: random.Random) -> Dict[str, Any]:
    nonmetals = rng.choice(["Carbon (C) and Sulfur (S)", "Phosphorus (P) and Oxygen (O)", "Nitrogen (N) and Chlorine (Cl)"])
    prompt = (
        f"Where on the Periodic Table are typical non-metals such as **{nonmetals}** located (apart from hydrogen)?\n\n"
        "State which side of the stepped dividing line they occupy and which group contains oxygen and sulfur [2]."
    )
    correct = "To the upper-right side of the stepped zig-zag line separating metals and semi-metals; Oxygen and Sulfur both belong to Group 16."
    options = [
        correct,
        "On the far bottom-left inside Group 1 alkali column exclusively.",
        "Scattered randomly inside the middle transition metal block (Groups 3–12).",
        "In Group 18 noble gases alongside helium and neon only.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Except for hydrogen at top-left, non-metals lie on the **upper-right side of the stepped line**.\n"
        "**Step 2:** Oxygen (period 2) and Sulfur (period 3) sit vertically in **Group 16** [2]."
    )
    return _q(
        rng, "03", "03_periodic_table_nonmetal_region_location", prompt, correct, sol, 2, "multiple_choice",
        ["periodic_table_nonmetal_region_error"],
        "Recall the diagonal stepped dividing line separating metals on the left from non-metals on the right.",
        "Non-metals = right of the stepped line; O & S = Group 16.",
        correct, options=options,
    )


def arch_04_carbon_combustion_word_and_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    fuel = rng.choice(["pure charcoal lump", "black graphite powder", "bituminous coal sample"])
    prompt = (
        f"A teacher heats a **{fuel}** (elemental carbon) until glowing red and lowers it into pure oxygen gas.\n\n"
        "1. Write the **word equation** for the complete combustion of carbon [1].\n"
        "2. Write the **balanced chemical equation** with state symbols [2]."
    )
    correct = "Carbon + Oxygen -> Carbon dioxide; C(s) + O2(g) -> CO2(g)"
    sol = (
        "**Step 1:** Word equation: **Carbon + Oxygen $\\rightarrow$ Carbon dioxide** [1].\n\n"
        "**Step 2:** Balanced symbol equation: **$$\\text{C}(s) + \\text{O}_2(g) \\rightarrow \\text{CO}_2(g)$$** (1 C and 2 O atoms conserved on both sides) [2]."
    )
    return _q(
        rng, "04", "04_carbon_combustion_word_and_balanced_equation", prompt, correct, sol, 3, "structured",
        ["carbon_dioxide_balancing_error"],
        "Carbon has symbol C; complete combustion adds O2 to make CO2.",
        "C(s) + O2(g) -> CO2(g) is already balanced 1 : 1 : 1.",
        correct,
    )


def arch_05_carbon_combustion_macroscopic_observations(rng: random.Random) -> Dict[str, Any]:
    temp_ctx = rng.choice(["deflagrating spoon in an oxygen gas jar", "braai charcoal bed fanned with air"])
    prompt = (
        f"Compare what is seen during the combustion of carbon in a **{temp_ctx}** versus burning magnesium ribbon.\n\n"
        "State **two distinct macroscopic observations** when charcoal burns cleanly in oxygen [2]."
    )
    correct = "Charcoal glows bright red/orange (with small yellow/orange sparks in pure O2 without blinding white light) and forms a colourless, odourless gas (CO2) rather than white solid ash."
    sol = (
        "**Step 1:** Carbon burns by **glowing bright red-orange** (producing hot embers/sparks) rather than a dazzling white UV flame [1].\n\n"
        "**Step 2:** Instead of leaving solid metal oxide ash, the reaction releases a **colourless gas ($\\text{CO}_2$)** into the jar/air [1]."
    )
    return _q(
        rng, "05", "05_carbon_combustion_macroscopic_observations", prompt, correct, sol, 2, "short_answer",
        ["carbon_combustion_white_flame_myth"],
        "Think about red-hot braai coals vs blinding white Mg flame, and solid ash vs colourless gas.",
        "Glowing red/orange embers + colourless gas product (CO2).",
        correct,
    )


def arch_06_coal_as_carbon_fossil_fuel_electricity_sa(rng: random.Random) -> Dict[str, Any]:
    station = rng.choice(["Medupi", "Kusile", "Kendal", "Matimba", "Lethabo"])
    prompt = (
        f"South African coal-fired power stations such as **{station}** burn pulverised coal rich in **carbon** to boil water into high-pressure steam.\n\n"
        "1. Classify coal scientifically as a **fossil fuel** and state whether it is renewable or non-renewable [2].\n"
        "2. Explain the core energy transformation starting from coal's chemical bonds through combustion [2]."
    )
    correct = "Fossil fuel (formed over millions of years from ancient plant matter), non-renewable; Chemical potential energy -> Thermal energy (combustion) -> Kinetic energy (steam turbines) -> Electrical energy (generators)."
    sol = (
        "**Step 1:** Coal is a carbon-rich **fossil fuel** formed over geological millions of years from compressed prehistoric vegetation, making it **non-renewable** [2].\n\n"
        "**Step 2:** Burning coal oxidises carbon exothermically: **Chemical potential energy $\\rightarrow$ Thermal energy $\\rightarrow$ Kinetic energy (spinning turbine) $\\rightarrow$ Electrical energy** [2]."
    )
    return _q(
        rng, "06", "06_coal_as_carbon_fossil_fuel_electricity_sa", prompt, correct, sol, 4, "structured",
        ["coal_renewable_misconception"],
        "How long does coal take to form underground? Trace energy from chemical bonds to electricity.",
        "Non-renewable fossil fuel; Chemical -> Heat -> Kinetic (steam/turbine) -> Electrical.",
        correct,
    )


def arch_07_nonrenewable_coal_vs_renewable_alternatives_sa(rng: random.Random) -> Dict[str, Any]:
    region_res = rng.choice([
        ("high year-round solar irradiance in the Northern Cape (Upington/De Aar)", "Solar photovoltaic (PV) or Concentrated Solar Power (CSP)"),
        ("strong coastal and escarpment winds in the Eastern and Western Cape (Jeffreys Bay / Darling)", "Wind turbine electricity generation"),
        ("high-altitude river dams and pumped-storage reservoirs in the Drakensberg", "Hydroelectric generation"),
    ])
    region, tech = region_res
    prompt = (
        f"To lower greenhouse gas and sulfur oxide emissions from coal combustion, South Africa expands clean energy harnessing **{region}**.\n\n"
        f"1. Name the **renewable energy technology** suited to this region [1].\n"
        "2. State **two environmental advantages** of shifting away from burning coal in oxygen [2]."
    )
    correct = f"{tech}; Advantages: does not deplete finite fossil fuel reserves, emits zero operational CO2 greenhouse gas, and eliminates SO2/acid-rain soot pollution."
    sol = (
        f"**Step 1:** Suitable renewable system: **{tech}** [1].\n\n"
        "**Step 2:** Shifting away from coal combustion avoids finite resource depletion, prevents greenhouse **$CO_2$** build-up driving climate change, and eliminates toxic **$SO_2$** / particulate air pollution [2]."
    )
    return _q(
        rng, "07", "07_nonrenewable_coal_vs_renewable_alternatives_sa", prompt, correct, sol, 3, "structured",
        ["renewable_energy_identification_error"],
        "Match the geographical climate feature to solar, wind, or hydro energy.",
        f"{tech} removes coal combustion emissions (CO2 + SO2).",
        correct,
    )


def arch_08_limewater_test_positive_milky_observation(rng: random.Random) -> Dict[str, Any]:
    vessel = rng.choice(["gas jar containing burned charcoal fumes", "bubbling fermentation flask", "exhaled breath tube"])
    prompt = (
        f"A learner shakes clear, colourless **limewater** inside a **{vessel}** suspected of holding carbon dioxide gas ($\\text{{CO}}_2$).\n\n"
        "What specific visual change confirms a positive test for carbon dioxide?"
    )
    correct = "The clear, colourless limewater turns cloudy or milky white."
    options = [
        correct,
        "A glowing wooden splint bursts back into bright yellow flames immediately.",
        "Blue cobalt chloride indicator strips turn bright purple within seconds.",
        "Hydrogen bubbles catch alight with an explosive squeaky pop.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Limewater is clear aqueous calcium hydroxide ($\\text{Ca(OH)}_2$).\n"
        "**Step 2:** When $CO_2$ bubbles through, fine insoluble white calcium carbonate crystals precipitate, making the clear liquid turn **milky / cloudy white** [2]."
    )
    return _q(
        rng, "08", "08_limewater_test_positive_milky_observation", prompt, correct, sol, 2, "multiple_choice",
        ["gas_test_co2_vs_o2_h2_confusion"],
        "Remember: Oxygen relights a glowing splint; Hydrogen pops; Carbon dioxide tests with limewater.",
        "CO2 + clear limewater -> milky/cloudy white precipitate.",
        correct, options=options,
    )


def arch_09_limewater_precipitate_chemical_equation_caco3(rng: random.Random) -> Dict[str, Any]:
    focus = rng.choice(["chemical name and formula of limewater", "precipitate responsible for the milkiness"])
    prompt = (
        f"During the carbon dioxide test (focusing on **{focus}**), carbon dioxide reacts with limewater:\n"
        "$$\\text{CO}_2(g) + \\text{Ca(OH)}_2(aq) \\rightarrow \\text{Product}_1(s) + \\text{H}_2\\text{O}(l)$$\n\n"
        "1. State the proper chemical name of **limewater ($\\text{Ca(OH)}_2$)** [1].\n"
        "2. Name and write the chemical formula of the insoluble white precipitate ($\\text{Product}_1$) [2]."
    )
    correct = "Limewater = aqueous calcium hydroxide; White precipitate = Calcium carbonate (CaCO3)"
    sol = (
        "**Step 1:** Clear limewater is an aqueous solution of **calcium hydroxide** ($\\text{Ca(OH)}_2$)—not citrus fruit juice! [1]\n\n"
        "**Step 2:** The cloudy white precipitate suspended in the liquid is insoluble **calcium carbonate ($\\text{CaCO}_3$)** [2]."
    )
    return _q(
        rng, "09", "09_limewater_precipitate_chemical_equation_caco3", prompt, correct, sol, 3, "structured",
        ["limewater_confused_with_lemon_juice_myth"],
        "Ca(OH)2 is calcium hydroxide. What carbonate forms when Ca combines with CO2?",
        "Calcium hydroxide + CO2 -> Calcium carbonate (CaCO3) + water.",
        correct,
    )


def arch_10_particle_diagram_carbon_dioxide_combustion(rng: random.Random) -> Dict[str, Any]:
    c_col = rng.choice(["#334155", "#1e293b", "#475569"])
    o_col = rng.choice(["#dc2626", "#ef4444"])
    svg = (
        f'<svg viewBox="0 0 380 148" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="380" height="148" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="190" y="18" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Submicroscopic Model: Combustion of Carbon</text>'
        f'<rect x="16" y="30" width="146" height="90" rx="6" fill="#fff" stroke="#94a3b8"/>'
        f'<text x="89" y="43" font-size="8" font-weight="bold" fill="#334155" text-anchor="middle">Reactants</text>'
        f'<circle cx="48" cy="82" r="14" fill="{c_col}"/><text x="48" y="86" font-size="9" fill="#fff" text-anchor="middle">C</text>'
        f'<circle cx="108" cy="82" r="11" fill="{o_col}"/><text x="108" y="86" font-size="8" fill="#fff" text-anchor="middle">O</text>'
        f'<circle cx="130" cy="82" r="11" fill="{o_col}"/><text x="130" y="86" font-size="8" fill="#fff" text-anchor="middle">O</text>'
        f'<path d="M 171,75 L 204,75 M 199,70 L 206,75 L 199,80" fill="none" stroke="#0284c7" stroke-width="2.5"/>'
        f'<rect x="214" y="30" width="150" height="90" rx="6" fill="#fff" stroke="#94a3b8"/>'
        f'<text x="289" y="43" font-size="8" font-weight="bold" fill="#334155" text-anchor="middle">Product Molecule</text>'
        f'<circle cx="267" cy="82" r="11" fill="{o_col}"/><text x="267" y="86" font-size="8" fill="#fff" text-anchor="middle">O</text>'
        f'<circle cx="289" cy="82" r="14" fill="{c_col}"/><text x="289" y="86" font-size="9" fill="#fff" text-anchor="middle">C</text>'
        f'<circle cx="311" cy="82" r="11" fill="{o_col}"/><text x="311" y="86" font-size="8" fill="#fff" text-anchor="middle">O</text>'
        f'<text x="190" y="136" font-size="8" fill="#475569" text-anchor="middle">Key: Dark grey = C atom; Red = O atom</text>'
        f'</svg>'
    )
    prompt = (
        "Inspect the particle model diagram showing carbon burning in oxygen.\n\n"
        "1. Translate the reactants and product directly into a **balanced chemical equation** [2].\n"
        "2. Describe how atom arrangement changed between Reactants and Product Molecule [1]."
    )
    correct = "C + O2 -> CO2; The bond holding the two red O atoms split apart, and each O atom bonded on opposite sides of the central grey C atom."
    sol = (
        "**Step 1:** Left box holds 1 isolated C atom + 1 diatomic $O_2$ molecule; Right box holds 1 linear triatomic $CO_2$ molecule -> **$$\\text{C} + \\text{O}_2 \\rightarrow \\text{CO}_2$$** [2].\n\n"
        "**Step 2:** The $O=O$ bond broke so two separate oxygen atoms each formed new bonds to carbon [1]."
    )
    return _q(
        rng, "10", "10_particle_diagram_carbon_dioxide_combustion", prompt, correct, sol, 3, "structured",
        ["particle_model_co2_bond_rearrangement"],
        "Count grey C spheres and bonded red O spheres in each box.",
        "1 C + 1 O2 -> 1 CO2 molecule (O-C-O).",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_11_sulfur_element_physical_appearance_and_group16(rng: random.Random) -> Dict[str, Any]:
    state_prop = rng.choice(["pure yellow crystalline powder", "brittle yellow solid lumps"])
    prompt = (
        f"Elemental sulfur appears as **{state_prop}** at room temperature and sits directly beneath oxygen on the Periodic Table.\n\n"
        "1. State sulfur's chemical symbol and Periodic Table Group number [2].\n"
        "2. Predict whether solid sulfur conducts electricity well like copper, and justify why [1]."
    )
    correct = "Symbol: S, Group 16; Sulfur does NOT conduct electricity because it is a non-metal electrical insulator."
    sol = (
        "**Step 1:** Sulfur has symbol **S** and sits directly below oxygen in **Group 16** [2].\n\n"
        "**Step 2:** As a brittle non-metal solid, sulfur lacks free-moving metallic electrons and acts as an **electrical insulator** [1]."
    )
    return _q(
        rng, "11", "11_sulfur_element_physical_appearance_and_group16", prompt, correct, sol, 3, "structured",
        ["sulfur_group_and_properties_error"],
        "Check Group 16 where oxygen sits; remember non-metal properties.",
        "Sulfur = S, Group 16, brittle yellow non-metal insulator.",
        correct,
    )


def arch_12_sulfur_combustion_vivid_blue_flame_observation(rng: random.Random) -> Dict[str, Any]:
    flame_col = rng.choice(["#2563eb", "#1d4ed8"])
    svg = (
        f'<svg viewBox="0 0 360 155" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="360" height="155" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="180" y="18" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Sulfur Burning Inside an Oxygen Gas Jar</text>'
        f'<rect x="135" y="34" width="90" height="104" rx="4" fill="#eff6ff" stroke="#334155" stroke-width="2"/>'
        f'<line x1="180" y1="22" x2="180" y2="104" stroke="#475569" stroke-width="2.5"/>'
        f'<path d="M 168,104 L 192,104 L 188,114 L 172,114 Z" fill="#64748b"/>'
        f'<ellipse cx="180" cy="102" rx="9" ry="4" fill="#facc15"/>'
        f'<path d="M 171,100 Q 180,68 189,100 Z" fill="{flame_col}" opacity="0.85"/>'
        f'<text x="238" y="88" font-size="8" fill="{flame_col}" font-weight="bold">Vivid flame</text>'
        f'<text x="238" y="106" font-size="8" fill="#334155">O2 gas jar</text>'
        f'<text x="64" y="102" font-size="8" fill="#334155" text-anchor="middle">Deflagrating spoon</text>'
        f'<line x1="108" y1="100" x2="168" y2="108" stroke="#64748b" stroke-dasharray="2,2"/>'
        f'</svg>'
    )
    prompt = (
        "Inspect the apparatus diagram illustrating a teacher heating yellow sulfur inside a fume cupboard oxygen jar.\n\n"
        "1. State the exact **colour of the flame** produced when molten sulfur burns in oxygen [1].\n"
        "2. State two physical characteristics of the gas formed inside the jar [2]."
    )
    correct = "Vivid bright blue flame; Gas formed (SO2) is colourless with a sharp, pungent, choking/suffocating odour."
    sol = (
        "**Step 1:** Molten sulfur ignites with a characteristic **bright/vivid blue flame** [1].\n\n"
        "**Step 2:** The product ($\\text{SO}_2$) is a **colourless** gas possessing a **sharp, pungent, choking odour** [2]."
    )
    return _q(
        rng, "12", "12_sulfur_combustion_vivid_blue_flame_observation", prompt, correct, sol, 3, "structured",
        ["sulfur_flame_color_confusion"],
        "Unlike magnesium's white glare or orange charcoal glow, sulfur's flame has a distinct cool colour.",
        "Blue flame + colourless choking SO2 gas.",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_13_sulfur_dioxide_word_and_balanced_equation(rng: random.Random) -> Dict[str, Any]:
    jar_ctx = rng.choice(["fume-cupboard oxygen jar", "copper smelter furnace", "sulfuric acid plant"])
    prompt = (
        f"Sulfur reacts with oxygen gas inside a **{jar_ctx}** to form sulfur dioxide.\n\n"
        "1. Write the **word equation** [1].\n"
        "2. Write the **chemical formula** for sulfur dioxide and explain why it ends with subscript `2` [2].\n"
        "3. Write the complete **balanced chemical equation** [1]."
    )
    correct = "Sulfur + Oxygen -> Sulfur dioxide; Formula SO2 ('di-' means two oxygen atoms bonded per sulfur atom); S + O2 -> SO2"
    sol = (
        "**Step 1:** Word equation: **Sulfur + Oxygen $\\rightarrow$ Sulfur dioxide** [1].\n\n"
        "**Step 2:** Formula is **$\\text{SO}_2$** because the prefix *di-* specifies **2 oxygen atoms** bonded to 1 sulfur atom [2].\n\n"
        "**Step 3:** Balanced chemical equation: **$$\\text{S}(s) + \\text{O}_2(g) \\rightarrow \\text{SO}_2(g)$$** [1]."
    )
    return _q(
        rng, "13", "13_sulfur_dioxide_word_and_balanced_equation", prompt, correct, sol, 4, "structured",
        ["sulfur_dioxide_formula_error"],
        "Pay attention to the Greek prefix 'di-' in dioxide.",
        "S + O2 -> SO2 (1 S atom + 2 O atoms on each side).",
        correct,
    )


def arch_14_meaning_of_prefix_di_in_dioxide_nomenclature(rng: random.Random) -> Dict[str, Any]:
    sample_q = rng.choice([
        ("carbon monoxide (CO) vs carbon dioxide (CO2) vs sulfur trioxide (SO3)", "mono- = 1, di- = 2, tri- = 3 oxygen atoms"),
        ("dinitrogen tetroxide (N2O4) vs nitrogen dioxide (NO2) vs diphosphorus pentoxide (P2O5)", "di- = 2, tetra- = 4, penta- = 5 atoms"),
    ])
    compounds, mapping = sample_q
    prompt = (
        f"Systematic names for covalent non-metal oxides use number prefixes as in **{compounds}**.\n\n"
        "Decode what number each prefix specifies (**mono-, di-, tri-, penta-**) and write the formula of **carbon dioxide** vs **carbon monoxide** [3]."
    )
    correct = f"mono- = 1, di- = 2, tri- = 3, penta- = 5; Carbon dioxide = CO2 (2 O atoms), Carbon monoxide = CO (1 O atom) [{mapping}]."
    sol = (
        f"**Step 1:** Prefixes: **mono- = 1, di- = 2, tri- = 3, penta- = 5** ({mapping}) [2].\n\n"
        "**Step 2:** Therefore carbon **di**oxide is **$\\text{CO}_2$** while carbon **mon**oxide is **$\\text{CO}$** [1]."
    )
    return _q(
        rng, "14", "14_meaning_of_prefix_di_in_dioxide_nomenclature", prompt, correct, sol, 3, "structured",
        ["covalent_prefix_decoding_error"],
        "Remember: 'monorail' (1), 'dialogue/dioxide' (2), 'triangle' (3), 'pentagon' (5).",
        "mono=1, di=2, tri=3, penta=5 -> CO vs CO2.",
        correct,
    )


def arch_15_sulfur_dioxide_toxicity_and_fume_hood_protocol(rng: random.Random) -> Dict[str, Any]:
    rule_ctx = rng.choice(["Grade 9 class", "school physical science lab"])
    prompt = (
        f"In a **{rule_ctx}**, curriculum safety rules explicitly warn teachers NOT to burn open piles of sulfur on a classroom desk without extraction.\n\n"
        "Explain the specific chemical hazard of sulfur dioxide gas ($\\text{SO}_2$) and state the required ventilation control [2]."
    )
    correct = "Sulfur dioxide is an acutely toxic, suffocating gas with a pungent smell that irritates eyes, throats, and lungs; It must only be demonstrated inside a working fume cupboard or outdoors upwind."
    sol = (
        "**Step 1:** Burning sulfur produces **$SO_2$ gas**, a toxic respiratory irritant that rapidly dissolves in moist airway linings to form corrosive sulfurous acid [1].\n\n"
        "**Step 2:** Teachers must strictly enclose combustion inside a **fume cupboard (extractor hood)** with sealed jars to prevent inhalation by learners [1]."
    )
    return _q(
        rng, "15", "15_sulfur_dioxide_toxicity_and_fume_hood_protocol", prompt, correct, sol, 2, "short_answer",
        ["fume_hood_safety_omission"],
        "Why is SO2 gas dangerous to learners standing around a classroom table?",
        "Poisonous choking gas -> requires fume cupboard extraction.",
        correct,
    )


def arch_16_sulfur_dioxide_asthma_bronchospasm_respiratory_hazard(rng: random.Random) -> Dict[str, Any]:
    patient = rng.choice(["learner with bronchial asthma", "elderly worker with chronic bronchitis"])
    prompt = (
        f"A **{patient}** is particularly vulnerable if exposed even briefly to sulfur dioxide fumes ($\\text{{SO}}_2$).\n\n"
        "Explain biologically what happens inside their airways when $SO_2$ is inhaled [2]."
    )
    correct = "SO2 dissolves in respiratory mucus to form acidic sulfurous acid, causing intense airway inflammation, coughing spasms, and dangerous bronchial constriction (asthma attack)."
    sol = (
        "**Step 1:** $SO_2$ reacts rapidly with water in moist throat/bronchial tissues to form **sulfurous acid ($H_2SO_3$)** [1].\n\n"
        "**Step 2:** Acid irritation triggers sudden **bronchospasm (tightening of air passages), mucus build-up, wheezing, and acute asthma attacks** [1]."
    )
    return _q(
        rng, "16", "16_sulfur_dioxide_asthma_bronchospasm_respiratory_hazard", prompt, correct, sol, 2, "short_answer",
        ["so2_asthma_mechanism_error"],
        "Remember: SO2 dissolves in moist mucus linings like a non-metal oxide in water.",
        "Forms acid on lung walls -> airway swelling & severe bronchospasm.",
        correct,
    )


def arch_17_sulfur_mining_occupational_respiratory_risk(rng: random.Random) -> Dict[str, Any]:
    site = rng.choice(["volcanic crater sulfur deposit", "underground sulfide smelting shaft"])
    prompt = (
        f"Miners working near a **{site}** constantly face toxic sulfur dioxide vapours unless equipped with gas masks and forced ventilation.\n\n"
        "1. State what sensory warning sign $SO_2$ gives at low concentrations [1].\n"
        "2. Name one personal protective measure required for miners working in $SO_2$ zones [1]."
    )
    correct = "Sharp, choking burnt-match odour and stinging eyes/throat; Positive-pressure air respirators / chemical acid-gas masks and continuous gas monitoring."
    sol = (
        "**Step 1:** Even in small quantities, $SO_2$ produces a piercing, **choking burnt-match smell** and stinging irritation in eyes and nostrils [1].\n\n"
        "**Step 2:** Workers require certified **acid-gas cartridge respirators / breathing apparatus** and active air monitoring [1]."
    )
    return _q(
        rng, "17", "17_sulfur_mining_occupational_respiratory_risk", prompt, correct, sol, 2, "short_answer",
        ["sulfur_dioxide_odorless_myth"],
        "Is SO2 odourless like CO2, or does it have a noticeable smell?",
        "Sharp pungent burnt-match smell; respirator / gas detector needed.",
        correct,
    )


def arch_18_sulfur_dioxide_food_preservative_dried_fruit_sa(rng: random.Random) -> Dict[str, Any]:
    snack = rng.choice(["sun-dried Wellington apricots", "dried peaches", "traditional guava rolls", "dried mango strips"])
    prompt = (
        f"Food labels on South African packets of **{snack}** frequently list **\"Preservative: Sulfur dioxide ($\\text{{SO}}_2$)\"**.\n\n"
        "How can a gas classified as toxic in high concentrations safely preserve dried fruit for human consumption?"
    )
    correct = "At carefully controlled trace levels, SO2 is potent enough to kill spoilage bacteria and moulds and prevent enzymatic browning, while remaining too dilute to harm large organisms like humans."
    options = [
        correct,
        "SO2 reacts with fruit sugar to turn the fruit into poisonous sulfuric acid crystals.",
        "Sulfur dioxide completely freezes moisture inside the fruit to -40 °C permanently.",
        "Large amounts of liquefied pure SO2 are poured inside each packet to sterilise it.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Toxicity depends critically on **dosage relative to body mass**.\n"
        f"**Step 2:** Microorganisms (bacteria/moulds) die at trace $SO_2$ concentrations that keep **{snack}** bright and shelf-stable without harming non-asthmatic human consumers [2]."
    )
    return _q(
        rng, "18", "18_sulfur_dioxide_food_preservative_dried_fruit_sa", prompt, correct, sol, 2, "multiple_choice",
        ["food_preservative_dosage_misconception"],
        "Compare the body size and lethal dose of microscopic bacteria vs humans.",
        "Tiny controlled doses inhibit bacteria/fungi without harming humans.",
        correct, options=options,
    )


def arch_19_sulfur_dioxide_south_african_wine_preservation(rng: random.Random) -> Dict[str, Any]:
    region = rng.choice(["Stellenbosch", "Paarl", "Franschhoek", "Robertson", "Swartland"])
    prompt = (
        f"Vintners across **{region}** in the Western Cape add trace amounts of sulfur dioxide (\"sulfites\") during winemaking and bottling.\n\n"
        "State **two distinct reasons** winemakers add strictly measured amounts of $SO_2$, and explain why wine bottles still require a **\"Contains Sulfites\"** warning [3]."
    )
    correct = "1. Kills unwanted wild bacteria/yeasts (antimicrobial); 2. Acts as an antioxidant stopping wine turning into vinegar; Labelled because trace sulfites can trigger severe allergic/asthmatic reactions in sensitive people."
    sol = (
        "**Step 1:** Trace $SO_2$ suppresses **spoilage bacteria and wild yeasts**, and protects flavour by acting as an **antioxidant** so alcohol does not sour [2].\n\n"
        "**Step 2:** Allergen laws require **\"Contains Sulfites\"** labels because even tiny residues can trigger asthma symptoms in sensitive consumers [1]."
    )
    return _q(
        rng, "19", "19_sulfur_dioxide_south_african_wine_preservation", prompt, correct, sol, 3, "structured",
        ["wine_preservative_so2_rationale"],
        "Think of spoilage microbes, unwanted oxidation to vinegar, and human asthma sensitivity.",
        "Kills spoilage microbes + prevents oxidation; allergy warning for asthmatics.",
        correct,
    )


def arch_20_hydrogen_combustion_dihydrogen_monoxide_equation(rng: random.Random) -> Dict[str, Any]:
    source = rng.choice(["green hydrogen fuel-cell car", "popping hydrogen gas test tube", "rocket propulsion engine"])
    prompt = (
        f"In a **{source}**, pure hydrogen gas reacts cleanly with oxygen gas.\n\n"
        "1. Write the **balanced chemical equation** for hydrogen burning in oxygen [2].\n"
        "2. State both the **common name** and **systematic non-metal oxide name** of the product [2].\n"
        "3. State whether water turns blue litmus red, and justify why hydrogen qualifies as a non-metal oxide [1]."
    )
    correct = "2H2 + O2 -> 2H2O; Common name: Water, Systematic name: Dihydrogen monoxide; Water is neutral (pH 7, litmus unchanged), yet is a non-metal oxide because hydrogen (H) is a non-metal."
    sol = (
        "**Step 1:** Balanced equation: **$$2\\text{H}_2(g) + \\text{O}_2(g) \\rightarrow 2\\text{H}_2\\text{O}(l)$$** [2].\n\n"
        "**Step 2:** Common name: **Water**; Systematic chemical name: **Dihydrogen monoxide** (2 H atoms + 1 O atom) [2].\n\n"
        "**Step 3:** Hydrogen is a non-metal chemically combined with oxygen, making water an unusual **neutral non-metal oxide (pH 7)** rather than acidic or a dioxide [1]."
    )
    return _q(
        rng, "20", "20_hydrogen_combustion_dihydrogen_monoxide_equation", prompt, correct, sol, 5, "structured",
        ["hydrogen_not_nonmetal_myth", "all_nonmetal_oxides_acidic_overgeneralization"],
        "Check hydrogen's chemical category and count oxygen atoms in H2O.",
        "2H2 + O2 -> 2H2O (dihydrogen monoxide / water, pH 7 neutral non-metal oxide).",
        correct,
    )


def arch_21_phosphorus_combustion_diphosphorus_pentoxide(rng: random.Random) -> Dict[str, Any]:
    form_style = rng.choice(["white/red phosphorus", "match-box striking compound phosphorus"])
    prompt = (
        f"When **{form_style}** burns rapidly in excess oxygen, dense white smoke clouds form with a **2 : 5** atom ratio of phosphorus to oxygen.\n\n"
        "1. Decode the systematic name **diphosphorus pentoxide** into its formula [1].\n"
        "2. Write the **balanced chemical equation** starting from atomic phosphorus ($\\text{P}$) + $\\text{O}_2$ [2]."
    )
    correct = "Formula: P2O5 (empirical/textbook diphosphorus pentoxide, molecular P4O10); Balanced equation: 4P + 5O2 -> 2P2O5"
    sol = (
        "**Step 1:** *Di-* = 2 P atoms, *pent(a)-* = 5 O atoms -> formula **$\\text{P}_2\\text{O}_5$** (molecular dimer $P_4O_{10}$) [1].\n\n"
        "**Step 2:** LCM of 2 ($O_2$) and 5 ($O_5$) is 10 O atoms: **$$4\\text{P} + 5\\text{O}_2 \\rightarrow 2\\text{P}_2\\text{O}_5$$** [2]."
    )
    return _q(
        rng, "21", "21_phosphorus_combustion_diphosphorus_pentoxide", prompt, correct, sol, 3, "structured",
        ["phosphorus_oxide_formula_balancing_error"],
        "'di-' = 2 phosphorus, 'pent-' = 5 oxygen -> find lowest common multiple of O2 and O5.",
        "4P + 5O2 -> 2P2O5.",
        correct,
    )


def arch_22_carbon_monoxide_incomplete_combustion_hazard(rng: random.Random) -> Dict[str, Any]:
    appliance = rng.choice(["closed-room imbawula coal brazier", "faulty unflued gas heater", "idling bakkie engine in a closed garage"])
    prompt = (
        f"Burning carbon-based fuel inside an **{appliance}** restricts the oxygen supply, causing **incomplete combustion**.\n\n"
        "1. Write the **balanced chemical equation** forming carbon monoxide ($\\text{CO}$) instead of $\\text{CO}_2$ [2].\n"
        "2. Why is carbon monoxide gas far more acutely deadly indoors than carbon dioxide? [1]"
    )
    correct = "2C + O2 -> 2CO; CO is a colourless, odourless poison that binds tightly to blood haemoglobin, blocking oxygen delivery to brain and heart cells."
    sol = (
        "**Step 1:** Balanced incomplete combustion: **$$2\\text{C} + \\text{O}_2 \\rightarrow 2\\text{CO}$$** [2].\n\n"
        "**Step 2:** Carbon monoxide is **odourless and invisible**, locking onto red blood cell haemoglobin ~200× stronger than oxygen and starving organs of oxygen silently [1]."
    )
    return _q(
        rng, "22", "22_carbon_monoxide_incomplete_combustion_hazard", prompt, correct, sol, 3, "structured",
        ["co_vs_co2_incomplete_combustion_confusion"],
        "Mono = 1 oxygen atom per carbon when air supply is scarce.",
        "2C + O2 -> 2CO; CO blocks oxygen transport on haemoglobin silently.",
        correct,
    )


def arch_23_nitrogen_monoxide_and_nitrogen_dioxide_exhaust_oxides(rng: random.Random) -> Dict[str, Any]:
    temp_src = rng.choice(["high-temperature petrol/diesel engine cylinders", "intense thunderstorm lightning bolts"])
    prompt = (
        f"Under normal room air, nitrogen ($\\text{{N}}_2$) and oxygen ($\\text{{O}}_2$) stay unmixed, yet inside **{temp_src}** they react.\n\n"
        "1. Name **two nitrogen oxides** formed sequentially in engine exhaust and atmosphere [2].\n"
        "2. State the visible colour of toxic **$NO_2$** urban smog plumes [1]."
    )
    correct = "Nitrogen monoxide (NO) and Nitrogen dioxide (NO2); Reddish-brown pungent gas."
    sol = (
        f"**Step 1:** Extreme energy in {temp_src} drives nitrogen oxidation forming **nitrogen monoxide ($\\text{{NO}}$)**, which quickly oxidises further in air to **nitrogen dioxide ($\\text{{NO}}_2$)** [2].\n\n"
        "**Step 2:** **$\\text{NO}_2$** is a toxic **reddish-brown** gas causing photochemical smog and acid rain [1]."
    )
    return _q(
        rng, "23", "23_nitrogen_monoxide_and_nitrogen_dioxide_exhaust_oxides", prompt, correct, sol, 3, "structured",
        ["nitrogen_oxides_smog_confusion"],
        "Think of NO and NO2; one turns city air brown-haze during rush hour.",
        "NO (nitrogen monoxide) + NO2 (reddish-brown nitrogen dioxide).",
        correct,
    )


def arch_24_dioxide_misconception_remediation_varied_ratios(rng: random.Random) -> Dict[str, Any]:
    claim_pair = rng.choice([
        ("dihydrogen monoxide (H2O) and diphosphorus pentoxide (P2O5)", "2:1 and 2:5"),
        ("carbon monoxide (CO) and sulfur trioxide (SO3)", "1:1 and 1:3"),
    ])
    ex_str, ratio_str = claim_pair
    prompt = (
        "After studying $C + O_2 \\rightarrow CO_2$ and $S + O_2 \\rightarrow SO_2$, a Grade 9 learner claims:\n"
        "*\"All non-metals react with oxygen strictly to form non-metal dioxides with two oxygens per non-metal atom.\"*\n\n"
        f"Refute this misconception using **{ex_str}** ({ratio_str}) as evidence [2]."
    )
    correct = f"False claim: Non-metal bonding ratios vary widely with valency and oxygen supply. {ex_str} prove non-metal oxides can carry 1, 3, or 5 oxygens (ratios {ratio_str}) instead of only dioxides."
    sol = (
        "**Step 1:** The learner's claim is **incorrect**—$CO_2$ and $SO_2$ happen to be dioxides, not a universal rule [1].\n\n"
        f"**Step 2:** Counterexamples like **{ex_str}** (element-to-oxygen ratios **{ratio_str}**) demonstrate monoxides, trioxides, and pentoxides also form [1]."
    )
    return _q(
        rng, "24", "24_dioxide_misconception_remediation_varied_ratios", prompt, correct, sol, 2, "short_answer",
        ["all_nonmetal_oxides_are_dioxides_myth"],
        "Remember water (H2O) and phosphorus pentoxide (P2O5) from Section 4.4.",
        f"Cite {ex_str} with ratios {ratio_str} to prove dioxides are only one subgroup.",
        correct,
    )


def arch_25_particle_diagram_sulfur_and_hydrogen_combustion_comparison(rng: random.Random) -> Dict[str, Any]:
    s_col = rng.choice(["#eab308", "#facc15"])
    o_col = rng.choice(["#dc2626", "#ef4444"])
    h_col = rng.choice(["#cbd5e1", "#e2e8f0"])
    svg = (
        f'<svg viewBox="0 0 380 155" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="380" height="155" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="190" y="18" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Non-Metal Oxide Particle Comparison</text>'
        # Row 1: SO2
        f'<rect x="16" y="30" width="166" height="106" rx="6" fill="#fff" stroke="#94a3b8"/>'
        f'<text x="99" y="45" font-size="8.5" font-weight="bold" fill="#334155" text-anchor="middle">Molecule X (Bent 1:2)</text>'
        f'<circle cx="99" cy="84" r="14" fill="{s_col}" stroke="#713f12"/><text x="99" y="88" font-size="9" fill="#0f172a" text-anchor="middle">S</text>'
        f'<circle cx="77" cy="100" r="10" fill="{o_col}"/><text x="77" y="103" font-size="7.5" fill="#fff" text-anchor="middle">O</text>'
        f'<circle cx="121" cy="100" r="10" fill="{o_col}"/><text x="121" y="103" font-size="7.5" fill="#fff" text-anchor="middle">O</text>'
        f'<text x="99" y="128" font-size="7.5" fill="#475569" text-anchor="middle">Yellow = S; Red = O</text>'
        # Row 2: H2O
        f'<rect x="198" y="30" width="166" height="106" rx="6" fill="#fff" stroke="#94a3b8"/>'
        f'<text x="281" y="45" font-size="8.5" font-weight="bold" fill="#334155" text-anchor="middle">Molecule Y (Bent 2:1)</text>'
        f'<circle cx="281" cy="84" r="11" fill="{o_col}"/><text x="281" y="88" font-size="8" fill="#fff" text-anchor="middle">O</text>'
        f'<circle cx="263" cy="100" r="8" fill="{h_col}" stroke="#475569"/><text x="263" y="103" font-size="7" fill="#0f172a" text-anchor="middle">H</text>'
        f'<circle cx="299" cy="100" r="8" fill="{h_col}" stroke="#475569"/><text x="299" y="103" font-size="7" fill="#0f172a" text-anchor="middle">H</text>'
        f'<text x="281" y="128" font-size="7.5" fill="#475569" text-anchor="middle">Grey = H; Red = O</text>'
        f'</svg>'
    )
    prompt = (
        "Inspect the particle diagram showing Molecule X and Molecule Y.\n\n"
        "1. Write the **chemical formula** and **systematic name** for both Molecule X and Molecule Y [2].\n"
        "2. Explain which molecule represents a **dioxide** and which is a **monoxide** [2]."
    )
    correct = "Molecule X = SO2 (Sulfur dioxide, a dioxide with 2 O atoms); Molecule Y = H2O (Dihydrogen monoxide / water, a monoxide with 1 O atom)."
    sol = (
        "**Step 1:** Molecule X has 1 S + 2 O -> **$\\text{SO}_2$ (Sulfur dioxide)**; Molecule Y has 2 H + 1 O -> **$\\text{H}_2\\text{O}$ (Dihydrogen monoxide / water)** [2].\n\n"
        "**Step 2:** Molecule X contains **2 oxygen atoms** (dioxide), whereas Molecule Y contains **1 oxygen atom** (monoxide) [2]."
    )
    return _q(
        rng, "25", "25_particle_diagram_sulfur_and_hydrogen_combustion_comparison", prompt, correct, sol, 4, "structured",
        ["so2_vs_h2o_particle_decoding_error"],
        "Count the red oxygen spheres in Molecule X vs Molecule Y carefully.",
        "X = SO2 (2 red O -> dioxide); Y = H2O (1 red O -> monoxide).",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


BUILDERS_01_25: Dict[str, Any] = {
    "01_nonmetal_oxidation_general_word_equation": arch_01_nonmetal_oxidation_general_word_equation,
    "02_reactive_vs_inert_elements_definition": arch_02_reactive_vs_inert_elements_definition,
    "03_periodic_table_nonmetal_region_location": arch_03_periodic_table_nonmetal_region_location,
    "04_carbon_combustion_word_and_balanced_equation": arch_04_carbon_combustion_word_and_balanced_equation,
    "05_carbon_combustion_macroscopic_observations": arch_05_carbon_combustion_macroscopic_observations,
    "06_coal_as_carbon_fossil_fuel_electricity_sa": arch_06_coal_as_carbon_fossil_fuel_electricity_sa,
    "07_nonrenewable_coal_vs_renewable_alternatives_sa": arch_07_nonrenewable_coal_vs_renewable_alternatives_sa,
    "08_limewater_test_positive_milky_observation": arch_08_limewater_test_positive_milky_observation,
    "09_limewater_precipitate_chemical_equation_caco3": arch_09_limewater_precipitate_chemical_equation_caco3,
    "10_particle_diagram_carbon_dioxide_combustion": arch_10_particle_diagram_carbon_dioxide_combustion,
    "11_sulfur_element_physical_appearance_and_group16": arch_11_sulfur_element_physical_appearance_and_group16,
    "12_sulfur_combustion_vivid_blue_flame_observation": arch_12_sulfur_combustion_vivid_blue_flame_observation,
    "13_sulfur_dioxide_word_and_balanced_equation": arch_13_sulfur_dioxide_word_and_balanced_equation,
    "14_meaning_of_prefix_di_in_dioxide_nomenclature": arch_14_meaning_of_prefix_di_in_dioxide_nomenclature,
    "15_sulfur_dioxide_toxicity_and_fume_hood_protocol": arch_15_sulfur_dioxide_toxicity_and_fume_hood_protocol,
    "16_sulfur_dioxide_asthma_bronchospasm_respiratory_hazard": arch_16_sulfur_dioxide_asthma_bronchospasm_respiratory_hazard,
    "17_sulfur_mining_occupational_respiratory_risk": arch_17_sulfur_mining_occupational_respiratory_risk,
    "18_sulfur_dioxide_food_preservative_dried_fruit_sa": arch_18_sulfur_dioxide_food_preservative_dried_fruit_sa,
    "19_sulfur_dioxide_south_african_wine_preservation": arch_19_sulfur_dioxide_south_african_wine_preservation,
    "20_hydrogen_combustion_dihydrogen_monoxide_equation": arch_20_hydrogen_combustion_dihydrogen_monoxide_equation,
    "21_phosphorus_combustion_diphosphorus_pentoxide": arch_21_phosphorus_combustion_diphosphorus_pentoxide,
    "22_carbon_monoxide_incomplete_combustion_hazard": arch_22_carbon_monoxide_incomplete_combustion_hazard,
    "23_nitrogen_monoxide_and_nitrogen_dioxide_exhaust_oxides": arch_23_nitrogen_monoxide_and_nitrogen_dioxide_exhaust_oxides,
    "24_dioxide_misconception_remediation_varied_ratios": arch_24_dioxide_misconception_remediation_varied_ratios,
    "25_particle_diagram_sulfur_and_hydrogen_combustion_comparison": arch_25_particle_diagram_sulfur_and_hydrogen_combustion_comparison,
}
