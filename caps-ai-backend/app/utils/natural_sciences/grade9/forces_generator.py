"""Natural Sciences Grade 9 Term 3: Forces Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 3/01. Forces.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. contact_vs_field_forces: Classification into Contact (friction, tension, compression) and Field forces (gravitational, magnetic, electrostatic).
2. gravitational_force_and_weight_calc: Mass vs weight calculation using W = m * g across Earth, Moon, Mars, and Jupiter.
3. magnetic_field_and_poles: Magnetic poles, attraction/repulsion, field line direction (N -> S), and ferromagnetic materials.
4. electrostatic_forces_and_charging: Frictional electron transfer, positive/negative charge states, and charge conservation.
5. atmospheric_electrostatics_and_lightning: Lightning discharge mechanism, lightning conductors, and thunderstorm safety precautions.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Forces"
ORDERED_SUBSKILLS = [
    "contact_vs_field_forces",
    "gravitational_force_and_weight_calc",
    "magnetic_field_and_poles",
    "electrostatic_forces_and_charging",
    "atmospheric_electrostatics_and_lightning",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_frc"
    return sha256(raw.encode("utf-8")).hexdigest()[:8]


def _normalize_res(res: Dict[str, Any], term: int = 3) -> Dict[str, Any]:
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

    # Subskill 1: Contact vs Field Forces
    if chosen_subskill == "contact_vs_field_forces":
        question_text = (
            "In physics, a force is defined as a push or a pull exerted upon an object, measured in Newtons (N).\n\n"
            "1. Differentiate fundamentally between a **contact force** and a **field force (non-contact force)**.\n"
            "2. Classify each of the following four physical forces as either a **contact force** or a **field force**:\n"
            "   • (a) Friction opposing a sliding wooden block\n"
            "   • (b) Gravitational attraction pulling a falling apple towards Earth\n"
            "   • (c) Tension in a stretched steel elevator cable\n"
            "   • (d) Electrostatic repulsion between two similarly charged balloons\n"
            "3. State **three observable changes** that a resultant force can produce on a physical object."
        )
        sample = (
            "1. **Difference:**\n"
            "   • **Contact Force:** Occurs only when two physical bodies are touching each other directly;\n"
            "   • **Field Force (Non-contact):** Operates through empty space over a distance without physical contact, resulting from an invisible force field (e.g. gravitational, magnetic, or electrostatic);\n"
            "2. **Classification:**\n"
            "   • (a) Friction: **Contact force**\n"
            "   • (b) Gravitational attraction: **Field force**\n"
            "   • (c) Tension: **Contact force**\n"
            "   • (d) Electrostatic repulsion: **Field force**;\n"
            "3. **Effects of Force:** A force can:\n"
            "   • Change the speed of an object (accelerate or decelerate);\n"
            "   • Change the direction of motion of an object;\n"
            "   • Change the shape or size (deform) of an object."
        )
        marking = (
            "• 2 marks: Clear distinction between contact (physical touching) [1] and field forces (action-at-a-distance) [1]\n"
            "• 2 marks: 4 correct classifications (0.5 mark each) [2]\n"
            "• 2 marks: Three valid effects of force (speed, direction, deformation) [2]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Contact vs Field Forces & Effects of Force",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 3,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Contact forces require physical touching (friction, tension, normal force).",
                "Field forces act across space without touching (gravity, magnetism, electrostatic).",
                "Forces can change speed, direction, or shape.",
            ],
            "misconception_tags": ["gravity_is_a_contact_force_myth", "forces_can_only_push_not_pull_myth"],
            "learning_objective_id": "NS9.EC.13.01",
        })

    # Subskill 2: Gravitational Force and Weight Calculation
    if chosen_subskill == "gravitational_force_and_weight_calc":
        bodies = [
            ("Earth", 9.8, "standard terrestrial gravity"),
            ("the Moon", 1.6, "lunar gravity (approximately one-sixth of Earth)"),
            ("Mars", 3.7, "martian surface gravity"),
            ("Jupiter", 24.8, "massive gas giant gravity"),
        ]
        chosen_body = bodies[actual_seed % len(bodies)]
        masses = [45, 60, 75, 80, 95]
        m_val = masses[actual_seed % len(masses)]
        w_earth = round(m_val * 9.8, 1)
        w_target = round(m_val * chosen_body[1], 1)

        question_text = (
            f"An astronaut has an instrument package with a mass of **{m_val} kg**.\n\n"
            "1. Explain the scientific difference between **mass** and **weight**, stating the SI unit for each.\n"
            f"2. Calculate the **weight of the instrument package on Earth** (where g = 9.8 N/kg).\n"
            f"3. Calculate the **weight of the package on {chosen_body[0]}**, where gravitational acceleration is **g = {chosen_body[1]} N/kg**.\n"
            f"4. State the **mass** of the instrument package when placed on the surface of {chosen_body[0]}."
        )
        sample = (
            "1. **Mass vs Weight:**\n"
            "   • **Mass:** The measure of the amount of matter in an object; invariant (remains constant everywhere); SI unit: **kilogram (kg)**;\n"
            "   • **Weight:** The gravitational downward pulling force exerted on an object by a celestial body; varies depending on local gravity; SI unit: **Newton (N)**;\n"
            f"2. **Weight on Earth:**\n"
            f"   W = m · g = {m_val} kg × 9.8 N/kg = **{w_earth} N**;\n"
            f"3. **Weight on {chosen_body[0]}:**\n"
            f"   W = m · g = {m_val} kg × {chosen_body[1]} N/kg = **{w_target} N**;\n"
            f"4. **Mass on {chosen_body[0]}:**\n"
            f"   The mass remains exactly **{m_val} kg** because mass is an intrinsic property of matter that does not change with location."
        )
        marking = (
            "• 2 marks: Clear distinction between mass (amount of matter, kg) [1] and weight (gravitational force, N) [1]\n"
            f"• 2 marks: Weight on Earth calculation: W = mg [1], {w_earth} N [1]\n"
            f"• 2 marks: Weight on {chosen_body[0]} calculation: W = mg [1], {w_target} N [1]\n"
            f"• 1 mark: Invariant mass ({m_val} kg) correctly stated [1]\n"
            "**Total: 7 marks**"
        )
        return _normalize_res({
            "title": f"Mass vs Weight & Gravity: {chosen_body[0]}",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 3,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Mass is measured in kilograms (kg) and never changes with location.",
                "Weight is a force measured in Newtons (N) using the formula W = m × g.",
                f"On {chosen_body[0]}, multiply {m_val} kg by {chosen_body[1]} N/kg to find weight in Newtons.",
            ],
            "misconception_tags": ["mass_changes_on_the_moon_myth", "weight_measured_in_kilograms_error"],
            "learning_objective_id": "NS9.EC.13.02",
        })

    # Subskill 3: Magnetic Field and Poles
    if chosen_subskill == "magnetic_field_and_poles":
        materials = [
            ("Iron nail", True, "Ferromagnetic material strongly attracted by magnetic fields"),
            ("Copper wire", False, "Non-magnetic metal that is not attracted to magnets"),
            ("Aluminium foil", False, "Non-magnetic metal that is not attracted to magnets"),
            ("Cobalt strip", True, "Ferromagnetic element attracted to magnetic poles"),
            ("Plastic ruler", False, "Non-magnetic polymer insulator"),
            ("Nickel coin / strip", True, "Ferromagnetic metal attracted to magnets"),
        ]
        subset = materials[actual_seed % len(materials)]
        question_text = (
            "A bar magnet is surrounded by an invisible region of magnetic influence called a magnetic field.\n\n"
            "1. State the fundamental **Law of Magnetic Poles** regarding attraction and repulsion.\n"
            "2. State the standard **direction of magnetic field lines** outside a permanent bar magnet (from which pole to which pole).\n"
            "3. Name the **three main ferromagnetic metals** that are strongly attracted to permanent magnets.\n"
            "4. Describe how a learner can experimentally visualize the continuous magnetic field line pattern around a bar magnet using iron filings."
        )
        sample = (
            "1. **Law of Magnetic Poles:** Like magnetic poles repel each other (North repels North, South repels South); opposite magnetic poles attract each other (North attracts South);\n"
            "2. **Field Line Direction:** Outside a magnet, field lines always point **from the North pole (N) to the South pole (S)**;\n"
            "3. **Ferromagnetic Metals:** **Iron (Fe)**, **Nickel (Ni)**, and **Cobalt (Co)** (and alloys such as steel);\n"
            "4. **Visualization Experiment:**\n"
            "   • Place a bar magnet flat on a clean table and lay a stiff sheet of paper or plastic overhead transparency smoothly over it;\n"
            "   • Gently sprinkle fine iron filings uniformly across the paper;\n"
            "   • Lightly tap the paper; the iron filings align along the magnetic field flux lines, clustering most densely at the two poles where the field is strongest."
        )
        marking = (
            "• 1 mark: Like poles repel, opposite poles attract [1]\n"
            "• 1 mark: Field lines directed North to South [1]\n"
            "• 2 marks: Ferromagnetic metals named (Iron, Nickel, Cobalt) [2]\n"
            "• 2 marks: Experimental procedure with sheet over magnet [1], sprinkling filings and tapping to reveal dense pole pattern [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Magnetic Fields, Poles & Ferromagnetic Materials",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 3,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Like poles repel (N-N or S-S); unlike poles attract (N-S).",
                "Field lines run from North to South outside the magnet.",
                "The three ferromagnetic elements are iron, nickel, and cobalt. Iron filings align along field lines.",
            ],
            "misconception_tags": ["all_metals_are_magnetic_myth", "magnetic_field_lines_cross_over_myth"],
            "learning_objective_id": "NS9.EC.13.03",
        })

    # Subskill 4: Electrostatic Forces and Charging
    if chosen_subskill == "electrostatic_forces_and_charging":
        charging_pairs = [
            ("Perspex rod rubbed with a silk cloth", "loses electrons to the silk cloth", "positively charged", "negatively charged"),
            ("Plastic ruler rubbed with a woollen duster", "gains electrons from the wool", "negatively charged", "positively charged"),
            ("Inflated balloon rubbed against human hair", "gains electrons from the hair", "negatively charged", "positively charged"),
        ]
        ch = charging_pairs[actual_seed % len(charging_pairs)]
        question_text = (
            "Electrostatics involves the behaviour of stationary electric charges accumulated on surfaces.\n\n"
            f"Consider the experimental scenario: **{ch[0]}**.\n\n"
            "1. Explain the **subatomic mechanism** of electrostatic charging: Which subatomic particles move during friction, and which remain stationary?\n"
            f"2. During this friction, the rod/object {ch[1]}. Deduce whether the rubbed object becomes **positively charged** or **negatively charged**.\n"
            "3. State the **Law of Electrostatic Charges** regarding attraction and repulsion.\n"
            "4. Why does an electrostatically charged balloon stick to a neutral plastered wall?"
        )
        sample = (
            "1. **Subatomic Mechanism:** Only **electrons** (which reside in outer atomic orbitals) are mobile and transferred between materials by friction. "
            "**Protons** are tightly bound within heavy atomic nuclei and remain completely stationary;\n"
            f"2. **Charge Deduction:** The object becomes **{ch[2]}** (and the rubbing material becomes {ch[3]});\n"
            "3. **Law of Charges:** Like charges repel each other (positive repels positive, negative repels negative); opposite charges attract each other (positive attracts negative);\n"
            "4. **Attraction to Neutral Wall (Induction):** The charged balloon brings its electric field near the neutral wall, repelling electrons in the wall surface deeper inward. "
            "This leaves an induced opposite charge on the surface of the wall, causing an electrostatic force of attraction between the balloon and the wall."
        )
        marking = (
            "• 2 marks: Electrons are transferred [1], protons remain stationary in nuclei [1]\n"
            f"• 1 mark: Correct charge sign ({ch[2]}) [1]\n"
            "• 1 mark: Like charges repel, unlike attract [1]\n"
            "• 2 marks: Charge polarization / induction explanation on neutral wall [2]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Electrostatic Charging & Subatomic Electron Transfer",
            "topic": TOPIC_NAME,
            "grade": "9",
            "term": 3,
            "subskill": chosen_subskill,
            "question_type": "structured",
            "prompt": question_text,
            "question": question_text,
            "sample_answer": sample,
            "marking_guide": marking,
            "hints": [
                "Protons NEVER move during rubbing. Only negative electrons transfer.",
                "Gaining electrons gives a negative charge; losing electrons leaves an excess positive charge.",
                "A charged object attracts a neutral wall by inducing opposite charges on the surface.",
            ],
            "misconception_tags": ["protons_move_during_electrostatic_rubbing_myth", "neutral_objects_have_no_charges_myth"],
            "learning_objective_id": "NS9.EC.13.04",
        })

    # Subskill 5: Atmospheric Electrostatics and Lightning
    question_text = (
        "Lightning is a colossal, high-voltage electrostatic discharge occurring in Earth's atmosphere during severe thunderstorms.\n\n"
        "1. Describe how clouds become electrostatically charged during a thunderstorm.\n"
        "2. Explain what occurs at the moment a **lightning bolt** strikes between a thundercloud and the ground.\n"
        "3. Explain the scientific function of a **lightning conductor** (metal rod) installed on the roof of a thatched house or tall building.\n"
        "4. List **three vital personal safety rules** that a person must follow when caught outdoors in an open field during a severe lightning storm."
    )
    sample = (
        "1. **Cloud Charging Mechanism:** Vigorous convection currents inside cumulonimbus clouds cause turbulent collisions between rising water droplets and falling ice particles (graupel). "
        "Frictional rubbing transfers electrons, causing negative charges to accumulate at the bottom of the cloud and positive charges at the cloud top;\n"
        "2. **Lightning Discharge:** The concentrated negative charge at the cloud base repels electrons in the ground, inducing a strong positive charge on the Earth's surface. "
        "When the electrostatic potential difference exceeds the breakdown dielectric strength of air, a massive discharge of electrons surges along an ionized plasma channel, releasing blinding light, thunder, and extreme heat;\n"
        "3. **Lightning Conductor Function:** A thick copper rod extends above the roofline connected directly to a heavy copper strap anchored deep into damp earth. "
        "It provides a dedicated **low-resistance earthing path**, safely channeling lightning current directly into the ground without setting fire to thatched roof materials or shocking occupants;\n"
        "4. **Outdoor Safety Rules:**\n"
        "   • Never shelter under isolated tall trees or near metal fences/poles;\n"
        "   • Avoid open bodies of water (lakes, dams, swimming pools);\n"
        "   • If stranded in an open field, crouch down low on the balls of your feet with feet close together (minimize contact area and ground potential difference), with hands over ears; never lie flat on the ground."
    )
    marking = (
        "• 1 mark: Frictional collisions between ice and water droplets in clouds [1]\n"
        "• 2 marks: Massive electron discharge between charged cloud and induced ground [1], dielectric breakdown of air [1]\n"
        "• 2 marks: Low-resistance earthing path to earth [1], prevents structural fires/damage [1]\n"
        "• 2 marks: Two valid safety rules (avoid tall trees/water [1], crouch low with feet together, don't lie flat [1])\n"
        "**Total: 7 marks**"
    )
    return _normalize_res({
        "title": "Lightning: Atmospheric Electrostatic Discharge & Safety",
        "topic": TOPIC_NAME,
        "grade": "9",
        "term": 3,
        "subskill": chosen_subskill,
        "question_type": "structured",
        "prompt": question_text,
        "question": question_text,
        "sample_answer": sample,
        "marking_guide": marking,
        "hints": [
            "Colliding water droplets and ice particles charge storm clouds through friction.",
            "Lightning is a massive spark discharge when the electric field breaks down air.",
            "Lightning conductors safely guide huge currents into the ground. Never stand under isolated trees during storms.",
        ],
        "misconception_tags": ["lightning_never_strikes_the_same_place_twice_myth", "lying_flat_in_a_storm_is_safe_myth"],
        "learning_objective_id": "NS9.EC.13.05",
    })
