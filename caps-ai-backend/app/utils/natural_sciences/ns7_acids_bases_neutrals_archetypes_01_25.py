"""
Grade 7 Natural Sciences - Term 2: Acids, Bases and Neutral Substances (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/NaturalSciences_Gr7/Term 2/03. Acids bases and neutral substances.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Taste & Sensory Adaptation (01 - 04)
# ==============================================================================

def arch_01_tongue_taste_buds_and_papillae(rng: random.Random) -> Dict[str, Any]:
    structures = [
        ("papillae", "small raised bumps covering the upper surface of the tongue"),
        ("taste buds", "microscopic sensory organs located in the grooves around papillae"),
        ("chemoreceptors", "specialised sensory cells that detect dissolved chemical molecules"),
    ]
    name, role = rng.choice(structures)

    prompt = (
        f"The human tongue is the primary sensory organ for detecting flavours in foods and beverages.\n\n"
        f"1. Name the small raised bumps on the surface of the tongue that contain taste buds: **{name}**.\n"
        f"2. Explain why food molecules must first dissolve in saliva before we can experience any taste sensation."
    )
    sol = (
        f"**Step 1:** The raised bumps are called **{name}** ({role}) [1 Mark: Anatomy].\n\n"
        f"**Step 2:** Taste receptors are chemoreceptors that can only detect chemical molecules in liquid solution; saliva dissolves food particles so molecules can enter taste pores and stimulate receptor hairs [1 Mark: Physiology]."
    )
    return {
        "id": f"ns7_ab_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name}; food molecules must dissolve in saliva to enter taste pores and stimulate chemoreceptors",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "01_tongue_taste_buds_and_papillae",
        "misconception_tags": ["taste_bud_structure"],
        "hints": {
            "tier_1": "Taste buds sit in bumps called papillae.",
            "tier_2": "Chemicals must dissolve in saliva to reach receptor hairs.",
            "tier_3": f"{name}; must dissolve in saliva to stimulate receptors."
        }
    }


def arch_02_four_primary_tastes_identification(rng: random.Random) -> Dict[str, Any]:
    food_lists = [
        ("fresh lemon juice", "Sour", "Citric acid"),
        ("unsweetened black coffee or raw bitter gourd", "Bitter", "Alkaloids / quinine"),
        ("ripe honey or pure table sugar", "Sweet", "Fructose / sucrose carbohydrates"),
        ("coarse rock salt or potato crisps", "Salty", "Sodium chloride mineral ions"),
    ]
    f1, f2 = rng.sample(food_lists, 2)

    prompt = (
        f"Humans perceive five basic taste modalities.\n\n"
        f"Consider two food items:\n"
        f"- Item A: {f1[0]}\n"
        f"- Item B: {f2[0]}\n\n"
        f"1. Identify the primary taste sensation produced by Item A.\n"
        f"2. Identify the primary taste sensation produced by Item B.\n"
        f"3. Name the fifth basic taste modality (associated with savory meat broth or MSG)."
    )
    sol = (
        f"**Step 1:** Item A ({f1[0]}) tastes **{f1[1].lower()}** [1 Mark: Taste A].\n\n"
        f"**Step 2:** Item B ({f2[0]}) tastes **{f2[1].lower()}** [1 Mark: Taste B].\n\n"
        f"**Step 3:** The fifth basic taste is **umami** (savory / meaty taste) [1 Mark: Umami]."
    )
    return {
        "id": f"ns7_ab_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Item A: {f1[1]}; Item B: {f2[1]}; Umami (savory)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "02_four_primary_tastes_identification",
        "misconception_tags": ["five_primary_tastes"],
        "hints": {
            "tier_1": "Think of sweet, sour, salty, bitter, and umami.",
            "tier_2": f"{f1[0]} is {f1[1].lower()}; {f2[0]} is {f2[1].lower()}.",
            "tier_3": f"{f1[1]}; {f2[1]}; Umami."
        }
    }


def arch_03_evolutionary_survival_taste_sour_bitter(rng: random.Random) -> Dict[str, Any]:
    tastes = [
        ("Sour taste", "warns animals that fruit is unripe, or that food has gone sour/spoiled due to bacterial decomposition and acid buildup"),
        ("Bitter taste", "warns animals against ingesting toxic, poisonous plant chemicals and lethal alkaloids"),
    ]
    taste_name, survival_role = rng.choice(tastes)

    prompt = (
        f"From an evolutionary perspective, our sense of taste is a vital survival mechanism rather than merely for pleasure.\n\n"
        f"1. Explain how the sensation of **{taste_name}** helped our ancient ancestors survive.\n"
        f"2. Contrast this with the evolutionary purpose of the sweet taste sensation."
    )
    sol = (
        f"**Step 1:** {taste_name} {survival_role} [1 Mark: Warning function].\n\n"
        f"**Step 2:** Sweet taste attracts animals to calorie-dense, energy-rich carbohydrates (sugars) necessary to fuel bodily metabolism [1 Mark: Calorie signal]."
    )
    return {
        "id": f"ns7_ab_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{survival_role}; sweet signals energy-rich carbohydrates",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "03_evolutionary_survival_taste_sour_bitter",
        "misconception_tags": ["evolutionary_taste_adaptation"],
        "hints": {
            "tier_1": "What dangerous foods taste sour or bitter?",
            "tier_2": "Sour warns of spoilage/decay; bitter warns of poison; sweet provides energy.",
            "tier_3": f"{survival_role}; sweet indicates carbohydrates."
        }
    }


def arch_04_laboratory_safety_rule_no_tasting(rng: random.Random) -> Dict[str, Any]:
    chemicals = [
        ("colourless hydrochloric acid solution", "causes severe chemical burns to tongue, mouth lining, and esophagus"),
        ("clear sodium hydroxide (caustic soda) solution", "corrosive alkali that dissolves mouth tissues and skin lipids"),
        ("copper sulfate blue solution", "toxic heavy metal salt causing severe poisoning and organ failure"),
    ]
    sub, hazard = rng.choice(chemicals)

    prompt = (
        f"In school science laboratories, teachers strictly enforce the safety rule:\n"
        f"'**NEVER taste or sip any substance in the science laboratory!**'\n\n"
        f"1. State TWO reasons why a learner must never taste an unknown clear liquid (such as {sub}) to identify whether it is an acid or water.\n"
        f"2. Name TWO safe scientific tools or methods used instead to test whether an unknown liquid is acidic, basic, or neutral."
    )
    sol = (
        f"**Step 1:** Many laboratory acids and bases are extremely **toxic, poisonous, and corrosive** ({hazard}); tasting can cause permanent tissue destruction or fatal poisoning [1 Mark: Chemical hazard].\n\n"
        f"**Step 2:** Safe methods (any two): **litmus paper**, **universal indicator solution / pH strips**, or a **digital pH meter** [1 Mark: Scientific indicators]."
    )
    return {
        "id": f"ns7_ab_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Chemicals are toxic and corrosive causing severe burns; use litmus paper or pH indicator strips",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "04_laboratory_safety_rule_no_tasting",
        "misconception_tags": ["laboratory_safety_rules"],
        "hints": {
            "tier_1": "Laboratory chemicals can cause burns or poison you.",
            "tier_2": "Use litmus paper or pH strips instead of tasting.",
            "tier_3": "Corrosive and toxic; test safely with litmus paper or pH meter."
        }
    }


# ==============================================================================
# CLUSTER 2: Properties of Acids & Bases (05 - 14)
# ==============================================================================

def arch_05_acid_definition_and_sensory_properties(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Acids are an important class of chemical substances found in foods, living organisms, and industry.\n\n"
        f"1. What characteristic taste do edible acids produce on the tongue?\n"
        f"2. How does an acid typically feel on broken skin (such as a small cut on your finger)?\n"
        f"3. Name the chemical ion ($H^+$ or $OH^-$) released by acids in aqueous solution."
    )
    sol = (
        f"**Step 1:** Acids produce a **sour taste** [1 Mark: Taste].\n\n"
        f"**Step 2:** An acid feels **rough / non-soapy**, and causes a sharp **stinging or burning** sensation on broken skin [1 Mark: Feel].\n\n"
        f"**Step 3:** Acids release **hydrogen ions ($H^+$)** in water [1 Mark: Ion]."
    )
    return {
        "id": f"ns7_ab_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Sour; stinging / burning sensation; hydrogen ions (H+)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "05_acid_definition_and_sensory_properties",
        "misconception_tags": ["acid_sensory_properties"],
        "hints": {
            "tier_1": "Think of lemons and vinegar: how do they taste and feel on a cut?",
            "tier_2": "Sour taste; stings on cuts; releases H+ ions.",
            "tier_3": "Sour; sharp stinging sensation; H+."
        }
    }


def arch_06_everyday_household_acids_examples(rng: random.Random) -> Dict[str, Any]:
    acids = [
        ("Vinegar used in salad dressings", "Ethanoic acid (acetic acid)"),
        ("Fresh lemon juice or orange juice", "Citric acid"),
        ("Sour milk, amasi, or plain yoghurt", "Lactic acid"),
        ("Fizzy carbonated soft drinks", "Carbonic acid and phosphoric acid"),
        ("Vitamin C chewable tablets", "Ascorbic acid"),
        ("Grapes and cream of tartar", "Tartaric acid"),
    ]
    item, acid_type = rng.choice(acids)

    prompt = (
        f"Many common foods and household products contain weak, safe acids.\n\n"
        f"Consider: **{item}**.\n\n"
        f"1. Name the specific scientific acid present in this product: **{acid_type}**.\n"
        f"2. Explain why it is safe to ingest this household acid, whereas laboratory hydrochloric acid must never be consumed."
    )
    sol = (
        f"**Step 1:** The acid present is **{acid_type}** [1 Mark: Acid identification].\n\n"
        f"**Step 2:** Household food acids are **weak acids** in very dilute concentrations that our digestive system easily metabolises, whereas concentrated laboratory acids are **strong acids** that destroy mucous membranes and burn digestive tissue [1 Mark: Weak vs strong acids]."
    )
    return {
        "id": f"ns7_ab_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{acid_type}; food acids are weak/dilute whereas concentrated lab acids are corrosive",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "06_everyday_household_acids_examples",
        "misconception_tags": ["household_acids_weakness"],
        "hints": {
            "tier_1": "What acid is in lemons, vinegar, or milk?",
            "tier_2": f"This product contains {acid_type}.",
            "tier_3": f"{acid_type}; food acids are weak and safe to digest."
        }
    }


def arch_07_laboratory_acids_identification_formulas(rng: random.Random) -> Dict[str, Any]:
    lab_acids = [
        ("Hydrochloric acid", "HCl", "stomach gastric juice / pool acid / spirit of salts"),
        ("Sulfuric acid", "H2SO4", "lead-acid car batteries / industrial fertilizer manufacture"),
        ("Nitric acid", "HNO3", "explosives / industrial agricultural nitrates"),
    ]
    name, formula, use = rng.choice(lab_acids)

    prompt = (
        f"In school science laboratories and industrial chemistry, three mineral acids are standard reagents.\n\n"
        f"1. Name the acid: **{name}**.\n"
        f"2. State its chemical formula: **{formula}**.\n"
        f"3. Identify ONE major real-world or biological occurrence: {use}."
    )
    sol = (
        f"**Step 1:** Acid name: **{name}** [1 Mark: Name].\n\n"
        f"**Step 2:** Chemical formula: **${formula}$** [1 Mark: Formula].\n\n"
        f"**Step 3:** Occurrence/use: **{use.capitalize()}** [1 Mark: Occurrence]."
    )
    return {
        "id": f"ns7_ab_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name}; {formula}; {use}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "07_laboratory_acids_identification_formulas",
        "misconception_tags": ["laboratory_acid_formulas"],
        "hints": {
            "tier_1": "Common lab acids: HCl, H2SO4, HNO3.",
            "tier_2": f"{name} has formula {formula}.",
            "tier_3": f"{name}; {formula}; {use}."
        }
    }


def arch_08_corrosive_nature_of_strong_acids(rng: random.Random) -> Dict[str, Any]:
    materials = [
        ("zinc metal granule dropped in concentrated hydrochloric acid", "vigorous bubbling and effervescence as the metal dissolves to release hydrogen gas"),
        ("drop of concentrated sulfuric acid spilled on a cotton lab coat", "causes black dehydration charring and eats a hole right through the fabric"),
        ("acid spilled on skin", "causes severe chemical burns and tissue destruction"),
    ]
    scenario, effect = rng.choice(materials)

    prompt = (
        f"Concentrated mineral acids carry a yellow hazard symbol warning of high **corrosiveness**.\n"
        f"Consider: '{scenario}'.\n\n"
        f"1. Define the term **corrosive** in the context of acids.\n"
        f"2. Describe the destructive effect observed: {effect}.\n"
        f"3. State TWO vital safety gear items a learner must wear when handling concentrated acids."
    )
    sol = (
        f"**Step 1:** Corrosive means capable of eating away, dissolving, or destroying solid materials (metals, stone, living tissue) through chemical reactions [1 Mark: Definition].\n\n"
        f"**Step 2:** Effect: {effect.capitalize()} [1 Mark: Observation].\n\n"
        f"**Step 3:** Safety gear (any two): **safety goggles / eye protection**, **rubber lab gloves**, or a **protective lab coat** [1 Mark: PPE]."
    )
    return {
        "id": f"ns7_ab_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Eats away and destroys materials chemically; {effect}; safety goggles, gloves, lab coat",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "08_corrosive_nature_of_strong_acids",
        "misconception_tags": ["corrosive_meaning"],
        "hints": {
            "tier_1": "Corrosive means it eats through materials.",
            "tier_2": "Always wear safety goggles and gloves.",
            "tier_3": f"Eats away materials; {effect}; goggles and gloves."
        }
    }


def arch_09_base_definition_and_sensory_properties(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Bases are another fundamental class of chemical compounds, chemically opposite to acids.\n\n"
        f"1. What characteristic taste do edible or mild bases produce on the tongue?\n"
        f"2. How does a dilute base (such as soapy water) feel when rubbed between the fingertips?\n"
        f"3. Explain why bases feel slippery on human skin."
    )
    sol = (
        f"**Step 1:** Bases have a **bitter taste** [1 Mark: Taste].\n\n"
        f"**Step 2:** Bases feel **slippery / soapy** between the fingers [1 Mark: Feel].\n\n"
        f"**Step 3:** The alkaline solution reacts with the natural oils and fatty acids on skin in a mild saponification reaction, producing a microscopic film of soap [1 Mark: Saponification]."
    )
    return {
        "id": f"ns7_ab_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Bitter; slippery / soapy; reacts with skin oils to form a thin film of soap",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "09_base_definition_and_sensory_properties",
        "misconception_tags": ["base_sensory_properties"],
        "hints": {
            "tier_1": "How does soap taste (bitter) and feel (slippery)?",
            "tier_2": "Bitter taste; slippery feel; reacts with oils on skin.",
            "tier_3": "Bitter; slippery; saponifies skin oils."
        }
    }


def arch_10_alkali_definition_soluble_bases(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In chemistry, teachers often say: '**All alkalis are bases, but not all bases are alkalis.**'\n\n"
        f"1. Define the specific term **alkali**.\n"
        f"2. Give ONE example of a soluble base (alkali).\n"
        f"3. Give ONE example of an insoluble base (a base that does not dissolve in water)."
    )
    sol = (
        f"**Step 1:** An alkali is a base that is **soluble in water** [1 Mark: Definition].\n\n"
        f"**Step 2:** Soluble base (alkali): **sodium hydroxide ($NaOH$)**, potassium hydroxide ($KOH$), or calcium hydroxide ($Ca(OH)_2$ in limewater) [1 Mark: Soluble example].\n\n"
        f"**Step 3:** Insoluble base: **copper(II) oxide ($CuO$)**, iron(III) oxide, or magnesium oxide ($MgO$) [1 Mark: Insoluble example]."
    )
    return {
        "id": f"ns7_ab_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "An alkali is a base that dissolves in water; Soluble: NaOH; Insoluble: copper oxide / magnesium oxide",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "10_alkali_definition_soluble_bases",
        "misconception_tags": ["base_vs_alkali_distinction"],
        "hints": {
            "tier_1": "An alkali is simply a water-soluble base.",
            "tier_2": "Sodium hydroxide dissolves (alkali); copper oxide does not dissolve (base only).",
            "tier_3": "Base soluble in water; NaOH is alkali; copper oxide is insoluble base."
        }
    }


def arch_11_everyday_household_bases_examples(rng: random.Random) -> Dict[str, Any]:
    household_bases = [
        ("Baking soda (sodium bicarbonate)", "baking powder, deodorizing fridges, mild antacid"),
        ("Toothpaste", "cleaning teeth and neutralising plaque acids"),
        ("Handy Andy / ammonia cleaning solution", "cutting through kitchen grease and cleaning windows"),
        ("Bar soap or washing powder", "laundering clothes and cleaning greasy hands"),
        ("Milk of Magnesia (magnesium hydroxide)", "antacid suspension to soothe stomach acid"),
    ]
    base_name, uses = rng.choice(household_bases)

    prompt = (
        f"Many common household cleaning and personal care products are basic.\n\n"
        f"Consider: **{base_name}**.\n\n"
        f"1. State whether this substance is an acid, a base, or neutral.\n"
        f"2. Explain why alkaline properties make this product ideal for {uses}."
    )
    sol = (
        f"**Step 1:** It is a **base** (alkaline substance) [1 Mark: Classification].\n\n"
        f"**Step 2:** Bases chemically break down and emulsify insoluble fatty grease, or neutralise harmful acidic residues [1 Mark: Cleaning action]."
    )
    return {
        "id": f"ns7_ab_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Base; breaks down greasy fats and oils or neutralises acids",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "11_everyday_household_bases_examples",
        "misconception_tags": ["household_bases_function"],
        "hints": {
            "tier_1": "Cleaning products and antacids are bases.",
            "tier_2": "Bases dissolve grease and neutralise acids.",
            "tier_3": "Base; dissolves fatty grease and neutralises acid."
        }
    }


def arch_12_laboratory_bases_identification_formulas(rng: random.Random) -> Dict[str, Any]:
    bases = [
        ("Sodium hydroxide", "NaOH", "caustic soda / drain cleaner"),
        ("Calcium hydroxide", "Ca(OH)2", "slaked lime / clear limewater for CO2 test"),
        ("Potassium hydroxide", "KOH", "caustic potash / alkaline battery electrolyte"),
        ("Ammonium hydroxide", "NH4OH", "household cloudy ammonia cleaner"),
    ]
    name, formula, use = rng.choice(bases)

    prompt = (
        f"In school science laboratories, several common alkalis are studied.\n\n"
        f"1. Name the alkali: **{name}**.\n"
        f"2. State its chemical formula: **{formula}**.\n"
        f"3. Name the common real-world application: {use}."
    )
    sol = (
        f"**Step 1:** Name: **{name}** [1 Mark: Name].\n\n"
        f"**Step 2:** Chemical formula: **${formula}$** [1 Mark: Formula].\n\n"
        f"**Step 3:** Application: **{use.capitalize()}** [1 Mark: Application]."
    )
    return {
        "id": f"ns7_ab_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{name}; {formula}; {use}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "12_laboratory_bases_identification_formulas",
        "misconception_tags": ["laboratory_base_formulas"],
        "hints": {
            "tier_1": "Alkalis contain hydroxide groups (OH).",
            "tier_2": f"{name} is {formula}.",
            "tier_3": f"{name}; {formula}; {use}."
        }
    }


def arch_13_caustic_nature_of_strong_bases(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Strong bases like sodium hydroxide are described as **caustic** rather than merely corrosive.\n\n"
        f"1. Explain what the word **caustic** means.\n"
        f"2. Commercial drain cleaners contain concentrated sodium hydroxide. Explain why this chemical effectively unblocks clogged bathroom pipes containing hair and grease.\n"
        f"3. Explain why getting drain cleaner in your eyes is considered an extreme medical emergency."
    )
    sol = (
        f"**Step 1:** Caustic means able to burn, dissolve, or corrode organic matter (tissue, proteins, and fats) by chemical action [1 Mark: Definition].\n\n"
        f"**Step 2:** Sodium hydroxide dissolves hair keratin protein and reacts with fatty grease in the clog to form soluble soap that washes down the pipe [1 Mark: Mechanism].\n\n"
        f"**Step 3:** Strong bases penetrate corneal eye tissue very rapidly, destroying proteins and causing permanent blindness within seconds [1 Mark: Eye hazard]."
    )
    return {
        "id": f"ns7_ab_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Burns and dissolves organic matter; dissolves hair protein and turns grease into soap; rapidly penetrates eye tissue causing permanent blindness",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "13_caustic_nature_of_strong_bases",
        "misconception_tags": ["caustic_base_danger"],
        "hints": {
            "tier_1": "Caustic bases destroy proteins and fats.",
            "tier_2": "Drain cleaner dissolves hair and turns grease to soap; in eyes it causes blindness.",
            "tier_3": "Dissolves organic matter; unblocks drains by breaking down hair/fat; causes blindness in eyes."
        }
    }


def arch_14_neutral_substance_definition_properties(rng: random.Random) -> Dict[str, Any]:
    neutrals = [
        ("pure distilled water", "pH exactly 7,0"),
        ("table salt solution (sodium chloride dissolved in water)", "pH 7,0"),
        ("sugar solution (glucose dissolved in water)", "pH 7,0"),
        ("sunflower cooking oil", "pH approximately 7"),
    ]
    sub, ph_note = rng.choice(neutrals)

    prompt = (
        f"Consider the substance: **{sub}** ({ph_note}).\n\n"
        f"1. Explain what makes a substance **neutral** in terms of acids and bases.\n"
        f"2. State its exact pH value at $25^\\circ\\text{{C}}$.\n"
        f"3. What will happen to red litmus paper and blue litmus paper dipped into this substance?"
    )
    sol = (
        f"**Step 1:** A neutral substance is **neither an acid nor a base** (contains equal concentrations of $H^+$ and $OH^-$ ions) [1 Mark: Definition].\n\n"
        f"**Step 2:** Its pH value is exactly **7,0** [1 Mark: pH].\n\n"
        f"**Step 3:** **Neither litmus paper changes colour** (red litmus remains red, blue litmus remains blue) [1 Mark: Litmus response]."
    )
    return {
        "id": f"ns7_ab_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Neither acid nor base; pH = 7,0; red stays red, blue stays blue (no colour change)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "14_neutral_substance_definition_properties",
        "misconception_tags": ["neutral_litmus_behaviour"],
        "hints": {
            "tier_1": "Neutral substances are pH 7 and do not change litmus paper.",
            "tier_2": "Red stays red, blue stays blue.",
            "tier_3": "Neither acid nor base; pH 7; neither litmus changes colour."
        }
    }


# ==============================================================================
# CLUSTER 3: Litmus, Indicators & The pH Scale (15 - 25)
# ==============================================================================

def arch_15_red_litmus_paper_reaction_acid_base(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("soap solution", "Base", "Blue", "turns blue in a base"),
        ("vinegar", "Acid", "Red", "remains red in an acid"),
        ("distilled water", "Neutral", "Red", "remains red in a neutral substance"),
    ]
    sub, cat, color, rule = rng.choice(cases)

    prompt = (
        f"A strip of dry **red litmus paper** is dipped into an unknown liquid: **{sub}** ({cat}).\n\n"
        f"1. Predict the final colour of the red litmus paper ({color} or otherwise).\n"
        f"2. State the general rule for how red litmus paper responds in acids, bases, and neutral substances."
    )
    sol = (
        f"**Step 1:** The red litmus paper will be **{color.lower()}** ({rule}) [1 Mark: Prediction].\n\n"
        f"**Step 2:** Rule: Red litmus paper **turns blue in bases**, but **remains red in both acids and neutral substances** [1 Mark: Rule]."
    )
    return {
        "id": f"ns7_ab_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{color}; turns blue in bases, remains red in acids and neutral substances",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "15_red_litmus_paper_reaction_acid_base",
        "misconception_tags": ["red_litmus_rules"],
        "hints": {
            "tier_1": "Red litmus only turns blue in a base.",
            "tier_2": f"{sub} is a {cat}. So it will be {color}.",
            "tier_3": f"{color}; turns blue only in bases."
        }
    }


def arch_16_blue_litmus_paper_reaction_acid_base(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("lemon juice", "Acid", "Red", "turns red in an acid"),
        ("baking soda solution", "Base", "Blue", "remains blue in a base"),
        ("pure salt water", "Neutral", "Blue", "remains blue in a neutral substance"),
    ]
    sub, cat, color, rule = rng.choice(cases)

    prompt = (
        f"A strip of dry **blue litmus paper** is dipped into an unknown liquid: **{sub}** ({cat}).\n\n"
        f"1. Predict the final colour of the blue litmus paper ({color} or otherwise).\n"
        f"2. State the general rule for how blue litmus paper responds in acids, bases, and neutral substances."
    )
    sol = (
        f"**Step 1:** The blue litmus paper will be **{color.lower()}** ({rule}) [1 Mark: Prediction].\n\n"
        f"**Step 2:** Rule: Blue litmus paper **turns red in acids**, but **remains blue in both bases and neutral substances** [1 Mark: Rule]."
    )
    return {
        "id": f"ns7_ab_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{color}; turns red in acids, remains blue in bases and neutral substances",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "16_blue_litmus_paper_reaction_acid_base",
        "misconception_tags": ["blue_litmus_rules"],
        "hints": {
            "tier_1": "Blue litmus only turns red in an acid.",
            "tier_2": f"{sub} is a {cat}. So it will be {color}.",
            "tier_3": f"{color}; turns red only in acids."
        }
    }


def arch_17_two_litmus_test_identifying_neutral(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A student tests an unknown clear liquid using only red litmus paper. The red litmus paper remains red.\n\n"
        f"1. Can the student conclusively declare that the liquid is an acid? Explain why or why not.\n"
        f"2. Explain why BOTH red litmus paper and blue litmus paper must be used together to identify a neutral liquid with certainty."
    )
    sol = (
        f"**Step 1:** **No.** Red litmus stays red in both acids and neutral substances, so the liquid could be either an acid or neutral [1 Mark: Ambiguity].\n\n"
        f"**Step 2:** If blue litmus also remains blue while red litmus remains red, neither an acid nor a base is present, confirming conclusively that the substance is **neutral** [1 Mark: Dual litmus proof]."
    )
    return {
        "id": f"ns7_ab_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "No, could be acid or neutral; both needed because neutral leaves red as red AND blue as blue",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "17_two_litmus_test_identifying_neutral",
        "misconception_tags": ["single_litmus_insufficient_for_neutral"],
        "hints": {
            "tier_1": "Red litmus stays red in both acid and neutral.",
            "tier_2": "You must check blue litmus as well.",
            "tier_3": "No, could be acid or neutral; dual test needed."
        }
    }


def arch_18_interpreting_litmus_test_data_table(rng: random.Random) -> Dict[str, Any]:
    solutions = [
        {"name": "Solution P", "red": "Blue", "blue": "Blue", "class": "Base"},
        {"name": "Solution Q", "red": "Red", "blue": "Red", "class": "Acid"},
        {"name": "Solution R", "red": "Red", "blue": "Blue", "class": "Neutral"},
    ]
    rng.shuffle(solutions)

    tbl = (
        "| Solution | Red Litmus Result | Blue Litmus Result |\n"
        "| :--- | :---: | :---: |\n"
    )
    for s in solutions:
        tbl += f"| {s['name']} | {s['red']} | {s['blue']} |\n"

    p_sol = [s for s in solutions if s["class"] == "Base"][0]["name"]
    q_sol = [s for s in solutions if s["class"] == "Acid"][0]["name"]
    r_sol = [s for s in solutions if s["class"] == "Neutral"][0]["name"]

    prompt = (
        f"A learner records the following litmus test results for three unknown solutions:\n\n"
        f"{tbl}\n"
        f"Classify each solution as an **acid**, a **base**, or **neutral**:\n"
        f"1. {p_sol}\n"
        f"2. {q_sol}\n"
        f"3. {r_sol}"
    )
    sol = (
        f"**Step 1:** **{p_sol}** is a **base** (turns red litmus blue) [1 Mark].\n\n"
        f"**Step 2:** **{q_sol}** is an **acid** (turns blue litmus red) [1 Mark].\n\n"
        f"**Step 3:** **{r_sol}** is **neutral** (leaves red as red, blue as blue) [1 Mark]."
    )
    return {
        "id": f"ns7_ab_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{p_sol}: Base; {q_sol}: Acid; {r_sol}: Neutral",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "18_interpreting_litmus_test_data_table",
        "misconception_tags": ["litmus_table_interpretation"],
        "hints": {
            "tier_1": "Turns red to blue = base. Turns blue to red = acid. No change = neutral.",
            "tier_2": f"{p_sol} is Base, {q_sol} is Acid, {r_sol} is Neutral.",
            "tier_3": f"{p_sol}: Base; {q_sol}: Acid; {r_sol}: Neutral."
        }
    }


def arch_19_plant_indicator_red_cabbage_preparation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In schools without manufactured chemical indicators, teachers make a natural indicator using red cabbage.\n\n"
        f"1. Describe the laboratory procedure to extract the purple indicator juice from raw red cabbage leaves.\n"
        f"2. Name the class of biological pigment in red cabbage responsible for changing colour with pH changes (anthocyanins).\n"
        f"3. Why must the extracted cabbage water be cooled and strained before use?"
    )
    sol = (
        f"**Step 1:** Chop fresh red cabbage leaves finely, place in a beaker, cover with boiling water, and boil/steep for 10 minutes until deep purple [1 Mark: Extraction procedure].\n\n"
        f"**Step 2:** The plant pigments are **anthocyanins** [1 Mark: Pigment].\n\n"
        f"**Step 3:** Straining through a sieve removes solid leaf fragments so the clear liquid can clearly show colour changes [1 Mark: Filtration reason]."
    )
    return {
        "id": f"ns7_ab_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Boil chopped cabbage in water; anthocyanin pigment; removes solid leaf fragments to leave clear liquid",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "19_plant_indicator_red_cabbage_preparation",
        "misconception_tags": ["red_cabbage_indicator_preparation"],
        "hints": {
            "tier_1": "Chop and boil in water, then strain.",
            "tier_2": "The pigment is anthocyanin.",
            "tier_3": "Boil chopped cabbage; anthocyanins; strain solids to leave clear indicator."
        }
    }


def arch_20_red_cabbage_indicator_colour_changes(rng: random.Random) -> Dict[str, Any]:
    substances = [
        ("lemon juice (strong acid)", "Red / Pink", "#ec4899", "Acid"),
        ("pure water (neutral)", "Purple / Violet", "#8b5cf6", "Neutral"),
        ("baking soda solution (weak base)", "Blue / Green", "#10b981", "Base"),
        ("caustic drain cleaner (strong base)", "Yellow / Green", "#eab308", "Base"),
    ]
    sub, expected_col, col_code, category = rng.choice(substances)

    svg = (
        f'<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<rect x="150" y="20" width="60" height="120" fill="none" stroke="#334155" stroke-width="2" rx="30"/>'
        f'<path d="M 152,80 L 208,80 L 208,110 Q 180,140 152,110 Z" fill="{col_code}" opacity="0.8"/>'
        f'<text x="180" y="160" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{sub}</text>'
        f'<text x="180" y="105" font-family="sans-serif" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">{expected_col}</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": f"Red cabbage indicator test with {sub}",
        "diagram_role": "context"
    }

    prompt = (
        f"Red cabbage juice indicator exhibits a range of colours across the pH spectrum.\n\n"
        f"A student adds red cabbage juice to: **{sub}**.\n\n"
        f"1. Predict the colour change observed ({expected_col} or otherwise).\n"
        f"2. Summarise the general colour changes of red cabbage juice in acids, neutral substances, and bases."
    )
    sol = (
        f"**Step 1:** The mixture turns **{expected_col.lower()}** [1 Mark: Observation].\n\n"
        f"**Step 2:** Summary: Turns **red / pink in acids**, stays **purple in neutral**, and turns **green, blue, or yellow in bases** [1 Mark: General rule]."
    )
    return {
        "id": f"ns7_ab_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{expected_col}; Red/pink in acid, purple in neutral, green/blue/yellow in base",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "20_red_cabbage_indicator_colour_changes",
        "misconception_tags": ["red_cabbage_colour_scale"],
        "hints": {
            "tier_1": "Red/pink for acid, purple for neutral, green/yellow for base.",
            "tier_2": f"{sub} is a {category}, so it turns {expected_col.lower()}.",
            "tier_3": f"{expected_col}; Red/pink in acid, purple in neutral, green/blue/yellow in base."
        }
    }


def arch_21_alternative_natural_indicators_turmeric_tea(rng: random.Random) -> Dict[str, Any]:
    plants = [
        ("Turmeric powder (borrie)", "yellow in acid and neutral", "deep reddish-brown in base"),
        ("Black tea infusion", "bright pale golden yellow in acid (lemon)", "dark brown/black in base"),
        ("Beetroot juice", "bright red in acid and neutral", "yellowish-purple in strong base"),
    ]
    p_name, acid_col, base_col = rng.choice(plants)

    prompt = (
        f"Besides red cabbage, many household plant extracts function as natural pH indicators.\n\n"
        f"Consider: **{p_name}**.\n\n"
        f"1. Describe the colour of {p_name} in an acidic solution ({acid_col}).\n"
        f"2. Describe the colour of {p_name} when added to an alkaline base ({base_col}).\n"
        f"3. Explain why a yellow curry stain on a white shirt turns reddish-brown when washed with alkaline laundry soap."
    )
    sol = (
        f"**Step 1:** In acid: **{acid_col}** [1 Mark: Acid colour].\n\n"
        f"**Step 2:** In base: **{base_col}** [1 Mark: Base colour].\n\n"
        f"**Step 3:** Curry contains turmeric; when exposed to the alkaline pH of laundry soap, the curcumin pigment undergoes a chemical structure change turning reddish-brown [1 Mark: Real-world explanation]."
    )
    return {
        "id": f"ns7_ab_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Acid: {acid_col}; Base: {base_col}; Turmeric in curry reacts with alkaline soap turning reddish-brown",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "21_alternative_natural_indicators_turmeric_tea",
        "misconception_tags": ["turmeric_curry_indicator"],
        "hints": {
            "tier_1": "Soap is alkaline; turmeric turns reddish-brown in base.",
            "tier_2": f"Acid: {acid_col}; Base: {base_col}.",
            "tier_3": f"Acid: {acid_col}; Base: {base_col}; Alkaline soap changes turmeric color."
        }
    }


def arch_22_universal_indicator_concept_and_colours(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Unlike litmus paper which only tells whether a substance is acid, base, or neutral, **Universal Indicator** provides much more information.\n\n"
        f"1. Explain what Universal Indicator is made of (a mixture of several different indicators).\n"
        f"2. What additional quantitative measurement does Universal Indicator indicate that simple litmus cannot?\n"
        f"3. State the colour Universal Indicator displays in a neutral solution of pure water at pH 7."
    )
    sol = (
        f"**Step 1:** Universal indicator is a blend/mixture of several different dye indicators that change colour at different pH values [1 Mark: Composition].\n\n"
        f"**Step 2:** It shows the **relative strength (exact pH value on 0-14 scale)** of the acid or base [1 Mark: Quantitative pH].\n\n"
        f"**Step 3:** In a neutral solution (pH 7), Universal Indicator displays a **green** colour [1 Mark: Neutral colour]."
    )
    return {
        "id": f"ns7_ab_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Mixture of several indicators; shows exact strength / pH value; green at pH 7",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "subskill": "22_universal_indicator_concept_and_colours",
        "misconception_tags": ["universal_indicator_vs_litmus"],
        "hints": {
            "tier_1": "Universal indicator shows strength across the whole 0 to 14 spectrum.",
            "tier_2": "Neutral pH 7 is green.",
            "tier_3": "Blend of indicators; measures pH strength; green at pH 7."
        }
    }


def arch_23_ph_scale_range_and_neutral_point(rng: random.Random) -> Dict[str, Any]:
    test_ph = rng.choice([2, 5, 7, 9, 12])
    colors = {2: ("Red", "#ef4444", "Strong acid"), 5: ("Orange/Yellow", "#f59e0b", "Weak acid"), 7: ("Green", "#22c55e", "Neutral"), 9: ("Blue", "#3b82f6", "Weak base"), 12: ("Purple", "#8b5cf6", "Strong base")}
    c_name, c_hex, c_type = colors[test_ph]

    svg = (
        f'<svg viewBox="0 0 360 140" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">'
        f'<defs>'
        f'<linearGradient id="phGrad" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0%" stop-color="#ef4444"/>'
        f'<stop offset="35%" stop-color="#f59e0b"/>'
        f'<stop offset="50%" stop-color="#22c55e"/>'
        f'<stop offset="70%" stop-color="#3b82f6"/>'
        f'<stop offset="100%" stop-color="#8b5cf6"/>'
        f'</linearGradient>'
        f'</defs>'
        f'<rect x="20" y="30" width="320" height="30" fill="url(#phGrad)" rx="4"/>'
        f'<text x="25" y="80" font-family="sans-serif" font-size="10" font-weight="bold" fill="#ef4444">0</text>'
        f'<text x="180" y="80" font-family="sans-serif" font-size="10" font-weight="bold" fill="#22c55e" text-anchor="middle">7 (Neutral)</text>'
        f'<text x="335" y="80" font-family="sans-serif" font-size="10" font-weight="bold" fill="#8b5cf6" text-anchor="end">14</text>'
        f'<circle cx="{20 + int(test_ph * 320 / 14)}" cy="45" r="10" fill="#ffffff" stroke="{c_hex}" stroke-width="3"/>'
        f'<text x="{20 + int(test_ph * 320 / 14)}" y="115" font-family="sans-serif" font-size="11" font-weight="bold" fill="{c_hex}" text-anchor="middle">Sample pH {test_ph}</text>'
        f'</svg>'
    )
    diag = {
        "kind": "inline_svg",
        "svg": svg,
        "caption": f"The pH scale from 0 to 14 highlighting pH {test_ph}",
        "diagram_role": "context"
    }

    prompt = (
        f"The pH scale measures how acidic or basic a substance is.\n\n"
        f"A sample has a measured **pH of {test_ph}**.\n\n"
        f"1. State the numerical range of the entire pH scale.\n"
        f"2. Classify this sample as a **strong acid**, **weak acid**, **neutral**, **weak base**, or **strong base**.\n"
        f"3. What colour does Universal Indicator display at pH {test_ph}?"
    )
    sol = (
        f"**Step 1:** The pH scale ranges from **0 to 14** [1 Mark: Range].\n\n"
        f"**Step 2:** A pH of {test_ph} is classified as a **{c_type}** [1 Mark: Classification].\n\n"
        f"**Step 3:** Universal Indicator displays **{c_name}** at pH {test_ph} [1 Mark: Colour]."
    )
    return {
        "id": f"ns7_ab_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"0 to 14; {c_type}; {c_name}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 3,
        "term": 2,
        "diagram_spec": diag,
        "subskill": "23_ph_scale_range_and_neutral_point",
        "misconception_tags": ["ph_scale_interpretation"],
        "hints": {
            "tier_1": "Scale is 0 to 14. 7 is neutral.",
            "tier_2": f"pH {test_ph} is a {c_type}.",
            "tier_3": f"0 to 14; {c_type}; {c_name}."
        }
    }


def arch_24_ranking_substances_by_ph_scale(rng: random.Random) -> Dict[str, Any]:
    items = [
        ("battery acid (sulfuric acid)", 1),
        ("lemon juice", 2),
        ("black coffee", 5),
        ("pure water", 7),
        ("baking soda solution", 9),
        ("soapy water", 10),
        ("bleach / drain cleaner", 13),
    ]
    sampled = rng.sample(items, 4)
    sorted_items = sorted(sampled, key=lambda x: x[1])

    names_list = ", ".join([f"{x[0]} (pH {x[1]})" for x in sampled])
    correct_order = " < ".join([x[0] for x in sorted_items])

    prompt = (
        f"Consider four everyday substances and their measured pH values:\n"
        f"{names_list}.\n\n"
        f"1. Arrange these four substances in order of **increasing pH** (from lowest pH to highest pH).\n"
        f"2. Identify the single most acidic substance among the four."
    )
    sol = (
        f"**Step 1:** Order from lowest pH to highest pH: **{correct_order}** [1 Mark: Ranking].\n\n"
        f"**Step 2:** The most acidic substance is **{sorted_items[0][0]}** (lowest pH value of {sorted_items[0][1]}) [1 Mark: Acid strength]."
    )
    return {
        "id": f"ns7_ab_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Order: {correct_order}; Most acidic: {sorted_items[0][0]}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "24_ranking_substances_by_ph_scale",
        "misconception_tags": ["lower_ph_means_more_acidic"],
        "hints": {
            "tier_1": "Lower pH means more acidic. Highest pH is most basic.",
            "tier_2": f"Lowest pH is {sorted_items[0][0]} (pH {sorted_items[0][1]}).",
            "tier_3": f"Order: {correct_order}; Most acidic: {sorted_items[0][0]}."
        }
    }


def arch_25_strong_vs_weak_acids_ph_comparison(rng: random.Random) -> Dict[str, Any]:
    pairs = [
        ("Hydrochloric acid ($HCl$)", 1, "Ethanoic acid / vinegar", 4),
        ("Sulfuric acid ($H_2SO_4$)", 1, "Citric acid / lemon juice", 3),
        ("Nitric acid ($HNO_3$)", 2, "Carbonic acid / soda water", 5),
    ]
    s_acid, s_ph, w_acid, w_ph = rng.choice(pairs)

    prompt = (
        f"Compare two acidic solutions:\n"
        f"- Acid X: {s_acid} (pH {s_ph})\n"
        f"- Acid Y: {w_acid} (pH {w_ph})\n\n"
        f"1. Which acid is the **stronger acid**? Justify using pH values.\n"
        f"2. Explain what 'acid strength' means in terms of how completely the acid molecules dissociate/ionise in water."
    )
    sol = (
        f"**Step 1:** **Acid X ({s_acid})** is the stronger acid because a lower pH ({s_ph} vs {w_ph}) indicates a much higher concentration of free hydrogen ions ($H^+$) [1 Mark: Strength & pH].\n\n"
        f"**Step 2:** A strong acid **ionises completely (100%)** in water to release all its $H^+$ ions, whereas a weak acid only **partially ionises**, leaving most molecules intact [1 Mark: Ionisation definition]."
    )
    return {
        "id": f"ns7_ab_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"Acid X ({s_acid}); lower pH indicates higher H+ concentration; strong acids ionise completely whereas weak acids only partially ionise",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 2,
        "subskill": "25_strong_vs_weak_acids_ph_comparison",
        "misconception_tags": ["acid_strength_vs_concentration"],
        "hints": {
            "tier_1": "Lower pH means stronger acid.",
            "tier_2": "Strong acids ionise completely in water.",
            "tier_3": f"Acid X ({s_acid}); complete vs partial ionisation."
        }
    }
