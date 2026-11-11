"""Remediate all 21 missing subskills in gr12_maps_and_plans_models.
"""
from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# 1. scale_selection_page_fit.py (01, 02, 03, 05, 06)
# ---------------------------------------------------------------------------
p_ssf = "caps-ai-backend/app/utils/mathematical_literacy/gr12_maps_and_plans_models/scale_selection_page_fit.py"
c_ssf = open(p_ssf, "r", encoding="utf-8").read()

# 01
old_01 = '''    prompt = (
        f"A learner is deciding on an architectural scale to build a physical 3D model of a house.\\n"
        f"Three candidate scales are considered: {scale_choices[0]}, {scale_choices[1]}, and {scale_choices[2]}.\\n\\n"
        f"Which of these scales will produce the LARGEST physical model, and what is the mathematical reason?"
    )'''
new_01 = '''    prompt = (
        f"Refer to the model scale comparison shown in the diagram. "
        f"A learner is deciding on an architectural scale to build a physical 3D model of a house, "
        f"considering three candidate scales: {scale_choices[0]}, {scale_choices[1]}, and {scale_choices[2]}.\\n\\n"
        f"Which of these scales will produce the LARGEST physical model, and what is the mathematical reason?"
    )
    d_spec_01 = {
        "kind": "bar_scale",
        "title": f"Model Scale Comparison (Candidate Scales: {scale_choices[0]}, {scale_choices[1]}, {scale_choices[2]})",
        "ratio_str": largest_scale_str,
        "segments": [{"length_cm": 2.0, "real_val": smallest_denom * 2 / 100, "unit": "m"}],
    }'''
c_ssf = c_ssf.replace(old_01, new_01)
idx_01 = c_ssf.find('gr12_models_subskill_01')
idx_diff_01 = c_ssf.find('difficulty="easy",\n    )', idx_01)
c_ssf = c_ssf[:idx_diff_01] + 'difficulty="easy",\n        diagram_spec=d_spec_01,\n    )' + c_ssf[idx_diff_01 + len('difficulty="easy",\n    )'):]

# 02
old_02 = '''    prompt = (
        f"{name} needs to draw a scale floor plan of a {project['type']} to fit onto a standard A4 sheet of paper.\\n"
        f"The actual building measures {_fmt(real_l_m, 1)} m long by {_fmt(real_w_m, 1)} m wide.\\n"
        f"Usable drawing dimensions on an A4 page (leaving margins) are 27,0 cm × 18,0 cm.\\n\\n"
        f"Evaluate scales 1 : 20, 1 : 50, and 1 : 100. Which is the LARGEST standard architectural scale that fits on the page?"
    )'''
new_02 = '''    prompt = (
        f"Refer to the A4 page layout shown in the diagram. "
        f"{name} needs to draw a scale floor plan of a {project['type']} to fit onto a standard A4 sheet of paper. "
        f"The building measures {_fmt(real_l_m, 1)} m long by {_fmt(real_w_m, 1)} m wide, "
        f"and usable drawing dimensions on an A4 page are 27,0 cm × 18,0 cm.\\n\\n"
        f"Evaluate scales 1 : 20, 1 : 50, and 1 : 100. Which is the LARGEST standard architectural scale that fits on the page?"
    )
    d_spec_02 = {
        "kind": "floor_plan",
        "title": f"A4 Page Fit ({project['type']}: {_fmt(real_l_m, 1)} m × {_fmt(real_w_m, 1)} m)",
        "rooms": [{"name": project["type"], "length": real_l_m, "width": real_w_m}],
    }'''
c_ssf = c_ssf.replace(old_02, new_02)
idx_02 = c_ssf.find('gr12_models_subskill_02')
idx_diff_02 = c_ssf.find('difficulty="medium",\n    )', idx_02)
c_ssf = c_ssf[:idx_diff_02] + 'difficulty="medium",\n        diagram_spec=d_spec_02,\n    )' + c_ssf[idx_diff_02 + len('difficulty="medium",\n    )'):]

# 03
old_03 = '''    prompt = (
        f"{name} is creating an architectural display model of a community center measuring "
        f"{_fmt(length_m, 1)} m long by {_fmt(width_m, 1)} m wide.\\n"
        f"The model baseboard is an A3 wooden poster board (dimensions: 42,0 cm × 29,7 cm).\\n\\n"
        f"Which standard scale (1 : 20, 1 : 50, or 1 : 100) is the BEST choice to maximize model size while fitting comfortably on the board?"
    )'''
new_03 = '''    prompt = (
        f"Refer to the A3 display board layout shown in the diagram. "
        f"{name} is creating an architectural display model of a community center measuring "
        f"{_fmt(length_m, 1)} m long by {_fmt(width_m, 1)} m wide on an A3 board (42,0 cm × 29,7 cm).\\n\\n"
        f"Which standard scale (1 : 20, 1 : 50, or 1 : 100) is the BEST choice to maximize model size while fitting comfortably on the board?"
    )
    d_spec_03 = {
        "kind": "floor_plan",
        "title": f"A3 Display Board Fit ({_fmt(length_m, 1)} m × {_fmt(width_m, 1)} m)",
        "rooms": [{"name": "Community Center", "length": length_m, "width": width_m}],
    }'''
c_ssf = c_ssf.replace(old_03, new_03)
idx_03 = c_ssf.find('gr12_models_subskill_03')
idx_diff_03 = c_ssf.find('difficulty="medium",\n    )', idx_03)
c_ssf = c_ssf[:idx_diff_03] + 'difficulty="medium",\n        diagram_spec=d_spec_03,\n    )' + c_ssf[idx_diff_03 + len('difficulty="medium",\n    )'):]

# 05
old_05 = '''    prompt = (
        f"An elevation drawing shows a cottage with vertical wall height of {_fmt(wall_h_m, 1)} m "
        f"and a pitched roof apex rising an additional {_fmt(roof_h_m, 1)} m above the walls (total height: {_fmt(total_real_h_m, 1)} m).\\n"
        f"A learner constructs a 3D architectural model at a scale of 1 : {scale}.\\n\\n"
        f"Calculate the total vertical height of the finished physical model from ground to roof apex in centimetres (cm)."
    )'''
new_05 = '''    prompt = (
        f"Refer to the cottage elevation drawing shown in the diagram (scale ratio 1 : {scale}). "
        f"The vertical wall height is {_fmt(wall_h_m, 1)} m and the pitched roof apex rises an additional {_fmt(roof_h_m, 1)} m (total height {_fmt(total_real_h_m, 1)} m).\\n\\n"
        f"Calculate the total vertical height of the finished physical model from ground to roof apex in centimetres (cm)."
    )
    d_spec_05 = {
        "kind": "elevation_view",
        "title": f"Cottage Model Height ({_fmt(total_real_h_m, 1)} m at Scale 1 : {scale})",
        "wall_height_m": wall_h_m,
        "roof_height_m": roof_h_m,
        "total_height_m": total_real_h_m,
    }'''
c_ssf = c_ssf.replace(old_05, new_05)
idx_05 = c_ssf.find('gr12_models_subskill_05')
idx_diff_05 = c_ssf.find('difficulty="easy",\n    )', idx_05)
c_ssf = c_ssf[:idx_diff_05] + 'difficulty="easy",\n        diagram_spec=d_spec_05,\n    )' + c_ssf[idx_diff_05 + len('difficulty="easy",\n    )'):]

# 06
old_06 = '''    prompt = (
        f"When choosing a scale for a physical display model, a student proposes using a scale of {item['scale']}.\\n"
        f"Why is {item['scale']} an unfeasible architectural model scale for a classroom presentation?"
    )'''
new_06 = '''    prompt = (
        f"Refer to the model scale feasibility diagram shown. "
        f"When choosing a scale for a physical display model, a student proposes using a scale of {item['scale']}.\\n"
        f"Why is {item['scale']} an unfeasible architectural model scale for a classroom presentation?"
    )
    v_denom = int(item["scale"].split(":")[-1].strip())
    d_spec_06 = {
        "kind": "bar_scale",
        "title": f"Scale Detail vs Feasibility ({item['scale']})",
        "ratio_str": item["scale"],
        "segments": [{"length_cm": 2.0, "real_val": v_denom * 2 / 100, "unit": "m"}],
    }'''
c_ssf = c_ssf.replace(old_06, new_06)
idx_06 = c_ssf.find('gr12_models_subskill_06')
idx_diff_06 = c_ssf.find('difficulty="easy",\n    )', idx_06)
c_ssf = c_ssf[:idx_diff_06] + 'difficulty="easy",\n        diagram_spec=d_spec_06,\n    )' + c_ssf[idx_diff_06 + len('difficulty="easy",\n    )'):]

open(p_ssf, "w", encoding="utf-8").write(c_ssf)
print("Updated scale_selection_page_fit.py (5 subskills)")


# ---------------------------------------------------------------------------
# 2. architectural_models_rdp_house.py (09, 11, 13)
# ---------------------------------------------------------------------------
p_rdp = "caps-ai-backend/app/utils/mathematical_literacy/gr12_maps_and_plans_models/architectural_models_rdp_house.py"
c_rdp = open(p_rdp, "r", encoding="utf-8").read()

# 09
old_09 = '''    prompt = (
        f"A community contractor is presenting a 1 : {scale} display model of a government-subsidized RDP house.\\n"
        f"The actual exterior dimensions of the house are {_fmt(real_l_m, 1)} m long by {_fmt(real_w_m, 1)} m wide.\\n\\n"
        f"Calculate the dimensions (length and width in centimetres) that the contractor should cut out for the model cardboard base."
    )'''
new_09 = '''    prompt = (
        f"Refer to the RDP house plan shown in the diagram (scale ratio 1 : {scale}). "
        f"The exterior dimensions of the house are {_fmt(real_l_m, 1)} m long by {_fmt(real_w_m, 1)} m wide.\\n\\n"
        f"Calculate the dimensions (length and width in centimetres) that the contractor should cut out for the model cardboard base."
    )
    d_spec_09 = {
        "kind": "floor_plan",
        "title": f"RDP House Model Base (Scale 1 : {scale})",
        "rooms": [{"name": "RDP House", "length": real_l_m, "width": real_w_m}],
    }'''
c_rdp = c_rdp.replace(old_09, new_09)
idx_09 = c_rdp.find('gr12_models_subskill_09')
idx_diff_09 = c_rdp.find('difficulty="easy",\n    )', idx_09)
c_rdp = c_rdp[:idx_diff_09] + 'difficulty="easy",\n        diagram_spec=d_spec_09,\n    )' + c_rdp[idx_diff_09 + len('difficulty="easy",\n    )'):]

# 11
old_11 = '''    prompt = (
        f"According to South African architectural standards, a standard external front entrance door measures "
        f"{_fmt(door_w_mm, 0)} mm wide by {_fmt(door_h_mm, 0)} mm high.\\n"
        f"In a 1 : {scale} scale model of an RDP house, what should be the width and height of the doorway opening cutout, in millimetres?"
    )'''
new_11 = '''    prompt = (
        f"Refer to the entrance door cutout specification shown in the diagram (scale ratio 1 : {scale}). "
        f"A standard external entrance door measures {_fmt(door_w_mm, 0)} mm wide by {_fmt(door_h_mm, 0)} mm high.\\n\\n"
        f"In a 1 : {scale} scale model of an RDP house, what should be the width and height of the doorway opening cutout, in millimetres?"
    )
    d_spec_11 = {
        "kind": "elevation_view",
        "title": f"Doorway Opening Cutout (Scale 1 : {scale})",
        "door_w_mm": door_w_mm,
        "door_h_mm": door_h_mm,
        "model_w_mm": model_w_mm,
        "model_h_mm": model_h_mm,
    }'''
c_rdp = c_rdp.replace(old_11, new_11)
idx_11 = c_rdp.find('gr12_models_subskill_11')
idx_diff_11 = c_rdp.find('difficulty="easy",\n    )', idx_11)
c_rdp = c_rdp[:idx_diff_11] + 'difficulty="easy",\n        diagram_spec=d_spec_11,\n    )' + c_rdp[idx_diff_11 + len('difficulty="easy",\n    )'):]

# 13
old_13 = '''    prompt = (
        f"{name} is building a 1 : {scale} model of a cottage on a completely flat, horizontal baseboard.\\n"
        f"The actual building has uniform vertical walls of {_fmt(wall_height_m, 1)} m on both the North and South sides.\\n\\n"
        f"What should be the vertical height of both the North and South cardboard wall panels on the model, in centimetres?"
    )'''
new_13 = '''    prompt = (
        f"Refer to the cottage elevation model shown in the diagram (scale ratio 1 : {scale}). "
        f"{name} is building a model of a cottage with uniform vertical walls of {_fmt(wall_height_m, 1)} m on both sides.\\n\\n"
        f"What should be the vertical height of both the North and South cardboard wall panels on the model, in centimetres?"
    )
    d_spec_13 = {
        "kind": "elevation_view",
        "title": f"Cottage Elevation Model (Scale 1 : {scale})",
        "wall_height_m": wall_height_m,
        "scaled_height_cm": scaled_h_cm,
    }'''
c_rdp = c_rdp.replace(old_13, new_13)
idx_13 = c_rdp.find('gr12_models_subskill_13')
idx_diff_13 = c_rdp.find('difficulty="easy",\n    )', idx_13)
c_rdp = c_rdp[:idx_diff_13] + 'difficulty="easy",\n        diagram_spec=d_spec_13,\n    )' + c_rdp[idx_diff_13 + len('difficulty="easy",\n    )'):]

open(p_rdp, "w", encoding="utf-8").write(c_rdp)
print("Updated architectural_models_rdp_house.py (3 subskills)")


# ---------------------------------------------------------------------------
# 3. nets_materials_costing.py (17, 23)
# ---------------------------------------------------------------------------
p_nm = "caps-ai-backend/app/utils/mathematical_literacy/gr12_maps_and_plans_models/nets_materials_costing.py"
c_nm = open(p_nm, "r", encoding="utf-8").read()

# 17
old_17 = '''    prompt = (
        f"A student is constructing an open-topped cardboard model of an RDP house main living block.\\n"
        f"The model rectangular prism measures {_fmt(model_l_cm, 1)} cm long, {_fmt(model_w_cm, 1)} cm wide, and {_fmt(model_h_cm, 1)} cm high.\\n"
        f"The net consists of the bottom base panel plus four vertical wall panels.\\n\\n"
        f"Calculate the TOTAL surface area of cardboard required for the net, in square centimetres (cm²)."
    )'''
new_17 = '''    prompt = (
        f"Refer to the cardboard net layout shown in the diagram. "
        f"A student is constructing an open-topped cardboard model of an RDP house living block measuring "
        f"{_fmt(model_l_cm, 1)} cm long, {_fmt(model_w_cm, 1)} cm wide, and {_fmt(model_h_cm, 1)} cm high.\\n\\n"
        f"Calculate the TOTAL surface area of cardboard required for the net, in square centimetres (cm²)."
    )
    d_spec_17 = {
        "kind": "mensuration_2d",
        "title": f"Prism Net Cardboard Layout ({_fmt(model_l_cm, 1)} cm × {_fmt(model_w_cm, 1)} cm)",
        "shape": "rectangle",
        "width": model_l_cm,
        "height": model_w_cm,
        "labels": {"length": f"{_fmt(model_l_cm, 1)} cm", "width": f"{_fmt(model_w_cm, 1)} cm"},
    }'''
c_nm = c_nm.replace(old_17, new_17)
idx_17 = c_nm.find('gr12_models_subskill_17')
idx_diff_17 = c_nm.find('difficulty="easy",\n    )', idx_17)
c_nm = c_nm[:idx_diff_17] + 'difficulty="easy",\n        diagram_spec=d_spec_17,\n    )' + c_nm[idx_diff_17 + len('difficulty="easy",\n    )'):]

# 23
old_23 = '''    prompt = (
        f"A student 3D-prints a scaled plastic model of an architectural pavilion.\\n"
        f"The 3D slicing software calculates that the solid plastic volume of the model is {_fmt(model_vol_cm3, 1)} cm³.\\n"
        f"The density of the PLA plastic filament is {_fmt(pla_density, 2)} g/cm³.\\n\\n"
        f"Calculate the total mass of plastic filament used to print the model, in grams (g)."
    )'''
new_23 = '''    prompt = (
        f"Refer to the 3D-printed model specification shown in the diagram. "
        f"The slicing software calculates that the solid plastic volume of the model is {_fmt(model_vol_cm3, 1)} cm³, "
        f"and the density of the PLA filament is {_fmt(pla_density, 2)} g/cm³.\\n\\n"
        f"Calculate the total mass of plastic filament used to print the model, in grams (g)."
    )
    d_spec_23 = {
        "kind": "mensuration_2d",
        "title": f"3D Printed Model Mass ({_fmt(model_vol_cm3, 1)} cm³ Volume)",
        "shape": "cube",
        "width": 30,
        "height": 30,
        "labels": {"vol": f"{_fmt(model_vol_cm3, 1)} cm³", "density": f"{_fmt(pla_density, 2)} g/cm³"},
    }'''
c_nm = c_nm.replace(old_23, new_23)
idx_23 = c_nm.find('gr12_models_subskill_23')
idx_diff_23 = c_nm.find('difficulty="easy",\n    )', idx_23)
c_nm = c_nm[:idx_diff_23] + 'difficulty="easy",\n        diagram_spec=d_spec_23,\n    )' + c_nm[idx_diff_23 + len('difficulty="easy",\n    )'):]

open(p_nm, "w", encoding="utf-8").write(c_nm)
print("Updated nets_materials_costing.py (2 subskills)")


# ---------------------------------------------------------------------------
# 4. area_volume_scaling_factors.py (25, 26, 27, 28, 30, 31)
# ---------------------------------------------------------------------------
p_av = "caps-ai-backend/app/utils/mathematical_literacy/gr12_maps_and_plans_models/area_volume_scaling_factors.py"
c_av = open(p_av, "r", encoding="utf-8").read()

# 25
old_25 = '''    prompt = (
        f"An architectural model of an exhibition pavilion is built to a scale of 1 : {scale}.\\n"
        f"What is the mathematical AREA scale factor (k²) between the model and the actual building?\\n"
        f"(How many square centimetres in the real building does 1 cm² of model area represent?)"
    )'''
new_25 = '''    prompt = (
        f"Refer to the area scale factor diagram shown (Scale ratio 1 : {scale}). "
        f"What is the mathematical AREA scale factor (k²) between the model and the actual building?\\n"
        f"(How many square centimetres in the real building does 1 cm² of model area represent?)"
    )
    d_spec_25 = {
        "kind": "mensuration_2d",
        "title": f"Area Scaling Factor k² (Scale 1 : {scale})",
        "shape": "square",
        "width": 25,
        "height": 25,
        "labels": {"scale": f"1 : {scale}", "area_factor": f"{area_factor:,}"},
    }'''
c_av = c_av.replace(old_25, new_25)
idx_25 = c_av.find('gr12_models_subskill_25')
idx_diff_25 = c_av.find('difficulty="easy",\n    )', idx_25)
c_av = c_av[:idx_diff_25] + 'difficulty="easy",\n        diagram_spec=d_spec_25,\n    )' + c_av[idx_diff_25 + len('difficulty="easy",\n    )'):]

# 26
old_26 = '''    prompt = (
        f"A detailed scale model of a hospital maternity ward is built to a scale of 1 : {scale}.\\n"
        f"On the model, the floor area of the main ward measures {_fmt(model_area_cm2, 1)} cm².\\n\\n"
        f"Calculate the ACTUAL real-world floor area of the ward in square metres (m²)."
    )'''
new_26 = '''    prompt = (
        f"Refer to the maternity ward scale model floor plan shown in the diagram (scale ratio 1 : {scale}). "
        f"On the model, the floor area of the ward measures {_fmt(model_area_cm2, 1)} cm² on paper.\\n\\n"
        f"Calculate the ACTUAL real-world floor area of the ward in square metres (m²)."
    )
    d_spec_26 = {
        "kind": "floor_plan",
        "title": f"Hospital Ward Model Area ({_fmt(model_area_cm2, 1)} cm² at 1 : {scale})",
        "rooms": [{"name": "Maternity Ward", "length": 20, "width": 15}],
        "annotations": [{"text": f"Model: {_fmt(model_area_cm2, 1)} cm²"}],
    }'''
c_av = c_av.replace(old_26, new_26)
idx_26 = c_av.find('gr12_models_subskill_26')
idx_diff_26 = c_av.find('difficulty="medium",\n    )', idx_26)
c_av = c_av[:idx_diff_26] + 'difficulty="medium",\n        diagram_spec=d_spec_26,\n    )' + c_av[idx_diff_26 + len('difficulty="medium",\n    )'):]

# 27
old_27 = '''    prompt = (
        f"A 3D solid model of a municipal water purification cylinder is constructed at a linear scale of 1 : {scale}.\\n"
        f"What is the mathematical VOLUME scale factor (k³) between the model and the real cylinder?\\n"
        f"(How many cubic centimetres of real volume does 1 cm³ of model volume represent?)"
    )'''
new_27 = '''    prompt = (
        f"Refer to the volume scale factor representation shown in the diagram (Scale ratio 1 : {scale}). "
        f"What is the mathematical VOLUME scale factor (k³) between the model and the real purification cylinder?\\n"
        f"(How many cubic centimetres of real volume does 1 cm³ of model volume represent?)"
    )
    d_spec_27 = {
        "kind": "mensuration_2d",
        "title": f"Volume Scaling Factor k³ (Scale 1 : {scale})",
        "shape": "cylinder",
        "width": 25,
        "height": 40,
        "labels": {"scale": f"1 : {scale}", "vol_factor": f"{vol_factor:,}"},
    }'''
c_av = c_av.replace(old_27, new_27)
idx_27 = c_av.find('gr12_models_subskill_27')
idx_diff_27 = c_av.find('difficulty="easy",\n    )', idx_27)
c_av = c_av[:idx_diff_27] + 'difficulty="easy",\n        diagram_spec=d_spec_27,\n    )' + c_av[idx_diff_27 + len('difficulty="easy",\n    )'):]

# 28
old_28 = '''    prompt = (
        f"A scaled hydraulic model of a farm reservoir holds {_fmt(model_vol_ml, 1)} mL of water (where 1 mL = 1 cm³).\\n"
        f"The model is constructed at a scale of 1 : {scale}.\\n\\n"
        f"Calculate the actual storage capacity of the real reservoir in litres (L)."
    )'''
new_28 = '''    prompt = (
        f"Refer to the reservoir scale model shown in the diagram (scale ratio 1 : {scale}). "
        f"The model holds {_fmt(model_vol_ml, 1)} mL of water (1 mL = 1 cm³).\\n\\n"
        f"Calculate the actual storage capacity of the real reservoir in litres (L)."
    )
    d_spec_28 = {
        "kind": "mensuration_2d",
        "title": f"Reservoir Scale Model ({_fmt(model_vol_ml, 1)} mL at 1 : {scale})",
        "shape": "cylinder",
        "width": 30,
        "height": 25,
        "labels": {"model_vol": f"{_fmt(model_vol_ml, 1)} mL", "scale": f"1 : {scale}"},
    }'''
c_av = c_av.replace(old_28, new_28)
idx_28 = c_av.find('gr12_models_subskill_28')
idx_diff_28 = c_av.find('difficulty="medium",\n    )', idx_28)
c_av = c_av[:idx_diff_28] + 'difficulty="medium",\n        diagram_spec=d_spec_28,\n    )' + c_av[idx_diff_28 + len('difficulty="medium",\n    )'):]

# 30
old_30 = '''    prompt = (
        "A student is calculating the real floor area of a hall from a 1 : 100 scale model. "
        "The model floor area measures 500 cm².\n"
        "The student calculates:\n"
        "  Real Area = 500 cm² × 100 = 50 000 cm² = 5 m².\n\n"
        "Explain the conceptual error in the student's calculation and state the correct method."
    )'''
new_30 = '''    v_cm2 = r.choice([400, 500, 600, 800])
    prompt = (
        f"Refer to the area scaling misconception diagram shown. "
        f"A student calculates the real floor area of a hall from a 1 : 100 scale model measuring {v_cm2} cm² by multiplying by 100:\\n"
        f"  Real Area = {v_cm2} cm² × 100 = {v_cm2 * 100:,} cm² = {v_cm2 / 100:.1f} m².\\n\\n"
        f"Explain the conceptual error in the student's calculation and state the correct method."
    )
    d_spec_30 = {
        "kind": "floor_plan",
        "title": f"Scaling Misconception Analysis (Model {v_cm2} cm²)",
        "rooms": [{"name": "Hall", "length": 25, "width": 20}],
        "annotations": [{"text": f"Model: {v_cm2} cm² (Scale 1 : 100)"}],
    }'''
c_av = c_av.replace(old_30, new_30)
idx_30 = c_av.find('gr12_models_subskill_30')
idx_diff_30 = c_av.find('difficulty="easy",\n    )', idx_30)
c_av = c_av[:idx_diff_30] + 'difficulty="easy",\n        diagram_spec=d_spec_30,\n    )' + c_av[idx_diff_30 + len('difficulty="easy",\n    )'):]

# 31
old_31 = '''    prompt = (
        f"A physical 1 : {scale} scale model of a concert hall is tested inside an acoustics laboratory.\\n"
        f"To model the physical reflection of sound waves correctly, wavelengths must be scaled down by {scale}.\\n"
        f"Because wave speed is constant (v = f × λ), frequency is inversely proportional to wavelength.\\n\\n"
        f"If the real orchestra sound has a pitch frequency of {_fmt(test_freq_hz, 0)} Hz, "
        f"what test frequency must the acoustic speaker emit inside the 1 : {scale} model?"
    )'''
new_31 = '''    prompt = (
        f"Refer to the acoustic scale model test diagram shown (Scale ratio 1 : {scale}). "
        f"To model the reflection of sound waves correctly, wavelengths are scaled down by {scale}. "
        f"If the real orchestra sound has a pitch frequency of {_fmt(test_freq_hz, 0)} Hz, "
        f"what test frequency must the acoustic speaker emit inside the 1 : {scale} model?"
    )
    d_spec_31 = {
        "kind": "mensuration_2d",
        "title": f"Acoustic Testing ({test_freq_hz} Hz at Scale 1 : {scale})",
        "shape": "wave",
        "width": 50,
        "height": 20,
        "labels": {"freq": f"{test_freq_hz} Hz", "scale": f"1 : {scale}"},
    }'''
c_av = c_av.replace(old_31, new_31)
idx_31 = c_av.find('gr12_models_subskill_31')
idx_diff_31 = c_av.find('difficulty="medium",\n    )', idx_31)
c_av = c_av[:idx_diff_31] + 'difficulty="medium",\n        diagram_spec=d_spec_31,\n    )' + c_av[idx_diff_31 + len('difficulty="medium",\n    )'):]

open(p_av, "w", encoding="utf-8").write(c_av)
print("Updated area_volume_scaling_factors.py (6 subskills)")


# ---------------------------------------------------------------------------
# 5. assembly_instructions_packaging.py (37)
# ---------------------------------------------------------------------------
p_aip = "caps-ai-backend/app/utils/mathematical_literacy/gr12_maps_and_plans_models/assembly_instructions_packaging.py"
c_aip = open(p_aip, "r", encoding="utf-8").read()

old_37 = '''    prompt = (
        f"A manufacturer designs a heavy-duty corrugated shipping box for flat-pack furniture.\\n"
        f"The exterior dimensions of the box are {_fmt(ext_l_mm, 0)} mm long × {_fmt(ext_w_mm, 0)} mm wide × {_fmt(ext_h_mm, 0)} mm high.\\n"
        f"The box is made from double-wall corrugated cardboard of thickness {_fmt(wall_thickness_mm, 1)} mm on all sides.\\n\\n"
        f"Calculate the internal length, width, and height of the box (deducting wall thickness from both sides), in millimetres."
    )'''
new_37 = '''    prompt = (
        f"Refer to the corrugated shipping carton specification shown in the diagram. "
        f"The exterior dimensions of the box are {_fmt(ext_l_mm, 0)} mm long × {_fmt(ext_w_mm, 0)} mm wide × {_fmt(ext_h_mm, 0)} mm high, "
        f"made from double-wall cardboard of thickness {_fmt(wall_thickness_mm, 1)} mm on all sides.\\n\\n"
        f"Calculate the internal length, width, and height of the box (deducting wall thickness from both sides), in millimetres."
    )
    d_spec_37 = {
        "kind": "packaging_spec",
        "title": f"Corrugated Carton Internal Capacity ({ext_l_mm} × {ext_w_mm} × {ext_h_mm} mm)",
        "wall_thickness_mm": wall_thickness_mm,
        "dimensions": {"length": ext_l_mm, "width": ext_w_mm, "height": ext_h_mm},
    }'''
c_aip = c_aip.replace(old_37, new_37)
idx_37 = c_aip.find('gr12_models_subskill_37')
idx_diff_37 = c_aip.find('difficulty="easy",\n    )', idx_37)
c_aip = c_aip[:idx_diff_37] + 'difficulty="easy",\n        diagram_spec=d_spec_37,\n    )' + c_aip[idx_diff_37 + len('difficulty="easy",\n    )'):]
open(p_aip, "w", encoding="utf-8").write(c_aip)
print("Updated assembly_instructions_packaging.py (1 subskill)")


# ---------------------------------------------------------------------------
# 6. contour_topographic_site_models.py (47, 48, 50, 51)
# ---------------------------------------------------------------------------
p_ct = "caps-ai-backend/app/utils/mathematical_literacy/gr12_maps_and_plans_models/contour_topographic_site_models.py"
c_ct = open(p_ct, "r", encoding="utf-8").read()

# 47
old_47 = '''    prompt = (
        f"An architecture student is building a stepped topographical site model from stacked foam board layers.\\n"
        f"The contour map has a vertical interval of {_fmt(contour_interval_m, 1)} m between successive contour lines.\\n"
        f"The vertical scale of the physical model is 1 : {vert_scale}.\\n\\n"
        f"What thickness of foam board (in millimetres) must the student use for each contour step layer?"
    )'''
new_47 = '''    prompt = (
        f"Refer to the stepped contour model diagram shown (vertical scale ratio 1 : {vert_scale}). "
        f"The contour map has a vertical interval of {_fmt(contour_interval_m, 1)} m between successive contour lines.\\n\\n"
        f"What thickness of foam board (in millimetres) must the student use for each contour step layer?"
    )
    d_spec_47 = {
        "kind": "elevation_view",
        "title": f"Stepped Contour Model (Interval {_fmt(contour_interval_m, 1)} m, Scale 1 : {vert_scale})",
        "interval_m": contour_interval_m,
        "vert_scale": vert_scale,
    }'''
c_ct = c_ct.replace(old_47, new_47)
idx_47 = c_ct.find('gr12_models_subskill_47')
idx_diff_47 = c_ct.find('difficulty="easy",\n    )', idx_47)
c_ct = c_ct[:idx_diff_47] + 'difficulty="easy",\n        diagram_spec=d_spec_47,\n    )' + c_ct[idx_diff_47 + len('difficulty="easy",\n    )'):]

# 48
old_48 = '''    prompt = (
        "On a stepped topographical scale model, a student notices a series of closed concentric contour rings.\\n"
        "The outermost ring is labeled '120 m' and the innermost central ring is labeled '180 m'.\\n\\n"
        "Does this contour pattern represent a hill peak or a valley depression, and how would the pattern differ for the opposite feature?"
    )'''
new_48 = '''    outer_m = r.choice([100, 120, 140])
    inner_m = outer_m + r.choice([40, 60, 80])
    prompt = (
        f"Refer to the concentric contour rings shown in the diagram. "
        f"The outermost ring is labeled '{outer_m} m' and the innermost central ring is labeled '{inner_m} m'.\\n\\n"
        f"Does this contour pattern represent a hill peak or a valley depression, and how would the pattern differ for the opposite feature?"
    )
    d_spec_48 = {
        "kind": "site_plan",
        "title": f"Concentric Contour Model ({outer_m} m to {inner_m} m)",
        "contours": [{"elevation": outer_m}, {"elevation": outer_m + 20}, {"elevation": inner_m}],
    }'''
c_ct = c_ct.replace(old_48, new_48)
idx_48 = c_ct.find('gr12_models_subskill_48')
idx_diff_48 = c_ct.find('difficulty="easy",\n    )', idx_48)
c_ct = c_ct[:idx_diff_48] + 'difficulty="easy",\n        diagram_spec=d_spec_48,\n    )' + c_ct[idx_diff_48 + len('difficulty="easy",\n    )'):]

# 50
old_50 = '''    prompt = (
        f"A civil earthworks contractor is terracing a sloping hillside site for an RDP housing development.\\n"
        f"The cut volume excavated from higher ground is {_fmt(cut_vol_m3, 0)} m³ in situ.\\n"
        f"Due to soil loosening, excavated soil expands by 15% (bulking factor = 1,15).\\n"
        f"The fill volume required to build up lower terraces is {_fmt(fill_required_m3, 0)} m³ of compacted soil.\\n\\n"
        f"Calculate the net loose soil surplus (or deficit) in cubic metres (m³)."
    )'''
new_50 = '''    prompt = (
        f"Refer to the cut-and-fill terracing diagram shown. "
        f"A contractor excavates {_fmt(cut_vol_m3, 0)} m³ of cut soil from higher ground (15% bulking factor = 1,15). "
        f"The compacted fill required for lower terraces is {_fmt(fill_required_m3, 0)} m³.\\n\\n"
        f"Calculate the net loose soil surplus (or deficit) in cubic metres (m³)."
    )
    d_spec_50 = {
        "kind": "site_plan",
        "title": f"Cut-and-Fill Terracing ({_fmt(cut_vol_m3, 0)} m³ Cut)",
        "cut_volume_m3": cut_vol_m3,
        "bulking_factor": bulking_factor,
        "fill_required_m3": fill_required_m3,
    }'''
c_ct = c_ct.replace(old_50, new_50)
idx_50 = c_ct.find('gr12_models_subskill_50')
idx_diff_50 = c_ct.find('difficulty="medium",\n    )', idx_50)
c_ct = c_ct[:idx_diff_50] + 'difficulty="medium",\n        diagram_spec=d_spec_50,\n    )' + c_ct[idx_diff_50 + len('difficulty="medium",\n    )'):]

# 51
old_51 = '''    prompt = (
        f"An architect is designing a shopping centre parking lot drawn to a scale of 1 : {scale}.\\n"
        f"Each standard parking bay measures {_fmt(bay_l_m, 1)} m long by {_fmt(bay_w_m, 1)} m wide.\\n\\n"
        f"What should be the length and width of each parking bay as drawn on the 1 : {scale} plan, in centimetres?"
    )'''
new_51 = '''    prompt = (
        f"Refer to the parking layout plan shown in the diagram (scale ratio 1 : {scale}). "
        f"Each standard parking bay measures {_fmt(bay_l_m, 1)} m long by {_fmt(bay_w_m, 1)} m wide.\\n\\n"
        f"What should be the length and width of each parking bay as drawn on the 1 : {scale} plan, in centimetres?"
    )
    d_spec_51 = {
        "kind": "site_plan",
        "title": f"Parking Bay Layout ({bay_l_m} m × {bay_w_m} m at 1 : {scale})",
        "bay": {"length": bay_l_m, "width": bay_w_m},
        "aisle_width": aisle_w_m,
        "scale": scale,
    }'''
c_ct = c_ct.replace(old_51, new_51)
idx_51 = c_ct.find('gr12_models_subskill_51')
idx_diff_51 = c_ct.find('difficulty="easy",\n    )', idx_51)
c_ct = c_ct[:idx_diff_51] + 'difficulty="easy",\n        diagram_spec=d_spec_51,\n    )' + c_ct[idx_diff_51 + len('difficulty="easy",\n    )'):]

open(p_ct, "w", encoding="utf-8").write(c_ct)
print("Updated contour_topographic_site_models.py (4 subskills)")
