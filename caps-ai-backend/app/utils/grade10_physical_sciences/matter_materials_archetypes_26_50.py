"""Grade 10 Physical Sciences — Matter and Materials Archetypes 26–50.
Grounded in curriculum_docs_auto/PhysicalSciences_Gr10/:
- Term 1: Chemical bonding (covalent, ionic, metallic, crystal lattices).
- Term 2: The particles that substances are made of (atoms, molecules, giant structures, empirical/molecular formulas).
- Term 4: The hydrosphere (water cycle, water purity, hard/soft water).
- Term 4: Units of measurement applied, scientific notation, sig figs, diagnostic triage.

100% Aligned with South African National Curriculum Standards.
Complies strictly with 6-Pillar Generator Contract.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional

TOPIC = "Chemical bonding"
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
    term: int = 1,
    weight: int = 15,
    duration: int = 4,
    misconceptions: Optional[List[str]] = None,
    criteria: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    return {
        "term": term,
        "caps_weight_percent": weight,
        "suggested_duration_mins": duration,
        "mode": f"elementary_{subskill}",
        "topic": TOPIC,
        "subject": SUBJECT,
        "grade": GRADE,
        "subskill": subskill,
        "misconception_tags": misconceptions or ["bonding_misconception"],
        "marking_schema": {
            "total_marks": sum(c.get("marks", 1) for c in (criteria or [{"criterion": "Accurate answer", "marks": 2}])),
            "criteria": criteria or [{"criterion": "Accurate chemical reasoning and formula", "marks": 2}],
        },
    }


# --------------------------------------------------------------------------- #
# 26_lewis_dot_diagrams_neutral_atoms
# --------------------------------------------------------------------------- #
def _build_26_lewis_dot_diagrams_neutral_atoms(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    elements = [
        {"name": "Carbon", "sym": "\\text{C}", "group": 14, "valence": 4, "dots": "four single unpaired valence electrons surrounding the chemical symbol"},
        {"name": "Nitrogen", "sym": "\\text{N}", "group": 15, "valence": 5, "dots": "one lone pair and three unpaired single valence electrons"},
        {"name": "Oxygen", "sym": "\\text{O}", "group": 16, "valence": 6, "dots": "two lone pairs and two single unpaired valence electrons"},
        {"name": "Fluorine", "sym": "\\text{F}", "group": 17, "valence": 7, "dots": "three lone pairs and one single unpaired valence electron"},
        {"name": "Phosphorus", "sym": "\\text{P}", "group": 15, "valence": 5, "dots": "one lone pair and three single unpaired valence electrons"},
        {"name": "Sulfur", "sym": "\\text{S}", "group": 16, "valence": 6, "dots": "two lone pairs and two single unpaired valence electrons"},
        {"name": "Neon", "sym": "\\text{Ne}", "group": 18, "valence": 8, "dots": "four lone pairs (complete stable octet of eight valence electrons)"},
    ]
    el = r.choice(elements)
    prompt = (
        f"\\text{{1. Define a }} \\textbf{{Lewis dot diagram (Lewis structure)}}.\n\n"
        f"\\text{{2. For a neutral atom of }} \\textbf{{{el['name']}}} ({el['sym']}, \\text{{Group {el['group']}}}):\n"
        f"\\text{{a) State the number of valence electrons.}}\n"
        f"\\text{{b) Describe the arrangement of valence dots and lone pairs around the chemical symbol.}}"
    )
    ans = (
        f"1. A Lewis dot diagram is a structural representation of a molecule or atom where valence electrons are shown as dots (or crosses) around the chemical symbol. "
        f"2. a) {el['valence']} valence electrons. b) Arranged as {el['dots']}."
    )
    q = {
        "id": f"mat10_26_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"{el['name']} has {el['valence']} valence electrons (Group {el['group']}). In a Lewis dot diagram: {el['dots']}.",
        "hints": {
            "tier_1": "Lewis diagrams show only outermost valence electrons.",
            "tier_2": "Group number determines valence count: Group 14 has 4, Group 15 has 5, Group 16 has 6, Group 17 has 7.",
            "tier_3": f"{el['name']} has {el['valence']} valence electrons.",
        },
    }
    q.update(_make_meta("26_lewis_dot_diagrams_neutral_atoms", 1, 15, 3, ["includes_inner_core_electrons_in_lewis_diagram"]))
    return q


# --------------------------------------------------------------------------- #
# 27_covalent_bonding_electron_sharing_diatomic_molecules_svg
# --------------------------------------------------------------------------- #
def _build_27_covalent_bonding_electron_sharing_diatomic_molecules_svg(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    diatomics = [
        {"name": "Hydrogen", "formula": "\\text{H}_2", "bonds": 1, "type": "single covalent bond (sharing 1 pair of electrons)", "col": "#38BDF8"},
        {"name": "Oxygen", "formula": "\\text{O}_2", "bonds": 2, "type": "double covalent bond (sharing 2 pairs of electrons)", "col": "#EF4444"},
        {"name": "Nitrogen", "formula": "\\text{N}_2", "bonds": 3, "type": "triple covalent bond (sharing 3 pairs of electrons)", "col": "#10B981"},
        {"name": "Chlorine", "formula": "\\text{Cl}_2", "bonds": 1, "type": "single covalent bond (sharing 1 pair of electrons)", "col": "#F59E0B"},
    ]
    di = r.choice(diatomics)

    # Dynamic Lewis overlap diagram in SVG
    svg = f"""<svg viewBox="0 0 460 200" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
  <!-- Covalent molecule {di['name']} ({di['formula']}) -->
  <circle cx="170" cy="100" r="60" fill="none" stroke="{di['col']}" stroke-width="2" stroke-dasharray="4,4" />
  <circle cx="290" cy="100" r="60" fill="none" stroke="{di['col']}" stroke-width="2" stroke-dasharray="4,4" />
  <text x="140" y="105" font-size="18" fill="#0F172A" font-weight="bold" text-anchor="middle">{di['name'][0]}</text>
  <text x="320" y="105" font-size="18" fill="#0F172A" font-weight="bold" text-anchor="middle">{di['name'][0]}</text>

  <!-- Shared overlap zone -->
  <ellipse cx="230" cy="100" rx="25" ry="45" fill="{di['col']}" opacity="0.15" />
  <text x="230" y="85" font-size="14" fill="#0F172A" text-anchor="middle">{"• " * di['bonds']}</text>
  <text x="230" y="115" font-size="14" fill="#0F172A" text-anchor="middle">{"× " * di['bonds']}</text>
  <text x="230" y="170" font-size="11" fill="#475569" text-anchor="middle">Shared Region ({di['bonds']} pair(s))</text>
</svg>"""

    prompt = (
        f"\\text{{Refer to the Lewis electron-sharing diagram for a molecule of }} \\textbf{{{di['name']}}} ({di['formula']}):\n\n"
        f"\\text{{1. Define a }} \\textbf{{covalent bond}}.\n"
        f"\\text{{2. State whether a single, double, or triple covalent bond forms between the two atoms in }} {di['formula']}.\n"
        f"\\text{{3. State how many electrons are shared in total in the bonding region.}}"
    )
    ans = (
        f"1. A covalent bond is a chemical bond formed by the sharing of at least one pair of electrons between two non-metal atoms. "
        f"2. A {di['type']}. "
        f"3. {di['bonds'] * 2} electrons in total ({di['bonds']} shared pair(s))."
    )
    q = {
        "id": f"mat10_27_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"Covalent bonding involves shared electron pairs. {di['name']} ({di['formula']}) shares {di['bonds']} pair(s) = {di['bonds']*2} electrons.",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Covalent bonds form between non-metals sharing electron pairs.",
            "tier_2": "H2 and Cl2 share 1 pair; O2 shares 2 pairs; N2 shares 3 pairs.",
            "tier_3": f"{di['formula']} forms a {di['type']}.",
        },
    }
    q.update(_make_meta("27_covalent_bonding_electron_sharing_diatomic_molecules_svg", 1, 15, 3, ["believes_covalent_bonds_involve_electron_transfer"]))
    return q


# --------------------------------------------------------------------------- #
# 28_covalent_bonding_polyatomic_molecules_water_ammonia_methane
# --------------------------------------------------------------------------- #
def _build_28_covalent_bonding_polyatomic_molecules_water_ammonia_methane(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    molecules = [
        {"name": "Water", "formula": "\\text{H}_2\\text{O}", "central": "Oxygen", "bonds": 2, "lone_pairs": 2, "shape": "bent (angular)"},
        {"name": "Ammonia", "formula": "\\text{NH}_3", "central": "Nitrogen", "bonds": 3, "lone_pairs": 1, "shape": "trigonal pyramidal"},
        {"name": "Methane", "formula": "\\text{CH}_4", "central": "Carbon", "bonds": 4, "lone_pairs": 0, "shape": "tetrahedral"},
        {"name": "Hydrogen fluoride", "formula": "\\text{HF}", "central": "Fluorine", "bonds": 1, "lone_pairs": 3, "shape": "linear"},
    ]
    mol = r.choice(molecules)
    prompt = (
        f"\\text{{Consider the polyatomic covalent molecule }} \\textbf{{{mol['name']}}} ({mol['formula']}):\n\n"
        f"\\text{{1. Identify the central atom.}}\n"
        f"\\text{{2. State the number of shared covalent bonding pairs around the central atom.}}\n"
        f"\\text{{3. State the number of unshared lone pairs on the central atom.}}\n"
        f"\\text{{4. State the molecular geometry (shape) predicted for this molecule.}}"
    )
    ans = f"1. {mol['central']}; 2. {mol['bonds']} bonding pairs; 3. {mol['lone_pairs']} lone pair(s); 4. {mol['shape']}."
    q = {
        "id": f"mat10_28_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"In {mol['name']} ({mol['formula']}), the central {mol['central']} has {mol['bonds']} bonding pairs and {mol['lone_pairs']} lone pairs, giving a {mol['shape']} geometry.",
        "hints": {
            "tier_1": "Count valence electrons of the central atom and subtract bonding pairs to find lone pairs.",
            "tier_2": "H2O: 2 bonds + 2 lone pairs. NH3: 3 bonds + 1 lone pair. CH4: 4 bonds + 0 lone pairs.",
            "tier_3": f"{mol['bonds']} bonds, {mol['lone_pairs']} lone pair(s), {mol['shape']}.",
        },
    }
    q.update(_make_meta("28_covalent_bonding_polyatomic_molecules_water_ammonia_methane", 1, 15, 3, ["forgets_lone_pairs_on_oxygen_or_nitrogen"]))
    return q


# --------------------------------------------------------------------------- #
# 29_ionic_bonding_electron_transfer_and_ion_formation
# --------------------------------------------------------------------------- #
def _build_29_ionic_bonding_electron_transfer_and_ion_formation(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    compounds = [
        {"metal": "Sodium (Na)", "nonmetal": "Chlorine (Cl)", "m_ion": "\\text{Na}^+", "nm_ion": "\\text{Cl}^-", "trans": "one electron transferred from sodium to chlorine", "formula": "\\text{NaCl}"},
        {"metal": "Magnesium (Mg)", "nonmetal": "Oxygen (O)", "m_ion": "\\text{Mg}^{2+}", "nm_ion": "\\text{O}^{2-}", "trans": "two electrons transferred from magnesium to oxygen", "formula": "\\text{MgO}"},
        {"metal": "Calcium (Ca)", "nonmetal": "Fluorine (F)", "m_ion": "\\text{Ca}^{2+}", "nm_ion": "2\\;\\text{F}^-", "trans": "two electrons transferred: one to each of two fluorine atoms", "formula": "\\text{CaF}_2"},
        {"metal": "Potassium (K)", "nonmetal": "Bromine (Br)", "m_ion": "\\text{K}^+", "nm_ion": "\\text{Br}^-", "trans": "one electron transferred from potassium to bromine", "formula": "\\text{KBr}"},
    ]
    cp = r.choice(compounds)
    prompt = (
        f"\\text{{Explain the formation of the ionic compound }} \\textbf{{{cp['formula']}}} \\text{{ from }} \\textbf{{{cp['metal']}}} \\text{{ and }} \\textbf{{{cp['nonmetal']}}}:\n\n"
        f"\\text{{1. Define an }} \\textbf{{ionic bond}}.\n"
        f"\\text{{2. Describe the electron transfer process that occurs between the atoms.}}\n"
        f"\\text{{3. Write the chemical symbols and charges of the resulting cation and anion.}}"
    )
    ans = (
        f"1. An ionic bond is a chemical bond formed by the electrostatic attraction between oppositely charged ions created by electron transfer from a metal to a non-metal. "
        f"2. {cp['trans'].capitalize()}. "
        f"3. Cation: {cp['m_ion']}; Anion: {cp['nm_ion']}."
    )
    q = {
        "id": f"mat10_29_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"Ionic bonding involves complete electron transfer. {cp['metal']} loses electrons to form {cp['m_ion']}, while {cp['nonmetal']} gains electrons to form {cp['nm_ion']}.",
        "hints": {
            "tier_1": "Metals lose valence electrons to form positive cations; non-metals gain electrons to form negative anions.",
            "tier_2": "State the definition: electrostatic attraction between oppositely charged ions.",
            "tier_3": f"Cation: {cp['m_ion']}, Anion: {cp['nm_ion']}.",
        },
    }
    q.update(_make_meta("29_ionic_bonding_electron_transfer_and_ion_formation", 1, 15, 3, ["believes_electrons_are_shared_in_ionic_compounds"]))
    return q


# --------------------------------------------------------------------------- #
# 30_ionic_crystal_lattice_structure_and_properties_svg
# --------------------------------------------------------------------------- #
def _build_30_ionic_crystal_lattice_structure_and_properties_svg(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    compounds = [
        {"name": "Sodium chloride (NaCl)", "cation": "Na+", "anion": "Cl-", "mp": 801},
        {"name": "Magnesium oxide (MgO)", "cation": "Mg2+", "anion": "O2-", "mp": 2852},
        {"name": "Potassium chloride (KCl)", "cation": "K+", "anion": "Cl-", "mp": 770},
    ]
    cp = r.choice(compounds)

    # 3D-effect crystal lattice grid in SVG
    svg = f"""<svg viewBox="0 0 460 220" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
  <!-- Ionic Crystal Lattice: {cp['name']} -->
  <g stroke="#94A3B8" stroke-width="1.5">
    <line x1="120" y1="60" x2="260" y2="60" />
    <line x1="120" y1="140" x2="260" y2="140" />
    <line x1="120" y1="60" x2="120" y2="140" />
    <line x1="260" y1="60" x2="260" y2="140" />

    <line x1="160" y1="30" x2="300" y2="30" />
    <line x1="160" y1="110" x2="300" y2="110" />
    <line x1="160" y1="30" x2="160" y2="110" />
    <line x1="300" y1="30" x2="300" y2="110" />

    <!-- Connecting edges -->
    <line x1="120" y1="60" x2="160" y2="30" />
    <line x1="260" y1="60" x2="300" y2="30" />
    <line x1="120" y1="140" x2="160" y2="110" />
    <line x1="260" y1="140" x2="300" y2="110" />
  </g>

  <!-- Alternating Ions -->
  <circle cx="120" cy="60" r="12" fill="#3B82F6" /><text x="120" y="64" font-size="9" fill="#FFF" text-anchor="middle">{cp['cation']}</text>
  <circle cx="260" cy="60" r="16" fill="#10B981" /><text x="260" y="64" font-size="9" fill="#FFF" text-anchor="middle">{cp['anion']}</text>
  <circle cx="120" cy="140" r="16" fill="#10B981" /><text x="120" y="144" font-size="9" fill="#FFF" text-anchor="middle">{cp['anion']}</text>
  <circle cx="260" cy="140" r="12" fill="#3B82F6" /><text x="260" y="144" font-size="9" fill="#FFF" text-anchor="middle">{cp['cation']}</text>

  <circle cx="160" cy="30" r="16" fill="#10B981" /><text x="160" y="34" font-size="9" fill="#FFF" text-anchor="middle">{cp['anion']}</text>
  <circle cx="300" cy="30" r="12" fill="#3B82F6" /><text x="300" y="34" font-size="9" fill="#FFF" text-anchor="middle">{cp['cation']}</text>
  <circle cx="160" cy="110" r="12" fill="#3B82F6" /><text x="160" y="114" font-size="9" fill="#FFF" text-anchor="middle">{cp['cation']}</text>
  <circle cx="300" cy="110" r="16" fill="#10B981" /><text x="300" y="114" font-size="9" fill="#FFF" text-anchor="middle">{cp['anion']}</text>

  <!-- Legend -->
  <circle cx="370" cy="80" r="10" fill="#3B82F6" /><text x="390" y="84" font-size="11" fill="#0F172A">Cation ({cp['cation']})</text>
  <circle cx="370" cy="110" r="13" fill="#10B981" /><text x="390" y="114" font-size="11" fill="#0F172A">Anion ({cp['anion']})</text>
</svg>"""

    prompt = (
        f"\\text{{Refer to the 3D crystal lattice diagram representing solid }} \\textbf{{{cp['name']}}} (\\text{{melting point }} {cp['mp']}^\\circ\\text{{C}}):\n\n"
        f"\\text{{1. Explain why solid {cp['name']} does not conduct electricity, but conducts electricity when melted (molten) or dissolved in water.}}\n"
        f"\\text{{2. Explain why ionic crystals are characteristically }} \\textbf{{brittle}} \\text{{ when struck with a hammer.}}"
    )
    ans = (
        f"1. In the solid state, ions are locked into fixed positions within the crystal lattice and cannot move; when molten or dissolved in water, the lattice breaks down and free mobile ions are available to carry electrical current. "
        f"2. A mechanical strike shifts planes of ions, bringing ions of like charge next to each other (e.g. cation next to cation); electrostatic repulsion between like charges then shatters the crystal."
    )
    q = {
        "id": f"mat10_30_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": "Solid: ions locked in lattice (insulator). Aqueous/molten: free mobile ions (conductor). Brittleness: like charges align under stress causing repulsive cleavage.",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Electrical conduction requires mobile charge carriers. What are the charge carriers in salts?",
            "tier_2": "In solids, ions are fixed; in molten/aqueous states, ions are free to move. Shifting lattice brings like charges together.",
            "tier_3": "Requires free mobile ions. Shifting like charges causes repulsive shattering (brittleness).",
        },
    }
    q.update(_make_meta("30_ionic_crystal_lattice_structure_and_properties_svg", 1, 15, 4, ["believes_electrons_conduct_electricity_in_molten_salts"]))
    return q


# --------------------------------------------------------------------------- #
# 31_metallic_bonding_sea_of_delocalised_electrons_svg
# --------------------------------------------------------------------------- #
def _build_31_metallic_bonding_sea_of_delocalised_electrons_svg(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    metals = [
        {"name": "Copper wire", "cation": "Cu2+", "use": "electrical wiring"},
        {"name": "Aluminum sheet", "cation": "Al3+", "use": "aircraft fuselage and foil"},
        {"name": "Iron beam", "cation": "Fe2+", "use": "structural construction"},
        {"name": "Silver jewellery", "cation": "Ag+", "use": "precision contacts and ornamentation"},
    ]
    met = r.choice(metals)

    # Electron sea model SVG
    svg = f"""<svg viewBox="0 0 460 200" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
  <!-- Metallic bonding: {met['name']} -->
  <!-- Blue background sea -->
  <rect x="40" y="30" width="380" height="140" fill="#E0F2FE" rx="6" stroke="#0284C7" stroke-width="2" />
  <text x="230" y="25" font-size="11" fill="#0369A1" font-weight="bold" text-anchor="middle">Sea of Delocalised Valence Electrons</text>

  <!-- Positive Kernels (Cations) -->
  <g fill="#EF4444" stroke="#991B1B" stroke-width="1.5">
    <circle cx="80" cy="65" r="16" /><text x="80" y="70" font-size="10" fill="#FFF" text-anchor="middle" font-weight="bold">+</text>
    <circle cx="155" cy="65" r="16" /><text x="155" y="70" font-size="10" fill="#FFF" text-anchor="middle" font-weight="bold">+</text>
    <circle cx="230" cy="65" r="16" /><text x="230" y="70" font-size="10" fill="#FFF" text-anchor="middle" font-weight="bold">+</text>
    <circle cx="305" cy="65" r="16" /><text x="305" y="70" font-size="10" fill="#FFF" text-anchor="middle" font-weight="bold">+</text>
    <circle cx="380" cy="65" r="16" /><text x="380" y="70" font-size="10" fill="#FFF" text-anchor="middle" font-weight="bold">+</text>

    <circle cx="80" cy="135" r="16" /><text x="80" y="140" font-size="10" fill="#FFF" text-anchor="middle" font-weight="bold">+</text>
    <circle cx="155" cy="135" r="16" /><text x="155" y="140" font-size="10" fill="#FFF" text-anchor="middle" font-weight="bold">+</text>
    <circle cx="230" cy="135" r="16" /><text x="230" y="140" font-size="10" fill="#FFF" text-anchor="middle" font-weight="bold">+</text>
    <circle cx="305" cy="135" r="16" /><text x="305" y="140" font-size="10" fill="#FFF" text-anchor="middle" font-weight="bold">+</text>
    <circle cx="380" cy="135" r="16" /><text x="380" y="140" font-size="10" fill="#FFF" text-anchor="middle" font-weight="bold">+</text>
  </g>

  <!-- Free Delocalized Electrons -->
  <g fill="#0284C7" font-size="9" text-anchor="middle" font-weight="bold">
    <text x="115" y="55">e⁻</text><text x="190" y="55">e⁻</text><text x="265" y="55">e⁻</text><text x="340" y="55">e⁻</text>
    <text x="115" y="105">e⁻</text><text x="190" y="105">e⁻</text><text x="265" y="105">e⁻</text><text x="340" y="105">e⁻</text>
    <text x="115" y="155">e⁻</text><text x="190" y="155">e⁻</text><text x="265" y="155">e⁻</text><text x="340" y="155">e⁻</text>
  </g>
</svg>"""

    prompt = (
        f"\\text{{Refer to the electron-sea model diagram representing metallic bonding in a sample of }} \\textbf{{{met['name']}}}:\n\n"
        f"\\text{{1. Define }} \\textbf{{metallic bonding}}.\n"
        f"\\text{{2. Explain why {met['name']} is an excellent electrical and thermal conductor.}}\n"
        f"\\text{{3. Explain why metals are }} \\textbf{{malleable}} \\text{{ (can be hammered into sheets) rather than brittle.}}"
    )
    ans = (
        "1. Metallic bonding is the electrostatic attraction between positive metallic kernels (cations) and a sea of delocalised valence electrons. "
        "2. The delocalised electrons are free to move throughout the metallic lattice under an applied potential difference or thermal gradient. "
        "3. When struck, layers of positive cations can slide past each other without shattering because the flexible delocalised electron sea maintains bonding throughout the deformation."
    )
    q = {
        "id": f"mat10_31_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": "Metallic bonding: attraction between positive kernels and sea of delocalized electrons. Delocalized electrons enable conduction and allow cation layers to slide smoothly (malleability).",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Recall: positive kernels + sea of delocalized electrons.",
            "tier_2": "Electrical conductivity is due to mobile delocalized electrons. Malleability is due to sliding cation layers cushioned by the electron sea.",
            "tier_3": "Attraction between cations and delocalized electrons.",
        },
    }
    q.update(_make_meta("31_metallic_bonding_sea_of_delocalised_electrons_svg", 1, 15, 4, ["believes_positive_kernels_move_to_conduct_electricity"]))
    return q


# --------------------------------------------------------------------------- #
# 32_chemical_formula_writing_binary_ionic_compounds
# --------------------------------------------------------------------------- #
def _build_32_chemical_formula_writing_binary_ionic_compounds(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    compounds = [
        {"name": "magnesium chloride", "cation": "Mg^{2+}", "anion": "Cl^-", "formula": "\\text{MgCl}_2"},
        {"name": "aluminium oxide", "cation": "Al^{3+}", "anion": "O^{2-}", "formula": "\\text{Al}_2\\text{O}_3"},
        {"name": "calcium sulfide", "cation": "Ca^{2+}", "anion": "S^{2-}", "formula": "\\text{CaS}"},
        {"name": "sodium nitride", "cation": "Na^+", "anion": "N^{3-}", "formula": "\\text{Na}_3\\text{N}"},
        {"name": "potassium oxide", "cation": "K^+", "anion": "O^{2-}", "formula": "\\text{K}_2\\text{O}"},
        {"name": "aluminium fluoride", "cation": "Al^{3+}", "anion": "F^-", "formula": "\\text{AlF}_3"},
    ]
    cp = r.choice(compounds)
    prompt = (
        f"\\text{{Write down the correct chemical formula for the binary ionic compound:}}\n\n"
        f"\\textbf{{{cp['name']}}}.\n\n"
        f"\\text{{Show the cross-over of charges method or zero-net-charge calculation using ions }} "
        f"{cp['cation']} \\text{{ and }} {cp['anion']}."
    )
    ans = f"Formula: {cp['formula']}. Net charge: sum of cation and anion charges equals zero."
    q = {
        "id": f"mat10_32_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 2,
        "explanation": f"Balancing {cp['cation']} and {cp['anion']} to achieve overall electrical neutrality gives {cp['formula']}.",
        "hints": {
            "tier_1": "The total positive charges must balance the total negative charges.",
            "tier_2": "Cross-over the valency magnitudes to determine subscripts, then simplify if needed.",
            "tier_3": f"Formula is {cp['formula']}.",
        },
    }
    q.update(_make_meta("32_chemical_formula_writing_binary_ionic_compounds", 1, 15, 2, ["omits_subscripts_or_carries_signs_into_formula"]))
    return q


# --------------------------------------------------------------------------- #
# 33_chemical_formula_writing_polyatomic_ionic_compounds
# --------------------------------------------------------------------------- #
def _build_33_chemical_formula_writing_polyatomic_ionic_compounds(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    compounds = [
        {"name": "copper(II) nitrate", "cation": "Cu^{2+}", "anion": "\\text{NO}_3^-", "formula": "\\text{Cu(NO}_3\\text{)}_2"},
        {"name": "ammonium sulfate", "cation": "\\text{NH}_4^+", "anion": "\\text{SO}_4^{2-}", "formula": "\\text{(NH}_4\\text{)}_2\\text{SO}_4"},
        {"name": "calcium phosphate", "cation": "Ca^{2+}", "anion": "\\text{PO}_4^{3-}", "formula": "\\text{Ca}_3\\text{(PO}_4\\text{)}_2"},
        {"name": "iron(III) hydroxide", "cation": "Fe^{3+}", "anion": "\\text{OH}^-", "formula": "\\text{Fe(OH)}_3"},
        {"name": "magnesium carbonate", "cation": "Mg^{2+}", "anion": "\\text{CO}_3^{2-}", "formula": "\\text{MgCO}_3"},
    ]
    cp = r.choice(compounds)
    prompt = (
        f"\\text{{Write down the correct chemical formula for the polyatomic ionic compound:}}\n\n"
        f"\\textbf{{{cp['name']}}}.\n\n"
        f"\\text{{(Note: remember to use brackets correctly when more than one polyatomic ion is required.)}}"
    )
    ans = f"Formula: {cp['formula']}."
    q = {
        "id": f"mat10_33_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 2,
        "explanation": f"Combining {cp['cation']} with {cp['anion']} requires brackets around polyatomic ions when multiplied, yielding {cp['formula']}.",
        "hints": {
            "tier_1": "Use parentheses around the polyatomic group if its subscript is 2 or more.",
            "tier_2": f"Balance the charges of {cp['cation']} and {cp['anion']}.",
            "tier_3": f"Formula: {cp['formula']}.",
        },
    }
    q.update(_make_meta("33_chemical_formula_writing_polyatomic_ionic_compounds", 1, 15, 2, ["forgets_parentheses_around_polyatomic_ions"]))
    return q


# --------------------------------------------------------------------------- #
# 34_naming_covalent_and_ionic_chemical_compounds
# --------------------------------------------------------------------------- #
def _build_34_naming_covalent_and_ionic_chemical_compounds(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    compounds = [
        {"formula": "\\text{N}_2\\text{O}_4", "name": "dinitrogen tetroxide", "kind": "covalent compound", "rule": "uses Greek numerical prefixes (di- = 2, tetra- = 4)"},
        {"formula": "\\text{Fe}_2\\text{O}_3", "name": "iron(III) oxide", "kind": "ionic compound", "rule": "uses Roman numeral (III) to denote the +3 oxidation state of iron"},
        {"formula": "\\text{PCl}_5", "name": "phosphorus pentachloride", "kind": "covalent compound", "rule": "uses penta- prefix for 5 chlorine atoms"},
        {"formula": "\\text{CuSO}_4", "name": "copper(II) sulfate", "kind": "ionic compound", "rule": "uses Roman numeral (II) for Cu2+ with the polyatomic sulfate ion"},
        {"formula": "\\text{SF}_6", "name": "sulfur hexafluoride", "kind": "covalent compound", "rule": "uses hexa- prefix for 6 fluorine atoms"},
    ]
    cp = r.choice(compounds)
    prompt = (
        f"\\text{{Provide the systematic IUPAC chemical name for the compound: }}\n\n"
        f"\\textbf{{{cp['formula']}}}.\n\n"
        f"\\text{{State the naming convention applied (e.g. Greek prefixes vs Roman numeral oxidation states).}}"
    )
    ans = f"Name: {cp['name']}. Naming convention: {cp['rule']}."
    q = {
        "id": f"mat10_34_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 2,
        "explanation": f"{cp['formula']} is systematically named {cp['name']} according to IUPAC rules: {cp['rule']}.",
        "hints": {
            "tier_1": "Is it ionic with a multivalent transition metal or molecular covalent?",
            "tier_2": "Covalent compounds use prefixes like di-, tri-, tetra-. Transition metals use Roman numerals.",
            "tier_3": f"Name: {cp['name']}.",
        },
    }
    q.update(_make_meta("34_naming_covalent_and_ionic_chemical_compounds", 1, 15, 2, ["uses_greek_prefixes_for_ionic_compounds"]))
    return q


# --------------------------------------------------------------------------- #
# 35_physical_properties_correlated_to_bonding_type
# --------------------------------------------------------------------------- #
def _build_35_physical_properties_correlated_to_bonding_type(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    types = [
        {"type": "Simple molecular covalent (e.g. Iodine I2 or Ice H2O)", "mp": "low melting and boiling points", "cond": "non-conductor in all states", "reason": "intermolecular forces (London or dipole-dipole) are weak and easily overcome, and there are no mobile charge carriers"},
        {"type": "Giant ionic lattice (e.g. Sodium chloride NaCl)", "mp": "high melting and boiling points", "cond": "insulator as solid, conductor when molten or aqueous", "reason": "strong electrostatic attractions between oppositely charged ions require high thermal energy to break; ions become mobile in liquid/solution"},
        {"type": "Giant covalent network (e.g. Diamond or Silicon dioxide)", "mp": "extremely high melting points", "cond": "non-conductor (except graphite)", "reason": "atoms are held together by an extensive 3D framework of strong covalent bonds with localized electrons"},
        {"type": "Metallic lattice (e.g. Copper or Iron)", "mp": "moderate to high melting points", "cond": "excellent conductor in solid and liquid states", "reason": "strong attraction between cations and delocalised electron sea; mobile electrons conduct thermal and electrical energy"},
    ]
    tp = r.choice(types)
    prompt = (
        f"\\text{{Correlate the bonding model of a }} \\textbf{{{tp['type']}}} \\text{{ with its physical properties:}}\n\n"
        f"\\text{{1. Describe its melting and boiling point characteristics.}}\n"
        f"\\text{{2. Describe its electrical conductivity behavior in both solid and liquid states.}}\n"
        f"\\text{{3. Explain these macroscopic physical properties in terms of microscopic bonding and structure.}}"
    )
    ans = f"1. {tp['mp']}. 2. {tp['cond']}. 3. {tp['reason']}."
    q = {
        "id": f"mat10_35_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"For {tp['type']}: {tp['mp']}, {tp['cond']}, because {tp['reason']}.",
        "hints": {
            "tier_1": "Consider whether forces holding the solid are weak intermolecular forces, ionic attractions, or metallic bonds.",
            "tier_2": "Look for the presence of mobile electrons or mobile ions.",
            "tier_3": f"{tp['mp']}; {tp['cond']}.",
        },
    }
    q.update(_make_meta("35_physical_properties_correlated_to_bonding_type", 1, 15, 3, ["confuses_intermolecular_forces_with_intramolecular_covalent_bonds"]))
    return q


# --------------------------------------------------------------------------- #
# 36_electronegativity_difference_and_bond_polarity_classification
# --------------------------------------------------------------------------- #
def _build_36_electronegativity_difference_and_bond_polarity_classification(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    bonds = [
        {"bond": "C-H", "en1": 2.5, "en2": 2.1, "diff": 0.4, "type": "non-polar covalent bond (pure covalent)"},
        {"bond": "H-Cl", "en1": 3.0, "en2": 2.1, "diff": 0.9, "type": "polar covalent bond"},
        {"bond": "O-H", "en1": 3.5, "en2": 2.1, "diff": 1.4, "type": "strongly polar covalent bond"},
        {"bond": "Na-Cl", "en1": 3.0, "en2": 0.9, "diff": 2.1, "type": "predominantly ionic bond"},
        {"bond": "F-F", "en1": 4.0, "en2": 4.0, "diff": 0.0, "type": "pure non-polar covalent bond"},
    ]
    bd = r.choice(bonds)
    diff_str = _fmt_sa(bd["diff"], 1)

    prompt = (
        f"\\text{{Given Pauling electronegativity values:}}\n\n"
        f"\\text{{Element 1: }} {bd['en1']} \\quad \\text{{and}} \\quad \\text{{Element 2: }} {bd['en2']}.\n\n"
        f"\\text{{1. Calculate the electronegativity difference (}}\\Delta\\text{{EN) for the }} \\textbf{{{bd['bond']}}} \\text{{ bond.}}\n"
        f"\\text{{2. Classify the bond as }} \\textbf{{non-polar covalent}}, \\textbf{{polar covalent}}, \\text{{ or }} \\textbf{{ionic}}.\n"
        f"\\text{{3. Explain what causes unequal electron sharing in a polar covalent bond.}}"
    )
    ans = (
        f"1. Delta EN = {_fmt_sa(bd['en1'])} - {_fmt_sa(bd['en2'])} = {diff_str}. "
        f"2. {bd['type']}. "
        f"3. The atom with higher electronegativity exerts a stronger pull on the shared bonding electron pair, creating a partial negative charge (delta-) on itself and a partial positive charge (delta+) on the other atom."
    )
    q = {
        "id": f"mat10_36_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"Delta EN = {diff_str}. Guidelines: Delta EN < 0.5 = non-polar covalent; 0.5 <= Delta EN <= 1.7 = polar covalent; Delta EN > 1.7 = ionic.",
        "hints": {
            "tier_1": "Subtract the lower electronegativity from the higher.",
            "tier_2": "Delta EN < 0.5 is non-polar; 0.5 to 1.7 is polar covalent; > 1.7 is ionic.",
            "tier_3": f"Delta EN = {diff_str} -> {bd['type']}.",
        },
    }
    q.update(_make_meta("36_electronegativity_difference_and_bond_polarity_classification", 1, 15, 3, ["believes_c_h_bond_is_polar"]))
    return q


# --------------------------------------------------------------------------- #
# 37_particles_nature_atomic_molecular_giant_covalent_network
# --------------------------------------------------------------------------- #
def _build_37_particles_nature_atomic_molecular_giant_covalent_network(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    substances = [
        {"name": "Helium gas", "unit": "monatomic atoms", "forces": "extremely weak London dispersion forces between isolated atoms"},
        {"name": "Carbon dioxide dry ice", "unit": "discrete covalent molecules (CO2)", "forces": "weak London dispersion forces between neutral non-polar molecules"},
        {"name": "Silicon dioxide (quartz sand)", "unit": "giant covalent 3D network of silicon and oxygen atoms", "forces": "strong continuous tetrahedral covalent bonds throughout"},
        {"name": "Solid copper rod", "unit": "metallic crystal lattice of positive copper ions", "forces": "strong metallic bonding with a delocalised sea of electrons"},
    ]
    sub = r.choice(substances)
    prompt = (
        f"\\text{{For the substance }} \\textbf{{{sub['name']}}}:\n\n"
        f"\\text{{1. Identify the fundamental particle unit that constitutes this substance (e.g. atoms, discrete molecules, ions, or giant network).}}\n"
        f"\\text{{2. State the nature of the forces or bonds holding these constituent particles together.}}"
    )
    ans = f"1. {sub['unit']}. 2. {sub['forces']}."
    q = {
        "id": f"mat10_37_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 2,
        "explanation": f"{sub['name']} consists of {sub['unit']}, held by {sub['forces']}.",
        "hints": {
            "tier_1": "Ask: Is it made of single atoms, separate molecules, or a giant continuous lattice?",
            "tier_2": "Noble gases are monatomic; CO2 has discrete molecules; quartz is giant network.",
            "tier_3": f"{sub['unit']}.",
        },
    }
    q.update(_make_meta("37_particles_nature_atomic_molecular_giant_covalent_network", 2, 15, 2, ["confuses_network_solids_with_molecular_solids"]))
    return q


# --------------------------------------------------------------------------- #
# 38_allotropes_of_carbon_diamond_graphite_fullerenes_svg
# --------------------------------------------------------------------------- #
def _build_38_allotropes_of_carbon_diamond_graphite_fullerenes_svg(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    allotropes = [
        {"name": "Diamond", "hybrid": "sp3 tetrahedral", "bonds_per_c": 4, "conducts": "non-conductor (all 4 valence electrons bonded)", "hardness": "exceptionally hard (Mohs 10)", "layers": False},
        {"name": "Graphite", "hybrid": "sp2 planar hexagonal layers", "bonds_per_c": 3, "conducts": "good electrical conductor (1 delocalised electron per carbon free between layers)", "hardness": "soft and slippery (weak van der Waals forces between sheets)", "layers": True},
    ]
    al = r.choice(allotropes)

    # Simplified graphic showing graphite layers vs diamond tetrahedral
    svg = f"""<svg viewBox="0 0 460 200" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
  <!-- Allotrope of carbon: {al['name']} -->
  <rect x="30" y="30" width="400" height="140" fill="#F8FAFC" stroke="#334155" stroke-width="2" rx="6" />
  <text x="230" y="60" font-size="16" fill="#0F172A" font-weight="bold" text-anchor="middle">Carbon Allotrope: {al['name']}</text>
  <text x="230" y="90" font-size="13" fill="#2563EB" text-anchor="middle">Structure: {al['hybrid']}</text>
  <text x="230" y="115" font-size="12" fill="#475569" text-anchor="middle">C-C Bonds per Atom: {al['bonds_per_c']}</text>
  <text x="230" y="140" font-size="12" fill="#16A34A" font-weight="bold" text-anchor="middle">Electrical Property: {al['conducts']}</text>
</svg>"""

    prompt = (
        f"\\text{{1. Define the term }} \\textbf{{allotropes}}.\n\n"
        f"\\text{{2. For the carbon allotrope }} \\textbf{{{al['name']}}}:\n"
        f"\\text{{a) State how many covalent bonds each carbon atom forms with neighboring carbon atoms.}}\n"
        f"\\text{{b) Explain why {al['name']} is {al['conducts']} and {al['hardness']}.}}"
    )
    ans = (
        f"1. Allotropes are different structural modifications of the same element in the same physical state. "
        f"2. a) Each carbon forms {al['bonds_per_c']} covalent bonds. "
        f"b) Structural reason: {al['hybrid']}; {al['conducts']}; {al['hardness']}."
    )
    q = {
        "id": f"mat10_38_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"Allotropes are different forms of the same element. Diamond: 4 bonds/atom (tetrahedral, insulator, hard). Graphite: 3 bonds/atom (layers, delocalized electrons conduct, soft).",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Allotropes = same element, different crystalline structure.",
            "tier_2": "In diamond each C bonds to 4 carbons; in graphite each C bonds to 3 carbons leaving 1 delocalized electron.",
            "tier_3": f"{al['name']} forms {al['bonds_per_c']} bonds per carbon.",
        },
    }
    q.update(_make_meta("38_allotropes_of_carbon_diamond_graphite_fullerenes_svg", 2, 15, 3, ["believes_diamond_and_graphite_are_different_elements"]))
    return q


# --------------------------------------------------------------------------- #
# 39_percentage_composition_by_mass_calculation
# --------------------------------------------------------------------------- #
def _build_39_percentage_composition_by_mass_calculation(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    compounds = [
        {"name": "Water (H2O)", "formula": "\\text{H}_2\\text{O}", "molar_mass": 18.0, "elem": "Oxygen", "part_mass": 16.0, "pct": 88.89},
        {"name": "Carbon dioxide (CO2)", "formula": "\\text{CO}_2", "molar_mass": 44.0, "elem": "Carbon", "part_mass": 12.0, "pct": 27.27},
        {"name": "Methane (CH4)", "formula": "\\text{CH}_4", "molar_mass": 16.0, "elem": "Hydrogen", "part_mass": 4.0, "pct": 25.0},
        {"name": "Calcium carbonate (CaCO3)", "formula": "\\text{CaCO}_3", "molar_mass": 100.0, "elem": "Calcium", "part_mass": 40.0, "pct": 40.0},
        {"name": "Sulfur trioxide (SO3)", "formula": "\\text{SO}_3", "molar_mass": 80.0, "elem": "Sulfur", "part_mass": 32.0, "pct": 40.0},
    ]
    cp = r.choice(compounds)
    pct_str = _fmt_sa(cp["pct"], 2)

    prompt = (
        f"\\text{{Calculate the percentage by mass of }} \\textbf{{{cp['elem']}}} \\text{{ in }} \\textbf{{{cp['name']}}} ({cp['formula']}).\n\n"
        f"\\text{{Use standard relative atomic masses: H = 1; C = 12; O = 16; S = 32; Ca = 40. Show your step-by-step working.}}"
    )
    ans = f"Molar mass of {cp['formula']} = {cp['molar_mass']} g/mol. % {cp['elem']} = ({cp['part_mass']} / {cp['molar_mass']}) * 100 = {pct_str}%."
    q = {
        "id": f"mat10_39_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"% composition = $\\dfrac{{\\text{{total mass of element}}}}{{\\text{{molar mass of compound}}}} \\times 100 = \\dfrac{{{cp['part_mass']}}}{{{cp['molar_mass']}}} \\times 100 = {pct_str}\\%$.",
        "hints": {
            "tier_1": "Calculate molar mass of the compound first.",
            "tier_2": "Divide the total mass of the specific element by the molar mass and multiply by 100.",
            "tier_3": f"{pct_str}%.",
        },
    }
    q.update(_make_meta("39_percentage_composition_by_mass_calculation", 2, 15, 3, ["forgets_to_multiply_element_by_its_subscript"]))
    return q


# --------------------------------------------------------------------------- #
# 40_empirical_formula_from_percentage_composition
# --------------------------------------------------------------------------- #
def _build_40_empirical_formula_from_percentage_composition(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    scenarios = [
        {"name": "a hydrocarbon", "data": "80% Carbon, 20% Hydrogen", "c_moles": 80.0/12.0, "h_moles": 20.0/1.0, "ratio": "1:3", "emp": "\\text{CH}_3"},
        {"name": "an iron oxide mineral", "data": "70% Iron (Fe, RAM = 56), 30% Oxygen (O, RAM = 16)", "c_moles": 70.0/56.0, "h_moles": 30.0/16.0, "ratio": "2:3", "emp": "\\text{Fe}_2\\text{O}_3"},
        {"name": "a nitrogen oxide gas", "data": "30,4% Nitrogen (N, RAM = 14), 69,6% Oxygen (O, RAM = 16)", "c_moles": 30.4/14.0, "h_moles": 69.6/16.0, "ratio": "1:2", "emp": "\\text{NO}_2"},
        {"name": "a sulfur oxide pollutant", "data": "40% Sulfur (S, RAM = 32), 60% Oxygen (O, RAM = 16)", "c_moles": 40.0/32.0, "h_moles": 60.0/16.0, "ratio": "1:3", "emp": "\\text{SO}_3"},
    ]
    sc = r.choice(scenarios)
    prompt = (
        f"\\text{{Quantitative analysis of a pure chemical sample of {sc['name']} reveals the following percentage composition by mass:}}\n\n"
        f"\\textbf{{{sc['data']}}}.\n\n"
        f"\\text{{1. Define the term }} \\textbf{{empirical formula}}.\n"
        f"\\text{{2. Determine the empirical formula of the compound. Show all mole ratios clearly.}}"
    )
    ans = (
        f"1. The empirical formula is the simplest whole-number ratio of atoms of each element in a compound. "
        f"2. Calculating moles in 100 g: mole ratio = {sc['ratio']} -> Empirical formula is {sc['emp']}."
    )
    q = {
        "id": f"mat10_40_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 5,
        "explanation": f"Assume 100 g sample. Convert mass to moles: $n = m / M$. Divide by smallest mole value to find simplest whole-number ratio ({sc['ratio']}) -> {sc['emp']}.",
        "hints": {
            "tier_1": "Assume a 100 g sample: grams equal percentages.",
            "tier_2": "Calculate moles of each element (m / M), then divide all mole amounts by the smallest value.",
            "tier_3": f"Empirical formula is {sc['emp']}.",
        },
    }
    q.update(_make_meta("40_empirical_formula_from_percentage_composition", 2, 15, 4, ["uses_mass_ratio_directly_as_subscripts"]))
    return q


# --------------------------------------------------------------------------- #
# 41_molecular_formula_from_empirical_formula_and_molar_mass
# --------------------------------------------------------------------------- #
def _build_41_molecular_formula_from_empirical_formula_and_molar_mass(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    compounds = [
        {"name": "Butane", "emp": "\\text{CH}_3", "emp_mass": 15.0, "mol_mass": 30.0, "factor": 2, "mol_form": "\\text{C}_2\\text{H}_6"},
        {"name": "Glucose", "emp": "\\text{CH}_2\\text{O}", "emp_mass": 30.0, "mol_mass": 180.0, "factor": 6, "mol_form": "\\text{C}_6\\text{H}_{12}\\text{O}_6"},
        {"name": "Benzene", "emp": "\\text{CH}", "emp_mass": 13.0, "mol_mass": 78.0, "factor": 6, "mol_form": "\\text{C}_6\\text{H}_6"},
        {"name": "Hydrogen peroxide", "emp": "\\text{HO}", "emp_mass": 17.0, "mol_mass": 34.0, "factor": 2, "mol_form": "\\text{H}_2\\text{O}_2"},
        {"name": "Dinitrogen tetroxide", "emp": "\\text{NO}_2", "emp_mass": 46.0, "mol_mass": 92.0, "factor": 2, "mol_form": "\\text{N}_2\\text{O}_4"},
    ]
    cp = r.choice(compounds)
    prompt = (
        f"\\text{{A chemical compound has an empirical formula of }} \\textbf{{{cp['emp']}}} "
        f"\\text{{ and an experimentally determined molar mass of }} \\textbf{{{cp['mol_mass']}\\text{{ g}}\\cdot\\text{{mol}}^{{-1}}}}.\n\n"
        f"\\text{{1. Distinguish between an empirical formula and a molecular formula.}}\n"
        f"\\text{{2. Calculate the scaling factor }} n = \\dfrac{{\\text{{Molar Mass}}}}{{\\text{{Empirical Mass}}}}.\n"
        f"\\text{{3. Determine the actual molecular formula of the compound.}}"
    )
    ans = (
        f"1. An empirical formula gives the simplest whole-number ratio of atoms, whereas a molecular formula gives the actual number of atoms of each element in a molecule. "
        f"2. n = {cp['mol_mass']} / {cp['emp_mass']} = {cp['factor']}. "
        f"3. Molecular formula = ({cp['emp']})_{cp['factor']} = {cp['mol_form']}."
    )
    q = {
        "id": f"mat10_41_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"Empirical mass = {cp['emp_mass']} g/mol. Ratio $n = {cp['mol_mass']} / {cp['emp_mass']} = {cp['factor']}$. Multiply subscripts by {cp['factor']} -> {cp['mol_form']}.",
        "hints": {
            "tier_1": "Calculate the mass of the empirical formula first.",
            "tier_2": "Divide the given molar mass by the empirical formula mass to find n.",
            "tier_3": f"Molecular formula: {cp['mol_form']}.",
        },
    }
    q.update(_make_meta("41_molecular_formula_from_empirical_formula_and_molar_mass", 2, 15, 3, ["leaves_formula_in_unmultiplied_bracket_form"]))
    return q


# --------------------------------------------------------------------------- #
# 42_water_of_crystallisation_hydrated_salts_formula
# --------------------------------------------------------------------------- #
def _build_42_water_of_crystallisation_hydrated_salts_formula(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    salts = [
        {"name": "hydrated copper(II) sulfate", "anhydrous": "\\text{CuSO}_4", "m_anhydrous": 159.5, "x": 5, "m_water": 90.0, "total_mass": 249.5, "formula": "\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O}"},
        {"name": "hydrated magnesium sulfate (Epsom salts)", "anhydrous": "\\text{MgSO}_4", "m_anhydrous": 120.4, "x": 7, "m_water": 126.0, "total_mass": 246.4, "formula": "\\text{MgSO}_4\\cdot 7\\text{H}_2\\text{O}"},
        {"name": "hydrated cobalt(II) chloride", "anhydrous": "\\text{CoCl}_2", "m_anhydrous": 129.8, "x": 6, "m_water": 108.0, "total_mass": 237.8, "formula": "\\text{CoCl}_2\\cdot 6\\text{H}_2\\text{O}"},
    ]
    salt = r.choice(salts)
    pct_water = round((salt["m_water"] / salt["total_mass"]) * 100.0, 1)

    prompt = (
        f"\\text{{A sample of {salt['name']} ({salt['anhydrous']}\\cdot x\\text{{H}}_2\\text{{O}}) is heated strongly in a crucible to drive off all water of crystallisation:}}\n\n"
        f"\\text{{Initial mass of hydrated salt = }} {salt['total_mass']}\\text{{ g}}\n\n"
        f"\\text{{Final mass of anhydrous salt ({salt['anhydrous']}) = }} {salt['m_anhydrous']}\\text{{ g}}\n\n"
        f"\\text{{1. Define the term }} \\textbf{{water of crystallisation}}.\n"
        f"\\text{{2. Calculate the mass of water driven off as steam.}}\n"
        f"\\text{{3. Calculate the value of the integer }} x \\text{{ in the formula }} {salt['anhydrous']}\\cdot x\\text{{H}}_2\\text{{O}}."
    )
    ans = (
        f"1. Water of crystallisation is water that is chemically stoichiometric and trapped in the crystalline framework of a salt. "
        f"2. Mass of water = {salt['total_mass']} - {salt['m_anhydrous']} = {salt['m_water']} g. "
        f"3. Moles of anhydrous salt = {salt['m_anhydrous']} / {salt['m_anhydrous']} = 1,0 mol; Moles of water = {salt['m_water']} / 18,0 = {salt['x']},0 mol -> x = {salt['x']}. Formula: {salt['formula']}."
    )
    q = {
        "id": f"mat10_42_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 5,
        "explanation": f"Mass of water = {salt['total_mass']} - {salt['m_anhydrous']} = {salt['m_water']} g. Mole ratio of salt to water = 1 : {salt['x']}. Hence x = {salt['x']}.",
        "hints": {
            "tier_1": "Mass of water lost = initial mass of hydrate - final mass of dry anhydrous salt.",
            "tier_2": "Convert both masses into moles: n(salt) = m/M and n(H2O) = m/18. Divide n(H2O) by n(salt) to find x.",
            "tier_3": f"x = {salt['x']}.",
        },
    }
    q.update(_make_meta("42_water_of_crystallisation_hydrated_salts_formula", 2, 15, 4, ["divides_water_mass_by_total_mass_instead_of_salt_moles"]))
    return q


# --------------------------------------------------------------------------- #
# 43_concentration_of_solutions_standard_volumetric_prep
# --------------------------------------------------------------------------- #
def _build_43_concentration_of_solutions_standard_volumetric_prep(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    salts = [
        {"name": "sodium hydroxide", "formula": "\\text{NaOH}", "M": 40.0},
        {"name": "sodium chloride", "formula": "\\text{NaCl}", "M": 58.5},
        {"name": "sodium carbonate", "formula": "\\text{Na}_2\\text{CO}_3", "M": 106.0},
        {"name": "potassium permanganate", "formula": "\\text{KMnO}_4", "M": 158.0},
    ]
    s = r.choice(salts)
    conc = r.choice([0.1, 0.2, 0.25, 0.5])  # mol/dm3
    vol_cm3 = r.choice([250, 500, 1000])  # cm3
    vol_dm3 = vol_cm3 / 1000.0
    moles = conc * vol_dm3
    mass = round(moles * s["M"], 2)
    conc_str = _fmt_sa(conc, 2)
    mass_str = _fmt_sa(mass, 2)

    prompt = (
        f"\\text{{A laboratory technician needs to prepare exactly }} {vol_cm3}\\text{{ cm}}^3 \\text{{ of a }} "
        f"{conc_str}\\text{{ mol}}\\cdot\\text{{dm}}^{{-3}} \\text{{ standard solution of }} \\textbf{{{s['name']}}} ({s['formula']}, M = {s['M']}\\text{{ g/mol}}).\n\n"
        f"\\text{{1. Convert the volume from cm}}^3 \\text{{ to dm}}^3.\n"
        f"\\text{{2. Calculate the number of moles of {s['formula']} required.}}\n"
        f"\\text{{3. Calculate the exact mass of {s['name']} that must be weighed on an analytical balance.}}"
    )
    ans = (
        f"1. V = {vol_cm3} / 1000 = {_fmt_sa(vol_dm3, 3)} dm^3. "
        f"2. n = c * V = {conc_str} * {_fmt_sa(vol_dm3, 3)} = {_fmt_sa(moles, 3)} mol. "
        f"3. m = n * M = {_fmt_sa(moles, 3)} * {s['M']} = {mass_str} g."
    )
    q = {
        "id": f"mat10_43_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"Using $c = n/V \\implies n = c \\times V = {conc_str} \\times {_fmt_sa(vol_dm3, 3)} = {_fmt_sa(moles, 3)}\\text{{ mol}}$. Then $m = n \\times M = {mass_str}\\text{{ g}}$.",
        "hints": {
            "tier_1": "Remember: 1 dm3 = 1000 cm3. Divide cm3 by 1000.",
            "tier_2": "Calculate moles using n = c * V, then mass using m = n * M.",
            "tier_3": f"Mass = {mass_str} g.",
        },
    }
    q.update(_make_meta("43_concentration_of_solutions_standard_volumetric_prep", 3, 20, 3, ["cm3_to_dm3_volume_conversion"]))
    return q


# --------------------------------------------------------------------------- #
# 44_hydrosphere_water_cycle_reservoirs_and_phase_changes_svg
# --------------------------------------------------------------------------- #
def _build_44_hydrosphere_water_cycle_reservoirs_and_phase_changes_svg(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    procs = [
        {"name": "Evaporation", "desc": "solar energy converts liquid water from oceans and dams into atmospheric water vapour (gas)", "col": "#0284C7"},
        {"name": "Transpiration", "desc": "plants release water vapour into the atmosphere through stomata in leaves", "col": "#16A34A"},
        {"name": "Condensation", "desc": "cooling water vapour condenses around microscopic dust particles to form clouds (liquid droplets)", "col": "#9333EA"},
        {"name": "Precipitation", "desc": "condensed water droplets become heavy and fall to the ground as rain, hail, or snow", "col": "#2563EB"},
    ]
    target = r.choice(procs)

    # Simplified water cycle schematic SVG with dynamic focus
    svg = f"""<svg viewBox="0 0 460 220" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
  <!-- Hydrosphere water cycle schematic: Focus on {target['name']} -->
  <!-- Sun -->
  <circle cx="60" cy="50" r="22" fill="#FBBF24" />
  <text x="60" y="55" font-size="10" fill="#78350F" text-anchor="middle" font-weight="bold">Sun</text>

  <!-- Cloud -->
  <ellipse cx="230" cy="50" rx="45" ry="20" fill="#E2E8F0" stroke="#94A3B8" stroke-width="1.5" />
  <text x="230" y="54" font-size="11" fill="#334155" text-anchor="middle">Clouds</text>

  <!-- Mountain / Land -->
  <polygon points="260,180 340,90 420,180" fill="#CBD5E1" stroke="#64748B" stroke-width="2" />
  <text x="340" y="150" font-size="11" fill="#334155" text-anchor="middle">Land / Mountains</text>

  <!-- Ocean -->
  <rect x="30" y="170" width="400" height="35" fill="#38BDF8" rx="4" />
  <text x="140" y="192" font-size="12" fill="#0C4A6E" font-weight="bold">Ocean / Hydrosphere</text>

  <!-- Upward evaporation arrow -->
  <line x1="120" y1="160" x2="120" y2="85" stroke="#0284C7" stroke-width="2.5" stroke-dasharray="4,4" />
  <polygon points="115,85 120,75 125,85" fill="#0284C7" />
  <text x="105" y="125" font-size="10" fill="#0284C7" text-anchor="end">Evaporation</text>

  <!-- Downward precipitation arrow -->
  <line x1="270" y1="75" x2="270" y2="140" stroke="#2563EB" stroke-width="2.5" />
  <polygon points="265,140 270,150 275,140" fill="#2563EB" />
  <text x="285" y="115" font-size="10" fill="#2563EB">Precipitation</text>

  <!-- Focus Tag -->
  <rect x="320" y="20" width="120" height="25" fill="#EFF6FF" stroke="{target['col']}" stroke-width="1.5" rx="4" />
  <text x="380" y="37" font-size="11" fill="{target['col']}" font-weight="bold" text-anchor="middle">{target['name']}</text>
</svg>"""

    prompt = (
        f"\\text{{Refer to the schematic diagram illustrating the Earth's }} \\textbf{{Hydrosphere and Water Cycle}} (\\text{{focus: }} {target['name']}):\n\n"
        f"\\text{{1. Define the term }} \\textbf{{hydrosphere}}.\n"
        f"\\text{{2. Explain the physical mechanism and energy changes involved in }} \\textbf{{{target['name']}}}.\n"
        f"\\text{{3. Identify which primary source of external energy powers the global water cycle.}}"
    )
    ans = (
        f"1. The hydrosphere is the total mass of water found on, under, and over the surface of the Earth (oceans, ice caps, rivers, groundwater, atmosphere). "
        f"2. {target['desc'].capitalize()}. "
        f"3. Solar radiation (energy from the Sun)."
    )
    q = {
        "id": f"mat10_44_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"The hydrosphere encompasses all Earth's water. {target['name']}: {target['desc']}. The water cycle is powered by solar energy.",
        "diagram_spec": {"kind": "inline_svg", "svg": svg, "diagram_role": "context"},
        "hints": {
            "tier_1": "Hydrosphere = all water on Earth.",
            "tier_2": "The sun heats water, driving evaporation.",
            "tier_3": f"Process is {target['name']}: {target['desc']}.",
        },
    }
    q.update(_make_meta("44_hydrosphere_water_cycle_reservoirs_and_phase_changes_svg", 4, 15, 3, ["believes_water_cycle_creates_new_water"]))
    return q


# --------------------------------------------------------------------------- #
# 45_hydrosphere_water_purity_total_dissolved_solids_tds
# --------------------------------------------------------------------------- #
def _build_45_hydrosphere_water_purity_total_dissolved_solids_tds(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    samples = [
        {"source": "Municipal tap water in Johannesburg", "tds": 140, "safe": "Safe for drinking (< 300 mg/L is excellent)"},
        {"source": "Untreated borehole water from a rural farming district", "tds": 650, "safe": "Poor drinking water quality (exceeds recommended 500 mg/L limit; requires filtration)"},
        {"source": "Seawater collected near Durban harbour", "tds": 35000, "safe": "Unsafe for drinking (hyper-saline; requires reverse osmosis desalination)"},
        {"source": "Deionised distilled water prepared for laboratory titrations", "tds": 2, "safe": "Ultra-pure (near-zero mineral ion content)"},
    ]
    s = r.choice(samples)
    prompt = (
        f"\\text{{Water quality testing of a sample from }} \\textbf{{{s['source']}}} \\text{{ yields a Total Dissolved Solids (TDS) reading of }} "
        f"\\textbf{{{s['tds']}\\text{{ mg}}\\cdot\\text{{L}}^{{-1}}}}.\n\n"
        f"\\text{{1. Explain what }} \\textbf{{Total Dissolved Solids (TDS)}} \\text{{ measures in an aqueous sample.}}\n"
        f"\\text{{2. State two common mineral ions that contribute to the TDS value in natural water bodies.}}\n"
        f"\\text{{3. Evaluate whether this water sample is suitable for human drinking consumption without prior treatment.}}"
    )
    ans = f"1. TDS measures the combined total content of all inorganic mineral salts and small amounts of organic matter dissolved in water. 2. Ca2+, Mg2+, Na+, Cl-, SO4^2-, HCO3^-. 3. {s['safe']}."
    q = {
        "id": f"mat10_45_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"TDS measures dissolved mineral salts. Common ions include calcium, magnesium, sodium, chloride, sulfate. Sample assessment: {s['safe']}.",
        "hints": {
            "tier_1": "TDS = Total Dissolved Solids, usually measured in mg/L or ppm.",
            "tier_2": "Drinking water standards recommend TDS < 500 mg/L.",
            "tier_3": f"{s['safe']}.",
        },
    }
    q.update(_make_meta("45_hydrosphere_water_purity_total_dissolved_solids_tds", 4, 15, 3, ["confuses_tds_with_suspended_insoluble_solids"]))
    return q


# --------------------------------------------------------------------------- #
# 46_hydrosphere_hard_vs_soft_water_and_precipitation_chemistry
# --------------------------------------------------------------------------- #
def _build_46_hydrosphere_hard_vs_soft_water_and_precipitation_chemistry(r: random.Random, difficulty: str = "medium") -> Dict[str, Any]:
    scenarios = [
        {"type": "Temporary hard water", "ion": "\\text{Ca(HCO}_3\\text{)}_2", "removal": "Boiling causes calcium bicarbonate to decompose and precipitate as insoluble calcium carbonate scale: Ca(HCO3)2 -> CaCO3(s) + H2O + CO2"},
        {"type": "Permanent hard water", "ion": "\\text{CaSO}_4 \\text{ or } \\text{MgSO}_4", "removal": "Cannot be softened by boiling; requires chemical precipitation using washing soda (sodium carbonate, Na2CO3) or ion exchange resin columns"},
    ]
    sc = r.choice(scenarios)
    prompt = (
        f"\\text{{In an investigation into domestic water quality in a dolomitic limestone region:}}\n\n"
        f"\\text{{1. Distinguish between }} \\textbf{{hard water}} \\text{{ and }} \\textbf{{soft water}} \\text{{ in terms of mineral ion content and soap lathering.}}\n"
        f"\\text{{2. For }} \\textbf{{{sc['type']}}} \\text{{ (containing {sc['ion']}):}}\n"
        f"\\text{{Explain how this hardness can be removed to soften the water.}}"
    )
    ans = (
        f"1. Hard water contains high concentrations of dissolved multivalent mineral cations (principally Ca2+ and Mg2+) and does not readily form a lather with soap, forming scum instead. Soft water contains low mineral concentrations and lathers easily. "
        f"2. Softening method: {sc['removal']}."
    )
    q = {
        "id": f"mat10_46_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 4,
        "explanation": f"Hard water has dissolved Ca2+/Mg2+. Temporary hardness ({sc['ion']}) is softened by boiling; permanent hardness requires ion exchange or washing soda.",
        "hints": {
            "tier_1": "Hard water = rich in Ca2+ and Mg2+; fails to lather with soap.",
            "tier_2": "Temporary hardness decomposes upon boiling to form limescale; permanent hardness requires chemical softening.",
            "tier_3": f"{sc['removal']}.",
        },
    }
    q.update(_make_meta("46_hydrosphere_hard_vs_soft_water_and_precipitation_chemistry", 4, 15, 3, ["believes_all_hard_water_can_be_softened_by_boiling"]))
    return q


# --------------------------------------------------------------------------- #
# 47_units_of_measurement_si_base_units_and_derived_units
# --------------------------------------------------------------------------- #
def _build_47_units_of_measurement_si_base_units_and_derived_units(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    quantities = [
        {"name": "Force", "sym": "F", "si": "newton (N)", "base": "\\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-2}", "formula": "F = m \\cdot a"},
        {"name": "Pressure", "sym": "p", "si": "pascal (Pa)", "base": "\\text{kg}\\cdot\\text{m}^{-1}\\cdot\\text{s}^{-2}", "formula": "p = F / A"},
        {"name": "Energy / Work", "sym": "E / W", "si": "joule (J)", "base": "\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2}", "formula": "W = F \\cdot s"},
        {"name": "Power", "sym": "P", "si": "watt (W)", "base": "\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}", "formula": "P = W / \\Delta t"},
        {"name": "Electric Charge", "sym": "Q", "si": "coulomb (C)", "base": "\\text{A}\\cdot\\text{s}", "formula": "Q = I \\cdot \\Delta t"},
        {"name": "Potential Difference", "sym": "V", "si": "volt (V)", "base": "\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\cdot\\text{A}^{-1}", "formula": "V = W / Q"},
    ]
    q_item = r.choice(quantities)
    prompt = (
        f"\\text{{In scientific measurement, physical quantities are expressed in SI units.}}\n\n"
        f"\\text{{For the derived physical quantity }} \\textbf{{{q_item['name']}}} ({q_item['sym']}):\n"
        f"\\text{{1. State its special SI unit name and symbol.}}\n"
        f"\\text{{2. State its defining physical equation ({q_item['formula']}).}}\n"
        f"\\text{{3. Express this derived unit strictly in terms of }} \\textbf{{SI base units}} \\text{{ (kg, m, s, A, mol, K).}}"
    )
    ans = f"1. {q_item['si']}. 2. {q_item['formula']}. 3. In SI base units: {q_item['base']}."
    q = {
        "id": f"mat10_47_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"{q_item['name']} has SI unit {q_item['si']}. Using {q_item['formula']}, base units evaluate to {q_item['base']}.",
        "hints": {
            "tier_1": "Substitute base units of mass (kg), length (m), time (s), and current (A) into the defining formula.",
            "tier_2": "F = m*a gives kg * m/s^2 = N. Then substitute into the definition.",
            "tier_3": f"{q_item['si']} = {q_item['base']}.",
        },
    }
    q.update(_make_meta("47_units_of_measurement_si_base_units_and_derived_units", 4, 15, 3, ["confuses_derived_unit_with_base_unit"]))
    return q


# --------------------------------------------------------------------------- #
# 48_metric_prefix_conversions_micro_milli_kilo_mega
# --------------------------------------------------------------------------- #
def _build_48_metric_prefix_conversions_micro_milli_kilo_mega(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    conversions = [
        {"val": 450, "from_u": "\\text{cm}^3", "to_u": "\\text{dm}^3", "factor": 1e-3, "res": 0.45, "unit_name": "volume"},
        {"val": 25, "from_u": "\\text{mA}", "to_u": "\\text{A}", "factor": 1e-3, "res": 0.025, "unit_name": "electric current"},
        {"val": 4.8, "from_u": "\\mu\\text{C}", "to_u": "\\text{C}", "factor": 1e-6, "res": 4.8e-6, "unit_name": "electric charge"},
        {"val": 72, "from_u": "\\text{km/h}", "to_u": "\\text{m/s}", "factor": 1.0/3.6, "res": 20.0, "unit_name": "velocity"},
        {"val": 1500, "from_u": "\\text{kJ}", "to_u": "\\text{J}", "factor": 1000.0, "res": 1.5e6, "unit_name": "energy"},
        {"val": 2.5, "from_u": "\\text{dm}^3", "to_u": "\\text{m}^3", "factor": 1e-3, "res": 0.0025, "unit_name": "volume"},
    ]
    conv = r.choice(conversions)
    v_str = _fmt_sa(conv["val"])
    res_str = f"{conv['res']:.2e}" if conv["res"] < 1e-3 or conv["res"] > 1e4 else _fmt_sa(conv["res"], 4)

    prompt = (
        f"\\text{{Perform the following standard scientific unit conversion for {conv['unit_name']}:}}\n\n"
        f"\\text{{Convert }} \\textbf{{{v_str} {conv['from_u']}}} \\text{{ to }} \\textbf{{{conv['to_u']}}}.\n\n"
        f"\\text{{Show the multiplication conversion factor clearly.}}"
    )
    ans = f"{v_str} {conv['from_u']} = {res_str} {conv['to_u']}."
    q = {
        "id": f"mat10_48_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 2,
        "explanation": f"Multiply {v_str} by conversion factor {conv['factor']} -> {res_str} {conv['to_u']}.",
        "hints": {
            "tier_1": "Recall: milli = 10^-3, micro = 10^-6, kilo = 10^3, 1 dm3 = 1000 cm3.",
            "tier_2": "Check whether you are moving from smaller to larger or vice-versa.",
            "tier_3": f"Result is {res_str} {conv['to_u']}.",
        },
    }
    q.update(_make_meta("48_metric_prefix_conversions_micro_milli_kilo_mega", 4, 15, 2, ["cm3_to_dm3_volume_conversion"]))
    return q


# --------------------------------------------------------------------------- #
# 49_scientific_notation_and_significant_figures_in_measurement
# --------------------------------------------------------------------------- #
def _build_49_scientific_notation_and_significant_figures_in_measurement(r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    numbers = [
        {"raw": "0.000450", "sig_figs": 3, "sci": "4,50 \\times 10^{-4}", "reason": "leading zeros are not significant; trailing zero after decimal is significant"},
        {"raw": "304000", "sig_figs": 3, "sci": "3,04 \\times 10^{5}", "reason": "captured zeros between non-zero digits are significant; trailing zeros without a decimal are ambiguous/not significant"},
        {"raw": "0.05020", "sig_figs": 4, "sci": "5,020 \\times 10^{-2}", "reason": "leading zeros are placeholders; trapped zero and trailing zero are significant"},
        {"raw": "12.00", "sig_figs": 4, "sci": "1,200 \\times 10^{1}", "reason": "all digits after the decimal following non-zero numbers indicate precision and are significant"},
    ]
    num = r.choice(numbers)
    prompt = (
        f"\\text{{A laboratory measurement records the numerical quantity: }} \\textbf{{{num['raw']}}}.\n\n"
        f"\\text{{1. State the number of significant figures in this measurement.}}\n"
        f"\\text{{2. Justify your answer based on the rules for significant figures.}}\n"
        f"\\text{{3. Express the measurement in standard scientific notation (with South African comma decimal separator).}}"
    )
    ans = f"1. {num['sig_figs']} significant figures. 2. {num['reason']}. 3. {num['sci']}."
    q = {
        "id": f"mat10_49_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 3,
        "explanation": f"{num['raw']} has {num['sig_figs']} significant figures because {num['reason']}. In scientific notation: {num['sci']}.",
        "hints": {
            "tier_1": "Leading zeros are never significant; trailing zeros after a decimal point are significant.",
            "tier_2": "Count digits that reflect measurement precision.",
            "tier_3": f"{num['sig_figs']} sig figs; {num['sci']}.",
        },
    }
    q.update(_make_meta("49_scientific_notation_and_significant_figures_in_measurement", 4, 15, 3, ["counts_leading_zeros_as_significant"]))
    return q


# --------------------------------------------------------------------------- #
# 50_matter_and_materials_diagnostic_autopsy_and_misconception_repair
# --------------------------------------------------------------------------- #
def _build_50_matter_and_materials_diagnostic_autopsy_and_misconception_repair(r: random.Random, difficulty: str = "hard") -> Dict[str, Any]:
    misconceptions = [
        {
            "statement": "When water boils at 100 °C, the covalent bonds between hydrogen and oxygen inside the water molecule break to produce hydrogen and oxygen gas.",
            "validity": "FALSE",
            "autopsy": "Phase changes are physical changes, not chemical changes. Boiling only overcomes weak intermolecular hydrogen bonds between separate H2O molecules; the strong intramolecular covalent O-H bonds inside the molecules remain completely intact.",
            "repair": "Distinguish between intermolecular forces (broken during boiling) and intramolecular covalent bonds (broken only in chemical decomposition reactions like electrolysis)."
        },
        {
            "statement": "A sodium ion (Na+) is larger in radius than a neutral sodium atom (Na) because it is positively charged and attracts extra space.",
            "validity": "FALSE",
            "autopsy": "When a neutral sodium atom (2,8,1) forms a sodium cation (2,8), it completely loses its outermost principal electron shell (n=3). The remaining 10 electrons in n=2 are pulled inward by 11 protons with increased effective nuclear force.",
            "repair": "Cations are always significantly smaller than their parent neutral atoms due to the loss of an electron shell and higher proton-to-electron ratio."
        },
        {
            "statement": "During the melting of ice at 0 °C, the temperature rises steadily because heat energy is continuously added to the beaker.",
            "validity": "FALSE",
            "autopsy": "During a phase transition at the melting point, temperature remains strictly constant at 0 °C. The added heat is latent heat of fusion, which increases potential energy by weakening intermolecular bonds without increasing the average kinetic energy.",
            "repair": "Temperature is directly proportional to average kinetic energy. Along a phase change plateau, kinetic energy is constant, so temperature does not rise until all solid has melted."
        },
    ]
    diag = r.choice(misconceptions)
    prompt = (
        f"\\text{{A Grade 10 learner writes the following explanation in a Physical Sciences exam debrief:}}\n\n"
        f"\\text{{''\\textit{{{diag['statement']}}}''}}\n\n"
        f"\\text{{1. State whether this statement is }} \\textbf{{TRUE}} \\text{{ or }} \\textbf{{FALSE}}.\n"
        f"\\text{{2. Provide a rigorous diagnostic autopsy explaining the fundamental misconception in this statement.}}\n"
        f"\\text{{3. Formulate the scientifically correct repair principle.}}"
    )
    ans = f"1. {diag['validity']}. 2. Diagnostic autopsy: {diag['autopsy']} 3. Scientific repair: {diag['repair']}"
    q = {
        "id": f"mat10_50_{r.randint(1000, 9999)}",
        "question": prompt,
        "question_text": prompt,
        "prompt": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "answer": ans,
        "marks": 5,
        "explanation": f"Diagnostic verdict: {diag['validity']}. {diag['autopsy']} {diag['repair']}",
        "hints": {
            "tier_1": "Carefully distinguish physical phase changes from chemical bond breaking, or cation sizes from neutral atoms.",
            "tier_2": "Examine whether intermolecular or intramolecular bonds are involved.",
            "tier_3": f"Statement is {diag['validity']}.",
        },
    }
    q.update(_make_meta("50_matter_and_materials_diagnostic_autopsy_and_misconception_repair", 1, 20, 5, ["confuses_intermolecular_and_intramolecular_bonds"]))
    return q


# Export mapping
BUILDERS_26_50: Dict[str, Any] = {
    "26_lewis_dot_diagrams_neutral_atoms": _build_26_lewis_dot_diagrams_neutral_atoms,
    "27_covalent_bonding_electron_sharing_diatomic_molecules_svg": _build_27_covalent_bonding_electron_sharing_diatomic_molecules_svg,
    "28_covalent_bonding_polyatomic_molecules_water_ammonia_methane": _build_28_covalent_bonding_polyatomic_molecules_water_ammonia_methane,
    "29_ionic_bonding_electron_transfer_and_ion_formation": _build_29_ionic_bonding_electron_transfer_and_ion_formation,
    "30_ionic_crystal_lattice_structure_and_properties_svg": _build_30_ionic_crystal_lattice_structure_and_properties_svg,
    "31_metallic_bonding_sea_of_delocalised_electrons_svg": _build_31_metallic_bonding_sea_of_delocalised_electrons_svg,
    "32_chemical_formula_writing_binary_ionic_compounds": _build_32_chemical_formula_writing_binary_ionic_compounds,
    "33_chemical_formula_writing_polyatomic_ionic_compounds": _build_33_chemical_formula_writing_polyatomic_ionic_compounds,
    "34_naming_covalent_and_ionic_chemical_compounds": _build_34_naming_covalent_and_ionic_chemical_compounds,
    "35_physical_properties_correlated_to_bonding_type": _build_35_physical_properties_correlated_to_bonding_type,
    "36_electronegativity_difference_and_bond_polarity_classification": _build_36_electronegativity_difference_and_bond_polarity_classification,
    "37_particles_nature_atomic_molecular_giant_covalent_network": _build_37_particles_nature_atomic_molecular_giant_covalent_network,
    "38_allotropes_of_carbon_diamond_graphite_fullerenes_svg": _build_38_allotropes_of_carbon_diamond_graphite_fullerenes_svg,
    "39_percentage_composition_by_mass_calculation": _build_39_percentage_composition_by_mass_calculation,
    "40_empirical_formula_from_percentage_composition": _build_40_empirical_formula_from_percentage_composition,
    "41_molecular_formula_from_empirical_formula_and_molar_mass": _build_41_molecular_formula_from_empirical_formula_and_molar_mass,
    "42_water_of_crystallisation_hydrated_salts_formula": _build_42_water_of_crystallisation_hydrated_salts_formula,
    "43_concentration_of_solutions_standard_volumetric_prep": _build_43_concentration_of_solutions_standard_volumetric_prep,
    "44_hydrosphere_water_cycle_reservoirs_and_phase_changes_svg": _build_44_hydrosphere_water_cycle_reservoirs_and_phase_changes_svg,
    "45_hydrosphere_water_purity_total_dissolved_solids_tds": _build_45_hydrosphere_water_purity_total_dissolved_solids_tds,
    "46_hydrosphere_hard_vs_soft_water_and_precipitation_chemistry": _build_46_hydrosphere_hard_vs_soft_water_and_precipitation_chemistry,
    "47_units_of_measurement_si_base_units_and_derived_units": _build_47_units_of_measurement_si_base_units_and_derived_units,
    "48_metric_prefix_conversions_micro_milli_kilo_mega": _build_48_metric_prefix_conversions_micro_milli_kilo_mega,
    "49_scientific_notation_and_significant_figures_in_measurement": _build_49_scientific_notation_and_significant_figures_in_measurement,
    "50_matter_and_materials_diagnostic_autopsy_and_misconception_repair": _build_50_matter_and_materials_diagnostic_autopsy_and_misconception_repair,
}
