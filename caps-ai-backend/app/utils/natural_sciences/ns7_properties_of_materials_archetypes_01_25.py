"""
Grade 7 Natural Sciences - Term 2: Properties of Materials (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/01. Properties of materials.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Mechanical & Physical Properties (01 - 09)
# ==============================================================================

def arch_01_malleability_definition_and_examples(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("aluminium", "pressed into aluminium foil and cold-drink cans"),
        ("iron", "hammered into corrugated sheets for roofing panels"),
        ("gold", "beaten into ultra-thin decorative gold leaf sheets"),
        ("copper", "hammered into artisanal cooking bowls and decorative plates"),
    ]
    metal, application = rng.choice(metals)

    prompt = (
        f"A sheet metal worker shapes a piece of {metal} into a flat sheet without it cracking or shattering.\n\n"
        f"1. Identify the physical property of matter that allows {metal} to be {application}.\n"
        f"2. Explain what this property means in terms of shaping a solid material."
    )
    sol = (
        f"**Step 1:** The physical property demonstrated is **malleability** [1 Mark: Knowledge].\n\n"
        f"**Step 2:** Malleability is the ability of a material to be hammered, rolled, or pressed into thin flat sheets without breaking, cracking, or shattering [1 Mark: Explanation]."
    )
    return {
        "id": f"ns7_prop_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Malleability; ability to be hammered or pressed into thin sheets without shattering",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "01_malleability_definition_and_examples",
        "misconception_tags": ["malleability_vs_ductility"],
        "hints": {
            "tier_1": "Think of what property allows metals to form flat sheets or foil.",
            "tier_2": "The word starts with 'm'. It is different from stretching into wires.",
            "tier_3": "The property is malleability."
        }
    }


def arch_02_ductility_definition_and_wires(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("copper", "drawn into electrical wiring for domestic house circuits"),
        ("aluminium", "stretched into overhead transmission power cables"),
        ("gold", "pulled into fine delicate threads for jewellery"),
        ("silver", "drawn into microscopic contact wires in electronic circuit boards"),
    ]
    metal, use_case = rng.choice(metals)

    prompt = (
        f"In an industrial processing plant, thick bars of {metal} are pulled through progressively smaller dies until they become long, flexible strands.\n\n"
        f"1. Name the property of {metal} that allows it to be {use_case}.\n"
        f"2. Contrast this property with malleability."
    )
    sol = (
        f"**Step 1:** The property is **ductility** [1 Mark: Knowledge].\n\n"
        f"**Step 2:** Ductility is the ability to be drawn or stretched into thin wires, whereas malleability is the ability to be hammered or pressed into flat sheets [1 Mark: Explanation]."
    )
    return {
        "id": f"ns7_prop_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Ductility; ductility forms wires whereas malleability forms sheets",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "02_ductility_definition_and_wires",
        "misconception_tags": ["malleability_vs_ductility"],
        "hints": {
            "tier_1": "Think of forming wires versus sheets.",
            "tier_2": "Ductile materials can be pulled into long wires.",
            "tier_3": "The property is ductility."
        }
    }


def arch_03_tensile_strength_applications(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("steel cables on a suspension bridge carrying heavy truck traffic", "tensile strength", "stretching or pulling forces"),
        ("nylon climbing rope supporting the weight of a mountaineer during a fall", "tensile strength", "pulling forces along its length"),
        ("high-tensile wire in a farm game fence resisting tension from straining posts", "tensile strength", "stretching forces without snapping"),
    ]
    scenario, prop, force_type = rng.choice(cases)

    prompt = (
        f"Consider this engineering scenario:\n"
        f"'{scenario}'.\n\n"
        f"1. Which specific type of strength must this material have to prevent it from snapping?\n"
        f"2. Describe the direction of the forces acting on the material in this application."
    )
    sol = (
        f"**Step 1:** The required property is **{prop}** [1 Mark: Knowledge].\n\n"
        f"**Step 2:** The material experiences {force_type} (forces pulling in opposite directions away from each other) [1 Mark: Explanation]."
    )
    return {
        "id": f"ns7_prop_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{prop}; resists pulling or stretching forces",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "03_tensile_strength_applications",
        "misconception_tags": ["tensile_vs_compressive_strength"],
        "hints": {
            "tier_1": "Is the material being pulled or pushed?",
            "tier_2": "Pulling forces require tensile strength.",
            "tier_3": f"The answer is {prop}."
        }
    }


def arch_04_compressive_strength_construction(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("concrete pillars supporting the deck of a multi-storey highway bridge", "compressive strength", "crushing or pushing forces"),
        ("solid clay bricks stacked to build the ground floor load-bearing walls of a building", "compressive strength", "downward pushing forces from the weight above"),
        ("granite foundation blocks supporting an industrial mining crane", "compressive strength", "heavy crushing loads pushing down"),
    ]
    scenario, prop, force_type = rng.choice(cases)

    prompt = (
        f"An architect designs structural elements for a large building:\n"
        f"'{scenario}'.\n\n"
        f"1. Which specific type of strength is most vital for these structural blocks?\n"
        f"2. Explain why a material with high tensile strength but low compressive strength would be unsuitable here."
    )
    sol = (
        f"**Step 1:** The material must possess high **{prop}** [1 Mark: Knowledge].\n\n"
        f"**Step 2:** The blocks experience {force_type}. If compressive strength is low, the material would crush, buckle, or crumble under the downward load, causing catastrophic collapse [1 Mark: Explanation]."
    )
    return {
        "id": f"ns7_prop_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{prop}; prevents crushing under downward load",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "04_compressive_strength_construction",
        "misconception_tags": ["tensile_vs_compressive_strength"],
        "hints": {
            "tier_1": "Are these pillars/blocks being stretched or crushed?",
            "tier_2": "Resisting crushing loads is called compressive strength.",
            "tier_3": f"The property is {prop}."
        }
    }


def arch_05_experimental_strength_test_load(rng: random.Random) -> Dict[str, Any]:
    mat_a = rng.choice(["Cardboard strip", "Kraft paper strip", "Polyester strip"])
    mat_b = rng.choice(["Cotton twill strip", "Nylon webbing strip", "Rayon ribbon strip"])
    w_a = rng.choice([8, 12, 16])
    w_b = w_a + rng.choice([10, 15, 20])

    svg = (
        f'<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<rect x="20" y="20" width="320" height="20" fill="#64748b" rx="3"/>'
        f'<rect x="80" y="40" width="20" height="15" fill="#334155"/>'
        f'<rect x="240" y="40" width="20" height="15" fill="#334155"/>'
        f'<line x1="90" y1="55" x2="90" y2="140" stroke="#f59e0b" stroke-width="6"/>'
        f'<line x1="250" y1="55" x2="250" y2="140" stroke="#3b82f6" stroke-width="6"/>'
        f'<rect x="70" y="140" width="40" height="40" fill="#d97706" rx="4"/>'
        f'<rect x="230" y="140" width="40" height="40" fill="#1d4ed8" rx="4"/>'
        f'<text x="90" y="165" font-family="sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">{w_a} N</text>'
        f'<text x="250" y="165" font-family="sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">{w_b} N</text>'
        f'<text x="90" y="200" font-family="sans-serif" font-size="11" fill="#334155" text-anchor="middle">Material A</text>'
        f'<text x="250" y="200" font-family="sans-serif" font-size="11" fill="#334155" text-anchor="middle">Material B</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": "Experimental setup testing tensile breaking load of two material strips",
        "diagram_role": "context"
    }

    prompt = (
        f"Two material strips of identical length, width, and thickness ({mat_a} as Material A, and {mat_b} as Material B) "
        f"are clamped to a horizontal support. Weights are added gradually to a hanger attached to the bottom of each strip until the strip tears.\n\n"
        f"- Material A snaps when the hanging load reaches {w_a} N.\n"
        f"- Material B snaps when the hanging load reaches {w_b} N.\n\n"
        f"1. Which material has the higher tensile strength?\n"
        f"2. Calculate the difference in breaking load between the two materials.\n"
        f"3. State TWO variables that had to be kept constant to make this a fair test."
    )
    diff = w_b - w_a
    sol = (
        f"**Step 1:** **Material B ({mat_b})** has the higher tensile strength because it supported a greater load ({w_b} N vs {w_a} N) before failing [1 Mark: Analysis].\n\n"
        f"**Step 2:** Difference in breaking load: $${w_b} - {w_a} = \\mathbf{{{diff}\\text{{ N}}}} \\text{{ [1 Mark: Calculation]}}$$\n\n"
        f"**Step 3:** Controlled variables (any two): strip width, strip length, strip thickness, rate of adding weights, or clamp tightness [1 Mark: Scientific Inquiry]."
    )
    return {
        "id": f"ns7_prop_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Material B ({mat_b}); difference = {diff} N; controlled width, length, thickness",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "05_experimental_strength_test_load",
        "misconception_tags": ["fair_testing_variables"],
        "hints": {
            "tier_1": "Compare the loads each strip could support before snapping.",
            "tier_2": f"Material B snapped at {w_b} N, Material A at {w_a} N. Subtract to find the difference.",
            "tier_3": f"Material B has higher strength; difference is {diff} N."
        }
    }


def arch_06_flexibility_vs_stiffness(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("a silicone baking spatula", "a cast iron frying pan", "silicone spatula", "cast iron pan"),
        ("a rubber garden hose", "a galvanized steel pipe", "rubber hose", "steel pipe"),
        ("a plastic ruler that curves into an arc", "a thick wooden metre stick", "plastic ruler", "wooden metre stick"),
    ]
    item_flex, item_rigid, name_f, name_r = rng.choice(pairs)

    prompt = (
        f"Compare {item_flex} with {item_rigid}.\n\n"
        f"1. Which of these objects exhibits high **flexibility**?\n"
        f"2. Define what is meant by **flexibility** in material science.\n"
        f"3. Name the opposing property shown by the {name_r}."
    )
    sol = (
        f"**Step 1:** The **{name_f}** exhibits high flexibility [1 Mark: Identification].\n\n"
        f"**Step 2:** Flexibility is the ability of a material to bend easily without breaking or cracking, and return to its original shape [1 Mark: Definition].\n\n"
        f"**Step 3:** The opposing property is **stiffness** (or rigidity) [1 Mark: Terminology]."
    )
    return {
        "id": f"ns7_prop_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name_f}; bends without breaking; stiffness / rigidity",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "06_flexibility_vs_stiffness",
        "misconception_tags": ["flexibility_vs_elasticity"],
        "hints": {
            "tier_1": "Which item can bend when a force is applied?",
            "tier_2": "Flexibility allows bending without snapping.",
            "tier_3": f"{name_f} is flexible; the opposite property is stiffness or rigidity."
        }
    }


def arch_07_brittleness_in_solids(rng: random.Random) -> Dict[str, Any]:
    materials = [
        ("pane of window glass", "ceramic coffee mug", "aluminium cooldrink can"),
        ("chalk stick", "fired clay brick", "copper pipe"),
        ("hard unbaked spaghetti stick", "porcelain plate", "lead fishing sinker"),
    ]
    m1, m2, ductile_m = rng.choice(materials)

    prompt = (
        f"When struck sharply with a hammer, a {m1} shatters into many sharp fragments, whereas an object made of {ductile_m} merely dents.\n\n"
        f"1. Name the property describing materials that break, snap, or shatter easily under sudden impact without prior bending.\n"
        f"2. Identify which of the three items ({m1}, {m2}, or {ductile_m}) does NOT show this property."
    )
    sol = (
        f"**Step 1:** The property is **brittleness** [1 Mark: Knowledge].\n\n"
        f"**Step 2:** **{ductile_m}** does NOT show brittleness; it is malleable and ductile, so it deforms without shattering [1 Mark: Analysis]."
    )
    return {
        "id": f"ns7_prop_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Brittleness; {ductile_m}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "07_brittleness_in_solids",
        "misconception_tags": ["brittleness_vs_hardness"],
        "hints": {
            "tier_1": "Brittle materials shatter rather than bend.",
            "tier_2": "Metals usually dent, glass and ceramics shatter.",
            "tier_3": f"Property is brittleness; non-brittle item is {ductile_m}."
        }
    }


def arch_08_hardness_scratch_test(rng: random.Random) -> Dict[str, Any]:
    minerals = [
        ("Gypsum", "Fluorite", "Quartz", "Diamond"),
        ("Calcite", "Apatite", "Topaz", "Corundum"),
        ("Talc", "Feldspar", "Quartz", "Diamond"),
    ]
    m_list = rng.choice(minerals)
    m1, m2, m3, m4 = m_list

    prompt = (
        f"A learner carries out a scratch test on four mineral specimens ({m1}, {m2}, {m3}, and {m4}):\n"
        f"- {m4} scratches all other specimens.\n"
        f"- {m3} scratches {m1} and {m2}, but cannot scratch {m4}.\n"
        f"- {m2} scratches {m1}, but cannot scratch {m3}.\n"
        f"- {m1} cannot scratch any of the other specimens.\n\n"
        f"1. Define the property of **hardness** in material science.\n"
        f"2. Arrange the four minerals in order from **softest to hardest**."
    )
    order = f"{m1} < {m2} < {m3} < {m4}"
    sol = (
        f"**Step 1:** Hardness is the resistance of a material to being scratched, abraded, or indented by another material [1 Mark: Definition].\n\n"
        f"**Step 2:** Order from softest to hardest: **{order}** [1 Mark: Deduction]."
    )
    return {
        "id": f"ns7_prop_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Resistance to scratching; order: {order}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "08_hardness_scratch_test",
        "misconception_tags": ["hardness_vs_strength"],
        "hints": {
            "tier_1": "A harder material always scratches a softer material.",
            "tier_2": f"{m1} is scratched by all others, so it is the softest.",
            "tier_3": f"Order: {order}."
        }
    }


def arch_09_density_comparison_floating_sinking(rng: random.Random) -> Dict[str, Any]:
    substances = [
        ("Pine wood", 0.55, "floats", "less dense than water"),
        ("Paraffin wax", 0.90, "floats", "less dense than water"),
        ("Solid aluminium", 2.70, "sinks", "denser than water"),
        ("Solid copper", 8.96, "sinks", "denser than water"),
        ("Lead sinker", 11.34, "sinks", "denser than water"),
    ]
    sub, density, behavior, reason = rng.choice(substances)

    prompt = (
        f"Pure water has a density of $1{{,}}0\\text{{ g/cm}}^3$.\n\n"
        f"A solid cube of {sub} has a measured density of ${str(density).replace('.', ',')}\\text{{ g/cm}}^3$.\n\n"
        f"1. Predict whether this cube will float or sink when placed in a tank of pure water.\n"
        f"2. Explain your prediction using the scientific concept of density."
    )
    sol = (
        f"**Step 1:** The cube of {sub} will **{behavior}** [1 Mark: Prediction].\n\n"
        f"**Step 2:** Since its density (${str(density).replace('.', ',')}\\text{{ g/cm}}^3$) is {reason} ($1{{,}}0\\text{{ g/cm}}^3$), the buoyant force cannot overcome its weight if denser, or easily supports it if less dense [1 Mark: Explanation]."
    )
    return {
        "id": f"ns7_prop_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{behavior}; {reason}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "09_density_comparison_floating_sinking",
        "misconception_tags": ["mass_vs_density_floating"],
        "hints": {
            "tier_1": "Compare the density of the substance to the density of water (1.0 g/cm^3).",
            "tier_2": "Objects with density < 1.0 g/cm^3 float; objects with density > 1.0 g/cm^3 sink.",
            "tier_3": f"{sub} has density {density} g/cm^3, so it {behavior}."
        }
    }


# ==============================================================================
# CLUSTER 2: Boiling, Melting & Thermal Curves (10 - 16)
# ==============================================================================

def arch_10_melting_point_definition_and_state(rng: random.Random) -> Dict[str, Any]:
    substances = [
        ("lead", 327, 25, "solid"),
        ("mercury", -39, 25, "liquid"),
        ("gallium", 30, 20, "solid"),
        ("paraffin wax", 55, 20, "solid"),
    ]
    sub, mp, t_room, state = rng.choice(substances)

    prompt = (
        f"The melting point of pure {sub} is ${mp}^\\circ\\text{{C}}$.\n\n"
        f"1. Define the term **melting point**.\n"
        f"2. What physical state (solid, liquid, or gas) is {sub} in at a room temperature of ${t_room}^\\circ\\text{{C}}$?"
    )
    sol = (
        f"**Step 1:** Melting point is the specific temperature at which a solid substance changes state into a liquid [1 Mark: Definition].\n\n"
        f"**Step 2:** At ${t_room}^\\circ\\text{{C}}$, which is {'below' if t_room < mp else 'above'} its melting point of ${mp}^\\circ\\text{{C}}$, {sub} is in the **{state}** state [1 Mark: State deduction]."
    )
    return {
        "id": f"ns7_prop_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Temperature at which solid turns to liquid; {state}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "10_melting_point_definition_and_state",
        "misconception_tags": ["melting_vs_dissolving"],
        "hints": {
            "tier_1": "Melting is the transition from solid to liquid.",
            "tier_2": f"If room temp ({t_room} °C) is below melting point ({mp} °C), it has not melted yet.",
            "tier_3": f"It is a {state}."
        }
    }


def arch_11_boiling_point_definition_and_state(rng: random.Random) -> Dict[str, Any]:
    substances = [
        ("pure ethanol", 78, 90, "gas / vapour"),
        ("water at sea level", 100, 60, "liquid"),
        ("acetone", 56, 70, "gas / vapour"),
        ("glycerol", 290, 150, "liquid"),
    ]
    sub, bp, test_t, state = rng.choice(substances)

    prompt = (
        f"The boiling point of {sub} is ${bp}^\\circ\\text{{C}}$.\n\n"
        f"1. Explain what happens throughout a liquid when it reaches its **boiling point**.\n"
        f"2. State whether {sub} is a liquid or a gas when maintained at ${test_t}^\\circ\\text{{C}}$."
    )
    sol = (
        f"**Step 1:** At the boiling point, bubbles of vapour form throughout the entire bulk of the liquid and rise rapidly to escape as gas [1 Mark: Explanation].\n\n"
        f"**Step 2:** At ${test_t}^\\circ\\text{{C}}$, which is {'above' if test_t > bp else 'below'} its boiling point of ${bp}^\\circ\\text{{C}}$, {sub} exists as a **{state}** [1 Mark: State deduction]."
    )
    return {
        "id": f"ns7_prop_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Liquid turns to gas throughout liquid; {state}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "11_boiling_point_definition_and_state",
        "misconception_tags": ["boiling_vs_evaporation"],
        "hints": {
            "tier_1": "Boiling occurs throughout the liquid, not just at the surface.",
            "tier_2": f"Compare {test_t} °C to the boiling point of {bp} °C.",
            "tier_3": f"At {test_t} °C it is a {state}."
        }
    }


def arch_12_three_states_state_identification_temp(rng: random.Random) -> Dict[str, Any]:
    materials = [
        ("Substance P", -114, 78, [-150, 20, 100], ["solid", "liquid", "gas"]),
        ("Substance Q", 0, 100, [-10, 50, 120], ["solid", "liquid", "gas"]),
        ("Substance R", -7, 59, [-20, 25, 80], ["solid", "liquid", "gas"]),
    ]
    name, mp, bp, temps, states = rng.choice(materials)
    idx = rng.choice([0, 1, 2])
    chosen_t = temps[idx]
    correct_state = states[idx]

    prompt = (
        f"A scientist records the thermal properties of {name}:\n"
        f"- Melting point: ${mp}^\\circ\\text{{C}}$\n"
        f"- Boiling point: ${bp}^\\circ\\text{{C}}$\n\n"
        f"Determine the physical state of {name} at a temperature of ${chosen_t}^\\circ\\text{{C}}$. Justify your answer."
    )
    if idx == 0:
        just = f"temperature (${chosen_t}^\\circ\\text{{C}}$) is below the melting point (${mp}^\\circ\\text{{C}}$)"
    elif idx == 1:
        just = f"temperature (${chosen_t}^\\circ\\text{{C}}$) is between the melting point (${mp}^\\circ\\text{{C}}$) and boiling point (${bp}^\\circ\\text{{C}}$)"
    else:
        just = f"temperature (${chosen_t}^\\circ\\text{{C}}$) is above the boiling point (${bp}^\\circ\\text{{C}}$)"

    sol = (
        f"**Step 1:** The physical state is **{correct_state}** [1 Mark: State].\n\n"
        f"**Step 2:** Reason: The {just} [1 Mark: Justification]."
    )
    return {
        "id": f"ns7_prop_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{correct_state}; {just}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "12_three_states_state_identification_temp",
        "misconception_tags": ["phase_changes_temperature_ranges"],
        "hints": {
            "tier_1": f"Solid below mp ({mp} °C), liquid between mp and bp, gas above bp ({bp} °C).",
            "tier_2": f"Where does {chosen_t} °C fall relative to {mp} °C and {bp} °C?",
            "tier_3": f"It is a {correct_state}."
        }
    }


def arch_13_pure_substance_sharp_melting_point(rng: random.Random) -> Dict[str, Any]:
    substances = [
        ("pure ice/water", 0, "sharp fixed temperature of exactly 0 °C"),
        ("pure naphthalene (mothballs)", 80, "sharp fixed temperature of exactly 80 °C"),
        ("pure sulfur powder", 115, "sharp fixed temperature of exactly 115 °C"),
    ]
    sub, temp, desc = rng.choice(substances)

    prompt = (
        f"In a science laboratory, a learner heats a small sample of {sub}.\n\n"
        f"1. How does the melting behaviour of a **pure substance** differ from that of a mixture?\n"
        f"2. If the thermometer reads a constant ${temp}^\\circ\\text{{C}}$ while the solid is actively turning into liquid, "
        f"what does this constant temperature tell us about the purity of the sample?"
    )
    sol = (
        f"**Step 1:** A pure substance melts at a **sharp, fixed, constant temperature** ({desc}), whereas an impure mixture melts over a range of temperatures [1 Mark: Contrast].\n\n"
        f"**Step 2:** The flat, constant temperature during melting confirms that the sample is **pure** [1 Mark: Conclusion]."
    )
    return {
        "id": f"ns7_prop_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Pure substances melt at a sharp fixed temperature; confirms sample is pure",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "13_pure_substance_sharp_melting_point",
        "misconception_tags": ["purity_and_melting_point"],
        "hints": {
            "tier_1": "Pure substances have sharp melting points.",
            "tier_2": "Mixtures melt over a range.",
            "tier_3": "Constant temperature during melting confirms purity."
        }
    }


def arch_14_mixtures_melting_range_impure(rng: random.Random) -> Dict[str, Any]:
    ranges = [
        ("Candle wax", 48, 56),
        ("Solder alloy (tin and lead mixture)", 183, 190),
        ("Butter / margarine mixture", 32, 38),
    ]
    mat, t1, t2 = rng.choice(ranges)

    prompt = (
        f"A learner records that a sample of {mat} begins to soften at ${t1}^\\circ\\text{{C}}$ and only completely melts at ${t2}^\\circ\\text{{C}}$.\n\n"
        f"1. State whether {mat} is a pure substance or a mixture.\n"
        f"2. Justify your answer using the temperature data provided."
    )
    sol = (
        f"**Step 1:** {mat} is a **mixture** [1 Mark: Classification].\n\n"
        f"**Step 2:** It melts over a **temperature range** (${t1}^\\circ\\text{{C}}$ to ${t2}^\\circ\\text{{C}}$) rather than at a single sharp, fixed temperature [1 Mark: Justification]."
    )
    return {
        "id": f"ns7_prop_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Mixture; melts over a temperature range ({t1} °C to {t2} °C)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "14_mixtures_melting_range_impure",
        "misconception_tags": ["purity_and_melting_point"],
        "hints": {
            "tier_1": "Do pure substances melt over a range or at a single fixed temperature?",
            "tier_2": f"Because it melts between {t1} °C and {t2} °C, it is not a single pure substance.",
            "tier_3": "It is a mixture."
        }
    }


def arch_15_heating_curve_phase_change_plateau(rng: random.Random) -> Dict[str, Any]:
    mp = rng.choice([0, 17, 44])
    bp = mp + rng.choice([80, 100, 120])

    svg = (
        f'<svg viewBox="0 0 380 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<line x1="50" y1="180" x2="350" y2="180" stroke="#1e293b" stroke-width="2"/>'
        f'<line x1="50" y1="180" x2="50" y2="20" stroke="#1e293b" stroke-width="2"/>'
        f'<text x="200" y="210" font-family="sans-serif" font-size="11" fill="#1e293b" text-anchor="middle">Heating time (minutes)</text>'
        f'<text x="20" y="100" font-family="sans-serif" font-size="11" fill="#1e293b" text-anchor="middle" transform="rotate(-90 20 100)">Temperature (°C)</text>'
        f'<polyline points="50,170 100,130 160,130 220,60 280,60 330,30" fill="none" stroke="#2563eb" stroke-width="3"/>'
        f'<line x1="45" y1="130" x2="55" y2="130" stroke="#ef4444" stroke-width="2"/>'
        f'<text x="40" y="134" font-family="sans-serif" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="end">{mp}°C</text>'
        f'<line x1="45" y1="60" x2="55" y2="60" stroke="#ef4444" stroke-width="2"/>'
        f'<text x="40" y="64" font-family="sans-serif" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="end">{bp}°C</text>'
        f'<text x="130" y="120" font-family="sans-serif" font-size="10" font-weight="bold" fill="#2563eb" text-anchor="middle">Plateau 1</text>'
        f'<text x="250" y="50" font-family="sans-serif" font-size="10" font-weight="bold" fill="#2563eb" text-anchor="middle">Plateau 2</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": "Heating curve showing temperature plateaus during phase changes",
        "diagram_role": "context"
    }

    prompt = (
        f"A pure substance is heated continuously at a steady rate. A heating curve is plotted from the experimental data.\n\n"
        f"1. Identify the physical change occurring at **Plateau 1** (${mp}^\\circ\\text{{C}}$).\n"
        f"2. Identify the physical change occurring at **Plateau 2** (${bp}^\\circ\\text{{C}}$).\n"
        f"3. Explain why the temperature remains flat and constant during each plateau even though heat energy is still being added."
    )
    sol = (
        f"**Step 1:** Plateau 1 represents **melting** (solid turning to liquid) at ${mp}^\\circ\\text{{C}}$ [1 Mark: Identification].\n\n"
        f"**Step 2:** Plateau 2 represents **boiling** (liquid turning to gas) at ${bp}^\\circ\\text{{C}}$ [1 Mark: Identification].\n\n"
        f"**Step 3:** The added heat energy is used to overcome intermolecular forces separating particles during the phase change, rather than raising kinetic energy/temperature [1 Mark: Scientific Explanation]."
    )
    return {
        "id": f"ns7_prop_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Plateau 1 = melting; Plateau 2 = boiling; heat overcomes intermolecular forces",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "15_heating_curve_phase_change_plateau",
        "misconception_tags": ["plateau_constant_temperature_latent_heat"],
        "hints": {
            "tier_1": "The first plateau is solid to liquid; the second is liquid to gas.",
            "tier_2": "During phase change, temperature does not rise because energy separates particles.",
            "tier_3": "Plateau 1 is melting, Plateau 2 is boiling."
        }
    }


def arch_16_cooling_curve_freezing_condensation(rng: random.Random) -> Dict[str, Any]:
    gas_name = rng.choice(["Water vapour", "Ethanol vapour", "Stearic acid vapour"])
    cond_temp = rng.choice([100, 78, 69])
    freeze_temp = cond_temp - rng.choice([50, 70, 78])

    prompt = (
        f"A sample of {gas_name} is allowed to cool down slowly from a very high temperature.\n\n"
        f"- The first horizontal plateau on the cooling curve occurs at ${cond_temp}^\\circ\\text{{C}}$.\n"
        f"- The second horizontal plateau occurs at ${freeze_temp}^\\circ\\text{{C}}$.\n\n"
        f"1. Name the phase change occurring at ${cond_temp}^\\circ\\text{{C}}$.\n"
        f"2. Name the phase change occurring at ${freeze_temp}^\\circ\\text{{C}}$.\n"
        f"3. For a pure substance, how does the freezing point compare to its melting point?"
    )
    sol = (
        f"**Step 1:** At ${cond_temp}^\\circ\\text{{C}}$, gas turns to liquid: **condensation** [1 Mark: Process].\n\n"
        f"**Step 2:** At ${freeze_temp}^\\circ\\text{{C}}$, liquid turns to solid: **freezing** (or solidification) [1 Mark: Process].\n\n"
        f"**Step 3:** For a pure substance, the freezing point is **identical (equal)** to its melting point [1 Mark: Concept]."
    )
    return {
        "id": f"ns7_prop_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Condensation; freezing / solidification; freezing point equals melting point",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "16_cooling_curve_freezing_condensation",
        "misconception_tags": ["freezing_equals_melting_point"],
        "hints": {
            "tier_1": "Cooling a gas first causes condensation, then freezing.",
            "tier_2": "Freezing point and melting point are the exact same temperature for a pure substance.",
            "tier_3": "1. Condensation, 2. Freezing, 3. They are equal."
        }
    }


# ==============================================================================
# CLUSTER 3: Electrical & Thermal Conductivity (17 - 25)
# ==============================================================================

def arch_17_electrical_conductors_identification(rng: random.Random) -> Dict[str, Any]:
    groups = [
        (["Copper wire", "Aluminium strip", "Iron nail", "Graphite rod"], "Wood block", "Graphite rod"),
        (["Silver coin", "Brass screw", "Steel paperclip", "Gold leaf"], "Plastic spoon", "Steel paperclip"),
        (["Zinc plate", "Bronze medal", "Copper coin", "Nichrome wire"], "Rubber band", "Nichrome wire"),
    ]
    conductors, insulator, highlighted = rng.choice(groups)

    prompt = (
        f"A learner has the following materials:\n"
        f"{', '.join(conductors)}, and {insulator}.\n\n"
        f"1. Define an **electrical conductor**.\n"
        f"2. Identify the single non-metal on this list that conducts electricity.\n"
        f"3. Identify the material that does NOT conduct electricity."
    )
    non_metal_cond = "Graphite rod" if "Graphite rod" in conductors else "None on this sub-list (all listed conductors are metals)"
    if "Graphite rod" not in conductors:
        non_metal_cond = "Graphite (carbon form)"

    sol = (
        f"**Step 1:** An electrical conductor is a material that allows electric current (charges) to flow easily through it [1 Mark: Definition].\n\n"
        f"**Step 2:** The non-metal conductor is **graphite** (a form of carbon) [1 Mark: Knowledge].\n\n"
        f"**Step 3:** The non-conducting material is the **{insulator}** [1 Mark: Identification]."
    )
    return {
        "id": f"ns7_prop_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Allows current to flow; graphite; {insulator}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "17_electrical_conductors_identification",
        "misconception_tags": ["all_non_metals_are_insulators_myth"],
        "hints": {
            "tier_1": "Conductors allow electric charges to pass through them.",
            "tier_2": "Graphite is a non-metal that conducts electricity.",
            "tier_3": f"Insulator is {insulator}."
        }
    }


def arch_18_electrical_insulators_identification(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Rubber gloves worn by municipal electricians handling live power cables", "rubber", "prevents electric current from passing into the electrician's body (prevents shock/electrocution)"),
        ("Plastic PVC coating on household kettle electrical cords", "polyvinyl chloride (PVC) plastic", "insulates live wires and prevents accidental electric shock"),
        ("Ceramic / porcelain discs supporting high-voltage cables on transmission pylons", "ceramic / porcelain", "stops electric charges from leaking into the metal pylon and reaching the ground"),
    ]
    scenario, mat, safety_role = rng.choice(cases)

    prompt = (
        f"Examine this electrical safety application:\n"
        f"'{scenario}'.\n\n"
        f"1. What class of electrical material is {mat} (conductor or insulator)?\n"
        f"2. Explain why this material is chosen from a safety perspective."
    )
    sol = (
        f"**Step 1:** {mat.capitalize()} is an **electrical insulator** [1 Mark: Classification].\n\n"
        f"**Step 2:** It has extremely high electrical resistance and does not allow electric charges to flow through it. Therefore, it {safety_role} [1 Mark: Safety reasoning]."
    )
    return {
        "id": f"ns7_prop_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Electrical insulator; {safety_role}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "18_electrical_insulators_identification",
        "misconception_tags": ["insulator_role_in_circuits"],
        "hints": {
            "tier_1": "Does this material allow or block electricity?",
            "tier_2": "Insulators protect people from electric shock.",
            "tier_3": f"It is an electrical insulator."
        }
    }


def arch_19_testing_electrical_conductivity_circuit(rng: random.Random) -> Dict[str, Any]:
    test_items = [
        ("brass key", True, "glows brightly", "good electrical conductor"),
        ("wooden toothpick", False, "remains unlit", "electrical insulator"),
        ("plastic paperclip", False, "remains unlit", "electrical insulator"),
        ("steel needle", True, "glows brightly", "good electrical conductor"),
    ]
    item, conducts, bulb_state, conclusion = rng.choice(test_items)

    bulb_fill = "#fef08a" if conducts else "#cbd5e1"
    bulb_glow = "#ca8a04" if conducts else "#64748b"
    bulb_emoji = "💡" if conducts else "⚫"

    svg = (
        f'<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<rect x="140" y="20" width="80" height="30" fill="#334155" rx="4"/>'
        f'<text x="180" y="40" font-family="sans-serif" font-size="12" fill="#ffffff" text-anchor="middle">Cell (1.5 V)</text>'
        f'<line x1="140" y1="35" x2="60" y2="35" stroke="#1e293b" stroke-width="2.5"/>'
        f'<line x1="60" y1="35" x2="60" y2="140" stroke="#1e293b" stroke-width="2.5"/>'
        f'<line x1="220" y1="35" x2="300" y2="35" stroke="#1e293b" stroke-width="2.5"/>'
        f'<line x1="300" y1="35" x2="300" y2="100" stroke="#1e293b" stroke-width="2.5"/>'
        f'<circle cx="300" cy="115" r="15" fill="{bulb_fill}" stroke="{bulb_glow}" stroke-width="2"/>'
        f'<text x="300" y="120" font-family="sans-serif" font-size="12" fill="{bulb_glow}" text-anchor="middle">{bulb_emoji}</text>'
        f'<line x1="300" y1="130" x2="300" y2="140" stroke="#1e293b" stroke-width="2.5"/>'
        f'<line x1="60" y1="140" x2="130" y2="140" stroke="#1e293b" stroke-width="2.5"/>'
        f'<line x1="230" y1="140" x2="300" y2="140" stroke="#1e293b" stroke-width="2.5"/>'
        f'<circle cx="130" cy="140" r="4" fill="#ef4444"/>'
        f'<circle cx="230" cy="140" r="4" fill="#ef4444"/>'
        f'<rect x="135" y="132" width="90" height="16" fill="#94a3b8" rx="2"/>'
        f'<text x="180" y="144" font-family="sans-serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">{item}</text>'
        f'<text x="180" y="180" font-family="sans-serif" font-size="11" fill="#475569" text-anchor="middle">Testing gap between clips</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": "Series circuit with gap for testing electrical conductivity of objects",
        "diagram_role": "context"
    }

    prompt = (
        f"A learner sets up a test circuit with a 1,5 V cell, connecting wires, and a small torch bulb.\n"
        f"A {item} is connected across the testing gap between the crocodile clips.\n\n"
        f"1. Predict what will happen to the torch bulb ({bulb_state} or otherwise).\n"
        f"2. What scientific conclusion can be drawn about the {item}?"
    )
    sol = (
        f"**Step 1:** The torch bulb **{bulb_state}** [1 Mark: Observation].\n\n"
        f"**Step 2:** Scientific conclusion: The {item} is a **{conclusion}** [1 Mark: Deduction]."
    )
    return {
        "id": f"ns7_prop_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Bulb {bulb_state}; {conclusion}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "19_testing_electrical_conductivity_circuit",
        "misconception_tags": ["open_vs_closed_circuit"],
        "hints": {
            "tier_1": "Does the test item conduct electricity?",
            "tier_2": f"If it conducts, the circuit is closed and the bulb lights. If not, it stays dark.",
            "tier_3": f"Bulb {bulb_state}; it is a {conclusion}."
        }
    }


def arch_20_thermal_conductors_identification(rng: random.Random) -> Dict[str, Any]:
    appliances = [
        ("the base of a stainless steel saucepan with an encapsulated copper bottom", "copper and stainless steel", "rapidly transfer heat from stove burner to the soup inside"),
        ("an aluminium heat sink attached to a computer processor", "aluminium", "quickly conduct waste heat away from the microchip to prevent overheating"),
        ("a cast iron wood-burning stove", "cast iron", "efficiently conduct and radiate heat from the fire into the room"),
    ]
    app, metal, role = rng.choice(appliances)

    prompt = (
        f"In household appliances and electronics, engineers select specific materials:\n"
        f"'{app}'.\n\n"
        f"1. Name the primary physical property of {metal} that makes it ideal for this function.\n"
        f"2. Explain how this property operates at the particle level."
    )
    sol = (
        f"**Step 1:** The primary property is high **thermal conductivity** (it is a good conductor of heat) [1 Mark: Knowledge].\n\n"
        f"**Step 2:** Particles at the hot end gain kinetic energy, vibrate faster, and collide with neighbouring particles, transferring thermal energy quickly throughout the solid [1 Mark: Particle explanation]."
    )
    return {
        "id": f"ns7_prop_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Thermal conductivity; vibrating particles transfer kinetic energy through collisions",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "20_thermal_conductors_identification",
        "misconception_tags": ["thermal_vs_electrical_conductivity"],
        "hints": {
            "tier_1": "What property allows heat to flow quickly through metals?",
            "tier_2": "Thermal conductivity.",
            "tier_3": "High thermal conductivity; vibrating particles collide and pass on heat."
        }
    }


def arch_21_thermal_insulators_everyday_uses(rng: random.Random) -> Dict[str, Any]:
    insulators = [
        ("expanded polystyrene takeaway cup holding boiling coffee", "polystyrene", "keeps the beverage hot while protecting hands from burns"),
        ("thick knitted woollen blanket on a bed during a freezing winter night", "wool", "traps a layer of stagnant air, preventing body heat from escaping"),
        ("wooden spoon used to stir a pot of boiling vegetable stew", "wood", "does not conduct heat up the handle, so the cook's hand does not get burned"),
    ]
    scenario, mat, purpose = rng.choice(insulators)

    prompt = (
        f"Consider the everyday object described below:\n"
        f"'{scenario}'.\n\n"
        f"1. What term describes a material that resists the transfer of heat energy?\n"
        f"2. Explain why {mat} is an effective choice in this scenario."
    )
    sol = (
        f"**Step 1:** Such a material is called a **thermal insulator** [1 Mark: Terminology].\n\n"
        f"**Step 2:** {mat.capitalize()} has low thermal conductivity (it conducts heat very slowly/poorly). Consequently, it {purpose} [1 Mark: Application]."
    )
    return {
        "id": f"ns7_prop_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Thermal insulator; poor conductor of heat that {purpose}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "21_thermal_insulators_everyday_uses",
        "misconception_tags": ["insulators_generate_heat_myth"],
        "hints": {
            "tier_1": "Does this material conduct heat quickly or slowly?",
            "tier_2": "Materials that conduct heat poorly are thermal insulators.",
            "tier_3": "Thermal insulator."
        }
    }


def arch_22_thermal_conductivity_experiment_wax_pins(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Copper", 1, 15),
        ("Aluminium", 2, 28),
        ("Iron", 3, 55),
        ("Lead", 4, 90),
    ]
    rng.shuffle(metals)
    fastest = min(metals, key=lambda x: x[2])
    slowest = max(metals, key=lambda x: x[2])

    svg = (
        f'<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<rect x="20" y="60" width="340" height="12" fill="#cbd5e1" stroke="#334155"/>'
        f'<path d="M 40,140 L 55,90 L 70,140 Z" fill="#3b82f6"/>'
        f'<path d="M 47,120 L 55,80 L 63,120 Z" fill="#ef4444"/>'
        f'<text x="55" y="165" font-family="sans-serif" font-size="11" fill="#1e293b" text-anchor="middle">Heat Source</text>'
        f'<line x1="120" y1="72" x2="120" y2="110" stroke="#f59e0b" stroke-width="3"/>'
        f'<circle cx="120" cy="115" r="4" fill="#d97706"/>'
        f'<line x1="200" y1="72" x2="200" y2="110" stroke="#f59e0b" stroke-width="3"/>'
        f'<circle cx="200" cy="115" r="4" fill="#d97706"/>'
        f'<line x1="280" y1="72" x2="280" y2="110" stroke="#f59e0b" stroke-width="3"/>'
        f'<circle cx="280" cy="115" r="4" fill="#d97706"/>'
        f'<text x="120" y="135" font-family="sans-serif" font-size="10" fill="#475569" text-anchor="middle">{metals[0][0]}</text>'
        f'<text x="200" y="135" font-family="sans-serif" font-size="10" fill="#475569" text-anchor="middle">{metals[1][0]}</text>'
        f'<text x="280" y="135" font-family="sans-serif" font-size="10" fill="#475569" text-anchor="middle">{metals[2][0]}</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": "Experiment measuring heat conduction along metal rods using melting wax drops and pins",
        "diagram_role": "context"
    }

    prompt = (
        f"In a science investigation, four metal rods of identical length and thickness are heated at one end with a Bunsen burner.\n"
        f"Drawing pins are fixed to the far ends using identical drops of candle wax. The time taken for the wax to melt and the pin to drop is recorded:\n\n"
        f"- {metals[0][0]}: {metals[0][2]} seconds\n"
        f"- {metals[1][0]}: {metals[1][2]} seconds\n"
        f"- {metals[2][0]}: {metals[2][2]} seconds\n"
        f"- {metals[3][0]}: {metals[3][2]} seconds\n\n"
        f"1. Which metal is the best thermal conductor?\n"
        f"2. Which metal is the poorest thermal conductor?\n"
        f"3. Explain why the pin on the best conductor dropped first."
    )
    sol = (
        f"**Step 1:** The best thermal conductor is **{fastest[0]}** because its pin fell in the shortest time ({fastest[2]} seconds) [1 Mark: Identification].\n\n"
        f"**Step 2:** The poorest thermal conductor is **{slowest[0]}** because its pin took the longest time ({slowest[2]} seconds) to fall [1 Mark: Identification].\n\n"
        f"**Step 3:** Heat travelled along the rod most rapidly through conduction, melting the wax holding the pin first [1 Mark: Explanation]."
    )
    return {
        "id": f"ns7_prop_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Best = {fastest[0]}; Poorest = {slowest[0]}; heat conducted fastest to melt wax",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "22_thermal_conductivity_experiment_wax_pins",
        "misconception_tags": ["time_vs_rate_of_conduction"],
        "hints": {
            "tier_1": "Shorter time to melt wax means faster heat transfer.",
            "tier_2": f"Shortest time is {fastest[2]} s ({fastest[0]}); longest is {slowest[2]} s ({slowest[0]}).",
            "tier_3": f"Best conductor: {fastest[0]}; Poorest: {slowest[0]}."
        }
    }


def arch_23_dual_property_selection_cookware(rng: random.Random) -> Dict[str, Any]:
    pots = [
        ("frying pan", "aluminium", "Bakelite / silicone", "conduct heat to food", "insulate cook's hand"),
        ("stock pot", "stainless steel", "hardwood handle", "transfer thermal energy from burner", "prevent heat transfer to hands"),
        ("camping kettle", "copper base", "heat-resistant plastic grip", "boil water quickly", "allow safe lifting without gloves"),
    ]
    vessel, base_mat, handle_mat, base_func, handle_func = rng.choice(pots)

    prompt = (
        f"A commercial kitchen cookware manufacturer designs a {vessel}.\n"
        f"The body and base are made of {base_mat}, while the handle is covered with {handle_mat}.\n\n"
        f"1. Explain the scientific reason for selecting {base_mat} for the base of the {vessel}.\n"
        f"2. Explain the scientific reason for selecting {handle_mat} for the handle.\n"
        f"3. What would happen if the entire {vessel}, including the handle, was manufactured from {base_mat} alone?"
    )
    sol = (
        f"**Step 1:** {base_mat.capitalize()} is a good **thermal conductor**, allowing heat to transfer rapidly from the stove to cook food efficiently [1 Mark: Base explanation].\n\n"
        f"**Step 2:** {handle_mat.capitalize()} is a **thermal insulator**, preventing heat from conducting into the handle so that the user does not burn their hand [1 Mark: Handle explanation].\n\n"
        f"**Step 3:** The handle would conduct heat rapidly and become extremely hot, creating a severe burn hazard for anyone lifting it without heat-proof gloves [1 Mark: Consequence]."
    )
    return {
        "id": f"ns7_prop_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Base conducts heat; handle insulates heat; all-metal handle would burn user's hand",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "23_dual_property_selection_cookware",
        "misconception_tags": ["material_property_pairing"],
        "hints": {
            "tier_1": "Think about what the base needs to do versus what the handle needs to do.",
            "tier_2": "Base needs thermal conduction; handle needs thermal insulation.",
            "tier_3": "Base conducts heat to food; handle insulates to prevent burns."
        }
    }


def arch_24_dual_property_selection_cables(rng: random.Random) -> Dict[str, Any]:
    cables = [
        ("household electrical appliance power cord", "copper", "flexible PVC plastic"),
        ("submersible water pump power lead", "copper", "synthetic rubber sheath"),
        ("extension lead for outdoor power tools", "copper", "flexible polyurethane outer casing"),
    ]
    desc, core, sheath = rng.choice(cables)

    prompt = (
        f"Examine the construction of a typical {desc}:\n"
        f"It consists of internal stranded wires made of {core}, surrounded by an outer sheath of {sheath}.\n\n"
        f"1. State the electrical function of the inner {core} wires.\n"
        f"2. State the electrical and mechanical function of the outer {sheath} sheath.\n"
        f"3. Explain why {sheath} is preferred over glass as an insulator in this application."
    )
    sol = (
        f"**Step 1:** The inner {core} acts as an **electrical conductor**, allowing electric current to flow to power the appliance [1 Mark: Core function].\n\n"
        f"**Step 2:** The outer {sheath} acts as an **electrical insulator** (preventing electric shock/short circuits) and provides mechanical protection [1 Mark: Sheath function].\n\n"
        f"**Step 3:** {sheath.capitalize()} is **flexible** and bendable without cracking, whereas glass is brittle and would shatter when the cord is coiled or bent [1 Mark: Material comparison]."
    )
    return {
        "id": f"ns7_prop_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Core conducts electricity; sheath insulates electricity; sheath is flexible whereas glass is brittle",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "24_dual_property_selection_cables",
        "misconception_tags": ["flexibility_and_electrical_insulation"],
        "hints": {
            "tier_1": "Core conducts electricity; sheath insulates.",
            "tier_2": "Cords must bend, so the insulator must be flexible, not brittle like glass.",
            "tier_3": "Core is conductor; sheath is flexible insulator."
        }
    }


def arch_25_magnetic_vs_non_magnetic_materials(rng: random.Random) -> Dict[str, Any]:
    items = [
        ("Steel paperclip", True, "contains iron, attracted to magnet"),
        ("Aluminium cooldrink can", False, "non-ferrous metal, not attracted"),
        ("Copper water pipe", False, "non-ferrous metal, not attracted"),
        ("Iron nail", True, "ferromagnetic element, strongly attracted"),
        ("Brass picture hook", False, "copper-zinc alloy, not attracted"),
        ("Nickel coin alloy", True, "nickel is magnetic, attracted"),
    ]
    rng.shuffle(items)
    chosen_pair = [items[0], items[1]]

    prompt = (
        f"A learner tests several household objects using a bar magnet:\n"
        f"- Object 1: {chosen_pair[0][0]}\n"
        f"- Object 2: {chosen_pair[1][0]}\n\n"
        f"1. Predict whether each object will be attracted to the magnet.\n"
        f"2. Name the THREE pure metallic elements that are naturally attracted to magnets."
    )
    ans_1 = "Attracted" if chosen_pair[0][1] else "Not attracted"
    ans_2 = "Attracted" if chosen_pair[1][1] else "Not attracted"

    sol = (
        f"**Step 1:**\n"
        f"- Object 1 ({chosen_pair[0][0]}): **{ans_1}** [1 Mark: Observation].\n"
        f"- Object 2 ({chosen_pair[1][0]}): **{ans_2}** [1 Mark: Observation].\n\n"
        f"**Step 2:** The three naturally magnetic elements are **iron (Fe)**, **nickel (Ni)**, and **cobalt (Co)** [1 Mark: Knowledge]."
    )
    return {
        "id": f"ns7_prop_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Obj 1: {ans_1}; Obj 2: {ans_2}; Iron, nickel, cobalt",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "25_magnetic_vs_non_magnetic_materials",
        "misconception_tags": ["all_metals_are_magnetic_myth"],
        "hints": {
            "tier_1": "Only ferromagnetic metals (iron, nickel, cobalt) and steel are attracted to magnets.",
            "tier_2": "Aluminium, copper, and brass are NOT magnetic.",
            "tier_3": f"Obj 1: {ans_1}; Obj 2: {ans_2}; Magnetic elements: Iron, Nickel, Cobalt."
        }
    }
