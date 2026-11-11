"""
Grade 7 Natural Sciences - Term 2: Properties of Materials (Archetypes 26 to 50).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/01. Properties of materials.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 4: Metal Types, Corrosion & Optical Properties (26 - 30)
# ==============================================================================

def arch_26_ferrous_vs_non_ferrous_metals(rng: random.Random) -> Dict[str, Any]:
    metals = [
        ("Mild steel", True, "contains iron, susceptible to rust, magnetic"),
        ("Cast iron", True, "contains high proportion of iron, rusts readily, magnetic"),
        ("Aluminium", False, "contains no iron, does not rust, non-magnetic"),
        ("Copper", False, "pure non-ferrous metal, forms green patina not rust, non-magnetic"),
        ("Brass", False, "alloy of copper and zinc, non-ferrous, non-magnetic"),
    ]
    rng.shuffle(metals)
    m1, m2 = metals[0], metals[1]

    prompt = (
        f"In metallurgy, metals are broadly classified as **ferrous** or **non-ferrous**.\n\n"
        f"- Metal A: {m1[0]}\n"
        f"- Metal B: {m2[0]}\n\n"
        f"1. Classify each of these two metals as ferrous or non-ferrous.\n"
        f"2. Explain what distinguishes a ferrous metal from a non-ferrous metal."
    )
    ans1 = "Ferrous" if m1[1] else "Non-ferrous"
    ans2 = "Ferrous" if m2[1] else "Non-ferrous"

    sol = (
        f"**Step 1:**\n"
        f"- Metal A ({m1[0]}): **{ans1}** [1 Mark: Classification].\n"
        f"- Metal B ({m2[0]}): **{ans2}** [1 Mark: Classification].\n\n"
        f"**Step 2:** Ferrous metals contain iron (Fe) as a principal component, making them usually magnetic and prone to rusting; non-ferrous metals do not contain iron and do not rust [1 Mark: Distinction]."
    )
    return {
        "id": f"ns7_prop_26_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Metal A: {ans1}; Metal B: {ans2}; Ferrous contains iron, non-ferrous does not",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "26_ferrous_vs_non_ferrous_metals",
        "misconception_tags": ["all_metals_rust_myth"],
        "hints": {
            "tier_1": "Ferrous comes from the Latin 'ferrum' meaning iron.",
            "tier_2": "Metals containing iron are ferrous; metals without iron are non-ferrous.",
            "tier_3": f"Metal A: {ans1}; Metal B: {ans2}."
        }
    }


def arch_27_corrosion_and_rusting_protection(rng: random.Random) -> Dict[str, Any]:
    structures = [
        ("steel security gate exposed to coastal sea air in Durban", "painting with anti-rust primer", "barrier coating that prevents oxygen and moisture from contacting iron"),
        ("underground corrugated steel drainage culvert", "galvanising with a zinc coating", "zinc creates a protective barrier and sacrificially corrodes before iron"),
        ("bicycle drive chain and gears", "regular oiling or greasing", "lubricating film repels water and prevents air contact"),
    ]
    structure, method, mechanism = rng.choice(structures)

    prompt = (
        f"Iron and steel items exposed to weather are prone to rusting.\n"
        f"Consider: '{structure}'.\n\n"
        f"1. State the TWO environmental substances that must both be present for iron to rust.\n"
        f"2. Describe the protective method '{method}' and explain how it prevents rust."
    )
    sol = (
        f"**Step 1:** Rusting requires both **water (moisture)** and **oxygen (air)** to be in contact with iron [1 Mark: Reagents].\n\n"
        f"**Step 2:** {method.capitalize()} acts as a {mechanism} [1 Mark: Mechanism]."
    )
    return {
        "id": f"ns7_prop_27_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Water and oxygen; {mechanism}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "27_corrosion_and_rusting_protection",
        "misconception_tags": ["rust_only_needs_water_myth"],
        "hints": {
            "tier_1": "Rust needs both air and moisture.",
            "tier_2": "Oxygen and water are both essential for iron to rust.",
            "tier_3": "Water and oxygen; method blocks contact with air and moisture."
        }
    }


def arch_28_transparency_translucency_opacity(rng: random.Random) -> Dict[str, Any]:
    examples = [
        ("clear sheet of window glass", "Transparent", "allows almost all light to pass through clearly without scattering"),
        ("frosted glass shower panel or tracing paper", "Translucent", "allows some light to pass through but scatters it, so objects cannot be clearly seen"),
        ("thick sheet of plywood or sheet metal", "Opaque", "blocks all light completely, casting a dark shadow"),
    ]
    item_info = rng.choice(examples)
    item, category, description = item_info

    op = "0.2" if category == "Transparent" else ("0.6" if category == "Translucent" else "1.0")
    ray_dash = "none" if category == "Transparent" else ("4,4" if category == "Translucent" else "none")
    ray_color = "#f59e0b" if category != "Opaque" else "none"

    svg = (
        f'<svg viewBox="0 0 360 160" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<circle cx="30" cy="80" r="16" fill="#facc15"/>'
        f'<line x1="60" y1="50" x2="140" y2="50" stroke="#f59e0b" stroke-width="2"/>'
        f'<line x1="60" y1="80" x2="140" y2="80" stroke="#f59e0b" stroke-width="2"/>'
        f'<line x1="60" y1="110" x2="140" y2="110" stroke="#f59e0b" stroke-width="2"/>'
        f'<rect x="150" y="30" width="30" height="100" fill="#93c5fd" opacity="{op}" rx="2"/>'
        f'<line x1="190" y1="50" x2="270" y2="50" stroke="{ray_color}" stroke-width="2" stroke-dasharray="{ray_dash}"/>'
        f'<line x1="190" y1="80" x2="270" y2="80" stroke="{ray_color}" stroke-width="2" stroke-dasharray="{ray_dash}"/>'
        f'<line x1="190" y1="110" x2="270" y2="110" stroke="{ray_color}" stroke-width="2" stroke-dasharray="{ray_dash}"/>'
        f'<text x="165" y="145" font-family="sans-serif" font-size="10" fill="#1e293b" text-anchor="middle">{item}</text>'
        f'<text x="30" y="115" font-family="sans-serif" font-size="10" fill="#b45309" text-anchor="middle">Light source</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": f"Light rays interacting with {item}",
        "diagram_role": "context"
    }

    prompt = (
        f"Materials interact with visible light in different ways.\n\n"
        f"Consider: **{item}**.\n\n"
        f"1. Classify this material as **transparent**, **translucent**, or **opaque**.\n"
        f"2. Explain what happens to light rays as they strike this material."
    )
    sol = (
        f"**Step 1:** {item} is **{category.lower()}** [1 Mark: Classification].\n\n"
        f"**Step 2:** It {description} [1 Mark: Explanation]."
    )
    return {
        "id": f"ns7_prop_28_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{category}; {description}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "28_transparency_translucency_opacity",
        "misconception_tags": ["transparent_vs_translucent"],
        "hints": {
            "tier_1": "Can you see clearly through it, partially through it, or not at all?",
            "tier_2": "Transparent = see clearly; translucent = partial/scattered; opaque = blocks light.",
            "tier_3": f"It is {category.lower()}."
        }
    }


def arch_29_suitability_of_materials_safety_gear(rng: random.Random) -> Dict[str, Any]:
    gear = [
        ("construction safety hard hat / helmet", "rigid high-density polyethylene (HDPE) plastic", "high impact strength and compressive rigidity to protect the skull from falling bricks"),
        ("firefighter heat-resistant gloves", "thick Kevlar and aluminized fabric", "exceptional thermal insulation to protect hands from intense radiant heat and flames"),
        ("laboratory safety goggles", "polycarbonate transparent plastic", "transparent for clear vision while offering high impact resistance against chemical splashes and flying glass"),
    ]
    item, mat, rationale = rng.choice(gear)

    prompt = (
        f"Industrial safety equipment must be carefully engineered from suitable materials.\n"
        f"Consider: '{item}'.\n\n"
        f"1. Identify the primary material typically chosen: {mat}.\n"
        f"2. Discuss TWO essential physical properties this material provides that make it suitable for protecting the worker."
    )
    sol = (
        f"**Step 1:** The selected material is {mat} [1 Mark: Knowledge].\n\n"
        f"**Step 2:** Essential properties: {rationale} [2 Marks: Critical analysis]."
    )
    return {
        "id": f"ns7_prop_29_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{mat}; {rationale}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "29_suitability_of_materials_safety_gear",
        "misconception_tags": ["material_property_alignment"],
        "hints": {
            "tier_1": "What dangers does the worker face?",
            "tier_2": "The material must provide specific protection such as impact strength or thermal insulation.",
            "tier_3": f"Properties: {rationale}."
        }
    }


def arch_30_textiles_natural_vs_synthetic_fibres(rng: random.Random) -> Dict[str, Any]:
    fibres = [
        ("Cotton", "Natural plant fibre", "absorbs water/sweat well, breathable, biodegrades naturally, but wrinkles easily"),
        ("Wool", "Natural animal fibre", "excellent thermal insulation due to crimped fibres trapping air, warm even when damp"),
        ("Nylon", "Synthetic polymer fibre", "very high tensile strength, quick-drying, durable, but made from fossil fuels and non-biodegradable"),
        ("Polyester", "Synthetic polymer fibre", "resists wrinkling and stretching, quick-drying, but non-biodegradable and sheds microfibres"),
    ]
    f1, f2 = rng.sample(fibres, 2)

    prompt = (
        f"Compare the properties of two textile materials:\n"
        f"- Fibre 1: {f1[0]} ({f1[1]})\n"
        f"- Fibre 2: {f2[0]} ({f2[1]})\n\n"
        f"1. State whether each fibre is natural or synthetic.\n"
        f"2. Compare ONE advantage and ONE disadvantage of using natural vs synthetic fibres in clothing."
    )
    sol = (
        f"**Step 1:** {f1[0]} is a **{f1[1].split()[0].lower()}** fibre; {f2[0]} is a **{f2[1].split()[0].lower()}** fibre [1 Mark: Classification].\n\n"
        f"**Step 2:** Natural fibres are typically breathable, comfortable against the skin, and biodegradable, but may shrink or wrinkle easily. Synthetic fibres have superior tensile strength and dry quickly, but are non-biodegradable and derived from non-renewable petrochemicals [2 Marks: Comparison]."
    )
    return {
        "id": f"ns7_prop_30_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{f1[0]}={f1[1].split()[0]}; {f2[0]}={f2[1].split()[0]}; Natural is breathable/biodegradable; synthetic is stronger/quick-drying but non-biodegradable",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "30_textiles_natural_vs_synthetic_fibres",
        "misconception_tags": ["natural_vs_synthetic_polymers"],
        "hints": {
            "tier_1": "Natural fibres come from plants or animals; synthetic fibres are manufactured from petroleum.",
            "tier_2": "Cotton and wool are natural; nylon and polyester are synthetic.",
            "tier_3": "Natural is biodegradable and breathable; synthetic is stronger and dries faster."
        }
    }


# ==============================================================================
# CLUSTER 5: Environmental Impact of Mining & Manufacturing (31 - 37)
# ==============================================================================

def arch_31_environmental_impact_open_cast_mining(rng: random.Random) -> Dict[str, Any]:
    minerals = [
        ("open-cast coal mining in Mpumalanga", "coal for electricity generation"),
        ("open-cast iron ore mining in Sishen (Northern Cape)", "iron ore for steel manufacturing"),
        ("open-cast copper mining in Phalaborwa (Limpopo)", "copper ore for electrical wiring"),
    ]
    mine, resource = rng.choice(minerals)

    prompt = (
        f"To obtain raw materials for manufacturing, large-scale mining operations are established:\n"
        f"'{mine}'.\n\n"
        f"1. Explain how open-cast surface mining alters the local terrestrial ecosystem.\n"
        f"2. Identify TWO distinct environmental problems caused by massive open-pit excavation."
    )
    sol = (
        f"**Step 1:** Open-cast mining strips away topsoil and vegetation over massive areas, destroying indigenous animal and plant habitats and disrupting biodiversity [1 Mark: Ecosystem impact].\n\n"
        f"**Step 2:** Environmental problems (any two): severe soil erosion, dust and air pollution from blasting, destruction of fertile agricultural land, or creation of dangerous open pits and tailings dumps [2 Marks: Detail]."
    )
    return {
        "id": f"ns7_prop_31_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Destroys vegetation and topsoil; habitat loss, soil erosion, air/dust pollution",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "31_environmental_impact_open_cast_mining",
        "misconception_tags": ["mining_ecosystem_disruption"],
        "hints": {
            "tier_1": "What happens to the land, trees, and animals when a massive hole is dug?",
            "tier_2": "Vegetation and soil are cleared, destroying habitats and causing dust and erosion.",
            "tier_3": "Destruction of habitats, dust pollution, and soil erosion."
        }
    }


def arch_32_acid_mine_drainage_and_water(rng: random.Random) -> Dict[str, Any]:
    provinces = ["Gauteng (Witwatersrand goldfields)", "Mpumalanga (Highveld coal basin)"]
    prov = rng.choice(provinces)

    prompt = (
        f"In historical mining regions of {prov}, abandoned underground mines frequently produce **Acid Mine Drainage (AMD)**.\n\n"
        f"1. Describe what chemical conditions create acid mine drainage.\n"
        f"2. Explain the devastating ecological consequences when AMD decants into natural rivers and groundwater."
    )
    sol = (
        f"**Step 1:** When sulfide minerals (like iron pyrite) buried underground are exposed to water and oxygen during mining, they react chemically to form dilute sulfuric acid [1 Mark: Chemistry].\n\n"
        f"**Step 2:** The acidic water drastically lowers the pH of streams and rivers, dissolves toxic heavy metals (lead, arsenic, uranium), and kills aquatic life, making water unsafe for humans, livestock, and irrigation [2 Marks: Ecological impact]."
    )
    return {
        "id": f"ns7_prop_32_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Sulfide minerals react with water and oxygen to make sulfuric acid; lowers pH and poisons aquatic life with heavy metals",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "32_acid_mine_drainage_and_water",
        "misconception_tags": ["acid_mine_drainage_formation"],
        "hints": {
            "tier_1": "Mining exposes sulfur minerals to water and air, forming acid.",
            "tier_2": "Acidic water dissolves heavy metals and poisons streams.",
            "tier_3": "Forms sulfuric acid, drastically lowers river pH, kills fish and aquatic plants."
        }
    }


def arch_33_energy_consumption_raw_vs_recycled(rng: random.Random) -> Dict[str, Any]:
    percent_saved = rng.choice([90, 95])
    kwh_raw = 100
    kwh_recycled = kwh_raw * (100 - percent_saved) // 100

    prompt = (
        f"Smelting raw aluminium metal from mined bauxite ore requires huge amounts of electrical energy ($100\\text{{ kWh}}$ per test unit).\n"
        f"In contrast, remelting discarded aluminium cold-drink cans saves {percent_saved}% of this energy.\n\n"
        f"1. Calculate how many kilowatt-hours (kWh) of electrical energy are needed to process the same unit of recycled aluminium.\n"
        f"2. Explain why recycling aluminium has such a dramatic positive impact on South Africa's national electricity grid."
    )
    sol = (
        f"**Step 1:** Energy required for recycling: $${kwh_raw} \\times \\left(1 - \\frac{{{percent_saved}}}{{100}}\\right) = {kwh_raw} \\times {100 - percent_saved}\\% = \\mathbf{{{kwh_recycled}\\text{{ kWh}}}} \\text{{ [1 Mark: Calculation]}}$$\n\n"
        f"**Step 2:** Because {percent_saved}% less electricity is used, power stations burn significantly less coal, reducing carbon dioxide emissions and alleviating strain on Eskom's power generation capacity [1 Mark: Grid impact]."
    )
    return {
        "id": f"ns7_prop_33_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{kwh_recycled} kWh; saves electricity and reduces coal burning and emissions",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "33_energy_consumption_raw_vs_recycled",
        "misconception_tags": ["energy_conservation_in_recycling"],
        "hints": {
            "tier_1": f"If {percent_saved}% is saved, only {100 - percent_saved}% of the original 100 kWh is used.",
            "tier_2": f"Calculate {100 - percent_saved}% of 100 kWh.",
            "tier_3": f"{kwh_recycled} kWh."
        }
    }


def arch_34_air_pollution_smelting_greenhouse_gases(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("iron blast furnace converting hematite ore to pig iron using coke (coal carbon)", "Carbon dioxide (CO2)", "acts as a major greenhouse gas trapping heat and causing global climate change"),
        ("copper and zinc smelting furnaces heating sulfide ores", "Sulfur dioxide (SO2)", "reacts with atmospheric moisture to form acid rain which damages forests, buildings, and water bodies"),
    ]
    furnace, gas, consequence = rng.choice(cases)

    prompt = (
        f"Industrial metal refineries use extreme heat to extract pure metals:\n"
        f"'{furnace}'.\n\n"
        f"1. Name the primary air pollutant gas emitted in this specific process: **{gas}**.\n"
        f"2. Explain the negative environmental impact this gas has on the atmosphere and surrounding ecosystems."
    )
    sol = (
        f"**Step 1:** The pollutant gas is **{gas}** [1 Mark: Identification].\n\n"
        f"**Step 2:** {gas} {consequence} [1 Mark: Environmental mechanism]."
    )
    return {
        "id": f"ns7_prop_34_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{gas}; {consequence}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "34_air_pollution_smelting_greenhouse_gases",
        "misconception_tags": ["greenhouse_gases_vs_acid_rain"],
        "hints": {
            "tier_1": "Carbon gases cause global warming; sulfur gases cause acid rain.",
            "tier_2": f"This process releases {gas}.",
            "tier_3": f"{gas} {consequence}."
        }
    }


def arch_35_biodegradable_definition_and_examples(rng: random.Random) -> Dict[str, Any]:
    items = [
        ("banana peel", "Biodegradable", "broken down into natural compost by bacteria and fungi within weeks"),
        ("polystyrene fast-food container", "Non-biodegradable", "synthetic polymer that cannot be decomposed by natural microbes, persisting for centuries"),
        ("cotton paper napkin", "Biodegradable", "made of plant cellulose which decomposers digest readily"),
        ("polyethylene plastic shopping bag", "Non-biodegradable", "synthetic petroleum product resistant to biological decomposition"),
    ]
    rng.shuffle(items)
    i1, i2 = items[0], items[1]

    prompt = (
        f"Waste materials are categorized according to whether they can rot or break down naturally.\n\n"
        f"- Item 1: {i1[0]}\n"
        f"- Item 2: {i2[0]}\n\n"
        f"1. Define what is meant by a **biodegradable** material.\n"
        f"2. Classify each of the two items as biodegradable or non-biodegradable."
    )
    sol = (
        f"**Step 1:** A biodegradable material is capable of being broken down and decomposed naturally into harmless organic substances by living organisms (microorganisms like bacteria and fungi) [1 Mark: Definition].\n\n"
        f"**Step 2:**\n"
        f"- Item 1 ({i1[0]}): **{i1[1]}** [1 Mark: Classification].\n"
        f"- Item 2 ({i2[0]}): **{i2[1]}** [1 Mark: Classification]."
    )
    return {
        "id": f"ns7_prop_35_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Decomposed naturally by microorganisms; Item 1: {i1[1]}; Item 2: {i2[1]}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "35_biodegradable_definition_and_examples",
        "misconception_tags": ["biodegradable_meaning"],
        "hints": {
            "tier_1": "Can bacteria and fungi eat and break down this material?",
            "tier_2": "Organic plant/animal matter is biodegradable; synthetic plastics are non-biodegradable.",
            "tier_3": f"Item 1: {i1[1]}; Item 2: {i2[1]}."
        }
    }


def arch_36_non_biodegradable_plastics_persistence(rng: random.Random) -> Dict[str, Any]:
    years = rng.choice([400, 450, 500])
    plastic_item = rng.choice(["PET cold-drink bottle", "HDPE plastic shampoo bottle", "plastic drinking straw"])

    prompt = (
        f"A discarded {plastic_item} is buried in a modern municipal landfill site. Scientists estimate it will take over {years} years to break down.\n\n"
        f"1. Explain why natural decomposers (bacteria and fungi) cannot easily break down synthetic plastics.\n"
        f"2. Name the process by which sunlight slowly causes plastic to become brittle and fragment into tiny pieces without chemically decomposing it."
    )
    sol = (
        f"**Step 1:** Synthetic plastics consist of long, strong artificial polymer chains that do not occur in nature, so microorganisms lack the specific digestive enzymes needed to break the chemical bonds [1 Mark: Enzymatic reason].\n\n"
        f"**Step 2:** The process of breakdown caused by ultraviolet light from the sun is called **photodegradation** (forming microplastics) [1 Mark: Terminology]."
    )
    return {
        "id": f"ns7_prop_36_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Microbes lack enzymes to break synthetic polymer chains; photodegradation",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "36_non_biodegradable_plastics_persistence",
        "misconception_tags": ["photodegradation_vs_biodegradation"],
        "hints": {
            "tier_1": "Microbes do not have enzymes for artificial polymers.",
            "tier_2": "Sunlight breaks plastics into smaller pieces through photodegradation.",
            "tier_3": "Microbes lack enzymes; process is photodegradation."
        }
    }


def arch_37_impact_of_plastics_on_marine_life(rng: random.Random) -> Dict[str, Any]:
    animals = [
        ("Sea turtles", "mistake clear plastic bags floating in the ocean for jellyfish, swallow them, causing lethal intestinal blockage and starvation"),
        ("Seabirds (such as albatrosses)", "ingest brightly coloured plastic bottle caps floating on water, filling their stomachs so they starve"),
        ("Seals and dolphins", "become entangled in discarded plastic six-pack rings and nylon ghost fishing nets, causing severe injuries and drowning"),
    ]
    animal, effect = rng.choice(animals)

    prompt = (
        f"Millions of tonnes of plastic waste enter the world's oceans each year.\n\n"
        f"1. Describe how plastic debris specifically threatens **{animal}**.\n"
        f"2. Define the term **microplastics** and explain why they pose a hazard throughout the marine food chain."
    )
    sol = (
        f"**Step 1:** {animal} {effect} [1 Mark: Animal impact].\n\n"
        f"**Step 2:** Microplastics are microscopic plastic fragments smaller than $5\\text{{ mm}}$. Plankton and small fish ingest them, concentrating toxic chemicals that bioaccumulate up the food chain to larger predators and humans [2 Marks: Microplastics definition & food web]."
    )
    return {
        "id": f"ns7_prop_37_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{effect}; microplastics are plastic pieces < 5 mm that bioaccumulate in food chains",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "37_impact_of_plastics_on_marine_life",
        "misconception_tags": ["marine_plastic_ingestion"],
        "hints": {
            "tier_1": "Turtles mistake plastic bags for food; birds eat bottle caps.",
            "tier_2": "Microplastics are tiny pieces (< 5 mm) eaten by small organisms.",
            "tier_3": f"{effect}; microplastics bioaccumulate."
        }
    }


# ==============================================================================
# CLUSTER 6: Recycling & Material Selection (38 - 50)
# ==============================================================================

def arch_38_waste_hierarchy_refuse_reduce_reuse_recycle(rng: random.Random) -> Dict[str, Any]:
    actions = [
        ("Saying 'no thank you' to a single-use plastic straw at a restaurant", "Refuse", "prevents the waste item from ever being manufactured or entering the waste stream"),
        ("Washing an empty glass peanut butter jar and using it to store paperclips", "Reuse", "extends the product life directly without expending industrial recycling energy"),
        ("Placing crushed clean aluminium cold-drink cans into the school green recycling crate", "Recycle", "allows the material to be reprocessed into brand new products"),
    ]
    action, tier, rationale = rng.choice(actions)

    highlight_box = f'<rect x="15" y="10" width="130" height="22" fill="#0f172a" rx="4"/><text x="80" y="25" font-family="sans-serif" font-size="10" font-weight="bold" fill="#f8fafc" text-anchor="middle">Focus: {tier}</text>'

    svg = (
        f'<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'{highlight_box}'
        f'<polygon points="40,36 320,36 280,72 80,72" fill="#22c55e"/>'
        f'<polygon points="80,74 280,74 245,110 115,110" fill="#84cc16"/>'
        f'<polygon points="115,112 245,112 210,148 150,148" fill="#eab308"/>'
        f'<polygon points="150,150 210,150 180,186" fill="#ef4444"/>'
        f'<text x="180" y="58" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. REFUSE / REDUCE</text>'
        f'<text x="180" y="96" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. REUSE</text>'
        f'<text x="180" y="134" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. RECYCLE</text>'
        f'<text x="180" y="172" font-family="sans-serif" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">DISPOSE</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": f"Waste Management Hierarchy emphasizing {tier}",
        "diagram_role": "context"
    }

    prompt = (
        f"The Waste Management Hierarchy prioritises options according to environmental benefit.\n\n"
        f"Consider this daily action:\n"
        f"'{action}'.\n\n"
        f"1. Which tier of the hierarchy does this action represent (**Refuse**, **Reduce**, **Reuse**, or **Recycle**)?\n"
        f"2. Explain why 'Reducing' or 'Refusing' waste is ranked as more environmentally effective than 'Recycling'."
    )
    sol = (
        f"**Step 1:** This action represents **{tier}** [1 Mark: Classification].\n\n"
        f"**Step 2:** Refusing or reducing prevents waste at the source, eliminating the raw materials, water, transportation, and industrial energy needed to manufacture and reprocess products [1 Mark: Hierarchy explanation]."
    )
    return {
        "id": f"ns7_prop_38_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{tier}; prevents waste generation at the source without using reprocessing energy",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "38_waste_hierarchy_refuse_reduce_reuse_recycle",
        "misconception_tags": ["recycling_is_not_first_choice"],
        "hints": {
            "tier_1": "Is the item being rejected, used again, or processed into something new?",
            "tier_2": f"Action: {action}. That is {tier}.",
            "tier_3": f"It is {tier}; reducing prevents waste at source."
        }
    }


def arch_39_recyclable_materials_identification_symbols(rng: random.Random) -> Dict[str, Any]:
    codes = [
        (1, "PET / PETE", "Polyethylene Terephthalate", "Clear beverage bottles, peanut butter jars", "High recyclability into polyester fleece and new bottles"),
        (2, "HDPE", "High-Density Polyethylene", "Milk bottles, detergent containers, shampoo bottles", "High recyclability into piping, plastic crates, and bins"),
        (4, "LDPE", "Low-Density Polyethylene", "Shopping bags, bread bags, squeeze bottles", "Can be recycled into plastic film and bin liners"),
        (5, "PP", "Polypropylene", "Yoghurt tubs, bottle caps, straws, medicine bottles", "Recyclable into battery casings, broom bristles, trays"),
    ]
    code, abbrev, full_name, examples, note = rng.choice(codes)

    prompt = (
        f"Plastic products are stamped with a triangular recycling identification code containing a number from 1 to 7.\n\n"
        f"A container is stamped with recycling code **Number {code} ({abbrev})**.\n\n"
        f"1. State the full chemical name of the plastic material for code {code}.\n"
        f"2. Give TWO common household packaging examples made from this resin.\n"
        f"3. Explain why different plastic polymers must be sorted and separated before recycling."
    )
    sol = (
        f"**Step 1:** Code {code} ({abbrev}) is **{full_name}** [1 Mark: Knowledge].\n\n"
        f"**Step 2:** Common examples: {examples} [1 Mark: Examples].\n\n"
        f"**Step 3:** Different plastics have different melting points and chemical structures; mixing them together weakens the recycled product and ruins the batch [1 Mark: Science reasoning]."
    )
    return {
        "id": f"ns7_prop_39_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{full_name}; {examples}; different plastics have different melting points and do not mix",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "39_recyclable_materials_identification_symbols",
        "misconception_tags": ["all_plastics_melt_together_myth"],
        "hints": {
            "tier_1": f"Code 1 is PET, Code 2 is HDPE, Code 5 is PP.",
            "tier_2": f"Code {code} stands for {full_name}.",
            "tier_3": f"{full_name}; sorting is needed because polymers do not mix well."
        }
    }


def arch_40_non_recyclable_items_contamination(rng: random.Random) -> Dict[str, Any]:
    contaminants = [
        ("greasy cardboard pizza box with melted cheese stains", "food oil and grease soak into the paper fibres and prevent them from bonding into new paper slurry"),
        ("broken window pane or drinking glass placed in a glass bottle bin", "window glass contains different minerals and a higher melting temperature than bottle glass"),
        ("disposable nappies or used medical bandages", "biological contamination hazard creating health risks for sorting workers"),
    ]
    item, reason = rng.choice(contaminants)

    prompt = (
        f"In a municipal recycling facility, an entire batch of recyclable material can be rejected due to contamination.\n\n"
        f"Consider: **{item}**.\n\n"
        f"1. Explain why this item CANNOT be processed in a standard curbside recycling stream.\n"
        f"2. What is the consequence for an entire recycling bin if heavily contaminated items are mixed into it?"
    )
    sol = (
        f"**Step 1:** Reason: {reason} [1 Mark: Contamination mechanism].\n\n"
        f"**Step 2:** The contaminated batch cannot be processed and must be diverted straight to a **landfill dump**, wasting all the clean recyclables in that load [1 Mark: Consequence]."
    )
    return {
        "id": f"ns7_prop_40_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{reason}; entire load sent to landfill",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "40_non_recyclable_items_contamination",
        "misconception_tags": ["wishcycling_and_contamination"],
        "hints": {
            "tier_1": "Oil, grease, or different melting points ruin recycling batches.",
            "tier_2": "Contaminated bins get rejected and dumped in landfill.",
            "tier_3": f"{reason}; diverted to landfill."
        }
    }


def arch_41_landfill_management_leachate_problems(rng: random.Random) -> Dict[str, Any]:
    pollutants = [
        ("leachate", "toxic liquid that percolates through decomposing waste, carrying heavy metals and pathogens into groundwater"),
        ("methane gas (CH4)", "potent greenhouse gas produced by anaerobic decomposition of organic waste, which can also trigger landfill fires"),
    ]
    p_name, desc = rng.choice(pollutants)

    prompt = (
        f"When household waste is dumped in landfills without proper sorting, environmental hazards emerge.\n\n"
        f"1. Name the dark, toxic liquid formed when rainwater percolates through decomposing landfill waste.\n"
        f"2. Describe the risk this liquid poses to nearby rural communities relying on borehole water.\n"
        f"3. Name the flammable greenhouse gas generated inside anaerobic landfill layers."
    )
    sol = (
        f"**Step 1:** The toxic liquid is called **leachate** [1 Mark: Terminology].\n\n"
        f"**Step 2:** If the landfill lacks an impermeable lining, leachate seeps deep into underground aquifers, contaminating drinking boreholes with poisons and heavy metals [1 Mark: Water hazard].\n\n"
        f"**Step 3:** The gas produced is **methane ($CH_4$)** [1 Mark: Gas identification]."
    )
    return {
        "id": f"ns7_prop_41_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Leachate; contaminates groundwater aquifers; methane",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "41_landfill_management_leachate_problems",
        "misconception_tags": ["landfill_leachate_contamination"],
        "hints": {
            "tier_1": "Think of the polluted liquid draining from rubbish, and the swamp gas produced.",
            "tier_2": "Liquid is leachate; gas is methane.",
            "tier_3": "1. Leachate, 2. Contaminates groundwater, 3. Methane."
        }
    }


def arch_42_informal_waste_reclaimers_role(rng: random.Random) -> Dict[str, Any]:
    provinces = ["Johannesburg (Gauteng)", "Durban (KwaZulu-Natal)", "Cape Town (Western Cape)"]
    city = rng.choice(provinces)

    prompt = (
        f"In cities like {city}, thousands of informal waste pickers (waste reclaimers) collect cardboard, plastic, and metal scrap from household wheelie bins.\n\n"
        f"1. Explain the positive environmental service informal waste reclaimers provide to South African municipalities.\n"
        f"2. Identify TWO significant health or safety risks these reclaimers face during their daily work."
    )
    sol = (
        f"**Step 1:** Reclaimers divert massive tonnages of recyclable materials away from municipal landfills, extending landfill lifespan and supplying raw feedstocks to recycling plants [1 Mark: Environmental contribution].\n\n"
        f"**Step 2:** Risks (any two): cuts from broken glass and exposed needles/sharps, exposure to toxic household chemicals and rot, traffic accidents while pulling trolleys on busy roads, and extreme weather [2 Marks: Occupational risks]."
    )
    return {
        "id": f"ns7_prop_42_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Divert recyclables from landfill; cuts from glass/sharps, chemical exposure, traffic hazards",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "42_informal_waste_reclaimers_role",
        "misconception_tags": ["informal_recycling_economy"],
        "hints": {
            "tier_1": "How do reclaimers help landfills, and what dangers do they face?",
            "tier_2": "They save landfill space by collecting recyclables; they face cuts, chemicals, and traffic.",
            "tier_3": "Divert recyclable waste; risks include sharps, infection, traffic."
        }
    }


def arch_43_lifecycle_analysis_shopping_bags(rng: random.Random) -> Dict[str, Any]:
    bags = [
        ("Single-use plastic HDPE bag", "Very cheap and light, but made from fossil fuels, rarely recycled, and persists in environment for centuries"),
        ("Single-use paper bag", "Biodegradable and recyclable, but requires cutting trees, large amounts of water and energy to manufacture"),
        ("Reusable cotton tote bag", "Durable and reused hundreds of times, but requires significant water and land to grow cotton crop"),
    ]
    b1, b2 = rng.sample(bags, 2)

    prompt = (
        f"A consumer compares shopping bag options:\n"
        f"- Option A: {b1[0]}\n"
        f"- Option B: {b2[0]}\n\n"
        f"1. State ONE environmental advantage and ONE environmental disadvantage for Option A.\n"
        f"2. Explain why a reusable bag only becomes greener than single-use bags if it is reused dozens of times."
    )
    sol = (
        f"**Step 1:** Option A ({b1[0]}): {b1[1]} [1 Mark: Analysis].\n\n"
        f"**Step 2:** Reusable bags require far more energy, water, and raw material to manufacture initially; they only achieve a lower net environmental footprint per trip if used repeatedly over many shopping trips [1 Mark: Lifecycle reasoning]."
    )
    return {
        "id": f"ns7_prop_43_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Option A: {b1[1]}; high upfront production footprint requires repeated use to break even",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "43_lifecycle_analysis_shopping_bags",
        "misconception_tags": ["single_use_vs_reusable_lifecycle"],
        "hints": {
            "tier_1": "Think about raw materials used to make each bag.",
            "tier_2": "Cotton and paper take a lot of water and energy to make, so cotton must be used many times.",
            "tier_3": "Reusable bags have higher initial manufacturing cost, so they must be reused many times."
        }
    }


def arch_44_glass_recycling_closed_loop(rng: random.Random) -> Dict[str, Any]:
    temp_drop = rng.choice([300, 350, 400])
    raw_melt = 1500
    cullet_melt = raw_melt - temp_drop

    prompt = (
        f"Crushed recycled glass used in furnace smelting is called **cullet**.\n"
        f"Melting raw silica sand requires temperatures of ${raw_melt}^\\circ\\text{{C}}$, whereas cullet melts at only ${cullet_melt}^\\circ\\text{{C}}$.\n\n"
        f"1. Explain why glass is considered an ideal 'closed-loop' recyclable material compared to plastics.\n"
        f"2. Calculate the temperature difference (reduction in furnace temperature) achieved by using cullet instead of raw silica sand."
    )
    sol = (
        f"**Step 1:** Glass is 100% recyclable infinitely without any loss of purity, strength, or structural quality, whereas plastic degrades each time it is re-melted [1 Mark: Closed loop].\n\n"
        f"**Step 2:** Temperature reduction: $${raw_melt} - {cullet_melt} = \\mathbf{{{temp_drop}^\\circ\\text{{C}}}} \\text{{ [1 Mark: Calculation]}}$$"
    )
    return {
        "id": f"ns7_prop_44_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Glass can be recycled infinitely without quality loss; reduction = {temp_drop} °C",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "44_glass_recycling_closed_loop",
        "misconception_tags": ["infinite_recyclability_of_glass"],
        "hints": {
            "tier_1": "Does glass lose quality when remelted?",
            "tier_2": f"Subtract {cullet_melt} from {raw_melt}.",
            "tier_3": f"Recycled infinitely without degradation; difference is {temp_drop} °C."
        }
    }


def arch_45_paper_recycling_and_deforestation(rng: random.Random) -> Dict[str, Any]:
    trees = rng.choice([15, 17, 20])
    water_kl = rng.choice([25, 30, 35])
    tonnes = rng.choice([2, 3, 5])
    total_trees = trees * tonnes

    prompt = (
        f"Recycling $1\\text{{ tonne}}$ of waste office paper saves approximately {trees} mature trees and {water_kl}\\text{{ kL}} of water.\n\n"
        f"1. If a high school recycling campaign collects {tonnes} tonnes of paper this term, calculate how many trees are saved from being felled.\n"
        f"2. Explain how recycling paper helps conserve forest ecosystems and reduces greenhouse gases."
    )
    sol = (
        f"**Step 1:** Total trees saved: $${tonnes} \\times {trees} = \\mathbf{{{total_trees}\\text{{ trees}}}} \\text{{ [1 Mark: Calculation]}}$$\n\n"
        f"**Step 2:** Living trees absorb carbon dioxide ($CO_2$) through photosynthesis; leaving trees standing in forests preserves natural carbon sinks and wildlife biodiversity [1 Mark: Ecological benefit]."
    )
    return {
        "id": f"ns7_prop_45_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total_trees} trees; preserves standing trees to absorb CO2 through photosynthesis",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "45_paper_recycling_and_deforestation",
        "misconception_tags": ["deforestation_carbon_sink"],
        "hints": {
            "tier_1": f"Multiply {tonnes} tonnes by {trees} trees per tonne.",
            "tier_2": f"{tonnes} * {trees} = {total_trees}.",
            "tier_3": f"{total_trees} trees saved."
        }
    }


def arch_46_designing_sustainable_packaging(rng: random.Random) -> Dict[str, Any]:
    products = [
        ("fresh organic apples packaged on a Styrofoam tray wrapped in plastic clingfilm", "switch to a loose display or brown unbleached kraft paper bag", "eliminates non-biodegradable polystyrene and film"),
        ("cardboard toy box with a large clear PVC plastic window and multiple plastic cable ties", "use an all-cardboard interlocking box printed with soy-based inks", "allows entire packaging box to be placed directly into paper recycling"),
        ("liquid laundry detergent sold in thick single-use HDPE bottles", "sell concentrated refill pouches or tablet concentrates in dissolving paper sachets", "drastically reduces plastic mass per wash and cuts transport weight"),
    ]
    problem, eco_fix, benefit = rng.choice(products)

    prompt = (
        f"A packaging designer audits excessive plastic use in retail stores:\n"
        f"Problem: '{problem}'.\n\n"
        f"1. Propose an eco-friendly packaging redesign for this product.\n"
        f"2. Explain how your redesign aligns with sustainable material principles."
    )
    sol = (
        f"**Step 1:** Redesign: {eco_fix} [1 Mark: Creative design].\n\n"
        f"**Step 2:** Benefit: It {benefit} [1 Mark: Sustainability reasoning]."
    )
    return {
        "id": f"ns7_prop_46_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{eco_fix}; {benefit}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "46_designing_sustainable_packaging",
        "misconception_tags": ["overpackaging_reduction"],
        "hints": {
            "tier_1": "Can the plastic be reduced or replaced with a recyclable or biodegradable material?",
            "tier_2": "Replace multi-material packaging with simple paper or refill pouches.",
            "tier_3": f"Redesign: {eco_fix}."
        }
    }


def arch_47_evaluating_material_tradeoffs_cost_strength(rng: random.Random) -> Dict[str, Any]:
    materials = [
        ("Steel", 7.8, "Very high", "Low / affordable", "Strong and cheap, but heavy and rusts if unpainted"),
        ("Aluminium", 2.7, "Moderate to high", "Medium", "Lightweight and corrosion-resistant, but more expensive than steel"),
        ("Carbon fibre", 1.6, "Extremely high", "Very expensive", "Incredibly light and strong, but very costly and hard to recycle"),
    ]
    prompt = (
        f"A bicycle frame engineer compares three materials:\n"
        f"- Steel (Density: $7{{,}}8\\text{{ g/cm}}^3$, Tensile strength: Very high, Cost: Low)\n"
        f"- Aluminium (Density: $2{{,}}7\\text{{ g/cm}}^3$, Tensile strength: High, Cost: Medium)\n"
        f"- Carbon fibre (Density: $1{{,}}6\\text{{ g/cm}}^3$, Tensile strength: Extremely high, Cost: High)\n\n"
        f"1. Which material is best suited for an affordable commuter bike where keeping price low is critical?\n"
        f"2. Which material is chosen by professional racing cyclists where minimizing weight is paramount regardless of cost?\n"
        f"3. Explain the trade-off between material performance and financial cost."
    )
    sol = (
        f"**Step 1:** **Steel** is best for the budget commuter bike due to low cost and high durability [1 Mark: Selection].\n\n"
        f"**Step 2:** **Carbon fibre** is chosen by professional racers for minimal weight and maximum stiffness [1 Mark: Selection].\n\n"
        f"**Step 3:** High-performance materials (low density, ultra-high strength) require specialized, energy-intensive manufacturing processes, which greatly increases product retail price [1 Mark: Tradeoff]."
    )
    return {
        "id": f"ns7_prop_47_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Steel for budget; Carbon fibre for racing; higher performance involves higher manufacturing cost",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "47_evaluating_material_tradeoffs_cost_strength",
        "misconception_tags": ["engineering_material_tradeoffs"],
        "hints": {
            "tier_1": "Look at cost for commuter, and density for racing.",
            "tier_2": "Steel is cheapest; carbon fibre is lightest.",
            "tier_3": "Steel; Carbon fibre; cost increases with high-tech processing."
        }
    }


def arch_48_evaluating_material_tradeoffs_weight_insulation(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("portable camping cooler box", "expanded polystyrene lining inside rigid plastic shell", "lightweight for carrying, excellent thermal insulation, waterproof"),
        ("vacuum-insulated stainless steel flask", "double-walled stainless steel with vacuum gap", "durable against drops, zero heat conduction across vacuum, reusable"),
    ]
    item, design, reasons = rng.choice(cases)

    prompt = (
        f"Designers must balance weight, thermal insulation, and durability when building items to keep food cold or hot.\n\n"
        f"Consider: **{item}** ({design}).\n\n"
        f"1. State TWO key physical properties that make this design effective.\n"
        f"2. Explain why solid metal walls without an insulating core or vacuum would be ineffective for keeping drinks cold on a sunny day."
    )
    sol = (
        f"**Step 1:** Key physical properties: {reasons} [1 Mark: Properties].\n\n"
        f"**Step 2:** Metals are excellent thermal conductors; heat from warm outside air would conduct rapidly through solid metal into the drink, causing it to warm up quickly [1 Mark: Conduction flaw]."
    )
    return {
        "id": f"ns7_prop_48_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{reasons}; solid metal conducts heat quickly, warming the cold contents",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "48_evaluating_material_tradeoffs_weight_insulation",
        "misconception_tags": ["insulation_design_principles"],
        "hints": {
            "tier_1": "What prevents heat from entering a cold container?",
            "tier_2": "Thermal insulation stops heat conduction.",
            "tier_3": f"{reasons}; metal conducts heat too fast."
        }
    }


def arch_49_scientific_inquiry_fair_test_variables(rng: random.Random) -> Dict[str, Any]:
    tests = [
        ("Testing which fabric (cotton, wool, or nylon) absorbs the most water", "Type of fabric material", "Volume of water absorbed (mL)", "Fabric sample mass/area, immersion duration, water temperature"),
        ("Testing which metal rod (copper, brass, or iron) conducts heat fastest", "Type of metal rod", "Time taken for wax drop to melt (seconds)", "Length of rod, diameter of rod, size of wax droplet, position of Bunsen flame"),
        ("Testing which plastic strip supports the greatest weight before snapping", "Type of plastic material", "Maximum breaking load / mass supported (kg)", "Strip thickness, strip length, strip width, rate of adding weights"),
    ]
    investigation, ind_var, dep_var, ctrl_vars = rng.choice(tests)

    prompt = (
        f"A Grade 7 science group plans an investigation:\n"
        f"'{investigation}'.\n\n"
        f"1. Identify the **independent variable** (the factor changed by the experimenter).\n"
        f"2. Identify the **dependent variable** (the factor measured as the result).\n"
        f"3. State TWO **controlled variables** that must be kept constant to ensure a fair test."
    )
    sol = (
        f"**Step 1:** Independent variable: **{ind_var}** [1 Mark: Independent variable].\n\n"
        f"**Step 2:** Dependent variable: **{dep_var}** [1 Mark: Dependent variable].\n\n"
        f"**Step 3:** Controlled variables: Any two of: {ctrl_vars} [1 Mark: Controlled variables]."
    )
    return {
        "id": f"ns7_prop_49_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Independent: {ind_var}; Dependent: {dep_var}; Controlled: {ctrl_vars}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "49_scientific_inquiry_fair_test_variables",
        "misconception_tags": ["independent_vs_dependent_variable"],
        "hints": {
            "tier_1": "Independent = what you change. Dependent = what you measure.",
            "tier_2": f"Change: {ind_var}. Measure: {dep_var}.",
            "tier_3": f"Independent: {ind_var}; Dependent: {dep_var}; Controlled: {ctrl_vars}."
        }
    }


def arch_50_interpreting_data_tables_material_selection(rng: random.Random) -> Dict[str, Any]:
    rows = [
        {"name": "Material W", "density": 8.9, "thermal_cond": "High", "elec_cond": "Conductor", "flex": "Low", "cost": "High"},
        {"name": "Material X", "density": 0.9, "thermal_cond": "Very Low", "elec_cond": "Insulator", "flex": "High", "cost": "Low"},
        {"name": "Material Y", "density": 2.5, "thermal_cond": "Moderate", "elec_cond": "Insulator", "flex": "Rigid", "cost": "Moderate"},
        {"name": "Material Z", "density": 1.2, "thermal_cond": "Very Low", "elec_cond": "Insulator", "flex": "Rigid", "cost": "Low"},
    ]
    rng.shuffle(rows)

    # find which is insulator + low density for insulation
    insulator_light = [r for r in rows if r["elec_cond"] == "Insulator" and r["density"] < 1.5][0]
    conductor_metal = [r for r in rows if r["elec_cond"] == "Conductor"][0]

    tbl_text = (
        "| Material | Density (g/cm³) | Thermal Conductivity | Electrical Property | Flexibility | Relative Cost |\n"
        "| :--- | :---: | :---: | :---: | :---: | :---: |\n"
    )
    for r in rows:
        tbl_text += f"| {r['name']} | {str(r['density']).replace('.', ',')} | {r['thermal_cond']} | {r['elec_cond']} | {r['flex']} | {r['cost']} |\n"

    prompt = (
        f"A laboratory tests four candidate materials for various products:\n\n"
        f"{tbl_text}\n"
        f"1. Which material is best suited for an electrical wiring core that must conduct current efficiently?\n"
        f"2. Which material is best suited for a lightweight, flexible insulating jacket to wrap around cold pipes?\n"
        f"3. Explain why {conductor_metal['name']} would be completely unsuitable as a cold-box thermal insulator."
    )
    sol = (
        f"**Step 1:** Wiring core: **{conductor_metal['name']}** (high electrical conductivity) [1 Mark: Selection].\n\n"
        f"**Step 2:** Flexible cold-pipe jacket: **{insulator_light['name']}** (insulator, low density, high flexibility) [1 Mark: Selection].\n\n"
        f"**Step 3:** {conductor_metal['name']} has high thermal conductivity; heat would conduct straight through it, destroying the cooling effect [1 Mark: Explanation]."
    )
    return {
        "id": f"ns7_prop_50_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Wiring: {conductor_metal['name']}; Jacket: {insulator_light['name']}; {conductor_metal['name']} conducts heat too fast",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "50_interpreting_data_tables_material_selection",
        "misconception_tags": ["tabular_data_interpretation"],
        "hints": {
            "tier_1": "Look at the electrical and thermal properties in the table.",
            "tier_2": f"Conductor is {conductor_metal['name']}. Insulator with flexibility is {insulator_light['name']}.",
            "tier_3": f"1. {conductor_metal['name']}, 2. {insulator_light['name']}."
        }
    }
