"""Natural Sciences Grade 9 Term 4: The Lithosphere Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 4/02. Lithosphere.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. concentric_layers_of_the_earth: Four concentric layers: Crust, Mantle, Outer Core, Inner Core; radial ordering and compositions.
2. rock_cycle_three_classes: Three rock families: Igneous, Sedimentary, Metamorphic; definitions and cyclical transitions.
3. cooling_rate_and_crystal_size: Igneous dynamics: crystal size inversely related to cooling rate (rapid extrusive vs slow intrusive).
4. sedimentary_lithification_and_fossils: Weathering, erosion, deposition, compaction, cementation; why fossils only exist in sedimentary rocks.
5. metamorphic_transformation_pathways: Protolith transformations (Limestone -> Marble, Shale -> Slate, Sandstone -> Quartzite).
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Lithosphere"
ORDERED_SUBSKILLS = [
    "concentric_layers_of_the_earth",
    "rock_cycle_three_classes",
    "cooling_rate_and_crystal_size",
    "sedimentary_lithification_and_fossils",
    "metamorphic_transformation_pathways",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_lit"
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

    # Subskill 1: Concentric Layers of the Earth
    if chosen_subskill == "concentric_layers_of_the_earth":
        question_text = (
            "The internal structure of the Earth consists of four distinct concentric layers organized by density.\n\n"
            "1. List the **four concentric layers of the Earth** in sequential order from the surface down to the center (r_crust > r_mantle > r_outer_core > r_inner_core).\n"
            "2. Contrast the physical state and chemical composition of the **Crust** with the **Mantle**.\n"
            "3. Differentiate between the **Outer Core** and the **Inner Core** in terms of physical state (liquid vs solid) and explain why the inner core remains solid despite having temperatures exceeding 5500 °C.\n"
            "4. Which layer is directly responsible for generating Earth's planetary geomagnetic field?"
        )
        sample = (
            "1. **Concentric Earth Layers (Surface to Center):**\n"
            "   1. **Crust** (outermost rigid solid shell);\n"
            "   2. **Mantle** (thickest semi-molten silicate layer);\n"
            "   3. **Outer Core** (dense liquid metal layer);\n"
            "   4. **Inner Core** (solid metal ball at the center);\n"
            "2. **Crust vs Mantle:**\n"
            "   • **Crust:** Cold, thin (5–70 km), brittle solid rock composed primarily of lightweight silicates, aluminium, and oxygen (granite and basalt);\n"
            "   • **Mantle:** Immense layer (2900 km thick) of dense, hot silicate rock rich in iron and magnesium. Its upper asthenosphere behaves as a plastic, semi-solid fluid that slowly convects;\n"
            "3. **Outer Core vs Inner Core:**\n"
            "   • **Outer Core:** **Liquid molten metal** composed of iron and nickel;\n"
            "   • **Inner Core:** **Solid metal sphere** of iron and nickel. It remains solid despite scorching 5500 °C temperatures because the **unimaginable lithostatic pressure** exerted by the entire weight of the overlying planet forces the iron-nickel atoms into a tightly packed crystalline lattice, preventing melting;\n"
            "4. **Geomagnetic Generator:** The churning liquid convection currents of conductive molten iron in the **Outer Core** act as a planetary geodynamo, generating Earth's magnetic field."
        )
        marking = (
            "• 2 marks: Four layers correctly ordered from surface to center (Crust, Mantle, Outer Core, Inner Core) [2]\n"
            "• 2 marks: Crust (thin, brittle solid silicate) vs Mantle (thick, dense, semi-solid convecting silicate) [2]\n"
            "• 2 marks: Outer core liquid iron/nickel [1], Inner core solid due to extreme confining pressure [1]\n"
            "• 1 mark: Outer core liquid iron convection generates geomagnetic field [1]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": "Earth's Concentric Layers: Geodynamo & Core Physics",
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
                "Layers from outside in: Crust → Mantle → Outer Core → Inner Core.",
                "Outer core is liquid iron-nickel; inner core is solid iron-nickel.",
                "The inner core is solid because of crushing pressure, and the liquid outer core makes Earth's magnetic field.",
            ],
            "misconception_tags": ["mantle_is_a_raging_lake_of_pure_liquid_magma_myth", "earth_is_hollow_myth"],
            "learning_objective_id": "NS9.PE.21.01",
        })

    # Subskill 2: Rock Cycle Three Classes
    if chosen_subskill == "rock_cycle_three_classes":
        question_text = (
            "All rocks on Earth are continuously formed, broken down, and transformed through the dynamic Rock Cycle.\n\n"
            "1. Define the **three major rock families** based on their geological mode of formation:\n"
            "   • (a) **Igneous rocks**\n"
            "   • (b) **Sedimentary rocks**\n"
            "   • (c) **Metamorphic rocks**\n"
            "2. Describe the step-by-step geological pathway by which an **igneous rock** (like granite) can be transformed into a **sedimentary rock** (like sandstone).\n"
            "3. Describe how that sedimentary rock can subsequently transform into a **metamorphic rock** (like quartzite).\n"
            "4. What final geological event turns metamorphic rock back into an igneous rock?"
        )
        sample = (
            "1. **Three Rock Families:**\n"
            "   • (a) **Igneous Rocks:** Formed from the cooling and solidification of molten rock (magma beneath the surface or lava on the surface);\n"
            "   • (b) **Sedimentary Rocks:** Formed from the accumulation, compaction, and cementation of mineral particles and rock fragments (sediments) or organic remains over geological time;\n"
            "   • (c) **Metamorphic Rocks:** Formed when pre-existing parent rocks are subjected to extreme subterranean heat and tectonic pressure, altering their crystal structure and mineralogy without melting;\n"
            "2. **Igneous to Sedimentary Pathway:**\n"
            "   • The granite on the surface undergoes **weathering** (broken into mineral grains by rain, freeze-thaw, and wind);\n"
            "   • Grains are **eroded and transported** by rivers into lakes or ocean basins;\n"
            "   • Layers of sand are **deposited**, and over millions of years, overlying sediment pressure causes **compaction and cementation** into sandstone;\n"
            "3. **Sedimentary to Metamorphic Pathway:** Tectonic plate subduction or nearby magma intrusions subject the sandstone to **intense heat and crushing pressure**, causing quartz grains to recrystallize and fuse into durable **quartzite**;\n"
            "4. **Return to Igneous:** If the metamorphic rock is pushed even deeper into the asthenosphere, temperatures exceed its melting point. It completely **melts into molten magma**, which upon cooling solidifies into a brand-new igneous rock."
        )
        marking = (
            "• 3 marks: Definitions of Igneous [1], Sedimentary [1], and Metamorphic rocks [1]\n"
            "• 2 marks: Igneous to Sedimentary (weathering/erosion [1], deposition/compaction/cementation [1])\n"
            "• 1 mark: Sedimentary to Metamorphic (intense heat and pressure recrystallizes without melting) [1]\n"
            "• 1 mark: Complete melting into magma and subsequent cooling/crystallisation [1]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": "The Dynamic Rock Cycle: Tripartite Transformations",
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
                "Igneous = cooled magma/lava. Sedimentary = cemented layers. Metamorphic = changed by heat and pressure.",
                "Weathering + erosion + compaction turns igneous into sedimentary.",
                "Heat and pressure turn sedimentary into metamorphic. Complete melting resets the cycle to igneous.",
            ],
            "misconception_tags": ["rocks_never_change_myth", "metamorphic_rocks_must_melt_first_myth"],
            "learning_objective_id": "NS9.PE.21.02",
        })

    # Subskill 3: Cooling Rate and Crystal Size
    if chosen_subskill == "cooling_rate_and_crystal_size":
        rock_pairs = [
            ("Granite (intrusive / plutonic)", "Basalt (extrusive / volcanic)", "coarse-grained with large visible interlocking pink, grey, and black crystals", "fine-grained with microscopic crystals and a uniform dark grey/black texture"),
            ("Gabbro (intrusive / plutonic)", "Pumice / Obsidian (extrusive / volcanic)", "large coarse dark pyroxene and plagioclase crystals", "glassy with zero crystals (obsidian) or highly vesicular porous foam (pumice)"),
        ]
        chosen_pair = rock_pairs[actual_seed % len(rock_pairs)]
        question_text = (
            "The physical texture and crystal grain size of an igneous rock are dictated by its thermal cooling history.\n\n"
            f"Compare the two igneous rocks: **{chosen_pair[0]}** versus **{chosen_pair[1]}**.\n\n"
            "1. State the mathematical/physical relationship between the **cooling time (t)** of molten rock and the resulting **mineral crystal size (s)**.\n"
            f"2. Explain where and at what rate **{chosen_pair[0]}** solidified, and describe its resulting visual crystal texture: *{chosen_pair[2]}*.\n"
            f"3. Explain where and at what rate **{chosen_pair[1]}** solidified, and describe its resulting visual crystal texture: *{chosen_pair[3]}*.\n"
            "4. Why does volcanic obsidian glass possess zero mineral crystals?"
        )
        sample = (
            "1. **Cooling Rate vs Crystal Size Relationship:** Crystal size (s) is **inversely proportional to the cooling rate** (and directly proportional to cooling time, s ∝ t). "
            "Slower cooling allows atoms more time to migrate and bond to growing crystal lattices, producing large crystals;\n"
            f"2. **Intrusive Formation ({chosen_pair[0]}):** Solidified deep underground inside the Earth's crust (plutonic). "
            f"Surrounded by thick rock that acts as a thermal insulator, magma cools **extremely slowly over hundreds of thousands of years**, resulting in {chosen_pair[2]};\n"
            f"3. **Extrusive Formation ({chosen_pair[1]}):** Solidified on the surface of the Earth after erupting from a volcano (volcanic). "
            f"Exposed directly to cold atmospheric air or ocean water, lava cools **extremely rapidly in hours or days**, freezing crystal growth early to produce {chosen_pair[3]};\n"
            "4. **Obsidian Glass Mechanism:** Obsidian forms when silica-rich lava cools instantaneously (quenched) upon contact with water or air. "
            "Cooling is so instantaneous that atoms are frozen in disordered liquid positions before they can organize into crystalline mineral lattices."
        )
        marking = (
            "• 1 mark: Slower cooling produces larger crystals / crystal size directly proportional to cooling time [1]\n"
            f"• 2 marks: Intrusive cools slowly underground [1], large coarse interlocking crystals ({chosen_pair[2]}) [1]\n"
            f"• 2 marks: Extrusive cools rapidly on surface [1], microscopic fine-grained texture ({chosen_pair[3]}) [1]\n"
            "• 1 mark: Quenched instantaneously, atoms freeze before forming crystalline lattices [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": f"Igneous Textures: Cooling Rates ({chosen_pair[0].split(' ')[0]} vs {chosen_pair[1].split(' ')[0]})",
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
                "Slow cooling underground = big visible crystals (intrusive, like granite).",
                "Fast cooling on surface = tiny crystals (extrusive, like basalt).",
                "Obsidian cooled so instantly that crystals had zero time to form.",
            ],
            "misconception_tags": ["all_igneous_rocks_have_identical_crystals_myth", "granite_cooled_on_the_surface_myth"],
            "learning_objective_id": "NS9.PE.21.03",
        })

    # Subskill 4: Sedimentary Lithification and Fossils
    if chosen_subskill == "sedimentary_lithification_and_fossils":
        question_text = (
            "Sedimentary rocks form through a continuous, multi-stage geological process known as lithification.\n\n"
            "1. Sequence the **five geological stages** of sedimentary rock formation in correct chronological order:\n"
            "   *Deposition, Weathering, Compaction, Erosion & Transport, Cementation*.\n"
            "2. Distinguish between the role of **compaction** (lithostatic overburden pressure) and **cementation** (mineral precipitation) in lithification.\n"
            "3. Name **three examples** of common sedimentary rocks (e.g. clastic, organic, chemical).\n"
            "4. Explain why **fossils of prehistoric organisms** are found almost exclusively in sedimentary rocks, and are virtually never found in igneous or metamorphic rocks."
        )
        sample = (
            "1. **Chronological Sequence:**\n"
            "   1. **Weathering** (breakdown of pre-existing rocks by physical and chemical agents);\n"
            "   2. **Erosion & Transport** (movement of particles by wind, rivers, or glaciers);\n"
            "   3. **Deposition** (sediment particles settle into horizontal layers in low-energy floodplains or sea basins);\n"
            "   4. **Compaction** (weight of accumulating overlying layers presses down, squeezing pore spaces and expelling trapped water);\n"
            "   5. **Cementation** (dissolved groundwater minerals like calcite or silica precipitate into pore spaces, gluing sediment grains together into solid rock);\n"
            "2. **Compaction vs Cementation:** Compaction mechanically squeezes sediment grains tightly together under pressure; cementation chemically glues and bonds the grains with precipitated mineral crystals;\n"
            "3. **Three Sedimentary Examples:** **Sandstone**, **Shale / Mudstone**, and **Limestone** (or Coal / Conglomerate);\n"
            "4. **Fossil Preservation Exclusivity:** Dead organisms sink into soft, calm aquatic sediments and are rapidly buried, shielding them from scavengers and oxygen decomposition, preserving bones/shells as sediment gently hardens. "
            "In contrast, the scorching 1000 °C heat of molten **igneous** magma incinerates organic remains instantly, while the crushing tectonic pressures and shearing heat of **metamorphic** formation deform and obliterate fossil skeletons."
        )
        marking = (
            "• 2 marks: Correct 5-stage chronological order (Weathering → Erosion → Deposition → Compaction → Cementation) [2]\n"
            "• 1 mark: Compaction presses grains together [1], cementation glues them with minerals [1]\n"
            "• 1 mark: Three valid examples named (sandstone, shale, limestone, coal) [1]\n"
            "• 2 marks: Sedimentary buries and protects gently [1], igneous magma burns/incinerates fossils, metamorphic crushing destroys them [1]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": "Lithification Stages & Fossil Preservation in Sedimentary Rocks",
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
                "Order: Weathering → Erosion → Deposition → Compaction → Cementation.",
                "Compaction squeezes grains; cementation glues them with mineral crystals.",
                "Fossils survive only in sedimentary rock because magma melts them and metamorphism crushes them.",
            ],
            "misconception_tags": ["fossils_can_be_found_in_granite_myth", "sediments_turn_into_rock_instantly_myth"],
            "learning_objective_id": "NS9.PE.21.04",
        })

    # Subskill 5: Metamorphic Transformation Pathways
    pathways = [
        ("Sedimentary Limestone (calcium carbonate, CaCO₃)", "Metamorphic Marble", "coarse interlocking calcite crystals, smooth surface prized for sculptures, effervesces with acid"),
        ("Sedimentary Shale / Mudstone (fine clay layers)", "Metamorphic Slate", "dense foliated rock that splits into smooth, impermeable flat sheets used for roofing tiles"),
        ("Sedimentary Sandstone (quartz sand grains)", "Metamorphic Quartzite", "extremely hard, non-porous interlocking quartz crystals that fracture across grains"),
        ("Igneous Granite (coarse intrusive feldspar, quartz, mica)", "Metamorphic Gneiss ('nice')", "distinct alternating light and dark banded mineral foliation stripes due to intense directional pressure"),
    ]
    p = pathways[actual_seed % len(pathways)]
    question_text = (
        "Metamorphism transforms pre-existing parent rocks (protoliths) through subterranean heat, pressure, and hydrothermal fluids.\n\n"
        f"Consider the specific transformation pathway: **{p[0]} → {p[1]}**.\n\n"
        f"1. Name the original **parent rock (protolith)**: *{p[0].split(' (')[0]}*.\n"
        f"2. Name the resulting **metamorphic rock**: *{p[1].split(' (')[0]}*.\n"
        "3. Explain the subterranean conditions of **temperature and pressure** required to drive this transformation without completely melting the rock.\n"
        f"4. Describe **two key physical or structural differences** in texture and durability between the parent rock and the metamorphic daughter rock: *{p[2]}*."
    )
    sample = (
        f"1. **Protolith:** **{p[0].split(' (')[0]}**;\n"
        f"2. **Metamorphic Rock:** **{p[1].split(' (')[0]}**;\n"
        "3. **Metamorphic Conditions:** Temperatures between **300 °C and 700 °C** and intense lithostatic/tectonic pressures (hundreds of Megapascals) deep in the lower crust. "
        "The heat softens the rock and mobilizes atomic diffusion, permitting mineral recrystallization and reorientation in the solid state **without ever reaching the melting point** of magma;\n"
        f"4. **Texture & Durability Differences:** {p[2]}. The metamorphic rock is significantly more compact, has vastly lower porosity, higher mechanical hardness, and reoriented interlocking crystalline boundaries."
    )
    marking = (
        f"• 1 mark: Correct protolith identified ({p[0].split(' (')[0]}) [1]\n"
        f"• 1 mark: Correct metamorphic rock ({p[1].split(' (')[0]}) [1]\n"
        "• 2 marks: High temperature (300-700 °C) and intense pressure [1], recrystallization occurs in the solid state without melting [1]\n"
        f"• 2 marks: Two accurate physical differences ({p[2]}) [2]\n"
        "**Total: 6 marks**"
    )
    return _normalize_res({
        "title": f"Metamorphic Protolith Pathways: {p[0].split(' (')[0]} to {p[1].split(' ')[1]}",
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
            "Limestone turns into Marble.",
            "Shale turns into Slate. Sandstone turns into Quartzite. Granite turns into Gneiss.",
            "Metamorphism happens under intense heat and pressure WITHOUT melting.",
        ],
        "misconception_tags": ["marble_is_sedimentary_myth", "slate_is_an_igneous_rock_myth"],
        "learning_objective_id": "NS9.PE.21.05",
    })
