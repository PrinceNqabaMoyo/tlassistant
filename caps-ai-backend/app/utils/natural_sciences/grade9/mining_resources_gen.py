"""Natural Sciences Grade 9 Term 4: Mining of Mineral Resources Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 4/03. Mining of mineral resources.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. ores_and_native_minerals: Ore definition, native unreactive elements (Au, Pt) vs mineral compound ores (hematite, bauxite, galena).
2. chemical_reduction_of_metal_oxides: Smelting reactions with carbon (2PbO + C -> 2Pb + CO2, 2Fe2O3 + 3C -> 4Fe + 3CO2).
3. south_african_archaeological_smelting: Mapungubwe gold rhino, Phalaborwa copper, and KZN Iron Age bloomery archaeology.
4. physical_separation_vs_chemical_refining: Density panning, magnetic separation, froth flotation vs chemical smelting.
5. environmental_impacts_and_acid_mine_drainage: Tailings dust, dolomitic sinkholes, and Acid Mine Drainage (AMD) pyrite oxidation.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Mining of mineral resources"
ORDERED_SUBSKILLS = [
    "ores_and_native_minerals",
    "chemical_reduction_of_metal_oxides",
    "south_african_archaeological_smelting",
    "physical_separation_vs_chemical_refining",
    "environmental_impacts_and_acid_mine_drainage",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_mmr"
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

    # Subskill 1: Ores and Native Minerals
    if chosen_subskill == "ores_and_native_minerals":
        ores_data = [
            ("Hematite", "Iron", "Fe2O3", "Iron(III) oxide", "Reddish-brown mineral mined in Sishen, Northern Cape"),
            ("Bauxite", "Aluminium", "Al2O3", "Aluminium oxide", "Clay-like reddish rock refined into aluminium metal"),
            ("Galena", "Lead", "PbS", "Lead(II) sulfide", "Dense metallic grey crystal mined for lead"),
            ("Malachite", "Copper", "Cu2CO3(OH)2", "Basic copper carbonate", "Vibrant green banded mineral mined for copper"),
        ]
        chosen_ore = ores_data[actual_seed % len(ores_data)]
        question_text = (
            "The Earth's crust is rich in mineral wealth, extracted by the mining industry.\n\n"
            "1. Define the geological and economic term **ore**.\n"
            "2. Explain why precious metals like **gold (Au) and platinum (Pt)** can be found in Earth's crust as pure **native elements**, "
            f"whereas metals like **{chosen_ore[1]}** must be extracted from chemical compound ores.\n"
            f"3. State the name and chemical formula of the major ore of {chosen_ore[1]}: **{chosen_ore[0]} ({chosen_ore[2]})**.\n"
            "4. What factors determine whether a subterranean mineral deposit is economically viable to mine as an ore body?"
        )
        sample = (
            "1. **Definition of an Ore:** A naturally occurring rock or sediment containing a sufficiently high concentration of valuable minerals (usually metals) "
            "that can be extracted, refined, and sold at an economic profit;\n"
            "2. **Native vs Compound Metals:** Gold and platinum are extremely unreactive (noble metals at the very bottom of the reactivity series); "
            "they do not react with oxygen, water, or sulfur over millions of years and thus remain in elemental pure form. "
            f"In contrast, {chosen_ore[1]} is chemically reactive, readily combining with oxygen or sulfur to form stable chemical compounds ({chosen_ore[3]});\n"
            f"3. **Ore Name & Formula:** **{chosen_ore[0]}** with formula **{chosen_ore[2]}**;\n"
            "4. **Economic Viability Factors:** Concentration/grade of the metal in the rock, depth and accessibility beneath the surface, current market price of the metal, "
            "transportation infrastructure, labor costs, and environmental remediation requirements."
        )
        marking = (
            "• 1 mark: Ore defined (rock with enough valuable metal to extract profitably) [1]\n"
            f"• 2 marks: Gold/platinum are unreactive noble metals [1], {chosen_ore[1]} is reactive and forms compounds [1]\n"
            f"• 1 mark: Ore name ({chosen_ore[0]}) and formula ({chosen_ore[2]}) [1]\n"
            "• 1 mark: Two economic factors (metal grade, depth, market price, extraction cost) [1]\n"
            "**Total: 5 marks**"
        )
        return _normalize_res({
            "title": f"Mineral Ores & Native Elements: {chosen_ore[0]} ({chosen_ore[1]})",
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
                "An ore is a rock with enough metal in it to mine for profit.",
                "Gold is unreactive, so it exists pure. Most metals reacted with oxygen or sulfur.",
                f"{chosen_ore[0]} is {chosen_ore[2]}, the main ore of {chosen_ore[1]}.",
            ],
            "misconception_tags": ["all_rocks_are_ores_myth", "gold_is_extracted_from_oxide_ores_myth"],
            "learning_objective_id": "NS9.PE.22.01",
        })

    # Subskill 2: Chemical Reduction of Metal Oxides
    if chosen_subskill == "chemical_reduction_of_metal_oxides":
        smelting_cases = [
            (
                "Lead(II) oxide (PbO, yellow powder) heated with carbon powder on a charcoal block using a blowpipe",
                "2PbO + C → 2Pb + CO₂",
                "Lead",
                "Carbon is more reactive than lead, removing oxygen from lead oxide to form carbon dioxide and pure shiny molten lead beads",
                "Shiny malleable silver-grey metallic bead of lead",
            ),
            (
                "Iron(III) oxide (Fe₂O₃, red hematite) heated with carbon (coke) in a blast furnace",
                "2Fe₂O₃ + 3C → 4Fe + 3CO₂",
                "Iron",
                "Carbon has a higher affinity for oxygen than iron at high temperatures, reducing iron oxide to liquid molten iron metal",
                "Molten iron tapping out at the base of the furnace",
            ),
        ]
        chosen_sm = smelting_cases[actual_seed % len(smelting_cases)]
        question_text = (
            "Smelting involves chemical reduction of metal ores at high temperatures in a furnace.\n\n"
            f"Consider the chemical reduction demonstration: **{chosen_sm[0]}**.\n\n"
            "1. Define the term **chemical reduction** in terms of oxygen transfer.\n"
            f"2. Write the **balanced chemical equation** for this smelting reaction: *{chosen_sm[1]}*.\n"
            f"3. Explain the role of **carbon (charcoal / coke)** in this extraction reaction: *{chosen_sm[3]}*.\n"
            f"4. Describe the **key observation** that confirms pure metal was extracted: *{chosen_sm[4]}*.\n"
            "5. Why can carbon reduction NOT be used to extract aluminium from aluminium oxide?"
        )
        sample = (
            "1. **Chemical Reduction Definition:** A chemical reaction in which a substance **loses oxygen atoms** (or gains electrons);\n"
            f"2. **Balanced Chemical Equation:** **{chosen_sm[1]}**;\n"
            f"3. **Role of Carbon (Reducing Agent):** Carbon acts as a **reducing agent**. Because carbon is more reactive and has a stronger chemical affinity for oxygen than {chosen_sm[2]}, "
            "it competes for and strips oxygen atoms away from the metal oxide, releasing carbon dioxide gas and freeing pure elemental metal;\n"
            f"4. **Visual Observation:** {chosen_sm[4]};\n"
            "5. **Why Carbon Cannot Reduce Aluminium:** Aluminium is significantly **more reactive than carbon**. The chemical bond between aluminium and oxygen in Al₂O₃ is far too strong for carbon to break; "
            "aluminium can only be extracted through electrolytic decomposition (electrolysis of molten cryolite)."
        )
        marking = (
            "• 1 mark: Reduction defined as loss of oxygen [1]\n"
            f"• 2 marks: Correct balanced equation ({chosen_sm[1]}) [2]\n"
            f"• 1 mark: Carbon acts as reducing agent stripping oxygen because it is more reactive [1]\n"
            f"• 1 mark: Observation ({chosen_sm[4]}) [1]\n"
            "• 1 mark: Aluminium is more reactive than carbon / bonds too strong, requires electrolysis [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": f"Chemical Reduction & Smelting: {chosen_sm[2]} Extraction",
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
                "Reduction means removing oxygen from a compound.",
                "Carbon steals the oxygen because it is more reactive than lead or iron.",
                "Aluminium is more reactive than carbon, so carbon cannot reduce it (electrolysis needed).",
            ],
            "misconception_tags": ["carbon_adds_oxygen_to_metals_myth", "all_metals_can_be_extracted_with_carbon_myth"],
            "learning_objective_id": "NS9.PE.22.02",
        })

    # Subskill 3: South African Archaeological Smelting
    if chosen_subskill == "south_african_archaeological_smelting":
        question_text = (
            "Archaeological discoveries across Southern Africa prove that indigenous African societies possessed sophisticated metallurgical technologies long before European arrival.\n\n"
            "1. Identify the world-famous archaeological kingdom on the Limpopo River (1075–1220 AD) renowned for its master goldsmiths, "
            "and name the iconic gold foil animal figurine excavated from its royal graves.\n"
            "2. Describe the traditional indigenous technique used by Mapungubwe metalworkers to smelt gold and manufacture ornate foil jewelry.\n"
            "3. Identify the ancient copper mining and smelting settlement in Limpopo Province that has been continuously mined for centuries.\n"
            "4. Describe how indigenous Iron Age communities in KwaZulu-Natal and Mpumalanga constructed **clay bloomery furnaces** to smelt iron ore using wood charcoal and animal skin bellows."
        )
        sample = (
            "1. **Archaeological Kingdom & Figurine:** The **Kingdom of Mapungubwe** (in the Limpopo Valley); the iconic artifact is the **Golden Rhinoceros of Mapungubwe** (carved wood covered in beaten gold foil held with tiny gold tacks);\n"
            "2. **Mapungubwe Goldsmithing Technique:** Gold was collected from alluvial gravels or shallow quartz reef workings. "
            "Artisans melted gold dust inside clay crucibles in high-temperature charcoal fires, poured small gold beads, and expertly hammered (annealed) them into paper-thin gold foils, "
            "which were intricately incised and wrapped around carved wooden ceremonial sceptres and animal figures;\n"
            "3. **Ancient Copper Mining Site:** **Phalaborwa** (in eastern Limpopo), where ancient Sotho-speaking metalworkers mined copper ores from carbonatite pipes in conical pits and smelted refined copper ingots traded across ancient Indian Ocean networks;\n"
            "4. **Indigenous Clay Bloomery Furnaces:**\n"
            "   • Communities built vertical cylindrical furnaces out of ant-hill clay;\n"
            "   • Alternating layers of crushed iron ore (hematite/magnetite) and hardwood charcoal (acacia fuel) were packed inside;\n"
            "   • Clay pipes (tuyères) inserted into the base were pumped with cowhide or goatskin bellows to blast oxygen and reach 1200 °C;\n"
            "   • Carbon monoxide reduced the ore into a spongy metallic iron mass ('bloom'), which smiths reheated and forged into hoes, spears, and axes."
        )
        marking = (
            "• 2 marks: Mapungubwe [1], Golden Rhinoceros figurine [1]\n"
            "• 1 mark: Melting in clay crucibles and hammering into beaten gold foil [1]\n"
            "• 1 mark: Phalaborwa copper mining identified [1]\n"
            "• 2 marks: Clay furnace with charcoal/ore layers [1], skin bellows blasting air through pipes to produce iron bloom [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Indigenous African Metallurgy: Mapungubwe & Iron Age Blooms",
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
                "Mapungubwe in Limpopo is famous for the Golden Rhinoceros.",
                "Phalaborwa is famous for historic indigenous copper mining.",
                "Traditional iron smelters used clay furnaces, charcoal, and leather bellows to smelt iron bloom.",
            ],
            "misconception_tags": ["african_societies_had_no_metallurgy_myth", "mapungubwe_imported_all_gold_myth"],
            "learning_objective_id": "NS9.PE.22.03",
        })

    # Subskill 4: Physical Separation vs Chemical Refining
    if chosen_subskill == "physical_separation_vs_chemical_refining":
        question_text = (
            "Extracted ore contains large quantities of worthless waste rock (gangue) that must be removed before refining.\n\n"
            "1. Differentiate fundamentally between **physical separation methods** and **chemical extraction/refining methods** in mineral processing.\n"
            "2. Describe how **gravity panning** exploits differences in physical density to separate alluvial gold flakes from river sand and gravel.\n"
            "3. Describe how **magnetic separation** is used to separate magnetic iron ore (magnetite) from non-magnetic quartz sand.\n"
            "4. Explain the principle of **froth flotation** in concentrating copper sulfide ores."
        )
        sample = (
            "1. **Physical vs Chemical Processing:**\n"
            "   • **Physical Separation:** Concentrates the valuable mineral by exploiting physical property differences (density, magnetism, surface wettability) without altering the chemical molecular formula of the mineral;\n"
            "   • **Chemical Refining:** Involves chemical bond-breaking reactions (smelting, acid leaching, electrolysis) to convert the mineral compound into pure elemental metal;\n"
            "2. **Gravity Panning Principle:** Gold is exceptionally dense (density ≈ 19.3 g/cm³), while river sand/gravel has a density of only 2.6 g/cm³. "
            "When the pan is swirled with water, lighter sand particles are suspended and washed over the rim, leaving dense gold grains settled in the bottom ridges;\n"
            "3. **Magnetic Separation:** Crushed ore passes on a conveyor belt over a magnetic pulley roller. "
            "Magnetic iron minerals are attracted to the magnet and carried underneath into a separate collection chute, while non-magnetic gangue rock falls straight off into waste bins;\n"
            "4. **Froth Flotation Principle:** Finely milled ore is mixed with water, frothing agents, and collectors in a tank. "
            "Air is bubbled through the mixture; hydrophobic copper sulfide particles adhere to ascending air bubbles and float to the surface as a mineral-rich foam, while hydrophilic gangue sinks."
        )
        marking = (
            "• 2 marks: Physical exploits physical properties without bond breaking [1], chemical uses chemical reactions to liberate metal [1]\n"
            "• 1 mark: Density difference: dense gold settles while lighter sand washes away [1]\n"
            "• 1 mark: Magnetic roller pulls magnetic magnetite away from non-magnetic gangue [1]\n"
            "• 2 marks: Air bubbles attach to treated hydrophobic copper particles, floating to surface as froth [2]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Ore Beneficiation: Physical Concentration vs Chemical Refining",
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
                "Physical separation does not change chemical bonds (density, magnetism).",
                "Panning works because gold is 7 times denser than sand.",
                "Froth flotation floats bubbles with copper to the top of the tank.",
            ],
            "misconception_tags": ["panning_is_a_chemical_reaction_myth", "all_metals_float_on_water_myth"],
            "learning_objective_id": "NS9.PE.22.04",
        })

    # Subskill 5: Environmental Impacts and Acid Mine Drainage
    question_text = (
        "Mining is a major economic cornerstone of South Africa, but historically caused massive environmental degradation.\n\n"
        "1. Explain the scientific formation mechanism of **Acid Mine Drainage (AMD)** in the Witwatersrand gold fields and Mpumalanga coal basins:\n"
        "   • Identify the common mineral involved (iron pyrite, FeS₂);\n"
        "   • Explain what happens when this mineral is exposed to underground water and atmospheric oxygen.\n"
        "2. What makes Acid Mine Drainage so devastating to aquatic ecosystems and groundwater aquifers?\n"
        "3. Explain why un-rehabilitated yellow **mine tailing dumps (slime dams)** in Johannesburg present severe respiratory health hazards to surrounding communities.\n"
        "4. Describe how underground dewatering of gold mines can trigger catastrophic **sinkholes** in dolomitic rock areas."
    )
    sample = (
        "1. **AMD Formation Mechanism:**\n"
        "   • Gold and coal deposits are naturally surrounded by **iron pyrite (FeS₂, 'fool's gold')**;\n"
        "   • When underground mining tunnels expose deep pyrite beds to **atmospheric oxygen and infiltrating water**, the pyrite oxidizes chemically:\n"
        "     2FeS₂ + 7O₂ + 2H₂O → 2Fe²⁺ + 4SO₄²⁻ + 4H⁺\n"
        "     This produces high concentrations of dilute **sulfuric acid (H₂SO₄)** and dissolved iron;\n"
        "2. **Ecological Toxicity:** The hyper-acidic water (pH 2–3) dissolves and leaches toxic heavy metals (arsenic, cadmium, lead, uranium) out of underground rocks. "
        "When it decants into streams, it poisons fish, burns aquatic vegetation, precipitates heavy orange-yellow iron sludge ('yellow boy') that suffocates riverbeds, and renders drinking water undrinkable;\n"
        "3. **Tailing Dump Respiratory Hazards:** Fine silica dust containing trace cyanide and radioactive uranium is blown off dry tailing dumps by high winds into nearby residential townships. "
        "Inhaling crystalline silica dust causes irreversible lung diseases (silicosis) and exacerbates chronic asthma in children;\n"
        "4. **Dolomitic Sinkholes:** Pumping groundwater out of deep mines lowers the water table in overlying soluble dolomitic limestone rock. "
        "Water that previously provided buoyant hydrostatic support to subterranean caverns is removed, causing subterranean cavern roofs to collapse suddenly into catastrophic ground sinkholes."
    )
    marking = (
        "• 2 marks: Iron pyrite (FeS₂) [1] oxidizes with air and water to form sulfuric acid [1]\n"
        "• 2 marks: Hyper-acidic water leaches toxic heavy metals/uranium [1], sterilizes rivers and poisons drinking water [1]\n"
        "• 1 mark: Wind blown silica dust causes respiratory illnesses (silicosis/asthma) [1]\n"
        "• 2 marks: Lowering water table removes buoyant support in soluble dolomite [1], triggering cavern collapse/sinkholes [1]\n"
        "**Total: 7 marks**"
    )
    return _normalize_res({
        "title": "Acid Mine Drainage (AMD), Tailings & Mining Environmental Hazards",
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
            "Pyrite (FeS₂) + Oxygen + Water = Sulfuric acid (AMD).",
            "Acid mine water dissolves toxic heavy metals and uranium.",
            "Mine dust causes silicosis. Pumping groundwater out can cause dolomitic sinkholes.",
        ],
        "misconception_tags": ["acid_mine_drainage_is_just_dirty_muddy_water_myth", "mine_dumps_are_harsh_sand_with_no_chemicals_myth"],
        "learning_objective_id": "NS9.PE.22.05",
    })
