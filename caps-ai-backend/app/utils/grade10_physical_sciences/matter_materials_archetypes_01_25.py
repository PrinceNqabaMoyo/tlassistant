"""Grade 10 Physical Sciences — Matter and Materials Archetypes 01–25.
Grounded in curriculum_docs_auto/PhysicalSciences_Gr10/:
- Term 1: Classification of matter, The atom, The periodic table, Chemical bonding.
- Term 2: The particles that substances are made of.
- Term 4: The hydrosphere, Units of measurement applied.

100% Aligned with South African National Curriculum Standards.
Complies strictly with 6-Pillar Generator Contract.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "Classification of matter"
SUBJECT = "Physical Sciences"
GRADE = "10"


def _fmt_sa(val: float | int, decimals: int = 2) -> str:
    """Format decimal numbers using South African comma decimal separator."""
    if isinstance(val, int) or val == int(val):
        return str(int(val))
    s = f"{val:.{decimals}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _make_meta(
    subskill: str,
    weight: int = 15,
    duration: int = 4,
    misconceptions: Optional[List[str]] = None,
    criteria: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    return {
        "term": 1,
        "caps_weight_percent": weight,
        "suggested_duration_mins": duration,
        "mode": f"elementary_{subskill}",
        "topic": TOPIC,
        "subject": SUBJECT,
        "grade": GRADE,
        "subskill": subskill,
        "misconception_tags": misconceptions or ["conceptual_matter_misconception"],
        "marking_schema": {
            "total_marks": sum(c.get("marks", 1) for c in (criteria or [{"criterion": "Accurate answer", "marks": 2}])),
            "criteria": criteria or [{"criterion": "Accurate scientific reasoning and value", "marks": 2}],
        },
    }


# --------------------------------------------------------------------------- #
# 01_classify_substance_element_compound_mixture
# --------------------------------------------------------------------------- #
def _build_01_classify_substance_element_compound_mixture(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    substances = [
        {"name": "Pure copper wire", "formula": "\\text{Cu}", "type": "an element", "reason": "it consists of only one type of atom with atomic number 29"},
        {"name": "Distilled water", "formula": "\\text{H}_2\\text{O}", "type": "a compound", "reason": "it consists of two or more elements chemically bonded in a fixed ratio"},
        {"name": "Table salt dissolved in water", "formula": "\\text{NaCl(aq)}", "type": "a homogeneous mixture (solution)", "reason": "it has a uniform composition throughout and can be separated by physical means"},
        {"name": "Dry air", "formula": "\\text{N}_2, \\text{O}_2, \\text{Ar}, \\text{CO}_2", "type": "a homogeneous mixture", "reason": "it consists of gases physically mixed in varying proportions"},
        {"name": "Iron filings mixed with sulfur powder", "formula": "\\text{Fe + S}", "type": "a heterogeneous mixture", "reason": "the individual substances retain their chemical identities and can be separated magnetically"},
        {"name": "Pure sucrose crystals", "formula": "\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}", "type": "a compound", "reason": "it consists of carbon, hydrogen, and oxygen atoms chemically bonded in a definite proportion"},
        {"name": "Argon gas in an incandescent bulb", "formula": "\\text{Ar}", "type": "an element", "reason": "it consists of single monatomic atoms that cannot be broken down chemically into simpler substances"},
        {"name": "Brass alloy used in musical instruments", "formula": "\\text{Cu-Zn alloy}", "type": "a homogeneous mixture (solid solution / alloy)", "reason": "it consists of copper and zinc melted together without a fixed chemical stoichiometric formula"},
    ]
    sub = r.choice(substances)
    prompt = (
        f"\\text{{Classify the following substance as an element, a compound, or a mixture: }}\n\n"
        f"\\textbf{{{sub['name']}}} ({sub['formula']}).\n\n"
        f"\\text{{Provide a clear scientific reason for your classification.}}"
    )
    ans = f"It is {sub['type']}. Scientific reason: {sub['reason']}."
    q = {
        "id": f"mat10_01_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 2,
        "explanation": f"{sub['name']} is classified as {sub['type']} because {sub['reason']}.",
        "hints": {
            "tier_1": "Elements have one type of atom; compounds have chemically bonded elements; mixtures can be separated physically.",
            "tier_2": "Check whether the formula represents a single atom type, a fixed chemical molecule, or physical blending.",
            "tier_3": f"{sub['name']} is {sub['type']}.",
        },
    }
    q.update(_make_meta("01_classify_substance_element_compound_mixture", 15, 3, ["confuses_compound_with_homogeneous_mixture"]))
    return q


# --------------------------------------------------------------------------- #
# 02_homogeneous_vs_heterogeneous_mixtures
# --------------------------------------------------------------------------- #
def _build_02_homogeneous_vs_heterogeneous_mixtures(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    examples = [
        {"name": "Muddy river water from the Tugela River", "kind": "heterogeneous mixture", "phase": "two distinct phases (suspended solid silt particles and liquid water)", "optical": "exhibits the Tyndall effect and settles upon standing"},
        {"name": "Clear filtered apple juice", "kind": "homogeneous mixture", "phase": "a single uniform liquid phase throughout", "optical": "uniform optical transmission without visible particle boundaries"},
        {"name": "Granite rock sample from the Drakensberg", "kind": "heterogeneous mixture", "phase": "distinct crystalline phases of quartz, feldspar, and mica visible to the naked eye", "optical": "non-uniform composition across different regions"},
        {"name": "Household white vinegar (5% ethanoic acid in water)", "kind": "homogeneous mixture", "phase": "a single uniform liquid solution phase", "optical": "solute particles are dispersed at the molecular scale"},
        {"name": "A salad dressing of olive oil and balsamic vinegar", "kind": "heterogeneous mixture", "phase": "two immiscible liquid layers with a clearly visible meniscus boundary", "optical": "distinct phase boundaries exist between the non-polar oil and polar aqueous vinegar"},
    ]
    item = r.choice(examples)
    prompt = (
        f"\\text{{A learner analyzes a sample of }} \\textbf{{{item['name']}}}.\n\n"
        f"\\text{{1. State whether this sample is a }} \\textbf{{homogeneous}} \\text{{ or }} \\textbf{{heterogeneous}} \\text{{ mixture.}}\n"
        f"\\text{{2. Explain your classification in terms of visible phases and uniformity of composition.}}"
    )
    ans = f"1. {item['kind']}. 2. It has {item['phase']}, meaning {item['optical']}."
    q = {
        "id": f"mat10_02_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"A homogeneous mixture has a single uniform phase throughout. A heterogeneous mixture has distinct boundaries or visible phases. {item['name']} is {item['kind']}.",
        "hints": {
            "tier_1": "Can you see distinct boundaries or layers, or is the appearance completely uniform down to the microscopic scale?",
            "tier_2": "Homogeneous = uniform single phase. Heterogeneous = two or more distinct phases.",
            "tier_3": f"This sample is a {item['kind']}.",
        },
    }
    q.update(_make_meta("02_homogeneous_vs_heterogeneous_mixtures", 15, 3, ["thinks_cloudy_liquid_is_homogeneous"]))
    return q


# --------------------------------------------------------------------------- #
# 03_separation_techniques_filtration_distillation_chromatography
# --------------------------------------------------------------------------- #
def _build_03_separation_techniques_filtration_distillation_chromatography(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    scenarios = [
        {"mixture": "Ethanol (boiling point 78 °C) and water (boiling point 100 °C)", "technique": "Fractional distillation", "property": "difference in boiling points of the miscible liquids"},
        {"mixture": "Fine sand and aqueous copper(II) sulfate solution", "technique": "Filtration followed by crystallization / evaporation", "property": "difference in solubility and particle size (sand is insoluble, CuSO4 is dissolved)"},
        {"mixture": "Iron filings and table salt (NaCl) crystals", "technique": "Magnetic separation (or dissolving salt in water and filtration)", "property": "difference in ferromagnetic properties of iron versus diamagnetic salt"},
        {"mixture": "Black ink containing multiple water-soluble synthetic dyes", "technique": "Paper chromatography", "property": "differences in adsorption onto the stationary paper phase and solubility in the mobile solvent phase"},
        {"mixture": "Crude petroleum oil containing petrol, diesel, kerosene, and bitumen", "technique": "Fractional distillation in a fractionating column", "property": "differences in boiling points resulting from differing hydrocarbon molecular chain lengths"},
        {"mixture": "Sodium chloride recovered from seawater", "technique": "Solar evaporation or simple distillation to collect both pure water and solid salt", "property": "water is volatile while sodium chloride has a very high boiling point (non-volatile solute)"},
    ]
    sc = r.choice(scenarios)
    prompt = (
        f"\\text{{In an analytical chemistry laboratory, a technician must separate the components of:}}\n\n"
        f"\\textbf{{{sc['mixture']}}}.\n\n"
        f"\\text{{1. Identify the most suitable physical separation technique.}}\n"
        f"\\text{{2. State the key physical property difference upon which this separation is based.}}"
    )
    ans = f"1. {sc['technique']}. 2. Based on {sc['property']}."
    q = {
        "id": f"mat10_03_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"The appropriate technique is {sc['technique']}, which exploits the {sc['property']}.",
        "hints": {
            "tier_1": "Consider whether the components differ in boiling point, particle size, magnetic attraction, or chromatographic solubility.",
            "tier_2": "Miscible liquids with different boiling points are separated by distillation; insoluble solids by filtration.",
            "tier_3": f"Technique: {sc['technique']}.",
        },
    }
    q.update(_make_meta("03_separation_techniques_filtration_distillation_chromatography", 15, 3, ["confuses_filtration_with_distillation"]))
    return q


# --------------------------------------------------------------------------- #
# 04_states_of_matter_kinetic_molecular_theory_properties
# --------------------------------------------------------------------------- #
def _build_04_states_of_matter_kinetic_molecular_theory_properties(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    states = [
        {"state": "solid", "shape": "fixed definite shape", "volume": "fixed definite volume", "particles": "closely packed in an orderly fixed lattice with minimal spaces", "motion": "vibrate about fixed equilibrium positions", "kmt": "intermolecular forces are very strong and thermal kinetic energy is low"},
        {"state": "liquid", "shape": "takes the shape of the container", "volume": "fixed definite volume", "particles": "closely spaced but disorderly without a fixed lattice", "motion": "slide and rotate past one another with translational freedom", "kmt": "intermolecular forces are strong enough to maintain constant volume but allow fluidity"},
        {"state": "gas", "shape": "expands to fill the entire container", "volume": "indefinite volume (highly compressible)", "particles": "widely separated with vast intermolecular empty spaces", "motion": "rapid, continuous, random straight-line motion undergoing elastic collisions", "kmt": "kinetic energy far overcomes negligible intermolecular forces"},
    ]
    st = r.choice(states)
    temp_c = r.choice([-15, 20, 85, 120, 250])
    prompt = (
        f"\\text{{According to the Kinetic Molecular Theory (KMT) of matter, describe the microscopic behavior of a substance in the }} "
        f"\\textbf{{{st['state']}}} \\text{{ state at }} {temp_c}^\\circ\\text{{C:}}\n\n"
        f"\\text{{1. Describe the arrangement and spacing of the particles.}}\n"
        f"\\text{{2. Describe the motion of the particles.}}\n"
        f"\\text{{3. Explain how the relative strength of intermolecular forces compares to the average kinetic energy of the particles.}}"
    )
    ans = f"1. Particles are {st['particles']}. 2. Particles {st['motion']}. 3. {st['kmt']}."
    q = {
        "id": f"mat10_04_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"In a {st['state']}: particles are {st['particles']}, move by {st['motion']}, and {st['kmt']}.",
        "hints": {
            "tier_1": "Recall the 3 pillars of KMT: particle arrangement, particle movement, and intermolecular forces.",
            "tier_2": "Solids vibrate in fixed positions; liquids slide past one another; gases move rapidly in straight lines.",
            "tier_3": f"State is {st['state']}: {st['particles']}.",
        },
    }
    q.update(_make_meta("04_states_of_matter_kinetic_molecular_theory_properties", 15, 3, ["believes_particles_expand_when_heated"]))
    return q


# --------------------------------------------------------------------------- #
# 05_heating_cooling_curve_phase_transitions_latent_heat_svg
# --------------------------------------------------------------------------- #
def _build_05_heating_cooling_curve_phase_transitions_latent_heat_svg(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    substance_choices = [
        {"name": "Water", "mp": 0, "bp": 100, "t_start": -20, "t_end": 120},
        {"name": "Ethanol", "mp": -114, "bp": 78, "t_start": -130, "t_end": 95},
        {"name": "Benzene", "mp": 5.5, "bp": 80.1, "t_start": -10, "t_end": 100},
        {"name": "Naphthalene", "mp": 80.2, "bp": 218, "t_start": 25, "t_end": 240},
    ]
    sub = r.choice(substance_choices)
    mp_str = _fmt_sa(sub["mp"])
    bp_str = _fmt_sa(sub["bp"])

    # Create dynamic heating curve SVG
    svg = f"""<svg viewBox="0 0 500 280" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- Heating curve for {sub['name']} -->
  <line x1="60" y1="240" x2="460" y2="240" stroke="#0F172A" stroke-width="2" />
  <line x1="60" y1="240" x2="60" y2="30" stroke="#0F172A" stroke-width="2" />
  <text x="460" y="260" font-size="12" fill="#0F172A" text-anchor="end">Time (min)</text>
  <text x="50" y="25" font-size="12" fill="#0F172A" text-anchor="middle">Temp (°C)</text>

  <!-- Curve segments: AB solid, BC melting, CD liquid, DE boiling, EF gas -->
  <polyline points="70,225 130,170 210,170 290,90 380,90 440,45" fill="none" stroke="#2563EB" stroke-width="3" />

  <!-- Dotted plateau levels -->
  <line x1="60" y1="170" x2="210" y2="170" stroke="#94A3B8" stroke-dasharray="4,4" />
  <line x1="60" y1="90" x2="380" y2="90" stroke="#94A3B8" stroke-dasharray="4,4" />

  <!-- Y-axis labels -->
  <text x="50" y="174" font-size="11" fill="#1E293B" text-anchor="end">{mp_str}°C</text>
  <text x="50" y="94" font-size="11" fill="#1E293B" text-anchor="end">{bp_str}°C</text>

  <!-- Segment annotations -->
  <circle cx="100" cy="197" r="3" fill="#DC2626" /><text x="95" y="190" font-size="11" fill="#DC2626">A-B</text>
  <circle cx="170" cy="170" r="3" fill="#DC2626" /><text x="165" y="160" font-size="11" fill="#DC2626" font-weight="bold">B-C (Plateau 1)</text>
  <circle cx="250" cy="130" r="3" fill="#DC2626" /><text x="245" y="125" font-size="11" fill="#DC2626">C-D</text>
  <circle cx="335" cy="90" r="3" fill="#DC2626" /><text x="330" y="80" font-size="11" fill="#DC2626" font-weight="bold">D-E (Plateau 2)</text>
  <circle cx="410" cy="67" r="3" fill="#DC2626" /><text x="405" y="60" font-size="11" fill="#DC2626">E-F</text>
</svg>"""

    prompt = (
        f"\\text{{Refer to the heating curve graph for pure }} \\textbf{{{sub['name']}}} \\text{{ heated uniformly at constant pressure:}}\n\n"
        f"\\text{{1. Identify the physical process occurring along the horizontal plateau }} \\textbf{{B-C}}.\n"
        f"\\text{{2. State what happens to the temperature and the average kinetic energy of particles along region }} \\textbf{{B-C}}.\n"
        f"\\text{{3. Explain why heat energy is absorbed along }} \\textbf{{B-C}} \\text{{ without any increase in temperature.}}"
    )
    ans = (
        f"1. Melting (fusion from solid to liquid) at {mp_str} °C. "
        f"2. Temperature and average kinetic energy remain constant. "
        f"3. Absorbed thermal energy is latent heat of fusion, used to weaken and break intermolecular bonds rather than increasing kinetic energy."
    )
    q = {
        "id": f"mat10_05_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"Along horizontal plateaus B-C and D-E, phase transitions occur at constant temperature ({mp_str} °C and {bp_str} °C). The heat added overcomes intermolecular forces (latent heat) without increasing average kinetic energy ($T$).",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Along horizontal plateaus of a heating curve, the temperature does not rise despite continuous heating.",
            "tier_2": "Temperature measures average kinetic energy. If T is constant, Ek is constant, and energy goes into potential energy (overcoming bonds).",
            "tier_3": f"B-C represents melting at {mp_str} °C. Heat is latent heat of fusion.",
        },
    }
    q.update(_make_meta("05_heating_cooling_curve_phase_transitions_latent_heat_svg", 15, 4, ["believes_kinetic_energy_increases_during_melting"]))
    return q


# --------------------------------------------------------------------------- #
# 06_microscopic_particle_representation_phases_svg
# --------------------------------------------------------------------------- #
def _build_06_microscopic_particle_representation_phases_svg(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    phase_pairs = [
        ("Solid to Liquid", "Melting / Fusion", "regular lattice breaking into free-flowing particles", "#3B82F6", "substance A (ice to water)"),
        ("Liquid to Gas", "Evaporation / Boiling", "particles overcoming intermolecular forces to become widely spaced", "#10B981", "substance B (water to steam)"),
        ("Gas to Liquid", "Condensation", "gas particles losing kinetic energy and clustering into liquid droplets", "#8B5CF6", "substance C (water vapor to dew)"),
        ("Solid to Gas", "Sublimation", "solid particles directly breaking free into gaseous phase", "#F59E0B", "substance D (dry ice CO2)"),
    ]
    pair = r.choice(phase_pairs)
    title, proc, desc, col, sample_name = pair

    # Generate 2-box comparison SVG showing microscopic particles
    svg = f"""<svg viewBox="0 0 460 200" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
  <!-- Microscopic particle model: {title} for {sample_name} -->
  <!-- Box 1 -->
  <rect x="30" y="30" width="160" height="130" fill="#F8FAFC" stroke="#334155" stroke-width="2" rx="4" />
  <text x="110" y="180" font-size="12" fill="#0F172A" text-anchor="middle" font-weight="bold">State 1</text>
  <circle cx="70" cy="70" r="10" fill="{col}" opacity="0.8" />
  <circle cx="95" cy="70" r="10" fill="{col}" opacity="0.8" />
  <circle cx="120" cy="70" r="10" fill="{col}" opacity="0.8" />
  <circle cx="145" cy="70" r="10" fill="{col}" opacity="0.8" />
  <circle cx="70" cy="95" r="10" fill="{col}" opacity="0.8" />
  <circle cx="95" cy="95" r="10" fill="{col}" opacity="0.8" />
  <circle cx="120" cy="95" r="10" fill="{col}" opacity="0.8" />
  <circle cx="145" cy="95" r="10" fill="{col}" opacity="0.8" />
  <circle cx="70" cy="120" r="10" fill="{col}" opacity="0.8" />
  <circle cx="95" cy="120" r="10" fill="{col}" opacity="0.8" />
  <circle cx="120" cy="120" r="10" fill="{col}" opacity="0.8" />
  <circle cx="145" cy="120" r="10" fill="{col}" opacity="0.8" />

  <!-- Transition Arrow -->
  <line x1="210" y1="95" x2="250" y2="95" stroke="#E11D48" stroke-width="3" />
  <polygon points="250,90 260,95 250,100" fill="#E11D48" />
  <text x="235" y="85" font-size="11" fill="#E11D48" text-anchor="middle">+ Energy</text>

  <!-- Box 2 -->
  <rect x="270" y="30" width="160" height="130" fill="#F8FAFC" stroke="#334155" stroke-width="2" rx="4" />
  <text x="350" y="180" font-size="12" fill="#0F172A" text-anchor="middle" font-weight="bold">State 2</text>
  <circle cx="310" cy="120" r="10" fill="{col}" opacity="0.8" />
  <circle cx="335" cy="135" r="10" fill="{col}" opacity="0.8" />
  <circle cx="360" cy="118" r="10" fill="{col}" opacity="0.8" />
  <circle cx="385" cy="130" r="10" fill="{col}" opacity="0.8" />
  <circle cx="320" cy="85" r="10" fill="{col}" opacity="0.8" />
  <circle cx="350" cy="95" r="10" fill="{col}" opacity="0.8" />
  <circle cx="380" cy="75" r="10" fill="{col}" opacity="0.8" />
  <circle cx="330" cy="55" r="10" fill="{col}" opacity="0.8" />
</svg>"""

    prompt = (
        f"\\text{{Refer to the microscopic sub-microscopic particle model diagrams for {sample_name} transitioning from State 1 to State 2:}}\n\n"
        f"\\text{{1. Identify the states of matter represented in State 1 and State 2.}}\n"
        f"\\text{{2. Name the physical phase transition process ({proc}) represented by this model.}}\n"
        f"\\text{{3. Contrast the intermolecular distance and order between the two states.}}"
    )
    ans = f"1. State 1 is a solid; State 2 is a liquid. 2. Melting (fusion). 3. In State 1 particles are in a regular packed lattice with minimal spaces; in State 2 particles are disorderly with freedom to slide past one another."
    q = {
        "id": f"mat10_06_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"State 1 depicts a tightly packed, orderly crystalline lattice (solid). State 2 depicts random close packing with fluidity (liquid). The transition is melting.",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Look at the order and spacing in State 1 versus State 2.",
            "tier_2": "State 1 has an orderly grid (solid); State 2 is disordered but still at the bottom (liquid).",
            "tier_3": "State 1 is solid, State 2 is liquid; process is melting.",
        },
    }
    q.update(_make_meta("06_microscopic_particle_representation_phases_svg", 15, 3, ["misidentifies_liquid_as_gas"]))
    return q


# --------------------------------------------------------------------------- #
# 07_atomic_number_mass_number_subatomic_particles
# --------------------------------------------------------------------------- #
def _build_07_atomic_number_mass_number_subatomic_particles(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    elements = [
        {"name": "Sodium", "sym": "\\text{Na}", "z": 11, "a": 23, "charge": 0},
        {"name": "Aluminum", "sym": "\\text{Al}", "z": 13, "a": 27, "charge": 3},
        {"name": "Chlorine", "sym": "\\text{Cl}", "z": 17, "a": 35, "charge": -1},
        {"name": "Oxygen", "sym": "\\text{O}", "z": 8, "a": 16, "charge": -2},
        {"name": "Magnesium", "sym": "\\text{Mg}", "z": 12, "a": 24, "charge": 2},
        {"name": "Phosphorus", "sym": "\\text{P}", "z": 15, "a": 31, "charge": 0},
        {"name": "Potassium", "sym": "\\text{K}", "z": 19, "a": 39, "charge": 1},
        {"name": "Calcium", "sym": "\\text{Ca}", "z": 20, "a": 40, "charge": 2},
    ]
    el = r.choice(elements)
    protons = el["z"]
    neutrons = el["a"] - el["z"]
    electrons = el["z"] - el["charge"]
    ch_str = f"^{{{el['charge']}+}}" if el["charge"] > 0 else (f"^{{{abs(el['charge'])}-}}" if el["charge"] < 0 else "")
    nuclide_latex = f"_{{{el['z']}}}^{{{el['a']}}}{el['sym']}{ch_str}"

    prompt = (
        f"\\text{{Consider the chemical species represented in nuclide notation as: }} {nuclide_latex}.\n\n"
        f"\\text{{Determine:}}\n"
        f"\\text{{1. The atomic number (Z).}}\n"
        f"\\text{{2. The mass number (A).}}\n"
        f"\\text{{3. The number of protons, neutrons, and electrons in this species.}}"
    )
    ans = f"1. Z = {el['z']}; 2. A = {el['a']}; 3. Protons = {protons}, Neutrons = {neutrons}, Electrons = {electrons}."
    q = {
        "id": f"mat10_07_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"In nuclide notation $^{{A}}_{{Z}}X^{{q}}$: atomic number Z = {el['z']} gives protons ({protons}). Neutrons = A - Z = {el['a']} - {el['z']} = {neutrons}. Electrons = Z - charge = {el['z']} - ({el['charge']}) = {electrons}.",
        "hints": {
            "tier_1": "Subscript is atomic number Z (protons); superscript is mass number A (protons + neutrons).",
            "tier_2": "Neutrons = A - Z. If there is a charge q, electrons = protons - q.",
            "tier_3": f"p = {protons}, n = {neutrons}, e = {electrons}.",
        },
    }
    q.update(_make_meta("07_atomic_number_mass_number_subatomic_particles", 15, 3, ["subtracts_electrons_for_negative_ion"]))
    return q


# --------------------------------------------------------------------------- #
# 08_isotope_notation_and_subatomic_composition
# --------------------------------------------------------------------------- #
def _build_08_isotope_notation_and_subatomic_composition(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    isotopes_data = [
        {"elem": "Carbon", "sym": "\\text{C}", "z": 6, "a1": 12, "a2": 14},
        {"elem": "Chlorine", "sym": "\\text{Cl}", "z": 17, "a1": 35, "a2": 37},
        {"elem": "Uranium", "sym": "\\text{U}", "z": 92, "a1": 235, "a2": 238},
        {"elem": "Hydrogen", "sym": "\\text{H}", "z": 1, "a1": 1, "a2": 2},
    ]
    iso = r.choice(isotopes_data)
    n1 = iso["a1"] - iso["z"]
    n2 = iso["a2"] - iso["z"]

    prompt = (
        f"\\text{{Two naturally occurring isotopes of {iso['elem']} are represented as: }}\n\n"
        f"_{{{iso['z']}}}^{{{iso['a1']}}}{iso['sym']} \\quad \\text{{and}} \\quad _{{{iso['z']}}}^{{{iso['a2']}}}{iso['sym']}.\n\n"
        f"\\text{{1. Define the term }} \\textbf{{isotopes}}.\n"
        f"\\text{{2. State what characteristic of the nucleus is identical for both isotopes.}}\n"
        f"\\text{{3. State how many neutrons each isotope possesses.}}\n"
        f"\\text{{4. Explain why both isotopes exhibit identical chemical properties.}}"
    )
    ans = (
        f"1. Isotopes are atoms of the same element having the same number of protons (same atomic number) but different numbers of neutrons (different mass numbers). "
        f"2. Number of protons (Z = {iso['z']}). "
        f"3. {iso['elem']}-{iso['a1']} has {n1} neutrons; {iso['elem']}-{iso['a2']} has {n2} neutrons. "
        f"4. Chemical properties are determined by electron configuration (valence electrons), which is identical in both neutral isotopes."
    )
    q = {
        "id": f"mat10_08_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 5,
        "explanation": f"Isotopes have identical atomic numbers (Z = {iso['z']} protons) and identical electron clouds, giving identical chemical properties, but differ in neutron counts ({n1} vs {n2}).",
        "hints": {
            "tier_1": "Recall: Iso = same, tope = place in periodic table (same atomic number).",
            "tier_2": "Chemical reactions depend on valence electrons, not the mass of the nucleus.",
            "tier_3": f"Neutrons: A - Z = {iso['a1']} - {iso['z']} = {n1}, and {iso['a2']} - {iso['z']} = {n2}.",
        },
    }
    q.update(_make_meta("08_isotope_notation_and_subatomic_composition", 15, 4, ["believes_isotopes_have_different_chemical_properties"]))
    return q


# --------------------------------------------------------------------------- #
# 09_relative_atomic_mass_from_isotopic_abundance
# --------------------------------------------------------------------------- #
def _build_09_relative_atomic_mass_from_isotopic_abundance(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    elements = [
        {"name": "Chlorine", "sym": "\\text{Cl}", "iso1": (35, 75.78), "iso2": (37, 24.22), "known": 35.45},
        {"name": "Copper", "sym": "\\text{Cu}", "iso1": (63, 69.17), "iso2": (65, 30.83), "known": 63.55},
        {"name": "Gallium", "sym": "\\text{Ga}", "iso1": (69, 60.11), "iso2": (71, 39.89), "known": 69.72},
        {"name": "Bromine", "sym": "\\text{Br}", "iso1": (79, 50.69), "iso2": (81, 49.31), "known": 79.90},
        {"name": "Silver", "sym": "\\text{Ag}", "iso1": (107, 51.84), "iso2": (109, 48.16), "known": 107.87},
    ]
    el = r.choice(elements)
    m1, p1 = el["iso1"]
    m2, p2 = el["iso2"]
    ram = round((m1 * p1 + m2 * p2) / 100.0, 2)
    p1_str = _fmt_sa(p1, 2)
    p2_str = _fmt_sa(p2, 2)
    ram_str = _fmt_sa(ram, 2)

    prompt = (
        f"\\text{{Naturally occurring {el['name']} consists of two stable isotopes:}}\n\n"
        f"\\bullet\\; ^{{{m1}}}{el['sym']} \\text{{ with an abundance of }} {p1_str}\\%\n\n"
        f"\\bullet\\; ^{{{m2}}}{el['sym']} \\text{{ with an abundance of }} {p2_str}\\%\n\n"
        f"\\text{{Calculate the relative atomic mass (RAM) of {el['name']}. Show all your working to 2 decimal places.}}"
    )
    ans = f"RAM = ({m1} \\times {p1_str} + {m2} \\times {p2_str}) / 100 = {ram_str} amu"
    q = {
        "id": f"mat10_09_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"RAM is the weighted average mass: $\\text{{RAM}} = \\dfrac{{({m1} \\times {p1_str}) + ({m2} \\times {p2_str})}}{{100}} = \\dfrac{{{_fmt_sa(m1*p1, 2)} + {_fmt_sa(m2*p2, 2)}}}{{100}} = {ram_str}$.",
        "hints": {
            "tier_1": "Use the formula: RAM = [(mass1 * %1) + (mass2 * %2)] / 100.",
            "tier_2": f"Multiply {m1} by {p1_str}, and {m2} by {p2_str}, add the products and divide by 100.",
            "tier_3": f"RAM = {ram_str} amu.",
        },
    }
    q.update(_make_meta("09_relative_atomic_mass_from_isotopic_abundance", 15, 3, ["divides_by_two_instead_of_one_hundred"]))
    return q


# --------------------------------------------------------------------------- #
# 10_mass_spectrometry_isotope_peaks_calculation
# --------------------------------------------------------------------------- #
def _build_10_mass_spectrometry_isotope_peaks_calculation(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    # 3-isotope elements: e.g. Magnesium (24: 79%, 25: 10%, 26: 11%) or Neon (20: 90.48%, 21: 0.27%, 22: 9.25%)
    scenarios = [
        {"elem": "Magnesium", "sym": "\\text{Mg}", "peaks": [(24, 78.99), (25, 10.00), (26, 11.01)]},
        {"elem": "Silicon", "sym": "\\text{Si}", "peaks": [(28, 92.23), (29, 4.67), (30, 3.10)]},
        {"elem": "Neon", "sym": "\\text{Ne}", "peaks": [(20, 90.48), (21, 0.27), (22, 9.25)]},
    ]
    sc = r.choice(scenarios)
    peaks = sc["peaks"]
    ram_calc = round(sum(m * p for m, p in peaks) / 100.0, 2)
    ram_str = _fmt_sa(ram_calc, 2)

    peaks_desc = ", ".join([f"m/z = {m} (intensity {_fmt_sa(p, 2)}\\%)" for m, p in peaks])
    prompt = (
        f"\\text{{A mass spectrum of a purified gaseous sample of {sc['elem']} reveals three distinct isotopic mass peaks:}}\n\n"
        f"\\text{{{peaks_desc}}}.\n\n"
        f"\\text{{1. Explain what the m/z ratio represents in a mass spectrometer.}}\n"
        f"\\text{{2. Calculate the relative atomic mass of {sc['elem']} from the mass spectrum data.}}"
    )
    ans = f"1. m/z represents the mass-to-charge ratio of the ion (where z = +1 usually). 2. RAM = {ram_str} amu."
    q = {
        "id": f"mat10_10_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"m/z is mass to charge ratio. RAM = $\\sum(\\text{{mass}} \\times \\%) / 100 = {ram_str}$.",
        "hints": {
            "tier_1": "Multiply each isotopic mass by its respective relative percentage intensity and sum them.",
            "tier_2": "Divide the total sum by 100 to get the weighted atomic mass.",
            "tier_3": f"RAM = {ram_str} amu.",
        },
    }
    q.update(_make_meta("10_mass_spectrometry_isotope_peaks_calculation", 15, 4, ["confuses_peak_height_with_atomic_number"]))
    return q


# --------------------------------------------------------------------------- #
# 11_bohr_model_energy_levels_quantum_shells
# --------------------------------------------------------------------------- #
def _build_11_bohr_model_energy_levels_quantum_shells(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    elements = [
        {"name": "Sodium", "z": 11, "shells": [2, 8, 1], "valence": 1, "period": 3},
        {"name": "Oxygen", "z": 8, "shells": [2, 6], "valence": 6, "period": 2},
        {"name": "Chlorine", "z": 17, "shells": [2, 8, 7], "valence": 7, "period": 3},
        {"name": "Calcium", "z": 20, "shells": [2, 8, 8, 2], "valence": 2, "period": 4},
        {"name": "Silicon", "z": 14, "shells": [2, 8, 4], "valence": 4, "period": 3},
        {"name": "Fluorine", "z": 9, "shells": [2, 7], "valence": 7, "period": 2},
    ]
    el = r.choice(elements)
    sh_str = ")(".join(str(s) for s in el["shells"])
    sh_format = f"2,{','.join(str(s) for s in el['shells'][1:])}"

    prompt = (
        f"\\text{{In the Bohr atomic model, electrons occupy discrete principal energy levels (shells }} n = 1, 2, 3, \\dots\\text{{).}}\n\n"
        f"\\text{{For a neutral atom of }} \\textbf{{{el['name']}}} \\text{{ (atomic number Z = {el['z']}):}}\n"
        f"\\text{{1. Write down the electron configuration in shell notation (e.g. 2,8,...).}}\n"
        f"\\text{{2. State the number of occupied principal energy levels (shells).}}\n"
        f"\\text{{3. State the number of valence electrons.}}"
    )
    ans = f"1. {sh_format}; 2. {len(el['shells'])} occupied shells (Period {el['period']}); 3. {el['valence']} valence electrons."
    q = {
        "id": f"mat10_11_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"{el['name']} has Z = {el['z']} electrons filling shells as: {sh_format}. It has {len(el['shells'])} shells and {el['valence']} valence electrons.",
        "hints": {
            "tier_1": "Maximum shell capacities: n=1 holds 2, n=2 holds 8, n=3 holds 8 (for Grade 10).",
            "tier_2": "The outermost occupied shell holds the valence electrons.",
            "tier_3": f"Configuration is {sh_format}.",
        },
    }
    q.update(_make_meta("11_bohr_model_energy_levels_quantum_shells", 15, 3, ["overfills_first_shell_beyond_two"]))
    return q


# --------------------------------------------------------------------------- #
# 12_sp_electron_configuration_notation_elements_1_to_20
# --------------------------------------------------------------------------- #
def _build_12_sp_electron_configuration_notation_elements_1_to_20(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    configs = [
        {"name": "Carbon", "z": 6, "sp": "1s^2\\; 2s^2\\; 2p^2", "noble": "[\\text{He}]\\; 2s^2\\; 2p^2"},
        {"name": "Nitrogen", "z": 7, "sp": "1s^2\\; 2s^2\\; 2p^3", "noble": "[\\text{He}]\\; 2s^2\\; 2p^3"},
        {"name": "Sodium", "z": 11, "sp": "1s^2\\; 2s^2\\; 2p^6\\; 3s^1", "noble": "[\\text{Ne}]\\; 3s^1"},
        {"name": "Magnesium", "z": 12, "sp": "1s^2\\; 2s^2\\; 2p^6\\; 3s^2", "noble": "[\\text{Ne}]\\; 3s^2"},
        {"name": "Aluminum", "z": 13, "sp": "1s^2\\; 2s^2\\; 2p^6\\; 3s^2\\; 3p^1", "noble": "[\\text{Ne}]\\; 3s^2\\; 3p^1"},
        {"name": "Phosphorus", "z": 15, "sp": "1s^2\\; 2s^2\\; 2p^6\\; 3s^2\\; 3p^3", "noble": "[\\text{Ne}]\\; 3s^2\\; 3p^3"},
        {"name": "Sulfur", "z": 16, "sp": "1s^2\\; 2s^2\\; 2p^6\\; 3s^2\\; 3p^4", "noble": "[\\text{Ne}]\\; 3s^2\\; 3p^4"},
        {"name": "Chlorine", "z": 17, "sp": "1s^2\\; 2s^2\\; 2p^6\\; 3s^2\\; 3p^5", "noble": "[\\text{Ne}]\\; 3s^2\\; 3p^5"},
        {"name": "Argon", "z": 18, "sp": "1s^2\\; 2s^2\\; 2p^6\\; 3s^2\\; 3p^6", "noble": "[\\text{Ne}]\\; 3s^2\\; 3p^6"},
        {"name": "Potassium", "z": 19, "sp": "1s^2\\; 2s^2\\; 2p^6\\; 3s^2\\; 3p^6\\; 4s^1", "noble": "[\\text{Ar}]\\; 4s^1"},
        {"name": "Calcium", "z": 20, "sp": "1s^2\\; 2s^2\\; 2p^6\\; 3s^2\\; 3p^6\\; 4s^2", "noble": "[\\text{Ar}]\\; 4s^2"},
    ]
    cfg = r.choice(configs)
    prompt = (
        f"\\text{{Write down the ground-state }} \\textbf{{sp-electron configuration}} \\text{{ for a neutral atom of }} "
        f"\\textbf{{{cfg['name']}}} \\text{{ (atomic number Z = {cfg['z']}):}}\n\n"
        f"\\text{{1. In full spectroscopic notation.}}\n"
        f"\\text{{2. In condensed noble gas core notation.}}"
    )
    ans = f"1. {cfg['sp']}. 2. {cfg['noble']}."
    q = {
        "id": f"mat10_12_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"{cfg['name']} (Z = {cfg['z']}) has configuration: {cfg['sp']} or {cfg['noble']}.",
        "hints": {
            "tier_1": "Subshell filling order: 1s, 2s, 2p, 3s, 3p, 4s.",
            "tier_2": "s holds up to 2 electrons; p holds up to 6 electrons.",
            "tier_3": f"Full notation: {cfg['sp']}.",
        },
    }
    q.update(_make_meta("12_sp_electron_configuration_notation_elements_1_to_20", 15, 3, ["fills_3d_before_4s_in_first_20_elements"]))
    return q


# --------------------------------------------------------------------------- #
# 13_aufbau_diagram_orbital_box_representation_svg
# --------------------------------------------------------------------------- #
def _build_13_aufbau_diagram_orbital_box_representation_svg(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    elements = [
        {"name": "Carbon", "z": 6, "p_unpaired": 2, "box_2p": ["↑", "↑", ""]},
        {"name": "Nitrogen", "z": 7, "p_unpaired": 3, "box_2p": ["↑", "↑", "↑"]},
        {"name": "Oxygen", "z": 8, "p_unpaired": 2, "box_2p": ["↑↓", "↑", "↑"]},
        {"name": "Fluorine", "z": 9, "p_unpaired": 1, "box_2p": ["↑↓", "↑↓", "↑"]},
    ]
    el = r.choice(elements)

    # Build Aufbau energy ladder diagram in SVG
    svg = f"""<svg viewBox="0 0 460 220" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
  <!-- Aufbau diagram for {el['name']} (Z={el['z']}) -->
  <!-- Energy axis -->
  <line x1="40" y1="200" x2="40" y2="30" stroke="#0F172A" stroke-width="2" />
  <polygon points="35,30 40,20 45,30" fill="#0F172A" />
  <text x="35" y="18" font-size="11" fill="#0F172A" text-anchor="middle">Energy</text>

  <!-- 1s level -->
  <rect x="70" y="170" width="30" height="25" fill="#F1F5F9" stroke="#1E293B" stroke-width="1.5" />
  <text x="85" y="188" font-size="14" fill="#0284C7" text-anchor="middle">↑↓</text>
  <text x="85" y="210" font-size="12" fill="#334155" text-anchor="middle">1s</text>

  <!-- 2s level -->
  <rect x="130" y="120" width="30" height="25" fill="#F1F5F9" stroke="#1E293B" stroke-width="1.5" />
  <text x="145" y="138" font-size="14" fill="#0284C7" text-anchor="middle">↑↓</text>
  <text x="145" y="160" font-size="12" fill="#334155" text-anchor="middle">2s</text>

  <!-- 2p level (3 boxes) -->
  <rect x="200" y="70" width="30" height="25" fill="#F1F5F9" stroke="#1E293B" stroke-width="1.5" />
  <text x="215" y="88" font-size="14" fill="#E11D48" text-anchor="middle">{el['box_2p'][0]}</text>
  <rect x="235" y="70" width="30" height="25" fill="#F1F5F9" stroke="#1E293B" stroke-width="1.5" />
  <text x="250" y="88" font-size="14" fill="#E11D48" text-anchor="middle">{el['box_2p'][1]}</text>
  <rect x="270" y="70" width="30" height="25" fill="#F1F5F9" stroke="#1E293B" stroke-width="1.5" />
  <text x="285" y="88" font-size="14" fill="#E11D48" text-anchor="middle">{el['box_2p'][2]}</text>
  <text x="250" y="110" font-size="12" fill="#334155" text-anchor="middle">2p</text>
</svg>"""

    prompt = (
        f"\\text{{Refer to the Aufbau energy level orbital box diagram for a neutral atom of }} \\textbf{{{el['name']}}} \\text{{ (Z = {el['z']}):}}\n\n"
        f"\\text{{1. State the }} \\textbf{{Aufbau principle}}.\n"
        f"\\text{{2. State how many unpaired electrons are present in the }} 2p \\text{{ subshell.}}\n"
        f"\\text{{3. Identify which rule or principle governs the individual occupation of the three }} 2p \\text{{ degenerate orbitals before pairing occurs.}}"
    )
    ans = (
        f"1. The Aufbau principle states that electrons fill orbitals of lowest available energy first before occupying higher energy levels. "
        f"2. {el['p_unpaired']} unpaired electron(s). "
        f"3. Hund's rule of maximum multiplicity."
    )
    q = {
        "id": f"mat10_13_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"Aufbau principle dictates lower orbitals (1s, 2s) fill first. Hund's rule states electrons singly occupy degenerate 2p orbitals with parallel spins before pairing. {el['name']} has {el['p_unpaired']} unpaired electrons.",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Aufbau = building up from lowest energy. Hund's rule = singly occupy before pairing.",
            "tier_2": "Count how many boxes have only one arrow in the 2p level.",
            "tier_3": f"{el['p_unpaired']} unpaired electron(s); governed by Hund's rule.",
        },
    }
    q.update(_make_meta("13_aufbau_diagram_orbital_box_representation_svg", 15, 3, ["pairs_electrons_in_p_before_singly_occupying"]))
    return q


# --------------------------------------------------------------------------- #
# 14_pauli_exclusion_principle_application
# --------------------------------------------------------------------------- #
def _build_14_pauli_exclusion_principle_application(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    examples = [
        {"name": "Helium (He)", "subshell": "1s", "z": 2},
        {"name": "Beryllium (Be)", "subshell": "2s", "z": 4},
        {"name": "Magnesium (Mg)", "subshell": "3s", "z": 12},
        {"name": "Calcium (Ca)", "subshell": "4s", "z": 20},
    ]
    ex = r.choice(examples)
    prompt = (
        f"\\text{{In a neutral atom of }} \\textbf{{{ex['name']}}} \\text{{ (atomic number Z = {ex['z']}), two electrons share the }} "
        f"{ex['subshell']} \\text{{ orbital:}}\n\n"
        f"\\text{{1. State the }} \\textbf{{Pauli Exclusion Principle}} \\text{{ as applied to electrons in an atom.}}\n"
        f"\\text{{2. Explain why the two electrons in the }} {ex['subshell']} \\text{{ orbital must have opposite spins (represented as }} \\uparrow\\downarrow\\text{{).}}"
    )
    ans = (
        f"1. The Pauli Exclusion Principle states that an orbital can hold a maximum of two electrons, provided they have opposite spins (or: no two electrons can have identical four quantum numbers). "
        f"2. For {ex['name']}, opposite spins create opposing magnetic moments, minimizing electrostatic repulsion and satisfying quantum exclusion."
    )
    q = {
        "id": f"mat10_14_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"Pauli Exclusion Principle limits the {ex['subshell']} orbital to 2 electrons with paired opposite spins ($\\uparrow\\downarrow$).",
        "hints": {
            "tier_1": "State the maximum number of electrons in an orbital and their spin requirement.",
            "tier_2": "Maximum of 2 electrons per orbital with opposite spins (m_s = +1/2 and -1/2).",
            "tier_3": "An orbital can hold at most two electrons, which must have opposite spins.",
        },
    }
    q.update(_make_meta("14_pauli_exclusion_principle_application", 15, 3, ["allows_two_electrons_with_same_spin_in_one_orbital"]))
    return q


# --------------------------------------------------------------------------- #
# 15_hunds_rule_orbital_filling_and_unpaired_electrons
# --------------------------------------------------------------------------- #
def _build_15_hunds_rule_orbital_filling_and_unpaired_electrons(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    elements = [
        {"name": "Nitrogen", "z": 7, "sp": "1s^2 2s^2 2p^3", "unpaired": 3, "reason": "each of the three 2p orbitals (2px, 2py, 2pz) holds one electron with parallel spin"},
        {"name": "Oxygen", "z": 8, "sp": "1s^2 2s^2 2p^4", "unpaired": 2, "reason": "one 2p orbital has a pair of electrons, while the other two 2p orbitals each hold one unpaired electron"},
        {"name": "Carbon", "z": 6, "sp": "1s^2 2s^2 2p^2", "unpaired": 2, "reason": "two 2p orbitals each contain one single electron with parallel spin, while one 2p orbital remains empty"},
        {"name": "Silicon", "z": 14, "sp": "1s^2 2s^2 2p^6 3s^2 3p^2", "unpaired": 2, "reason": "two 3p orbitals each hold one unpaired electron"},
        {"name": "Phosphorus", "z": 15, "sp": "1s^2 2s^2 2p^6 3s^2 3p^3", "unpaired": 3, "reason": "all three 3p orbitals are half-filled with one electron each"},
    ]
    el = r.choice(elements)
    prompt = (
        f"\\text{{1. State }} \\textbf{{Hund's Rule}}.\n\n"
        f"\\text{{2. For a neutral atom of }} \\textbf{{{el['name']}}} \\text{{ (Z = {el['z']}):}}\n"
        f"\\text{{a) Write down the number of unpaired electrons in the ground state.}}\n"
        f"\\text{{b) Explain your answer by referencing the filling of the }} p \\text{{ subshell.}}"
    )
    ans = (
        f"1. Hund's rule states that no pairing of electrons in orbitals of equal energy (degenerate orbitals) occurs until each orbital has one electron with parallel spin. "
        f"2. a) {el['unpaired']} unpaired electron(s). b) {el['reason']}."
    )
    q = {
        "id": f"mat10_15_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"Hund's rule dictates parallel spins in degenerate orbitals. For {el['name']}, there are {el['unpaired']} unpaired electrons because {el['reason']}.",
        "hints": {
            "tier_1": "Degenerate orbitals (like px, py, pz) must each get one electron before any pairing.",
            "tier_2": "Draw the 3 p-boxes and distribute the p-electrons singly first.",
            "tier_3": f"{el['unpaired']} unpaired electrons.",
        },
    }
    q.update(_make_meta("15_hunds_rule_orbital_filling_and_unpaired_electrons", 15, 3, ["pairs_electrons_prematurely"]))
    return q


# --------------------------------------------------------------------------- #
# 16_periodic_table_periods_groups_and_blocks
# --------------------------------------------------------------------------- #
def _build_16_periodic_table_periods_groups_and_blocks(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    elements = [
        {"name": "Sodium", "sym": "\\text{Na}", "z": 11, "period": 3, "group": 1, "block": "s-block", "family": "Alkali metals"},
        {"name": "Magnesium", "sym": "\\text{Mg}", "z": 12, "period": 3, "group": 2, "block": "s-block", "family": "Alkaline earth metals"},
        {"name": "Chlorine", "sym": "\\text{Cl}", "z": 17, "period": 3, "group": 17, "block": "p-block", "family": "Halogens"},
        {"name": "Argon", "sym": "\\text{Ar}", "z": 18, "period": 3, "group": 18, "block": "p-block", "family": "Noble gases"},
        {"name": "Oxygen", "sym": "\\text{O}", "z": 8, "period": 2, "group": 16, "block": "p-block", "family": "Chalcogens"},
        {"name": "Iron", "sym": "\\text{Fe}", "z": 26, "period": 4, "group": 8, "block": "d-block", "family": "Transition metals"},
    ]
    el = r.choice(elements)
    prompt = (
        f"\\text{{Identify the position and classification of the element }} \\textbf{{{el['name']}}} ({el['sym']}, Z = {el['z']}) "
        f"\\text{{ on the Periodic Table:}}\n\n"
        f"\\text{{1. The Period number.}}\n"
        f"\\text{{2. The Group number (IUPAC 1–18).}}\n"
        f"\\text{{3. The electronic block (s, p, d, or f).}}\n"
        f"\\text{{4. The chemical family name (e.g. Halogens, Alkali metals).}}"
    )
    ans = f"1. Period {el['period']}; 2. Group {el['group']}; 3. {el['block']}; 4. {el['family']}."
    q = {
        "id": f"mat10_16_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"{el['name']} is in Period {el['period']} (highest n = {el['period']}), Group {el['group']}, belongs to the {el['block']}, and is known as {el['family']}.",
        "hints": {
            "tier_1": "Period corresponds to highest principal quantum number n; Group corresponds to valence electron count.",
            "tier_2": "Groups 1-2 are s-block; Groups 13-18 are p-block; Groups 3-12 are d-block.",
            "tier_3": f"Period {el['period']}, Group {el['group']}, {el['block']}.",
        },
    }
    q.update(_make_meta("16_periodic_table_periods_groups_and_blocks", 15, 3, ["confuses_group_number_with_period_number"]))
    return q


# --------------------------------------------------------------------------- #
# 17_classification_metals_nonmetals_metalloids
# --------------------------------------------------------------------------- #
def _build_17_classification_metals_nonmetals_metalloids(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    elements = [
        {"name": "Silicon", "sym": "\\text{Si}", "type": "Metalloid (semi-metal)", "props": "lustrous appearance but brittle; acts as a semiconductor with electrical conductivity increasing with temperature"},
        {"name": "Copper", "sym": "\\text{Cu}", "type": "Metal", "props": "ductile, malleable, high thermal and electrical conductivity, high melting point"},
        {"name": "Sulfur", "sym": "\\text{S}", "type": "Non-metal", "props": "brittle yellow solid, poor electrical conductor (insulator), low melting point"},
        {"name": "Germanium", "sym": "\\text{Ge}", "type": "Metalloid (semi-metal)", "props": "intermediate electronic band gap, exhibits semi-metallic electrical conductivities"},
        {"name": "Bromine", "sym": "\\text{Br}", "type": "Non-metal", "props": "red-brown liquid at room temperature, forms covalent diatomic molecules, non-conductor"},
    ]
    el = r.choice(elements)
    prompt = (
        f"\\text{{The element }} \\textbf{{{el['name']}}} ({el['sym']}) \\text{{ is tested in a physical science laboratory.}}\n\n"
        f"\\text{{1. Classify this element as a }} \\textbf{{metal}}, \\textbf{{non-metal}}, \\text{{ or }} \\textbf{{metalloid (semi-metal)}}.\n"
        f"\\text{{2. State two characteristic physical properties that justify this classification.}}"
    )
    ans = f"1. {el['type']}. 2. Properties: {el['props']}."
    q = {
        "id": f"mat10_17_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"{el['name']} is classified as a {el['type']} because {el['props']}.",
        "hints": {
            "tier_1": "Metals conduct electricity well and are malleable; non-metals are insulators; metalloids have intermediate semiconductor properties.",
            "tier_2": "Boron, Silicon, Germanium, Arsenic, Antimony, Tellurium are metalloids along the dividing staircase.",
            "tier_3": f"{el['name']} is a {el['type']}.",
        },
    }
    q.update(_make_meta("17_classification_metals_nonmetals_metalloids", 15, 3, ["believes_all_shiny_elements_are_metals"]))
    return q


# --------------------------------------------------------------------------- #
# 18_valence_electrons_and_core_charge_deduction
# --------------------------------------------------------------------------- #
def _build_18_valence_electrons_and_core_charge_deduction(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    elements = [
        {"name": "Sodium", "sym": "\\text{Na}", "z": 11, "core": 10, "valence": 1, "eff_charge": 1},
        {"name": "Magnesium", "sym": "\\text{Mg}", "z": 12, "core": 10, "valence": 2, "eff_charge": 2},
        {"name": "Aluminum", "sym": "\\text{Al}", "z": 13, "core": 10, "valence": 3, "eff_charge": 3},
        {"name": "Phosphorus", "sym": "\\text{P}", "z": 15, "core": 10, "valence": 5, "eff_charge": 5},
        {"name": "Chlorine", "sym": "\\text{Cl}", "z": 17, "core": 10, "valence": 7, "eff_charge": 7},
    ]
    el = r.choice(elements)
    prompt = (
        f"\\text{{Core charge (effective nuclear charge approximation) is given by: }}\n\n"
        f"\\text{{Core Charge}} = \\text{{Atomic Number (Z)}} - \\text{{Number of Inner Core Electrons}}.\n\n"
        f"\\text{{For a neutral atom of }} \\textbf{{{el['name']}}} ({el['sym']}, Z = {el['z']}):\n"
        f"\\text{{1. State the number of inner core electrons.}}\n"
        f"\\text{{2. State the number of valence electrons.}}\n"
        f"\\text{{3. Calculate the core charge experienced by the valence electrons.}}"
    )
    ans = f"1. Core electrons = {el['core']}; 2. Valence electrons = {el['valence']}; 3. Core charge = {el['z']} - {el['core']} = +{el['eff_charge']}."
    q = {
        "id": f"mat10_18_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"{el['name']} has Z = {el['z']}, 10 inner core electrons (1s2 2s2 2p6), and {el['valence']} valence electrons. Core charge = {el['z']} - 10 = +{el['eff_charge']}.",
        "hints": {
            "tier_1": "Inner core electrons are all electrons in completed shells inside the valence shell.",
            "tier_2": "For Period 3 elements, the inner core is the 10 electrons of neon.",
            "tier_3": f"Core charge = +{el['eff_charge']}.",
        },
    }
    q.update(_make_meta("18_valence_electrons_and_core_charge_deduction", 15, 3, ["counts_valence_electrons_as_part_of_core"]))
    return q


# --------------------------------------------------------------------------- #
# 19_periodic_trend_atomic_radius_variation
# --------------------------------------------------------------------------- #
def _build_19_periodic_trend_atomic_radius_variation(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    trends = [
        {"dir": "across Period 3 from Sodium (Na) to Chlorine (Cl)", "trend": "decreases", "reason": "nuclear charge (number of protons) increases while electrons are added to the same principal energy shell (n=3), resulting in stronger electrostatic attraction pulling electrons closer to the nucleus"},
        {"dir": "down Group 1 from Lithium (Li) to Cesium (Cs)", "trend": "increases", "reason": "an additional principal electron shell is added with each successive period, increasing shielding by inner core electrons and placing valence electrons farther from the nucleus"},
        {"dir": "across Period 2 from Lithium (Li) to Fluorine (F)", "trend": "decreases", "reason": "effective nuclear charge increases across the period with no additional shielding shells, pulling valence electrons inwards"},
        {"dir": "down Group 17 from Fluorine (F) to Iodine (I)", "trend": "increases", "reason": "the number of occupied electron shells increases down the group, increasing the atomic radius"},
    ]
    t = r.choice(trends)
    prompt = (
        f"\\text{{Explain the periodic trend in }} \\textbf{{atomic radius}} \\text{{ as one moves }} \\textbf{{{t['dir']}}}.\n\n"
        f"\\text{{1. State whether atomic radius increases or decreases.}}\n"
        f"\\text{{2. Explain this trend in terms of nuclear charge, number of shells, and electron shielding.}}"
    )
    ans = f"1. It {t['trend']}. 2. Scientific explanation: {t['reason']}."
    q = {
        "id": f"mat10_19_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"Atomic radius {t['trend']} {t['dir']} because {t['reason']}.",
        "hints": {
            "tier_1": "Across a period: more protons pull same shell closer. Down a group: new shells added.",
            "tier_2": "Look at whether new shells are being added or whether nuclear charge is increasing in the same shell.",
            "tier_3": f"Trend: {t['trend']}.",
        },
    }
    q.update(_make_meta("19_periodic_trend_atomic_radius_variation", 15, 3, ["believes_radius_increases_across_a_period_due_to_more_electrons"]))
    return q


# --------------------------------------------------------------------------- #
# 20_periodic_trend_first_ionisation_energy
# --------------------------------------------------------------------------- #
def _build_20_periodic_trend_first_ionisation_energy(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    elements = [
        {"e1": "Sodium (Na, Group 1)", "e2": "Chlorine (Cl, Group 17)", "period": 3, "higher": "Chlorine", "reason": "Chlorine has a higher nuclear charge (+17 vs +11) and a smaller atomic radius in the same period, holding its valence electrons much more strongly"},
        {"e1": "Lithium (Li)", "e2": "Potassium (K)", "group": 1, "higher": "Lithium", "reason": "Lithium has fewer electron shells and a smaller atomic radius, so its valence electron experiences less shielding and is held more tightly by the nucleus"},
        {"e1": "Neon (Ne)", "e2": "Sodium (Na)", "higher": "Neon", "reason": "Neon has a stable octet in a smaller shell (n=2), whereas Sodium's valence electron is in a new outer shell (n=3) shielded by 10 core electrons"},
    ]
    el = r.choice(elements)
    prompt = (
        f"\\text{{1. Define the term }} \\textbf{{First Ionisation Energy}}.\n\n"
        f"\\text{{2. Between }} \\textbf{{{el['e1']}}} \\text{{ and }} \\textbf{{{el['e2']}}}, \\text{{ which element has the }} "
        f"\\textbf{{higher}} \\text{{ first ionisation energy?}}\n\n"
        f"\\text{{3. Justify your answer by referencing atomic radius and effective nuclear attraction.}}"
    )
    ans = (
        f"1. First ionisation energy is the energy required to remove the first electron from an isolated neutral atom in the gaseous state: X(g) + energy -> X+(g) + e-. "
        f"2. {el['higher']}. "
        f"3. {el['reason']}."
    )
    q = {
        "id": f"mat10_20_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"First ionisation energy definition: energy to remove 1 mol of electrons from 1 mol of gaseous atoms. {el['higher']} has higher ionisation energy because {el['reason']}.",
        "hints": {
            "tier_1": "Definition requires: energy to remove an electron from a neutral atom in the GASEOUS state.",
            "tier_2": "Smaller atoms with higher nuclear charge hold electrons more tightly and require more energy to ionize.",
            "tier_3": f"Higher: {el['higher']}.",
        },
    }
    q.update(_make_meta("20_periodic_trend_first_ionisation_energy", 15, 4, ["omits_gaseous_state_in_ionisation_definition"]))
    return q


# --------------------------------------------------------------------------- #
# 21_periodic_trend_electron_affinity_and_electronegativity
# --------------------------------------------------------------------------- #
def _build_21_periodic_trend_electron_affinity_and_electronegativity(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    pairs = [
        {"e1": "Fluorine (F)", "e2": "Lithium (Li)", "higher": "Fluorine", "prop": "Electronegativity", "val": 4.0},
        {"e1": "Oxygen (O)", "e2": "Nitrogen (N)", "higher": "Oxygen", "prop": "Electronegativity", "val": 3.5},
        {"e1": "Chlorine (Cl)", "e2": "Sodium (Na)", "higher": "Chlorine", "prop": "Electron Affinity", "val": -349},
    ]
    p = r.choice(pairs)
    prompt = (
        f"\\text{{1. Distinguish clearly between }} \\textbf{{electronegativity}} \\text{{ and }} \\textbf{{electron affinity}}.\n\n"
        f"\\text{{2. Between }} \\textbf{{{p['e1']}}} \\text{{ and }} \\textbf{{{p['e2']}}}, \\text{{ which element has the higher value for }} \\textbf{{{p['prop']}}}?\n\n"
        f"\\text{{3. State the general trend in electronegativity across a period from left to right.}}"
    )
    ans = (
        "1. Electronegativity is a measure of the tendency of an atom to attract a shared pair of electrons in a chemical bond. "
        "Electron affinity is the energy change that occurs when an electron is added to a neutral gaseous atom. "
        f"2. {p['higher']}. "
        "3. Electronegativity increases across a period from left to right."
    )
    q = {
        "id": f"mat10_21_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"Electronegativity applies to shared bonding electrons; electron affinity applies to isolated gaseous atoms. {p['higher']} is higher. Electronegativity increases across periods.",
        "hints": {
            "tier_1": "Electronegativity = shared bonding pair attraction; Electron affinity = adding an electron to gaseous atom.",
            "tier_2": "Non-metals (top right, e.g. Fluorine) have the highest electronegativity.",
            "tier_3": f"Higher: {p['higher']}.",
        },
    }
    q.update(_make_meta("21_periodic_trend_electron_affinity_and_electronegativity", 15, 4, ["confuses_electronegativity_with_electron_affinity"]))
    return q


# --------------------------------------------------------------------------- #
# 22_periodic_trends_graphical_analysis_svg
# --------------------------------------------------------------------------- #
def _build_22_periodic_trends_graphical_analysis_svg(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    # Plot of first ionization energy for elements Z=1 to 10
    # H: 1312, He: 2372, Li: 520, Be: 899, B: 801, C: 1086, N: 1402, O: 1314, F: 1681, Ne: 2081
    ie_data = [(1, 1312), (2, 2372), (3, 520), (4, 899), (5, 801), (6, 1086), (7, 1402), (8, 1314), (9, 1681), (10, 2081)]
    questions_pool = [
        (
            "Lithium (Z = 3) compared to Helium (Z = 2)",
            "Explain why there is a dramatic drop in ionisation energy from Helium (Z = 2) to Lithium (Z = 3).",
            "In Lithium (Z=3), the third electron enters a new principal quantum shell (n=2, 2s1) which is further from the nucleus and shielded by the two inner 1s electrons, requiring much less energy to remove."
        ),
        (
            "Nitrogen (Z = 7) compared to Oxygen (Z = 8)",
            "Explain why Nitrogen (Z = 7) has a slightly higher first ionisation energy than Oxygen (Z = 8), despite Oxygen having a greater nuclear charge.",
            "Nitrogen has a stable half-filled 2p subshell (2p3) where each orbital is singly occupied. Oxygen (2p4) has one paired orbital, resulting in electron-electron spin repulsion which makes it slightly easier to remove the fourth electron."
        ),
        (
            "Beryllium (Z = 4) compared to Boron (Z = 5)",
            "Explain why Beryllium (Z = 4) has a higher first ionisation energy than Boron (Z = 5).",
            "Beryllium has a completely filled, stable 2s subshell (2s2). In Boron (2s2 2p1), the fifth electron enters a higher-energy 2p subshell shielded by the 2s electrons, making it easier to remove."
        ),
        (
            "Neon (Z = 10) compared to all preceding elements in Period 2",
            "Explain why Neon (Z = 10) has the maximum first ionisation energy among all elements in Period 2.",
            "Neon has the highest effective nuclear charge (+8) and smallest atomic radius in Period 2, with a completely filled, exceptionally stable octet (2s2 2p6)."
        ),
    ]
    focus_topic, specific_q, specific_ans = r.choice(questions_pool)

    # Generate graph SVG
    svg = f"""<svg viewBox="0 0 480 240" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- First Ionization Energy vs Atomic Number (Z=1 to 10) Focus: {focus_topic} -->
  <line x1="50" y1="200" x2="450" y2="200" stroke="#0F172A" stroke-width="2" />
  <line x1="50" y1="200" x2="50" y2="20" stroke="#0F172A" stroke-width="2" />
  <text x="450" y="225" font-size="11" fill="#0F172A" text-anchor="end">Atomic Number (Z)</text>
  <text x="40" y="20" font-size="11" fill="#0F172A" text-anchor="middle">First IE (kJ/mol)</text>

  <!-- Polyline plotting points -->
  <polyline points="70,110 100,30 140,180 180,145 220,155 260,130 300,105 340,112 380,85 420,50" fill="none" stroke="#2563EB" stroke-width="2.5" />

  <!-- Data dots and labels -->
  <circle cx="70" cy="110" r="3" fill="#0F172A" /><text x="70" y="125" font-size="9" text-anchor="middle">1(H)</text>
  <circle cx="100" cy="30" r="4" fill="#16A34A" /><text x="100" y="25" font-size="10" text-anchor="middle" font-weight="bold">2(He)</text>
  <circle cx="140" cy="180" r="4" fill="#DC2626" /><text x="140" y="195" font-size="10" text-anchor="middle" font-weight="bold">3(Li)</text>
  <circle cx="300" cy="105" r="3" fill="#0F172A" /><text x="300" y="98" font-size="9" text-anchor="middle">7(N)</text>
  <circle cx="340" cy="112" r="3" fill="#0F172A" /><text x="340" y="127" font-size="9" text-anchor="middle">8(O)</text>
  <circle cx="420" cy="50" r="4" fill="#16A34A" /><text x="420" y="42" font-size="10" text-anchor="middle" font-weight="bold">10(Ne)</text>
</svg>"""

    prompt = (
        f"\\text{{Refer to the graph showing First Ionisation Energy versus Atomic Number (Z = 1 to 10) with special focus on {focus_topic}:}}\n\n"
        f"\\text{{1. State the general trend in first ionisation energy across Period 2 from Lithium to Neon.}}\n"
        f"\\text{{2. {specific_q}}}"
    )
    ans = (
        f"1. First ionisation energy generally increases across Period 2 due to increasing nuclear charge and decreasing atomic radius. "
        f"2. {specific_ans}"
    )
    q = {
        "id": f"mat10_22_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 5,
        "explanation": "Drop at Z=3 is due to start of new n=2 shell and shielding. Small dip between N and O is due to pairing repulsion in Oxygen's 2p4 orbital.",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "He is a filled shell; Li starts a new shell further away.",
            "tier_2": "Look at electron configurations of N (2p3) and O (2p4) and consider electron-electron repulsion in the paired orbital.",
            "tier_3": "Nitrogen has stable half-filled 2p3; Oxygen has paired repulsion in 2p4.",
        },
    }
    q.update(_make_meta("22_periodic_trends_graphical_analysis_svg", 15, 4, ["forgets_electron_electron_repulsion_in_oxygen_2p"]))
    return q


# --------------------------------------------------------------------------- #
# 23_chemical_reactivity_trends_alkali_metals_and_halogens
# --------------------------------------------------------------------------- #
def _build_23_chemical_reactivity_trends_alkali_metals_and_halogens(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    families = [
        {"family": "Group 1 (Alkali metals)", "elements": "Lithium, Sodium, Potassium", "trend": "increases down the group", "mechanism": "they react by losing their single valence electron; as atomic radius increases down the group, ionization energy decreases and the electron is lost more readily"},
        {"family": "Group 17 (Halogens)", "elements": "Fluorine, Chlorine, Bromine, Iodine", "trend": "decreases down the group", "mechanism": "they react by gaining an electron to form a stable octet; smaller atoms like Fluorine have their valence shell closer to the nucleus and attract electrons with higher force than larger atoms"},
    ]
    fam = r.choice(families)
    prompt = (
        f"\\text{{Investigate the chemical reactivity trends for }} \\textbf{{{fam['family']}}} ({fam['elements']}):\n\n"
        f"\\text{{1. State how chemical reactivity varies going down the group (increases or decreases).}}\n"
        f"\\text{{2. Explain this trend in terms of atomic radius, electron transfer, and nuclear attraction.}}"
    )
    ans = f"1. Reactivity {fam['trend']}. 2. Scientific reason: {fam['mechanism']}."
    q = {
        "id": f"mat10_23_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"In {fam['family']}, reactivity {fam['trend']} because {fam['mechanism']}.",
        "hints": {
            "tier_1": "Do these elements react by losing electrons or gaining electrons?",
            "tier_2": "Alkali metals lose electrons (easier when larger). Halogens gain electrons (easier when smaller).",
            "tier_3": f"Reactivity {fam['trend']}.",
        },
    }
    q.update(_make_meta("23_chemical_reactivity_trends_alkali_metals_and_halogens", 15, 3, ["assumes_all_groups_increase_reactivity_downwards"]))
    return q


# --------------------------------------------------------------------------- #
# 24_transition_metals_and_noble_gas_stability
# --------------------------------------------------------------------------- #
def _build_24_transition_metals_and_noble_gas_stability(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    noble_gases = [
        {"name": "Helium", "sym": "\\text{He}", "z": 2, "cfg": "1s^2 (duplet)"},
        {"name": "Neon", "sym": "\\text{Ne}", "z": 10, "cfg": "1s^2 2s^2 2p^6 (octet)"},
        {"name": "Argon", "sym": "\\text{Ar}", "z": 18, "cfg": "1s^2 2s^2 2p^6 3s^2 3p^6 (octet)"},
    ]
    ng = r.choice(noble_gases)
    prompt = (
        f"\\text{{The Group 18 element }} \\textbf{{{ng['name']}}} ({ng['sym']}, Z = {ng['z']}) \\text{{ is chemically unreactive (inert).}}\n\n"
        f"\\text{{1. Write down its ground state electron configuration.}}\n"
        f"\\text{{2. Explain its chemical inertness in terms of valence electron shell stability (octet/duplet rule).}}"
    )
    ans = f"1. {ng['cfg']}. 2. It has a completely filled outer valence shell, conferring high thermodynamic stability with zero tendency to gain, lose, or share electrons."
    q = {
        "id": f"mat10_24_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"{ng['name']} has a completely filled outer shell ({ng['cfg']}), which is energetically stable, resulting in no chemical reactivity under standard conditions.",
        "hints": {
            "tier_1": "Consider how many electrons occupy the outer shell.",
            "tier_2": "Filled duplet for He; filled octet for Ne and Ar.",
            "tier_3": f"Configuration: {ng['cfg']}.",
        },
    }
    q.update(_make_meta("24_transition_metals_and_noble_gas_stability", 15, 3, ["believes_helium_has_an_octet"]))
    return q


# --------------------------------------------------------------------------- #
# 25_atomic_radii_vs_ionic_radii_cations_and_anions
# --------------------------------------------------------------------------- #
def _build_25_atomic_radii_vs_ionic_radii_cations_and_anions(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    comparisons = [
        {"atom": "Sodium atom (Na)", "ion": "Sodium cation (Na+)", "type": "cation", "size_rel": "smaller than", "reason": "it loses its outermost valence electron (n=3 shell is completely lost), leaving 10 electrons in n=2 pulled tightly by 11 protons"},
        {"atom": "Chlorine atom (Cl)", "ion": "Chloride anion (Cl-)", "type": "anion", "size_rel": "larger than", "reason": "it gains an electron into the 3p subshell; the increased electron-electron repulsion causes the electron cloud to expand while nuclear charge (+17) remains constant"},
        {"atom": "Magnesium atom (Mg)", "ion": "Magnesium cation (Mg2+)", "type": "cation", "size_rel": "smaller than", "reason": "it loses both 3s valence electrons, losing an entire electron shell and having a higher proton-to-electron ratio (12:10)"},
        {"atom": "Oxygen atom (O)", "ion": "Oxide anion (O2-)", "type": "anion", "size_rel": "larger than", "reason": "gaining two electrons increases electrostatic repulsion between valence electrons, pushing the cloud outwards"},
    ]
    comp = r.choice(comparisons)
    prompt = (
        f"\\text{{Compare the radius of a neutral }} \\textbf{{{comp['atom']}}} \\text{{ with its corresponding ion, }} \\textbf{{{comp['ion']}}}:\n\n"
        f"\\text{{1. State whether the ionic radius is }} \\textbf{{smaller than}} \\text{{ or }} \\textbf{{larger than}} \\text{{ the neutral atomic radius.}}\n"
        f"\\text{{2. Provide a rigorous scientific explanation based on electron shells, proton-to-electron ratio, and electron-electron repulsion.}}"
    )
    ans = f"1. The ion is {comp['size_rel']} the neutral atom. 2. Scientific justification: {comp['reason']}."
    q = {
        "id": f"mat10_25_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"Cations are always smaller than parent atoms (loss of shell/increased attraction). Anions are always larger (increased electron-electron repulsion). {comp['ion']} is {comp['size_rel']} {comp['atom']}.",
        "hints": {
            "tier_1": "Cations lose electrons (contract); anions gain electrons (expand).",
            "tier_2": "Cations lose a shell or have fewer electrons pulled by the same protons; anions experience extra repulsion.",
            "tier_3": f"The ion is {comp['size_rel']} the neutral atom.",
        },
    }
    q.update(_make_meta("25_atomic_radii_vs_ionic_radii_cations_and_anions", 15, 3, ["believes_cations_are_larger_than_neutral_atoms"]))
    return q


# Export mapping
BUILDERS_01_25: Dict[str, Any] = {
    "01_classify_substance_element_compound_mixture": _build_01_classify_substance_element_compound_mixture,
    "02_homogeneous_vs_heterogeneous_mixtures": _build_02_homogeneous_vs_heterogeneous_mixtures,
    "03_separation_techniques_filtration_distillation_chromatography": _build_03_separation_techniques_filtration_distillation_chromatography,
    "04_states_of_matter_kinetic_molecular_theory_properties": _build_04_states_of_matter_kinetic_molecular_theory_properties,
    "05_heating_cooling_curve_phase_transitions_latent_heat_svg": _build_05_heating_cooling_curve_phase_transitions_latent_heat_svg,
    "06_microscopic_particle_representation_phases_svg": _build_06_microscopic_particle_representation_phases_svg,
    "07_atomic_number_mass_number_subatomic_particles": _build_07_atomic_number_mass_number_subatomic_particles,
    "08_isotope_notation_and_subatomic_composition": _build_08_isotope_notation_and_subatomic_composition,
    "09_relative_atomic_mass_from_isotopic_abundance": _build_09_relative_atomic_mass_from_isotopic_abundance,
    "10_mass_spectrometry_isotope_peaks_calculation": _build_10_mass_spectrometry_isotope_peaks_calculation,
    "11_bohr_model_energy_levels_quantum_shells": _build_11_bohr_model_energy_levels_quantum_shells,
    "12_sp_electron_configuration_notation_elements_1_to_20": _build_12_sp_electron_configuration_notation_elements_1_to_20,
    "13_aufbau_diagram_orbital_box_representation_svg": _build_13_aufbau_diagram_orbital_box_representation_svg,
    "14_pauli_exclusion_principle_application": _build_14_pauli_exclusion_principle_application,
    "15_hunds_rule_orbital_filling_and_unpaired_electrons": _build_15_hunds_rule_orbital_filling_and_unpaired_electrons,
    "16_periodic_table_periods_groups_and_blocks": _build_16_periodic_table_periods_groups_and_blocks,
    "17_classification_metals_nonmetals_metalloids": _build_17_classification_metals_nonmetals_metalloids,
    "18_valence_electrons_and_core_charge_deduction": _build_18_valence_electrons_and_core_charge_deduction,
    "19_periodic_trend_atomic_radius_variation": _build_19_periodic_trend_atomic_radius_variation,
    "20_periodic_trend_first_ionisation_energy": _build_20_periodic_trend_first_ionisation_energy,
    "21_periodic_trend_electron_affinity_and_electronegativity": _build_21_periodic_trend_electron_affinity_and_electronegativity,
    "22_periodic_trends_graphical_analysis_svg": _build_22_periodic_trends_graphical_analysis_svg,
    "23_chemical_reactivity_trends_alkali_metals_and_halogens": _build_23_chemical_reactivity_trends_alkali_metals_and_halogens,
    "24_transition_metals_and_noble_gas_stability": _build_24_transition_metals_and_noble_gas_stability,
    "25_atomic_radii_vs_ionic_radii_cations_and_anions": _build_25_atomic_radii_vs_ionic_radii_cations_and_anions,
}
