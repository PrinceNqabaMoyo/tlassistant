"""Grade 7 Natural Sciences: Term 3 - Sources of Energy Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/01. Sources of energy.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "renewable_vs_nonrenewable_energy_sources",
    "fossil_fuels_formation_and_types",
    "south_african_coal_dependence_eskom",
    "environmental_impact_greenhouse_gases",
    "alternative_clean_energy_solutions"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 3/01. Sources of energy.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_renewable_vs_nonrenewable(rng: random.Random) -> Dict[str, Any]:
    sources = [
        ("Solar photovoltaic radiation from the Sun", "Renewable source", "replenished naturally on a continuous basis and cannot be permanently exhausted"),
        ("Coal mined from underground seams in Mpumalanga", "Non-renewable source", "takes hundreds of millions of years to form and will eventually be permanently depleted"),
        ("Wind kinetic energy captured by turbine blades in the Eastern Cape", "Renewable source", "replenished constantly by solar atmospheric heating and never runs out"),
        ("Crude petroleum oil extracted from offshore drilling rigs", "Non-renewable source", "a finite fossil fuel that cannot be replaced once combusted")
    ]
    src, cat, expl = rng.choice(sources)
    prompt = f"Classify **{src}** as a renewable or non-renewable energy source, and state the scientific reason."
    correct_opt = f"{cat}, because it is {expl}."
    alt_cat = "Non-renewable source" if cat == "Renewable source" else "Renewable source"
    options = [
        correct_opt,
        f"{alt_cat}, because all commercial power sources are legally classified as identical.",
        f"{alt_cat}, because solar and wind energy produce nuclear radioactive fallout.",
        "Neither, because electricity generation does not depend on natural resources."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Understand energy resource categories:\n"
        f"- Renewable: Resources replenished naturally by Earth's cycles (solar, wind, hydro, biomass).\n"
        f"- Non-renewable: Finite resources consumed faster than Earth can recreate them (coal, oil, gas, uranium).\n\n"
        f"Conclusion: {src} is a {cat} because it is {expl}."
    )
    return {
        "id": f"ns7_en_ren_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "renewable_vs_nonrenewable_energy_sources",
        "question_family_id": "renewable_vs_nonrenewable_energy_sources",
        "hints": {
            "tier_1": "Can Earth recreate this resource quickly, or will it run out forever when used up?",
            "tier_2": "Sunlight and wind are inexhaustible; coal and oil are finite fossil fuels.",
            "tier_3": f"This is classified as a {cat}."
        },
        "misconception_tags": ["renewable_clean_infinite_confusion"]
    }

def _build_fossil_fuels_formation(rng: random.Random) -> Dict[str, Any]:
    regions = [
        "the extensive Highveld coal basins of Mpumalanga",
        "the Waterberg coalfields in Limpopo",
        "the ancient Karoo basin deposits of South Africa"
    ]
    prompt = (
        f"South Africa extracts millions of tonnes of coal annually from {rng.choice(regions)}.\n\n"
        f"How did **coal deposits** in South Africa form over geological time?"
    )
    correct_opt = "Ancient swamp forests died millions of years ago, were buried under sediments, and were compressed under immense heat and pressure."
    options = [
        correct_opt,
        "Volcanic magma rapidly cooled on the surface of the ocean over the last decade.",
        "Dead dinosaur skeletons melted into black oil during ancient ice ages.",
        "Rainwater reacted with atmospheric oxygen to form solid black carbon rocks."
    ]
    rng.shuffle(options)
    sol = (
        "Formation of Coal (Carboniferous Period, ~300 million years ago):\n"
        "1. Ancient giant fern and tree swamps died in waterlogged, oxygen-poor bogs.\n"
        "2. Layers of mud, silt, and sand buried the organic matter, preventing complete decay.\n"
        "3. Over millions of years, tectonic pressure and geothermal heat drove out moisture and gases, transforming peat into lignite and bituminous coal."
    )
    return {
        "id": f"ns7_en_coal_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "fossil_fuels_formation_and_types",
        "question_family_id": "fossil_fuels_formation_and_types",
        "hints": {
            "tier_1": "Coal comes from ancient plant swamps, not dinosaur bones.",
            "tier_2": "Heat, pressure, and time over millions of years compressed the plant matter.",
            "tier_3": "Ancient swamp forests were compressed under sediment, heat, and pressure."
        },
        "misconception_tags": ["dinosaur_coal_fallacy"]
    }

def _build_sa_coal_dependence(rng: random.Random) -> Dict[str, Any]:
    stations = [
        "baseload power stations like Kendal, Matla, and Duvha in Mpumalanga",
        "modern coal stations like Medupi in Lephalale and Kusile in eMalahleni",
        "large-scale coal-fired thermal generation plants across the Highveld"
    ]
    prompt = (
        f"In South Africa, the majority of electricity generated by Eskom comes from burning pulverized coal in {rng.choice(stations)}.\n\n"
        f"State ONE historical reason for this reliance and ONE major environmental or operational challenge associated with coal-fired power stations. (4 marks)"
    )
    sample_answer = (
        "Historical reason: South Africa possesses vast, easily accessible, and inexpensive domestic bituminous coal reserves, "
        "mainly in Mpumalanga and Limpopo, which allowed the country to build large-scale baseload thermal power stations.\n"
        "Operational challenge: Burning coal generates severe atmospheric emissions (carbon dioxide, sulfur dioxide, particulate ash), "
        "consumes enormous quantities of cooling water in a water-stressed country, and relies on aging power plants that suffer breakdowns."
    )
    sol = (
        "Marking Rubric (4 marks total):\n"
        "1. Reason for dependence: Abundant, cheap domestic coal deposits in Mpumalanga/Limpopo (2 marks).\n"
        "2. Challenge: Air pollution/greenhouse gas emissions, massive water consumption, or breakdowns/maintenance backlog (2 marks)."
    )
    return {
        "id": f"ns7_en_eskom_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "subskill": "south_african_coal_dependence_eskom",
        "question_family_id": "south_african_coal_dependence_eskom",
        "hints": {
            "tier_1": "Why does SA have so many coal power stations, and what problems do they cause?",
            "tier_2": "Abundant local coal reserves provided cheap baseload; challenges include emissions and water use.",
            "tier_3": "Discuss cheap domestic coal reserves and the resulting greenhouse emissions and maintenance issues."
        },
        "misconception_tags": ["infinite_coal_assumption"]
    }

def _build_environmental_impact(rng: random.Random) -> Dict[str, Any]:
    contexts = [
        "Global emissions monitoring reveals millions of metric tonnes of CO2 discharged annually into the atmosphere.",
        "Climate scientists warn of rising global temperatures driven by heavy combustion of coal, diesel, and natural gas.",
        "Industrial energy generation relying on carbon-dense fuels releases massive plumes of carbon dioxide."
    ]
    prompt = (
        f"{rng.choice(contexts)}\n\n"
        f"What is the primary global environmental concern associated with combusting fossil fuels (coal, petrol, and gas) "
        f"for electricity and transport?"
    )
    correct_opt = "It releases massive volumes of carbon dioxide (CO2), intensifying the enhanced greenhouse effect and driving global climate change."
    options = [
        correct_opt,
        "It causes the ozone layer to turn permanently purple across the equator.",
        "It stops the Earth from rotating on its axis every 24 hours.",
        "It creates massive amounts of liquid oxygen that freeze the oceans."
    ]
    rng.shuffle(options)
    sol = (
        "Environmental Impact of Fossil Fuel Combustion:\n"
        "Combusting hydrocarbons (C + O2 -> CO2) releases trapped ancient carbon into the atmosphere as greenhouse gases. "
        "This traps outgoing infrared radiation, causing global atmospheric warming, rising sea levels, and extreme weather events."
    )
    return {
        "id": f"ns7_en_co2_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "environmental_impact_greenhouse_gases",
        "question_family_id": "environmental_impact_greenhouse_gases",
        "hints": {
            "tier_1": "Think about CO2 and the greenhouse effect.",
            "tier_2": "Combustion produces carbon dioxide which traps atmospheric heat.",
            "tier_3": "It increases CO2, causing the enhanced greenhouse effect and climate change."
        },
        "misconception_tags": ["greenhouse_ozone_confusion"]
    }

def _build_alternative_clean_energy(rng: random.Random) -> Dict[str, Any]:
    alternatives = [
        ("Solar photovoltaic farms in the Northern Cape", "abundant sunny cloudless skies (>300 days per year) generating electricity without emissions"),
        ("Wind turbine farms along the Eastern and Western Cape coastlines", "strong, consistent coastal onshore winds driving turbine generators"),
        ("Hydroelectric pumped-storage schemes (e.g. Drakensberg Pumped Storage)", "pumping water to high reservoirs at night and releasing it through turbines during peak demand")
    ]
    sol_type, adv = rng.choice(alternatives)
    prompt = f"Why is **{sol_type}** a promising alternative energy solution for South Africa?"
    correct_opt = f"It harnesses South Africa's natural geographic advantages ({adv})."
    options = [
        correct_opt,
        "It consumes more coal than standard thermal power stations.",
        "It guarantees that electricity will only work during winter nights.",
        "It replaces all electricity with wood-burning braai fires."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Renewable energy potential in South Africa:\n"
        f"South Africa has world-class solar irradiance (Northern Cape) and coastal wind regimes (Eastern/Western Cape).\n\n"
        f"Conclusion: {sol_type} is effective because {adv}."
    )
    return {
        "id": f"ns7_en_alt_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "alternative_clean_energy_solutions",
        "question_family_id": "alternative_clean_energy_solutions",
        "hints": {
            "tier_1": "Consider South Africa's climate: lots of sunshine and windy coastal plains.",
            "tier_2": "Renewables harness abundant sun and wind to generate clean electricity.",
            "tier_3": f"It harnesses SA's natural geographic conditions ({adv})."
        },
        "misconception_tags": ["renewable_unreliability_myth"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "renewable_vs_nonrenewable_energy_sources": _build_renewable_vs_nonrenewable,
        "fossil_fuels_formation_and_types": _build_fossil_fuels_formation,
        "south_african_coal_dependence_eskom": _build_sa_coal_dependence,
        "environmental_impact_greenhouse_gases": _build_environmental_impact,
        "alternative_clean_energy_solutions": _build_alternative_clean_energy
    }
    if target in builders:
        return [builders[target](rng) for _ in range(count)]
    for k, fn in builders.items():
        if target and target in k:
            return [fn(rng) for _ in range(count)]
    res = []
    for i in range(count):
        sub = SUBSKILLS[i % len(SUBSKILLS)]
        res.append(builders[sub](rng))
    return res
