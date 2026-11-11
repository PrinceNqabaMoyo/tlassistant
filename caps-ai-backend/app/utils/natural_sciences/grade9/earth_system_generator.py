"""Natural Sciences Grade 9 Term 4: The Earth as a System Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 4/01. The earth as a system.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. four_spheres_identification_and_roles: Lithosphere, Hydrosphere, Atmosphere, and Biosphere definitions and roles.
2. inter_sphere_biogeochemical_interactions: Cross-sphere matter cycles: Water cycle, carbon transfers across spheres.
3. volcanic_eruption_multisphere_impact: Volcanic eruption cascading sequence across Lithosphere, Atmosphere, Hydrosphere, Biosphere.
4. human_impact_across_earth_spheres: Anthropogenic deforestation, mining, and greenhouse emissions impacting all spheres.
5. earth_system_equilibrium_and_feedback: Open energy vs closed matter system, negative feedback loops maintaining planetary homeostasis.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "The earth as a system"
ORDERED_SUBSKILLS = [
    "four_spheres_identification_and_roles",
    "inter_sphere_biogeochemical_interactions",
    "volcanic_eruption_multisphere_impact",
    "human_impact_across_earth_spheres",
    "earth_system_equilibrium_and_feedback",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_eas"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any], term: int = 4) -> Dict[str, Any]:
    if "marking_guide" not in res and "marking_schema" in res:
        res["marking_guide"] = res["marking_schema"]
    elif "marking_schema" not in res and "marking_guide" in res:
        res["marking_schema"] = res["marking_guide"]
    res["grade"] = "9"
    res["term"] = term
    return res


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "practice",
    seed: Optional[int] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    r = random.Random(seed)
    actual_seed = seed if seed is not None else r.randint(1, 1_000_000_000)

    if subskill in ("mixed", "auto", "", None):
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]
    elif subskill in ORDERED_SUBSKILLS:
        chosen_subskill = subskill
    else:
        chosen_subskill = ORDERED_SUBSKILLS[actual_seed % len(ORDERED_SUBSKILLS)]

    # Subskill 1: Four Spheres Identification and Roles
    if chosen_subskill == "four_spheres_identification_and_roles":
        question_text = (
            "Earth scientists view our planet not as isolated parts, but as a complex, dynamic system comprised of four interconnected spheres.\n\n"
            "1. Define and describe the primary composition of each of the **four Earth spheres**:\n"
            "   • (a) The **Lithosphere (Geosphere)**\n"
            "   • (b) The **Hydrosphere**\n"
            "   • (c) The **Atmosphere**\n"
            "   • (d) The **Biosphere**\n"
            "2. State where on Earth the **Biosphere** exists in relation to the other three spheres.\n"
            "3. Why is Earth classified as a **closed system** with respect to matter, but an **open system** with respect to energy?"
        )
        sample = (
            "1. **Four Earth Spheres:**\n"
            "   • (a) **Lithosphere (Geosphere):** The solid, rocky outer layer of Earth, comprising the brittle crust and uppermost solid mantle, including mountains, continents, rocks, minerals, and oceanic floor;\n"
            "   • (b) **Hydrosphere:** All the liquid, frozen, and gaseous water on Earth, including oceans (97%), ice sheets/glaciers (cryosphere), freshwater rivers, lakes, and underground aquifers;\n"
            "   • (c) **Atmosphere:** The gaseous envelope held by gravity around Earth, composed predominantly of nitrogen (78%), oxygen (21%), and trace greenhouse gases, shielding the surface from radiation;\n"
            "   • (d) **Biosphere:** The global sum of all living organisms (plants, animals, fungi, protists, bacteria) and their organic environments;\n"
            "2. **Location of Biosphere:** The biosphere is not a separate physical layer; it occupies the dynamic **interfacial zone** where the lower atmosphere, the surface of the lithosphere, and the hydrosphere overlap and interact;\n"
            "3. **Closed vs Open System:**\n"
            "   • **Closed to Matter:** Earth does not exchange significant physical matter with outer space (except minor meteorites); all chemical atoms and nutrients must be recycled internally;\n"
            "   • **Open to Energy:** Earth constantly receives incoming solar radiation from the Sun, and continuously radiates infrared heat energy back into outer space."
        )
        marking = (
            "• 4 marks: Accurate definitions of Lithosphere [1], Hydrosphere [1], Atmosphere [1], Biosphere [1]\n"
            "• 1 mark: Biosphere exists where the other three spheres overlap [1]\n"
            "• 2 marks: Closed to matter (recycles internal atoms) [1], open to energy (receives sunlight, radiates heat) [1]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": "Earth as a System: The Four Interacting Spheres",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 4,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Lithosphere = rock/crust. Hydrosphere = all water. Atmosphere = air. Biosphere = all life.",
                "The biosphere lives where air, water, and soil meet.",
                "Earth is closed to matter (we don't get new atoms) but open to solar energy.",
            ],
            "misconception_tags": ["biosphere_is_a_separate_bubble_in_space_myth", "earth_gains_new_water_from_space_myth"],
            "learning_objective_id": "NS9.PE.20.01",
        })

    # Subskill 2: Inter-Sphere Biogeochemical Interactions
    if chosen_subskill == "inter_sphere_biogeochemical_interactions":
        cycles = [
            (
                "The Global Hydrological (Water) Cycle",
                "Solar radiation heats ocean surface water in the Hydrosphere causing evaporation into water vapour that ascends into the Atmosphere. "
                "As air cools, condensation forms clouds that precipitate rain onto the continental Lithosphere. "
                "Surface runoff flows across rocks weathering minerals, while plant roots in the Biosphere absorb groundwater and release moisture via transpiration back into the Atmosphere.",
            ),
            (
                "The Global Carbon Cycle",
                "Atmospheric CO₂ is absorbed by green plants in the Biosphere via photosynthesis to build glucose and cellulose. "
                "Marine organisms in the Hydrosphere incorporate dissolved carbonate ions into calcium carbonate seashells. "
                "When marine organisms die, sediment layers on the Lithosphere floor compress their shells over millions of years into limestone rock, which later releases CO₂ back into the Atmosphere during volcanic metamorphism.",
            ),
        ]
        chosen_cyc = cycles[actual_seed % len(cycles)]
        question_text = (
            f"Matter continuously circulates between Earth's spheres through global biogeochemical cycles.\n\n"
            f"Consider: **{chosen_cyc[0]}**.\n\n"
            "1. Trace how a single molecule or atom transitions sequentially through all **four Earth spheres** in this cycle: *Atmosphere → Hydrosphere → Lithosphere → Biosphere*.\n"
            "2. Identify the primary **external energy source** that drives this global circulation of matter.\n"
            "3. Explain what would occur to the global cycle if one of the spheres (e.g. the Biosphere through deforestation) was severely damaged."
        )
        sample = (
            f"1. **Sequential Inter-Sphere Pathway ({chosen_cyc[0]}):**\n"
            f"   {chosen_cyc[1]};\n"
            "2. **Primary Energy Driving Source:** **Solar radiant energy from the Sun** (and secondarily geothermal heat from Earth's radioactive mantle);\n"
            "3. **System Disruption (Deforestation Impact):** Removing the Biosphere's vegetation halts transpiration, causing regional atmospheric droughts and reducing rainfall. "
            "Without plant root networks anchoring the Lithosphere, flash floods from the Hydrosphere cause catastrophic soil erosion, silting rivers and destabilizing regional climate equilibrium."
        )
        marking = (
            "• 4 marks: Clear, explicit movement of matter through all 4 spheres (Atmosphere [1], Hydrosphere [1], Lithosphere [1], Biosphere [1])\n"
            "• 1 mark: Solar energy from the Sun identified as driver [1]\n"
            "• 2 marks: Valid systemic consequence of sphere disruption (drought, soil erosion, cycle breakdown) [2]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": f"Biogeochemical Cycling: {chosen_cyc[0]}",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 4,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Track how water or carbon moves from air → ocean → rocks → plants and animals.",
                "The Sun powers wind, currents, and evaporation.",
                "Breaking one sphere disrupts the whole system like dominoes.",
            ],
            "misconception_tags": ["water_cycle_only_involves_clouds_and_rain_myth", "matter_disappears_during_cycles_myth"],
            "learning_objective_id": "NS9.PE.20.02",
        })

    # Subskill 3: Volcanic Eruption Multi-Sphere Impact
    if chosen_subskill == "volcanic_eruption_multisphere_impact":
        question_text = (
            "A catastrophic volcanic eruption (such as Mount Pinatubo or Krakatoa) originates deep in the Earth but cascades through every planetary sphere.\n\n"
            "Analyze and explain the specific impact of a major explosive volcanic eruption on:\n"
            "1. The **Lithosphere** (origin and geological changes);\n"
            "2. The **Atmosphere** (emissions and climate modulation);\n"
            "3. The **Hydrosphere** (rainfall, river channels, and ocean chemistry);\n"
            "4. The **Biosphere** (immediate mortality and long-term ecological succession)."
        )
        sample = (
            "1. **Impact on Lithosphere:** Molten magma under extreme pressure fractures crustal tectonic plates, blasting craters and depositing new igneous basalt/pumice layers. "
            "Pyroclastic flows rapidly reshape topography and trigger massive landslides;\n"
            "2. **Impact on Atmosphere:** Millions of tons of fine ash, water vapour, carbon dioxide, and sulfur dioxide (SO₂) are injected into the stratosphere. "
            "The SO₂ forms reflective sulfate aerosol veils that scatter incoming solar radiation, causing temporary global dimming and planetary cooling ('volcanic winter');\n"
            "3. **Impact on Hydrosphere:** Sulfur dioxide dissolves in cloud moisture to form dilute sulfuric acid precipitation, severely acidifying freshwater streams and surface lakes. "
            "Heavy lahars (volcanic mudflows) dam river channels and alter drainage networks;\n"
            "4. **Impact on Biosphere:** Immediate devastating mortality of vegetation, wildlife, and human populations from toxic asphyxiating gases and pyroclastic surges. "
            "Over decades, however, volcanic ash weathers into exceptionally mineral-rich, fertile agricultural volcanic soils, supporting flourishing ecological succession."
        )
        marking = (
            "• 2 marks: Lithosphere: magma breaks crust [1], new igneous rock/landforms deposited [1]\n"
            "• 2 marks: Atmosphere: SO₂/ash injected into stratosphere [1], sulfate aerosols cause global cooling/dimming [1]\n"
            "• 1 mark: Hydrosphere: acid rain in lakes and mudflow river damming [1]\n"
            "• 2 marks: Biosphere: immediate mortality [1], long-term soil fertility and re-growth [1]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": "Volcanic Eruptions: Cascading Multi-Sphere Interactions",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 4,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Lithosphere: magma erupts, new rocks form.",
                "Atmosphere: ash and SO₂ block sunlight, cooling the climate.",
                "Hydrosphere: acid rain in rivers.",
                "Biosphere: plants/animals die immediately, but ash eventually makes fertile soil.",
            ],
            "misconception_tags": ["volcanoes_only_affect_the_ground_myth", "volcanic_ash_is_just_burnt_wood_ash_myth"],
            "learning_objective_id": "NS9.PE.20.03",
        })

    # Subskill 4: Human Impact Across Earth Spheres
    human_activities = [
        ("Large-scale open-cast coal mining in Mpumalanga", "stripping lithosphere overburden, releasing toxic acid mine drainage into hydrosphere streams, and air pollution"),
        ("Deforestation of tropical rainforests in the Amazon and Congo basins", "stripping biosphere canopy, triggering severe lithosphere soil erosion, and disrupting atmospheric rainfall patterns"),
        ("Intensive industrial agriculture with chemical synthetic nitrogen fertilizers", "polluting hydrosphere aquifers via eutrophication, altering lithosphere soil microbiomes, and emitting nitrous oxide into atmosphere"),
    ]
    act = human_activities[actual_seed % len(human_activities)]
    question_text = (
        f"Anthropogenic human activities exert massive systemic pressure on Earth's interconnected spheres.\n\n"
        f"Consider the activity: **{act[0]}**.\n\n"
        "1. Identify the sphere that is **directly exploited** by this activity.\n"
        "2. Explain how this activity triggers a chain reaction that contaminates or degrades the **Hydrosphere**.\n"
        "3. Explain how this activity alters the composition and temperature of the **Atmosphere**.\n"
        "4. Describe the ultimate impact on the **Biosphere** (plants, wildlife, and human food security)."
    )
    sample = (
        f"1. **Directly Exploited Sphere:** The **Lithosphere** (and adjacent Biosphere ecosystems);\n"
        "2. **Hydrosphere Degradation:** Acid Mine Drainage (AMD) containing sulfuric acid and toxic dissolved heavy metals (arsenic, lead, mercury) leaches into groundwater aquifers and rivers. "
        "This drastically lowers freshwater pH, rendering regional water supplies undrinkable and toxic to aquatic ecosystems;\n"
        "3. **Atmospheric Impact:** Combustion of mined coal releases millions of tons of **carbon dioxide (CO₂)** (accelerating the enhanced greenhouse effect and climate heating) "
        "and **sulfur dioxide (SO₂)** (forming acid rain that falls back onto distant forests and dams);\n"
        "4. **Biosphere Impact:** Destroys natural habitats, leads to biodiversity collapse and fish die-offs, while toxic heavy metals bioaccumulate in agricultural irrigation water, contaminating crops and threatening human food security and community health."
    )
    marking = (
        "• 1 mark: Directly exploited sphere identified [1]\n"
        "• 2 marks: Hydrosphere impact (AMD / heavy metal leaching / pH drop) [2]\n"
        "• 2 marks: Atmosphere impact (CO₂ greenhouse warming [1], SO₂ acid rain [1])\n"
        "• 2 marks: Biosphere impact (biodiversity loss [1], bioaccumulation in food/crops [1])\n"
        "**Total: 7 marks**"
    )
    return _normalize_res({
        "title": f"Human Impacts on Earth Systems: {act[0].split(' in ')[0]}",
        "topic": TOPIC_NAME,
        "grade": "9",
        "term": 4,
        "subskill": chosen_subskill,
        "question_type": "structured",
        "prompt": question_text,
        "question": question_text,
        "sample_answer": sample,
        "marking_guide": marking,
        "hints": [
            "Human actions on rock and land always affect water and air too.",
            "Mining causes acid water that leaks into rivers.",
            "Burning coal releases carbon dioxide into the air, driving global warming.",
        ],
        "misconception_tags": ["pollution_stays_confined_to_one_sphere_myth", "dilution_eliminates_all_toxic_mine_waste_myth"],
        "learning_objective_id": "NS9.PE.20.04",
    })

    # Subskill 5: Earth System Equilibrium and Feedback
    question_text = (
        "Earth's climate stability is maintained by dynamic balance and feedback loops between the four spheres.\n\n"
        "1. Differentiate between a **positive feedback loop** and a **negative feedback loop** in system science.\n"
        "2. Explain the **Ice-Albedo Positive Feedback Loop** occurring in the Arctic:\n"
        "   • Atmospheric warming causes polar sea ice in the Hydrosphere/Cryosphere to melt.\n"
        "   • Explain why this causes further accelerated warming of the Atmosphere and oceans.\n"
        "3. Describe one **negative feedback mechanism** that helps stabilize planetary temperatures (e.g. increased cloud cover reflection).\n"
        "4. Why do scientists warn that positive feedback loops can trigger dangerous planetary **'tipping points'**?"
    )
    sample = (
        "1. **Positive vs Negative Feedback:**\n"
        "   • **Positive Feedback Loop:** A self-reinforcing cycle where a disturbance amplifies or magnifies the initial change, pushing the system further away from equilibrium;\n"
        "   • **Negative Feedback Loop:** A self-correcting regulatory mechanism that opposes and dampens the initial disturbance, restoring the system back towards balance and stability;\n"
        "2. **Ice-Albedo Feedback Mechanism:** Highly reflective white sea ice has a high **albedo**, reflecting 85% of solar radiation back into space. "
        "As global temperatures rise and ice melts into dark open ocean water, the ocean's albedo drops to just 10%. "
        "The dark water absorbs vast amounts of solar thermal energy, warming the ocean further and causing more ice to melt, creating a runaway warming loop;\n"
        "3. **Negative Stabilizing Feedback:** Higher temperatures cause increased ocean evaporation, forming denser low-altitude white cloud decks in the atmosphere. "
        "These clouds increase planetary albedo, reflecting sunlight back into space and cooling the planet back down;\n"
        "4. **Tipping Points:** Once a positive feedback loop accelerates past a critical threshold ('tipping point'), the process becomes irreversible on human timescales, leading to runaway catastrophic environmental shifts even if greenhouse emissions are subsequently halted."
    )
    marking = (
        "• 2 marks: Positive feedback amplifies change [1], negative feedback dampens and restores equilibrium [1]\n"
        "• 2 marks: Ice melts exposing dark water [1], dark water absorbs more heat causing more ice to melt [1]\n"
        "• 2 marks: Negative feedback (more clouds reflect sunlight, cooling planet) [2]\n"
        "• 1 mark: Tipping points become irreversible runaway shifts [1]\n"
        "**Total: 7 marks**"
    )
    return _normalize_res({
        "title": "Earth System Equilibrium: Feedbacks & Tipping Points",
        "topic": TOPIC_NAME,
        "grade": "9",
        "term": 4,
        "subskill": chosen_subskill,
        "question_type": "structured",
        "prompt": question_text,
        "question": question_text,
        "sample_answer": sample,
        "marking_guide": marking,
        "hints": [
            "Positive feedback amplifies a problem (runaway loop).",
            "Negative feedback balances and stabilizes the system.",
            "Melting white ice reveals dark ocean, which absorbs more heat and melts more ice.",
        ],
        "misconception_tags": ["positive_feedback_means_good_for_the_environment_myth", "earth_system_cannot_reach_irreversible_points_myth"],
        "learning_objective_id": "NS9.PE.20.05",
    })
