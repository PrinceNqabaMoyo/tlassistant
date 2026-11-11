"""Grade 9 Natural Sciences - The Lithosphere: Archetypes 01 to 25.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr9/Term 4/02. The lithosphere.md
Focus:
Concentric layers of the Earth (crust, mantle, core, dimensions, lithosphere vs asthenosphere, geodynamo),
Igneous rocks (magma vs lava, intrusive vs extrusive, granite, basalt, pumice, obsidian),
Sedimentary rocks (weathering, erosion, deposition, lithification, clastic vs chemical/organic, fossil preservation),
Metamorphic rocks (heat & pressure recrystallization, protolith transformations: shale->slate, limestone->marble,
sandstone->quartzite, granite->gneiss).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_01_earth_internal_structure_crust_mantle_core_dimensions(rng: random.Random) -> Dict[str, Any]:
    layer_info = rng.choice([
        ("Crust", "the thinnest, outermost rigid solid shell varying in thickness from ~5 km under oceans to ~70 km beneath high mountain ranges"),
        ("Mantle", "the thickest silicate layer (~2900 km thick) comprising about 84% of Earth's total planetary volume"),
        ("Outer Core", "a molten liquid layer (~2200 km thick) composed primarily of churning metallic iron and nickel"),
        ("Inner Core", "a solid metallic sphere with a radius of approximately 1220 km at the center of the Earth")
    ])
    layer_name, desc = layer_info
    prompt = (
        "Earth's interior is arranged in concentric spherical layers organized according to density.\n\n"
        f"Which statement accurately describes the dimensions and state of the **{layer_name}**?"
    )
    correct = f"It is {desc}."
    distractors = [
        "It is a gaseous shell of atmospheric ozone floating above the stratosphere.",
        "It is a layer of pure frozen water ice that covers the Earth's mantle.",
        "It is an artificial concrete vault constructed beneath continental tectonic plates."
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "Step 1: Concentric layers of Earth from surface to center:\n"
        "1. Crust (5–70 km), 2. Mantle (~2900 km, ~84% volume), 3. Outer Core (~2200 km liquid metal), 4. Inner Core (~1220 km radius solid metal).\n"
        f"Step 2: Characteristics of {layer_name}:\n"
        f"The {layer_name} is {desc}."
    )
    return {
        "id": f"ns9_lith_01_{rng.randint(100000, 999999)}",
        "subskill": "01_earth_internal_structure_crust_mantle_core_dimensions",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Recall the thickness and physical state of the {layer_name}.",
            "tier_2": f"It is {desc[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["earth_internal_concentric_layers"]
    }


def arch_02_continental_crust_vs_oceanic_crust_contrast(rng: random.Random) -> Dict[str, Any]:
    crust_type = rng.choice(["continental crust", "oceanic crust"])
    if crust_type == "continental crust":
        desc = "thicker (30 to 70 km), less dense (~2,7 g/cm³), primarily granitic (sial: rich in silica and aluminium), and geologically older"
        distractor = "thinner (5 to 10 km), denser (~3,0 g/cm³), primarily basaltic (sima: rich in silica and magnesium), and geologically younger"
    else:
        desc = "thinner (5 to 10 km), denser (~3,0 g/cm³), primarily basaltic (sima: rich in silica and magnesium), and geologically younger"
        distractor = "thicker (30 to 70 km), less dense (~2,7 g/cm³), primarily granitic (sial: rich in silica and aluminium), and geologically older"
    prompt = (
        "Earth's crust is divided into two distinct geological varieties: continental crust and oceanic crust.\n\n"
        f"What physical and compositional properties define **{crust_type}**?"
    )
    correct = f"It is {desc}."
    options = [
        correct,
        f"It is {distractor}.",
        "It is composed entirely of liquid metallic mercury floating on seawater.",
        "It is made of soft organic peat moss that dissolves in rain."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Properties of {crust_type}:\n"
        "Continental crust: 30–70 km, ~2,7 g/cm³, granitic (sial), ancient.\n"
        "Oceanic crust: 5–10 km, ~3,0 g/cm³, basaltic (sima), young (recycled at subduction zones).\n"
        f"Step 2: Conclusion:\n"
        f"{crust_type.capitalize()} is {desc}."
    )
    return {
        "id": f"ns9_lith_02_{rng.randint(100000, 999999)}",
        "subskill": "02_continental_crust_vs_oceanic_crust_contrast",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Is {crust_type} thick/granitic or thin/basaltic?",
            "tier_2": f"It is {desc[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["continental_vs_oceanic_crust_contrast"]
    }


def arch_03_lithosphere_vs_asthenosphere_rigidity_ductility(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In plate tectonics, geologists distinguish between the mechanical layers known as the **lithosphere** and the **asthenosphere**.\n\n"
        "What is the mechanical difference in rigidity and behavior between these two upper Earth layers?"
    )
    correct = "The lithosphere is a brittle, rigid solid shell (crust plus uppermost mantle) broken into tectonic plates, while the asthenosphere below is a ductile, semi-fluid plastic layer of the upper mantle that can slowly flow."
    options = [
        correct,
        "The lithosphere is completely liquid molten iron, while the asthenosphere is frozen solid nitrogen.",
        "The lithosphere is a high-altitude gas layer, while the asthenosphere is the Earth's solid inner core.",
        "Both layers are completely identical in rigidity and melt into water at room temperature."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Mechanical definitions:\n"
        "• Lithosphere (Greek 'lithos' = stone): rigid, brittle outer shell (0–100/150 km) comprising the crust and uppermost mantle.\n"
        "• Asthenosphere (Greek 'asthenes' = weak): semi-plastic, ductile upper mantle (100–350 km) where high temperature and pressure allow slow solid-state plastic creep/convection.\n"
        "Step 2: Tectonic significance:\n"
        "Rigid lithospheric plates float and slide atop the weaker, flowing asthenosphere."
    )
    return {
        "id": f"ns9_lith_03_{rng.randint(100000, 999999)}",
        "subskill": "03_lithosphere_vs_asthenosphere_rigidity_ductility",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Which layer is rigid/brittle and which is ductile/plastic?",
            "tier_2": "Lithosphere = rigid brittle plates; Asthenosphere = ductile plastic flowing mantle.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["lithosphere_vs_asthenosphere_rheology"]
    }


def arch_04_liquid_outer_core_geodynamo_magnetic_field(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Earth possesses a protective planetary magnetic field (the geomagnetic field) that deflects hazardous solar wind particles.\n\n"
        "Which internal layer of the Earth acts as a **geodynamo** to generate this magnetic field, and what mechanism produces it?"
    )
    correct = "The liquid outer core, through convective churning of electrically conductive molten iron and nickel driven by planetary rotation (Coriolis effect)."
    options = [
        correct,
        "The solid inner core, through radioactive decay of uranium in granite rocks.",
        "The crust, through the movement of iron railway tracks across continents.",
        "The atmosphere, through lightning strikes circulating between ocean clouds."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Planetary dynamo mechanism:\n"
        "A planetary magnetic field requires a convecting, electrically conductive fluid combined with rotation.\n"
        "Step 2: Responsible layer:\n"
        "The liquid outer core (~2900–5150 km depth) consists of molten Fe-Ni. Convection currents of liquid metal, organized into helical columns by Earth's rotation, generate the global dipolar magnetic field."
    )
    return {
        "id": f"ns9_lith_04_{rng.randint(100000, 999999)}",
        "subskill": "04_liquid_outer_core_geodynamo_magnetic_field",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Which layer has churning liquid molten iron?",
            "tier_2": "The liquid outer core acts as the planetary geodynamo.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["geodynamo_liquid_outer_core"]
    }


def arch_05_solid_inner_core_extreme_pressure_freezing(rng: random.Random) -> Dict[str, Any]:
    temp = rng.choice([5500, 5700, 6000])
    prompt = (
        f"At Earth's center, temperatures in the inner core reach an astounding **{temp} °C**, which is hotter than the surface of the Sun.\n\n"
        "Why does the inner core remain a dense, **solid sphere** of iron and nickel instead of melting into liquid?"
    )
    correct = "The immense lithostatic confining pressure exerted by the weight of the entire overlying planet forces iron and nickel atoms into a tightly packed solid crystalline lattice, raising the melting point well above the ambient temperature."
    options = [
        correct,
        "The inner core is cooled by an underground network of frozen ice oceans.",
        "The inner core is made of asbestos rock that cannot melt under any temperature.",
        "Chemical anti-freeze in the core prevents iron from ever turning into liquid."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Temperature vs Pressure:\n"
        f"While temperature is ~{temp} °C, pressure reaches ~330 to 360 GPa (over 3,3 million atmospheres).\n"
        "Step 2: Pressure freezing:\n"
        "Extreme confining pressure overcomes thermal agitation, preventing atoms from breaking out into a disordered liquid state. The melting temperature of iron at this pressure exceeds 6200 °C, keeping the inner core solid."
    )
    return {
        "id": f"ns9_lith_05_{rng.randint(100000, 999999)}",
        "subskill": "05_solid_inner_core_extreme_pressure_freezing",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What force counteracts the intense heat at the center of Earth?",
            "tier_2": "Immense lithostatic confining pressure forces atoms into a solid lattice.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["solid_inner_core_confining_pressure"]
    }


def arch_06_rock_cycle_fundamental_dynamic_equilibrium(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The **rock cycle** illustrates the continuous recycling and transformation of Earth materials over geological time.\n\n"
        "What two primary energy engines power the dynamic transformations of the rock cycle?"
    )
    correct = "Earth's internal geothermal heat engine (driving plate tectonics, volcanism, and metamorphism) and the external solar energy engine (driving weather, the water cycle, and surface erosion)."
    options = [
        correct,
        "Moonlight and artificial electricity from human power plants.",
        "Nuclear explosions in outer space and ocean tides alone.",
        "Static electricity from sandstorms and magnetic friction in the atmosphere."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Energy sources powering Earth:\n"
        "1. Internal heat engine: Primordial accretion heat + radioactive decay (U, Th, K) drive mantle convection, melting (igneous), and crustal deformation (metamorphism).\n"
        "2. External solar engine: Solar radiation drives atmospheric and hydrological circulation, causing weathering, erosion, and sedimentation.\n"
        "Step 2: Interaction:\n"
        "The rock cycle represents continuous matter transfer between these internal and external cycles."
    )
    return {
        "id": f"ns9_lith_06_{rng.randint(100000, 999999)}",
        "subskill": "06_rock_cycle_fundamental_dynamic_equilibrium",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What heat from inside and energy from outside power the rock cycle?",
            "tier_2": "Earth's internal geothermal heat and external solar energy.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["rock_cycle_energy_engines"]
    }


def arch_07_magma_vs_lava_location_and_volatile_gases(rng: random.Random) -> Dict[str, Any]:
    term = rng.choice(["magma", "lava"])
    if term == "magma":
        desc = "molten rock located beneath Earth's surface containing dissolved volatile gases (such as water vapor, CO2, and sulfur compounds) under high confining pressure"
        distractor = "molten rock that has breached the Earth's surface, where dissolved gases rapidly depressurize and escape into the atmosphere"
    else:
        desc = "molten rock that has breached the Earth's surface, where dissolved gases rapidly depressurize and escape into the atmosphere"
        distractor = "molten rock located beneath Earth's surface containing dissolved volatile gases (such as water vapor, CO2, and sulfur compounds) under high confining pressure"
    prompt = (
        "Geologists make a strict distinction between the terms 'magma' and 'lava'.\n\n"
        f"What is the precise definition and gas content of **{term}**?"
    )
    correct = f"It refers to {desc}."
    options = [
        correct,
        f"It refers to {distractor}.",
        "It refers to cold, frozen mineral brine found in polar glaciers.",
        "It refers to dried powdered limestone blowing across sand dunes."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Magma vs Lava:\n"
        "• Magma: Subsurface molten rock containing dissolved volatiles held in solution by confining pressure.\n"
        "• Lava: Extruded molten rock on the surface; rapid depressurization allows volatiles to boil off as volcanic gas emissions.\n"
        f"Step 2: Conclusion for {term}:\n"
        f"{term.capitalize()} is {desc}."
    )
    return {
        "id": f"ns9_lith_07_{rng.randint(100000, 999999)}",
        "subskill": "07_magma_vs_lava_location_and_volatile_gases",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Is {term} beneath the surface or erupted onto the surface?",
            "tier_2": f"It is {desc[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["magma_vs_lava_location_gas"]
    }


def arch_08_igneous_rock_definition_cooling_solidification(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The term **igneous** originates from the Latin word 'ignis', meaning fire.\n\n"
        "How do igneous rocks form, and why are they considered the primary 'parent' rocks of the Earth's crust?"
    )
    correct = "They form from the cooling, crystallization, and solidification of molten silicate rock (magma or lava); they are primary because all original crust was formed directly from cooled magma."
    options = [
        correct,
        "They form from the accumulation of compressed dead seashells on ocean floors.",
        "They form from the high-pressure baking of pre-existing shale without melting.",
        "They form from the condensation of atmospheric nitrogen into solid crystals."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Igneous rock definition:\n"
        "Formed by the crystallization and solidification of molten silicate liquid.\n"
        "Step 2: Primary crustal rocks:\n"
        "Earth's original crust solidified directly from a magma ocean ~4,5 billion years ago. All sedimentary and metamorphic rocks ultimately originate from the weathering or alteration of primary igneous rocks."
    )
    return {
        "id": f"ns9_lith_08_{rng.randint(100000, 999999)}",
        "subskill": "08_igneous_rock_definition_cooling_solidification",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What liquid solidifies to create igneous rocks?",
            "tier_2": "Crystallization and solidification of molten silicate rock (magma/lava).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["igneous_rock_definition_primary"]
    }


def arch_09_intrusive_plutonic_igneous_slow_cooling_granite(rng: random.Random) -> Dict[str, Any]:
    rock_ex = rng.choice(["granite", "gabbro", "diorite"])
    prompt = (
        f"**Intrusive (plutonic) igneous rocks**, such as {rock_ex}, solidify deep beneath Earth's surface.\n\n"
        "How does the subterranean cooling rate influence the texture and crystal size of intrusive igneous rocks?"
    )
    correct = "Surrounding country rock acts as a thermal insulator causing the magma to cool very slowly over thousands to millions of years, allowing ions ample time to migrate and grow large, visible interlocking mineral crystals (coarse-grained texture)."
    options = [
        correct,
        "Subterranean ice freezes the magma instantly, preventing any crystals from forming and producing smooth black glass.",
        "High underground winds crush all crystals into fine dust before the rock solidifies.",
        "The magma boils away into steam, leaving behind hollow porous rock that floats."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Intrusive thermal conditions:\n"
        "Magma emplaced deep within the crust is insulated by kilometers of rock.\n"
        "Step 2: Crystal growth kinetics:\n"
        "Slow cooling rate allows chemical elements sufficient time to diffuse through the melt and attach to nucleating crystal lattices. Result: Phaneritic (coarse-grained, >1 mm) interlocking texture (e.g. granite with visible quartz, feldspar, mica)."
    )
    return {
        "id": f"ns9_lith_09_{rng.randint(100000, 999999)}",
        "subskill": "09_intrusive_plutonic_igneous_slow_cooling_granite",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does deep magma cool slowly or quickly, and what does this do to crystal size?",
            "tier_2": "Slow cooling underground produces large, visible interlocking crystals.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["intrusive_igneous_slow_cooling_crystals"]
    }


def arch_10_extrusive_volcanic_igneous_fast_cooling_basalt(rng: random.Random) -> Dict[str, Any]:
    rock_ex = rng.choice(["basalt", "rhyolite", "andesite"])
    prompt = (
        f"**Extrusive (volcanic) igneous rocks**, such as {rock_ex}, solidify on or very near Earth's surface.\n\n"
        "How does surface exposure affect cooling rate, and what distinctive crystal texture results?"
    )
    correct = "Direct exposure to cool air or water causes the lava to cool rapidly within days or weeks, allowing very little time for crystal growth and producing fine-grained (aphanitic) crystals that cannot be distinguished without a magnifying lens."
    options = [
        correct,
        "Surface exposure causes crystals to expand into giant gemstones over billions of years.",
        "The rock dissolves completely into liquid mud whenever touched by rain.",
        "Surface heat causes the rock to boil and turn permanently into atmospheric cloud vapor."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Extrusive thermal regime:\n"
        "Lava erupts onto land (subaerial) or ocean floors (submarine).\n"
        "Step 2: Rapid solidification:\n"
        "Steep temperature gradient causes rapid heat loss. Rapid cooling quenches the melt quickly; many small nuclei form but have no time to grow into large crystals. Result: Aphanitic (fine-grained, <1 mm) texture (e.g. dark, dense basalt)."
    )
    return {
        "id": f"ns9_lith_10_{rng.randint(100000, 999999)}",
        "subskill": "10_extrusive_volcanic_igneous_fast_cooling_basalt",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What happens to crystal size when lava cools rapidly on the surface?",
            "tier_2": "Rapid cooling produces microscopic, fine-grained (aphanitic) crystals.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["extrusive_igneous_rapid_cooling_aphanitic"]
    }


def arch_11_pumice_vesicular_texture_and_buoyancy_physics(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "**Pumice** is a pale, lightweight volcanic rock with the unique physical property of being able to float on water.\n\n"
        "What volcanic eruption mechanism produces pumice's spongy, vesicular texture, and why does it float?"
    )
    correct = "Violent explosive degassing traps millions of expanding gas bubbles as frothy, silica-rich lava cools instantaneously, creating sealed vesicular cavities that reduce the rock's overall bulk density to less than that of water (density < 1,0 g/cm³)."
    options = [
        correct,
        "Pumice is made of hollow animal shells that were baked in volcanic lava.",
        "Pumice contains magnetic helium gas that lifts the rock into the sky.",
        "Pumice floats because it is chemically identical to frozen liquid nitrogen."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Formation of pumice:\n"
        "Viscous, gas-rich rhyolitic/dacitic magma erupts explosively. Rapid depressurization causes dissolved volatiles to froth out into bubbles (vesicles).\n"
        "Step 2: Buoyancy physics:\n"
        "The frothy lava quenches immediately into glass foam. Because a large fraction of the volume consists of air-filled vesicles, bulk density drops below 1,0 g/cm³ (water density = 1,0 g/cm³), satisfying Archimedes' principle for flotation."
    )
    return {
        "id": f"ns9_lith_11_{rng.randint(100000, 999999)}",
        "subskill": "11_pumice_vesicular_texture_and_buoyancy_physics",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What is trapped in pumice during explosive eruptions?",
            "tier_2": "Trapped gas bubbles create a vesicular sponge-like texture with density < 1,0 g/cm³.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["pumice_vesicular_texture_buoyancy"]
    }


def arch_12_obsidian_volcanic_glass_instant_quench_conchoidal(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "**Obsidian** is a dark, lustrous volcanic glass traditionally knapped by ancient peoples into razor-sharp surgical blades and arrowheads.\n\n"
        "Why does obsidian lack an orderly crystalline structure, and what distinctive fracture pattern does it display when struck?"
    )
    correct = "The highly viscous silica lava quenched (cooled) so instantaneously that ions had zero time to arrange into a crystal lattice, creating an amorphous glass that breaks along smooth, curved conchoidal fracture surfaces."
    options = [
        correct,
        "Obsidian was melted by prehistoric laser beams into diamond sheets.",
        "Obsidian is a metamorphic rock that splits into flat paper-thin cleavage sheets.",
        "Obsidian is an organic plant resin that crystallized inside fossil amber."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Quenching kinetics:\n"
        "When high-silica felsic lava cools almost instantly upon contact with air or water, viscosity prevents ion mobility. Freezing occurs before crystalline nucleation can start, yielding an amorphous glass.\n"
        "Step 2: Conchoidal fracture:\n"
        "Because glass lacks atomic cleavage planes, applied force propagates spherically, producing smooth, concave, shell-like (conchoidal) fracture edges sharper than steel."
    )
    return {
        "id": f"ns9_lith_12_{rng.randint(100000, 999999)}",
        "subskill": "12_obsidian_volcanic_glass_instant_quench_conchoidal",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Why is obsidian a glass rather than a crystalline rock?",
            "tier_2": "Instant quenching prevents crystal lattice formation, producing conchoidal fracture.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["obsidian_amorphous_glass_conchoidal"]
    }


def arch_13_sedimentary_rock_formation_five_stage_sequence(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The formation of clastic sedimentary rocks occurs across five sequential geological stages.\n\n"
        "Which list places the **five stages of sedimentary rock formation** in the correct chronological order?"
    )
    correct = "Weathering → Erosion → Transportation → Deposition (sedimentation) → Lithification (compaction and cementation)"
    options = [
        correct,
        "Lithification → Deposition → Transportation → Weathering → Erosion",
        "Deposition → Weathering → Lithification → Melting → Volcanism",
        "Compaction → Crystallization → Evaporation → Subduction → Quenching"
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Five stages of sedimentary rock formation:\n"
        "1. Weathering: In situ breakdown of exposed parent rock.\n"
        "2. Erosion: Detachment of loose weathered particles.\n"
        "3. Transportation: Movement by water, wind, or ice.\n"
        "4. Deposition: Settling out of suspension when energy drops.\n"
        "5. Lithification: Compaction under overburden and cementation by mineral precipitation."
    )
    return {
        "id": f"ns9_lith_13_{rng.randint(100000, 999999)}",
        "subskill": "13_sedimentary_rock_formation_five_stage_sequence",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does weathering happen before or after deposition?",
            "tier_2": "Weathering → Erosion → Transportation → Deposition → Lithification.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sedimentary_five_stage_sequence"]
    }


def arch_14_weathering_mechanical_vs_chemical_breakdown(rng: random.Random) -> Dict[str, Any]:
    w_type = rng.choice(["mechanical (physical) weathering", "chemical weathering"])
    if "mechanical" in w_type:
        desc = "the physical disintegration of rocks into smaller angular fragments without altering the chemical composition of their constituent minerals (e.g. frost wedging, thermal shattering)"
        distractor = "the decomposition and chemical alteration of primary minerals through reaction with water, oxygen, and atmospheric acids to form new minerals (e.g. rust oxidation, feldspar hydrolysis into clay)"
    else:
        desc = "the decomposition and chemical alteration of primary minerals through reaction with water, oxygen, and atmospheric acids to form new minerals (e.g. rust oxidation, feldspar hydrolysis into clay)"
        distractor = "the physical disintegration of rocks into smaller angular fragments without altering the chemical composition of their constituent minerals (e.g. frost wedging, thermal shattering)"
    prompt = (
        "Weathering breaks down exposed rock at or near Earth's surface into sediments.\n\n"
        f"What fundamental process defines **{w_type}**?"
    )
    correct = f"It refers to {desc}."
    options = [
        correct,
        f"It refers to {distractor}.",
        "It refers to the complete melting of rock into liquid basalt in the mantle.",
        "It refers to the radioactive synthesis of new chemical elements inside rocks."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Weathering classification:\n"
        "• Mechanical: Physical disintegration; changes grain size, mineral chemistry remains identical.\n"
        "• Chemical: Chemical decomposition; alters crystal lattices and produces new alteration minerals (clays, oxides).\n"
        f"Step 2: Analysis for {w_type}:\n"
        f"{w_type.capitalize()} is {desc}."
    )
    return {
        "id": f"ns9_lith_14_{rng.randint(100000, 999999)}",
        "subskill": "14_weathering_mechanical_vs_chemical_breakdown",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"Does {w_type} change the chemical composition of minerals?",
            "tier_2": f"It is {desc[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mechanical_vs_chemical_weathering"]
    }


def arch_15_erosion_and_transportation_agents_wind_water_ice(rng: random.Random) -> Dict[str, Any]:
    agent = rng.choice([
        ("Liquid running water (rivers and streams)", "most effective worldwide erosional agent, rounding sediment into smooth pebbles and sorting grains by mass and velocity"),
        ("Moving glacial ice", "scratches bedrock (striations) and transports giant boulders (erratics) without sorting, depositing unsorted till"),
        ("Wind (aeolian transport)", "lifts fine silt and dust over vast distances, sorting grains into uniform desert sand dunes and loess deposits")
    ])
    agent_name, effect = agent
    prompt = (
        "Erosion involves the mobilization and transportation of weathered sediments by natural moving agents.\n\n"
        f"What sedimentary characteristics and transport dynamics characterize **{agent_name}**?"
    )
    correct = f"It is the {effect}."
    options = [
        correct,
        "It melts all rock particles into boiling magma within two seconds.",
        "It causes rocks to float into outer space due to anti-gravity waves.",
        "It turns sand grains into radioactive uranium fuel rods."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Transportation agents in geology:\n"
        "Water, ice, wind, and gravity transport sediment.\n"
        f"Step 2: Specific characteristics of {agent_name}:\n"
        f"It is the {effect}."
    )
    return {
        "id": f"ns9_lith_15_{rng.randint(100000, 999999)}",
        "subskill": "15_erosion_and_transportation_agents_wind_water_ice",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"How does {agent_name} transport and deposit sediment?",
            "tier_2": f"It is the {effect[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["erosion_transport_agents_dynamics"]
    }


def arch_16_sedimentation_and_horizontal_stratification_beds(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In calm aquatic environments such as lakes, river floodplains, and sea floors, transported sediments settle under gravity.\n\n"
        "What geological structure is created by this settling process, and why are sedimentary rocks arranged in horizontal layers?"
    )
    correct = "Sediments settle out in flat, parallel horizontal sheets called strata (or beds) separated by bedding planes, because gravitational settling in calm water deposits each layer horizontally across depositional basins."
    options = [
        correct,
        "Sediments twist into vertical helical spirals because Earth rotates backward under the ocean.",
        "Sediments always solidify into hollow spheres that bounce across the sea floor.",
        "Sediments form randomly tangled balls of yarn with zero horizontal organization."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Principle of Original Horizontality (Steno):\n"
        "Particles settling out of a fluid suspension drop under gravity onto the basin floor.\n"
        "Step 2: Stratification:\n"
        "This forms continuous, flat-lying horizontal beds (strata). Differences in grain size, color, or mineralogy between successive depositional pulses produce visible bedding planes."
    )
    return {
        "id": f"ns9_lith_16_{rng.randint(100000, 999999)}",
        "subskill": "16_sedimentation_and_horizontal_stratification_beds",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What do we call the flat horizontal layers in sedimentary rocks?",
            "tier_2": "Strata (or beds) formed by gravitational settling in calm water.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sedimentary_stratification_horizontal_beds"]
    }


def arch_17_compaction_and_cementation_lithification_chemistry(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Loose sediment grains are turned into solid rock through the process of **lithification**.\n\n"
        "What two complementary physical and chemical processes drive lithification?"
    )
    correct = "Compaction (weight of overlying sediments squeezes pore spaces and expels water) and Cementation (percolating groundwater precipitates dissolved minerals like calcite or silica that glue grains together)."
    options = [
        correct,
        "Boiling (magma vaporizes all water) and Freezing (polar glaciers turn sand into ice).",
        "Photosynthesis (algae synthesize plant roots) and Combustion (lightning ignites coal).",
        "Nuclear fusion (hydrogen atoms fuse into helium inside loose pebbles)."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Lithification = Compaction + Cementation.\n"
        "Step 2: Compaction:\n"
        "As burial depth increases, overburden pressure squeezes loose sediment, reducing porosity from ~50% down to ~10%.\n"
        "Step 3: Cementation:\n"
        "Groundwater carrying dissolved ions (Ca²⁺, HCO3⁻, SiO4⁴⁻) percolates through remaining pores. Changes in pH or temperature trigger mineral precipitation (calcite CaCO3, silica SiO2, iron oxide Fe2O3), cementing loose grains into cohesive rock."
    )
    return {
        "id": f"ns9_lith_17_{rng.randint(100000, 999999)}",
        "subskill": "17_compaction_and_cementation_lithification_chemistry",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What squeezes loose sediment and what glues the grains together?",
            "tier_2": "Compaction squeezes out water; cementation glues grains with precipitated minerals.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["lithification_compaction_cementation"]
    }


def arch_18_clastic_sedimentary_rocks_sandstone_shale_conglomerate(rng: random.Random) -> Dict[str, Any]:
    rock_type, grain, name = rng.choice([
        ("shale / mudstone", "microscopic clay and silt particles (< 0,063 mm) deposited in very quiet, calm water", "Shale"),
        ("sandstone", "medium-sized sand grains (0,063 to 2 mm) deposited by river currents, beach waves, or desert dunes", "Sandstone"),
        ("conglomerate", "large, rounded gravel pebbles and cobbles (> 2 mm) cemented in a sandy matrix, deposited by energetic mountain torrents", "Conglomerate")
    ])
    prompt = (
        "Clastic sedimentary rocks are classified primarily according to the grain size of their sediment particles.\n\n"
        f"Which clastic sedimentary rock is formed from **{grain}**?"
    )
    correct = f"{name}."
    distractors = [
        "Obsidian.",
        "Marble.",
        "Basalt."
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        "Step 1: Clastic grain size hierarchy (Wentworth scale):\n"
        "• Clay/silt (<0,063 mm) → Shale/mudstone.\n"
        "• Sand (0,063–2 mm) → Sandstone.\n"
        "• Rounded gravel/pebbles (>2 mm) → Conglomerate.\n"
        f"Step 2: Conclusion:\n"
        f"Sediment composed of {grain} forms {name}."
    )
    return {
        "id": f"ns9_lith_18_{rng.randint(100000, 999999)}",
        "subskill": "18_clastic_sedimentary_rocks_sandstone_shale_conglomerate",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"What rock forms from {grain[:25]}...?",
            "tier_2": f"It forms {name}.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["clastic_sedimentary_grain_size"]
    }


def arch_19_chemical_and_organic_sedimentary_rocks_limestone_coal(rng: random.Random) -> Dict[str, Any]:
    rock_choice = rng.choice([
        ("biochemical / organic limestone", "accumulation of calcium carbonate (CaCO3) shells and skeletal debris from marine organisms (corals, molluscs, foraminifera)"),
        ("coal", "accumulation, compaction, and carbonization of ancient plant remains in anoxic swamp environments over millions of years"),
        ("rock salt (halite)", "chemical precipitation of dissolved mineral salts when mineral-rich lakes or shallow seas completely evaporate (evaporites)")
    ])
    rock_name, origin = rock_choice
    prompt = (
        "Non-clastic sedimentary rocks form either through chemical precipitation or organic accumulation.\n\n"
        f"What geological conditions and materials create **{rock_name}**?"
    )
    correct = f"It forms through the {origin}."
    options = [
        correct,
        "It forms from explosive volcanic ash quenched under glacial ice sheets.",
        "It forms when granite is crushed inside high-pressure laboratory vices.",
        "It forms when meteorites vaporize surface quartz sand into molten glass."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Origin of {rock_name}:\n"
        f"Non-clastic sedimentary rock classification.\n"
        f"Step 2: Formation mechanism:\n"
        f"It forms through the {origin}."
    )
    return {
        "id": f"ns9_lith_19_{rng.randint(100000, 999999)}",
        "subskill": "19_chemical_and_organic_sedimentary_rocks_limestone_coal",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": f"How does {rock_name} form?",
            "tier_2": f"It forms through the {origin[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["chemical_organic_sedimentary_rocks"]
    }


def arch_20_fossil_preservation_exclusive_to_sedimentary_strata(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Fossils (the preserved remains or traces of ancient organisms) are found almost exclusively in **sedimentary rocks**.\n\n"
        "Why are fossils virtually never preserved in igneous or metamorphic rocks?"
    )
    correct = "The scorching temperatures of molten magma/lava in igneous environments incinerate organic remains completely, while the extreme heat and differential pressure of metamorphism crush, distort, and recrystallize rock minerals, destroying any fossil impressions."
    options = [
        correct,
        "Animals in ancient times were chemically immune to sedimentary rocks.",
        "Igneous and metamorphic rocks are formed in outer space where no animals ever lived.",
        "Sedimentary rocks contain special artificial embalming chemicals that freeze bones."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Fossil preservation requirements:\n"
        "Requires gentle, low-temperature burial in fine sediments (mud/silt) to exclude oxygen and scavengers.\n"
        "Step 2: Why igneous and metamorphic rocks fail:\n"
        "• Igneous: Magma temperatures (700–1200 °C) vaporize organic tissue and melt bone phosphate.\n"
        "• Metamorphic: Intense directed stress, shearing, and temperatures (>200 °C) obliterate fossil structures through ductile deformation and mineral recrystallization."
    )
    return {
        "id": f"ns9_lith_20_{rng.randint(100000, 999999)}",
        "subskill": "20_fossil_preservation_exclusive_to_sedimentary_strata",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What happens to a fossil if it touches molten lava or high metamorphic heat/pressure?",
            "tier_2": "Magma incinerates remains; metamorphic pressure crushes and recrystallizes them.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["fossil_preservation_sedimentary_exclusivity"]
    }


def arch_21_metamorphic_rock_heat_and_pressure_recrystallization(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The word **metamorphism** means 'change of form'.\n\n"
        "What fundamental condition distinguishes metamorphic rock transformation from igneous rock formation?"
    )
    correct = "Metamorphic recrystallization occurs entirely in the solid state under elevated temperatures (200 °C to 800 °C) and directed pressures without the rock ever melting into magma."
    options = [
        correct,
        "Metamorphic transformation requires the rock to completely boil into steam in open air.",
        "Metamorphic rocks are formed when ocean water freezes solid into ice blocks.",
        "Metamorphism occurs only when human construction crews hammer rocks into powder."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Solid-state recrystallization:\n"
        "Metamorphism is defined as solid-state alteration. If a rock melts completely into liquid melt, it crosses into the igneous realm upon re-cooling.\n"
        "Step 2: Thermodynamic drivers:\n"
        "Elevated heat breaks weak bonds, allowing atoms to reorganize into more stable, denser crystal lattices under confining pressure and directional tectonic stress."
    )
    return {
        "id": f"ns9_lith_21_{rng.randint(100000, 999999)}",
        "subskill": "21_metamorphic_rock_heat_and_pressure_recrystallization",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does a rock melt when it undergoes metamorphism?",
            "tier_2": "No, it recrystallizes entirely in the solid state without melting.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["metamorphic_solid_state_recrystallization"]
    }


def arch_22_metamorphic_protolith_shale_to_slate_foliation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When sedimentary **shale** (composed of microscopic clay particles) is subjected to low-grade regional metamorphic heat and pressure, it transforms into **slate**.\n\n"
        "What physical property and texture develop during this transformation, making slate ideal for roofing tiles and blackboards?"
    )
    correct = "Planar slaty cleavage: microscopic clay minerals recrystallize into tiny mica flakes that align perpendicular to directional pressure, allowing the rock to split easily along flat, smooth, durable sheets."
    options = [
        correct,
        "Porous sponge holes that absorb rainwater and cause the rock to float.",
        "Vigorous chemical fizzing when touched by pure water.",
        "A soft rubbery texture that allows the rock to bend like plastic."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Protolith transformation: Shale → Slate.\n"
        "Low-grade regional metamorphism (~200–300 °C).\n"
        "Step 2: Slaty cleavage:\n"
        "Differential tectonic stress forces platy clay and microscopic mica crystals to rotate and recrystallize with their flat basal planes perpendicular to the maximum compressive stress direction. This produces excellent planar cleavage."
    )
    return {
        "id": f"ns9_lith_22_{rng.randint(100000, 999999)}",
        "subskill": "22_metamorphic_protolith_shale_to_slate_foliation",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What allows slate to split into flat sheets for roofing?",
            "tier_2": "Planar slaty cleavage formed by aligned microscopic mica flakes.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["shale_to_slate_slaty_cleavage"]
    }


def arch_23_metamorphic_protolith_limestone_to_marble_recrystallization(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Under metamorphic conditions, sedimentary **limestone** is transformed into the prized metamorphic rock **marble**.\n\n"
        "What structural change occurs during this transformation, and what diagnostic chemical test still identifies marble?"
    )
    correct = "Tiny calcite grains and fossil shells recrystallize into large, interlocking coarse calcite crystals forming a non-foliated sugary texture; it still effervesces (fizzes) vigorously when tested with dilute hydrochloric acid."
    options = [
        correct,
        "The calcite transforms into pure diamond, and it no longer reacts with any chemical acid.",
        "The rock melts into black obsidian glass that dissolves completely in river water.",
        "The rock becomes radioactive and emits glowing green gamma rays."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Protolith transformation: Limestone (or Dolostone) → Marble.\n"
        "Step 2: Microstructural recrystallization:\n"
        "Heat and uniform pressure drive solid-state recrystallization. Individual tiny calcite (CaCO3) grains fuse and grow into a tightly interlocking mosaic of coarse calcite crystals.\n"
        "Step 3: Chemical diagnostic:\n"
        "Because mineralogy remains CaCO3, marble effervesces vigorously (releases CO2) when touched by dilute HCl."
    )
    return {
        "id": f"ns9_lith_23_{rng.randint(100000, 999999)}",
        "subskill": "23_metamorphic_protolith_limestone_to_marble_recrystallization",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What happens to calcite grains when limestone turns into marble?",
            "tier_2": "They recrystallize into large interlocking crystals that still fizz with acid.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["limestone_to_marble_recrystallization"]
    }


def arch_24_metamorphic_protolith_sandstone_to_quartzite_hardness(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When quartz-rich sedimentary **sandstone** undergoes intense heat and pressure, it recrystallizes into **quartzite**.\n\n"
        "How can a field geologist definitively distinguish quartzite from ordinary sandstone using a rock hammer?"
    )
    correct = "When broken with a hammer, quartzite fractures right through the quartz grains because the grains are fused completely into an interlocking network, whereas sandstone fractures around the individual sand grains through the softer cement."
    options = [
        correct,
        "Sandstone scratches steel, whereas quartzite is as soft as butter.",
        "Quartzite dissolves in cold water, while sandstone does not.",
        "Sandstone bounces like a rubber ball, whereas quartzite explodes into steam."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Protolith transformation: Quartz Sandstone → Quartzite.\n"
        "Step 2: Recrystallization mechanism:\n"
        "Thermal metamorphism fuses quartz (SiO2) sand grains and silica cement into a single continuous crystalline network.\n"
        "Step 3: Fracture distinction:\n"
        "In sandstone, cracks travel through the weaker pore cement around grains. In tough quartzite, fractures cleanly slice straight through the fused quartz grains (Mohs hardness 7)."
    )
    return {
        "id": f"ns9_lith_24_{rng.randint(100000, 999999)}",
        "subskill": "24_metamorphic_protolith_sandstone_to_quartzite_hardness",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Does a fracture break around or through the quartz grains in quartzite?",
            "tier_2": "In quartzite, fractures slice right through the fused quartz grains.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sandstone_to_quartzite_fused_grains"]
    }


def arch_25_metamorphic_protolith_granite_to_gneiss_banding(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Under high-grade regional metamorphism involving intense differential compressive stress, igneous **granite** transforms into **gneiss**.\n\n"
        "What prominent visual texture characterizes gneiss, and how does metamorphic segregation produce it?"
    )
    correct = "Gneissic banding: extreme directional pressure and high temperatures cause minerals to segregate into alternating light-colored bands (rich in felsic quartz and feldspar) and dark-colored bands (rich in mafic biotite mica and amphibole)."
    options = [
        correct,
        "Vesicular sponge holes that allow water to flow freely through the rock.",
        "A glassy black mirror surface with zero visible crystals.",
        "Horizontal layers of fossil seashells compressed into pure chalk."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Protolith transformation: Granite (or Mudstone/Schist) → Gneiss.\n"
        "High-grade regional metamorphism (>600 °C, high differential stress).\n"
        "Step 2: Metamorphic segregation:\n"
        "Under directional shear and compressive stress, solid-state diffusion causes mineral segregation. Light felsic minerals (quartz, potassium feldspar) separate into light bands, while dark mafic minerals (biotite, hornblende) concentrate into alternating dark foliated bands."
    )
    return {
        "id": f"ns9_lith_25_{rng.randint(100000, 999999)}",
        "subskill": "25_metamorphic_protolith_granite_to_gneiss_banding",
        "question_type": "multiple_choice",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_answer": correct,
        "sample_answer": correct,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "What kind of alternating light and dark bands does gneiss show?",
            "tier_2": "Gneissic banding: alternating light (quartz/feldspar) and dark (mica/amphibole) bands.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["granite_to_gneiss_gneissic_banding"]
    }


BUILDERS_01_25 = {
    "01_earth_internal_structure_crust_mantle_core_dimensions": arch_01_earth_internal_structure_crust_mantle_core_dimensions,
    "02_continental_crust_vs_oceanic_crust_contrast": arch_02_continental_crust_vs_oceanic_crust_contrast,
    "03_lithosphere_vs_asthenosphere_rigidity_ductility": arch_03_lithosphere_vs_asthenosphere_rigidity_ductility,
    "04_liquid_outer_core_geodynamo_magnetic_field": arch_04_liquid_outer_core_geodynamo_magnetic_field,
    "05_solid_inner_core_extreme_pressure_freezing": arch_05_solid_inner_core_extreme_pressure_freezing,
    "06_rock_cycle_fundamental_dynamic_equilibrium": arch_06_rock_cycle_fundamental_dynamic_equilibrium,
    "07_magma_vs_lava_location_and_volatile_gases": arch_07_magma_vs_lava_location_and_volatile_gases,
    "08_igneous_rock_definition_cooling_solidification": arch_08_igneous_rock_definition_cooling_solidification,
    "09_intrusive_plutonic_igneous_slow_cooling_granite": arch_09_intrusive_plutonic_igneous_slow_cooling_granite,
    "10_extrusive_volcanic_igneous_fast_cooling_basalt": arch_10_extrusive_volcanic_igneous_fast_cooling_basalt,
    "11_pumice_vesicular_texture_and_buoyancy_physics": arch_11_pumice_vesicular_texture_and_buoyancy_physics,
    "12_obsidian_volcanic_glass_instant_quench_conchoidal": arch_12_obsidian_volcanic_glass_instant_quench_conchoidal,
    "13_sedimentary_rock_formation_five_stage_sequence": arch_13_sedimentary_rock_formation_five_stage_sequence,
    "14_weathering_mechanical_vs_chemical_breakdown": arch_14_weathering_mechanical_vs_chemical_breakdown,
    "15_erosion_and_transportation_agents_wind_water_ice": arch_15_erosion_and_transportation_agents_wind_water_ice,
    "16_sedimentation_and_horizontal_stratification_beds": arch_16_sedimentation_and_horizontal_stratification_beds,
    "17_compaction_and_cementation_lithification_chemistry": arch_17_compaction_and_cementation_lithification_chemistry,
    "18_clastic_sedimentary_rocks_sandstone_shale_conglomerate": arch_18_clastic_sedimentary_rocks_sandstone_shale_conglomerate,
    "19_chemical_and_organic_sedimentary_rocks_limestone_coal": arch_19_chemical_and_organic_sedimentary_rocks_limestone_coal,
    "20_fossil_preservation_exclusive_to_sedimentary_strata": arch_20_fossil_preservation_exclusive_to_sedimentary_strata,
    "21_metamorphic_rock_heat_and_pressure_recrystallization": arch_21_metamorphic_rock_heat_and_pressure_recrystallization,
    "22_metamorphic_protolith_shale_to_slate_foliation": arch_22_metamorphic_protolith_shale_to_slate_foliation,
    "23_metamorphic_protolith_limestone_to_marble_recrystallization": arch_23_metamorphic_protolith_limestone_to_marble_recrystallization,
    "24_metamorphic_protolith_sandstone_to_quartzite_hardness": arch_24_metamorphic_protolith_sandstone_to_quartzite_hardness,
    "25_metamorphic_protolith_granite_to_gneiss_banding": arch_25_metamorphic_protolith_granite_to_gneiss_banding,
}
