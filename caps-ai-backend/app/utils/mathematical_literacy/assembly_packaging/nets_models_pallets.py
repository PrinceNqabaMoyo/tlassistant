"""Cluster 6: 2D Nets, Models & Pallet Stacking (Subskills 45 to 52).

Covers:
45. 2D nets of rectangular prisms (matching opposite faces and glue tabs)
46. 2D nets of cubes & standard dice opposite faces rule (sum = 7)
47. Cylinder net decomposition (circular bases + rectangular curved wrapper C = πd)
48. Triangular prism 2D net layout (3 rectangular faces + 2 triangular ends)
49. Standard industrial wooden pallet dimensions & interlocking column stability (1 200 × 1 000 mm)
50. Maximum pallet vertical stacking layers constrained by truck container clearance
51. 3D architectural cardboard model scale dimensions from building plans
52. Geometric packing efficiency comparison: flat tessellating prisms vs cylindrical voids
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List

from .common import (
    SA_NAMES,
    _fmt,
    _build_question_payload,
)


def _gen_asm_net_rectangular_prism_face_identification(r: random.Random) -> Dict[str, Any]:
    b_len = r.choice([18, 20, 22, 24])
    b_wid = r.choice([5, 6, 7])
    b_hgt = r.choice([26, 28, 30])
    diag = {
        "kind": "rectangular_prism_net",
        "title": f"2D Net of Rectangular Box ({b_len}×{b_wid}×{b_hgt})",
        "length": b_len,
        "width": b_wid,
        "height": b_hgt,
    }

    prompt = (
        f"Inspect the accompanying 2D unfolded net of a rectangular cereal box with faces A through F.\n\n"
        f"Net specifications:\n"
        f"• Front panel B: {b_len} cm by {b_hgt} cm\n"
        f"• Back panel D: {b_len} cm by {b_hgt} cm\n"
        f"• Side panels A and C: {b_wid} cm by {b_hgt} cm\n"
        f"• Top closing flap E: {b_len} cm by {b_wid} cm\n\n"
        f"Which face forms the bottom base (matching flap E), and what are its dimensions?"
    )
    ans = f"Face F — dimensions: {b_len} cm × {b_wid} cm"
    opts = [
        f"Face F — dimensions: {b_len} cm × {b_wid} cm",
        f"Face A — dimensions: {b_wid} cm × {b_hgt} cm",
        f"Face D — dimensions: {b_len} cm × {b_hgt} cm",
        f"Face B — dimensions: {b_len} cm × {b_hgt} cm",
    ]

    s1 = f"Identify pairs of identical opposite faces in a rectangular prism net: Front opposes Back, Left opposes Right, Top opposes Bottom."
    s2 = f"✓ [1 Mark: Method – Identifying mating opposite face and congruent dimensions]\nThe bottom face must be congruent to the top flap (Face E) with dimensions 20 cm × 6 cm."
    s3 = f"✓ [1 Mark: Accuracy – Correct face label and dimensions]\nOpposite face: Face F (20 cm × 6 cm)."

    return _build_question_payload(
        "asm_net_rectangular_prism_face_identification",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="In a rectangular box, the top and bottom faces must have identical dimensions.",
        tier_2_hint="Face E has dimensions 20 cm × 6 cm. Find the matching remaining face.",
        tier_3_hint="Face F with dimensions 20 cm × 6 cm forms the bottom base.",
        diagram_spec=diag,
    )


def _gen_asm_net_cube_dice_opposite_faces_sum_seven(r: random.Random) -> Dict[str, Any]:
    known_face = r.choice([1, 2, 3, 4, 5, 6])
    opposite_face = 7 - known_face

    c_side = r.choice([4, 5, 6])
    diag = {
        "kind": "cube_net",
        "title": f"2D Net of Gaming Die ({c_side}cm, face {known_face})",
        "side": c_side,
        "faces": ["1", "2", "3", "4", "5", "6"],
    }

    prompt = (
        f"A learner cuts out the accompanying 2D net of a cube from cardboard to make a standard game die.\n\n"
        f"On all standard gaming dice, the dots (pips) on any two **opposite faces must add up to exactly 7**.\n\n"
        f"If one face of the die is marked with **{known_face}**, what number must be marked on the "
        f"face directly opposite to it when folded into a 3D cube?"
    )
    ans = str(opposite_face)

    s1 = f"Apply the standard dice configuration rule: Opposite Face = 7 − Known Face (7 − {known_face})."
    s2 = f"✓ [1 Mark: Method – Standard opposite dice face sum rule setup]\nSum of opposite faces = 7.\nOpposite = 7 − {known_face}."
    s3 = f"✓ [1 Mark: Accuracy – Value of opposite face]\nOpposite number = {opposite_face}."

    return _build_question_payload(
        "asm_net_cube_dice_opposite_faces_sum_seven",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Subtract {known_face} from 7.",
        tier_2_hint=f"7 − {known_face} = {opposite_face}.",
        tier_3_hint=f"The opposite face is {opposite_face}.",
        diagram_spec=diag,
    )


def _gen_asm_net_cylinder_curved_surface_and_circular_bases(r: random.Random) -> Dict[str, Any]:
    diameter_cm = r.choice([6.0, 7.0, 8.0, 10.0])
    height_cm = r.choice([10.0, 11.5, 12.0, 14.0])
    pi_val = 3.142
    circ_cm = round(pi_val * diameter_cm, 2)

    diag = {
        "kind": "cylinder_net",
        "title": "2D Net of Cylindrical Tin Can",
        "radius": round(diameter_cm / 2, 1),
        "height": height_cm,
    }

    prompt = (
        f"A manufacturer designs the flat 2D printing template (net) for a tin can (closed cylinder), shown in the accompanying net diagram.\n\n"
        f"Measurements of the tin can:\n"
        f"• Diameter of base: {_fmt(diameter_cm)} cm\n"
        f"• Height of can: {_fmt(height_cm)} cm\n"
        f"• Use the approximation: π = 3,142\n\n"
        f"Formula: Circumference = π × diameter\n\n"
        f"The net consists of two circular discs and one rectangular label sheet that wraps around the curved side.\n"
        f"Calculate the length of the rectangular sheet (which equals the circumference of the circle) in cm."
    )
    ans = f"{_fmt(circ_cm)} cm"

    s1 = f"The length of the unrolled rectangular curved surface of a cylinder equals the circular perimeter (circumference = π × d = 3,142 × {_fmt(diameter_cm)} cm)."
    s2 = f"✓ [1 Mark: Method – Circumference formula setup]\nCircumference = 3,142 × {_fmt(diameter_cm)} cm."
    s3 = f"✓ [1 Mark: Accuracy – Length of unrolled rectangle]\nLength = {_fmt(circ_cm)} cm."

    return _build_question_payload(
        "asm_net_cylinder_curved_surface_and_circular_bases",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Multiply π (3,142) by diameter ({_fmt(diameter_cm)} cm).",
        tier_2_hint=f"Circumference = 3,142 × {_fmt(diameter_cm)}.",
        tier_3_hint=f"Length = {_fmt(circ_cm)} cm.",
        diagram_spec=diag,
    )


def _gen_asm_net_triangular_prism_chocolate_box(r: random.Random) -> Dict[str, Any]:
    t_base = r.choice([5, 6, 7])
    t_hgt = r.choice([16, 18, 20])
    diag = {
        "kind": "triangular_prism_net",
        "title": f"2D Net of Triangular Prism ({t_base}×{t_hgt}cm)",
        "base": t_base,
        "height": t_hgt,
    }

    prompt = (
        f"Study the accompanying 2D unfolded packaging net of a triangular prism (used for packaging triangular chocolate bars).\n\n"
        f"Which 2D geometric shapes make up the complete net of this triangular prism?"
    )
    ans = "3 rectangular faces and 2 identical equilateral/isosceles triangular end flaps"
    opts = [
        "3 rectangular faces and 2 identical equilateral/isosceles triangular end flaps",
        "4 triangular faces and 1 square base",
        "2 rectangular faces and 4 circular end discs",
        "6 congruent square faces",
    ]

    s1 = f"Decompose 3D triangular prism into its constituent 2D boundary polygons: 3 lateral rectangular sides connecting 2 congruent parallel triangular bases."
    s2 = f"✓ [1 Mark: Method – Polyhedral face decomposition of a triangular prism]\nA triangular prism has 5 faces: 3 rectangular sides + 2 triangular bases."
    s3 = f"✓ [1 Mark: Accuracy – Exact polygon composition]\nComposition: 3 rectangular faces and 2 identical equilateral/isosceles triangular end flaps."

    return _build_question_payload(
        "asm_net_triangular_prism_chocolate_box",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="How many sides does a triangle have? 3 sides, each connected to a rectangular face.",
        tier_2_hint="The two ends are triangles; the three long sides are rectangles.",
        tier_3_hint="3 rectangular faces and 2 triangular end flaps.",
        diagram_spec=diag,
    )


def _gen_asm_pack_pallet_layer_interlocking_pattern(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"In logistics and warehousing, standard South African industrial wooden pallets measure "
        f"1 200 mm × 1 000 mm.\n\n"
        f"When warehouse forklift operators stack boxes onto a pallet across multiple tiers, they arrange "
        f"each alternating layer in an interlocking (pinwheel/brick) pattern rather than stacking boxes in "
        f"identical vertical columns.\n\n"
        f"What is the crucial mechanical stability advantage of stacking pallet boxes in an interlocking pattern?"
    )
    ans = "It binds the boxes together, preventing individual columns from shifting or toppling over during transit on rough roads or during forklift movement."
    opts = [
        "It binds the boxes together, preventing individual columns from shifting or toppling over during transit on rough roads or during forklift movement.",
        "It reduces the total mass of the goods by 15%.",
        "It prevents rain from falling onto the cardboard boxes.",
        "It makes the cardboard boxes fire-resistant.",
    ]

    s1 = f"Understand industrial cargo unitization, tensile cross-bonding, and load stability during logistics transit."
    s2 = f"✓ [1 Mark: Method – Mechanical stability rationale for interlocking pallet stacking]\nColumn stacking creates separate unbonded vertical pillars prone to tipping under horizontal inertial acceleration. Interlocking layers distribute shear forces across the stack."
    s3 = f"✓ [1 Mark: Accuracy – Correct logistics stability rationale]\nAdvantage: It binds the boxes together, preventing individual columns from shifting or toppling over during transit on rough roads or during forklift movement."

    return _build_question_payload(
        "asm_pack_pallet_layer_interlocking_pattern",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="Think about what happens to tall vertical columns of bricks if they are not overlapping.",
        tier_2_hint="Interlocking patterns tie adjacent boxes together to stop them toppling over.",
        tier_3_hint="It binds the boxes together to prevent columns tipping over during transit.",
    )


def _gen_asm_pack_pallet_maximum_height_stack_limit(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    truck_height_mm = 2400  # 2,4 m truck cargo door opening
    pallet_base_mm = 150   # 15 cm wooden pallet base height
    overhead_clearance_mm = 100 # 10 cm required safety clearance
    available_cargo_height = truck_height_mm - pallet_base_mm - overhead_clearance_mm # 2 150 mm
    box_height_mm = r.choice([250, 300, 350])
    max_layers = available_cargo_height // box_height_mm

    prompt = (
        f"{name} is loading stacked pallets of canned goods into a refrigerated delivery truck.\n\n"
        f"Logistics Constraints:\n"
        f"• Truck cargo door opening interior height: {truck_height_mm} mm\n"
        f"• Wooden pallet base height: {pallet_base_mm} mm\n"
        f"• Minimum overhead safety clearance required: {overhead_clearance_mm} mm\n"
        f"• Height of each layer of cartons: {box_height_mm} mm\n\n"
        f"Calculate the maximum number of carton layers that can be stacked on one pallet so the loaded "
        f"pallet fits safely through the truck cargo opening."
    )
    ans = f"{max_layers} layers"

    s1 = f"Deduct wooden pallet height ({pallet_base_mm} mm) and overhead clearance ({overhead_clearance_mm} mm) from truck height ({truck_height_mm} mm), then integer divide by box height ({box_height_mm} mm)."
    s2 = f"✓ [1 Mark: Method – Available vertical stacking calculation and integer division]\nAvailable height = {truck_height_mm} mm − {pallet_base_mm} mm − {overhead_clearance_mm} mm = {available_cargo_height} mm.\nLayers = {available_cargo_height} mm ÷ {box_height_mm} mm = {_fmt(round(available_cargo_height / box_height_mm, 2))} → {max_layers} layers."
    s3 = f"✓ [1 Mark: Accuracy – Maximum permitted stacking layers]\nMax layers = {max_layers} layers."

    return _build_question_payload(
        "asm_pack_pallet_maximum_height_stack_limit",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Subtract pallet ({pallet_base_mm} mm) and clearance ({overhead_clearance_mm} mm) from {truck_height_mm} mm.",
        tier_2_hint=f"Available height = {available_cargo_height} mm. Divide by box height of {box_height_mm} mm.",
        tier_3_hint=f"{available_cargo_height} ÷ {box_height_mm} = {max_layers} layers.",
    )


def _gen_asm_model_architectural_cardboard_scale(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    scale_factor = 50  # 1:50 scale
    real_length_m = r.choice([6.0, 7.5, 9.0, 10.5, 12.0])
    real_length_cm = real_length_m * 100.0
    model_length_cm = real_length_cm / scale_factor

    diag = {
        "kind": "floor_plan",
        "title": "Architectural Model Blueprint",
        "scale": f"1 : {scale_factor}",
        "rooms": [
            {"name": "Model Exterior Wall", "dims": f"Real: {_fmt(real_length_m)} m", "length_m": real_length_m, "width_m": 4.0},
        ],
        "length_m": real_length_m,
        "width_m": 4.0,
    }

    prompt = (
        f"{name} is an architecture student building a 3D cardboard presentation model of a modern house (refer to the floor plan blueprint).\n\n"
        f"Scale & Blueprints:\n"
        f"• Scale of model: 1 : {scale_factor}\n"
        f"• Real-life exterior wall length: {_fmt(real_length_m)} m\n\n"
        f"Calculate the length (in cm) that {name} must cut from cardboard to represent this exterior wall on the model."
    )
    ans = f"{_fmt(model_length_cm)} cm"

    s1 = f"Convert real-life dimension to centimetres ({_fmt(real_length_m)} m × 100 = {_fmt(real_length_cm)} cm), then divide by scale factor ({scale_factor})."
    s2 = f"✓ [1 Mark: Method – Unit conversion to cm and division by scale ratio]\nReal length (cm) = {_fmt(real_length_m)} × 100 = {_fmt(real_length_cm)} cm.\nModel length = {_fmt(real_length_cm)} cm ÷ {scale_factor}."
    s3 = f"✓ [1 Mark: Accuracy – Model dimension in cm]\nCardboard cut length = {_fmt(model_length_cm)} cm."

    return _build_question_payload(
        "asm_model_architectural_cardboard_scale",
        prompt,
        ans,
        s1, s2, s3, r,
        tier_1_hint=f"Convert {_fmt(real_length_m)} m to cm: {_fmt(real_length_m)} × 100 = {_fmt(real_length_cm)} cm.",
        tier_2_hint=f"Divide {_fmt(real_length_cm)} cm by scale factor {scale_factor}.",
        tier_3_hint=f"{_fmt(real_length_cm)} ÷ {scale_factor} = {_fmt(model_length_cm)} cm.",
        diagram_spec=diag,
    )


def _gen_asm_pack_triangular_prism_tessellation_vs_cylinder(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A confectionery exporter is choosing packaging for shipping candies overseas in master cartons.\n"
        f"They compare two item designs: cylindrical tins vs triangular prism boxes.\n\n"
        f"Why do triangular prism boxes achieve higher volumetric packing efficiency than round cylindrical tins?"
    )
    ans = "Triangular prisms have flat planar faces that can tessellate and fit flush against each other with zero gaps, whereas tangent circular cylinders always leave empty interstitial voids between them."
    opts = [
        "Triangular prisms have flat planar faces that can tessellate and fit flush against each other with zero gaps, whereas tangent circular cylinders always leave empty interstitial voids between them.",
        "Triangular prisms weigh half as much as cylinders of the same volume.",
        "Cardboard made into triangles does not absorb moisture from humid air.",
        "Round cylinders can only be transported by boat, not by air.",
    ]

    s1 = f"Understand 2D/3D tessellation and packing density comparison between polyhedra with planar faces vs curved circular cross-sections."
    s2 = f"✓ [1 Mark: Method – Geometric packing density and void space comparison]\nPlanar triangles tile the 2D plane with 100% surface filling (tessellation), eliminating empty interstitial voids inherent in circle packing."
    s3 = f"✓ [1 Mark: Accuracy – Correct geometric packing rationale]\nReason: Triangular prisms have flat planar faces that can tessellate and fit flush against each other with zero gaps, whereas tangent circular cylinders always leave empty interstitial voids between them."

    return _build_question_payload(
        "asm_pack_triangular_prism_tessellation_vs_cylinder",
        prompt,
        ans,
        s1, s2, s3, r,
        custom_options=opts,
        tier_1_hint="What happens when round cans are placed next to each other? They leave empty triangular gaps.",
        tier_2_hint="Triangular prisms can alternate points up and points down to fit perfectly together with zero gaps.",
        tier_3_hint="Flat planar faces tessellate with zero empty gaps, unlike round cylinders.",
    )

DEFAULT_DIAGRAM_ROLE = 'context'
# All diagrams emitted by this generator specify diagram_role: "context" | "identify"
