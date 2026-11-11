"""Natural Sciences Grade 9 Term 3: Safety with Electricity Generator.

Fully grounded in:
- curriculum_docs_auto/NaturalSciences_Gr9/Term 3/04. Safety with electricity.md
- curriculum_docs_auto/NaturalSciences_Gr9/Syllabus.md

Ordered Curriculum Subskills:
1. three_pin_plug_wiring_and_color_codes: Standard 3-pin plug wiring (Brown Live, Blue Neutral, Green/Yellow Earth), cord clamp.
2. fuse_operation_and_current_rating: Fuse mechanics, low melting point alloy wire, placement on Live line, rating selection.
3. circuit_breakers_and_earth_leakage: MCB trip mechanisms and Earth Leakage (RCD/ELCB) differential current shock prevention.
4. earthing_principle_and_shock_prevention: Earthing metal casings, low-resistance ground path, double insulation.
5. domestic_hazards_and_illegal_connections: Multi-plug overloading, frayed cables, water contact, and illegal connections hazards.
"""

from __future__ import annotations

import random
from hashlib import sha256
from typing import Any, Dict, List, Optional

TOPIC_NAME = "Safety with electricity"
ORDERED_SUBSKILLS = [
    "three_pin_plug_wiring_and_color_codes",
    "fuse_operation_and_current_rating",
    "circuit_breakers_and_earth_leakage",
    "earthing_principle_and_shock_prevention",
    "domestic_hazards_and_illegal_connections",
]


def _make_ref(seed: int, key: str, index: int) -> str:
    raw = f"{seed}_{key}_{index}_ns9_sfe"
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

    # Subskill 1: Three-Pin Plug Wiring and Color Codes
    if chosen_subskill == "three_pin_plug_wiring_and_color_codes":
        question_text = (
            "A standard South African domestic 3-pin plug (Type M, 16 A / 250 V) connects electrical appliances safely to the mains.\n\n"
            "1. Complete the standard electrical wiring color code specification:\n"
            "   • (a) **Live wire (L):** State insulation colour and which pin it connects to (Left, Right, or Top).\n"
            "   • (b) **Neutral wire (N):** State insulation colour and which pin it connects to (Left, Right, or Top).\n"
            "   • (c) **Earth wire (E):** State insulation colour and which pin it connects to (Left, Right, or Top).\n"
            "2. Explain why the **Earth pin** is physically longer and thicker than the Live and Neutral pins.\n"
            "3. State the purpose of the **cable clamp / cord grip** at the base of the plug."
        )
        sample = (
            "1. **3-Pin Plug Wiring Standard:**\n"
            "   • (a) **Live (L):** **Brown** insulation; connects to the **Right pin**;\n"
            "   • (b) **Neutral (N):** **Blue** insulation; connects to the **Left pin**;\n"
            "   • (c) **Earth (E):** **Green and Yellow stripes**; connects to the **Top large pin**;\n"
            "2. **Longer Earth Pin Function:** The longer Earth pin makes contact with the ground circuit first before the Live pin connects (providing immediate shock protection), "
            "and physically pushes open the child-safety shutters inside the wall socket to allow the other two pins to enter;\n"
            "3. **Cable Clamp Purpose:** Securely grips the outer insulated plastic cable sheath (not the individual coloured wires), "
            "ensuring that if the cord is tugged or tripped over, mechanical tension does not pull the copper wires loose from their terminal screw pins."
        )
        marking = (
            "• 3 marks: Live (Brown, Right) [1], Neutral (Blue, Left) [1], Earth (Green/Yellow, Top) [1]\n"
            "• 2 marks: Earth pin connects first for protection [1], opens wall socket safety shutters [1]\n"
            "• 1 mark: Cable clamp grips outer sheath to prevent wires pulling loose under strain [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Three-Pin Plug Wiring: Standards & Color Codes",
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
                "Brown = Live (Right, carries 230 V).",
                "Blue = Neutral (Left, completes circuit).",
                "Green and Yellow stripes = Earth (Top, safety grounding).",
            ],
            "misconception_tags": ["blue_is_live_wire_myth", "earth_wire_is_optional_myth"],
            "learning_objective_id": "NS9.EC.17.01",
        })

    # Subskill 2: Fuse Operation and Current Rating
    if chosen_subskill == "fuse_operation_and_current_rating":
        appliances = [
            ("Desk study lamp (rating: 60 W, drawing 0.26 A at 230 V)", [1, 3, 5, 13], 3, "A 3 A fuse provides safe headroom above 0.26 A while blowing quickly during a short circuit"),
            ("Electric kettle (rating: 2200 W, drawing 9.57 A at 230 V)", [3, 5, 10, 13], 13, "A 13 A fuse safely tolerates the 9.57 A running current while preventing fire from overcurrent"),
            ("Television set (rating: 150 W, drawing 0.65 A at 230 V)", [1, 3, 5, 13], 3, "A 3 A fuse provides reliable protection above 0.65 A"),
            ("Microwave oven (rating: 1200 W, drawing 5.22 A at 230 V)", [3, 5, 7, 13], 7, "A 7 A fuse safely accommodates 5.22 A without false blowing"),
        ]
        app_name, avail_fuses, chosen_fuse, reason = appliances[actual_seed % len(appliances)]
        fuses_str = ", ".join([f"{f} A" for f in avail_fuses])

        question_text = (
            "A fuse is a safety device engineered to protect domestic circuits and appliances from fire.\n\n"
            "1. Describe the internal construction of a standard cartridge fuse and explain how it operates when an electrical fault occurs.\n"
            f"2. An appliance, **{app_name}**, requires a fuse. Available fuse ratings are: **{fuses_str}**.\n"
            f"   Select the most appropriate fuse rating: *{chosen_fuse} A*.\n"
            f"3. Justify your selection: Explain why choosing a fuse with a rating that is too small or too large is hazardous: *{reason}*.\n"
            "4. Why must a fuse always be installed along the **Live wire** rather than the Neutral wire?"
        )
        sample = (
            "1. **Fuse Construction & Operation:** A cartridge fuse contains a thin wire made of an alloy with a **low melting point**. "
            "When current exceeds the fuse's rated capacity, excessive electrical energy converts into heat (P = I²R), causing the thin wire to melt and vaporize instantly ('blow'). "
            "This breaks the circuit, stopping all current before wires can overheat and ignite a fire;\n"
            f"2. **Selected Fuse Rating:** **{chosen_fuse} A**;\n"
            f"3. **Justification:** {reason}. If the fuse is too small (e.g. 1 A), it will blow under normal operating current; "
            "if the fuse is too large (e.g. 30 A), a dangerous fault current could overheat the wiring and cause a fire before the fuse ever melts;\n"
            "4. **Live Wire Placement:** The Live wire carries high potential (230 V). If the fuse is on the Live wire, when it blows, it isolates the appliance completely from high voltage. "
            "If placed on the Neutral wire, the fuse blowing would still leave the entire internal appliance live at 230 V, creating an electrocution hazard."
        )
        marking = (
            "• 2 marks: Low melting point thin wire [1], melts when current exceeds rating to break circuit [1]\n"
            f"• 1 mark: Correct fuse rating selected ({chosen_fuse} A) [1]\n"
            f"• 2 marks: Valid justification (too small blows nuisance [1], too large allows fire [1])\n"
            "• 1 mark: Live wire placement isolates appliance from high 230 V potential [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": f"Fuse Mechanics & Rating Selection: {app_name.split(' (')[0]}",
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
                "A fuse has a thin wire that melts when current is too high.",
                "Choose a fuse rating just slightly above the normal operating current.",
                "Always put the fuse on the LIVE wire so blowing it disconnects high voltage.",
            ],
            "misconception_tags": ["fuse_can_be_replaced_with_a_nail_myth", "fuse_slows_down_electricity_myth"],
            "learning_objective_id": "NS9.EC.17.02",
        })

    # Subskill 3: Circuit Breakers and Earth Leakage
    if chosen_subskill == "circuit_breakers_and_earth_leakage":
        question_text = (
            "In modern distribution boards (DB boards), electromechanical safety switches have largely replaced traditional disposable fuses.\n\n"
            "1. Explain how a **Miniature Circuit Breaker (MCB)** operates, and state **two significant advantages** it has over a disposable fuse.\n"
            "2. Explain the function of an **Earth Leakage Circuit Breaker (ELCB / RCD - Residual Current Device)**.\n"
            "3. State how an Earth Leakage unit detects that an electric shock is occurring to a person.\n"
            "4. What is the standard tripping threshold current (in milliamperes, mA) and response time of an Earth Leakage safety switch?"
        )
        sample = (
            "1. **MCB Operation & Advantages:** An MCB uses an electromagnet (for immediate magnetic trip during sudden short circuits) "
            "and a bimetallic strip (for thermal trip during gradual overload). When excessive current flows, the switch trips open automatically.\n"
            "   • **Advantages:** Can be reset immediately with a toggle switch once the fault is cleared (no need to replace burnt wire); faster and more precise tripping response;\n"
            "2. **Earth Leakage Function:** Specifically engineered to **protect human lives from fatal electrocution** by monitoring whether any electrical current is leaking to earth through a person's body;\n"
            "3. **Leakage Detection Principle:** It compares the current entering through the Live wire against the current returning through the Neutral wire. "
            "Under normal conditions, I_live = I_neutral. If a person touches a bare wire, some current leaks through their body into the ground, causing an imbalance (I_live > I_neutral);\n"
            "4. **Tripping Threshold & Speed:** Trips at a tiny leakage difference of just **30 mA (0.03 A)** within **less than 30 milliseconds (0.03 seconds)**, cutting off current before ventricular fibrillation of the human heart can occur."
        )
        marking = (
            "• 2 marks: MCB operation (electromagnet/bimetallic strip) [1], easily reset by switch [1]\n"
            "• 1 mark: ELCB protects human life from fatal shock [1]\n"
            "• 2 marks: Monitors balance between Live and Neutral currents [1], detects leakage current diverted through human to ground [1]\n"
            "• 1 mark: Trips at 30 mA in under 30 ms [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Circuit Breakers & Earth Leakage (RCD) Human Protection",
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
                "Circuit breakers can be flipped back on without replacing wire.",
                "Earth Leakage monitors the difference between Live and Neutral currents.",
                "If current leaks into a person to the ground, it trips in 30 milliseconds at 30 mA.",
            ],
            "misconception_tags": ["circuit_breakers_and_earth_leakage_are_the_same_thing_myth", "fuses_protect_against_electric_shock_myth"],
            "learning_objective_id": "NS9.EC.17.03",
        })

    # Subskill 4: Earthing Principle and Shock Prevention
    if chosen_subskill == "earthing_principle_and_shock_prevention":
        question_text = (
            "Appliances with conductive metal casings, such as electric kettles, washing machines, and toasters, rely on the earthing system for user protection.\n\n"
            "1. Describe where the **Earth wire** inside an appliance is physically connected.\n"
            "2. Explain step-by-step how the Earth wire and fuse work together to protect a person when an internal fault occurs (e.g. a loose 230 V live wire touches the metal chassis).\n"
            "3. What would happen to a person who touches the metal kettle if there were **no Earth wire** connected during this fault?\n"
            "4. Some modern appliances (such as plastic hair dryers and drills) only have a two-pin plug with no Earth wire. "
            "Explain what **double insulation** means and identify its safety symbol."
        )
        sample = (
            "1. **Earth Wire Connection:** The green/yellow striped Earth wire is bolted directly to the **outer metal conductive casing/chassis** of the appliance;\n"
            "2. **Protection Sequence During Fault:**\n"
            "   • If a live wire comes loose and touches the metal casing, high voltage is transferred to the chassis;\n"
            "   • The Earth wire provides a path of **extremely low electrical resistance** directly from the chassis into the ground;\n"
            "   • A massive surge of current immediately rushes through the Live wire and Earth wire into the ground (I = V/R_earth);\n"
            "   • This colossal surge instantly exceeds the fuse rating or MCB threshold, **blowing the fuse or tripping the breaker in milliseconds**, completely disconnecting the live power;\n"
            "3. **Absence of Earth Wire Hazard:** The metal casing would remain energized at 230 V. The moment a person touches the kettle, current would travel through their body into the floor to ground, causing severe electrical shock or fatal electrocution;\n"
            "4. **Double Insulation:** The appliance is constructed with two independent layers of electrical insulation (e.g. internal insulated wiring enclosed inside an outer non-conductive plastic casing), ensuring live wires can never make contact with external touchable surfaces. Its symbol is a **square inside a square**."
        )
        marking = (
            "• 1 mark: Connected to metal casing/chassis [1]\n"
            "• 2 marks: Low-resistance path to earth causes massive current surge [1], blows fuse/trips breaker immediately [1]\n"
            "• 1 mark: Without earth, person touching metal gets shocked/electrocuted [1]\n"
            "• 2 marks: Double insulation (two insulating layers/plastic casing) [1], square within square symbol [1]\n"
            "**Total: 6 marks**"
        )
        return _normalize_res({
            "title": "Earthing System Mechanics & Double Insulation",
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
                "The earth wire is attached to the metal body of the appliance.",
                "If live touches the metal body, current rushes down the earth wire, blowing the fuse instantly.",
                "Double insulated tools have plastic bodies and use the square-inside-a-square symbol.",
            ],
            "misconception_tags": ["earth_wire_carries_electricity_during_normal_use_myth", "plastic_appliances_need_earthing_myth"],
            "learning_objective_id": "NS9.EC.17.04",
        })

    # Subskill 5: Domestic Hazards and Illegal Connections
    question_text = (
        "Electrical safety violations cause thousands of domestic fires and fatal injuries each year.\n\n"
        "1. Explain the severe fire hazard caused by **overloading an electrical wall socket** with multiple multi-plug adaptors connecting high-power appliances (heaters, kettles, irons).\n"
        "2. Explain why using electrical appliances with **wet hands** or near a bathtub increases the risk of lethal electric shock by several orders of magnitude.\n"
        "3. Describe the severe community dangers of **illegal electrical connections ('izinyoka')** commonly found in informal settlements.\n"
        "4. State **two precautions** home dwellers must observe regarding damaged or frayed appliance power cords."
    )
    sample = (
        "1. **Overloading Socket Hazard:** Sockets and extension cords connect adaptors in **parallel**. Each additional appliance draws its own operating current, causing total current to sum (I_total = I₁ + I₂ + I₃). "
        "Excessive current causes intense thermal heating in wall wires (heating power P = I²R). The plastic insulation melts and catches fire inside wall cavities;\n"
        "2. **Wet Hands Hazard:** Dry human skin has a high electrical resistance (around 100 000 Ω), restricting current to safe levels. "
        "Water (especially containing dissolved skin salts) drastically drops skin resistance to under 1 000 Ω. According to Ohm's Law (I = V/R), this 100-fold reduction in resistance allows a massive, lethal current to surge across the heart, causing cardiac arrest;\n"
        "3. **Illegal Connections Hazards:** Unqualified individuals tap into overhead lines using uninsulated, low-hanging scrap wire lying across wet pathways or corrugated iron shacks without fuses or earthing. "
        "Children and pets stepping on exposed wires are fatally electrocuted, overloaded transformers explode, and corrugated iron shanties ignite uncontrollably;\n"
        "4. **Damaged Cord Precautions:**\n"
        "   • Never repair cracked or frayed cords with temporary insulation tape; replace the entire cord or discard the appliance;\n"
        "   • Never run cords under heavy carpets where foot traffic can abrade insulation unseen."
    )
    marking = (
        "• 2 marks: Parallel currents sum causing excessive I²R heating in wires [1], melting insulation and igniting fires [1]\n"
        "• 2 marks: Water drops skin resistance dramatically [1], allowing lethal current to surge across heart (I = V/R) [1]\n"
        "• 2 marks: Uninsulated wires on ground cause fatal electrocution of children/pedestrians [1], shack fires and transformer explosions [1]\n"
        "• 1 mark: Replace cord rather than tape, don't run under carpets [1]\n"
        "**Total: 7 marks**"
    )
    return _normalize_res({
        "title": "Domestic Electrical Hazards & Illegal Connections Safety",
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
            "Overloading draws too much current in parallel, causing wires to overheat (P = I²R).",
            "Water lowers skin resistance, allowing dangerous amounts of current to pass through the body.",
            "Illegal connections lack fuses and earth wires, leaving exposed live wires on the ground.",
        ],
        "misconception_tags": ["insulation_tape_is_permanent_cord_fix_myth", "voltage_kills_not_current_myth"],
        "learning_objective_id": "NS9.EC.17.05",
    })
