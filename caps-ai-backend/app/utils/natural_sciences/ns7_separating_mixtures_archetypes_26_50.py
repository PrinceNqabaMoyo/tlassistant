"""
Grade 7 Natural Sciences - Term 2: Separating Mixtures (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/PDF - Separating mixtures.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Fractional Distillation & Chromatography (26 - 34)
# ==============================================================================

def arch_26_fractional_distillation_differing_boiling_points(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("pure ethanol", 78, "water", 100),
        ("acetone", 56, "water", 100),
        ("methanol", 65, "ethanol", 78),
    ]
    sub1, bp1, sub2, bp2 = rng.choice(pairs)

    prompt = (
        f"A chemist separates a miscible liquid mixture containing {sub1} (boiling point ${bp1}^\\circ\\text{{C}}$) "
        f"and {sub2} (boiling point ${bp2}^\\circ\\text{{C}}$) using **fractional distillation**.\n\n"
        f"1. Which liquid distills over first into the collecting flask? Justify your choice.\n"
        f"2. What temperature will the thermometer at the top of the fractionating column read while this first liquid is collecting?\n"
        f"3. Explain why simple distillation cannot cleanly separate liquids with close boiling points."
    )
    sol = (
        f"**Step 1:** **{sub1}** distills over first because it has the **lower boiling point** (${bp1}^\\circ\\text{{C}}$ vs ${bp2}^\\circ\\text{{C}}$) [1 Mark: First distillate].\n\n"
        f"**Step 2:** The thermometer reads steady at **${bp1}^\\circ\\text{{C}}$** during collection of the first fraction [1 Mark: Thermometer plateau].\n\n"
        f"**Step 3:** Without a fractionating column, vapours of both liquids mix and condense together, yielding an impure distillate [1 Mark: Column rationale]."
    )
    return {
        "id": f"ns7_sep_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{sub1} distills first; {bp1} °C; vapours of both would mix and condense together without fractionating column",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "26_fractional_distillation_differing_boiling_points",
        "misconception_tags": ["boiling_point_fraction_order"],
        "hints": {
            "tier_1": "Lower boiling point boils and distills first.",
            "tier_2": f"{sub1} boils at {bp1} °C, which is lower than {bp2} °C.",
            "tier_3": f"{sub1} distills first at {bp1} °C."
        }
    }


def arch_27_fractional_distillation_crude_oil(rng: random.Random) -> Dict[str, Any]:
    fractions = [
        ("Refinery Gas (LPG)", "lowest boiling point (< 20 °C)", "bottled gas for camping stoves and domestic heating"),
        ("Petrol / Gasoline", "low boiling point (40 - 100 °C)", "fuel for light motor cars"),
        ("Paraffin / Kerosene", "medium boiling point (150 - 250 °C)", "fuel for jet aircraft and domestic paraffin heaters"),
        ("Diesel oil", "high boiling point (250 - 350 °C)", "fuel for heavy trucks, buses, and trains"),
        ("Bitumen / Asphalt", "highest boiling point (> 400 °C, collected at base)", "tar surfacing for tarmac roads and waterproofing roofs"),
    ]
    f1, f2 = rng.sample(fractions, 2)

    prompt = (
        f"Crude oil (petroleum) is a dark, viscous mixture of hydrocarbons separated in a refinery fractionating tower.\n\n"
        f"Consider two fractions:\n"
        f"- Fraction A: {f1[0]}\n"
        f"- Fraction B: {f2[0]}\n\n"
        f"1. Explain how a fractionating tower uses a temperature gradient (hot at the bottom, cooler at the top) to separate these fractions.\n"
        f"2. State the typical commercial use of **{f1[0]}**: {f1[2]}."
    )
    sol = (
        f"**Step 1:** Crude oil is vaporised at the bottom of the tower. As vapours rise, they cool; fractions with higher boiling points condense early near the hot bottom, while fractions with lower boiling points rise near the cool top before condensing [1 Mark: Tower gradient].\n\n"
        f"**Step 2:** Use of {f1[0]}: **{f1[2]}** [1 Mark: Application]."
    )
    return {
        "id": f"ns7_sep_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Rising vapours cool along gradient condensing at specific boiling points; {f1[0]}: {f1[2]}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "27_fractional_distillation_crude_oil",
        "misconception_tags": ["fractionating_column_gradient"],
        "hints": {
            "tier_1": "The tower is hottest at the bottom and cooler at the top.",
            "tier_2": "Vapours condense at trays matching their boiling points.",
            "tier_3": f"Vapours condense along temperature gradient; {f1[0]} is used for {f1[2]}."
        }
    }


def arch_28_fractionating_column_condensation_cycles(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A fractionating column is packed with glass beads or metal rings.\n\n"
        f"1. What is the physical purpose of the glass beads inside the fractionating column?\n"
        f"2. Explain how repeated cycles of **condensation and re-evaporation** inside the column produce a much purer distillate than simple distillation."
    )
    sol = (
        f"**Step 1:** The glass beads provide a **large internal surface area** for rising vapours to condense upon [1 Mark: Surface area].\n\n"
        f"**Step 2:** Rising vapor condenses on cooler beads lower down, and rising hot vapor from below re-heats and re-evaporates it. With each cycle, the vapor becomes richer in the more volatile component (lower boiling point), ensuring a pure separation [2 Marks: Repeated equilibrium cycles]."
    )
    return {
        "id": f"ns7_sep_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Provides large surface area; repeated condensation and re-evaporation cycles progressively enrich the more volatile vapour",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "28_fractionating_column_condensation_cycles",
        "misconception_tags": ["fractionating_column_bead_purpose"],
        "hints": {
            "tier_1": "Glass beads give extra surface area for vapor to condense on.",
            "tier_2": "Each condensation and boiling step purifies the vapor further.",
            "tier_3": "Provides surface area for repeated condensation and re-boiling."
        }
    }


def arch_29_paper_chromatography_baseline_pencil(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When preparing a paper chromatography strip to test a dye mixture, a learner marks a starting baseline $1{{,}}5\\text{{ cm}}$ from the bottom edge.\n\n"
        f"1. State which writing tool MUST be used to mark this baseline (graphite pencil or ballpoint ink pen).\n"
        f"2. Explain why using a ballpoint pen or felt-tip marker to mark the baseline would completely ruin the experiment."
    )
    sol = (
        f"**Step 1:** The baseline must be marked in **graphite pencil** [1 Mark: Instrument].\n\n"
        f"**Step 2:** Ink from a pen is soluble in the solvent and would itself dissolve, separate into colored pigments, travel up the paper, and contaminate the test sample [1 Mark: Scientific explanation]."
    )
    return {
        "id": f"ns7_sep_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Graphite pencil; pen ink dissolves in solvent, separates into dyes, and ruins/contaminates the chromatogram",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "29_paper_chromatography_baseline_pencil",
        "misconception_tags": ["pencil_baseline_rule"],
        "hints": {
            "tier_1": "Does graphite pencil lead dissolve in water/alcohol?",
            "tier_2": "Graphite is insoluble, but pen ink dissolves and spreads.",
            "tier_3": "Graphite pencil; pen ink would dissolve and separate."
        }
    }


def arch_30_paper_chromatography_solvent_level(rng: random.Random) -> Dict[str, Any]:
    d_line = rng.choice([1.5, 2.0])
    d_solv = d_line - rng.choice([0.5, 1.0])

    prompt = (
        f"A learner draws a pencil baseline at ${str(d_line).replace('.', ',')}\\text{{ cm}}$ from the bottom of a chromatography paper strip and spots a drop of black ink onto it.\n"
        f"The strip is hung vertically inside a beaker containing solvent.\n\n"
        f"1. Explain why the depth of solvent in the beaker (e.g. ${str(d_solv).replace('.', ',')}\\text{{ cm}}$) must be **strictly below the pencil line**.\n"
        f"2. What disaster would occur if the solvent level submerged the ink spot?"
    )
    sol = (
        f"**Step 1:** The solvent must be below the line so the solvent rises upwards past the spot through **capillary action** [1 Mark: Capillary action].\n\n"
        f"**Step 2:** If submerged, the ink spot would dissolve directly into the pool of solvent in the beaker and wash away, rather than travelling up the paper [1 Mark: Washout error]."
    )
    return {
        "id": f"ns7_sep_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Solvent must rise by capillary action; if submerged the ink spot dissolves directly into the beaker solvent and washes away",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "30_paper_chromatography_solvent_level",
        "misconception_tags": ["solvent_depth_chromatography"],
        "hints": {
            "tier_1": "What happens if you dip an ink spot directly into a pool of water?",
            "tier_2": "The ink dissolves into the water beaker and is washed away.",
            "tier_3": "Solvent must rise through capillary action; submerging washes ink into beaker."
        }
    }


def arch_31_paper_chromatography_pigment_separation(rng: random.Random) -> Dict[str, Any]:
    pigments = [
        ("chlorophyll a (blue-green)", "chlorophyll b (yellow-green)", "carotene (orange)"),
        ("tartrazine (yellow)", "erythrosine (red)", "brilliant blue (blue)"),
        ("rhodamine (magenta)", "fluorescein (yellow)", "cyan dye (cyan)"),
    ]
    p1, p2, p3 = rng.choice(pigments)

    prompt = (
        f"In paper chromatography, a solvent moves up cellulose paper via capillary action, carrying different dyes ({p1}, {p2}, and {p3}) at different speeds.\n\n"
        f"1. Explain the TWO competing physical forces/factors that determine how far a pigment travels:\n"
        f"   - Factor A: Solubility in the mobile phase (solvent).\n"
        f"   - Factor B: Affinity (adhesion) to the stationary phase (paper).\n"
        f"2. If {p3} travels closest to the solvent front, what does this indicate about its solubility relative to the other dyes?"
    )
    sol = (
        f"**Step 1:**\n"
        f"- Factor A: Pigments that are **more soluble** in the solvent spend more time moving with the liquid [1 Mark: Solubility].\n"
        f"- Factor B: Pigments with **weaker attraction** to the cellulose paper fibres move faster, whereas pigments strongly attracted to the paper are held back [1 Mark: Paper affinity].\n\n"
        f"**Step 2:** {p3} has the **highest solubility in the solvent** (and lowest affinity for the paper) among all three dyes [1 Mark: Fast traveler]."
    )
    return {
        "id": f"ns7_sep_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Solubility in solvent vs attraction to paper fibres; highest solubility in solvent travels furthest",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "31_paper_chromatography_pigment_separation",
        "misconception_tags": ["solubility_vs_adsorption"],
        "hints": {
            "tier_1": "More soluble dyes travel further with the liquid.",
            "tier_2": "Dyes attracted strongly to paper move slowly.",
            "tier_3": "Solubility in solvent vs attraction to paper; highest solubility travels furthest."
        }
    }


def arch_32_paper_chromatography_interpreting_spots(rng: random.Random) -> Dict[str, Any]:
    ink_choice = rng.choice(["Black Ink X", "Green Ink Y", "Brown Ink Z"])
    num_spots = rng.choice([2, 3])
    colors = [("#3b82f6", "Blue"), ("#eab308", "Yellow"), ("#ef4444", "Red")][:num_spots]
    y_coords = [110, 70, 40][:num_spots]

    svg_spots = "".join(
        f'<circle cx="180" cy="{y}" r="6" fill="{c[0]}"/><text x="200" y="{y+4}" font-family="sans-serif" font-size="10" fill="{c[0]}">{c[1]} spot</text>'
        for y, c in zip(y_coords, colors)
    )

    svg = (
        f'<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<rect x="140" y="20" width="80" height="160" fill="#f8fafc" stroke="#334155" stroke-width="2"/>'
        f'<line x1="145" y1="150" x2="215" y2="150" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>'
        f'<text x="130" y="153" font-family="sans-serif" font-size="9" fill="#64748b" text-anchor="end">Pencil line</text>'
        f'<line x1="145" y1="30" x2="215" y2="30" stroke="#0284c7" stroke-width="1.5"/>'
        f'<text x="130" y="33" font-family="sans-serif" font-size="9" fill="#0284c7" text-anchor="end">Solvent front</text>'
        f'{svg_spots}'
        f'<text x="180" y="170" font-family="sans-serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">{ink_choice}</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": f"Paper chromatogram developed for {ink_choice}",
        "diagram_role": "context"
    }

    color_names = " and ".join([c[1].lower() for c in colors])
    prompt = (
        f"A learner develops a paper chromatogram of **{ink_choice}**.\n\n"
        f"1. Is {ink_choice} a pure substance or a mixture? Justify using the chromatogram.\n"
        f"2. How many distinct dye pigments are present in this ink?\n"
        f"3. Name the colors of the separated spots ({color_names})."
    )
    sol = (
        f"**Step 1:** {ink_choice} is a **mixture** because it separates into multiple distinct colored spots along the strip [1 Mark: Classification].\n\n"
        f"**Step 2:** There are **{num_spots} distinct dye pigments** [1 Mark: Spot count].\n\n"
        f"**Step 3:** The separated pigments are **{color_names}** [1 Mark: Observation]."
    )
    return {
        "id": f"ns7_sep_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Mixture; {num_spots} pigments ({color_names})",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "32_paper_chromatography_interpreting_spots",
        "misconception_tags": ["chromatogram_pure_vs_mixture"],
        "hints": {
            "tier_1": "Multiple spots mean a mixture; a single spot means a pure substance.",
            "tier_2": f"Count the spots: there are {num_spots}.",
            "tier_3": f"Mixture; {num_spots} pigments."
        }
    }


def arch_33_paper_chromatography_forensic_ink_match(rng: random.Random) -> Dict[str, Any]:
    suspects = ["Pen 1 (Suspect A)", "Pen 2 (Suspect B)", "Pen 3 (Suspect C)"]
    culprit = rng.choice(suspects)
    spots_match = rng.choice(["two identical spots (blue and red at matching heights)", "three identical spots (yellow, red, blue at matching heights)"])

    prompt = (
        f"Forensic detectives analyze a handwritten ransom note found at a crime scene.\n"
        f"They extract the black ink and compare its chromatogram with ink samples from three suspects' pens (Pen 1, Pen 2, and Pen 3).\n\n"
        f"The chromatogram of the ransom note ink reveals {spots_match}.\n"
        f"Only {culprit} produces the exact same spot pattern and travel distances.\n\n"
        f"1. Which suspect's pen was used to write the ransom note?\n"
        f"2. Explain why two matching chromatograms provide strong scientific evidence of a match."
    )
    sol = (
        f"**Step 1:** The note was written with **{culprit}** [1 Mark: Identification].\n\n"
        f"**Step 2:** Each ink manufacturer uses a unique proprietary combination of specific dye molecules with characteristic solubilities and travel distances; identical spot numbers, colors, and heights confirm the same chemical formulation [1 Mark: Forensic explanation]."
    )
    return {
        "id": f"ns7_sep_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{culprit}; unique spot pattern, colors, and travel distances match proprietary formulation",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "33_paper_chromatography_forensic_ink_match",
        "misconception_tags": ["forensic_chromatography_matching"],
        "hints": {
            "tier_1": "Match the spot heights and colors.",
            "tier_2": f"{culprit} has the identical spot profile.",
            "tier_3": f"{culprit} matches."
        }
    }


def arch_34_paper_chromatography_retention_factor_rf(rng: random.Random) -> Dict[str, Any]:
    d_solv = rng.choice([80, 100])
    d_dye = rng.choice([20, 40, 60, 75])
    rf = d_dye / d_solv

    prompt = (
        f"On a paper chromatogram strip:\n"
        f"- The distance travelled by the solvent front from the baseline is ${d_solv}\\text{{ mm}}$.\n"
        f"- The distance travelled by a yellow dye spot from the baseline is ${d_dye}\\text{{ mm}}$.\n\n"
        f"1. Calculate the Retention Factor ($R_f$) for the yellow dye ($R_f = \\frac{{\\text{{distance moved by substance}}}}{{\\text{{distance moved by solvent front}}}}$).\n"
        f"2. Can an $R_f$ value ever be greater than $1{{,}}0$? Explain."
    )
    sol = (
        f"**Step 1:** $$R_f = \\frac{{{d_dye}}}{{{d_solv}}} = \\mathbf{{{str(rf).replace('.', ',')}}} \\text{{ [1 Mark: Calculation]}}$$\n\n"
        f"**Step 2:** **No.** A dissolved solute is carried by the moving solvent, so it can never travel further than the solvent front itself; the maximum possible $R_f$ is $1{{,}}0$ [1 Mark: Limit explanation]."
    )
    return {
        "id": f"ns7_sep_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Rf = {str(rf).replace('.', ',')}; No, solute cannot travel further than solvent front",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "34_paper_chromatography_retention_factor_rf",
        "misconception_tags": ["rf_value_bounds"],
        "hints": {
            "tier_1": "Divide distance moved by dye by distance moved by solvent.",
            "tier_2": f"{d_dye} / {d_solv} = {rf}.",
            "tier_3": f"Rf = {rf}; cannot exceed 1.0."
        }
    }


# ==============================================================================
# CLUSTER 5: Multi-Step Separation & Water Purification (35 - 42)
# ==============================================================================

def arch_35_separating_funnel_immiscible_liquids(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("cooking oil and water", "cooking oil", "#facc15", "tap water", "#38bdf8", "water (denser)"),
        ("kerosene (paraffin) and water", "paraffin", "#fde047", "tap water", "#38bdf8", "water (denser)"),
        ("benzene and water", "benzene", "#fed7aa", "salt water", "#0284c7", "salt water (denser)"),
    ]
    mix_name, top_liq, top_col, btm_liq, btm_col, drained = rng.choice(pairs)

    svg = (
        f'<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<line x1="80" y1="20" x2="80" y2="200" stroke="#334155" stroke-width="4"/>'
        f'<line x1="80" y1="70" x2="140" y2="70" stroke="#64748b" stroke-width="3"/>'
        f'<path d="M 150,30 L 210,30 L 220,90 Q 200,140 183,160 L 183,180 L 177,180 L 177,160 Q 160,140 140,90 Z" fill="none" stroke="#0284c7" stroke-width="2"/>'
        f'<path d="M 150,30 L 210,30 L 220,90 L 140,90 Z" fill="{top_col}" opacity="0.7"/>'
        f'<path d="M 140,90 L 220,90 Q 200,140 183,160 L 177,160 Q 160,140 140,90 Z" fill="{btm_col}" opacity="0.6"/>'
        f'<circle cx="180" cy="170" r="5" fill="#ef4444"/>'
        f'<rect x="155" y="195" width="50" height="20" fill="none" stroke="#475569" stroke-width="1.5"/>'
        f'<text x="235" y="65" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a">Top layer: {top_liq}</text>'
        f'<text x="235" y="125" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a">Bottom layer: {btm_liq}</text>'
        f'<text x="235" y="173" font-family="sans-serif" font-size="10" fill="#ef4444">Stopcock tap</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": f"Separating funnel containing {mix_name}",
        "diagram_role": "context"
    }

    prompt = (
        f"A mixture of **{mix_name}** is poured into a separating funnel and allowed to stand.\n\n"
        f"1. Explain why the two liquids separate into distinct layers rather than dissolving into each other.\n"
        f"2. Explain which liquid drains out of the funnel first when the stopcock tap is opened.\n"
        f"3. Describe how the operator knows when to close the tap to achieve clean separation."
    )
    sol = (
        f"**Step 1:** The liquids are **immiscible** (insoluble in each other) and have different densities [1 Mark: Immiscibility].\n\n"
        f"**Step 2:** The **{btm_liq}** drains first because it is denser and sits at the bottom of the funnel [1 Mark: Density order].\n\n"
        f"**Step 3:** The operator watches the interface line between the two liquids and closes the tap the instant the boundary line reaches the stopcock [1 Mark: Operation technique]."
    )
    return {
        "id": f"ns7_sep_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Immiscible with different densities; {btm_liq} drains first; close tap when liquid boundary line reaches stopcock",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "35_separating_funnel_immiscible_liquids",
        "misconception_tags": ["separating_funnel_operation"],
        "hints": {
            "tier_1": "Denser liquid is at the bottom and drains first.",
            "tier_2": f"Bottom layer is {btm_liq}.",
            "tier_3": f"Immiscible liquids; {btm_liq} drains first; close tap at interface."
        }
    }


def arch_36_multi_step_separation_sand_salt_water(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A beaker contains a dry solid mixture of coarse beach sand and fine table salt crystals.\n\n"
        f"Describe a step-by-step scientific method to completely separate this mixture into dry sand and dry salt crystals.\n"
        f"Include:\n"
        f"1. Step 1: Adding water and stirring.\n"
        f"2. Step 2: Filtration.\n"
        f"3. Step 3: Evaporation."
    )
    sol = (
        f"**Step 1:** Add warm water to the mixture and stir thoroughly so that all the salt dissolves to form a saltwater solution, while the insoluble sand remains solid [1 Mark: Dissolution].\n\n"
        f"**Step 2:** Pour the mixture through a filter funnel lined with filter paper; the sand is collected as the **residue** on the filter paper, rinsed with distilled water, and dried in the sun [1 Mark: Filtration].\n\n"
        f"**Step 3:** Heat the clear saltwater **filtrate** in an evaporating dish until all water evaporates, leaving dry white salt crystals [1 Mark: Evaporation]."
    )
    return {
        "id": f"ns7_sep_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. Dissolve salt in water, 2. Filter sand as residue, 3. Evaporate filtrate to recover salt crystals",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "36_multi_step_separation_sand_salt_water",
        "misconception_tags": ["multi_step_separation_logic"],
        "hints": {
            "tier_1": "Salt dissolves in water, sand does not.",
            "tier_2": "Add water -> filter out sand -> boil water away to leave salt.",
            "tier_3": "Dissolve in water, filter sand, evaporate saltwater."
        }
    }


def arch_37_multi_step_separation_iron_salt_sand(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A laboratory spill results in a three-component dry solid mixture: **iron filings, sand, and salt**.\n\n"
        f"1. Name the separation technique used first to extract the iron filings.\n"
        f"2. Name the separation technique used second to separate the sand.\n"
        f"3. Name the separation technique used third to recover the pure salt crystals.\n"
        f"4. Why must magnetic separation be done BEFORE adding water?"
    )
    sol = (
        f"**Step 1:** First: **Magnetic separation** using a bar magnet to pull out all iron filings [1 Mark: Step 1].\n\n"
        f"**Step 2:** Second: Add water to dissolve salt, then **filtration** to collect sand as residue [1 Mark: Step 2].\n\n"
        f"**Step 3:** Third: **Evaporation (or crystallization)** of the filtrate to recover salt [1 Mark: Step 3].\n\n"
        f"**Step 4:** Wet iron filings rust rapidly in saltwater, and wet iron particles cling to wet sand, making clean magnetic separation difficult [1 Mark: Order justification]."
    )
    return {
        "id": f"ns7_sep_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. Magnetic separation, 2. Filtration (after dissolving), 3. Evaporation; wet iron rusts and clumps with sand",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "term": 2,
        "subskill": "37_multi_step_separation_iron_salt_sand",
        "misconception_tags": ["order_of_separation_steps"],
        "hints": {
            "tier_1": "Take out magnetic iron first while dry.",
            "tier_2": "Then add water to dissolve salt, filter sand, evaporate salt.",
            "tier_3": "1. Magnet, 2. Filtration, 3. Evaporation."
        }
    }


def arch_38_separating_sawdust_and_sand_flotation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A carpenter drops wood shavings and sawdust into a bucket of builders' sand.\n\n"
        f"1. Explain how adding the mixture to a large bucket of water allows easy separation by **flotation**.\n"
        f"2. Relate the behaviour of sawdust and sand to their respective densities relative to water ($1{{,}}0\\text{{ g/cm}}^3$).\n"
        f"3. How is the floating sawdust removed from the top?"
    )
    sol = (
        f"**Step 1:** When tipped into water, the mixture separates into two levels based on density [1 Mark: Flotation].\n\n"
        f"**Step 2:** Sand is much denser than water (density $\\approx 2{{,}}6\\text{{ g/cm}}^3$) and sinks quickly to the bottom, whereas wood sawdust is less dense than water (density $\\approx 0{{,}}4 - 0{{,}}6\\text{{ g/cm}}^3$) and floats on the surface [1 Mark: Density comparison].\n\n"
        f"**Step 3:** The floating sawdust can be skimmed off the top using a sieve or slotted spoon [1 Mark: Skimming]."
    )
    return {
        "id": f"ns7_sep_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Sawdust floats while sand sinks; sand is denser than water, sawdust is less dense; skimmed off with sieve",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "38_separating_sawdust_and_sand_flotation",
        "misconception_tags": ["density_flotation_separation"],
        "hints": {
            "tier_1": "Does wood float or sink? Does sand float or sink?",
            "tier_2": "Wood floats (less dense); sand sinks (denser).",
            "tier_3": "Flotation: sawdust floats, sand sinks; skim sawdust."
        }
    }


def arch_39_water_purification_municipal_steps(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Municipal water purification plants (e.g. Rand Water or Umgeni Water) treat raw river water to make it safe for drinking.\n\n"
        f"Place the following five water purification stages in the correct chronological order from first to last:\n"
        f"- Filtration through sand and gravel beds\n"
        f"- Disinfection / Chlorination\n"
        f"- Coagulation / Flocculation (adding alum)\n"
        f"- Coarse metal screening (bar screens)\n"
        f"- Sedimentation in large settling tanks"
    )
    sol = (
        f"**Step 1:** Correct chronological sequence:\n"
        f"1. **Coarse metal screening** (removes large floating debris, branches, plastics) [1 Mark]\n"
        f"2. **Coagulation / Flocculation** (chemicals bind tiny clay particles) [1 Mark]\n"
        f"3. **Sedimentation** (flocs settle to tank bottom) [1 Mark]\n"
        f"4. **Filtration** (passes through sand/gravel beds) [1 Mark]\n"
        f"5. **Disinfection / Chlorination** (kills germs/bacteria before distribution) [1 Mark]"
    )
    return {
        "id": f"ns7_sep_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. Screening, 2. Coagulation/Flocculation, 3. Sedimentation, 4. Filtration, 5. Chlorination",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "39_water_purification_municipal_steps",
        "misconception_tags": ["water_treatment_sequence"],
        "hints": {
            "tier_1": "Start with big objects, end with killing microscopic germs.",
            "tier_2": "Screening -> Flocculation -> Settling -> Sand filtration -> Chlorine.",
            "tier_3": "1. Screening, 2. Flocculation, 3. Sedimentation, 4. Filtration, 5. Chlorination."
        }
    }


def arch_40_water_treatment_flocculation_coagulation(rng: random.Random) -> Dict[str, Any]:
    chemical = rng.choice(["Alum (aluminium sulfate)", "Ferric chloride"])

    prompt = (
        f"Fine clay and silt particles in river water are negatively charged and repel each other, remaining permanently suspended as a cloudy colloid.\n\n"
        f"1. Name the chemical process where a coagulant like **{chemical}** is added to water.\n"
        f"2. Explain how this coagulant transforms fine suspended particles into heavy 'flocs' that easily sink."
    )
    sol = (
        f"**Step 1:** The process is **coagulation and flocculation** [1 Mark: Process].\n\n"
        f"**Step 2:** The coagulant neutralises the electrical charges on the clay particles, allowing them to collide and clump together into larger, heavier sticky aggregates called **flocs**, which rapidly sink to the bottom during sedimentation [2 Marks: Chemical clumping]."
    )
    return {
        "id": f"ns7_sep_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Coagulation and flocculation; neutralises charges so particles clump into heavy flocs that sink",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "40_water_treatment_flocculation_coagulation",
        "misconception_tags": ["flocculation_mechanism"],
        "hints": {
            "tier_1": "Alum causes tiny particles to stick together.",
            "tier_2": "Coagulation and flocculation form clumps called flocs.",
            "tier_3": "Coagulation/flocculation; particles clump into heavy flocs that sink."
        }
    }


def arch_41_water_treatment_disinfection_chlorine(rng: random.Random) -> Dict[str, Any]:
    disinfectants = [
        ("Chlorine gas / sodium hypochlorite", "kills pathogenic bacteria like cholera and typhoid, leaving a residual protection in tap water pipes"),
        ("Ultraviolet (UV) radiation", "destroys bacterial DNA without adding chemicals or altering taste, but provides no residual pipe protection"),
    ]
    agent, mechanism = rng.choice(disinfectants)

    prompt = (
        f"The final essential step in municipal water treatment is disinfection.\n"
        f"Method: '{agent}'.\n\n"
        f"1. What is the biological goal of adding {agent} to purified water?\n"
        f"2. Why is physical filtration alone insufficient to make river water safe for drinking?"
    )
    sol = (
        f"**Step 1:** Goal: To destroy and kill harmful **pathogenic microorganisms (bacteria, viruses, and parasites)** that cause waterborne diseases like cholera and dysentery ({mechanism}) [1 Mark: Disinfection goal].\n\n"
        f"**Step 2:** Physical filtration removes suspended dirt and sand, but microscopic bacteria and viruses are tiny enough to pass straight through the pores of sand filters [1 Mark: Filtration limitation]."
    )
    return {
        "id": f"ns7_sep_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Kills pathogenic bacteria and viruses; microscopic pathogens pass through sand filter pores",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "41_water_treatment_disinfection_chlorine",
        "misconception_tags": ["clean_looking_water_safety_myth"],
        "hints": {
            "tier_1": "Can you see bacteria with your naked eye?",
            "tier_2": "Filtration removes dirt, but chlorine kills germs.",
            "tier_3": "Kills pathogens; bacteria are too small to be trapped by sand filters."
        }
    }


def arch_42_desalination_reverse_osmosis_distillation(rng: random.Random) -> Dict[str, Any]:
    coastal_cities = ["Cape Town", "Mossel Bay", "Port Elizabeth (Gqeberha)"]
    city = rng.choice(coastal_cities)

    prompt = (
        f"During severe droughts in coastal cities like {city}, municipal engineers build **desalination** plants to convert ocean seawater into fresh drinking water.\n\n"
        f"1. Define **desalination**.\n"
        f"2. Name TWO technological methods used for large-scale desalination.\n"
        f"3. State ONE major economic or environmental drawback of desalination plants."
    )
    sol = (
        f"**Step 1:** Desalination is the process of removing dissolved salts and minerals from seawater to produce fresh water suitable for human consumption or irrigation [1 Mark: Definition].\n\n"
        f"**Step 2:** Two methods: **Reverse Osmosis (RO)** (forcing water through semi-permeable membranes) and **Thermal Distillation / Multi-stage flash distillation** [1 Mark: Methods].\n\n"
        f"**Step 3:** Drawback: Extremely **high electricity / energy consumption** (high cost) and the environmental impact of discharging concentrated hypersaline brine back into local marine habitats [1 Mark: Drawback]."
    )
    return {
        "id": f"ns7_sep_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Removing dissolved salt from seawater; Reverse osmosis and distillation; high electricity cost and hypersaline brine discharge",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "42_desalination_reverse_osmosis_distillation",
        "misconception_tags": ["desalination_energy_cost"],
        "hints": {
            "tier_1": "Desalination takes salt out of seawater.",
            "tier_2": "Reverse osmosis and distillation; drawback is high energy cost.",
            "tier_3": "Removing salt from seawater; Reverse osmosis / distillation; high energy consumption."
        }
    }


# ==============================================================================
# CLUSTER 6: Sorting Waste & Separation Strategy (43 - 50)
# ==============================================================================

def arch_43_separation_at_source_waste_management(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Modern waste management encourages **separation at source** in homes and schools.\n\n"
        f"1. Explain what is meant by 'separation at source'.\n"
        f"2. Contrast the contents of a 'wet waste' bin with a 'dry recyclable' bin.\n"
        f"3. Explain why mixing food scraps with clean paper in the same bin undermines recycling."
    )
    sol = (
        f"**Step 1:** Separation at source means sorting waste into distinct categories at the point where it is generated (in the household or classroom) before collection [1 Mark: Definition].\n\n"
        f"**Step 2:** 'Wet waste' contains organic matter (food leftovers, vegetable peels, garden cuttings for compost), whereas 'dry recyclables' contain clean paper, cardboard, plastics, glass, and metal cans [1 Mark: Bin comparison].\n\n"
        f"**Step 3:** Food scraps and oils contaminate paper fibres, making them greasy, foul-smelling, and impossible to re-pulp at paper recycling mills [1 Mark: Contamination]."
    )
    return {
        "id": f"ns7_sep_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Sorting at the point of generation; wet=food/organics, dry=paper/plastics/glass/metal; food oil contaminates paper fibres",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "43_separation_at_source_waste_management",
        "misconception_tags": ["separation_at_source_principles"],
        "hints": {
            "tier_1": "Separate before putting it out for collection.",
            "tier_2": "Wet is food/garden; dry is glass/plastic/paper.",
            "tier_3": "Sorting where produced; wet=organics, dry=recyclables; food ruins paper."
        }
    }


def arch_44_mechanical_recycling_trommel_screens(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In Materials Recovery Facilities (MRFs), mixed dry recyclables pass through a **trommel screen** (a large rotating perforated cylindrical drum tilted at an angle).\n\n"
        f"1. On which physical principle does a trommel screen operate to sort mixed waste?\n"
        f"2. What happens to items smaller than the drum perforations compared to items larger than the perforations?\n"
        f"3. Name ONE material item typically separated out by the small holes (e.g. bottle caps, broken glass)."
    )
    sol = (
        f"**Step 1:** It operates on the principle of **sieving (particle size separation)** [1 Mark: Principle].\n\n"
        f"**Step 2:** Items smaller than the holes fall through onto a conveyor belt below, while larger items tumble down the length of the cylinder and exit at the far end [1 Mark: Mechanism].\n\n"
        f"**Step 3:** Small items: **bottle caps, shredded paper, or broken glass cullet** [1 Mark: Example]."
    )
    return {
        "id": f"ns7_sep_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Sieving / particle size; smaller fall through, larger tumble out end; bottle caps / broken glass",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "44_mechanical_recycling_trommel_screens",
        "misconception_tags": ["trommel_screen_sieving"],
        "hints": {
            "tier_1": "A trommel is a giant rotating sieve.",
            "tier_2": "Small things fall through holes; big things tumble out.",
            "tier_3": "Sieving by size; small fall through, large pass out end; bottle caps."
        }
    }


def arch_45_eddy_current_separators_aluminium(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Aluminium beverage cans are non-magnetic, yet automated recycling plants separate them from plastics using an **Eddy Current Separator**.\n\n"
        f"1. Explain how a rapidly spinning magnetic rotor creates eddy currents inside an electrical conductor like aluminium.\n"
        f"2. Describe the physical force that results and how it ejects the aluminium cans away from plastic containers on the conveyor belt."
    )
    sol = (
        f"**Step 1:** The spinning magnetic rotor generates a changing magnetic field that induces circulating electrical currents (eddy currents) within conductive aluminium cans [1 Mark: Induction].\n\n"
        f"**Step 2:** These eddy currents produce their own opposing magnetic field that repels the rotor, launching the aluminium cans forward over a splitter into a separate bin, while non-conductive plastics simply fall straight down off the belt [2 Marks: Repulsive ejection]."
    )
    return {
        "id": f"ns7_sep_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Changing magnetic field induces eddy currents; opposing magnetic field repels and launches aluminium cans over splitter",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "45_eddy_current_separators_aluminium",
        "misconception_tags": ["eddy_current_repulsion"],
        "hints": {
            "tier_1": "Aluminium is a conductor; changing magnets induce electric currents.",
            "tier_2": "The induced magnetic field repels the rotor and launches the can forward.",
            "tier_3": "Induces eddy currents; opposing magnetic field repels and ejects aluminium cans."
        }
    }


def arch_46_optical_sensor_sorting_near_infrared(rng: random.Random) -> Dict[str, Any]:
    polymers = [
        ("PET (clear beverage bottles)", "HDPE (opaque milk and detergent bottles)"),
        ("Polypropylene (yoghurt tubs)", "Polystyrene (foam trays)"),
    ]
    p1, p2 = rng.choice(polymers)

    prompt = (
        f"Advanced recycling facilities use **Near-Infrared (NIR) optical sorters** to separate different plastic polymers ({p1} from {p2}).\n\n"
        f"1. How does the optical sensor identify the specific plastic polymer of each item passing underneath on a conveyor belt?\n"
        f"2. Once an item is identified, what mechanical device shoots it into the correct collection bin?"
    )
    sol = (
        f"**Step 1:** The sensor beams infrared light onto the plastic; each polymer reflects a unique infrared absorption spectrum (an optical chemical fingerprint) that a computer instantly identifies [1 Mark: Optical fingerprint].\n\n"
        f"**Step 2:** A row of high-speed **compressed air jets (air nozzles)** fires precise bursts of air to blow the targeted item upward into the correct chute [1 Mark: Air jet ejection]."
    )
    return {
        "id": f"ns7_sep_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Unique infrared absorption spectrum / optical fingerprint; high-speed compressed air jets",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "46_optical_sensor_sorting_near_infrared",
        "misconception_tags": ["optical_nir_sorting"],
        "hints": {
            "tier_1": "Infrared light identifies plastic types by their optical fingerprint.",
            "tier_2": "Puffs of compressed air blast the plastic into bins.",
            "tier_3": "Infrared spectrum identification; compressed air jets."
        }
    }


def arch_47_air_classification_winnowing_density(rng: random.Random) -> Dict[str, Any]:
    contexts = [
        ("traditional rural farmers separating wheat grains from lightweight dry chaff husks", "tossing the harvested grain into the wind on a threshing floor"),
        ("recycling plants separating lightweight plastic film bags from dense rigid plastic bottles", "passing shredded waste through a rising column of blown air in an air classifier"),
    ]
    desc, action = rng.choice(contexts)

    prompt = (
        f"Density-based air separation has ancient roots and modern industrial applications:\n"
        f"'{desc}' by '{action}'.\n\n"
        f"1. Name this separation method (**winnowing** or **air classification**).\n"
        f"2. Explain how moving air separates the two components based on density and surface-area-to-weight ratio."
    )
    sol = (
        f"**Step 1:** The method is **winnowing** (or **air classification**) [1 Mark: Terminology].\n\n"
        f"**Step 2:** The wind or air blast exerts drag on the lightweight, high-surface-area pieces (chaff or plastic film), blowing them sideways or upward, while dense, heavy pieces fall straight down under gravity [1 Mark: Aerodynamic density separation]."
    )
    return {
        "id": f"ns7_sep_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Winnowing / air classification; air blows light, high-surface-area pieces while dense heavy pieces fall straight down",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "47_air_classification_winnowing_density",
        "misconception_tags": ["winnowing_air_classification"],
        "hints": {
            "tier_1": "Think of wind blowing chaff away from wheat.",
            "tier_2": "Light pieces blow away; heavy pieces fall down.",
            "tier_3": "Winnowing / air classification; light chaff blows away, heavy grains fall."
        }
    }


def arch_48_evaluating_separation_efficiency_percentage(rng: random.Random) -> Dict[str, Any]:
    total_sand = rng.choice([200, 250, 300])
    recovered = total_sand - rng.choice([20, 25, 30])
    pct = round((recovered / total_sand) * 100, 1)

    prompt = (
        f"A learner is given a mixture containing exactly {total_sand} g of sand mixed with salt.\n"
        f"After dissolving, filtering, and drying the recovered sand on filter paper, the final mass of dry sand is measured as {recovered} g.\n\n"
        f"1. Calculate the percentage recovery of sand ($\\text{{Percentage Recovery}} = \\frac{{\\text{{mass recovered}}}}{{\\text{{initial mass}}}} \\times 100\\%$).\n"
        f"2. Suggest TWO practical reasons why recovery was less than $100\\%$."
    )
    sol = (
        f"**Step 1:** $$\\text{{Percentage Recovery}} = \\frac{{{recovered}}}{{{total_sand}}} \\times 100\\% = \\mathbf{{{str(pct).replace('.', ',')}\\%}} \\text{{ [1 Mark: Calculation]}}$$\n\n"
        f"**Step 2:** Reasons for loss (any two): some fine sand particles remained stuck to the inside walls of the beaker, spilled during transfer, or trapped inside the fibres of the filter paper [1 Mark: Experimental error]."
    )
    return {
        "id": f"ns7_sep_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{str(pct).replace('.', ',')}%; sand stuck to beaker walls, trapped in filter paper, or transfer spills",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "48_evaluating_separation_efficiency_percentage",
        "misconception_tags": ["percentage_recovery_yield"],
        "hints": {
            "tier_1": f"Divide {recovered} by {total_sand} and multiply by 100.",
            "tier_2": f"({recovered} / {total_sand}) * 100 = {pct}%.",
            "tier_3": f"{pct}%; losses due to sand clinging to glass and paper."
        }
    }


def arch_49_troubleshooting_separation_method_errors(rng: random.Random) -> Dict[str, Any]:
    errors = [
        ("A student tried to separate dissolved salt from water by pouring the saltwater solution through filter paper. The liquid in the flask was still salty.", "Salt is completely dissolved into microscopic ions smaller than filter paper pores, so it cannot be filtered. They should have used evaporation or distillation."),
        ("A student boiled black ink in an open evaporating dish to recover the pure water solvent. The dish was left with dry black pigment and no water.", "Evaporation allows the vaporised solvent to escape into the atmosphere. To collect the water, they should have used simple distillation with a condenser."),
        ("A student tried to separate oil from water by filtration through paper. Both liquids soaked through the paper and formed a messy mixture.", "Filter paper only separates insoluble solids from liquids, not two liquids. They should have used a separating funnel."),
    ]
    mistake, remedy = rng.choice(errors)

    prompt = (
        f"A novice science learner made an experimental mistake:\n"
        f"'{mistake}'.\n\n"
        f"1. Explain the scientific flaw in the learner's chosen method.\n"
        f"2. Name the correct separation technique they should have used instead."
    )
    sol = (
        f"**Step 1:** Flaw: {remedy.split('. They')[0]}. [1 Mark: Flaw identification].\n\n"
        f"**Step 2:** Correct technique: {remedy.split('should have used ')[1]} [1 Mark: Correct method]."
    )
    return {
        "id": f"ns7_sep_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{remedy}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "49_troubleshooting_separation_method_errors",
        "misconception_tags": ["separation_flaw_diagnosis"],
        "hints": {
            "tier_1": "What can filter paper do, and what can it NOT do?",
            "tier_2": "Look at the states of matter: solid vs liquid, or liquid vs liquid.",
            "tier_3": f"{remedy}"
        }
    }


def arch_50_designing_separation_strategy_novel_mixture(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"You are challenged to separate a complex dry mixture containing:\n"
        f"**Iron filings, sand, salt, and small Styrofoam (polystyrene) beads**.\n\n"
        f"Design a complete sequential 4-step separation plan to isolate each of the four components in a pure, dry state.\n"
        f"List each step and name the component isolated at that stage."
    )
    sol = (
        f"**Step 1:** Pass a **magnet** over the dry mixture to remove all **iron filings** [1 Mark: Step 1].\n\n"
        f"**Step 2:** Add water to the remaining mixture; the lightweight **Styrofoam beads** float to the surface and are skimmed off with a sieve [1 Mark: Step 2].\n\n"
        f"**Step 3:** Pour the remaining sand and saltwater mixture through a **filter funnel and paper**; the **sand** is collected as residue and dried [1 Mark: Step 3].\n\n"
        f"**Step 4:** Heat the clear saltwater filtrate in an **evaporating dish** to boil off water and recover dry **salt crystals** [1 Mark: Step 4]."
    )
    return {
        "id": f"ns7_sep_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "1. Magnet (iron), 2. Flotation in water (Styrofoam), 3. Filtration (sand), 4. Evaporation (salt)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 4,
        "term": 2,
        "subskill": "50_designing_separation_strategy_novel_mixture",
        "misconception_tags": ["complex_mixture_separation_strategy"],
        "hints": {
            "tier_1": "1. Magnet for iron. 2. Water for floating Styrofoam. 3. Filter for sand. 4. Evaporate for salt.",
            "tier_2": "Follow physical properties: magnetic, density/flotation, solubility, boiling point.",
            "tier_3": "1. Magnet, 2. Float Styrofoam, 3. Filter sand, 4. Evaporate salt."
        }
    }
