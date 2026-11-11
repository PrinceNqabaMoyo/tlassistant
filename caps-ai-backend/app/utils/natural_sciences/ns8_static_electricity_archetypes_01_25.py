"""Grade 8 Natural Sciences: Term 3 - Static Electricity Archetypes (01 to 25).
100% Aligned with South African National Curriculum Standards.
Grounded directly in curriculum_docs_auto/NaturalSciences_Gr8/Term 3/01. Static electricity.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List


def arch_01_atomic_structure_and_electrical_charges(rng: random.Random) -> Dict[str, Any]:
    particles = [
        ("protons", "positively charged (+1)", "tightly bound inside the dense atomic nucleus"),
        ("electrons", "negatively charged (-1)", "orbiting the nucleus in outer electron shells, relatively free to move"),
        ("neutrons", "electrically neutral (0)", "located alongside protons within the atomic nucleus")
    ]
    name, charge, location = rng.choice(particles)
    prompt = (
        f"All matter is composed of microscopic atoms containing subatomic particles.\n\n"
        f"Which statement correctly describes the electrical charge and location of **{name}** in an atom?"
    )
    correct_opt = f"{name.capitalize()} are {charge} and are {location}."
    options = [
        correct_opt,
        f"{name.capitalize()} carry no charge and travel faster than light in empty space.",
        f"{name.capitalize()} carry variable random charges that change every second.",
        f"{name.capitalize()} are always positively charged and dissolve during chemical reactions."
    ]
    rng.shuffle(options)
    sol = (
        f"**Atomic Structure & Charges:**\n"
        f"- Protons: positive (+), inside the nucleus.\n"
        f"- Neutrons: neutral (0), inside the nucleus.\n"
        f"- Electrons: negative (-), orbiting in shells outside the nucleus.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_01_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "01_atomic_structure_and_electrical_charges",
        "question_family_id": "01_atomic_structure_and_electrical_charges",
        "hints": {
            "tier_1": f"Recall whether {name} are positive, negative, or neutral.",
            "tier_2": f"Consider where {name} are located relative to the atomic nucleus.",
            "tier_3": f"{name.capitalize()} are {charge} and are {location}."
        },
        "misconception_tags": ["confusing_subatomic_charges"]
    }


def arch_02_concept_of_neutral_uncharged_matter(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"An ordinary plastic ruler, a glass beaker, or a wooden tabletop is described in science as being **electrically neutral**.\n\n"
        f"What does it mean for an object to be electrically neutral at the atomic level?"
    )
    correct_opt = "The object contains an equal number of positive protons and negative electrons, so the opposite charges balance and cancel out to give a net charge of zero."
    options = [
        correct_opt,
        "The object contains zero protons and zero electrons; it is made purely of empty space.",
        "All electrical charges inside the material have been destroyed permanently by air pressure.",
        "The object contains only neutrons and has lost its atomic nuclei."
    ]
    rng.shuffle(options)
    sol = (
        f"**Meaning of Electrical Neutrality:**\n"
        f"1. A neutral object is NOT devoid of charges. It possesses billions of positive protons and negative electrons.\n"
        f"2. Because the total number of protons equals the total number of electrons ($N_p = N_e$):\n"
        f"   $$\\text{{Net charge}} = (+Q) + (-Q) = 0$$\n"
        f"3. The positive and negative charges balance out completely.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_02_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "02_concept_of_neutral_uncharged_matter",
        "question_family_id": "02_concept_of_neutral_uncharged_matter",
        "hints": {
            "tier_1": "Does neutral mean having no charges, or having balanced equal charges?",
            "tier_2": "Neutral objects contain equal numbers of positive protons and negative electrons.",
            "tier_3": "Equal number of positive protons and negative electrons balancing to net zero charge."
        },
        "misconception_tags": ["neutral_means_no_charges_exist"]
    }


def arch_03_mechanism_of_charging_by_friction_triboelectric(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When two different insulating materials (such as a plastic rod and a woollen cloth) are vigorously rubbed together, both materials acquire static electrical charges.\n\n"
        f"What physical process occurs during this friction (the triboelectric effect)?"
    )
    correct_opt = "Friction provides kinetic energy that knocks mobile valence electrons off one material and transfers them onto the other material."
    options = [
        correct_opt,
        "Protons are torn out of the atomic nuclei and move across to the other material.",
        "Friction creates new electrical charge out of nothing through thermal friction.",
        "Air molecules between the surfaces turn into pure liquid electrical current."
    ]
    rng.shuffle(options)
    sol = (
        f"**Triboelectric Charging Mechanism:**\n"
        f"1. Protons are bound strongly in the nucleus and CANNOT move during everyday friction.\n"
        f"2. Outer (valence) electrons are loosely held.\n"
        f"3. When surfaces rub together, contact friction transfers electrons from the material with lower electron affinity to the one with higher electron affinity.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_03_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "03_mechanism_of_charging_by_friction_triboelectric",
        "question_family_id": "03_mechanism_of_charging_by_friction_triboelectric",
        "hints": {
            "tier_1": "Which subatomic particles are transferred during friction: protons or electrons?",
            "tier_2": "Only electrons move; protons remain locked in atomic nuclei.",
            "tier_3": "Friction transfers mobile electrons from one material to the other."
        },
        "misconception_tags": ["protons_move_during_friction"]
    }


def arch_04_movement_of_electrons_versus_immobile_protons(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In an electrostatic experiment, a glass rod acquires a positive charge when rubbed with a silk cloth. "
        f"A learner explains: *'The glass rod gained protons from the silk.'*\n\n"
        f"Why is the learner's explanation scientifically incorrect?"
    )
    correct_opt = "Protons are massive and locked rigidly within the nucleus by strong nuclear forces; an object becomes positively charged ONLY by losing negative electrons."
    options = [
        correct_opt,
        "Protons do not carry any electrical charge in glass materials.",
        "The learner is correct because protons are light particles that move freely through air.",
        "Glass rods cannot acquire electrical charge under any circumstances."
    ]
    rng.shuffle(options)
    sol = (
        f"**Proton Immobility Law:**\n"
        f"- Protons are $\\approx 1836$ times more massive than electrons and are bound in the nucleus by the strong nuclear force.\n"
        f"- Protons NEVER move or transfer during electrostatic charging.\n"
        f"- When glass becomes positive, it has **lost negative electrons** to the silk cloth.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_04_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "04_movement_of_electrons_versus_immobile_protons",
        "question_family_id": "04_movement_of_electrons_versus_immobile_protons",
        "hints": {
            "tier_1": "Can protons move between atoms during friction?",
            "tier_2": "Protons never move. Positive charge comes from losing negative electrons.",
            "tier_3": "Protons are locked in the nucleus; positive charge is caused by a deficit of electrons."
        },
        "misconception_tags": ["positive_charge_from_gaining_protons"]
    }


def arch_05_perspex_rod_rubbed_with_cloth_electron_transfer(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A transparent Perspex (acrylic) rod is rubbed vigorously with a dry silk or woollen cloth. "
        f"During friction, electrons transfer from the Perspex rod onto the cloth.\n\n"
        f"What are the resulting electrical charges on the Perspex rod and on the cloth?"
    )
    correct_opt = "The Perspex rod becomes positively charged (lost electrons), and the cloth becomes negatively charged (gained electrons)."
    options = [
        correct_opt,
        "The Perspex rod becomes negatively charged, and the cloth becomes positively charged.",
        "Both the rod and the cloth become positively charged simultaneously.",
        "Both the rod and the cloth remain completely neutral because electrons disappear."
    ]
    rng.shuffle(options)
    sol = (
        f"**Charge Transfer Tracking:**\n"
        f"1. Electrons carry negative charge ($-e$).\n"
        f"2. Perspex rod loses electrons -> deficit of electrons -> excess protons -> **positively charged**.\n"
        f"3. Cloth gains the transferred electrons -> excess electrons -> **negatively charged**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_05_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "05_perspex_rod_rubbed_with_cloth_electron_transfer",
        "question_family_id": "05_perspex_rod_rubbed_with_cloth_electron_transfer",
        "hints": {
            "tier_1": "If an object loses negative electrons, what charge does it become?",
            "tier_2": "Losing electrons makes it positive; gaining electrons makes it negative.",
            "tier_3": "Perspex becomes positive (lost electrons); cloth becomes negative (gained electrons)."
        },
        "misconception_tags": ["both_objects_gain_same_charge"]
    }


def arch_06_polythene_rod_rubbed_with_wool_electron_transfer(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A black polythene (polyethylene) plastic rod is rubbed with a dry woollen duster. "
        f"Polythene has a strong affinity for electrons and pulls electrons from the wool.\n\n"
        f"What are the final charges on the polythene rod and on the wool duster?"
    )
    correct_opt = "The polythene rod becomes negatively charged (gained electrons), and the wool duster becomes positively charged (lost electrons)."
    options = [
        correct_opt,
        "The polythene rod becomes positively charged, and the wool duster becomes negatively charged.",
        "Both objects become negatively charged because friction always produces negative electricity.",
        "Neither object charges because plastic is an electrical insulator."
    ]
    rng.shuffle(options)
    sol = (
        f"**Polythene Triboelectric Interaction:**\n"
        f"- Polythene gains negative electrons from the wool -> has an excess of electrons -> **negatively charged**.\n"
        f"- Wool duster loses those electrons -> has an excess of positive protons -> **positively charged**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_06_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "06_polythene_rod_rubbed_with_wool_electron_transfer",
        "question_family_id": "06_polythene_rod_rubbed_with_wool_electron_transfer",
        "hints": {
            "tier_1": "Which gained electrons and which lost electrons?",
            "tier_2": "Gaining electrons gives a negative charge; losing electrons leaves a positive charge.",
            "tier_3": "Polythene becomes negative (gained electrons); wool becomes positive (lost electrons)."
        },
        "misconception_tags": ["insulators_cannot_be_charged"]
    }


def arch_07_identifying_positive_charge_from_electron_deficit(rng: random.Random) -> Dict[str, Any]:
    protons = rng.choice([1000, 5000, 10000])
    electrons = protons - rng.choice([50, 100, 200])
    prompt = (
        f"An insulated metal sphere is analyzed in an electrostatic laboratory. "
        f"It is found to contain ${protons}$ positive protons and ${electrons}$ negative electrons.\n\n"
        f"What is the overall electrical state of the sphere?"
    )
    correct_opt = f"Positively charged, because the number of protons ({protons}) exceeds the number of electrons ({electrons}), creating an electron deficit."
    options = [
        correct_opt,
        f"Negatively charged, because electrons are always more powerful than protons.",
        "Electrically neutral, because protons and electrons are in the same object.",
        "Unstable and about to explode from atomic fission."
    ]
    rng.shuffle(options)
    sol = (
        f"**Net Charge Calculation:**\n"
        f"$$\\text{{Protons}} = {protons} \\quad (+)\n$$\n"
        f"$$\\text{{Electrons}} = {electrons} \\quad (-)\n$$\n"
        f"$$\\text{{Net Charge}} = +{protons} - {electrons} = +{protons - electrons}\n$$\n"
        f"Because there is an excess of positive protons (electron deficit), the sphere is **positively charged**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_07_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "07_identifying_positive_charge_from_electron_deficit",
        "question_family_id": "07_identifying_positive_charge_from_electron_deficit",
        "hints": {
            "tier_1": "Are there more protons or more electrons?",
            "tier_2": f"Protons ({protons}) > Electrons ({electrons}).",
            "tier_3": "More protons than electrons means the object is positively charged."
        },
        "misconception_tags": ["electrons_dominate_protons"]
    }


def arch_08_identifying_negative_charge_from_electron_excess(rng: random.Random) -> Dict[str, Any]:
    electrons = rng.choice([1200, 6000, 15000])
    protons = electrons - rng.choice([100, 300, 500])
    prompt = (
        f"A suspended polystyrene sphere contains ${protons}$ positive protons and ${electrons}$ negative electrons.\n\n"
        f"What is the overall electrical state of the sphere?"
    )
    correct_opt = f"Negatively charged, because there are more negative electrons ({electrons}) than positive protons ({protons}), creating an electron excess."
    options = [
        correct_opt,
        f"Positively charged, because protons occupy the centre of the atom.",
        "Neutral, because polystyrene is a plastic that cannot hold a charge.",
        "Radioactive, because electrons outnumber protons."
    ]
    rng.shuffle(options)
    sol = (
        f"**Net Charge Evaluation:**\n"
        f"$$\\text{{Electrons}} = {electrons} \\quad (-)\n$$\n"
        f"$$\\text{{Protons}} = {protons} \\quad (+)\n$$\n"
        f"$$\\text{{Net}} = -{electrons} + {protons} = -{electrons - protons}\n$$\n"
        f"The excess of negative electrons makes the object **negatively charged**.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_08_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "08_identifying_negative_charge_from_electron_excess",
        "question_family_id": "08_identifying_negative_charge_from_electron_excess",
        "hints": {
            "tier_1": "Are there more electrons or protons?",
            "tier_2": f"Electrons ({electrons}) > Protons ({protons}).",
            "tier_3": "Excess electrons mean the sphere is negatively charged."
        },
        "misconception_tags": ["protons_cancel_excess_electrons"]
    }


def arch_09_fundamental_law_of_charges_attraction_repulsion(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In electrostatics, the fundamental law governing forces between charged bodies is universally observed.\n\n"
        f"Which statement correctly summarizes the **Fundamental Law of Electrostatics**?"
    )
    correct_opt = "Like charges repel each other (positive repels positive; negative repels negative), while unlike (opposite) charges attract each other."
    options = [
        correct_opt,
        "Like charges attract each other, while opposite charges repel each other.",
        "All electrical charges attract all other charges regardless of their sign.",
        "Electrical charges only exert forces when connected by a copper wire."
    ]
    rng.shuffle(options)
    sol = (
        f"**The Fundamental Law of Electrostatics:**\n"
        f"- $(+) \\leftrightarrow (+)$ : **Repel** (like charges)\n"
        f"- $(-) \\leftrightarrow (-)$ : **Repel** (like charges)\n"
        f"- $(+) \\rightarrow \\leftarrow (-)$ : **Attract** (unlike / opposite charges)\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_09_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "09_fundamental_law_of_charges_attraction_repulsion",
        "question_family_id": "09_fundamental_law_of_charges_attraction_repulsion",
        "hints": {
            "tier_1": "Do like charges attract or repel?",
            "tier_2": "Like charges repel; opposite charges attract.",
            "tier_3": "Like charges repel; unlike (opposite) charges attract."
        },
        "misconception_tags": ["like_charges_attract"]
    }


def arch_10_suspended_charged_rods_interaction(rng: random.Random) -> Dict[str, Any]:
    combinations = [
        ("negatively charged polythene rod", "negatively charged polythene rod", "repel each other and swing apart", "like charges repel"),
        ("positively charged Perspex rod", "negatively charged polythene rod", "attract each other and swing together", "unlike charges attract"),
        ("positively charged glass rod", "positively charged Perspex rod", "repel each other and swing apart", "like charges repel")
    ]
    rod1, rod2, motion, rule = rng.choice(combinations)
    prompt = (
        f"A {rod1} is suspended horizontally in a stirrup by a light nylon thread so it is free to rotate. "
        f"A teacher brings a second {rod2} close to one end of the suspended rod without touching it.\n\n"
        f"What will happen to the suspended rod, and which electrostatics rule explains it?"
    )
    correct_opt = f"The rods will {motion}, because {rule}."
    options = [
        correct_opt,
        f"The rods will not interact at all because electrical charges cannot act through air.",
        f"The suspended rod will immediately lose all charge and drop to the floor.",
        f"The rods will fuse together magnetically into a single metal bar."
    ]
    rng.shuffle(options)
    sol = (
        f"**Suspended Rod Interaction:**\n"
        f"- Rod 1: {rod1}\n"
        f"- Rod 2: {rod2}\n"
        f"- Applying the Fundamental Law of Electrostatics: {rule}.\n"
        f"- Therefore, the rods will {motion}.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_10_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "10_suspended_charged_rods_interaction",
        "question_family_id": "10_suspended_charged_rods_interaction",
        "hints": {
            "tier_1": "Are both rods having the same sign of charge or opposite signs?",
            "tier_2": f"Rule: {rule}.",
            "tier_3": f"The rods will {motion}, because {rule}."
        },
        "misconception_tags": ["suspended_rod_no_force"]
    }


def arch_11_charged_balloon_sticking_to_neutral_wall_induction(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A rubber balloon is rubbed against clean dry hair and acquires a negative charge. "
        f"When pressed against a neutral, unpainted plaster wall, the balloon sticks firmly to the wall.\n\n"
        f"Why does a negatively charged balloon stick to a completely neutral wall?"
    )
    correct_opt = "Electrostatic induction: negative electrons in the balloon repel electrons in the wall surface deeper inward, leaving the front surface with an induced positive charge that attracts the negative balloon."
    options = [
        correct_opt,
        "The wall produces wet glue automatically when touched by rubber.",
        "The rubber balloon creates a magnetic suction vacuum against the plaster.",
        "The balloon permanently transfers all its electrons to the wall within 1 millisecond."
    ]
    rng.shuffle(options)
    sol = (
        f"**Electrostatic Induction Mechanism:**\n"
        f"1. The balloon is negatively charged.\n"
        f"2. The wall is electrically neutral (protons = electrons).\n"
        f"3. When the balloon approaches, like charges repel: electrons in the wall surface are repelled deeper into the wall.\n"
        f"4. This leaves the front layer of the wall with an excess of positive protons (**induced positive charge**).\n"
        f"5. Because unlike charges attract, the negative balloon is attracted to the closer positive surface and sticks.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_11_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "11_charged_balloon_sticking_to_neutral_wall_induction",
        "question_family_id": "11_charged_balloon_sticking_to_neutral_wall_induction",
        "hints": {
            "tier_1": "Can a charged object attract a neutral object?",
            "tier_2": "Yes, by electrostatic induction (polarizing the surface).",
            "tier_3": "Electrons in the wall surface are repelled, inducing a positive charge that attracts the balloon."
        },
        "misconception_tags": ["charged_objects_cannot_attract_neutral"]
    }


def arch_12_charged_plastic_comb_attracting_paper_scraps(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A plastic comb is pulled through dry hair, gaining a negative charge. "
        f"When brought near small bits of neutral torn paper on a table, the paper bits jump up and cling to the comb.\n\n"
        f"What sequence of events causes the neutral paper scraps to jump up?"
    )
    correct_opt = "Negative charge on the comb repels electrons to the bottom of the paper scraps; the top surfaces become positively charged by induction and are pulled upward toward the comb."
    options = [
        correct_opt,
        "Paper contains magnetic iron dust that aligns with static electricity.",
        "The comb blows hot air downward that bounces the paper bits upward.",
        "Paper scraps become radioactive when exposed to plastic."
    ]
    rng.shuffle(options)
    sol = (
        f"**Electrostatic Attraction of Neutral Paper:**\n"
        f"1. The paper scraps are initially neutral.\n"
        f"2. As the negatively charged comb approaches, electrons within paper molecules are repelled away toward the lower side of each scrap (charge separation/polarisation).\n"
        f"3. The upper surface of the paper scraps acquires an **induced positive charge**.\n"
        f"4. The attractive force on the closer positive surface exceeds the repulsive force on the farther negative side.\n"
        f"5. The net electrostatic upward force overcomes gravity, causing the paper scraps to jump up.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_12_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "12_charged_plastic_comb_attracting_paper_scraps",
        "question_family_id": "12_charged_plastic_comb_attracting_paper_scraps",
        "hints": {
            "tier_1": "What happens to the charges in the paper when the comb gets close?",
            "tier_2": "Electrons are repelled away, leaving positive charges on the near side.",
            "tier_3": "Induced positive charges on the top of the paper scraps are attracted to the comb."
        },
        "misconception_tags": ["paper_is_magnetic"]
    }


def arch_13_bending_thin_stream_of_water_with_charged_rod(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A thin, smooth stream of tap water flows continuously from a faucet. "
        f"When a charged plastic ruler (either positively or negatively charged) is brought close to the stream without touching it, the water stream visibly bends toward the ruler.\n\n"
        f"Why is neutral liquid water attracted to both positively and negatively charged objects?"
    )
    correct_opt = "Water molecules ($H_2O$) are polar; their positive hydrogen ends rotate toward a negative rod, and their negative oxygen ends rotate toward a positive rod, creating an attractive force in both cases."
    options = [
        correct_opt,
        "Water is pure metal and conducts electric current straight from the plastic rod.",
        "The plastic ruler heats the surrounding air so water evaporates towards it.",
        "Water contains dissolved salt ions that only interact with gravity."
    ]
    rng.shuffle(options)
    sol = (
        f"**Polarity of Water in Electrostatics:**\n"
        f"1. Water ($H_2O$) is an asymmetrical **polar molecule** with a permanent electric dipole (partial positive $\\delta+$ on hydrogens, partial negative $\\delta-$ on oxygen).\n"
        f"2. When a **negative rod** approaches: Water molecules rotate so their $\\delta+$ hydrogen ends face the rod -> attraction.\n"
        f"3. When a **positive rod** approaches: Water molecules rotate so their $\\delta-$ oxygen ends face the rod -> attraction.\n"
        f"4. In both instances, the closer pole experiences a stronger force than the farther pole, bending the water stream toward the rod.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_13_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "13_bending_thin_stream_of_water_with_charged_rod",
        "question_family_id": "13_bending_thin_stream_of_water_with_charged_rod",
        "hints": {
            "tier_1": "What molecular property of water makes it respond to electrical charges?",
            "tier_2": "Water is a polar molecule with positive and negative ends.",
            "tier_3": "Water molecules are polar and rotate their opposite pole towards the charged rod."
        },
        "misconception_tags": ["water_only_attracted_to_one_charge"]
    }


def arch_14_electrostatic_induction_mechanism_in_neutral_objects(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Two neutral metal spheres (Sphere X and Sphere Y) resting on insulating stands touch each other. "
        f"A positively charged rod is held near Sphere X (without touching it). "
        f"While the rod is still in place, the two spheres are pulled apart.\n\n"
        f"What are the final electrical charges on Sphere X and Sphere Y?"
    )
    correct_opt = "Sphere X is negatively charged (electrons were drawn into it toward the positive rod), and Sphere Y is positively charged (lost electrons)."
    options = [
        correct_opt,
        "Both spheres are positively charged because the rod shared its protons with both.",
        "Both spheres remain completely neutral because no physical contact occurred.",
        "Sphere X is positive and Sphere Y is negative."
    ]
    rng.shuffle(options)
    sol = (
        f"**Charging by Electrostatic Induction:**\n"
        f"1. When the positive rod approaches Sphere X, mobile electrons from both touching spheres are attracted toward Sphere X.\n"
        f"2. Sphere X accumulates excess negative electrons.\n"
        f"3. Sphere Y is left with a deficit of electrons (excess positive protons).\n"
        f"4. When separated before removing the rod, the charges are trapped:\n"
        f"   - Sphere X: **Negative**\n"
        f"   - Sphere Y: **Positive**\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_14_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "14_electrostatic_induction_mechanism_in_neutral_objects",
        "question_family_id": "14_electrostatic_induction_mechanism_in_neutral_objects",
        "hints": {
            "tier_1": "Which sphere has electrons pulled towards it by the positive rod?",
            "tier_2": "Electrons move into Sphere X, leaving Sphere Y with an electron deficit.",
            "tier_3": "Sphere X is negative (accumulated electrons); Sphere Y is positive (lost electrons)."
        },
        "misconception_tags": ["induction_requires_touching_rod"]
    }


def arch_15_gold_leaf_electroscope_structure_and_operation(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A gold-leaf electroscope consists of a brass disc/cap at the top, a brass stem passing through an insulating rubber stopper, and a delicate gold leaf hanging parallel to the stem inside an earthed metal case with glass windows.\n\n"
        f"What is the primary scientific purpose of an electroscope?"
    )
    correct_opt = "To detect the presence, type, and relative quantity of electrostatic charge on an object."
    options = [
        correct_opt,
        "To generate 220-volt AC electricity for household kitchen appliances.",
        "To measure the atmospheric air pressure and humidity in weather forecasts.",
        "To store massive magnetic fields for medical MRI scanners."
    ]
    rng.shuffle(options)
    sol = (
        f"**Function of the Gold-Leaf Electroscope:**\n"
        f"- The electroscope is a classic electrostatic detector.\n"
        f"- It detects whether an object has an electrical charge.\n"
        f"- When charged, the gold leaf and the brass stem acquire like charges and repel, causing the leaf to diverge (spread away).\n"
        f"- The divergence angle indicates the relative quantity of charge.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_15_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "15_gold_leaf_electroscope_structure_and_operation",
        "question_family_id": "15_gold_leaf_electroscope_structure_and_operation",
        "hints": {
            "tier_1": "What does an electroscope detect?",
            "tier_2": "It detects electrical charge.",
            "tier_3": "To detect the presence, type, and relative quantity of electrostatic charge."
        },
        "misconception_tags": ["electroscope_is_a_generator"]
    }


def arch_16_detecting_charge_using_an_electroscope(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A negatively charged polythene rod touches the brass disc of an uncharged gold-leaf electroscope, and the rod is then removed.\n\n"
        f"What happens to the gold leaf, and what charge do the stem and leaf now hold?"
    )
    correct_opt = "The gold leaf diverges (lifts away from the stem) because negative electrons transferred onto the electroscope, giving both the stem and the leaf like negative charges that repel."
    options = [
        correct_opt,
        "The gold leaf remains completely flat because gold cannot conduct electric charges.",
        "The leaf curls up into a ball because it acquired positive protons from the plastic.",
        "The electroscope instantly discharges into lightning and disintegrates."
    ]
    rng.shuffle(options)
    sol = (
        f"**Charging an Electroscope by Conduction (Contact):**\n"
        f"1. When the negative rod touches the brass disc, excess electrons flow from the rod onto the disc.\n"
        f"2. Electrons conduct down through the brass stem to the gold leaf.\n"
        f"3. Both the brass plate/stem and the gold leaf become negatively charged.\n"
        f"4. Because like charges repel, the light, flexible gold leaf is pushed outward away from the stem (**divergence**).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_16_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "16_detecting_charge_using_an_electroscope",
        "question_family_id": "16_detecting_charge_using_an_electroscope",
        "hints": {
            "tier_1": "Do the stem and the leaf get the same charge when touched?",
            "tier_2": "Both get negative charge. Like charges repel, so the leaf diverges.",
            "tier_3": "The leaf diverges because like negative charges repel each other."
        },
        "misconception_tags": ["leaves_attract_when_charged"]
    }


def arch_17_electroscope_leaf_divergence_angle_and_charge_magnitude(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When Rod A is brought near an electroscope, the leaf diverges by $15^\\circ$. "
        f"When Rod B is brought to the exact same distance, the leaf diverges by $45^\\circ$.\n\n"
        f"What valid conclusion can be drawn regarding Rod A and Rod B?"
    )
    correct_opt = "Rod B carries a significantly greater quantity of electrostatic charge than Rod A, producing a stronger repulsive force on the leaf."
    options = [
        correct_opt,
        "Rod A is made of solid metal while Rod B is an electrical insulator.",
        "Rod A is positively charged while Rod B is completely uncharged.",
        "The electroscope is defective and produces random leaf movements."
    ]
    rng.shuffle(options)
    sol = (
        f"**Leaf Divergence vs Magnitude of Charge:**\n"
        f"- The electrostatic repulsive force between the stem and the leaf is directly proportional to the amount of charge present ($F \\propto q_1 q_2$).\n"
        f"- A larger divergence angle ($45^\\circ$ vs $15^\\circ$) indicates a stronger repulsive force, meaning Rod B carries a larger quantity of static charge.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_17_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "17_electroscope_leaf_divergence_angle_and_charge_magnitude",
        "question_family_id": "17_electroscope_leaf_divergence_angle_and_charge_magnitude",
        "hints": {
            "tier_1": "Does a wider divergence angle mean more or less charge?",
            "tier_2": "A wider angle means a stronger repulsive force from more charge.",
            "tier_3": "Rod B carries a greater quantity of charge than Rod A."
        },
        "misconception_tags": ["divergence_angle_is_random"]
    }


def arch_18_van_de_graaff_generator_belt_and_dome_mechanism(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A Van de Graaff generator is an electrostatic machine used in school science laboratories to generate high voltages. "
        f"A rubber belt travels over two rollers, passing metal combs near the bottom and inside a hollow metal sphere (dome).\n\n"
        f"How does the Van de Graaff generator accumulate huge static charges on its outer dome?"
    )
    correct_opt = "Friction between the moving belt and roller transfers electrons; the belt transports charge to the upper comb, which transfers charge to the outside surface of the hollow metal dome."
    options = [
        correct_opt,
        "The dome is connected directly to a nuclear power reactor in the base.",
        "The machine generates millions of protons by burning chemical fuel inside the column.",
        "The rubber belt converts sound vibrations from the classroom into static electricity."
    ]
    rng.shuffle(options)
    sol = (
        f"**Van de Graaff Generator Principles:**\n"
        f"1. A motorized rubber belt moving over acrylic/nylon rollers separates charge by continuous friction.\n"
        f"2. Sharp metal points (combs) spray charge onto the belt.\n"
        f"3. The belt carries this charge upward into the hollow metal dome.\n"
        f"4. Inside the sphere, an upper comb collects the charge.\n"
        f"5. Electrostatic law: All excess charge on a hollow conductor redistributes entirely onto the **outer surface**, allowing huge potential differences to accumulate.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_18_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "18_van_de_graaff_generator_belt_and_dome_mechanism",
        "question_family_id": "18_van_de_graaff_generator_belt_and_dome_mechanism",
        "hints": {
            "tier_1": "What moves the charge from bottom to top?",
            "tier_2": "The moving rubber belt transports charge separated by friction up to the dome.",
            "tier_3": "Friction between belt and roller separates charge, transported to the outer dome."
        },
        "misconception_tags": ["van_de_graaff_is_magnetic"]
    }


def arch_19_hair_standing_on_end_van_de_graaff_demonstration(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In a classic physics demonstration, a student stands on an insulating plastic stool and places their hands on the dome of a Van de Graaff generator before it is turned on. "
        f"As the machine runs, the student's strands of hair stand straight up and spread out like a fan.\n\n"
        f"What is the electrostatic explanation for why the hair strands stand on end and repel each other?"
    )
    correct_opt = "Charge spreads over the student's body to every individual strand of hair; because all strands acquire the same like charge, they mutually repel each other and stand up."
    options = [
        correct_opt,
        "The generator produces high-speed hurricane winds that blow the hair upward.",
        "The hair is magnetized and attracted to the ceiling fluorescent lights.",
        "Static electricity makes human hair grow ten times faster in five seconds."
    ]
    rng.shuffle(options)
    sol = (
        f"**Hair Repulsion Demonstration:**\n"
        f"1. The human body is an electrical conductor.\n"
        f"2. Standing on an insulator prevents charge from escaping to the ground.\n"
        f"3. Charge flows from the dome onto the student and distributes across the head and into each individual hair follicle.\n"
        f"4. Each hair strand acquires the **same sign of charge** (all positive or all negative).\n"
        f"5. **Like charges repel**: every hair strand repels adjacent hair strands, forcing them to spread as far apart as possible in all directions.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_19_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "19_hair_standing_on_end_van_de_graaff_demonstration",
        "question_family_id": "19_hair_standing_on_end_van_de_graaff_demonstration",
        "hints": {
            "tier_1": "Do all strands of hair get the same charge or different charges?",
            "tier_2": "All strands get the same charge, and like charges repel each other.",
            "tier_3": "Each hair strand acquires like charge; like charges repel, forcing strands to stand apart."
        },
        "misconception_tags": ["hair_attracted_to_ceiling"]
    }


def arch_20_standing_on_insulating_stool_during_van_de_graaff(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In the hair-raising demonstration, why is it absolutely mandatory for the volunteer to stand on an **insulating plastic stool** or thick polystyrene block?"
    )
    correct_opt = "To prevent charge from immediately conducting through the student's body down into the floor (earthing); the insulator allows electrostatic charge to accumulate on the body."
    options = [
        correct_opt,
        "To bring the student closer to the ceiling magnets.",
        "To prevent the student's shoes from catching fire from carpet friction.",
        "Because plastic stools generate positive protons that feed the dome."
    ]
    rng.shuffle(options)
    sol = (
        f"**Function of the Insulating Stool:**\n"
        f"- The human body is a conductor. If the student stands directly on the floor, electrons immediately flow into or out of the ground (earthing).\n"
        f"- The insulating stool breaks the circuit to the ground, preventing electrical discharge.\n"
        f"- This allows static charge to build up on the student's body and hair.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_20_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "20_standing_on_insulating_stool_during_van_de_graaff",
        "question_family_id": "20_standing_on_insulating_stool_during_van_de_graaff",
        "hints": {
            "tier_1": "What happens if a charged person touches the earth/floor?",
            "tier_2": "The charge flows into the ground (earthing) unless insulated.",
            "tier_3": "The stool prevents charge from conducting to the floor (earthing)."
        },
        "misconception_tags": ["stool_adds_voltage"]
    }


def arch_21_concept_of_earthing_or_grounding_a_conductor(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In electrical science and electrostatics, connecting a charged conductor to the Earth via a conducting wire or human touch is called **earthing** (or grounding).\n\n"
        f"What is the physical result of earthing a charged object?"
    )
    correct_opt = "The object becomes electrically neutral because the Earth acts as an immense reservoir that can donate or absorb electrons without changing its own potential."
    options = [
        correct_opt,
        "The object becomes permanently magnetized with north and south poles.",
        "All atomic nuclei in the object are destroyed by ground pressure.",
        "The object acquires an infinite positive charge that repels all matter."
    ]
    rng.shuffle(options)
    sol = (
        f"**Definition and Mechanism of Earthing:**\n"
        f"1. The Earth is a massive, conducting reservoir of electrical charge.\n"
        f"2. When a charged object is connected to the Earth, electrons transfer between the object and the Earth until the object's net charge becomes zero.\n"
        f"3. The object returns to a stable, neutral state.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_21_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "21_concept_of_earthing_or_grounding_a_conductor",
        "question_family_id": "21_concept_of_earthing_or_grounding_a_conductor",
        "hints": {
            "tier_1": "Does earthing leave an object charged or neutral?",
            "tier_2": "Earthing neutralizes the object by electron flow to or from the Earth.",
            "tier_3": "The object becomes electrically neutral as Earth donates or absorbs electrons."
        },
        "misconception_tags": ["earthing_magnifies_charge"]
    }


def arch_22_earthing_a_negatively_charged_body_electron_flow(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A metal sphere with an excess of negative electrons is earthed by touching it with an earthed copper wire.\n\n"
        f"In which direction do electrons flow during this earthing process to neutralize the sphere?"
    )
    correct_opt = "Electrons flow from the negatively charged sphere down through the wire into the Earth until the sphere is neutral."
    options = [
        correct_opt,
        "Electrons flow from the Earth upward into the sphere to neutralize the excess electrons.",
        "Positive protons flow from the Earth into the sphere to destroy the electrons.",
        "Neutrons flow out of the wire and form an insulating cloud."
    ]
    rng.shuffle(options)
    sol = (
        f"**Earthing a Negative Conductor:**\n"
        f"- The sphere has an excess of negative electrons.\n"
        f"- Like charges repel: the excess electrons repel each other and seek a path of least resistance to spread out.\n"
        f"- When connected to Earth, excess electrons flow **from the sphere into the Earth** until the sphere reaches neutral balance.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_22_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "22_earthing_a_negatively_charged_body_electron_flow",
        "question_family_id": "22_earthing_a_negatively_charged_body_electron_flow",
        "hints": {
            "tier_1": "Does a negative sphere have excess electrons or deficit?",
            "tier_2": "It has excess electrons; excess electrons escape into the Earth.",
            "tier_3": "Electrons flow from the negatively charged sphere into the Earth."
        },
        "misconception_tags": ["protons_flow_from_earth"]
    }


def arch_23_earthing_a_positively_charged_body_electron_flow(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A positively charged glass rod has a deficit of electrons. A person touches the metal cap of an electroscope carrying this positive charge.\n\n"
        f"How does the positive charge become neutralized during earthing?"
    )
    correct_opt = "Electrons flow from the Earth (through the person's body) into the positively charged object to cancel the electron deficit."
    options = [
        correct_opt,
        "Positive protons flow down through the person's legs into the Earth.",
        "Positive charges evaporate into the air as visible white smoke.",
        "The Earth absorbs the atom's nuclei into the carpet."
    ]
    rng.shuffle(options)
    sol = (
        f"**Earthing a Positive Conductor:**\n"
        f"1. Remember: Protons NEVER move.\n"
        f"2. A positive object has a shortage (deficit) of electrons.\n"
        f"3. When connected to the Earth, the positive potential attracts mobile electrons from the Earth.\n"
        f"4. Electrons flow **from the Earth into the object** until the number of electrons equals the number of protons.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_23_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "23_earthing_a_positively_charged_body_electron_flow",
        "question_family_id": "23_earthing_a_positively_charged_body_electron_flow",
        "hints": {
            "tier_1": "Do protons ever flow into the Earth?",
            "tier_2": "No, only electrons move. Electrons flow from Earth to cancel the positive deficit.",
            "tier_3": "Electrons flow from the Earth into the positive object."
        },
        "misconception_tags": ["protons_escape_to_earth"]
    }


def arch_24_electrostatic_shock_from_car_door_or_shopping_trolley(rng: random.Random) -> Dict[str, Any]:
    situations = [
        "pushing a supermarket shopping trolley on synthetic vinyl flooring and touching a metal shelf",
        "sliding across a fabric car seat in dry winter weather and touching the metal car door handle",
        "walking across a nylon carpet with rubber-soled shoes and touching a metal doorknob"
    ]
    scenario = rng.choice(situations)
    prompt = (
        f"Many people experience a sharp, tiny spark and shock when **{scenario}**.\n\n"
        f"What causes this sudden shock?"
    )
    correct_opt = "Friction separates static charges on your body; when you touch the metal conductor, the accumulated electrons rapidly jump through the air to discharge, heating the air into a tiny spark."
    options = [
        correct_opt,
        "Municipal power cables are illegally wired into shopping shelves and car frames.",
        "Your body generates 10 000 Watts of AC electrical current through muscle contraction.",
        "The metal doorknob produces radioactive rays that ionize human blood."
    ]
    rng.shuffle(options)
    sol = (
        f"**Electrostatic Discharge (ESD) Mechanism:**\n"
        f"1. Friction between shoes/carpet or clothes/car seat transfers electrons, building up a high voltage static charge ($>3000\\text{{ V}}$) on your insulated body.\n"
        f"2. Metal objects are grounded conductors.\n"
        f"3. Just before touching the metal, the strong electric field ionizes air molecules.\n"
        f"4. Electrons jump across the tiny gap in a rapid discharge, heating air particles to produce a visible spark, crackling sound, and brief nerve shock.\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_24_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "24_electrostatic_shock_from_car_door_or_shopping_trolley",
        "question_family_id": "24_electrostatic_shock_from_car_door_or_shopping_trolley",
        "hints": {
            "tier_1": "How does static charge accumulate and discharge?",
            "tier_2": "Friction builds up charge; touching metal causes a sudden rapid spark discharge.",
            "tier_3": "Friction charges your body; electrons rapidly jump to the metal conductor to discharge."
        },
        "misconception_tags": ["mains_electricity_leakage"]
    }


def arch_25_crackling_and_sparks_when_removing_woollen_jersey(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"When removing a woollen or synthetic school jersey over your head in a dark room during dry winter weather, you hear faint crackling sounds and see tiny sparks of light.\n\n"
        f"What is happening at the microscopic level to produce these sounds and sparks?"
    )
    correct_opt = "Friction between the jersey and your shirt separates electrons; as the fabrics pull apart, electrons jump across the air gaps to neutralize, producing tiny sparks and acoustic crackles."
    options = [
        correct_opt,
        "The jersey fibres are chemically decomposing into ash from body heat.",
        "Your hair is catching fire due to high body temperature.",
        "Radio waves from nearby cell phone towers are igniting fabric threads."
    ]
    rng.shuffle(options)
    sol = (
        f"**Static Sparking in Clothing:**\n"
        f"- Pulling the jersey over your shirt involves extensive friction between dissimilar fibres (wool/synthetic and cotton/hair).\n"
        f"- Electrons transfer, leaving one surface positive and the other negative.\n"
        f"- When pulled apart, high electric fields develop across tiny air gaps.\n"
        f"- Electrons spark across the gaps, creating miniature lightning discharges (light) and micro-thunder shockwaves (crackling sounds).\n\n"
        f"**Conclusion:** {correct_opt}"
    )
    return {
        "id": f"ns8_stat_25_{rng.randint(10000, 99999)}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_answer": correct_opt,
        "sample_answer": correct_opt,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "subskill": "25_crackling_and_sparks_when_removing_woollen_jersey",
        "question_family_id": "25_crackling_and_sparks_when_removing_woollen_jersey",
        "hints": {
            "tier_1": "What causes the sparks and crackling when pulling off a jersey?",
            "tier_2": "Friction separates electrons, which spark back across air gaps.",
            "tier_3": "Friction separates electrons; as fabrics separate, electrons spark across air gaps."
        },
        "misconception_tags": ["clothing_combustion_fallacy"]
    }
