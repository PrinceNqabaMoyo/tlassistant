"""Grade 9 Natural Sciences - Reactions of Metals with Oxygen: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards.
Grounded in curriculum_docs_auto/NaturalSciences_Gr9/Term 2/02. Reactions of metals with oxygen.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from .reactions_metals_oxygen_archetypes_01_25 import _q


def arch_26_rust_mechanical_failure_structural_loss(rng: random.Random) -> Dict[str, Any]:
    part = rng.choice(["heavy-duty security chain", "corrugated barn roof truss", "steel door hinge", "tractor axle bolt"])
    prompt = (
        f"When a **{part}** becomes severely rusted, it is no longer as strong or flexible as when newly forged.\n\n"
        "1. Explain chemically why rusting destroys the load-bearing strength of the component [2].\n"
        "2. Explain why rusty hinges seize or snap under tension [1]."
    )
    correct = "Metallic iron loses metallic bonds as it transforms into weak, crumbly iron(III) oxide powder; Flaky oxide expands, jams clearances, and thins the load-bearing steel core until fracture."
    sol = (
        "**Step 1:** Metallic iron atoms are held by strong, ductile metallic bonds, whereas rust ($\\text{Fe}_2\\text{O}_3$) is a **brittle, crumbling ionic oxide** that peels away and shrinks the load-bearing metal thickness [2].\n\n"
        "**Step 2:** Expanded flaky oxide jams moving parts while the thinned metal core snaps under load [1]."
    )
    return _q(
        rng, "26", "26_rust_mechanical_failure_structural_loss", prompt, correct, sol, 3, "structured",
        ["rust_mechanical_strength_confusion"],
        "Compare the physical strength of metallic iron with crumbly rust powder.",
        "Iron loses ductile metallic bonding and thickness as flakes drop off.",
        correct,
    )


def arch_27_wood_and_aluminium_alternative_materials_coastal_homes(rng: random.Random) -> Dict[str, Any]:
    town = rng.choice(["Umhlanga", "Muizenberg", "Jeffreys Bay", "Hermanus", "Ballito"])
    alt = rng.choice([
        ("treated hardwood", "does not contain iron and undergoes biological decay resistance rather than iron rusting"),
        ("anodised aluminium", "forms a thin airtight Al2O3 shield rather than porous iron rust"),
    ])
    mat_name, reason = alt
    prompt = (
        f"Homeowners building window frames and patio doors in coastal **{town}** often specify **{mat_name}** instead of bare mild steel.\n\n"
        f"Why is **{mat_name}** chosen over bare iron-based steel along the South African coastline?"
    )
    correct = f"Neither contains rust-prone iron, and {mat_name} {reason}, surviving humid sea-salt spray far longer."
    options = [
        correct,
        "Sea-salt spray dissolves wood and aluminium immediately into pure iron ingots.",
        "Mild steel is only magnetic indoors and melts in ocean sunlight.",
        f"{mat_name.capitalize()} generates electricity that evaporates ocean humidity.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Mild steel rusts rapidly in salt-laden coastal humidity.\n"
        f"**Step 2:** Switching to **{mat_name}** avoids iron rusting because it {reason} [2]."
    )
    return _q(
        rng, "27", "27_wood_and_aluminium_alternative_materials_coastal_homes", prompt, correct, sol, 2, "multiple_choice",
        ["all_metals_rust_myth"],
        "Does every material suffer from red flaky iron rust?",
        f"Remember only iron/steel forms flaky rust; {mat_name} {reason}.",
        correct, options=options,
    )


def arch_28_aluminium_self_passivating_oxide_layer_advantage(rng: random.Random) -> Dict[str, Any]:
    product = rng.choice(["coastal sliding-door frame", "aircraft fuselage panel", "outdoor aluminium ladder", "beverage can"])
    prompt = (
        f"Even though aluminium sits **higher** on the reactivity series than iron, an **{product}** resists destructive deep corrosion outdoors.\n\n"
        "1. Write the balanced chemical equation for aluminium forming aluminium oxide ($\\text{Al}_2\\text{O}_3$) [2].\n"
        "2. Contrast the physical structure of aluminium oxide vs iron rust on metal surfaces [2]."
    )
    correct = "4Al + 3O2 -> 2Al2O3; Aluminium oxide forms a thin, dense, airtight protective skin that seals underlying metal, whereas iron oxide flakes off exposing fresh iron."
    sol = (
        "**Step 1:** Balanced reaction: **$$4\\text{Al} + 3\\text{O}_2 \\rightarrow 2\\text{Al}_2\\text{O}_3$$** [2].\n\n"
        "**Step 2:** Unlike porous, flaky rust that drops off iron, $\\text{Al}_2\\text{O}_3$ bonds tightly into an **impermeable self-passivating barrier**, shielding deeper aluminium atoms from further oxygen and water [2]."
    )
    return _q(
        rng, "28", "28_aluminium_self_passivating_oxide_layer_advantage", prompt, correct, sol, 4, "structured",
        ["aluminium_rusting_myth"],
        "Think about whether the oxide layer seals the metal tightly or crumbles away.",
        "4Al + 3O2 -> 2Al2O3 forms an airtight barrier film.",
        correct,
    )


def arch_29_barrier_protection_painting_and_enamelling(rng: random.Random) -> Dict[str, Any]:
    obj = rng.choice(["wrought-iron driveway gate", "highway steel bridge girder", "outdoor steel swing frame", "roof gutter bracket"])
    prompt = (
        f"Maintenance crews apply primer and glossy oil-based paint onto a **{obj}**.\n\n"
        "1. Explain how a continuous paint layer prevents rusting [1].\n"
        "2. Explain what begins happening if a stone chips a **5 mm** scratch through the paint down to bare iron [2]."
    )
    correct = "1. Paint forms a physical barrier excluding oxygen and water from iron; 2. Exposed iron in the chip contacts air and moisture, initiating rust that creeps underneath surrounding paint."
    sol = (
        "**Step 1:** Paint acts as an impermeable **physical barrier**, sealing the iron surface off from both oxygen and moisture [1].\n\n"
        "**Step 2:** Once scratched, **bare iron is exposed** to air and water; rust forms at the chip and pushes outward under adjacent paint edges because paint offers **no sacrificial protection** [2]."
    )
    return _q(
        rng, "29", "29_barrier_protection_painting_and_enamelling", prompt, correct, sol, 3, "structured",
        ["paint_sacrificial_confusion"],
        "Painting is purely a barrier method — does paint react chemically on behalf of iron when scratched?",
        "If paint scratches, oxygen and water reach bare iron directly.",
        correct,
    )


def arch_30_barrier_protection_oiling_and_greasing(rng: random.Random) -> Dict[str, Any]:
    item = rng.choice(["mountain bike chain", "steel engine piston rings", "workshop vernier calipers", "gate padlock shackle"])
    prompt = (
        f"Why do mechanics lubricate a **{item}** with oil or thick grease rather than painting it?\n\n"
        "State **both** the corrosion-prevention mechanism and the mechanical reason oil/grease is chosen [2]."
    )
    correct = "Hydrophobic oil/grease repels water moisture and seals out oxygen; It permits smooth low-friction movement where rigid paint would crack, jam, and flake off."
    sol = (
        "**Step 1:** Hydrophobic oil/grease coats metal threads and excludes **water and oxygen** (barrier protection) [1].\n\n"
        "**Step 2:** Moving/sliding components would **crack and peel rigid paint**, whereas liquid oil or grease reduces mechanical friction while moving [1]."
    )
    return _q(
        rng, "30", "30_barrier_protection_oiling_and_greasing", prompt, correct, sol, 2, "short_answer",
        ["lubrication_rust_prevention_confusion"],
        "Think of two things a moving steel mechanism needs: keeping water out + staying flexible.",
        "Oil repels water/air AND reduces friction without cracking when parts move.",
        correct,
    )


def arch_31_galvanising_zinc_coating_mechanism(rng: random.Random) -> Dict[str, Any]:
    item = rng.choice(["corrugated steel roofing sheet", "farm barbed-wire fencing", "galvanised steel bucket", "highway crash barrier"])
    prompt = (
        f"Manufacturers dip a **{item}** into molten **zinc** during production—a process called **galvanising**.\n\n"
        "1. Define what galvanising means [1].\n"
        "2. Identify TWO common South African household or construction items protected in this way [2]."
    )
    correct = "Coating iron or steel objects with a protective thin outer layer of zinc metal; Examples include corrugated roofing sheets, fencing wire, nails, and steel buckets."
    sol = (
        "**Step 1:** **Galvanising** is the industrial process of coating iron or steel with a thin outer layer of **zinc (Zn)** to resist rusting [1].\n\n"
        "**Step 2:** Everyday examples: **corrugated roof sheets (sinkplate)**, diamond-mesh fencing, roofing nails, water tanks, and street light poles [2]."
    )
    return _q(
        rng, "31", "31_galvanising_zinc_coating_mechanism", prompt, correct, sol, 3, "short_answer",
        ["galvanising_is_painting_myth"],
        "Which metal is fused onto iron when an object is galvanised?",
        "Zinc coating seals steel sheets, nails, and fencing.",
        correct,
    )


def arch_32_sacrificial_protection_scratched_galvanised_iron(rng: random.Random) -> Dict[str, Any]:
    scratch_mm = rng.choice([2, 3, 4, 5])
    prompt = (
        f"A worker accidentally cuts a deep **{scratch_mm} mm** scratch across a galvanised roof sheet, exposing bare steel beneath the zinc coating. Even after rain, the exposed steel strip stays unrusted.\n\n"
        "Which scientific mechanism explains why zinc still protects scratched iron?"
    )
    correct = "Sacrificial protection: zinc is more reactive than iron, so zinc oxidises preferentially instead of iron even when exposed side by side."
    options = [
        correct,
        "Zinc melts back into liquid whenever rain falls and seals every scratch completely.",
        "Iron becomes magnetically immune to oxygen molecules once touched by zinc.",
        "Zinc destroys all oxygen atoms within 10 metres of the rooftop.",
    ]
    rng.shuffle(options)
    sol = (
        "**Step 1:** Zinc sits **higher on the reactivity series** than iron.\n"
        "**Step 2:** When air and rainwater contact both metals in a scratch, zinc oxidises first (**sacrificial protection**), giving away electrons and keeping the iron intact [2]."
    )
    return _q(
        rng, "32", "32_sacrificial_protection_scratched_galvanised_iron", prompt, correct, sol, 2, "multiple_choice",
        ["galvanizing_sacrificial_protection_error", "sacrificial_metal_reactivity_inversion"],
        "Compare the reactivity of zinc versus iron.",
        "More reactive Zn oxidises ('sacrifices' itself) so Fe does not rust.",
        correct, options=options,
    )


def arch_33_electroplating_chromium_chrome_taps_and_bumpers(rng: random.Random) -> Dict[str, Any]:
    part = rng.choice(["bathroom mixer tap", "vintage bakkie bumper", "bicycle handlebar", "kitchen kettle spout"])
    prompt = (
        f"A steel **{part}** has a mirror-bright silvery finish that resists corrosion even when washed daily.\n\n"
        "1. Name the unreactive metal electroplated onto steel to create this finish [1].\n"
        "2. Explain **how** electroplating prevents rusting and name one aesthetic advantage [2]."
    )
    correct = "Chromium (chrome plating); Deposits an impermeable corrosion-resistant metal barrier blocking air and water, while providing a hard shiny mirror finish."
    sol = (
        "**Step 1:** The metal electroplated onto steel is **chromium (Cr)** [1].\n\n"
        "**Step 2:** Chromium forms a **tough, non-rusting outer metallic barrier** excluding water and oxygen while giving a scratch-resistant **mirror-bright silver finish** [2]."
    )
    return _q(
        rng, "33", "33_electroplating_chromium_chrome_taps_and_bumpers", prompt, correct, sol, 3, "short_answer",
        ["electroplating_barrier_error"],
        "Think about the shiny 'chrome' coating on taps and car trim.",
        "Chromium electroplating provides an unreactive airtight shield plus shiny appearance.",
        correct,
    )


def arch_34_stainless_steel_alloying_chromium_nickel(rng: random.Random) -> Dict[str, Any]:
    item = rng.choice(["hospital surgical scalpel", "kitchen sink basin", "dining knife and fork", "dairy processing tank"])
    cr_pct = rng.choice(["12%–18%", "18%", "10,5%–18%"])
    prompt = (
        f"A **{item}** is manufactured from **stainless steel** containing iron alloyed with **{cr_pct} chromium** (and nickel).\n\n"
        "1. Why does stainless steel resist rusting throughout its entire body, even after deep surface scratches or sharpening? [2]\n"
        "2. How does stainless steel differ structurally from painted iron? [1]"
    )
    correct = "Chromium is alloyed uniformly throughout the steel and instantly forms a microscopic self-healing invisible chromium oxide film on any fresh surface; Painted iron only has an external skin coating."
    sol = (
        "**Step 1:** Because chromium is melted **throughout the entire alloy**, any fresh scratch still contains chromium atoms that immediately form an ultra-thin invisible chromium oxide film blocking oxygen and water [2].\n\n"
        "**Step 2:** Painted iron relies on a surface skin that peels when damaged, whereas stainless steel's corrosion resistance exists **internally throughout the whole metal** [1]."
    )
    return _q(
        rng, "34", "34_stainless_steel_alloying_chromium_nickel", prompt, correct, sol, 3, "structured",
        ["stainless_steel_coating_myth"],
        "Is chromium only painted on the outside of stainless steel, or mixed right through the molten metal?",
        "Alloying distributes chromium internally through the entire bulk.",
        correct,
    )


def arch_35_plastic_and_powder_coating_metal_fences(rng: random.Random) -> Dict[str, Any]:
    product = rng.choice(["palisade security fence", "dishwasher wire rack", "garden patio chair frame", "electric cable armour"])
    prompt = (
        f"Manufacturers bake tough plastic polymer powder onto a steel **{product}**.\n\n"
        "Explain why plastic/powder coating protects steel more durably outdoors than a thin coat of basic chalky paint, yet what happens if heavy abrasion strips the plastic off [2]."
    )
    correct = "Thick flexible baked polymer creates an impervious moisture/oxygen barrier resistant to chipping; If deep abrasion strips it bare, exposed iron still rusts without sacrificial metal."
    sol = (
        "**Step 1:** Plastic/powder coating bonds into a thick, impact-resistant polymer sheath blocking **$H_2O$ and $O_2$** [1].\n\n"
        "**Step 2:** However, plastic is still solely a **barrier**—once cracked or torn open, bare steel underneath begins rusting normally [1]."
    )
    return _q(
        rng, "35", "35_plastic_and_powder_coating_metal_fences", prompt, correct, sol, 2, "short_answer",
        ["plastic_coating_mechanism"],
        "Identify whether plastic coating is a barrier or sacrificial method.",
        "Thick flexible polymer barrier; deep tears expose steel to rusting.",
        correct,
    )


def arch_36_identifying_rust_prevention_method_by_application(rng: random.Random) -> Dict[str, Any]:
    scenario, answer = rng.choice([
        ("Lubricating a motorcycle drive chain", "Oiling / greasing (hydrophobic barrier + low friction)"),
        ("Zinc-coating a corrugated iron roof", "Galvanising (barrier + sacrificial zinc protection)"),
        ("Making rust-proof surgeon scissors", "Alloying iron with chromium/nickel (stainless steel)"),
        ("Refinishing a scratched park steel bench", "Painting (polymer/oil barrier exclusion of air and water)"),
    ])
    prompt = (
        f"Match the practical protection challenge **\"{scenario}\"** to the **most suitable rust-prevention technique** and briefly state why [2]."
    )
    correct = answer
    sol = f"**Step 1 & 2:** The optimal industrial/practical technique is **{answer}** [2]."
    return _q(
        rng, "36", "36_identifying_rust_prevention_method_by_application", prompt, correct, sol, 2, "short_answer",
        ["rust_method_application_mismatch"],
        "Consider movement, weathering cost, durability, or hygienic requirement.",
        f"Match '{scenario}' -> {answer}.",
        correct,
    )


def arch_37_calcium_and_sodium_combustion_flame_colors(rng: random.Random) -> Dict[str, Any]:
    metal, flame, eq, ox = rng.choice([
        ("Sodium (Na)", "intense golden-yellow flame", "4Na + O2 -> 2Na2O", "sodium oxide (Na2O)"),
        ("Calcium (Ca)", "bright brick-red/orange flame", "2Ca + O2 -> 2CaO", "calcium oxide (CaO)"),
        ("Potassium (K)", "lilac/violet flame", "4K + O2 -> 2K2O", "potassium oxide (K2O)"),
    ])
    prompt = (
        f"A small cleaned piece of **{metal}** is warmed in an oxygen jar until it catches alight.\n\n"
        f"1. Identify the characteristic **flame colour** observed when {metal} burns [1].\n"
        f"2. Name the white solid oxide formed and write the **balanced chemical equation** [2]."
    )
    correct = f"Flame colour: {flame}; Product: {ox}; Equation: {eq}"
    sol = (
        f"**Step 1:** {metal} burns vigorously with a characteristic **{flame}** [1].\n\n"
        f"**Step 2:** It forms white **{ox}** according to **$$\\text{{{eq}}}$$** [2]."
    )
    return _q(
        rng, "37", "37_calcium_and_sodium_combustion_flame_colors", prompt, correct, sol, 3, "structured",
        ["metal_flame_color_error"],
        "Group 1 and 2 metals show distinct diagnostic flame colours during combustion.",
        f"Match {metal} -> {flame}, product {ox}, balanced equation {eq}.",
        correct,
    )


def arch_38_reactivity_series_oxygen_order_experiment(rng: random.Random) -> Dict[str, Any]:
    order_q = rng.choice([
        ("Magnesium, Iron, Copper, Gold", "Magnesium > Iron > Copper > Gold", "from MOST reactive to LEAST reactive"),
        ("Zinc, Copper, Potassium, Iron", "Potassium > Zinc > Iron > Copper", "from MOST reactive to LEAST reactive"),
    ])
    metals_list, ordered_ans, direction = order_q
    prompt = (
        f"Equal dry ribbons or filings of four metals (**{metals_list}**) are heated equally in Bunsen air.\n\n"
        f"Arrange these metals **{direction}** toward oxygen, and justify the placement of the least reactive metal [3]."
    )
    correct = f"{ordered_ans}; Least reactive metal sits last because it reacts either very slowly on surface heating (Copper) or does not oxidise at all (Gold)."
    sol = (
        f"**Step 1:** Reactivity order toward oxygen: **{ordered_ans}** [2].\n\n"
        "**Step 2:** Metals like gold are noble and remain completely unoxidised even on strong heating, while reactive metals ignite fiercely [1]."
    )
    return _q(
        rng, "38", "38_reactivity_series_oxygen_order_experiment", prompt, correct, sol, 3, "short_answer",
        ["metal_reactivity_order_error"],
        "Rank metals by vigour: dazzling flash flame > bright sparks > surface blackening > zero reaction.",
        f"Order {direction}: {ordered_ans}.",
        correct,
    )


def arch_39_noble_unreactive_metals_gold_platinum_jewelry(rng: random.Random) -> Dict[str, Any]:
    metal = rng.choice(["gold (Au)", "platinum (Pt)"])
    region = rng.choice(["Witwatersrand goldfields", "Bushveld Igneous Complex platinum reefs"])
    prompt = (
        f"South Africa's **{region}** yield pure **{metal}** mined for rings and electronic contacts that remain shiny after decades in humid air.\n\n"
        f"Why does **{metal}** remain untarnished and unoxidised where iron rapidly crumbles?"
    )
    correct = f"{metal.capitalize()} is a chemically unreactive (noble) metal that does not readily bond with atmospheric oxygen or water under normal temperatures."
    options = [
        correct,
        f"{metal.capitalize()} constantly evaporates a thick layer of carbon dioxide oil over itself.",
        f"{metal.capitalize()} turns atmospheric oxygen into nitrogen gas upon contact.",
        f"{metal.capitalize()} forms loose flaky red rust that blows away invisibly each night.",
    ]
    rng.shuffle(options)
    sol = (
        f"**Step 1:** **{metal.capitalize()}** sits at the bottom of the metal reactivity series.\n"
        "**Step 2:** Because it resists oxidation by oxygen and water completely, it retains its metallic lustre indefinitely without corroding [2]."
    )
    return _q(
        rng, "39", "39_noble_unreactive_metals_gold_platinum_jewelry", prompt, correct, sol, 2, "multiple_choice",
        ["noble_metals_oxidise_myth"],
        "Consider where gold and platinum sit on the metal reactivity series.",
        "Noble metals are unreactive toward oxygen and water.",
        correct, options=options,
    )


def arch_40_calculating_oxygen_mass_consumed_in_metal_oxidation(rng: random.Random) -> Dict[str, Any]:
    m_cu = rng.choice([6.4, 9.6, 12.8, 16.0])
    # Cu (63.5 ~ 64) + O (16) -> CuO: ratio 4 : 1 mass
    m_ox_add = round(m_cu / 4.0, 2)
    m_total = round(m_cu + m_ox_add, 2)
    pct_o = round((m_ox_add / m_total) * 100.0, 1)
    cu_s = f"{m_cu:.2f}".replace(".", ",")
    tot_s = f"{m_total:.2f}".replace(".", ",")
    ox_s = f"{m_ox_add:.2f}".replace(".", ",")
    pct_s = f"{pct_o:.1f}".replace(".", ",")
    prompt = (
        f"A cleaned coil of copper wire of mass **{cu_s} g** is heated strongly in oxygen until fully oxidised into black copper(II) oxide of final mass **{tot_s} g**.\n\n"
        "1. Calculate the exact mass of oxygen gas consumed [1].\n"
        "2. Calculate the percentage by mass of oxygen inside the final $\\text{CuO}$ sample (round to 1 decimal place) [2]."
    )
    correct = f"Oxygen mass = {ox_s} g; Percentage oxygen by mass = {pct_s}%"
    sol = (
        f"**Step 1:** By conservation of mass: $m(\\text{{O}}) = {tot_s}\\text{{ g}} - {cu_s}\\text{{ g}} = {ox_s}\\text{{ g}}$ [1].\n\n"
        f"**Step 2:** Percentage of oxygen $= \\frac{{{ox_s}}}{{{tot_s}}} \\times 100\\% = {pct_s}\\%$ [2]."
    )
    return _q(
        rng, "40", "40_calculating_oxygen_mass_consumed_in_metal_oxidation", prompt, correct, sol, 3, "calculation",
        ["oxide_percentage_mass_calculation_error"],
        "Mass of O = total oxide mass minus initial metal mass.",
        f"Divide oxygen mass ({ox_s} g) by total compound mass ({tot_s} g) times 100%.",
        correct,
    )


def arch_41_particle_model_iron_rusting_conservation_of_atoms(rng: random.Random) -> Dict[str, Any]:
    fe_c = rng.choice(["#64748b", "#475569", "#334155"])
    o_c = rng.choice(["#dc2626", "#e11d48", "#ef4444"])
    svg = (
        f'<svg viewBox="0 0 380 150" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="380" height="150" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="190" y="18" font-family="sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Submicroscopic Model: 4Fe + 3O2 -> 2Fe2O3</text>'
        f'<rect x="14" y="30" width="150" height="92" rx="6" fill="#fff" stroke="#94a3b8"/>'
        f'<text x="89" y="43" font-size="8" font-weight="bold" fill="#334155" text-anchor="middle">Reactants (4 Fe, 3 O2)</text>'
        f'<circle cx="38" cy="66" r="10" fill="{fe_c}"/><circle cx="38" cy="96" r="10" fill="{fe_c}"/>'
        f'<circle cx="64" cy="66" r="10" fill="{fe_c}"/><circle cx="64" cy="96" r="10" fill="{fe_c}"/>'
        f'<text x="51" y="116" font-size="7" fill="#475569" text-anchor="middle">4 Fe</text>'
        f'<circle cx="106" cy="60" r="8" fill="{o_c}"/><circle cx="122" cy="60" r="8" fill="{o_c}"/>'
        f'<circle cx="106" cy="82" r="8" fill="{o_c}"/><circle cx="122" cy="82" r="8" fill="{o_c}"/>'
        f'<circle cx="106" cy="104" r="8" fill="{o_c}"/><circle cx="122" cy="104" r="8" fill="{o_c}"/>'
        f'<text x="114" y="118" font-size="7" fill="#b91c1c" text-anchor="middle">3 O2</text>'
        f'<path d="M 173,76 L 203,76 M 198,71 L 205,76 L 198,81" fill="none" stroke="#0284c7" stroke-width="2.5"/>'
        f'<rect x="214" y="30" width="152" height="92" rx="6" fill="#fff" stroke="#94a3b8"/>'
        f'<text x="290" y="43" font-size="8" font-weight="bold" fill="#334155" text-anchor="middle">Products (2 Fe2O3)</text>'
        f'<circle cx="242" cy="68" r="10" fill="{fe_c}"/><circle cx="262" cy="68" r="10" fill="{fe_c}"/>'
        f'<circle cx="235" cy="54" r="7" fill="{o_c}"/><circle cx="252" cy="54" r="7" fill="{o_c}"/><circle cx="269" cy="54" r="7" fill="{o_c}"/>'
        f'<circle cx="242" cy="104" r="10" fill="{fe_c}"/><circle cx="262" cy="104" r="10" fill="{fe_c}"/>'
        f'<circle cx="235" cy="90" r="7" fill="{o_c}"/><circle cx="252" cy="90" r="7" fill="{o_c}"/><circle cx="269" cy="90" r="7" fill="{o_c}"/>'
        f'<text x="322" y="84" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">2 units</text>'
        f'<text x="190" y="140" font-size="8" fill="#475569" text-anchor="middle">Conserved count: 4 Fe atoms &amp; 6 O atoms on both sides</text>'
        f'</svg>'
    )
    prompt = (
        "Inspect the particle model diagram of iron reacting with oxygen gas.\n\n"
        "1. Count the exact number of grey **Fe atoms** and red **O atoms** in the Products box [2].\n"
        "2. Verify how this model confirms the Law of Conservation of Atoms [1]."
    )
    correct = "4 Fe atoms and 6 O atoms in Products (two Fe2O3 clusters); Atom counts match Reactants exactly (4 Fe and 6 O before = 4 Fe and 6 O after), proving atoms only rearrange."
    sol = (
        "**Step 1:** Each $\\text{Fe}_2\\text{O}_3$ cluster holds 2 Fe + 3 O atoms; two clusters give **$2 \\times 2 = 4$ Fe** and **$2 \\times 3 = 6$ O** atoms [2].\n\n"
        "**Step 2:** Reactants also held 4 Fe + $3 \\times 2 = 6$ O atoms—proving no atoms were created or lost [1]."
    )
    return _q(
        rng, "41", "41_particle_model_iron_rusting_conservation_of_atoms", prompt, correct, sol, 3, "structured",
        ["atom_conservation_counting_error"],
        "Multiply 2 Fe2O3 by 2 Fe and 3 O per unit.",
        "Count spheres in both boxes: 4 Fe and 6 O on left = 4 Fe and 6 O on right.",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_42_steel_wool_surface_area_vs_solid_iron_bar(rng: random.Random) -> Dict[str, Any]:
    thick_obj = rng.choice(["heavy 10 mm solid iron rod", "cast-iron paperweight", "solid railway spike"])
    prompt = (
        f"A learner holds both a **{thick_obj}** and a loose ball of **fine steel wool** of identical mass **5,0 g** into two identical Bunsen flames.\n\n"
        "Predict which sample bursts into bright sparks rapidly, and explain chemically at the particle collision level [2]."
    )
    correct = f"The steel wool bursts into rapid bright sparks while the {thick_obj} barely glows superficially; Fine wool threads expose massively greater surface area for oxygen molecules to collide with iron atoms simultaneously."
    sol = (
        f"**Step 1:** The **steel wool** combusts vigorously with bright sparks, whereas the {thick_obj} reacts only slightly on its outer skin [1].\n\n"
        "**Step 2:** Thin woven steel threads give an enormous **surface area-to-volume ratio**, allowing far more $O_2$ collisions per second and trapping radiant heat efficiently [1]."
    )
    return _q(
        rng, "42", "42_steel_wool_surface_area_vs_solid_iron_bar", prompt, correct, sol, 2, "short_answer",
        ["surface_area_collision_rate_confusion"],
        "Both weigh 5,0 g — what physical geometry differs between fine threads and one solid bar?",
        "Surface area exposed to O2 gas determines collision frequency.",
        correct,
    )


def arch_43_diatomic_oxygen_o2_reactant_structure(rng: random.Random) -> Dict[str, Any]:
    bad_eq, metal = rng.choice([
        ("Mg + O -> MgO", "magnesium"),
        ("Ca + O -> CaO", "calcium"),
        ("Cu + O -> CuO", "copper"),
    ])
    prompt = (
        f"A student writes the chemical equation `$\\text{{{bad_eq}}}$` for **{metal}** burning in air.\n\n"
        "Identify the chemical formula error in the reactants and rewrite the balanced equation accurately [2]."
    )
    fixed = bad_eq.replace("+ O ->", "+ O2 ->").replace(f"{bad_eq.split()[0]} ", f"2{bad_eq.split()[0]} ", 1).replace("-> ", "-> 2")
    correct = f"Atmospheric oxygen exists naturally as diatomic O2 molecules rather than lone O atoms; Corrected equation: {fixed}"
    sol = (
        "**Step 1:** Error: pure oxygen gas occurs in nature as **diatomic molecules ($\\text{O}_2$)**—never stable lone O atoms [1].\n\n"
        f"**Step 2:** Using $\\text{{O}}_2$ and balancing gives **$$\\text{{{fixed}}}$$** [1]."
    )
    return _q(
        rng, "43", "43_diatomic_oxygen_o2_reactant_structure", prompt, correct, sol, 2, "short_answer",
        ["monatomic_oxygen_o_equation_error"],
        "How does elemental oxygen gas always exist in air?",
        "Oxygen is one of the 7 diatomic elements: O2 -> balance with coefficients of 2.",
        correct,
    )


def arch_44_identifying_insoluble_vs_soluble_metal_oxides_in_water(rng: random.Random) -> Dict[str, Any]:
    ox_choice, status, behaviour = rng.choice([
        ("Sodium oxide (Na2O)", "readily soluble", "reacts vigorously to produce alkaline sodium hydroxide solution (pH ~ 13)"),
        ("Copper(II) oxide (CuO)", "practically insoluble", "settles at the bottom as black powder and leaves neutral water unchanged"),
        ("Iron(III) oxide (Fe2O3)", "practically insoluble", "remains suspended or settles as reddish rust sediment without dissolving noticeably"),
    ])
    prompt = (
        f"Even though metal oxides are classified as basic compounds, a teacher stirs powdered **{ox_choice}** into distilled water.\n\n"
        f"State whether **{ox_choice}** dissolves noticeably or settles out, and predict the effect on pure water's colour/pH [2]."
    )
    correct = f"{ox_choice} is {status} in water and {behaviour}."
    sol = f"**Step 1 & 2:** **{ox_choice}** is **{status}**; consequently it {behaviour} [2]."
    return _q(
        rng, "44", "44_identifying_insoluble_vs_soluble_metal_oxides_in_water", prompt, correct, sol, 2, "short_answer",
        ["all_bases_soluble_alkali_myth"],
        "Remember: all metal oxides are bases, but only some bases (alkalis like Group 1 oxides/hydroxides) dissolve well in water.",
        f"{ox_choice} is {status}: {behaviour}.",
        correct,
    )


def arch_45_translating_word_equations_to_picture_and_symbol_equations(rng: random.Random) -> Dict[str, Any]:
    metal, sym, ox, form, bal = rng.choice([
        ("Zinc", "Zn", "Zinc oxide", "ZnO", "2Zn + O2 -> 2ZnO"),
        ("Magnesium", "Mg", "Magnesium oxide", "MgO", "2Mg + O2 -> 2MgO"),
        ("Iron", "Fe", "Iron(III) oxide", "Fe2O3", "4Fe + 3O2 -> 2Fe2O3"),
    ])
    prompt = (
        f"Translate the reaction involving **{metal}** across three science formats:\n"
        f"1. **Word equation** [1]\n"
        f"2. **Balanced symbolic chemical equation** [2]\n"
        f"3. **Particle count balance check** (state atom totals per element on left and right) [1]"
    )
    if metal == "Iron":
        cnt = "Left: 4 Fe, 6 O; Right: 4 Fe, 6 O"
    else:
        cnt = f"Left: 2 {sym}, 2 O; Right: 2 {sym}, 2 O"
    correct = f"Word: {metal} + Oxygen -> {ox}; Symbol: {bal}; Particle check: {cnt}"
    sol = (
        f"**Step 1:** Word equation: **{metal} + Oxygen $\\rightarrow$ {ox}** [1].\n\n"
        f"**Step 2:** Symbol equation: **$$\\text{{{bal}}}$$** [2].\n\n"
        f"**Step 3:** Particle balance: **{cnt}** (equal numbers conserved) [1]."
    )
    return _q(
        rng, "45", "45_translating_word_equations_to_picture_and_symbol_equations", prompt, correct, sol, 4, "structured",
        ["word_to_symbol_translation_error"],
        "Move sequentially: element names -> true compound formulas -> balance atoms cleanly.",
        f"{bal} satisfies {cnt}.",
        correct,
    )


def arch_46_diagnosing_rust_experiment_variable_identification(rng: random.Random) -> Dict[str, Any]:
    test_type = rng.choice([
        ("comparing rusting mass across plain water, 1% salt, 3% salt, and 5% salt solutions",
         "Salt concentration (%)", "Extent/mass of rust formed on each iron nail", "Identical iron nail size, water volume, temperature, and 14-day exposure time"),
        ("comparing uncoated iron nails, painted nails, oiled nails, and galvanised nails submerged in wet air",
         "Surface protection method applied to the iron nail", "Presence or mass of rust developed after two weeks", "Identical nail mass/alloy, vessel temperature, moisture level, and time period"),
    ])
    setup_desc, ind, dep, ctrl = test_type
    prompt = (
        f"A Grade 9 learner designs a fair test investigation **{setup_desc}**.\n\n"
        "Identify:\n"
        "1. The **independent variable** [1]\n"
        "2. The **dependent variable** [1]\n"
        "3. **Two controlled (constant) variables** essential for validity [2]"
    )
    correct = f"Independent: {ind}; Dependent: {dep}; Controlled: {ctrl}"
    sol = (
        f"**Step 1:** **Independent variable** (deliberately varied by investigator): **{ind}** [1].\n\n"
        f"**Step 2:** **Dependent variable** (measured outcome): **{dep}** [1].\n\n"
        f"**Step 3:** **Controlled variables** (held identical): **{ctrl}** [2]."
    )
    return _q(
        rng, "46", "46_diagnosing_rust_experiment_variable_identification", prompt, correct, sol, 4, "structured",
        ["scientific_method_variable_confusion"],
        "Ask: What did the learner deliberately change? What is measured at the end? What must stay identical?",
        f"Independent = {ind}; Dependent = {dep}.",
        correct,
    )


def arch_47_bar_graph_interpretation_corrosion_rate_environments(rng: random.Random) -> Dict[str, Any]:
    dry_mg = rng.choice([1, 2, 3])
    fresh_mg = rng.choice([24, 28, 32])
    coast_mg = rng.choice([68, 76, 84])
    galv_mg = rng.choice([2, 4, 5])
    bars = [
        ("Dry Inland", dry_mg, "#94a3b8"),
        ("Freshwater", fresh_mg, "#38bdf8"),
        ("Coastal Brine", coast_mg, "#dc2626"),
        ("Galv Coastal", galv_mg, "#16a34a"),
    ]
    bar_svg = ""
    for i, (label, val, col) in enumerate(bars):
        h = max(4, int((val / 90.0) * 84))
        x = 52 + i * 78
        y = 122 - h
        bar_svg += (
            f'<rect x="{x}" y="{y}" width="38" height="{h}" fill="{col}" rx="2"/>'
            f'<text x="{x+19}" y="{y-4}" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">{val}</text>'
            f'<text x="{x+19}" y="135" font-size="7.5" fill="#334155" text-anchor="middle">{label}</text>'
        )
    svg = (
        f'<svg viewBox="0 0 380 155" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="380" height="155" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>'
        f'<text x="190" y="18" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Iron Rust Mass Formed After 30 Days (mg)</text>'
        f'<line x1="40" y1="30" x2="40" y2="122" stroke="#475569" stroke-width="1.5"/>'
        f'<line x1="40" y1="122" x2="360" y2="122" stroke="#475569" stroke-width="1.5"/>'
        f'<text x="20" y="80" font-size="8" fill="#475569" transform="rotate(-90 20 80)" text-anchor="middle">Rust (mg)</text>'
        f'{bar_svg}'
        f'</svg>'
    )
    ratio = round(coast_mg / galv_mg, 1)
    ratio_s = str(ratio).replace(".", ",")
    prompt = (
        "Inspect the bar graph measuring rust mass formed on standard steel plates after 30 days across four conditions.\n\n"
        "1. Which condition produced the **highest rust mass** and by how many mg compared to Freshwater? [2]\n"
        f"2. Calculate how many times greater rusting on bare Coastal Brine steel ({coast_mg} mg) was than Galvanised Coastal steel ({galv_mg} mg) [2]."
    )
    diff = coast_mg - fresh_mg
    correct = f"Highest: Coastal Brine ({coast_mg} mg), which is {diff} mg higher than Freshwater ({fresh_mg} mg); {ratio_s} times greater rusting than Galvanised Coastal steel."
    sol = (
        f"**Step 1:** **Coastal Brine** shows **{coast_mg} mg**, exceeding Freshwater ({fresh_mg} mg) by ${coast_mg} - {fresh_mg} = {diff}\\text{{ mg}}$ [2].\n\n"
        f"**Step 2:** Ratio $= \\frac{{{coast_mg}}}{{{galv_mg}}} = {ratio_s}\\times$ more corrosion without zinc galvanising [2]."
    )
    return _q(
        rng, "47", "47_bar_graph_interpretation_corrosion_rate_environments", prompt, correct, sol, 4, "calculation",
        ["graph_bar_comparison_arithmetic_error"],
        "Read exact numerical heights directly above each bar.",
        f"Subtract {fresh_mg} from {coast_mg}, and divide {coast_mg} by {galv_mg}.",
        correct, diagram_spec={"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
    )


def arch_48_stainless_vs_galvanised_economic_lifecycle_tradeoff(rng: random.Random) -> Dict[str, Any]:
    struct = rng.choice(["massive low-cost agricultural shed roof", "submerged municipal brine valve"])
    prompt = (
        f"An engineer must select a metal for a **{struct}** balancing upfront cost against rust durability.\n\n"
        "Contrast **galvanised mild steel** vs **solid stainless steel** on cost and long-term sacrificial vs alloy protection [3]."
    )
    correct = "Galvanised steel is far cheaper per square metre for large roofs and uses barrier + sacrificial zinc until zinc wears away; Solid stainless steel is much costlier upfront but protects internally forever via chromium alloy."
    sol = (
        "**Step 1:** **Galvanised steel** coats inexpensive steel with sacrificial zinc—cost-effective for massive roofs/fences, though zinc slowly consumes itself over decades [1].\n\n"
        "**Step 2:** **Stainless steel** alloys chromium/nickel throughout—far higher initial cost, ideal for high-corrosion marine/chemical valves needing lifetime maintenance-free durability [2]."
    )
    return _q(
        rng, "48", "48_stainless_vs_galvanised_economic_lifecycle_tradeoff", prompt, correct, sol, 3, "structured",
        ["engineering_material_tradeoff_confusion"],
        "Consider both material price and how long each protection mechanism lasts.",
        "Galvanised = economical external sacrificial coat; Stainless = costly bulk internal alloy.",
        correct,
    )


def arch_49_thermodynamic_exothermic_heat_release_combustion(rng: random.Random) -> Dict[str, Any]:
    fuel_metal = rng.choice(["magnesium ribbon", "fine iron steel wool", "powdered aluminium in fireworks"])
    prompt = (
        f"During rapid oxidation (combustion) of **{fuel_metal}** in oxygen, chemical potential energy stored in reactants converts noticeably into thermal and radiant energy.\n\n"
        "1. State the formal term for a chemical reaction that releases thermal energy to its surroundings [1].\n"
        "2. Define **combustion** accurately in terms of oxygen and heat [1]."
    )
    correct = "Exothermic reaction; Combustion is a rapid chemical reaction between a fuel/substance and oxygen that releases significant heat and often light/flame."
    sol = (
        "**Step 1:** A reaction releasing thermal energy outward into the surroundings is **exothermic** [1].\n\n"
        "**Step 2:** **Combustion** is rapid oxidation (reaction with oxygen) producing heat and commonly light [1]."
    )
    return _q(
        rng, "49", "49_thermodynamic_exothermic_heat_release_combustion", prompt, correct, sol, 2, "short_answer",
        ["combustion_definition_error"],
        "Think about the word prefix 'exo-' (outward) + thermal energy.",
        "Exothermic = heat exits; Combustion = rapid reaction with oxygen releasing heat/light.",
        correct,
    )


def arch_50_comprehensive_metal_oxidation_synthesis_problem(rng: random.Random) -> Dict[str, Any]:
    metal_set = rng.choice([
        ("Magnesium", "2Mg + O2 -> 2MgO", "white MgO powder, alkaline pH ~ 10 in water", "Copper", "2Cu + O2 -> 2CuO", "black solid surface film CuO"),
        ("Iron", "4Fe + 3O2 -> 2Fe2O3", "red-orange rust flakes needing air + moisture", "Magnesium", "2Mg + O2 -> 2MgO", "white ash turning litmus blue"),
    ])
    m1, eq1, obs1, m2, eq2, obs2 = metal_set
    prompt = (
        f"In a practical assessment comparing **{m1}** and **{m2}** reacting with oxygen:\n\n"
        f"1. Write balanced chemical equations for **{m1}** [2] and **{m2}** [2].\n"
        "2. Compare the nature of their products and explain how iron-based steel roofs near the ocean are permanently protected [2]."
    )
    correct = f"{m1}: {eq1} ({obs1}); {m2}: {eq2} ({obs2}); Coastal steel roofs are galvanised with zinc (barrier + sacrificial protection) or replaced with aluminium/stainless."
    sol = (
        f"**Step 1:** **{m1}**: **$$\\text{{{eq1}}}$$** ({obs1}) [2].\n\n"
        f"**Step 2:** **{m2}**: **$$\\text{{{eq2}}}$$** ({obs2}) [2].\n\n"
        "**Step 3:** Metal oxides are basic compounds; coastal steel structures rely on **zinc galvanising** (sacrificial protection even when scratched) or self-passivating **aluminium** alternatives [2]."
    )
    return _q(
        rng, "50", "50_comprehensive_metal_oxidation_synthesis_problem", prompt, correct, sol, 6, "structured",
        ["metal_oxidation_synthesis_error"],
        "Write balanced equations carefully using diatomic O2 and exact oxide formulas.",
        f"{eq1}; {eq2}; zinc galvanising protects even when scratched.",
        correct,
    )


BUILDERS_26_50: Dict[str, Any] = {
    "26_rust_mechanical_failure_structural_loss": arch_26_rust_mechanical_failure_structural_loss,
    "27_wood_and_aluminium_alternative_materials_coastal_homes": arch_27_wood_and_aluminium_alternative_materials_coastal_homes,
    "28_aluminium_self_passivating_oxide_layer_advantage": arch_28_aluminium_self_passivating_oxide_layer_advantage,
    "29_barrier_protection_painting_and_enamelling": arch_29_barrier_protection_painting_and_enamelling,
    "30_barrier_protection_oiling_and_greasing": arch_30_barrier_protection_oiling_and_greasing,
    "31_galvanising_zinc_coating_mechanism": arch_31_galvanising_zinc_coating_mechanism,
    "32_sacrificial_protection_scratched_galvanised_iron": arch_32_sacrificial_protection_scratched_galvanised_iron,
    "33_electroplating_chromium_chrome_taps_and_bumpers": arch_33_electroplating_chromium_chrome_taps_and_bumpers,
    "34_stainless_steel_alloying_chromium_nickel": arch_34_stainless_steel_alloying_chromium_nickel,
    "35_plastic_and_powder_coating_metal_fences": arch_35_plastic_and_powder_coating_metal_fences,
    "36_identifying_rust_prevention_method_by_application": arch_36_identifying_rust_prevention_method_by_application,
    "37_calcium_and_sodium_combustion_flame_colors": arch_37_calcium_and_sodium_combustion_flame_colors,
    "38_reactivity_series_oxygen_order_experiment": arch_38_reactivity_series_oxygen_order_experiment,
    "39_noble_unreactive_metals_gold_platinum_jewelry": arch_39_noble_unreactive_metals_gold_platinum_jewelry,
    "40_calculating_oxygen_mass_consumed_in_metal_oxidation": arch_40_calculating_oxygen_mass_consumed_in_metal_oxidation,
    "41_particle_model_iron_rusting_conservation_of_atoms": arch_41_particle_model_iron_rusting_conservation_of_atoms,
    "42_steel_wool_surface_area_vs_solid_iron_bar": arch_42_steel_wool_surface_area_vs_solid_iron_bar,
    "43_diatomic_oxygen_o2_reactant_structure": arch_43_diatomic_oxygen_o2_reactant_structure,
    "44_identifying_insoluble_vs_soluble_metal_oxides_in_water": arch_44_identifying_insoluble_vs_soluble_metal_oxides_in_water,
    "45_translating_word_equations_to_picture_and_symbol_equations": arch_45_translating_word_equations_to_picture_and_symbol_equations,
    "46_diagnosing_rust_experiment_variable_identification": arch_46_diagnosing_rust_experiment_variable_identification,
    "47_bar_graph_interpretation_corrosion_rate_environments": arch_47_bar_graph_interpretation_corrosion_rate_environments,
    "48_stainless_vs_galvanised_economic_lifecycle_tradeoff": arch_48_stainless_vs_galvanised_economic_lifecycle_tradeoff,
    "49_thermodynamic_exothermic_heat_release_combustion": arch_49_thermodynamic_exothermic_heat_release_combustion,
    "50_comprehensive_metal_oxidation_synthesis_problem": arch_50_comprehensive_metal_oxidation_synthesis_problem,
}
