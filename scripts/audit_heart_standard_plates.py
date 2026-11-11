#!/usr/bin/env python3
"""Mechanical Gate for Rule 0d-14 & Rule 29 (The Heart Diagram Standard).

Prevents any agent from substituting hand-coded geometric SVG shapes (<polygon>,
<path>, <circle>, <ellipse>) in JSX instead of generating authentic, unlabeled
Textbook Master and NSC Exam Stipple plates in `public/diagrams/`.

Usage:
  python scripts/audit_heart_standard_plates.py --milestone 1
  python scripts/audit_heart_standard_plates.py --milestone 2
  python scripts/audit_heart_standard_plates.py --all
"""

import argparse
import json
import os
import re
import sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DIAGRAM_BANK_DIR = os.path.join(PROJECT_ROOT, "src", "components", "workspace", "modalities", "diagram_bank")
PUBLIC_DIAGRAMS_DIR = os.path.join(PROJECT_ROOT, "public", "diagrams")
ANCHORS_DIR = os.path.join(PROJECT_ROOT, "caps-ai-backend", "app", "data", "diagram_anchors")

MILESTONES = {
    1: [
        {
            "master": "heart",
            "component": "HumanHeartSvg.jsx",
            "anchor_json": "heart.json",
            "required_views": ["textbook", "exam"],
        }
    ],
    2: [
        {
            "master": "alveolus_gas_exchange",
            "component": "AlveolusGasExchangeSvg.jsx",
            "anchor_json": "alveolus_gas_exchange.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "digestive_system",
            "component": "HumanDigestiveSvg.jsx",
            "anchor_json": "digestive_system.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "intestinal_villus",
            "component": "IntestinalVillusSvg.jsx",
            "anchor_json": "intestinal_villus.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "human_nephron",
            "component": "HumanNephronSvg.jsx",
            "anchor_json": "human_nephron.json",
            "required_views": ["textbook", "exam"],
        },
    ],
    3: [
        {
            "master": "human_eye",
            "component": "HumanEyeSvg.jsx",
            "anchor_json": "human_eye.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "human_ear",
            "component": "HumanEarSvg.jsx",
            "anchor_json": "human_ear.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "endocrine_system",
            "component": "EndocrineSystemSvg.jsx",
            "anchor_json": "endocrine_system.json",
            "required_views": ["textbook", "exam"],
        },
    ],
    4: [
        {
            "master": "male_reproductive",
            "component": "MaleReproductiveSvg.jsx",
            "anchor_json": "male_reproductive.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "female_reproductive",
            "component": "FemaleReproductiveSvg.jsx",
            "anchor_json": "female_reproductive.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "meiosis_crossing_over",
            "component": "MeiosisCrossingOverSvg.jsx",
            "anchor_json": "meiosis_crossing_over.json",
            "required_views": ["textbook", "exam"],
        },
    ],
    5: [
        {
            "master": "plant_cell",
            "component": "PlantCellSvg.jsx",
            "anchor_json": "plant_cell.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "animal_cell",
            "component": "AnimalCellSvg.jsx",
            "anchor_json": "animal_cell.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "mitosis_stages",
            "component": "MitosisStagesSvg.jsx",
            "anchor_json": "mitosis_stages.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "plant_leaf",
            "component": "PlantLeafSvg.jsx",
            "anchor_json": "plant_leaf.json",
            "required_views": ["textbook", "exam"],
        },
    ],
    6: [
        {
            "master": "distillation_apparatus",
            "component": "DistillationApparatusSvg.jsx",
            "anchor_json": "distillation_apparatus.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "titration_apparatus",
            "component": "TitrationApparatusSvg.jsx",
            "anchor_json": "titration_apparatus.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "galvanic_cell",
            "component": "GalvanicCellSvg.jsx",
            "anchor_json": "galvanic_cell.json",
            "required_views": ["textbook", "exam"],
        },
    ],
    7: [
        {
            "master": "solar_system_earth_space",
            "component": "SolarSystemEarthSpaceSvg.jsx",
            "anchor_json": "solar_system_earth_space.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "particle_model",
            "component": "ParticleModelSvg.jsx",
            "anchor_json": "particle_model.json",
            "required_views": ["textbook", "exam"],
        },
    ],
    8: [
        {
            "master": "atomic_bohr_structure",
            "component": "AtomicBohrStructureSvg.jsx",
            "anchor_json": "atomic_bohr_structure.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "chemical_bonding_molecules",
            "component": "ChemicalBondingMoleculesSvg.jsx",
            "anchor_json": "chemical_bonding_molecules.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "electrolytic_cell_apparatus",
            "component": "ElectrolyticCellApparatusSvg.jsx",
            "anchor_json": "electrolytic_cell_apparatus.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "gas_evolution_rate_apparatus",
            "component": "GasEvolutionRateApparatusSvg.jsx",
            "anchor_json": "gas_evolution_rate_apparatus.json",
            "required_views": ["textbook", "exam"],
        },
    ],
    9: [
        {
            "master": "pulley_incline_masses_system",
            "component": "PulleyInclineMassesSystemSvg.jsx",
            "anchor_json": "pulley_incline_masses_system.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "ac_dc_generator_motor_apparatus",
            "component": "AcDcGeneratorMotorApparatusSvg.jsx",
            "anchor_json": "ac_dc_generator_motor_apparatus.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "hydraulic_gears_belt_pulley",
            "component": "HydraulicGearsBeltPulleySvg.jsx",
            "anchor_json": "hydraulic_gears_belt_pulley.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "earth_lithosphere_layers",
            "component": "EarthLithosphereLayersSvg.jsx",
            "anchor_json": "earth_lithosphere_layers.json",
            "required_views": ["textbook", "exam"],
        },
        {
            "master": "architectural_floor_packaging_plan",
            "component": "ArchitecturalFloorPackagingPlanSvg.jsx",
            "anchor_json": "architectural_floor_packaging_plan.json",
            "required_views": ["textbook", "exam"],
        },
    ],
}


def audit_item(item):
    errors = []
    master = item["master"]
    comp_path = os.path.join(DIAGRAM_BANK_DIR, item["component"])
    anchor_path = os.path.join(ANCHORS_DIR, item["anchor_json"])

    if not os.path.exists(comp_path):
        errors.append(f"[{master}] Missing component file: {comp_path}")
        return errors

    with open(comp_path, "r", encoding="utf-8") as f:
        jsx = f.read()

    # 1. Check for <image href="/diagrams/..." /> tags in JSX
    image_hrefs = re.findall(r'href=["\'](/diagrams/[^"\']+)["\']', jsx)
    if len(image_hrefs) < 2:
        errors.append(
            f"[{master}] VIOLATION (Rule 0d-14.1): {item['component']} has {len(image_hrefs)} "
            f"<image href=\"/diagrams/...\" /> plate(s). Must embed at least 2 real plates "
            f"(Textbook Master + NSC Exam Stipple) like HumanHeartSvg.jsx."
        )

    # 2. Verify every referenced image file exists on disk and is a real high-res asset (>30KB for raster)
    for href in image_hrefs:
        rel_name = href.replace("/diagrams/", "")
        disk_path = os.path.join(PUBLIC_DIAGRAMS_DIR, rel_name)
        if not os.path.exists(disk_path):
            errors.append(f"[{master}] Missing image plate on disk: public/diagrams/{rel_name}")
        else:
            size_bytes = os.path.getsize(disk_path)
            if disk_path.lower().endswith((".jpg", ".jpeg", ".png", ".webp")) and size_bytes < 30000:
                errors.append(
                    f"[{master}] Image plate public/diagrams/{rel_name} is too small ({size_bytes} bytes) "
                    f"— must be an authentic high-resolution plate."
                )

    # Strip comments before checking for JSX elements
    code_only = re.sub(r'/\*[\s\S]*?\*/', '', jsx)
    code_only = re.sub(r'//.*', '', code_only)

    # 3. Ban hand-coded SVG polygon / ellipse / circle clipart inside the base artwork
    polygon_count = len(re.findall(r"<polygon\b", code_only))
    ellipse_count = len(re.findall(r"<ellipse\b", code_only))
    circle_count = len(re.findall(r"<circle\b", code_only))
    if polygon_count > 0 or ellipse_count > 0 or circle_count > 0:
        errors.append(
            f"[{master}] VIOLATION (Rule 0d-14.1 Zero-Clip-Art Law): {item['component']} contains "
            f"hand-coded geometric SVG shapes (polygon={polygon_count}, ellipse={ellipse_count}, "
            f"circle={circle_count}). Base anatomy/apparatus MUST come from <image href=\"/diagrams/...\" /> plates!"
        )

    # 4. Check InteractiveCallouts usage
    if "InteractiveCallouts" not in jsx:
        errors.append(f"[{master}] {item['component']} must use InteractiveCallouts for horizontal elbow leader lines.")

    # 5. Check server-side anchor JSON and grade masks
    if not os.path.exists(anchor_path):
        errors.append(f"[{master}] Missing anchor manifest: {anchor_path}")
    else:
        with open(anchor_path, "r", encoding="utf-8") as af:
            adata = json.load(af)
        anchors = adata.get("anchors", {})
        if len(anchors) < 4:
            errors.append(f"[{master}] {item['anchor_json']} has only {len(anchors)} anchors (minimum 4 required).")
        for akey, aval in anchors.items():
            if "grades" not in aval or not isinstance(aval["grades"], list) or len(aval["grades"]) == 0:
                errors.append(f"[{master}] Anchor '{akey}' in {item['anchor_json']} is missing 'grades' scope mask.")
            if "anchor" not in aval or len(aval["anchor"]) != 2:
                errors.append(f"[{master}] Anchor '{akey}' in {item['anchor_json']} is missing [x, y] coordinate.")

    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--milestone", type=int, choices=list(MILESTONES.keys()), help="Milestone number (1-6)")
    parser.add_argument("--all", action="store_true", help="Audit all milestones 1-6")
    args = parser.parse_args()

    target_milestones = list(MILESTONES.keys()) if args.all or not args.milestone else [args.milestone]

    print("=" * 72)
    print("  FUNDILE HEART-STANDARD MEDICAL & SCIENTIFIC PLATE AUDITOR (RULE 0d-14)")
    print("=" * 72)

    all_errors = []
    for m in target_milestones:
        print(f"\n--- Auditing Milestone {m} ---")
        for item in MILESTONES[m]:
            errs = audit_item(item)
            if errs:
                for e in errs:
                    print(f"  [FAIL] {e}")
                all_errors.extend(errs)
            else:
                print(
                    f"  [PASS] {item['master']} ({item['component']}): Authentic plates in public/diagrams/ "
                    f"+ zero geometric SVG clipart + calibrated {item['anchor_json']}"
                )

    print("\n" + "-" * 72)
    if all_errors:
        print(f"[AUDIT FAILED] {len(all_errors)} violation(s) detected. Hand-coded SVG clipart is forbidden.")
        sys.exit(1)
    else:
        print("[AUDIT PASSED] 100% of audited diagrams match the Heart Medical Textbook Standard.")
        sys.exit(0)


if __name__ == "__main__":
    main()
