"""Grade 9 Natural Sciences - Mining of Mineral Resources: Archetypes 26 to 50.
Grounded in CAPS: curriculum_docs_auto/NaturalSciences_Gr9/Term 4/03. Mining of mineral resources.md
Focus:
Indigenous metallurgy (Phalaborwa copper, Iron Age bloomeries), Major South African deposits (Witwatersrand gold,
Bushveld PGMs, Sishen iron, Kalahari manganese, Highveld coal, Kimberley/Cullinan diamonds, Phalaborwa carbonatite,
Richards Bay heavy mineral sands), Environmental & health impacts (Acid Mine Drainage chemistry & toxicity, tailings dust,
dolomite sinkholes, silicosis & rockbursts), Mine rehabilitation & acid water neutralization, Socio-economic significance
(GDP, export freight rail & ports, green energy hydrogen transition, ore valuation formula, MPRDA licensing, Diagnostic Autopsy).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def arch_26_indigenous_copper_smelting_phalaborwa_clay_furnaces(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Archaeological excavations at **Phalaborwa** in Limpopo demonstrate that African smiths operated an advanced copper mining and smelting industry long before modern industrial mining.\n\n"
        "What pyrotechnological equipment and ore did indigenous Phalaborwa metallurgists use to produce copper?"
    )
    correct = "They mined green malachite copper ore, crushed it, and smelted it inside domed clay furnaces fueled by hardwood charcoal, using cattle-skin bellows connected to ceramic tuyeres to pump forced air and reduce the ore into molten copper ingots."
    options = [
        correct,
        "They used nuclear fission reactors buried beneath the sand dunes.",
        "They imported molten copper through transatlantic steamship pipelines from Europe.",
        "They soaked granite in ocean water until copper crystallized on the beach."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Phalaborwa indigenous copper metallurgy:\n"
        "Active from ~8th century AD onwards.\n"
        "Step 2: Smelting technology:\n"
        "Smiths built clay bowl furnaces. Charcoal fuel generated high temperatures and carbon monoxide reducing gas. Clay tuyere blowpipes channeled forced air from hand bellows, reducing malachite (Cu2CO3(OH)2) into pure copper."
    )
    return {
        "id": f"ns9_mine_26_{rng.randint(100000, 999999)}",
        "subskill": "26_indigenous_copper_smelting_phalaborwa_clay_furnaces",
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
            "tier_1": "What kind of clay furnaces and bellows were used at Phalaborwa?",
            "tier_2": "Clay furnaces, charcoal fuel, and hide bellows reducing malachite ore.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["indigenous_copper_smelting_phalaborwa"]
    }


def arch_27_traditional_iron_age_bloomery_smelting_tuyeres(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "During South Africa's **Early and Late Iron Age** (e.g. in KwaZulu-Natal and Mpumalanga), iron tools and spears were manufactured using **bloomery furnaces**.\n\n"
        "What physical product was produced in an Iron Age bloomery, and how did smiths turn it into usable steel and iron tools?"
    )
    correct = "The furnace did not reach iron's melting point (1538 °C), producing a spongy solid mass of metallic iron mixed with slag called a 'bloom'; smiths repeatedly reheated and hammered the bloom on stone anvils to squeeze out slag and consolidate the metal."
    options = [
        correct,
        "The furnace melted iron into water-like liquid that was poured into glass bottles.",
        "The furnace vaporized iron into green smoke that was inhaled by warriors.",
        "The furnace turned charcoal into solid diamond spearheads."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Bloomery direct reduction:\n"
        "Operating at 1100–1200 °C, below iron's melting point.\n"
        "Step 2: Bloom consolidation:\n"
        "CO gas reduces iron oxide to solid iron. Slag melts and pools. The resulting porous sponge iron ('bloom') contains entrapped silicate slag. Blacksmiths forge-weld the bloom, hammering out liquid slag to create tough wrought iron."
    )
    return {
        "id": f"ns9_mine_27_{rng.randint(100000, 999999)}",
        "subskill": "27_traditional_iron_age_bloomery_smelting_tuyeres",
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
            "tier_1": "Did bloomery furnaces melt iron or produce a solid spongy bloom?",
            "tier_2": "They produced a solid spongy bloom hammered on anvils to expel slag.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["iron_age_bloomery_solid_reduction"]
    }


def arch_28_witwatersrand_gold_paleoplacer_conglomerate_basin(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The **Witwatersrand Basin** in Gauteng and the Free State has produced approximately 40% to 50% of all gold ever mined in human history.\n\n"
        "What geological deposit type characterizes Witwatersrand gold, and in what rock formation is it found?"
    )
    correct = "An ancient Archean paleoplacer deposit (~2,8 billion years old), where native gold grains and heavy minerals accumulated in quartz pebble conglomerate beds (known as 'reefs') deposited by braided rivers into an inland lake basin."
    options = [
        correct,
        "A recent volcanic lava plateau that erupted molten gold onto grass fields fifty years ago.",
        "A coral reef formed by ocean sea animals that secrete metallic gold shells.",
        "A subterranean magma lake of liquid gold located in the Earth's mantle."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Witwatersrand geology:\n"
        "Formed ~2,9–2,7 Ga (Mesoarchean).\n"
        "Step 2: Paleoplacer model:\n"
        "Gold weathered from Archean granite-greenstone belts was transported by torrential braided river systems, concentrating in alluvial pebble conglomerate beds (e.g. Main Reef Leader, Ventersdorp Contact Reef)."
    )
    return {
        "id": f"ns9_mine_28_{rng.randint(100000, 999999)}",
        "subskill": "28_witwatersrand_gold_paleoplacer_conglomerate_basin",
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
            "tier_1": "What rock type hosts Witwatersrand gold?",
            "tier_2": "Ancient quartz pebble conglomerate paleoplacer reefs.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["witwatersrand_gold_conglomerate_paleoplacer"]
    }


def arch_29_bushveld_complex_merensky_ug2_platinum_chromite(rng: random.Random) -> Dict[str, Any]:
    reef = rng.choice(["Merensky Reef (rich in PGMs, base metal sulfides, and gold)", "UG2 Chromitite Reef (rich in chromite and high proportions of rhodium and platinum)"])
    prompt = (
        f"South Africa's **Bushveld Igneous Complex** hosts over 70% of global platinum reserves across stratiform layers like the **{reef}**.\n\n"
        "What geological phenomenon created these continuous, wafer-thin, ultra-rich mineral layers stretching across hundreds of kilometers?"
    )
    correct = "Repeated pulses of primitive magma entering a vast subterranean magma chamber, where fractional crystallization, cooling, and gravity settling concentrated dense platinum- and chromite-bearing crystals into distinct horizontal layers."
    options = [
        correct,
        "Ocean tsunamis that washed platinum dust from South America onto African beaches.",
        "Lightning bolts striking limestone caves and turning calcite into platinum.",
        "Underground trees that absorbed platinum from groundwater roots."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Bushveld Complex magmatic layering:\n"
        "Formed 2,06 billion years ago in Limpopo/Mpumalanga/North West.\n"
        "Step 2: Fractional crystallization:\n"
        "Magma cooling in an enormous lopolith underwent rhythmic crystallization. Dense chromite, sulfides, and PGMs settled out of the convective magma sheet, forming continuous, planar reef horizons."
    )
    return {
        "id": f"ns9_mine_29_{rng.randint(100000, 999999)}",
        "subskill": "29_bushveld_complex_merensky_ug2_platinum_chromite",
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
            "tier_1": "How did the Bushveld reefs form in a cooling magma chamber?",
            "tier_2": "Fractional crystallization and gravity settling in a layered intrusion.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["bushveld_complex_magmatic_reefs"]
    }


def arch_30_sishen_and_kolomela_hematite_iron_ore_corridor(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "South Africa's premier iron ore operations at **Sishen and Kolomela** in the Northern Cape produce some of the highest-grade iron ore in the world (>64% Fe).\n\n"
        "What geological rock sequence was naturally enriched to produce these massive supergene hematite deposits?"
    )
    correct = "Precambrian Banded Iron Formations (BIFs) where groundwater leaching dissolved away silica over millions of years, enriching the residual rock into dense, high-purity lump hematite (Fe2O3)."
    options = [
        correct,
        "Loose beach sand that was melted by forest fires into pure iron rods.",
        "Marine coral reefs where sea creatures deposited pure metallic iron shells.",
        "Modern river silt that was electroplated by lightning storms."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Protolith: Banded Iron Formation (Kuruman/Griquatown BIF).\n"
        "Alternating micro-layers of chert (silica) and iron oxides.\n"
        "Step 2: Supergene enrichment:\n"
        "Ancient weathering and deep meteoric groundwater circulation selectively dissolved and flushed out the silica, upgrading iron concentration from ~30% Fe up to >64% pure lump hematite."
    )
    return {
        "id": f"ns9_mine_30_{rng.randint(100000, 999999)}",
        "subskill": "30_sishen_and_kolomela_hematite_iron_ore_corridor",
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
            "tier_1": "What rock was enriched to form Sishen iron ore?",
            "tier_2": "Banded Iron Formations (BIF) enriched by groundwater leaching of silica.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["sishen_iron_ore_bif_supergene_enrichment"]
    }


def arch_31_kalahari_manganese_field_global_resource_significance(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The **Kalahari Manganese Field** in the Northern Cape (centered around Hotazel and Black Rock) holds over 70% of the world's known land-based manganese reserves.\n\n"
        "Why is **manganese** an irreplaceable strategic metal in global manufacturing?"
    )
    correct = "It is an essential, non-substitutable alloying element in steelmaking that acts as a deoxidizer and desulfurizer, improving the strength, toughness, and wear-resistance of all carbon steel."
    options = [
        correct,
        "It is used as a sweet food additive in place of cane sugar.",
        "It is the main fuel burned inside automobile combustion engines.",
        "It is woven into soft cotton fabrics to make lightweight summer clothing."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Global significance:\n"
        "Without manganese, steel cannot be manufactured economically.\n"
        "Step 2: Metallurgy of manganese:\n"
        "Adding manganese (as ferromanganese or silicomanganese) binds harmful sulfur (forming MnS instead of brittle FeS) and removes dissolved oxygen, imparting hardenability and impact toughness to steel."
    )
    return {
        "id": f"ns9_mine_31_{rng.randint(100000, 999999)}",
        "subskill": "31_kalahari_manganese_field_global_resource_significance",
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
            "tier_1": "Why is manganese essential in the production of steel?",
            "tier_2": "It acts as a deoxidizer and desulfurizer, imparting strength and toughness to steel.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["kalahari_manganese_steelmaking_role"]
    }


def arch_32_highveld_coalfields_emalahleni_thermal_power_generation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "South Africa's **Highveld and Witbank coalfields** around eMalahleni in Mpumalanga supply fuel for national electricity generation.\n\n"
        "What geological conditions in ancient South Africa created these thick bituminous coal seams?"
    )
    correct = "Vast Permian swamps in the Karoo Basin (~260 million years ago) where dead Glossopteris vegetation accumulated in cold, anoxic peat bogs, which were subsequently buried, compacted, and chemically carbonized under heat and pressure."
    options = [
        correct,
        "Recent forest fires along the coast that turned pine needles into liquid gasoline.",
        "Volcanic eruptions of black basalt lava that cooled into flammable coal rocks.",
        "Meteorite showers that deposited frozen carbon blocks across Mpumalanga."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Coal origin in the Karoo Supergroup:\n"
        "Ecca Group sediments (Vryheid Formation).\n"
        "Step 2: Coalification process:\n"
        "Anoxic water prevented bacterial decay of wetland plant matter. Stagnant peat accumulated, and deep burial under overlying Karoo strata squeezed out moisture and volatiles, upgrading peat through lignite to bituminous thermal coal."
    )
    return {
        "id": f"ns9_mine_32_{rng.randint(100000, 999999)}",
        "subskill": "32_highveld_coalfields_emalahleni_thermal_power_generation",
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
            "tier_1": "What plant matter accumulated to form Karoo coal seams?",
            "tier_2": "Permian swamp vegetation buried and carbonized in anoxic bogs.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["karoo_coal_formation_carbonization"]
    }


def arch_33_kimberley_big_hole_volcanic_pipe_diamond_rush(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The 1871 discovery of diamonds at Colesberg Kopje triggered the historic diamond rush that excavated the famous **Kimberley Big Hole**.\n\n"
        "What geological discovery was made at Kimberley that revolutionized worldwide diamond exploration?"
    )
    correct = "Geologists discovered that diamonds were not merely loose river gravel minerals, but were hosted in deep, carrot-shaped volcanic conduits of weathered igneous rock, named 'kimberlite pipes'."
    options = [
        correct,
        "Geologists discovered that diamonds were formed by lightning striking ostrich eggs.",
        "Geologists discovered that diamonds could be grown in wooden barrels using seawater.",
        "Geologists discovered that diamonds were living bacteria that reproduce in soil."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Historical context:\n"
        "Prior to 1870, diamonds were found only in secondary alluvial gravels (India, Brazil).\n"
        "Step 2: Primary pipe discovery:\n"
        "At Kimberley, digging beneath 'yellow ground' (weathered kimberlite) revealed 'blue ground' (unweathered kimberlite), establishing the primary volcanic pipe source for diamond exploration worldwide."
    )
    return {
        "id": f"ns9_mine_33_{rng.randint(100000, 999999)}",
        "subskill": "33_kimberley_big_hole_volcanic_pipe_diamond_rush",
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
            "tier_1": "What rock formation was discovered to be the primary source of diamonds?",
            "tier_2": "Volcanic conduits of igneous rock called kimberlite pipes.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["kimberley_big_hole_kimberlite_pipe"]
    }


def arch_34_cullinan_mine_gem_diamonds_premier_pipe(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In 1905, the **Cullinan Diamond**—the largest gem-quality rough diamond ever found (3 106 carats, ~621 g)—was discovered at the Premier Mine near Pretoria.\n\n"
        "What physical characteristics allow gem diamonds to be cut and polished to display intense brilliance and spectral 'fire'?"
    )
    correct = "Diamond possesses extreme hardness (Mohs 10), an exceptionally high refractive index (2,42) that traps light via total internal reflection, and high optical dispersion that splits white light into rainbow spectral flashes."
    options = [
        correct,
        "Diamond is made of soft rubber that absorbs water and bends light like a lens.",
        "Diamond is radioactive and glows with neon green light in the dark.",
        "Diamond is liquid at room temperature and freezes into glass under sunlight."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Optical physics of gem diamonds:\n"
        "Refractive index n = 2,42 (critical angle ~24,4°).\n"
        "Step 2: Brilliance and fire:\n"
        "High refractive index allows faceted brilliant cuts to achieve total internal reflection, bouncing light back out the crown. High dispersion (0,044) separates white light into spectral chromatic colors ('fire')."
    )
    return {
        "id": f"ns9_mine_34_{rng.randint(100000, 999999)}",
        "subskill": "34_cullinan_mine_gem_diamonds_premier_pipe",
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
            "tier_1": "What optical properties give diamonds their brilliance and rainbow fire?",
            "tier_2": "High refractive index (2,42) and high optical dispersion splitting light.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["diamond_optical_dispersion_brilliance"]
    }


def arch_35_phalaborwa_carbonatite_complex_copper_and_phosphate(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The **Phalaborwa Igneous Complex** is an extraordinary multi-commodity geological feature in Limpopo.\n\n"
        "What unique igneous rock body is mined at Phalaborwa, and what two vital industrial mineral commodities does it yield simultaneously?"
    )
    correct = "A carbonatite volcanic pipe (magmatic carbonate rock), mined simultaneously for copper sulfides and apatite (a rich phosphate mineral essential for agricultural fertilizer production)."
    options = [
        correct,
        "A granite batholith mined for table salt and petroleum.",
        "A basalt lava flow mined for drinking water and frozen ice.",
        "A sandstone cliff mined for plastic resin and automobile tires."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Phalaborwa carbonatite complex:\n"
        "A rare ~2,05 Ga alkaline-carbonatite ring complex.\n"
        "Step 2: Multi-commodity production:\n"
        "Primary products include copper (from bornite and chalcopyrite) and phosphate (from apatite Ca5(PO4)3(F,Cl,OH), feeding the South African fertilizer industry), plus byproduct baddeleyite (ZrO2) and vermiculite."
    )
    return {
        "id": f"ns9_mine_35_{rng.randint(100000, 999999)}",
        "subskill": "35_phalaborwa_carbonatite_complex_copper_and_phosphate",
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
            "tier_1": "What rare carbonate rock pipe at Phalaborwa yields copper and fertilizer phosphate?",
            "tier_2": "A carbonatite pipe yielding copper sulfides and apatite phosphate.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["phalaborwa_carbonatite_copper_phosphate"]
    }


def arch_36_richards_bay_mineral_sands_titanium_and_zircon(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "At Richards Bay in KwaZulu-Natal, massive coastal dune dredging operations extract **heavy mineral sands**.\n\n"
        "What key minerals are recovered from these coastal sands, and what is **titanium dioxide (TiO2)** used for globally?"
    )
    correct = "Ilmenite and rutile (sources of titanium) and zircon; titanium dioxide is the world's premier nontoxic white pigment used in paints, plastics, paper, and sunscreens because of its brilliant opacity."
    options = [
        correct,
        "Table salt and sugar; titanium dioxide is used to sweeten fruit juices and soft drinks.",
        "Pure coal and petroleum; titanium dioxide is burned in vehicle engines as rocket fuel.",
        "Gold and silver; titanium dioxide is used to mint commemorative coins."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Richards Bay Minerals:\n"
        "Dune sand dredging recovers heavy mineral suite: Ilmenite (FeTiO3), Rutile (TiO2), and Zircon (ZrSiO4).\n"
        "Step 2: TiO2 pigment applications:\n"
        "Over 90% of mined titanium is refined into pure white TiO2 pigment. Its exceptionally high refractive index (>2,7) scatters light efficiently, providing superior hiding power in coatings and paints."
    )
    return {
        "id": f"ns9_mine_36_{rng.randint(100000, 999999)}",
        "subskill": "36_richards_bay_mineral_sands_titanium_and_zircon",
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
            "tier_1": "What white pigment is refined from Richards Bay titanium sands?",
            "tier_2": "Titanium dioxide (TiO2), used as an opaque white pigment in paints and plastics.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["heavy_mineral_sands_titanium_dioxide"]
    }


def arch_37_acid_mine_drainage_pyrite_oxidation_chemistry(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "**Acid Mine Drainage (AMD)** is one of the most severe legacy environmental challenges facing South Africa's gold and coal mining districts.\n\n"
        "What chemical reaction occurs when underground gold mine workings are flooded and exposed to air and water?"
    )
    correct = "Iron pyrite (FeS2, fool's gold) in rock and tailings reacts with oxygen and water, generating sulfuric acid (H2SO4) and dissolved iron: 4FeS2 + 15O2 + 14H2O → 4Fe(OH)3 + 8H2SO4."
    options = [
        correct,
        "Limestone reacts with nitrogen gas to create drinkable mineral water.",
        "Pure gold reacts with carbon dioxide to form sweet sugary syrup.",
        "Granite dissolves into harmless salt that purifies all groundwater."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Pyrite oxidation stoichiometry:\n"
        "Pyrite (FeS2) is abundant in Witwatersrand gold reefs and Karoo coal seams.\n"
        "Step 2: Acid generation:\n"
        "2FeS2 + 7O2 + 2H2O → 2Fe²⁺ + 4SO4²⁻ + 4H⁺.\n"
        "Further oxidation catalyzed by Acidithiobacillus ferrooxidans bacteria generates ferric ions that accelerate pyrite breakdown, producing massive quantities of corrosive sulfuric acid."
    )
    return {
        "id": f"ns9_mine_37_{rng.randint(100000, 999999)}",
        "subskill": "37_acid_mine_drainage_pyrite_oxidation_chemistry",
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
            "tier_1": "What mineral oxidizes in water and air to create sulfuric acid?",
            "tier_2": "Iron pyrite (FeS2) oxidizes to produce sulfuric acid (H2SO4).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["acid_mine_drainage_pyrite_oxidation"]
    }


def arch_38_acid_mine_drainage_heavy_metal_aquatic_toxicity(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "When untreated Acid Mine Drainage (AMD) decants into South African rivers (such as the Vaal or Olifants catchments), it has a pH as low as 2 to 3.\n\n"
        "How does extreme acidity cause lethal toxic pollution in river ecosystems?"
    )
    correct = "The highly acidic water dissolves and leaches toxic heavy metals (aluminum, manganese, iron, and radioactive uranium) out of rocks, poisoning fish gills, wiping out aquatic organisms, and contaminating irrigation water."
    options = [
        correct,
        "The acidic water makes fish grow to ten times their normal size and live forever.",
        "The water freezes all aquatic plants into solid glass blocks on hot summer days.",
        "The acidity turns river water into sparkling apple juice safe for drinking."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Low pH and metal solubility:\n"
        "Heavy metals (Al³⁺, Mn²⁺, Fe³⁺, UO2²⁺) are insoluble at neutral pH but dissolve rapidly in strong acid.\n"
        "Step 2: Ecological toxicity:\n"
        "Aluminium ions precipitate on fish gills causing asphyxiation; heavy metals bioaccumulate in food webs, destroying benthic invertebrates and rendering water unfit for agriculture or human consumption."
    )
    return {
        "id": f"ns9_mine_38_{rng.randint(100000, 999999)}",
        "subskill": "38_acid_mine_drainage_heavy_metal_aquatic_toxicity",
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
            "tier_1": "What does acidic water leach out of rocks into rivers?",
            "tier_2": "It leaches toxic heavy metals (Al, Mn, U) that poison aquatic life.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["amd_heavy_metal_toxicity_aquatic"]
    }


def arch_39_mine_tailings_storage_facilities_dust_and_stability(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "The vast yellow mine dumps across Johannesburg and the East/West Rand are **Tailings Storage Facilities (TSFs)**.\n\n"
        "What major environmental and community health hazard is posed by un-rehabilitated dry gold tailings dams in windy winter weather?"
    )
    correct = "Blowing fine silica dust containing toxic trace arsenic and radioactive uranium particles causes chronic respiratory illness and eye irritation in nearby high-density residential townships."
    options = [
        correct,
        "The dumps emit pleasant floral perfume that attracts swarms of butterfly pollinators.",
        "The dumps absorb sound waves, preventing residents from hearing thunder storms.",
        "The dumps freeze ambient air, causing indoor snowflakes to fall in surrounding homes."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Tailings material characteristics:\n"
        "Milled to <75 micrometers (respirable silt/sand fraction).\n"
        "Step 2: Atmospheric dispersion hazard:\n"
        "Dry windy highveld winters lift fine particulate matter (PM10 and PM2.5). Unvegetated dumps disperse dust containing free crystalline silica, heavy metals, and radon gas daughter products into neighboring communities."
    )
    return {
        "id": f"ns9_mine_39_{rng.randint(100000, 999999)}",
        "subskill": "39_mine_tailings_storage_facilities_dust_and_stability",
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
            "tier_1": "What blows off dry mine dumps into nearby communities?",
            "tier_2": "Fine silica dust with trace toxic metals causing chronic respiratory illness.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["tailings_storage_dust_community_hazard"]
    }


def arch_40_dolomitic_dewatering_and_catastrophic_sinkholes(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In the Far West Rand goldfields (e.g. Carletonville and Merafong), deep mining required pumping millions of liters of water out of overlying **dolomite rock aquifers**.\n\n"
        "What catastrophic ground stability disaster was triggered by this large-scale dewatering?"
    )
    correct = "Lowering the water table removed buoyant support from water-filled subterranean karst dissolution caverns in the dolomite, causing cavern roofs to collapse and swallowing roads, homes, and mine buildings into sudden catastrophic sinkholes."
    options = [
        correct,
        "The ground rose into active volcanic mountains that erupted lava over the town.",
        "The aquifer turned into solid blocks of ice that pushed buildings into the sky.",
        "Underground rivers turned into petroleum that flooded street gutters."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Dolomite karst hydrogeology:\n"
        "Chuniespoort Group dolomites contain ancient dissolution cavities formed by acidic groundwater.\n"
        "Step 2: Dewatering collapse mechanism:\n"
        "Pumping water to keep deep gold stopes dry depleted the water table. Loss of hydrostatic pore pressure destabilized overlying residual wad and soil arches, triggering catastrophic sudden sinkholes."
    )
    return {
        "id": f"ns9_mine_40_{rng.randint(100000, 999999)}",
        "subskill": "40_dolomitic_dewatering_and_catastrophic_sinkholes",
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
            "tier_1": "What happens when water is pumped out of cavernous dolomite rock?",
            "tier_2": "Loss of buoyant water support causes subterranean cavern collapse (sinkholes).",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["dolomitic_dewatering_karst_sinkholes"]
    }


def arch_41_silicosis_quartz_dust_respiratory_occupational_disease(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "For decades, underground hard-rock gold miners in South Africa have faced the serious occupational lung disease known as **silicosis**.\n\n"
        "What causes silicosis, and how does it damage human lung tissue?"
    )
    correct = "Inhaling microscopic respirable crystalline silica (quartz) dust from rock drilling and blasting; alveolar macrophages engulf the sharp silica particles, triggering permanent chronic inflammation, progressive nodular fibrosis (scarring), and breathing disability."
    options = [
        correct,
        "Drinking cold mine water contaminated with dissolved gold coins.",
        "Standing too close to high-speed ventilation fans on cold mornings.",
        "Wearing protective leather boots that restrict blood circulation in miners' feet."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Etiology of silicosis:\n"
        "Gold reefs reside in quartzite host rocks (>90% free silica).\n"
        "Step 2: Pathophysiology:\n"
        "Dust particles <5 µm reach lung alveoli. Macrophages cannot digest silica; cell death releases inflammatory cytokines, stimulating collagen deposition and irreversible fibrotic nodule formation. Silicosis drastically increases vulnerability to tuberculosis (silico-tuberculosis)."
    )
    return {
        "id": f"ns9_mine_41_{rng.randint(100000, 999999)}",
        "subskill": "41_silicosis_quartz_dust_respiratory_occupational_disease",
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
            "tier_1": "What microscopic dust particles cause silicosis in gold miners?",
            "tier_2": "Respirable crystalline silica (quartz) dust causing permanent lung fibrosis.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["silicosis_crystalline_silica_fibrosis"]
    }


def arch_42_mine_safety_rockbursts_and_deep_seismic_mitigation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In ultra-deep gold and platinum mines operating kilometers beneath the surface, **rockbursts** present a severe safety hazard.\n\n"
        "What causes a rockburst, and what geotechnical engineering method is used to protect working miners?"
    )
    correct = "Immense lithostatic overburden stress causes brittle rock around excavations to suddenly shatter and violently explode into the tunnel; engineers mitigate this by pumping cement-stabilized tailings backfill into mined stopes and installing yielding rockbolts and wire mesh."
    options = [
        correct,
        "Rockbursts are caused by subterranean ghosts screaming inside caves; engineers burn incense to quiet them.",
        "Rockbursts are caused by rainwater freezing into ice cubes; engineers install outdoor electric blankets.",
        "Rockbursts are caused by miners talking loudly; engineers require miners to whisper at all times."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Geotechnical mechanism of rockbursts:\n"
        "At 3–4 km depth, confining stress exceeds rock compressive strength. Blasting concentrates stress in abutment pillars until sudden shear rupture releases stored elastic strain energy, ejecting rock violently.\n"
        "Step 2: Support mitigation:\n"
        "Yielding tendons (split sets, cable anchors) and chain-link mesh absorb kinetic energy, while backfilling old stopes with dewatered tailings distributes regional ground load."
    )
    return {
        "id": f"ns9_mine_42_{rng.randint(100000, 999999)}",
        "subskill": "42_mine_safety_rockbursts_and_deep_seismic_mitigation",
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
            "tier_1": "What violent event occurs when high rock stress causes tunnels to explode?",
            "tier_2": "Rockbursts mitigated by yielding rockbolts, mesh, and tailings backfilling.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["rockburst_seismic_mitigation_backfill"]
    }


def arch_43_mine_rehabilitation_topsoil_stockpiling_and_revegetation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Under South African environmental law, mining companies must execute a comprehensive **mine closure and rehabilitation plan**.\n\n"
        "What sequence of earthmoving and ecological steps restores an open-cast mine site to sustainable post-mining land use?"
    )
    correct = "Backfilling open pits with waste rock, reprofiling steep slopes to natural contours, replacing previously stockpiled fertile topsoil, and reseeding with indigenous grasses and trees to prevent erosion and restore biodiversity."
    options = [
        correct,
        "Flooding the open pit with crude oil and building plastic factories across the pit floor.",
        "Paving the entire open pit with solid black asphalt to make an airport runway.",
        "Covering the open pit with giant glass mirrors to reflect sunlight into outer space."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Mine rehabilitation sequence:\n"
        "1. Infill pit void with overburden/waste rock.\n"
        "2. Contour and grade slopes to stable angles (<18°) to prevent gullying.\n"
        "3. Replace preserved topsoil containing original seed bank and mycorrhizal fungi.\n"
        "4. Revegetation with hardy indigenous climax species (e.g. Acacia, Themeda triandra).\n"
        "Step 2: Long-term monitoring of water quality and vegetation canopy."
    )
    return {
        "id": f"ns9_mine_43_{rng.randint(100000, 999999)}",
        "subskill": "43_mine_rehabilitation_topsoil_stockpiling_and_revegetation",
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
            "tier_1": "How is an open pit restored to nature?",
            "tier_2": "Backfilling, contouring slopes, replacing topsoil, and replanting indigenous vegetation.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mine_rehabilitation_topsoil_revegetation"]
    }


def arch_44_water_treatment_limestone_neutralization_of_acid_water(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "To remediate Acid Mine Drainage (AMD) before discharging water into natural streams, treatment plants use **chemical neutralization**.\n\n"
        "What happens when slaked lime (calcium hydroxide, Ca(OH)2) is dosed into acidic mine water containing sulfuric acid (H2SO4)?"
    )
    correct = "The base neutralizes the acid (H2SO4 + Ca(OH)2 → CaSO4 + 2H2O), raising pH above 7; as pH rises, dissolved heavy metals lose solubility and precipitate out as solid metal hydroxide sludge (e.g. Fe(OH)3, Al(OH)3)."
    options = [
        correct,
        "The water explodes into radioactive sparks and turns into pure gasoline.",
        "The acid turns into pure gold nuggets that settle to the bottom of the tank.",
        "The water boils away into poisonous chlorine gas, leaving behind dry salt."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Acid-base neutralization:\n"
        "H⁺(aq) + OH⁻(aq) → H2O(l).\n"
        "Ca(OH)2 neutralizes sulfuric acid, forming gypsum precipitate: Ca²⁺ + SO4²⁻ + 2H2O → CaSO4·2H2O(s).\n"
        "Step 2: Metal precipitation:\n"
        "Raising pH to ~8,5 causes Fe³⁺, Al³⁺, and other heavy metals to precipitate as insoluble hydroxides, leaving treated water safe for industrial re-use."
    )
    return {
        "id": f"ns9_mine_44_{rng.randint(100000, 999999)}",
        "subskill": "44_water_treatment_limestone_neutralization_of_acid_water",
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
            "tier_1": "What happens when a base like Ca(OH)2 neutralizes sulfuric acid?",
            "tier_2": "It neutralizes acidity, forms gypsum, and precipitates toxic heavy metal hydroxides.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["water_treatment_neutralization_precipitation"]
    }


def arch_45_mining_economic_significance_gdp_and_foreign_exchange(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Mining has been the historical foundation of modern South Africa's industrial economy for over 150 years.\n\n"
        "What primary macroeconomic contributions does the mining industry continue to make to South Africa?"
    )
    correct = "It contributes approximately 7% to 8% directly to national GDP, accounts for over 50% of the country's total merchandise export earnings, directly employs nearly 450 000 workers, and underwrites critical rail and energy infrastructure."
    options = [
        correct,
        "It employs only three people nationwide and contributes 0,001% of export earnings.",
        "It operates entirely on paper with zero physical exports or real economic impact.",
        "It generates 100% of the nation's food and agricultural grain crops."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: Direct GDP contribution:\n"
        "Mining contributes ~R400–R500 billion annually (~7–8% of direct GDP, ~12% indirect GDP multiplier).\n"
        "Step 2: Foreign exchange and employment:\n"
        "PGMs, gold, coal, iron ore, and manganese are South Africa's largest earners of foreign exchange, funding imports and sustaining ~450 000 direct mining jobs and over 1,5 million dependent livelihoods."
    )
    return {
        "id": f"ns9_mine_45_{rng.randint(100000, 999999)}",
        "subskill": "45_mining_economic_significance_gdp_and_foreign_exchange",
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
            "tier_1": "What fraction of SA exports and jobs come from mining?",
            "tier_2": ">50% of export earnings, ~7–8% of GDP, and ~450 000 direct jobs.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mining_macroeconomic_contribution_sa"]
    }


def arch_46_mining_infrastructure_freight_rail_and_saldanha_port(rng: random.Random) -> Dict[str, Any]:
    corridor = rng.choice([
        ("Sishen–Saldanha Iron Ore Line (Orex)", "861 km dedicated heavy-haul freight railway carrying massive iron ore trains across the arid Karoo to the deepwater port of Saldanha Bay for bulk sea export"),
        ("Mpumalanga–Richards Bay Coal Line", "dedicated electric freight railway transporting millions of tonnes of bituminous coal to the Richards Bay Coal Terminal (RBCT), one of the world's largest coal export terminals")
    ])
    line_name, desc = corridor
    prompt = (
        f"South Africa's bulk mineral export industry depends on dedicated freight rail corridors and deepwater ports.\n\n"
        f"What infrastructure role is fulfilled by the **{line_name}**?"
    )
    correct = f"It is a {desc}."
    options = [
        correct,
        "It is a high-speed passenger monorail carrying tourists on game reserve safaris.",
        "It is an underground freshwater canal providing tap water to coastal desert towns.",
        "It is a pipeline pumping crude oil from Antarctica into Johannesburg power stations."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Purpose of {line_name}:\n"
        "Bulk commodities (iron ore, coal) require low-cost transport over long distances to coastal export harbors.\n"
        f"Step 2: Operating characteristics:\n"
        f"It is a {desc}."
    )
    return {
        "id": f"ns9_mine_46_{rng.randint(100000, 999999)}",
        "subskill": "46_mining_infrastructure_freight_rail_and_saldanha_port",
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
            "tier_1": f"Where does the {line_name[:20]} carry minerals?",
            "tier_2": f"It is a {desc[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["bulk_mineral_transport_rail_ports"]
    }


def arch_47_minerals_for_green_energy_transition_pgm_hydrogen_cells(rng: random.Random) -> Dict[str, Any]:
    min_tech = rng.choice([
        ("Platinum and Iridium", "hydrogen economy: essential catalytic coatings in Proton Exchange Membrane (PEM) water electrolyzers (producing green hydrogen) and hydrogen fuel cell electric vehicles"),
        ("Manganese and Copper", "battery energy storage: cathode active material in lithium-ion batteries and conductor wiring in electric vehicle motors and solar photovoltaic grids")
    ])
    min_name, tech_role = min_tech
    prompt = (
        f"As the global economy transitions away from fossil fuels toward clean energy, South African minerals are critical.\n\n"
        f"How do **{min_name}** contribute to the global green energy transition?"
    )
    correct = f"They are vital for the {tech_role}."
    options = [
        correct,
        "They are burned in thermal power stations to replace firewood in open braais.",
        "They are added to gasoline to make cars produce more exhaust greenhouse gases.",
        "They are used to manufacture disposable single-use plastic grocery bags."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Minerals for clean energy transition:\n"
        f"Decarbonization is mineral-intensive.\n"
        f"Step 2: Application for {min_name}:\n"
        f"They are vital for the {tech_role}."
    )
    return {
        "id": f"ns9_mine_47_{rng.randint(100000, 999999)}",
        "subskill": "47_minerals_for_green_energy_transition_pgm_hydrogen_cells",
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
            "tier_1": f"How is {min_name} used in green technology?",
            "tier_2": f"They are vital for the {tech_role[:35]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["green_energy_transition_critical_minerals"]
    }


def arch_48_economic_viability_cut_off_grade_ore_valuation_formula(rng: random.Random) -> Dict[str, Any]:
    q_tonnes = rng.choice([10000, 20000, 50000])
    p_price = rng.choice([400, 500, 600])
    total_cost = rng.choice([2000000, 3000000, 5000000])
    gross_rev = q_tonnes * p_price
    net_val = gross_rev - total_cost
    prompt = (
        f"A mining geologist models an ore deposit containing **{q_tonnes:,} tonnes** of copper ore.\n"
        f"The market price is **R{p_price} per tonne**, and total estimated costs (exploration, mining, transport) are **R{total_cost:,}**.\n\n"
        f"Using the economic viability formula: $$V = (Q \\times P) - \\text{{Costs}}$$, what is the deposit's Net Value ($V$) and is the project viable?"
    )
    if net_val > 0:
        correct = f"V = R{net_val:,}; because V > 0 (revenue exceeds total costs), the mining project is economically viable."
        alt = f"V = -R{abs(net_val):,}; because V < 0, the project is not viable."
    else:
        correct = f"V = R{net_val:,}; because V <= 0 (costs exceed or equal revenue), the mining project is not economically viable."
        alt = f"V = R{abs(net_val) + 1000000:,}; because V > 0, the project is viable."
    options = [
        correct,
        alt,
        f"V = R{gross_rev:,}; costs are completely ignored by mining economists.",
        f"V = R{total_cost:,}; market price has zero effect on project viability."
    ]
    rng.shuffle(options)
    sol = (
        f"Step 1: Calculate Gross Revenue:\n"
        f"Gross Revenue = Q × P = {q_tonnes:,} × R{p_price} = R{gross_rev:,}.\n"
        f"Step 2: Calculate Net Value:\n"
        f"V = Gross Revenue - Costs = R{gross_rev:,} - R{total_cost:,} = R{net_val:,}.\n"
        f"Step 3: Viability decision:\n"
        f"{correct}"
    )
    return {
        "id": f"ns9_mine_48_{rng.randint(100000, 999999)}",
        "subskill": "48_economic_viability_cut_off_grade_ore_valuation_formula",
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
            "tier_1": "Calculate Q × P, then subtract the total costs.",
            "tier_2": f"Gross revenue = R{gross_rev:,}. Subtract R{total_cost:,}.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["ore_economic_valuation_formula"]
    }


def arch_49_environmental_impact_assessments_mining_licensing_laws(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Under the Mineral and Petroleum Resources Development Act (MPRDA) and NEMA in South Africa, no company may mine without an approved **Environmental Management Plan (EMP)** and license.\n\n"
        "What legal requirement must a mining company satisfy before receiving a mining right?"
    )
    correct = "They must conduct an independent Environmental Impact Assessment (EIA) with public community consultation, submit a Social and Labour Plan (SLP), and provide upfront financial guarantees (bonds) for post-mining rehabilitation."
    options = [
        correct,
        "They only need to pay a cash bribe to local municipal traffic wardens with zero paperwork.",
        "They must promise never to employ any human workers and operate exclusively with robot dogs.",
        "They must guarantee that all extracted minerals will be dumped directly into the nearest river."
    ]
    rng.shuffle(options)
    sol = (
        "Step 1: South African mining statutory framework:\n"
        "MPRDA (Act 28 of 2002) and NEMA (Act 107 of 1998).\n"
        "Step 2: Core compliance mandates:\n"
        "Mining rights require: 1. Environmental Impact Assessment (EIA) assessing air/water/soil impacts; 2. Social and Labour Plan (SLP) investing in local community infrastructure and education; 3. Ring-fenced financial provisioning for environmental rehabilitation."
    )
    return {
        "id": f"ns9_mine_49_{rng.randint(100000, 999999)}",
        "subskill": "49_environmental_impact_assessments_mining_licensing_laws",
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
            "tier_1": "What assessment and community plan are legally required to get a mining license?",
            "tier_2": "Independent EIA, public consultation, Social & Labour Plan, and rehabilitation financial bond.",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mprda_eia_mining_license_compliance"]
    }


def arch_50_mining_mineral_resources_comprehensive_diagnostic_autopsy(rng: random.Random) -> Dict[str, Any]:
    min_case = rng.choice([
        ("Iron ore (hematite)", "Sishen / Kolomela open-cast pit", "crushing and magnetic/dense medium separation", "blast furnace smelting with coke and limestone flux reducing Fe2O3 to elemental Fe"),
        ("Copper ore (sulfides)", "Phalaborwa open-cast and underground", "milling and chemical froth flotation to concentrate copper sulfides", "pyrometallurgical smelting and electrolytic refining to 99,99% pure copper cathodes"),
        ("Gold ore (paleoplacer reef)", "Witwatersrand ultra-deep shaft mines", "milling to fine powder followed by cyanide leaching and Carbon-in-Pulp (CIP)", "elution, electrowinning, and smelting into 99,5% pure gold bullion doré bars")
    ])
    metal_name, mine_loc, sep_step, ref_step = min_case
    prompt = (
        f"A South African metallurgical engineer oversees the extraction of **{metal_name}**.\n\n"
        f"What complete flowsheet correctly traces the sequence from geological extraction to refined commercial metal for **{metal_name}**?"
    )
    correct = f"Mined at {mine_loc} → Comminution through {sep_step} → Final refining via {ref_step}."
    distractors = [
        f"Mined at {mine_loc} → Directly boiled in open ocean water without crushing → Freezing into ice cubes.",
        f"Mined at {mine_loc} → Baked in a household kitchen microwave oven with zero chemical processing.",
        f"Mined at {mine_loc} → Dissolved in pure milk and filtered through paper tissue napkins."
    ]
    options = [correct] + distractors
    rng.shuffle(options)
    sol = (
        f"Step 1: Mining and comminution for {metal_name}:\n"
        f"Extracted at {mine_loc}.\n"
        f"Step 2: Beneficiation flowsheet:\n"
        f"Physical separation via {sep_step}.\n"
        f"Step 3: Extractive metallurgy:\n"
        f"Final refining via {ref_step}."
    )
    return {
        "id": f"ns9_mine_50_{rng.randint(100000, 999999)}",
        "subskill": "50_mining_mineral_resources_comprehensive_diagnostic_autopsy",
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
            "tier_1": f"Follow the mining, separation, and refining steps for {metal_name}.",
            "tier_2": f"Mined at {mine_loc[:20]}... followed by {sep_step[:25]}...",
            "tier_3": f"Select: {correct}"
        },
        "misconception_tags": ["mining_comprehensive_flowsheet_autopsy"]
    }


BUILDERS_26_50 = {
    "26_indigenous_copper_smelting_phalaborwa_clay_furnaces": arch_26_indigenous_copper_smelting_phalaborwa_clay_furnaces,
    "27_traditional_iron_age_bloomery_smelting_tuyeres": arch_27_traditional_iron_age_bloomery_smelting_tuyeres,
    "28_witwatersrand_gold_paleoplacer_conglomerate_basin": arch_28_witwatersrand_gold_paleoplacer_conglomerate_basin,
    "29_bushveld_complex_merensky_ug2_platinum_chromite": arch_29_bushveld_complex_merensky_ug2_platinum_chromite,
    "30_sishen_and_kolomela_hematite_iron_ore_corridor": arch_30_sishen_and_kolomela_hematite_iron_ore_corridor,
    "31_kalahari_manganese_field_global_resource_significance": arch_31_kalahari_manganese_field_global_resource_significance,
    "32_highveld_coalfields_emalahleni_thermal_power_generation": arch_32_highveld_coalfields_emalahleni_thermal_power_generation,
    "33_kimberley_big_hole_volcanic_pipe_diamond_rush": arch_33_kimberley_big_hole_volcanic_pipe_diamond_rush,
    "34_cullinan_mine_gem_diamonds_premier_pipe": arch_34_cullinan_mine_gem_diamonds_premier_pipe,
    "35_phalaborwa_carbonatite_complex_copper_and_phosphate": arch_35_phalaborwa_carbonatite_complex_copper_and_phosphate,
    "36_richards_bay_mineral_sands_titanium_and_zircon": arch_36_richards_bay_mineral_sands_titanium_and_zircon,
    "37_acid_mine_drainage_pyrite_oxidation_chemistry": arch_37_acid_mine_drainage_pyrite_oxidation_chemistry,
    "38_acid_mine_drainage_heavy_metal_aquatic_toxicity": arch_38_acid_mine_drainage_heavy_metal_aquatic_toxicity,
    "39_mine_tailings_storage_facilities_dust_and_stability": arch_39_mine_tailings_storage_facilities_dust_and_stability,
    "40_dolomitic_dewatering_and_catastrophic_sinkholes": arch_40_dolomitic_dewatering_and_catastrophic_sinkholes,
    "41_silicosis_quartz_dust_respiratory_occupational_disease": arch_41_silicosis_quartz_dust_respiratory_occupational_disease,
    "42_mine_safety_rockbursts_and_deep_seismic_mitigation": arch_42_mine_safety_rockbursts_and_deep_seismic_mitigation,
    "43_mine_rehabilitation_topsoil_stockpiling_and_revegetation": arch_43_mine_rehabilitation_topsoil_stockpiling_and_revegetation,
    "44_water_treatment_limestone_neutralization_of_acid_water": arch_44_water_treatment_limestone_neutralization_of_acid_water,
    "45_mining_economic_significance_gdp_and_foreign_exchange": arch_45_mining_economic_significance_gdp_and_foreign_exchange,
    "46_mining_infrastructure_freight_rail_and_saldanha_port": arch_46_mining_infrastructure_freight_rail_and_saldanha_port,
    "47_minerals_for_green_energy_transition_pgm_hydrogen_cells": arch_47_minerals_for_green_energy_transition_pgm_hydrogen_cells,
    "48_economic_viability_cut_off_grade_ore_valuation_formula": arch_48_economic_viability_cut_off_grade_ore_valuation_formula,
    "49_environmental_impact_assessments_mining_licensing_laws": arch_49_environmental_impact_assessments_mining_licensing_laws,
    "50_mining_mineral_resources_comprehensive_diagnostic_autopsy": arch_50_mining_mineral_resources_comprehensive_diagnostic_autopsy,
}
