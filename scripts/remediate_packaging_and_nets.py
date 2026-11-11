"""Remediation for packaging_arrangements.py and nets_models_pallets.py (Grade 10)."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "caps-ai-backend", "app", "utils", "mathematical_literacy", "assembly_packaging")

def remediate_packaging_arrangements():
    p = os.path.join(BASE, "packaging_arrangements.py")
    code = open(p, encoding="utf-8").read()

    # 36. asm_pack_single_layer_box_grid_length_width
    old_p36 = '''def _gen_asm_pack_single_layer_box_grid_length_width(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    carton_L = r.choice([40, 45, 50, 60])
    carton_W = r.choice([25, 30, 35, 40])
    box_l = r.choice([6, 8, 10])
    box_w = r.choice([4, 5, 6])

    fit_L = carton_L // box_l
    fit_W = carton_W // box_w
    total_boxes = fit_L * fit_W

    prompt = (
        f"{name} works in a biscuit dispatch warehouse and must pack small rectangular biscuit boxes into "
        f"the base of a large shipping carton (single layer deep).\\n\\n"
        f"Dimensions:\\n"
        f"• Large shipping carton base: Length = {carton_L} cm, Width = {carton_W} cm\\n"
        f"• Small biscuit box base: Length = {box_l} cm, Width = {box_w} cm\\n\\n"
        f"The small boxes are arranged with their lengths parallel to the length of the carton.\\n\\n"
        f"1. How many boxes fit along the length of the carton?\\n"
        f"2. How many boxes fit along the width of the carton?\\n"
        f"3. Calculate the total number of small boxes that can fit in this single layer."
    )'''
    new_p36 = '''def _gen_asm_pack_single_layer_box_grid_length_width(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    carton_L = r.choice([40, 45, 50, 60])
    carton_W = r.choice([25, 30, 35, 40])
    box_l = r.choice([6, 8, 10])
    box_w = r.choice([4, 5, 6])

    fit_L = carton_L // box_l
    fit_W = carton_W // box_w
    total_boxes = fit_L * fit_W

    diag = {
        "kind": "packaging_packing",
        "title": "Carton Base Grid Packaging Layout",
        "carton_l": carton_L,
        "carton_w": carton_W,
        "box_l": box_l,
        "box_w": box_w,
        "boxes_l": fit_L,
        "boxes_w": fit_W,
        "total_boxes": total_boxes,
    }

    prompt = (
        f"{name} works in a biscuit dispatch warehouse and must pack small rectangular biscuit boxes into "
        f"the base of a large shipping carton (single layer deep), as shown in the accompanying layout.\\n\\n"
        f"Dimensions:\\n"
        f"• Large shipping carton base: Length = {carton_L} cm, Width = {carton_W} cm\\n"
        f"• Small biscuit box base: Length = {box_l} cm, Width = {box_w} cm\\n\\n"
        f"The small boxes are arranged with their lengths parallel to the length of the carton.\\n\\n"
        f"1. How many boxes fit along the length of the carton?\\n"
        f"2. How many boxes fit along the width of the carton?\\n"
        f"3. Calculate the total number of small boxes that can fit in this single layer."
    )'''
    code = code.replace(old_p36, new_p36)
    code = code.replace(
        'tier_3_hint=f"{fit_L} × {fit_W} = {total_boxes} boxes.",\n    )',
        'tier_3_hint=f"{fit_L} × {fit_W} = {total_boxes} boxes.",\n        diagram_spec=diag,\n    )'
    )

    # 37. asm_pack_multi_layer_3d_box_stacking
    old_p37 = '''def _gen_asm_pack_multi_layer_3d_box_stacking(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    carton_L = 500  # mm
    carton_W = 300  # mm
    carton_H = 240  # mm

    box_l = 100  # mm
    box_w = 60   # mm
    box_h = 80   # mm

    n_L = carton_L // box_l
    n_W = carton_W // box_w
    n_H = carton_H // box_h
    total_3d = n_L * n_W * n_H

    prompt = (
        f"{name} is packing identical tea boxes into a large rectangular corrugated shipping carton.\\n\\n"
        f"Dimensions of large carton: Length = {carton_L} mm, Width = {carton_W} mm, Height = {carton_H} mm\\n"
        f"Dimensions of tea box: Length = {box_l} mm, Width = {box_w} mm, Height = {box_h} mm\\n\\n"
        f"All tea boxes are packed upright in the same orientation.\\n\\n"
        f"Calculate the maximum number of tea boxes that can be packed into the shipping carton in three dimensions."
    )'''
    new_p37 = '''def _gen_asm_pack_multi_layer_3d_box_stacking(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    carton_L = r.choice([400, 480, 500, 600])
    carton_W = r.choice([280, 300, 320, 360])
    carton_H = r.choice([200, 240, 250, 300])

    box_l = r.choice([80, 100, 120])
    box_w = r.choice([50, 60, 80])
    box_h = r.choice([40, 50, 60, 80])

    n_L = carton_L // box_l
    n_W = carton_W // box_w
    n_H = carton_H // box_h
    total_3d = n_L * n_W * n_H

    diag = {
        "kind": "packaging_cartons",
        "title": "3D Multi-Layer Box Stacking Arrangement",
        "carton_l": carton_L,
        "carton_w": carton_W,
        "carton_h": carton_H,
        "box_l": box_l,
        "box_w": box_w,
        "box_h": box_h,
        "dims": f"{carton_L}×{carton_W}×{carton_H}",
    }

    prompt = (
        f"{name} is packing identical tea boxes into a large rectangular corrugated shipping carton (see accompanying 3D packing diagram).\\n\\n"
        f"Dimensions of large carton: Length = {carton_L} mm, Width = {carton_W} mm, Height = {carton_H} mm\\n"
        f"Dimensions of tea box: Length = {box_l} mm, Width = {box_w} mm, Height = {box_h} mm\\n\\n"
        f"All tea boxes are packed upright in the same orientation.\\n\\n"
        f"Calculate the maximum number of tea boxes that can be packed into the shipping carton in three dimensions."
    )'''
    code = code.replace(old_p37, new_p37)
    code = code.replace(
        'tier_3_hint=f"{n_L} × {n_W} × {n_H} = {total_3d} tea boxes.",\n    )',
        'tier_3_hint=f"{n_L} × {n_W} × {n_H} = {total_3d} tea boxes.",\n        diagram_spec=diag,\n    )'
    )

    # 38. asm_pack_orientation_comparison_lengthwise_vs_widthwise
    old_p38 = '''def _gen_asm_pack_orientation_comparison_lengthwise_vs_widthwise(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    carton_L = 60
    carton_W = 40
    carton_H = 30

    item_l = 15
    item_w = 12
    item_h = 10

    # Orientation A: item_l along carton_L, item_w along carton_W, item_h along carton_H
    a_L = carton_L // item_l  # 60 // 15 = 4
    a_W = carton_W // item_w  # 40 // 12 = 3
    a_H = carton_H // item_h  # 30 // 10 = 3
    total_A = a_L * a_W * a_H # 4 * 3 * 3 = 36

    # Orientation B: item_w along carton_L, item_l along carton_W, item_h along carton_H
    b_L = carton_L // item_w  # 60 // 12 = 5
    b_W = carton_W // item_l  # 40 // 15 = 2
    b_H = carton_H // item_h  # 30 // 10 = 3
    total_B = b_L * b_W * b_H # 5 * 2 * 3 = 30'''
    new_p38 = '''def _gen_asm_pack_orientation_comparison_lengthwise_vs_widthwise(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    carton_L = r.choice([60, 72, 80])
    carton_W = r.choice([40, 48, 50])
    carton_H = r.choice([30, 36, 40])

    item_l = r.choice([15, 16, 20])
    item_w = r.choice([10, 12, 15])
    item_h = r.choice([8, 10, 12])

    a_L = carton_L // item_l
    a_W = carton_W // item_w
    a_H = carton_H // item_h
    total_A = a_L * a_W * a_H

    b_L = carton_L // item_w
    b_W = carton_W // item_l
    b_H = carton_H // item_h
    total_B = b_L * b_W * b_H

    diag = {
        "kind": "packaging_packing",
        "title": "Carton Packing Orientation Comparison",
        "carton_l": carton_L,
        "carton_w": carton_W,
        "box_l": item_l,
        "box_w": item_w,
        "boxes_l": a_L,
        "boxes_w": a_W,
        "total_boxes": total_A,
    }'''
    code = code.replace(old_p38, new_p38)
    code = code.replace(
        'tier_3_hint=f"{ans}",\n    )',
        'tier_3_hint=f"{ans}",\n        diagram_spec=diag,\n    )'
    )

    # 40. asm_pack_area_division_fallacy_explanation
    old_p40 = '''def _gen_asm_pack_area_division_fallacy_explanation(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A learner attempts to calculate how many small square boxes (each 5 cm × 5 cm = 25 cm²) will fit "
        f"into a larger carton base measuring 45 cm long and 16 cm wide (Total Base Area = 720 cm²).\\n\\n"
        f"The learner calculates:\\n"
        f"720 cm² ÷ 25 cm² = 28,8 boxes → rounds down to 28 boxes.\\n\\n"
        f"However, when physically packing the boxes:\\n"
        f"• Length fit = 45 cm ÷ 5 cm = 9 boxes\\n"
        f"• Width fit = 16 cm ÷ 5 cm = 3,2 → 3 boxes\\n"
        f"• Actual total = 9 × 3 = 27 boxes.\\n\\n"
        f"Why did the learner's area division calculation give an incorrect answer of 28 boxes?"
    )'''
    new_p40 = '''def _gen_asm_pack_area_division_fallacy_explanation(r: random.Random) -> Dict[str, Any]:
    diag = {
        "kind": "packaging_packing",
        "title": "Packing: Discrete Grid vs Continuous Area",
        "carton_l": 45,
        "carton_w": 16,
        "box_l": 5,
        "box_w": 5,
        "boxes_l": 9,
        "boxes_w": 3,
        "total_boxes": 27,
    }

    prompt = (
        f"A learner attempts to calculate how many small square boxes (each 5 cm × 5 cm = 25 cm²) will fit "
        f"into a larger carton base measuring 45 cm long and 16 cm wide (see accompanying layout, Total Base Area = 720 cm²).\\n\\n"
        f"The learner calculates:\\n"
        f"720 cm² ÷ 25 cm² = 28,8 boxes → rounds down to 28 boxes.\\n\\n"
        f"However, when physically packing the boxes:\\n"
        f"• Length fit = 45 cm ÷ 5 cm = 9 boxes\\n"
        f"• Width fit = 16 cm ÷ 5 cm = 3,2 → 3 boxes\\n"
        f"• Actual total = 9 × 3 = 27 boxes.\\n\\n"
        f"Why did the learner's area division calculation give an incorrect answer of 28 boxes?"
    )'''
    code = code.replace(old_p40, new_p40)
    code = code.replace(
        'tier_3_hint="Area division ignores rigid boundaries and empty leftover strip spaces.",\n    )',
        'tier_3_hint="Area division ignores rigid boundaries and empty leftover strip spaces.",\n        diagram_spec=diag,\n    )'
    )

    # 41. asm_pack_wasted_volume_void_space_percentage
    old_p41 = '''def _gen_asm_pack_wasted_volume_void_space_percentage(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    carton_L = 40  # cm
    carton_W = 30  # cm
    carton_H = 20  # cm
    carton_vol = carton_L * carton_W * carton_H  # 24 000 cm³

    item_l = 10
    item_w = 10
    item_h = 10
    item_vol = item_l * item_w * item_h  # 1 000 cm³

    # Suppose packed count is 18 (e.g. 4x3x1 or 3x2x3)
    n_packed = (carton_L // item_l) * (carton_W // item_w) * (carton_H // item_h) # 4 * 3 * 2 = 24
    # Let's make an arrangement with non-zero void space
    carton_L = 45
    carton_W = 32
    carton_H = 22
    carton_vol = carton_L * carton_W * carton_H # 31 680 cm³
    fit_L = carton_L // item_l # 4
    fit_W = carton_W // item_w # 3
    fit_H = carton_H // item_h # 2
    n_packed = fit_L * fit_W * fit_H # 24
    used_vol = n_packed * item_vol # 24 000 cm³
    void_vol = carton_vol - used_vol # 7 680 cm³
    void_pct = round((void_vol / carton_vol) * 100, 1)'''
    new_p41 = '''def _gen_asm_pack_wasted_volume_void_space_percentage(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    item_l = r.choice([8, 10, 12])
    item_w = r.choice([8, 10])
    item_h = r.choice([8, 10])
    item_vol = item_l * item_w * item_h

    fit_L = r.choice([3, 4, 5])
    fit_W = r.choice([2, 3, 4])
    fit_H = r.choice([2, 3])
    n_packed = fit_L * fit_W * fit_H

    carton_L = fit_L * item_l + r.choice([3, 5])
    carton_W = fit_W * item_w + r.choice([2, 4])
    carton_H = fit_H * item_h + r.choice([2, 3])
    carton_vol = carton_L * carton_W * carton_H
    used_vol = n_packed * item_vol
    void_vol = carton_vol - used_vol
    void_pct = round((void_vol / carton_vol) * 100, 1)

    diag = {
        "kind": "packaging_cartons",
        "title": "Carton 3D Void Space Layout",
        "carton_l": carton_L,
        "carton_w": carton_W,
        "carton_h": carton_H,
        "box_l": item_l,
        "box_w": item_w,
        "box_h": item_h,
        "dims": f"{carton_L}×{carton_W}×{carton_H}",
    }'''
    code = code.replace(old_p41, new_p41)
    code = code.replace(
        'tier_3_hint=f"Percentage = ({_fmt(void_vol)} ÷ {_fmt(carton_vol)}) × 100 = {_fmt(void_pct)}%.",\n    )',
        'tier_3_hint=f"Percentage = ({_fmt(void_vol)} ÷ {_fmt(carton_vol)}) × 100 = {_fmt(void_pct)}%.",\n        diagram_spec=diag,\n    )'
    )

    with open(p, "w", encoding="utf-8") as f:
        f.write(code)
    print("remediated packaging_arrangements.py")

def remediate_nets_models_pallets():
    p = os.path.join(BASE, "nets_models_pallets.py")
    code = open(p, encoding="utf-8").read()

    # 45. asm_net_rectangular_prism_face_identification
    old_p45 = '''def _gen_asm_net_rectangular_prism_face_identification(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A 2D unfolded cardboard net of a rectangular cereal box consists of 6 rectangular faces labelled A, B, C, D, E, and F, "
        f"along with several perimeter glue tabs.\\n\\n"
        f"In this cross-shaped net layout:\\n"
        f"• Face B is the front panel (20 cm × 30 cm)\\n"
        f"• Face D is the back panel (20 cm × 30 cm)\\n"
        f"• Face A and Face C are the side panels (6 cm × 30 cm)\\n"
        f"• Face E is the top closing flap (20 cm × 6 cm)\\n\\n"
        f"Which face forms the **bottom base** of the cereal box, opposite to the top flap (Face E), and what are its dimensions?"
    )'''
    new_p45 = '''def _gen_asm_net_rectangular_prism_face_identification(r: random.Random) -> Dict[str, Any]:
    diag = {
        "kind": "rectangular_prism_net",
        "title": "2D Net of Rectangular Cereal Box",
        "length": 20,
        "width": 6,
        "height": 30,
    }

    prompt = (
        f"The accompanying diagram illustrates the 2D unfolded net of a rectangular cereal box consisting of 6 rectangular faces labelled A, B, C, D, E, and F, "
        f"along with perimeter glue tabs.\\n\\n"
        f"In this cross-shaped net layout:\\n"
        f"• Face B is the front panel (20 cm × 30 cm)\\n"
        f"• Face D is the back panel (20 cm × 30 cm)\\n"
        f"• Face A and Face C are the side panels (6 cm × 30 cm)\\n"
        f"• Face E is the top closing flap (20 cm × 6 cm)\\n\\n"
        f"Which face forms the **bottom base** of the cereal box, opposite to the top flap (Face E), and what are its dimensions?"
    )'''
    code = code.replace(old_p45, new_p45)
    code = code.replace(
        'tier_3_hint="Face F with dimensions 20 cm × 6 cm forms the bottom base.",\n    )',
        'tier_3_hint="Face F with dimensions 20 cm × 6 cm forms the bottom base.",\n        diagram_spec=diag,\n    )'
    )

    # 46. asm_net_cube_dice_opposite_faces_sum_seven
    old_p46 = '''def _gen_asm_net_cube_dice_opposite_faces_sum_seven(r: random.Random) -> Dict[str, Any]:
    known_face = r.choice([1, 2, 3, 4, 5, 6])
    opposite_face = 7 - known_face

    prompt = (
        f"A learner cuts out a 2D cross-shaped net of a cube from cardboard to make a standard game die.\\n\\n"
        f"On all standard gaming dice, the dots (pips) on any two **opposite faces must add up to exactly 7**.\\n\\n"
        f"If one face of the die is marked with **{known_face}**, what number must be marked on the "
        f"face directly opposite to it when folded into a 3D cube?"
    )'''
    new_p46 = '''def _gen_asm_net_cube_dice_opposite_faces_sum_seven(r: random.Random) -> Dict[str, Any]:
    known_face = r.choice([1, 2, 3, 4, 5, 6])
    opposite_face = 7 - known_face

    diag = {
        "kind": "cube_net",
        "title": "2D Net of Cube Gaming Die",
        "side": 5,
        "faces": ["1", "2", "3", "4", "5", "6"],
    }

    prompt = (
        f"A learner cuts out the accompanying 2D net of a cube from cardboard to make a standard game die.\\n\\n"
        f"On all standard gaming dice, the dots (pips) on any two **opposite faces must add up to exactly 7**.\\n\\n"
        f"If one face of the die is marked with **{known_face}**, what number must be marked on the "
        f"face directly opposite to it when folded into a 3D cube?"
    )'''
    code = code.replace(old_p46, new_p46)
    code = code.replace(
        'tier_3_hint=f"The opposite face is {opposite_face}.",\n    )',
        'tier_3_hint=f"The opposite face is {opposite_face}.",\n        diagram_spec=diag,\n    )'
    )

    # 47. asm_net_cylinder_curved_surface_and_circular_bases
    old_p47 = '''def _gen_asm_net_cylinder_curved_surface_and_circular_bases(r: random.Random) -> Dict[str, Any]:
    diameter_cm = r.choice([6.0, 7.0, 8.0, 10.0])
    height_cm = r.choice([10.0, 11.5, 12.0, 14.0])
    pi_val = 3.142
    circ_cm = round(pi_val * diameter_cm, 2)

    prompt = (
        f"A manufacturer designs the flat 2D printing template (net) for a tin can (closed cylinder).\\n\\n"
        f"Measurements of the tin can:\\n"
        f"• Diameter of base: {_fmt(diameter_cm)} cm\\n"
        f"• Height of can: {_fmt(height_cm)} cm\\n"
        f"• Use the approximation: π = 3,142\\n\\n"
        f"Formula: Circumference = π × diameter\\n\\n"
        f"The net consists of two circular discs and one rectangular label sheet that wraps around the curved side.\\n"
        f"Calculate the length of the rectangular sheet (which equals the circumference of the circle) in cm."
    )'''
    new_p47 = '''def _gen_asm_net_cylinder_curved_surface_and_circular_bases(r: random.Random) -> Dict[str, Any]:
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
        f"A manufacturer designs the flat 2D printing template (net) for a tin can (closed cylinder), shown in the accompanying net diagram.\\n\\n"
        f"Measurements of the tin can:\\n"
        f"• Diameter of base: {_fmt(diameter_cm)} cm\\n"
        f"• Height of can: {_fmt(height_cm)} cm\\n"
        f"• Use the approximation: π = 3,142\\n\\n"
        f"Formula: Circumference = π × diameter\\n\\n"
        f"The net consists of two circular discs and one rectangular label sheet that wraps around the curved side.\\n"
        f"Calculate the length of the rectangular sheet (which equals the circumference of the circle) in cm."
    )'''
    code = code.replace(old_p47, new_p47)
    code = code.replace(
        'tier_3_hint=f"Length = {_fmt(circ_cm)} cm.",\n    )',
        'tier_3_hint=f"Length = {_fmt(circ_cm)} cm.",\n        diagram_spec=diag,\n    )'
    )

    # 48. asm_net_triangular_prism_chocolate_box
    old_p48 = '''def _gen_asm_net_triangular_prism_chocolate_box(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Study the 2D unfolded packaging net of a triangular prism (used for packaging triangular chocolate bars).\\n\\n"
        f"Which 2D geometric shapes make up the complete net of this triangular prism?"
    )'''
    new_p48 = '''def _gen_asm_net_triangular_prism_chocolate_box(r: random.Random) -> Dict[str, Any]:
    diag = {
        "kind": "triangular_prism_net",
        "title": "2D Net of Triangular Prism Packaging",
        "base": 6,
        "height": 18,
    }

    prompt = (
        f"Study the accompanying 2D unfolded packaging net of a triangular prism (used for packaging triangular chocolate bars).\\n\\n"
        f"Which 2D geometric shapes make up the complete net of this triangular prism?"
    )'''
    code = code.replace(old_p48, new_p48)
    code = code.replace(
        'tier_3_hint="3 rectangular faces and 2 triangular end flaps.",\n    )',
        'tier_3_hint="3 rectangular faces and 2 triangular end flaps.",\n        diagram_spec=diag,\n    )'
    )

    # 51. asm_model_architectural_cardboard_scale
    old_p51 = '''def _gen_asm_model_architectural_cardboard_scale(r: random.Random) -> Dict[str, Any]:
    name = r.choice(SA_NAMES)
    scale_factor = 50  # 1:50 scale
    real_length_m = r.choice([6.0, 7.5, 9.0, 10.5, 12.0])
    real_length_cm = real_length_m * 100.0
    model_length_cm = real_length_cm / scale_factor

    prompt = (
        f"{name} is an architecture student building a 3D cardboard presentation model of a modern house.\\n\\n"
        f"Scale & Blueprints:\\n"
        f"• Scale of model: 1 : {scale_factor}\\n"
        f"• Real-life exterior wall length: {_fmt(real_length_m)} m\\n\\n"
        f"Calculate the length (in cm) that {name} must cut from cardboard to represent this exterior wall on the model."
    )'''
    new_p51 = '''def _gen_asm_model_architectural_cardboard_scale(r: random.Random) -> Dict[str, Any]:
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
        f"{name} is an architecture student building a 3D cardboard presentation model of a modern house (refer to the floor plan blueprint).\\n\\n"
        f"Scale & Blueprints:\\n"
        f"• Scale of model: 1 : {scale_factor}\\n"
        f"• Real-life exterior wall length: {_fmt(real_length_m)} m\\n\\n"
        f"Calculate the length (in cm) that {name} must cut from cardboard to represent this exterior wall on the model."
    )'''
    code = code.replace(old_p51, new_p51)
    code = code.replace(
        'tier_3_hint=f"{_fmt(real_length_cm)} ÷ {scale_factor} = {_fmt(model_length_cm)} cm.",\n    )',
        'tier_3_hint=f"{_fmt(real_length_cm)} ÷ {scale_factor} = {_fmt(model_length_cm)} cm.",\n        diagram_spec=diag,\n    )'
    )

    with open(p, "w", encoding="utf-8") as f:
        f.write(code)
    print("remediated nets_models_pallets.py")

remediate_packaging_arrangements()
remediate_nets_models_pallets()
