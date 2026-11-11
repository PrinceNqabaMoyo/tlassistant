"""
Grade 8 Natural Sciences - Term 2: Particle Model of Matter (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr8/Term 2/02. Particle model of matter.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Density, Mass, and Volume (26 - 34)
# ==============================================================================

def arch_26_density_definition_and_formula(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Density is a fundamental physical property that links the mass of an object to its volume.\n\n"
        f"1. State the scientific definition of **density**.\n"
        f"2. Write the standard mathematical formula used to calculate density, defining each variable symbol.\n"
        f"3. State the two standard scientific units for density (one in metric lab units and one in SI units), and explain how to convert between them."
    )
    sol = (
        f"**Step 1:** Density is defined as the **mass per unit volume** of a material [1 Mark: Definition].\n\n"
        f"**Step 2:** Formula: $$\\rho = \\frac{{m}}{{V}}$$\n"
        f"where $\\rho$ = density, $m$ = mass, and $V$ = volume [1 Mark: Formula and variables].\n\n"
        f"**Step 3:** Units: **$\\text{{g/cm}}^3$** (lab) and **$\\text{{kg/m}}^3$** (SI). To convert from $\\text{{g/cm}}^3$ to $\\text{{kg/m}}^3$, multiply by $1\\,000$ (e.g. $1\\text{{ g/cm}}^3 = 1\\,000\\text{{ kg/m}}^3$) [1 Mark: Units and conversion]."
    )
    return {
        "id": f"ns8_pmm_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Mass per unit volume; Density = mass / volume; g/cm3 and kg/m3 (multiply by 1000)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "26_density_definition_and_formula",
        "misconception_tags": ["density_definition_formula_units"],
        "hints": {
            "tier_1": "Density = mass divided by volume.",
            "tier_2": "Units are g/cm3 or kg/m3.",
            "tier_3": "Mass per unit volume; rho = m / V; 1 g/cm3 = 1000 kg/m3."
        }
    }


def arch_27_density_calculation_cube_or_block(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Aluminium block", 2.7, 5, 4, 2),
        ("Iron block", 7.8, 4, 3, 2),
        ("Copper block", 8.9, 5, 2, 2),
        ("Lead block", 11.3, 3, 2, 2),
    ]
    name, d_known, l, w, h = rng.choice(metals)
    vol = l * w * h
    mass = round(d_known * vol, 1)
    calc_d = round(mass / vol, 2)
    d_str = str(calc_d).replace(".", ",")

    prompt = (
        f"A rectangular solid block of an unknown metal has dimensions:\n"
        f"- Length = ${l}\\text{{ cm}}$\n"
        f"- Width = ${w}\\text{{ cm}}$\n"
        f"- Height = ${h}\\text{{ cm}}$\n\n"
        f"When placed on a top-pan balance, its mass is found to be **${str(mass).replace('.', ',')}\\text{{ g}}**.\n\n"
        f"1. Calculate the volume of the rectangular block in $\\text{{cm}}^3$.\n"
        f"2. Calculate the density of the metal (show formula and working).\n"
        f"3. State the correct unit for your answer."
    )
    sol = (
        f"**Step 1:** $\\text{{Volume}} = \\text{{length}} \\times \\text{{width}} \\times \\text{{height}} = {l} \\times {w} \\times {h} = \\mathbf{{{vol}\\text{{ cm}}^3}}$ [1 Mark: Volume].\n\n"
        f"**Step 2:** $\\rho = \\frac{{m}}{{V}} = \\frac{{{str(mass).replace('.', ',')}}}{{{vol}}} = \\mathbf{{{d_str}}}$ [1 Mark: Calculation].\n\n"
        f"**Step 3:** Unit: **$\\text{{g/cm}}^3$** [1 Mark: Unit]."
    )
    return {
        "id": f"ns8_pmm_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Volume = {vol} cm3; Density = {d_str} g/cm3",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "27_density_calculation_cube_or_block",
        "misconception_tags": ["density_calculation_regular_solid"],
        "hints": {
            "tier_1": "Volume = length x width x height. Density = mass / volume.",
            "tier_2": f"Volume = {vol} cm3. Divide {mass} by {vol}.",
            "tier_3": f"Volume = {vol} cm3; Density = {d_str} g/cm3."
        }
    }


def arch_28_density_displacement_can_eureka_method(rng: random.Random) -> Dict[str, Any]:
    v_initial = rng.choice([50, 60, 70])
    v_stone = rng.choice([15, 20, 25, 30])
    v_final = v_initial + v_stone
    stone_mass = round(v_stone * rng.choice([2.5, 2.6, 2.8]), 1)
    density = round(stone_mass / v_stone, 2)
    d_str = str(density).replace(".", ",")

    prompt = (
        f"To find the density of an irregular rock, a student uses a measuring cylinder water displacement method:\n"
        f"- Initial water level in cylinder = **${v_initial}\\text{{ cm}}^3$**\n"
        f"- Water level after gently submerging the rock = **${v_final}\\text{{ cm}}^3$**\n"
        f"- Mass of the rock on a digital balance = **${str(stone_mass).replace('.', ',')}\\text{{ g}}**\n\n"
        f"1. Calculate the volume of the rock.\n"
        f"2. Calculate the density of the rock in $\\text{{g/cm}}^3$.\n"
        f"3. Explain why the water displacement (Eureka) method is needed for a stone rather than using a ruler."
    )
    sol = (
        f"**Step 1:** $\\text{{Volume of rock}} = \\text{{Final level}} - \\text{{Initial level}} = {v_final} - {v_initial} = \\mathbf{{{v_stone}\\text{{ cm}}^3}}$ [1 Mark: Volume calculation].\n\n"
        f"**Step 2:** $\\rho = \\frac{{m}}{{V}} = \\frac{{{str(stone_mass).replace('.', ',')}}}{{{v_stone}}} = \\mathbf{{{d_str}\\text{{ g/cm}}^3}}$ [1 Mark: Density calculation].\n\n"
        f"**Step 3:** A stone has an **irregular, uneven shape**, so its dimensions cannot be measured with a ruler to apply a simple mathematical formula; submerged objects displace an equal volume of liquid [1 Mark: Displacement justification]."
    )
    return {
        "id": f"ns8_pmm_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Volume = {v_stone} cm3; Density = {d_str} g/cm3; Stone has irregular shape that cannot be measured with a ruler",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "28_density_displacement_can_eureka_method",
        "misconception_tags": ["displacement_method_density"],
        "hints": {
            "tier_1": "Subtract the two water levels to get the rock volume.",
            "tier_2": f"Volume = {v_final} - {v_initial} = {v_stone} cm3. Divide mass by volume.",
            "tier_3": f"Volume = {v_stone} cm3; Density = {d_str} g/cm3."
        }
    }


def arch_29_comparing_densities_of_solids_liquids_gases(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In general, solids are slightly denser than liquids, but both are about $1\\,000$ times denser than gases.\n\n"
        f"For example, at room temperature:\n"
        f"- Solid iron: $\\approx 7,8\\text{{ g/cm}}^3$\n"
        f"- Liquid water: $\\approx 1,0\\text{{ g/cm}}^3$\n"
        f"- Air (gas): $\\approx 0,0012\\text{{ g/cm}}^3$\n\n"
        f"1. Rank the three states of matter in order from **highest density to lowest density**.\n"
        f"2. Use the particle model (particle spacing and number of particles per unit volume) to explain why gases have such remarkably low densities.\n"
        f"3. Why are solid and liquid densities so similar to each other?"
    )
    sol = (
        f"**Step 1:** Ranking: **Solid > Liquid >> Gas** [1 Mark: Ranking].\n\n"
        f"**Step 2:** Gas particles are separated by **enormous empty spaces**, so there are very few particles (very little mass) in any given volume [1 Mark: Gas particle spacing].\n\n"
        f"**Step 3:** In both solids and liquids, particles are **closely packed together and touching**, meaning both states contain a similar number of particles per unit volume [1 Mark: Solid vs Liquid similarity]."
    )
    return {
        "id": f"ns8_pmm_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Solid > Liquid >> Gas; Gases have huge empty spaces with few particles per volume; Solids and liquids both have touching particles",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "29_comparing_densities_of_solids_liquids_gases",
        "misconception_tags": ["density_comparison_across_states"],
        "hints": {
            "tier_1": "Solids are heaviest for their size; gases are mostly empty space.",
            "tier_2": "Gas particles are far apart, meaning very few particles per cm3.",
            "tier_3": "Solid > Liquid >> Gas; large empty spaces in gas; particles touching in solids/liquids."
        }
    }


def arch_30_factors_influencing_density_particle_mass_and_spacing(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Gold ($19,3\\text{{ g/cm}}^3$) vs Aluminium ($2,7\\text{{ g/cm}}^3$)", "Gold atoms are much heavier (atomic mass 197 vs 27) and are packed tightly together"),
        ("Lead ($11,3\\text{{ g/cm}}^3$) vs Wood/pine ($0,5\\text{{ g/cm}}^3$)", "Lead contains heavy atoms tightly packed; wood consists of light carbon/hydrogen/oxygen with large cellular air cavities"),
    ]
    pair, explanation = rng.choice(pairs)

    prompt = (
        f"Even within the solid state, different materials have vastly different densities:\n"
        f"**{pair}**.\n\n"
        f"1. State the **two microscopic factors** that determine the density of any material.\n"
        f"2. Explain using these two factors why the denser material in this pair has such a higher density ({explanation.split(';')[0]})."
    )
    sol = (
        f"**Step 1:** The two factors are:\n"
        f"- (1) The **mass of the individual particles (atoms or molecules)** that make up the substance [1 Mark].\n"
        f"- (2) The **spacing / closeness of packing** between particles (how tightly packed they are) [1 Mark].\n\n"
        f"**Step 2:** {explanation} [1 Mark: Application]."
    )
    return {
        "id": f"ns8_pmm_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Mass of individual particles and particle spacing/packing; {explanation}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "30_factors_influencing_density_particle_mass_and_spacing",
        "misconception_tags": ["factors_influencing_density"],
        "hints": {
            "tier_1": "What makes one solid heavier than another? (1) Heavier atoms; (2) Tighter packing.",
            "tier_2": "Mass of particles and space between them.",
            "tier_3": "Individual particle mass and particle spacing; heavier atoms and tighter packing."
        }
    }


def arch_31_the_density_anomaly_of_water_and_ice(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"For almost all substances, the solid phase is denser than the liquid phase. However, **water is a famous exception**:\n"
        f"- Density of solid ice at $0^\\circ\\text{{C}} \\approx 0,92\\text{{ g/cm}}^3$\n"
        f"- Density of liquid water at $0^\\circ\\text{{C}} \\approx 1,00\\text{{ g/cm}}^3$\n\n"
        f"1. What happens when ice cubes are placed in a glass of water?\n"
        f"2. Explain at a molecular level why solid ice is **less dense** than liquid water.\n"
        f"3. Explain why this unique property of water is crucial for the survival of aquatic organisms during freezing winters."
    )
    sol = (
        f"**Step 1:** The ice cubes **float** on top of the liquid water [1 Mark: Observation].\n\n"
        f"**Step 2:** When water freezes, hydrogen bonds force the molecules into an **open hexagonal crystal lattice with large empty spaces** inside the framework; when ice melts, this rigid lattice collapses and molecules pack closer together in the liquid [1 Mark: Open lattice explanation].\n\n"
        f"**Step 3:** Lakes and rivers **freeze from the top down**, forming an insulating layer of floating ice that protects liquid water underneath, allowing fish and aquatic life to survive below the ice [1 Mark: Ecological importance]."
    )
    return {
        "id": f"ns8_pmm_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Ice floats; Open hexagonal lattice has larger empty spaces than liquid; Ice forms insulating top layer so aquatic life survives underneath",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "31_the_density_anomaly_of_water_and_ice",
        "misconception_tags": ["density_anomaly_of_water_ice"],
        "hints": {
            "tier_1": "Ice floats on water because it is less dense.",
            "tier_2": "Ice forms an open cage lattice that takes up more space.",
            "tier_3": "Ice floats; open hexagonal crystal lattice; insulating top layer keeps ponds from freezing solid."
        }
    }


def arch_32_floating_and_sinking_density_principles(rng: random.Random) -> Dict[str, Any]:
    objects = [
        ("Wood block", 0.65, "Water", 1.0, "Float", "its density (0,65 g/cm3) is lower than water"),
        ("Lead sinker", 11.3, "Water", 1.0, "Sink", "its density (11,3 g/cm3) is much higher than water"),
        ("Vegetable oil", 0.92, "Water", 1.0, "Float", "its density is lower than water, forming a layer on top"),
        ("Gold nugget", 19.3, "Liquid mercury", 13.6, "Sink", "gold is denser than liquid mercury"),
        ("Iron bolt", 7.8, "Liquid mercury", 13.6, "Float", "iron is less dense than liquid mercury"),
    ]
    sub, d_sub, fluid, d_fluid, action, reason = rng.choice(objects)

    prompt = (
        f"Consider an object made of **{sub}** (density = ${str(d_sub).replace('.', ',')}\\text{{ g/cm}}^3$) placed into **{fluid}** (density = ${str(d_fluid).replace('.', ',')}\\text{{ g/cm}}^3$).\n\n"
        f"1. Predict whether the {sub.lower()} will **float** or **sink** in the {fluid.lower()}.\n"
        f"2. State the scientific rule governing floating and sinking in terms of relative densities.\n"
        f"3. How does a massive steel ship (steel density $\\approx 7,8\\text{{ g/cm}}^3$) manage to float on water?"
    )
    sol = (
        f"**Step 1:** The {sub.lower()} will **{action.lower()}** [1 Mark: Prediction].\n\n"
        f"**Step 2:** An object **floats if its density is less than the fluid's density**, and **sinks if its density is greater** [1 Mark: Density rule].\n\n"
        f"**Step 3:** A ship has a hollow hull filled mostly with **air**, making the **overall (average) density of the ship less than the density of water** [1 Mark: Ship floating explanation]."
    )
    return {
        "id": f"ns8_pmm_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{action}; Floats if object density < fluid density, sinks if > fluid density; Hollow hull contains air lowering overall average density",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "32_floating_and_sinking_density_principles",
        "misconception_tags": ["floating_sinking_density_rules"],
        "hints": {
            "tier_1": f"Compare {d_sub} to {d_fluid}. Less dense floats, denser sinks.",
            "tier_2": "Ships have lots of air inside them, making average density low.",
            "tier_3": f"{action}; float if less dense, sink if more dense; hollow hull with air."
        }
    }


def arch_33_density_column_stacking_liquids(rng: random.Random) -> Dict[str, Any]:
    bead_dens = rng.choice([0.90, 0.92, 0.95])
    bead_col = rng.choice(["#dc2626", "#9333ea", "#16a34a"])
    bead_y = rng.choice([93, 95, 97])

    svg = (
        f'<svg viewBox="0 0 320 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="15" y="15" width="290" height="190" rx="6" fill="#f8fafc"/>'
        f'<text x="160" y="32" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Liquid Density Column</text>'
        # Cylinder outline
        f'<rect x="100" y="45" width="120" height="150" rx="4" fill="#ffffff" stroke="#334155" stroke-width="2"/>'
        # Layer 1
        f'<rect x="102" y="47" width="116" height="48" fill="#fef08a" opacity="0.8"/>'
        f'<text x="160" y="70" font-family="sans-serif" font-size="10" font-weight="bold" fill="#854d0e" text-anchor="middle">Liquid A (0,8)</text>'
        # Bead floating at boundary
        f'<circle cx="160" cy="{bead_y}" r="8" fill="{bead_col}" stroke="#1e293b" stroke-width="1.5"/>'
        # Layer 2
        f'<rect x="102" y="95" width="116" height="50" fill="#38bdf8" opacity="0.8"/>'
        f'<text x="160" y="125" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0369a1" text-anchor="middle">Liquid B (1,0)</text>'
        # Layer 3
        f'<rect x="102" y="145" width="116" height="48" fill="#d97706" opacity="0.8"/>'
        f'<text x="160" y="175" font-family="sans-serif" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">Liquid C (1,4)</text>'
        f'<text x="160" y="202" font-family="sans-serif" font-size="9" fill="#475569" text-anchor="middle">Plastic Bead: {str(bead_dens).replace(".", ",")} g/cm³</text>'
        f'</svg>'
    )

    prompt = (
        f"Three immiscible liquids of different densities are carefully poured into a cylinder:\n"
        f"- Liquid A: density $0,8\\text{{ g/cm}}^3$\n"
        f"- Liquid B: density $1,0\\text{{ g/cm}}^3$\n"
        f"- Liquid C: density $1,4\\text{{ g/cm}}^3$\n\n"
        f"1. In what order will the three liquids settle from **top to bottom**?\n"
        f"2. Explain why the liquids arrange themselves in this specific order.\n"
        f"3. If a small plastic bead of density **${str(bead_dens).replace('.', ',')}\\text{{ g/cm}}^3$** is dropped into the cylinder, where will it settle?"
    )
    sol = (
        f"**Step 1:** Top to bottom order: **Liquid A ($0,8\\text{{ g/cm}}^3$) at the top, Liquid B ($1,0\\text{{ g/cm}}^3$) in the middle, Liquid C ($1,4\\text{{ g/cm}}^3$) at the bottom** [1 Mark: Layer order].\n\n"
        f"**Step 2:** Less dense liquids float on top of denser liquids; the densest liquid sinks to the very bottom [1 Mark: Density settling rule].\n\n"
        f"**Step 3:** The bead (${str(bead_dens).replace('.', ',')}\\text{{ g/cm}}^3$) will sink through Liquid A ($0,8$) and **float on top of Liquid B ($1,0$)**, resting at the boundary between Layer A and Layer B [1 Mark: Bead location]."
    )
    return {
        "id": f"ns8_pmm_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Top: A (0,8), Middle: B (1,0), Bottom: C (1,4); Less dense floats on denser; Bead settles at boundary between A and B",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "33_density_column_stacking_liquids",
        "misconception_tags": ["density_column_layering"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Lightest on top, heaviest on bottom.",
            "tier_2": "0.92 is between 0.8 and 1.0, so the bead floats between layer A and B.",
            "tier_3": "Top A, Middle B, Bottom C; bead floats between A and B."
        }
    }


def arch_34_calculating_mass_or_volume_from_density(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("mass", "gold", 19.3, 50, "mass = density x volume"),
        ("volume", "iron", 7.8, 156, "volume = mass / density"),
        ("mass", "mercury", 13.6, 25, "mass = density x volume"),
        ("volume", "aluminium", 2.7, 81, "volume = mass / density"),
    ]
    target_var, material, d, val, formula_used = rng.choice(cases)

    if target_var == "mass":
        ans = round(d * val, 1)
        prompt = (
            f"The density of {material} is **${str(d).replace('.', ',')}\\text{{ g/cm}}^3$**.\n\n"
            f"Calculate the **mass** of a ${val}\\text{{ cm}}^3$ sample of {material}.\n"
            f"1. State the formula rearranged to solve for mass.\n"
            f"2. Show the calculation and state the final answer with units."
        )
        sol = (
            f"**Step 1:** Formula: $m = \\rho \\times V$ [1 Mark: Rearranged formula].\n\n"
            f"**Step 2:** $m = {str(d).replace('.', ',')} \\times {val} = \\mathbf{{{str(ans).replace('.', ',')}\\text{{ g}}}}$ [1 Mark: Calculation and units]."
        )
    else:
        ans = round(val / d, 1)
        prompt = (
            f"The density of {material} is **${str(d).replace('.', ',')}\\text{{ g/cm}}^3$**.\n\n"
            f"Calculate the **volume** occupied by a ${val}\\text{{ g}}$ sample of {material}.\n"
            f"1. State the formula rearranged to solve for volume.\n"
            f"2. Show the calculation and state the final answer with units."
        )
        sol = (
            f"**Step 1:** Formula: $V = \\frac{{m}}{{\\rho}}$ [1 Mark: Rearranged formula].\n\n"
            f"**Step 2:** $V = \\frac{{{val}}}{{{str(d).replace('.', ',')}}} = \\mathbf{{{str(ans).replace('.', ',')}\\text{{ cm}}^3}}$ [1 Mark: Calculation and units]."
        )

    return {
        "id": f"ns8_pmm_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Formula: {formula_used}; Answer: {str(ans).replace('.', ',')}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "34_calculating_mass_or_volume_from_density",
        "misconception_tags": ["density_triangle_rearrangement"],
        "hints": {
            "tier_1": f"Rearrange density = mass / volume to find {target_var}.",
            "tier_2": f"If finding mass, multiply density by volume; if finding volume, divide mass by density.",
            "tier_3": f"{formula_used}; {str(ans).replace('.', ',')}."
        }
    }


# ==============================================================================
# CLUSTER 5: Thermal Expansion and Contraction (35 - 41)
# ==============================================================================

def arch_35_thermal_expansion_particle_level_explanation(rng: random.Random) -> Dict[str, Any]:
    materials = [
        ("a long steel bridge deck", "expands by several centimeters on a hot summer day"),
        ("a copper hot water pipe", "lengthens when hot water begins flowing through it"),
        ("the metal rim of a wooden cart wheel", "heated until it expands to fit over the wooden wheel"),
    ]
    mat, context = rng.choice(materials)

    prompt = (
        f"When **{mat}** is heated, it undergoes **thermal expansion** ({context}).\n\n"
        f"1. Do the individual atoms/particles themselves get bigger during expansion? (Yes or No)\n"
        f"2. Explain what actually happens at a particle level when a solid is heated (motion, kinetic energy, and spacing).\n"
        f"3. What happens to the overall mass and the density of the material during thermal expansion?"
    )
    sol = (
        f"**Step 1:** **No**, the individual particles do NOT get bigger or change size [1 Mark: Yes/No].\n\n"
        f"**Step 2:** When heated, particles absorb thermal energy and **vibrate more vigorously**, pushing each other **slightly further apart**, increasing the empty space between them [1 Mark: Particle spacing explanation].\n\n"
        f"**Step 3:** The **mass remains constant** (no particles added/removed), but because volume increases, the **density decreases** [1 Mark: Mass and density changes]."
    )
    return {
        "id": f"ns8_pmm_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "No (particles stay same size); Particles vibrate more and push further apart; Mass is constant, density decreases",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "35_thermal_expansion_particle_level_explanation",
        "misconception_tags": ["thermal_expansion_particle_misconception"],
        "hints": {
            "tier_1": "Atoms never grow fat! The spaces between them just get bigger.",
            "tier_2": "Vibrating particles push neighbors away.",
            "tier_3": "No; particles vibrate more and push apart; mass constant, density decreases."
        }
    }


def arch_36_thermal_contraction_particle_level_explanation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When a hot solid or liquid cools down, it undergoes **thermal contraction** (shrinks in volume).\n\n"
        f"1. Use the particle model of matter to explain why materials contract when cooled.\n"
        f"2. Does the number of particles or the mass of the material decrease during contraction?\n"
        f"3. How does thermal contraction affect the density of the material?"
    )
    sol = (
        f"**Step 1:** As the material cools, particles **lose kinetic energy and vibrate/move slower**; attractive intermolecular forces pull them **closer together**, reducing the empty spaces between them [1 Mark: Contraction mechanism].\n\n"
        f"**Step 2:** **No**, the number of particles and total mass remain **strictly constant** [1 Mark: Constant mass].\n\n"
        f"**Step 3:** Because the same mass now occupies a smaller volume, the **density increases** [1 Mark: Density increase]."
    )
    return {
        "id": f"ns8_pmm_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Particles lose kinetic energy and attractive forces pull them closer; Mass/particles remain constant; Density increases",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "36_thermal_contraction_particle_level_explanation",
        "misconception_tags": ["thermal_contraction_particle_level"],
        "hints": {
            "tier_1": "Cooling means slower particles, so they settle closer together.",
            "tier_2": "Same mass in smaller volume = higher density.",
            "tier_3": "Slower motion allows forces to pull particles closer; mass constant; density increases."
        }
    }


def arch_37_ball_and_ring_apparatus_experiment(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a classic physics demonstration, the 'ball and ring' apparatus is used:\n"
        f"- At room temperature, a brass ball passes easily through a metal ring.\n"
        f"- The brass ball is heated strongly in a Bunsen burner flame for 3 minutes.\n"
        f"- The ball is placed on the ring again, but **cannot pass through the ring**.\n\n"
        f"1. Explain why the heated ball can no longer pass through the ring.\n"
        f"2. What happens if the heated ball is plunged into a beaker of cold water for 10 seconds?\n"
        f"3. How can the ring itself be used to make the hot ball fit through again without cooling the ball?"
    )
    sol = (
        f"**Step 1:** Heating causes **thermal expansion**; the brass atoms vibrate more vigorously and move slightly further apart, increasing the ball's volume and diameter so it is wider than the ring [1 Mark: Ball expansion].\n\n"
        f"**Step 2:** Plunging in cold water causes **thermal contraction**; the ball loses heat, shrinks back to its original size, and passes easily through the ring again [1 Mark: Ball contraction].\n\n"
        f"**Step 3:** By **heating the ring**, the ring will expand, increasing the inner diameter of the hole so the hot ball fits through [1 Mark: Ring expansion]."
    )
    return {
        "id": f"ns8_pmm_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Thermal expansion increases ball diameter; Cold water causes contraction so it fits again; Heat the ring so the hole expands",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "37_ball_and_ring_apparatus_experiment",
        "misconception_tags": ["ball_and_ring_thermal_expansion"],
        "hints": {
            "tier_1": "Heating makes the ball too big to fit; cooling makes it shrink.",
            "tier_2": "Heating the ring makes the hole bigger too.",
            "tier_3": "Thermal expansion increases diameter; cooling contracts it; heating the ring enlarges the hole."
        }
    }


def arch_38_bimetallic_strip_in_thermostats(rng: random.Random) -> Dict[str, Any]:
    strips = [
        ("Brass and Iron", "Brass expands much more than iron when heated", "bends toward the iron side"),
        ("Copper and Steel", "Copper expands faster and more than steel", "bends toward the steel side"),
    ]
    pair, exp_fact, bend_dir = rng.choice(strips)

    prompt = (
        f"A **bimetallic strip** consists of two different metals riveted firmly together: **{pair}** ({exp_fact}).\n\n"
        f"1. Predict what happens to the bimetallic strip when it is heated strongly ({bend_dir}).\n"
        f"2. Explain why the strip bends rather than simply staying straight.\n"
        f"3. Name one practical household appliance that uses a bimetallic strip as a thermostat switch."
    )
    sol = (
        f"**Step 1:** The strip **curves/bends** ({bend_dir}) [1 Mark: Bending observation].\n\n"
        f"**Step 2:** The metal on the outside expands more (becomes longer) than the metal on the inside; because they are bonded together, the differential expansion forces the strip to **bend into a curve** [1 Mark: Differential expansion explanation].\n\n"
        f"**Step 3:** Applications include: electric irons, household geysers, electric kettles, or refrigerator temperature controllers [1 Mark: Appliance]."
    )
    return {
        "id": f"ns8_pmm_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Bends ({bend_dir}); One metal expands more than the other forcing a curve; e.g. electric iron, geyser, or kettle",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "38_bimetallic_strip_in_thermostats",
        "misconception_tags": ["bimetallic_strip_thermostat"],
        "hints": {
            "tier_1": "The metal that expands more becomes longer and pushes the strip into a curve.",
            "tier_2": "Used in irons and geysers to click off when hot.",
            "tier_3": f"Bends ({bend_dir}); different expansion rates cause curving; electric iron/kettle."
        }
    }


def arch_39_engineering_solutions_railway_expansion_gaps(rng: random.Random) -> Dict[str, Any]:
    structures = [
        ("steel railway tracks", "small expansion gaps left between steel rail sections", "tracks buckling and derailing trains in hot weather"),
        ("concrete highway bridges", "interlocking metal comb expansion joints installed across road spans", "concrete expanding, cracking, and crushing itself in summer"),
        ("long steam pipelines in factories", "U-shaped expansion loops built into the pipe runs", "pipes warping and bursting under thermal stress"),
    ]
    struct, solution, disaster = rng.choice(structures)

    prompt = (
        f"Engineers must account for thermal expansion when designing large structures.\n\n"
        f"Consider: **{struct}**.\n\n"
        f"1. What engineering solution is used to handle thermal expansion in this structure ({solution})?\n"
        f"2. What catastrophic failure would happen during summer if engineers neglected thermal expansion ({disaster})?\n"
        f"3. Explain why the risk is greatest during extreme temperature swings between winter nights and summer days."
    )
    sol = (
        f"**Step 1:** Solution: Engineers leave **{solution}** [1 Mark: Engineering design].\n\n"
        f"**Step 2:** Catastrophic failure: {disaster} [1 Mark: Failure].\n\n"
        f"**Step 3:** Large temperature swings cause **maximum differences in expansion and contraction**, exerting enormous thermal stresses and strain on materials [1 Mark: Temperature swing explanation]."
    )
    return {
        "id": f"ns8_pmm_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{solution}; Prevents {disaster}; Large temperature changes cause extreme thermal expansion and stress",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "39_engineering_solutions_railway_expansion_gaps",
        "misconception_tags": ["engineering_expansion_gaps"],
        "hints": {
            "tier_1": "Gaps allow metal/concrete to expand safely without bending.",
            "tier_2": "Without gaps, railway lines buckle in hot sun.",
            "tier_3": f"{solution}; prevents {disaster}; large thermal stress."
        }
    }


def arch_40_overhead_power_lines_seasonal_sagging(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Electrical engineers notice that overhead high-voltage copper/aluminium cables sag significantly closer to the ground on hot summer days, but become tight and straight during cold winter mornings.\n\n"
        f"1. Explain why overhead power lines **sag in hot summer weather**.\n"
        f"2. Explain why they **tighten in cold winter weather**.\n"
        f"3. Why must engineers never string power cables completely tight and straight when installing them during a hot summer day?"
    )
    sol = (
        f"**Step 1:** Summer heat causes **thermal expansion**; metal atoms vibrate more and push apart, making cables longer and causing them to sag [1 Mark: Summer sagging].\n\n"
        f"**Step 2:** Winter cold causes **thermal contraction**; metal atoms move slower and settle closer, shortening the cables and pulling them taut [1 Mark: Winter tightening].\n\n"
        f"**Step 3:** If installed tight in summer, when winter comes the cables will **contract and become too tight, snapping the cables or toppling the pylons/poles** [1 Mark: Engineering warning]."
    )
    return {
        "id": f"ns8_pmm_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Thermal expansion lengthens cables (sagging); Thermal contraction shortens cables (tightening); If tight in summer, winter contraction will snap cables or break poles",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "40_overhead_power_lines_seasonal_sagging",
        "misconception_tags": ["power_lines_expansion_contraction"],
        "hints": {
            "tier_1": "Heat makes wires longer (they sag); cold makes wires shorter (they tighten).",
            "tier_2": "If tight in summer, winter cold will snap them.",
            "tier_3": "Expansion in summer (sag); contraction in winter (tight); avoids snapping in winter."
        }
    }


def arch_41_liquid_expansion_in_thermometers(rng: random.Random) -> Dict[str, Any]:
    liquids = [
        ("red-dyed alcohol", "expands uniformly and freezes at very low temperatures ($-114^\\circ\\text{{C}}$)"),
        ("mercury metal", "silvery liquid metal with a very uniform expansion rate over a wide temperature range"),
    ]
    liq, feature = rng.choice(liquids)

    prompt = (
        f"Traditional liquid-in-glass thermometers use **{liq}** inside a narrow glass capillary tube ({feature}).\n\n"
        f"1. What happens to the liquid inside the thermometer bulb when placed in hot liquid?\n"
        f"2. Explain this phenomenon at a particle level.\n"
        f"3. Why is the capillary tube made extremely narrow instead of wide?"
    )
    sol = (
        f"**Step 1:** The liquid undergoes **thermal expansion** and rises up the capillary tube [1 Mark: Liquid rises].\n\n"
        f"**Step 2:** As heat is absorbed, liquid particles gain kinetic energy, **slide faster, and push slightly further apart**, increasing the liquid's volume [1 Mark: Particle expansion].\n\n"
        f"**Step 3:** A very narrow capillary means a tiny volume increase creates a **large, easily readable rise in liquid height** (high sensitivity) [1 Mark: Narrow bore sensitivity]."
    )
    return {
        "id": f"ns8_pmm_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Liquid expands and rises up capillary; Particles gain kinetic energy and push further apart; Narrow tube gives high sensitivity for small volume changes",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "41_liquid_expansion_in_thermometers",
        "misconception_tags": ["thermometer_liquid_expansion"],
        "hints": {
            "tier_1": "Liquid expands and moves up the tube.",
            "tier_2": "Narrow tube makes tiny expansion easy to see.",
            "tier_3": "Liquid expands and rises; particles push apart; narrow tube increases sensitivity."
        }
    }


# ==============================================================================
# CLUSTER 6: Gas Pressure & Inquiry (42 - 50)
# ==============================================================================

def arch_42_gas_pressure_origin_particle_collisions(rng: random.Random) -> Dict[str, Any]:
    containers = [
        ("inflated bicycle tyre", "air particles pushing outward against the inner rubber walls"),
        ("sealed party balloon", "gas particles colliding with the elastic latex wall"),
        ("metal aerosol can", "gas propellant particles bouncing against the rigid steel walls"),
    ]
    cont, context = rng.choice(containers)

    prompt = (
        f"Consider an **{cont}** ({context}).\n\n"
        f"1. What is the fundamental cause of **gas pressure** inside any container according to the particle model?\n"
        f"2. State the scientific definition of pressure in terms of force and area.\n"
        f"3. Why is gas pressure exerted equally in all directions inside a closed container?"
    )
    sol = (
        f"**Step 1:** Gas pressure is caused by **gas particles continuously colliding with the inner walls of the container**, exerting an outward force with each impact [1 Mark: Collision cause].\n\n"
        f"**Step 2:** Pressure is defined as the **force exerted per unit area** ($P = \\frac{{F}}{{A}}$) [1 Mark: Pressure definition].\n\n"
        f"**Step 3:** Gas particles move **randomly at high speed in all directions**, resulting in an equal rate and force of collisions on all surfaces of the container [1 Mark: Equal in all directions]."
    )
    return {
        "id": f"ns8_pmm_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Particles continuously colliding with container walls; Force per unit area (P = F / A); Particles move randomly in all directions causing equal collisions",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "42_gas_pressure_origin_particle_collisions",
        "misconception_tags": ["gas_pressure_particle_collisions"],
        "hints": {
            "tier_1": "Pressure comes from particles bouncing off the walls.",
            "tier_2": "Pressure = Force / Area.",
            "tier_3": "Collisions with walls; Force per unit area; Random motion in all directions."
        }
    }


def arch_43_gas_pressure_and_number_of_particles(rng: random.Random) -> Dict[str, Any]:
    pumps = rng.choice([2, 3, 4])
    prompt = (
        f"A cyclist uses a bicycle pump to add {pumps} extra pumps of air into a bicycle tyre at constant temperature.\n\n"
        f"1. What happens to the pressure inside the tyre as more air particles are pumped in?\n"
        f"2. Explain this pressure increase in terms of **particle density and collision frequency**.\n"
        f"3. What will happen if someone continues pumping air into the tyre beyond its maximum rated pressure?"
    )
    sol = (
        f"**Step 1:** The pressure inside the tyre **increases** [1 Mark: Pressure change].\n\n"
        f"**Step 2:** Adding more air increases the **number of gas particles in the fixed volume (particle density)**; more particles mean **more frequent collisions** with the tyre walls every second, creating greater force per unit area [1 Mark: Collision frequency].\n\n"
        f"**Step 3:** The tyre will **burst / rupture / explode** when the outward force of collisions exceeds the structural tensile strength of the rubber [1 Mark: Consequence]."
    )
    return {
        "id": f"ns8_pmm_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Pressure increases; More particles mean more frequent collisions with tyre walls; Tyre will burst/explode",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "43_gas_pressure_and_number_of_particles",
        "misconception_tags": ["particle_number_and_pressure"],
        "hints": {
            "tier_1": "More air particles = more collisions = higher pressure.",
            "tier_2": "Too much pressure makes the tyre pop.",
            "tier_3": "Pressure increases; higher collision frequency; tyre bursts."
        }
    }


def arch_44_gas_pressure_and_volume_syringe_compression(rng: random.Random) -> Dict[str, Any]:
    v_start = rng.choice([20, 30, 40])
    v_end = v_start // 2

    # Dynamic SVG showing Syringe before and after compression
    svg = (
        f'<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;border:1px solid #cbd5e1;border-radius:8px;">'
        f'<rect x="10" y="10" width="340" height="180" rx="6" fill="#f8fafc"/>'
        f'<text x="180" y="28" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Syringe Compression Experiment</text>'
        # State A (Large volume)
        f'<rect x="30" y="45" width="130" height="50" rx="2" fill="#e2e8f0" stroke="#334155" stroke-width="1.5"/>'
        f'<rect x="110" y="46" width="15" height="48" fill="#64748b"/>'
        f'<text x="65" y="75" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">V = {v_start} cm³</text>'
        f'<text x="95" y="110" font-family="sans-serif" font-size="10" fill="#475569" text-anchor="middle">Normal Pressure (P₁)</text>'
        # State B (Halved volume)
        f'<rect x="200" y="45" width="130" height="50" rx="2" fill="#e2e8f0" stroke="#334155" stroke-width="1.5"/>'
        f'<rect x="240" y="46" width="15" height="48" fill="#64748b"/>'
        f'<text x="220" y="75" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">V = {v_end} cm³</text>'
        f'<text x="265" y="110" font-family="sans-serif" font-size="10" fill="#dc2626" font-weight="bold" text-anchor="middle">Higher Pressure (2×P₁)</text>'
        f'<text x="180" y="160" font-family="sans-serif" font-size="11" fill="#334155" text-anchor="middle">Decreasing volume increases collision rate</text>'
        f'</svg>'
    )

    prompt = (
        f"A sealed plastic syringe containing trapped air has its volume halved from **${v_start}\\text{{ cm}}^3$** to **${v_end}\\text{{ cm}}^3$** at constant temperature.\n\n"
        f"1. What happens to the air pressure inside the syringe when the volume is halved?\n"
        f"2. Explain this pressure change using the particle model of matter (particle spacing, collision rate).\n"
        f"3. State the relationship between gas volume and pressure at constant temperature (Boyle's Law concept)."
    )
    sol = (
        f"**Step 1:** The air pressure **doubles (increases significantly)** [1 Mark: Pressure change].\n\n"
        f"**Step 2:** Halving the volume crowds the same number of particles into half the space; particles have shorter distances to travel between collisions, causing them to **collide with the walls twice as frequently**, doubling the pressure [1 Mark: Collision explanation].\n\n"
        f"**Step 3:** Volume and pressure are **inversely proportional** (as volume decreases, pressure increases) [1 Mark: Inversely proportional relationship]."
    )
    return {
        "id": f"ns8_pmm_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Pressure doubles (increases); Particles are crowded into smaller space colliding twice as often; Inversely proportional relationship",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "44_gas_pressure_and_volume_syringe_compression",
        "misconception_tags": ["volume_vs_pressure_particles"],
        "diagram_spec": {
            "kind": "inline_svg",
            "svg": svg,
            "diagram_role": "context"
        },
        "hints": {
            "tier_1": "Squashing gas makes particles bump into walls more often.",
            "tier_2": "Half the volume = double the collisions = double the pressure.",
            "tier_3": "Pressure doubles; higher collision rate in smaller space; inversely proportional."
        }
    }


def arch_45_gas_pressure_and_temperature_heating_closed_can(rng: random.Random) -> Dict[str, Any]:
    can_types = [
        ("sealed aerosol deodorant can", "heating in a campfire"),
        ("closed empty metal paint tin", "left on a hot stove"),
        ("tightly sealed glass jar", "placed into an oven"),
    ]
    container, danger_action = rng.choice(can_types)

    prompt = (
        f"A safety warning on a **{container}** strictly forbids **{danger_action}**.\n\n"
        f"1. What happens to the gas pressure inside a sealed rigid container when its temperature increases?\n"
        f"2. Explain this pressure increase using the particle model (kinetic energy, speed, and force of collisions).\n"
        f"3. What dangerous outcome will occur if heating continues?"
    )
    sol = (
        f"**Step 1:** The gas pressure **increases rapidly** [1 Mark: Pressure increase].\n\n"
        f"**Step 2:** Heating increases the **average kinetic energy and speed** of the gas particles; they collide with the walls **more frequently and with much greater force**, generating higher pressure [1 Mark: Speed and force explanation].\n\n"
        f"**Step 3:** The container will violently **explode / burst**, creating flying shrapnel and dangerous fires [1 Mark: Explosion outcome]."
    )
    return {
        "id": f"ns8_pmm_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Pressure increases; Particles move faster colliding more frequently and with greater force; Container explodes/bursts",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "45_gas_pressure_and_temperature_heating_closed_can",
        "misconception_tags": ["temperature_vs_gas_pressure"],
        "hints": {
            "tier_1": "Hot particles move faster and hit walls harder.",
            "tier_2": "Higher temperature = more frequent and harder collisions.",
            "tier_3": "Pressure increases; faster particles hit walls harder/more often; container explodes."
        }
    }


def arch_46_atmospheric_pressure_and_altitude_trends(rng: random.Random) -> Dict[str, Any]:
    cities = [
        ("Durban (sea level, $0\\text{{ m}}$)", "Johannesburg (high altitude, $1\\,753\\text{{ m}}$)"),
        ("Cape Town (sea level, $0\\text{{ m}}$)", "Pretoria (high altitude, $1\\,339\\text{{ m}}$)"),
    ]
    sea, high = rng.choice(cities)

    prompt = (
        f"Atmospheric pressure changes significantly with altitude across South Africa:\n"
        f"**{sea}** vs **{high}**.\n\n"
        f"1. Which location experiences **higher atmospheric pressure**?\n"
        f"2. Explain why atmospheric pressure decreases as altitude increases using the particle model and gravity.\n"
        f"3. Why does water boil at a slightly lower temperature (e.g. $95^\\circ\\text{{C}}$) in {high.split(' (')[0]} than at sea level ($100^\\circ\\text{{C}}$)?"
    )
    sol = (
        f"**Step 1:** **{sea.split(' (')[0]} (sea level)** experiences higher atmospheric pressure [1 Mark: Higher pressure location].\n\n"
        f"**Step 2:** Earth's gravity pulls air particles down toward the surface; at sea level, there is a **taller column of air particles above**, creating greater weight and particle density, whereas at higher altitudes there are fewer air particles above [1 Mark: Altitude explanation].\n\n"
        f"**Step 3:** Lower atmospheric pressure means escaping water vapor molecules face **less downward resistance/pressure from the air**, allowing boiling bubbles to form at lower kinetic energies (lower temperature) [1 Mark: Lower boiling point explanation]."
    )
    return {
        "id": f"ns8_pmm_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{sea.split(' (')[0]}; Gravity pulls air particles down so sea level has taller column of particles above; Lower air pressure provides less resistance to boiling",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "46_atmospheric_pressure_and_altitude_trends",
        "misconception_tags": ["atmospheric_pressure_altitude"],
        "hints": {
            "tier_1": "Air is thickest at sea level and thinner on high mountains.",
            "tier_2": "Fewer air molecules pushing down means lower boiling point.",
            "tier_3": "Sea level is higher pressure; fewer air particles above at high altitude; water boils at lower temp."
        }
    }


def arch_47_crushing_can_experiment_implosion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In the dramatic 'crushing can' experiment:\n"
        f"1. A small amount of water is boiled inside an empty aluminium soda can until steam shoots out of the opening.\n"
        f"2. Using tongs, the can is quickly inverted upside-down into a bowl of ice-cold water.\n"
        f"3. Instantly, with a loud CRUNCH, the aluminium can is violently crushed inward!\n\n"
        f"1. What did the boiling steam do to the air originally inside the can?\n"
        f"2. What happened to the steam inside the can when inverted into cold water?\n"
        f"3. Explain what crushed the can (contrast inside pressure with outside atmospheric pressure)."
    )
    sol = (
        f"**Step 1:** The expanding steam **pushed out almost all the air** from inside the can [1 Mark: Air displaced].\n\n"
        f"**Step 2:** The cold water instantly **condensed the steam back into liquid water droplets**, which occupy thousands of times less volume, creating a **near-vacuum (extremely low pressure)** inside the sealed can [1 Mark: Steam condensation and vacuum].\n\n"
        f"**Step 3:** The **huge external atmospheric pressure pushing on the outside** of the can was far greater than the near-zero pressure inside, crushing the can inward instantly [1 Mark: Pressure difference crushed can]."
    )
    return {
        "id": f"ns8_pmm_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Steam pushed air out; Steam condensed to liquid creating a vacuum (low pressure); External atmospheric pressure crushed the can",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "47_crushing_can_experiment_implosion",
        "misconception_tags": ["crushing_can_atmospheric_pressure"],
        "hints": {
            "tier_1": "Cold water makes steam turn back into a few drops of water.",
            "tier_2": "This creates a vacuum inside, and the huge air pressure outside crushes it.",
            "tier_3": "Steam pushes air out; steam condenses creating vacuum; external air pressure crushes can."
        }
    }


def arch_48_evaluating_gas_pressure_data_table(rng: random.Random) -> Dict[str, Any]:
    readings = [
        (10, 100), (20, 200), (30, 300), (40, 400),
    ]
    p_factor = rng.choice([2, 5, 10])

    prompt = (
        f"A student measures the gas pressure inside a rigid sealed flask at different temperatures:\n"
        f"- At $10^\\circ\\text{{C}}$: Pressure = ${10 * p_factor}\\text{{ kPa}}$\n"
        f"- At $20^\\circ\\text{{C}}$: Pressure = ${20 * p_factor}\\text{{ kPa}}$\n"
        f"- At $30^\\circ\\text{{C}}$: Pressure = ${30 * p_factor}\\text{{ kPa}}$\n"
        f"- At $40^\\circ\\text{{C}}$: Pressure = ${40 * p_factor}\\text{{ kPa}}$\n\n"
        f"1. Describe the mathematical trend shown by this data.\n"
        f"2. Predict the expected pressure at **$50^\\circ\\text{{C}}$**.\n"
        f"3. Explain why the volume of the gas remained constant throughout this experiment."
    )
    sol = (
        f"**Step 1:** As temperature increases, gas pressure **increases directly / proportionally** [1 Mark: Trend].\n\n"
        f"**Step 2:** At $50^\\circ\\text{{C}}$, expected pressure = **${50 * p_factor}\\text{{ kPa}}$** [1 Mark: Prediction].\n\n"
        f"**Step 3:** The volume remained constant because the container is a **rigid, sealed glass/metal flask** that cannot expand [1 Mark: Constant volume explanation]."
    )
    return {
        "id": f"ns8_pmm_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Pressure increases directly with temperature; Predicted: {50 * p_factor} kPa; Rigid sealed flask prevents volume change",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "48_evaluating_gas_pressure_data_table",
        "misconception_tags": ["gas_pressure_data_evaluation"],
        "hints": {
            "tier_1": "Look at the pattern: each 10 degrees adds the same pressure.",
            "tier_2": f"At 50°C, it will be {50 * p_factor} kPa.",
            "tier_3": f"Direct trend; {50 * p_factor} kPa; rigid flask."
        }
    }


def arch_49_misconceptions_particles_expand_vs_spaces_expand(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner writes in a test: *'When a metal rod expands in the sun, it gets longer because each copper atom swells up and grows bigger.'*\n\n"
        f"1. Is this learner's statement scientifically correct? (Yes or No)\n"
        f"2. Correct the learner's statement using the particle model of matter.\n"
        f"3. Why is it essential to distinguish between the properties of individual particles and the properties of the bulk substance?"
    )
    sol = (
        f"**Step 1:** **No**, the statement is completely incorrect [1 Mark: Yes/No].\n\n"
        f"**Step 2:** Correction: Individual atoms **never change size, expand, or swell**; when heated, atoms vibrate more vigorously and **push further apart from each other, increasing the empty spaces between them** [1 Mark: Particle model correction].\n\n"
        f"**Step 3:** Properties like temperature, expansion, color, and density are **bulk properties of billions of particles interacting**, not properties of an isolated single particle [1 Mark: Bulk vs Particle distinction]."
    )
    return {
        "id": f"ns8_pmm_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "No; Atoms do not expand, they vibrate faster and push further apart increasing empty spaces; Expansion is a bulk property of particle spacing",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "49_misconceptions_particles_expand_vs_spaces_expand",
        "misconception_tags": ["atoms_do_not_expand_misconception"],
        "hints": {
            "tier_1": "Atoms never get fat! They just push their neighbors away.",
            "tier_2": "The space between atoms increases, not the atoms themselves.",
            "tier_3": "No; atoms stay same size, spaces between them increase; bulk property."
        }
    }


def arch_50_particle_model_master_synthesis_challenge(rng: random.Random) -> Dict[str, Any]:
    mass = rng.choice([200, 300, 400])
    vol = rng.choice([40, 50, 80])
    dens = round(mass / vol, 2)
    dens_str = str(dens).replace(".", ",")

    prompt = (
        f"Complete the comprehensive Grade 8 Particle Model of Matter synthesis review:\n\n"
        f"1. **Density Problem:** A block of metal has mass ${mass}\\text{{ g}}$ and volume ${vol}\\text{{ cm}}^3$. Calculate its density and state if it will float or sink in water (density $1,0\\text{{ g/cm}}^3$).\n"
        f"2. **State Changes:** Name the phase change where gas turns directly to liquid, and explain what happens to particle kinetic energy.\n"
        f"3. **Thermal Expansion:** Explain why a thermometer liquid rises when warmed (address particle size vs particle spacing).\n"
        f"4. **Gas Pressure:** Explain why heating a closed aerosol can causes its pressure to increase."
    )
    sol = (
        f"**Step 1:** Density $\\rho = \\frac{{{mass}}}{{{vol}}} = \\mathbf{{{dens_str}\\text{{ g/cm}}^3}}$; it will **sink** because ${dens_str} > 1,0\\text{{ g/cm}}^3$ [2 Marks: Density & Sinking].\n\n"
        f"**Step 2:** **Condensation**; particles **lose kinetic energy** and move slower, allowing attractive forces to pull them together [1 Mark: Condensation].\n\n"
        f"**Step 3:** Particles **do not change size**; they vibrate/move faster and **push slightly further apart**, increasing the liquid volume so it rises up the tube [1 Mark: Liquid expansion].\n\n"
        f"**Step 4:** Heating gives particles **higher kinetic energy/speed**, causing **more frequent and forceful collisions** against the container walls, increasing pressure [1 Mark: Gas pressure]."
    )
    return {
        "id": f"ns8_pmm_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Density = {dens_str} g/cm3 (sinks); Condensation (particles lose KE); Particles push further apart (size unchanged); Particles move faster colliding harder with walls",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 5,
        "term": 2,
        "subskill": "50_particle_model_master_synthesis_challenge",
        "misconception_tags": ["particle_model_master_synthesis"],
        "hints": {
            "tier_1": f"Density = {mass} / {vol}. Compare to 1.0 g/cm3.",
            "tier_2": "Gas to liquid = condensation. Expansion = spaces increase.",
            "tier_3": f"{dens_str} g/cm3 (sinks); Condensation; spacing increases; collisions increase."
        }
    }
