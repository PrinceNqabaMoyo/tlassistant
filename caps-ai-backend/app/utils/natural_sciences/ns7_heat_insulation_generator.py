"""Grade 7 Natural Sciences: Term 3 - Heat Insulation and Energy Saving Generator.
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr7/Term 3/04. Heat insulation and energy saving.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional

SUBSKILLS = [
    "thermal_insulators_definition_and_examples",
    "vacuum_flask_design_and_mechanics",
    "passive_solar_building_design",
    "household_energy_saving_strategies",
    "animal_thermal_adaptations"
]

CURRICULUM_DOC = "curriculum_docs_auto/NaturalSciences_Gr7/Term 3/04. Heat insulation and energy saving.md"

def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()

def _build_thermal_insulators(rng: random.Random) -> Dict[str, Any]:
    materials = [
        ("Glass fibre ceiling batts", "traps pockets of still air, which is a very poor thermal conductor, preventing heat loss through the roof in winter"),
        ("Expanded polystyrene cooler box", "contains millions of microscopic trapped air bubbles that resist the conduction of heat into the cold interior"),
        ("Thick woollen winter blankets", "the crimped wool fibres trap warm air close to the human body, reducing convective and conductive heat loss"),
        ("Double-glazed window panes", "a sealed air or argon gas gap between two glass sheets prevents conductive heat transfer between inside and outside")
    ]
    mat, role = rng.choice(materials)
    prompt = f"Why is **{mat}** an effective thermal insulator?"
    correct_opt = f"Because it {role}."
    options = [
        correct_opt,
        "Because it produces its own internal electrical heat via nuclear fusion.",
        "Because it converts incoming heat into liquid water.",
        "Because it conducts thermal energy ten times faster than solid silver."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Principles of thermal insulation:\n"
        f"Gases like air are extremely poor conductors of heat if prevented from circulating.\n"
        f"Materials like {mat} work because they {role}."
    )
    return {
        "id": f"ns7_ins_mat_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "thermal_insulators_definition_and_examples",
        "question_family_id": "thermal_insulators_definition_and_examples",
        "hints": {
            "tier_1": "Think about trapped air pockets that resist heat flow.",
            "tier_2": "Air is a poor conductor; trapping it prevents conduction and convection.",
            "tier_3": f"It works because it {role}."
        },
        "misconception_tags": ["insulator_active_heating_myth"]
    }

def _build_vacuum_flask(rng: random.Random) -> Dict[str, Any]:
    users = [
        "Hikers packing hot rooibos tea on an early winter morning in the Drakensberg mountains",
        "School learners carrying cold fruit juice to sports practice on a hot summer day in Pretoria",
        "Farm workers carrying hot coffee during morning fieldwork in the Free State"
    ]
    prompt = (
        f"{rng.choice(users)} rely on a double-walled vacuum flask (Thermos) to preserve beverage temperature.\n\n"
        f"Explain in detail how the flask's design features minimise all THREE modes of heat transfer: conduction, convection, and radiation. (6 marks)"
    )
    sample_answer = (
        "1. Conduction and Convection minimised by the vacuum: The space between the inner and outer glass/steel walls is an evacuated vacuum with all air removed. Because conduction and convection both require particles to transfer thermal energy, heat cannot travel across this vacuum.\n"
        "2. Radiation minimised by silvered walls: The internal walls are coated in reflective silvering. Shiny surfaces reflect radiant infrared heat back into a hot liquid (or reflect external radiation away from a cold liquid).\n"
        "3. Convection prevented by the insulating stopper: The tight plastic or cork stopper prevents warm air/steam from rising out of the top by convection."
    )
    sol = (
        "Marking Rubric (2 marks per heat transfer mode, total 6 marks):\n"
        "1. Vacuum prevents conduction and convection because there are no particles (2 marks).\n"
        "2. Silvered reflective lining reflects infrared radiation back into flask (2 marks).\n"
        "3. Tight insulating stopper stops convective heat loss through the opening (2 marks)."
    )
    return {
        "id": f"ns7_ins_flask_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "correct_answer": sample_answer,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 6,
        "subskill": "vacuum_flask_design_and_mechanics",
        "question_family_id": "vacuum_flask_design_and_mechanics",
        "hints": {
            "tier_1": "Address each feature: vacuum, silver lining, and stopper.",
            "tier_2": "Vacuum stops conduction and convection; silver stops radiation; stopper stops convective escape.",
            "tier_3": "Explain how the vacuum, silvered lining, and stopper counteract each specific mode of heat transfer."
        },
        "misconception_tags": ["vacuum_radiation_blocking_fallacy"]
    }

def _build_passive_solar(rng: random.Random) -> Dict[str, Any]:
    locations = [
        "the interior Highveld of Gauteng and the Free State",
        "the semi-arid Great Karoo with freezing winter nights and scorching summer days",
        "suburban neighbourhoods in Bloemfontein and Kimberley"
    ]
    prompt = (
        f"Architects designing energy-efficient homes in {rng.choice(locations)} utilize passive solar building principles.\n\n"
        f"In South Africa (Southern Hemisphere), which architectural design feature allows a house to stay naturally warmer in winter and cooler in summer?"
    )
    correct_opt = "Facing main living area windows towards the North with calculated roof overhangs that block high summer sun while admitting low winter sun."
    options = [
        correct_opt,
        "Facing all windows strictly South to catch maximum direct midday sunlight in winter.",
        "Painting all external walls matte black and removing the ceiling entirely.",
        "Installing single-pane unshaded windows facing west to maximize extreme afternoon heat."
    ]
    rng.shuffle(options)
    sol = (
        "Principles of Passive Solar Building Design in the Southern Hemisphere:\n"
        "In South Africa, the sun is always in the northern sky at solar noon.\n"
        "1. North-facing windows capture maximum winter solar radiation when the sun is at a low angle.\n"
        "2. Roof overhangs shade the windows during summer when the sun is high overhead, keeping the house cool."
    )
    return {
        "id": f"ns7_ins_solar_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "passive_solar_building_design",
        "question_family_id": "passive_solar_building_design",
        "hints": {
            "tier_1": "In South Africa, which direction does the midday sun face?",
            "tier_2": "The sun is in the north in SA. North-facing windows let in winter sun.",
            "tier_3": "North-facing windows with roof overhangs provide natural seasonal temperature control."
        },
        "misconception_tags": ["south_facing_sun_confusion_southern_hemisphere"]
    }

def _build_household_energy_saving(rng: random.Random) -> Dict[str, Any]:
    strategies = [
        ("Installing an insulating geyser blanket around an electric hot water cylinder", "Reduces heat dissipation from the water tank into the surrounding roof space, saving up to 20% on geyser electricity."),
        ("Replacing standard incandescent filament lightbulbs with Light Emitting Diodes (LEDs)", "LEDs convert over 85% of electrical energy into useful light rather than wasting it as heat."),
        ("Installing thick insulated curtains and closing them at sunset in winter", "Creates an insulating dead-air buffer against cold glass window panes, preventing indoor heat loss.")
    ]
    strat, benefit = rng.choice(strategies)
    prompt = f"How does **{strat}** save household electrical energy?"
    correct_opt = benefit
    options = [
        correct_opt,
        "It eliminates the need for any electricity by generating free perpetual energy.",
        "It forces the municipal electric grid to run backwards at night.",
        "It increases thermal heat waste to heat the neighborhood."
    ]
    rng.shuffle(options)
    sol = (
        f"Energy Conservation in Households:\n"
        f"{strat} works because {benefit}"
    )
    return {
        "id": f"ns7_ins_home_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "household_energy_saving_strategies",
        "question_family_id": "household_energy_saving_strategies",
        "hints": {
            "tier_1": "Think about cutting down on wasted heat loss.",
            "tier_2": "Insulation stops heat leaking out; efficient bulbs produce light instead of heat.",
            "tier_3": f"{benefit}"
        },
        "misconception_tags": ["geyser_blanket_waste_confusion"]
    }

def _build_animal_thermal_adaptations(rng: random.Random) -> Dict[str, Any]:
    animals = [
        ("The African penguin in cold sub-Antarctic waters", "a dense double layer of waterproof, overlapping feathers and a thick subcutaneous blubber fat layer to insulate against freezing seas"),
        ("The Arctic fox in sub-zero tundra", "thick hollow fur that traps insulating air, small compact rounded ears to reduce surface-area-to-volume heat loss"),
        ("The African elephant in hot savanna climates", "enormous vascularized ear flaps that act as thermal radiators to cool blood through convection and radiation")
    ]
    animal, adaptation = rng.choice(animals)
    prompt = f"Consider **{animal}**. How does its physiological adaptation ({adaptation}) regulate body temperature?"
    correct_opt = f"It controls the rate of conductive, convective, or radiative heat transfer with the external environment."
    options = [
        correct_opt,
        "It completely stops all internal blood circulation during hot or cold weather.",
        "It allows the animal to absorb zero oxygen while staying underwater for years.",
        "It transforms the animal from a mammal into a cold-blooded reptile."
    ]
    rng.shuffle(options)
    sol = (
        f"Thermoregulation Adaptations in Animals:\n"
        f"{animal} uses {adaptation} to balance metabolic heat production with environmental heat exchange, "
        f"preventing hypothermia or hyperthermia."
    )
    return {
        "id": f"ns7_ins_anim_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "animal_thermal_adaptations",
        "question_family_id": "animal_thermal_adaptations",
        "hints": {
            "tier_1": "Does this adaptation trap heat (insulate) or shed heat (radiate)?",
            "tier_2": "Blubber and fur insulate against cold; large ears radiate heat in the heat.",
            "tier_3": "It regulates heat transfer rates with the environment."
        },
        "misconception_tags": ["blubber_food_insulation_confusion"]
    }

def generate(subskill: Optional[str] = None, count: int = 1, seed: Optional[int] = None, **kwargs: Any) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    target = str(subskill or "").strip().lower()
    builders = {
        "thermal_insulators_definition_and_examples": _build_thermal_insulators,
        "vacuum_flask_design_and_mechanics": _build_vacuum_flask,
        "passive_solar_building_design": _build_passive_solar,
        "household_energy_saving_strategies": _build_household_energy_saving,
        "animal_thermal_adaptations": _build_animal_thermal_adaptations
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
