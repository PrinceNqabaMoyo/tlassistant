"""Remediate remaining 14 subskills in gr12_plans_and_scale:
- elevation_plans_multi_view.py (17, 18, 20, 21, 22)
- site_plans_boundaries_servitudes.py (33, 34, 35, 37, 38)
- cross_sectional_details.py (41, 45)
- architectural_floor_plans_symbols.py (29)
- material_takeoffs_costing.py (48)
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# 1. elevation_plans_multi_view.py (17, 18, 20, 21, 22)
# ---------------------------------------------------------------------------
p_ep = "caps-ai-backend/app/utils/mathematical_literacy/gr12_plans_and_scale/elevation_plans_multi_view.py"
c_ep = open(p_ep, "r", encoding="utf-8").read()

# Subskill 17
old_17 = '''    prompt = (
        f"On a municipal building plan, a compass rose points directly toward the top of the page (True North).\\n"
        f"Which architectural elevation corresponds to the exterior wall {target['face']}?"
    )'''
new_17 = '''    prompt = (
        f"Refer to the building plan orientation and compass rose shown in the diagram. "
        f"Which architectural elevation corresponds to the exterior wall {target['face']}?"
    )
    b_deg = 0 if "North" in target["dir"] else (180 if "South" in target["dir"] else (90 if "East" in target["dir"] else 270))
    d_spec_17 = {
        "kind": "compass_bearing",
        "title": f"Plan Orientation ({target['dir']})",
        "bearing_deg": b_deg,
        "target_dir": target["dir"],
    }'''
c_ep = c_ep.replace(old_17, new_17)
idx_17 = c_ep.find('gr12_plans_subskill_17')
idx_diff_17 = c_ep.find('difficulty="easy",\n    )', idx_17)
c_ep = c_ep[:idx_diff_17] + 'difficulty="easy",\n        diagram_spec=d_spec_17,\n    )' + c_ep[idx_diff_17 + len('difficulty="easy",\n    )'):]

# Subskill 18
old_18 = '''    prompt = (
        f"An architectural drawing set includes four orthogonal elevation drawings.\\n"
        f"Which elevation view {item['desc']}?"
    )'''
new_18 = '''    prompt = (
        f"Refer to the orthogonal elevation drawings shown in the diagram. "
        f"Which elevation view {item['desc']}?"
    )
    d_spec_18 = {
        "kind": "elevation_view",
        "title": f"Orthogonal Facade ({item['view']})",
        "view_name": item["view"],
        "features": [item["desc"]],
    }'''
c_ep = c_ep.replace(old_18, new_18)
idx_18 = c_ep.find('gr12_plans_subskill_18')
idx_diff_18 = c_ep.find('difficulty="easy",\n    )', idx_18)
c_ep = c_ep[:idx_diff_18] + 'difficulty="easy",\n        diagram_spec=d_spec_18,\n    )' + c_ep[idx_diff_18 + len('difficulty="easy",\n    )'):]

# Subskill 20
old_20 = '''    prompt = (
        f"One measurement that cannot be seen from the Left Side view of a Wendy house is the width of the front facade.\\n"
        f"The floor plan shows that the front of the structure is {_fmt(real_front_width_m, 1)} m wide.\\n"
        f"The elevation drawings are drawn to a scale of 1 : {scale}.\\n\\n"
        f"Calculate the width of the Wendy house as it should be drawn on the Front view elevation, in centimetres."
    )'''
new_20 = '''    prompt = (
        f"Refer to the Wendy house floor plan and elevation views shown in the diagram (scale ratio 1 : {scale}). "
        f"The front of the structure is {_fmt(real_front_width_m, 1)} m wide on the floor plan.\\n\\n"
        f"Calculate the width of the Wendy house as it should be drawn on the Front view elevation, in centimetres."
    )
    d_spec_20 = {
        "kind": "elevation_view",
        "title": f"Wendy House Elevation (Front Width {_fmt(real_front_width_m, 1)} m)",
        "scale_ratio": f"1 : {scale}",
        "front_width_m": real_front_width_m,
        "plan_width_cm": plan_width_cm,
    }'''
c_ep = c_ep.replace(old_20, new_20)
idx_20 = c_ep.find('gr12_plans_subskill_20')
idx_diff_20 = c_ep.find('difficulty="easy",\n    )', idx_20)
c_ep = c_ep[:idx_diff_20] + 'difficulty="easy",\n        diagram_spec=d_spec_20,\n    )' + c_ep[idx_diff_20 + len('difficulty="easy",\n    )'):]

# Subskill 21
old_21 = '''    prompt = (
        f"On a 1 : {scale} sectional elevation, a pitched roof extends beyond the external brick wall to create eaves.\\n"
        f"The builder's specification stipulates a standard roof overhang of {_fmt(overhang_real_mm, 0)} mm beyond the exterior brick face.\\n\\n"
        f"What distance (in millimetres) should represent this roof overhang on the 1 : {scale} drawing?"
    )'''
new_21 = '''    prompt = (
        f"Refer to the sectional elevation shown in the diagram (scale ratio 1 : {scale}), where a pitched roof creates eaves. "
        f"The specification stipulates a standard roof overhang of {_fmt(overhang_real_mm, 0)} mm beyond the exterior brick face.\\n\\n"
        f"What distance (in millimetres) should represent this roof overhang on the 1 : {scale} drawing?"
    )
    d_spec_21 = {
        "kind": "elevation_view",
        "title": f"Sectional Roof Eaves (Overhang {_fmt(overhang_real_mm, 0)} mm)",
        "scale_ratio": f"1 : {scale}",
        "overhang_mm": overhang_real_mm,
    }'''
c_ep = c_ep.replace(old_21, new_21)
idx_21 = c_ep.find('gr12_plans_subskill_21')
idx_diff_21 = c_ep.find('difficulty="easy",\n    )', idx_21)
c_ep = c_ep[:idx_diff_21] + 'difficulty="easy",\n        diagram_spec=d_spec_21,\n    )' + c_ep[idx_diff_21 + len('difficulty="easy",\n    )'):]

# Subskill 22
old_22 = '''    prompt = (
        f"On a residential elevation plan drawn to a scale of 1 : {scale}, the window sill height "
        f"above finished floor level (AFFL) measures {_fmt(plan_sill_mm, 1)} mm.\\n\\n"
        f"Calculate the actual construction height of the window sill above the floor in millimetres (mm)."
    )'''
new_22 = '''    prompt = (
        f"Refer to the residential elevation plan shown in the diagram (scale ratio 1 : {scale}). "
        f"The window sill height above finished floor level (AFFL) measures {_fmt(plan_sill_mm, 1)} mm on the paper.\\n\\n"
        f"Calculate the actual construction height of the window sill above the floor in millimetres (mm)."
    )
    d_spec_22 = {
        "kind": "elevation_view",
        "title": f"Window Sill Height Plan (Scale 1 : {scale})",
        "scale_ratio": f"1 : {scale}",
        "plan_sill_mm": plan_sill_mm,
        "real_sill_mm": sill_height_real_mm,
    }'''
c_ep = c_ep.replace(old_22, new_22)
idx_22 = c_ep.find('gr12_plans_subskill_22')
idx_diff_22 = c_ep.find('difficulty="easy",\n    )', idx_22)
c_ep = c_ep[:idx_diff_22] + 'difficulty="easy",\n        diagram_spec=d_spec_22,\n    )' + c_ep[idx_diff_22 + len('difficulty="easy",\n    )'):]

open(p_ep, "w", encoding="utf-8").write(c_ep)
print("Updated elevation_plans_multi_view.py (5 subskills)")


# ---------------------------------------------------------------------------
# 2. site_plans_boundaries_servitudes.py (33, 34, 35, 37, 38)
# ---------------------------------------------------------------------------
p_sp = "caps-ai-backend/app/utils/mathematical_literacy/gr12_plans_and_scale/site_plans_boundaries_servitudes.py"
c_sp = open(p_sp, "r", encoding="utf-8").read()

# Subskill 33
old_33 = '''    prompt = (
        f"On a municipal site cadastral plan drawn to a scale of 1 : {scale}, a rectangular residential erf (stand) "
        f"has boundary lengths of {_fmt(plan_l_cm, 1)} cm along the street frontage and {_fmt(plan_w_cm, 1)} cm along the side.\\n\\n"
        f"Calculate the actual area of the erf in square metres (m²)."
    )'''
new_33 = '''    prompt = (
        f"Refer to the municipal site cadastral plan shown in the diagram (scale ratio 1 : {scale}). "
        f"A rectangular residential erf (stand) has boundary lengths of {_fmt(plan_l_cm, 1)} cm along the street frontage and {_fmt(plan_w_cm, 1)} cm along the side on paper.\\n\\n"
        f"Calculate the actual area of the erf in square metres (m²)."
    )
    d_spec_33 = {
        "kind": "site_plan",
        "title": f"Erf Stand Plan ({_fmt(plan_l_cm, 1)} cm × {_fmt(plan_w_cm, 1)} cm)",
        "boundary": {"width": plan_w_cm * 10, "length": plan_l_cm * 10},
        "annotations": [{"text": f"Front: {_fmt(plan_l_cm, 1)} cm"}, {"text": f"Side: {_fmt(plan_w_cm, 1)} cm"}],
    }'''
c_sp = c_sp.replace(old_33, new_33)
idx_33 = c_sp.find('gr12_plans_subskill_33')
idx_diff_33 = c_sp.find('difficulty="easy",\n    )', idx_33)
c_sp = c_sp[:idx_diff_33] + 'difficulty="easy",\n        diagram_spec=d_spec_33,\n    )' + c_sp[idx_diff_33 + len('difficulty="easy",\n    )'):]

# Subskill 34
old_34 = '''    prompt = (
        f"Municipal town planning regulations dictate that total building coverage on a suburban stand "
        f"may NOT exceed 50% of the total erf area.\\n"
        f"A homeowner plans to build on an erf measuring {_fmt(erf_area_m2, 0)} m².\\n"
        f"The proposed structures include:\\n"
        f"  - Main dwelling footprint: {_fmt(house_footprint_m2, 0)} m²\\n"
        f"  - Double garage & storeroom footprint: {_fmt(garage_footprint_m2, 0)} m²\\n\\n"
        f"Calculate the site coverage percentage and state whether the plan complies with municipal bylaws."
    )'''
new_34 = '''    prompt = (
        f"Refer to the site plan and building footprint shown in the diagram. "
        f"Municipal town planning regulations dictate that total building coverage on a suburban stand "
        f"may NOT exceed 50% of the total erf area.\\n"
        f"A homeowner plans to build on an erf measuring {_fmt(erf_area_m2, 0)} m² with dwelling footprint {_fmt(house_footprint_m2, 0)} m² "
        f"and double garage footprint {_fmt(garage_footprint_m2, 0)} m².\\n\\n"
        f"Calculate the site coverage percentage and state whether the plan complies with municipal bylaws."
    )
    d_spec_34 = {
        "kind": "site_plan",
        "title": f"Erf Building Footprint ({int(erf_area_m2)} m² Stand)",
        "boundary": {"width": 80, "length": 100},
        "buildings": [{"name": "Dwelling", "area": house_footprint_m2}, {"name": "Garage", "area": garage_footprint_m2}],
    }'''
c_sp = c_sp.replace(old_34, new_34)
idx_34 = c_sp.find('gr12_plans_subskill_34')
idx_diff_34 = c_sp.find('difficulty="medium",\n    )', idx_34)
c_sp = c_sp[:idx_diff_34] + 'difficulty="medium",\n        diagram_spec=d_spec_34,\n    )' + c_sp[idx_diff_34 + len('difficulty="medium",\n    )'):]

# Subskill 35
old_35 = '''    prompt = (
        f"A site plan for a proposed new dwelling must comply with municipal building lines:\\n"
        f"  - Front street boundary setback: 4,5 m minimum\\n"
        f"  - Side boundary setback: 2,0 m minimum\\n\\n"
        f"On a 1 : {scale} layout plan, the distance from the front erf boundary to the front veranda wall "
        f"measures {_fmt(measured_front_cm, 1)} cm with a ruler.\\n\\n"
        f"Determine the actual front setback distance in metres, and state whether it complies with the municipal building line bylaw."
    )'''
new_35 = '''    prompt = (
        f"Refer to the site layout plan shown in the diagram (scale ratio 1 : {scale}). "
        f"A proposed new dwelling must comply with municipal building lines (front setback 4,5 m, side setback 2,0 m). "
        f"On the plan, the distance from the front erf boundary to the veranda measures {_fmt(measured_front_cm, 1)} cm on paper.\\n\\n"
        f"Determine the actual front setback distance in metres and state whether it complies with the municipal building line bylaw."
    )
    d_spec_35 = {
        "kind": "site_plan",
        "title": f"Building Line Setbacks (Scale 1 : {scale})",
        "boundary": {"width": 80, "length": 100},
        "setback": {"front_cm": measured_front_cm, "real_front_m": actual_front_m},
    }'''
c_sp = c_sp.replace(old_35, new_35)
idx_35 = c_sp.find('gr12_plans_subskill_35')
idx_diff_35 = c_sp.find('difficulty="medium",\n    )', idx_35)
c_sp = c_sp[:idx_diff_35] + 'difficulty="medium",\n        diagram_spec=d_spec_35,\n    )' + c_sp[idx_diff_35 + len('difficulty="medium",\n    )'):]

# Subskill 37
old_37 = '''    prompt = (
        f"To allow passenger vehicles to turn around on site without reversing into a busy public road, "
        f"a site plan includes a circular turning head with an outer radius of {_fmt(turning_radius_m, 1)} m.\\n"
        f"The site plan is drawn to a scale of 1 : {scale}.\\n\\n"
        f"What is the DIAMETER of this vehicular turning circle on the scale drawing, in centimetres?"
    )'''
new_37 = '''    turning_radius_m = r.choice([5.0, 6.0, 7.5])
    turning_diameter_m = 2 * turning_radius_m
    scale = r.choice([100, 200, 250])
    plan_diameter_cm = (turning_diameter_m * 100.0) / scale
    prompt = (
        f"Refer to the site plan shown in the diagram (scale ratio 1 : {scale}). "
        f"To allow passenger vehicles to turn around on site, a circular turning head has an outer radius of {_fmt(turning_radius_m, 1)} m.\\n\\n"
        f"What is the DIAMETER of this vehicular turning circle on the scale drawing, in centimetres?"
    )
    d_spec_37 = {
        "kind": "site_plan",
        "title": f"Driveway Turning Circle (Scale 1 : {scale})",
        "boundary": {"width": 80, "length": 100},
        "turning_circle": {"radius_m": turning_radius_m, "diameter_m": turning_diameter_m, "plan_cm": plan_diameter_cm},
    }'''
c_sp = c_sp.replace(old_37, new_37)
idx_37 = c_sp.find('gr12_plans_subskill_37')
idx_diff_37 = c_sp.find('difficulty="easy",\n    )', idx_37)
c_sp = c_sp[:idx_diff_37] + 'difficulty="easy",\n        diagram_spec=d_spec_37,\n    )' + c_sp[idx_diff_37 + len('difficulty="easy",\n    )'):]

# Subskill 38
old_38 = '''    prompt = (
        f"A homeowner is erecting a perimeter security wall around a rectangular property measuring "
        f"{_fmt(erf_l_m, 1)} m long by {_fmt(erf_w_m, 1)} m wide.\\n"
        f"Openings must be left in the front wall for:\\n"
        f"  - A sliding vehicular driveway gate: {_fmt(driveway_gate_w_m, 1)} m wide\\n"
        f"  - A pedestrian security gate: {_fmt(pedestrian_gate_w_m, 1)} m wide\\n\\n"
        f"Calculate the TOTAL net linear metres of brick wall to be constructed."
    )'''
new_38 = '''    prompt = (
        f"Refer to the property boundary diagram shown. "
        f"A homeowner is erecting a perimeter security wall around a property measuring {_fmt(erf_l_m, 1)} m long by {_fmt(erf_w_m, 1)} m wide, "
        f"with driveway gate {_fmt(driveway_gate_w_m, 1)} m and pedestrian gate {_fmt(pedestrian_gate_w_m, 1)} m.\\n\\n"
        f"Calculate the TOTAL net linear metres of brick wall to be constructed."
    )
    d_spec_38 = {
        "kind": "site_plan",
        "title": f"Erf Boundary Fence ({int(erf_l_m)} m × {int(erf_w_m)} m)",
        "boundary": {"width": erf_w_m, "length": erf_l_m},
        "gates": [{"name": "Driveway", "width": driveway_gate_w_m}, {"name": "Pedestrian", "width": pedestrian_gate_w_m}],
    }'''
c_sp = c_sp.replace(old_38, new_38)
idx_38 = c_sp.find('gr12_plans_subskill_38')
idx_diff_38 = c_sp.find('difficulty="easy",\n    )', idx_38)
c_sp = c_sp[:idx_diff_38] + 'difficulty="easy",\n        diagram_spec=d_spec_38,\n    )' + c_sp[idx_diff_38 + len('difficulty="easy",\n    )'):]

open(p_sp, "w", encoding="utf-8").write(c_sp)
print("Updated site_plans_boundaries_servitudes.py (5 subskills)")


# ---------------------------------------------------------------------------
# 3. cross_sectional_details.py (41, 45)
# ---------------------------------------------------------------------------
p_cs = "caps-ai-backend/app/utils/mathematical_literacy/gr12_plans_and_scale/cross_sectional_details.py"
c_cs = open(p_cs, "r", encoding="utf-8").read()

# Subskill 41
old_41 = '''    prompt = (
        f"A structural engineer's cross-sectional foundation detail is drawn to a scale of 1 : {scale}.\\n"
        f"The specification lists the following site dimensions:\\n"
        f"  - Strip footing concrete width: {_fmt(footing_w_mm, 0)} mm\\n"
        f"  - Reinforced floor slab thickness: {_fmt(slab_thickness_mm, 0)} mm\\n"
        f"  - Total foundation trench excavation depth: {_fmt(trench_depth_mm, 0)} mm\\n\\n"
        f"What should be the DRAWN measurement (in millimetres) of the foundation trench depth on the 1 : {scale} drawing?"
    )'''
new_41 = '''    prompt = (
        f"Refer to the foundation cross-sectional technical detail shown in the diagram (scale ratio 1 : {scale}). "
        f"The trench excavation depth is {_fmt(trench_depth_mm, 0)} mm with footing width {_fmt(footing_w_mm, 0)} mm and floor slab thickness {_fmt(slab_thickness_mm, 0)} mm.\\n\\n"
        f"What should be the DRAWN measurement (in millimetres) of the foundation trench depth on the 1 : {scale} drawing?"
    )
    d_spec_41 = {
        "kind": "elevation_view",
        "title": f"Foundation Trench Cross-Section (Trench {_fmt(trench_depth_mm, 0)} mm)",
        "scale_ratio": f"1 : {scale}",
        "footing_w_mm": footing_w_mm,
        "trench_depth_mm": trench_depth_mm,
        "slab_mm": slab_thickness_mm,
    }'''
c_cs = c_cs.replace(old_41, new_41)
idx_41 = c_cs.find('gr12_plans_subskill_41')
idx_diff_41 = c_cs.find('difficulty="easy",\n    )', idx_41)
c_cs = c_cs[:idx_diff_41] + 'difficulty="easy",\n        diagram_spec=d_spec_41,\n    )' + c_cs[idx_diff_41 + len('difficulty="easy",\n    )'):]

# Subskill 45
old_45 = '''    prompt = (
        f"SANS 10400 building standards require that Finished Floor Level (FFL) must be at least "
        f"150 mm above Natural Ground Level (NGL) to prevent stormwater and moisture ingress.\\n"
        f"A building inspector checks a foundation section drawing and measures an actual step-up "
        f"of {actual_step_mm} mm from NGL to FFL.\\n\\n"
        f"State whether this construction detail complies with SANS 10400, and calculate the margin (difference in mm) "
        f"relative to the minimum requirement."
    )'''
new_45 = '''    prompt = (
        f"Refer to the foundation cross-sectional detail shown in the diagram. "
        f"SANS 10400 building standards require that Finished Floor Level (FFL) must be at least 150 mm above Natural Ground Level (NGL). "
        f"An inspector notes a step-up of {actual_step_mm} mm from NGL to FFL.\\n\\n"
        f"State whether this construction detail complies with SANS 10400, and calculate the margin (difference in mm) relative to the minimum requirement."
    )
    d_spec_45 = {
        "kind": "elevation_view",
        "title": f"FFL vs NGL Step-Up Detail ({actual_step_mm} mm)",
        "step_mm": actual_step_mm,
        "min_sans_mm": min_step_mm,
    }'''
c_cs = c_cs.replace(old_45, new_45)
idx_45 = c_cs.find('gr12_plans_subskill_45')
idx_diff_45 = c_cs.find('difficulty="easy",\n    )', idx_45)
c_cs = c_cs[:idx_diff_45] + 'difficulty="easy",\n        diagram_spec=d_spec_45,\n    )' + c_cs[idx_diff_45 + len('difficulty="easy",\n    )'):]

open(p_cs, "w", encoding="utf-8").write(c_cs)
print("Updated cross_sectional_details.py (2 subskills)")


# ---------------------------------------------------------------------------
# 4. architectural_floor_plans_symbols.py (29)
# ---------------------------------------------------------------------------
p_fl = "caps-ai-backend/app/utils/mathematical_literacy/gr12_plans_and_scale/architectural_floor_plans_symbols.py"
c_fl = open(p_fl, "r", encoding="utf-8").read()
old_29 = '''    prompt = (
        f"An architectural floor plan displays two adjoining bedrooms:\\n"
        f"  - Bedroom 1 internal dimensions: {_fmt(l1, 1)} m × {_fmt(w1, 1)} m\\n"
        f"  - Bedroom 2 internal dimensions: {_fmt(l2, 1)} m × {_fmt(w2, 1)} m\\n\\n"
        f"Calculate the TOTAL net internal floor area of both bedrooms combined in square metres (m²)."
    )'''
new_29 = '''    prompt = (
        f"Refer to the two-bedroom floor plan shown in the diagram. "
        f"Bedroom 1 has dimensions of {_fmt(l1, 1)} m × {_fmt(w1, 1)} m, and Bedroom 2 has dimensions of {_fmt(l2, 1)} m × {_fmt(w2, 1)} m.\\n\\n"
        f"Calculate the TOTAL net internal floor area of both bedrooms combined in square metres (m²)."
    )
    d_spec_29 = {
        "kind": "floor_plan",
        "title": f"Two-Bedroom Floor Plan ({_fmt(l1, 1)} m × {_fmt(w1, 1)} m)",
        "rooms": [{"name": "Bedroom 1", "length": l1, "width": w1}, {"name": "Bedroom 2", "length": l2, "width": w2}],
    }'''
c_fl = c_fl.replace(old_29, new_29)
idx_29 = c_fl.find('gr12_plans_subskill_29')
idx_diff_29 = c_fl.find('difficulty="easy",\n    )', idx_29)
c_fl = c_fl[:idx_diff_29] + 'difficulty="easy",\n        diagram_spec=d_spec_29,\n    )' + c_fl[idx_diff_29 + len('difficulty="easy",\n    )'):]
open(p_fl, "w", encoding="utf-8").write(c_fl)
print("Updated architectural_floor_plans_symbols.py (1 subskill)")


# ---------------------------------------------------------------------------
# 5. material_takeoffs_costing.py (48)
# ---------------------------------------------------------------------------
p_mt = "caps-ai-backend/app/utils/mathematical_literacy/gr12_plans_and_scale/material_takeoffs_costing.py"
c_mt = open(p_mt, "r", encoding="utf-8").read()
old_48 = '''    prompt = (
        f"A timber skirting board is to be installed around the internal perimeter of a room measuring "
        f"{_fmt(room_l_m, 1)} m long by {_fmt(room_w_m, 1)} m wide.\\n"
        f"Skirting is NOT installed across openings. Deduct:\\n"
        f"  - Entrance doorway: {_fmt(door_opening_m, 1)} m\\n"
        f"  - Built-in cupboard sliding front opening: {_fmt(cupboard_opening_m, 1)} m\\n\\n"
        f"Calculate the net linear metres of skirting board required."
    )'''
new_48 = '''    prompt = (
        f"Refer to the room layout shown in the diagram. "
        f"A timber skirting board is installed around the internal perimeter of a room measuring {_fmt(room_l_m, 1)} m long by {_fmt(room_w_m, 1)} m wide, "
        f"deducting the door opening of {_fmt(door_opening_m, 1)} m and built-in cupboard opening of {_fmt(cupboard_opening_m, 1)} m.\\n\\n"
        f"Calculate the net linear metres of skirting board required."
    )
    d_spec_48 = {
        "kind": "floor_plan",
        "title": f"Room Skirting Layout ({_fmt(room_l_m, 1)} m × {_fmt(room_w_m, 1)} m)",
        "rooms": [{"name": "Living Room", "length": room_l_m, "width": room_w_m}],
        "openings": [{"name": "Door", "width": door_opening_m}, {"name": "Cupboard", "width": cupboard_opening_m}],
    }'''
c_mt = c_mt.replace(old_48, new_48)
idx_48 = c_mt.find('gr12_plans_subskill_48')
idx_diff_48 = c_mt.find('difficulty="easy",\n    )', idx_48)
c_mt = c_mt[:idx_diff_48] + 'difficulty="easy",\n        diagram_spec=d_spec_48,\n    )' + c_mt[idx_diff_48 + len('difficulty="easy",\n    )'):]
open(p_mt, "w", encoding="utf-8").write(c_mt)
print("Updated material_takeoffs_costing.py (1 subskill)")
