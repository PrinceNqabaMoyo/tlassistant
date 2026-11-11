"""Fix Batch B diagram specs for gr12_maps_and_plans_models."""
import re

# 1. area_volume_scaling_factors.py
av_path = "caps-ai-backend/app/utils/mathematical_literacy/gr12_maps_and_plans_models/area_volume_scaling_factors.py"
with open(av_path, "r", encoding="utf-8") as f:
    av_code = f.read()

# Define d_spec_25
av_code = av_code.replace(
    '    area_factor = scale ** 2\n\n    prompt = (',
    '''    area_factor = scale ** 2

    d_spec_25 = {
        "kind": "mensuration_2d",
        "shape": "square_pavilion",
        "scale": f"1:{scale}",
        "title": f"Pavilion Model (1 : {scale})",
        "area_ratio": f"1:{area_factor}",
    }

    prompt = ('''
)

# Define d_spec_26
av_code = av_code.replace(
    '    real_area_m2 = (model_area_cm2 * (scale ** 2)) / 10000.0\n\n    prompt = (',
    '''    real_area_m2 = (model_area_cm2 * (scale ** 2)) / 10000.0

    d_spec_26 = {
        "kind": "floor_plan",
        "title": f"Classroom Floor Plan (1 : {scale})",
        "rooms": [{"name": "Classroom", "area_cm2": model_area_cm2}],
    }

    prompt = ('''
)

# Define d_spec_27
av_code = av_code.replace(
    '    vol_factor = scale ** 3\n\n    prompt = (',
    '''    vol_factor = scale ** 3

    d_spec_27 = {
        "kind": "mensuration_3d",
        "shape": "cylinder",
        "scale": f"1:{scale}",
        "title": f"Cylinder Purification Model (1 : {scale})",
        "volume_ratio": f"1:{vol_factor}",
    }

    prompt = ('''
)

# Define d_spec_28
av_code = av_code.replace(
    '    real_vol_m3 = real_vol_cm3 / 1000000.0\n\n    prompt = (',
    '''    real_vol_m3 = real_vol_cm3 / 1000000.0

    d_spec_28 = {
        "kind": "mensuration_3d",
        "shape": "water_tank",
        "scale": f"1:{scale}",
        "title": f"Rainwater Tank Model ({_fmt(model_vol_ml, 0)} mL)",
    }

    prompt = ('''
)

# Define d_spec_30
av_code = av_code.replace(
    'def gen_subskill_30(r: random.Random) -> Dict[str, Any]:\n    """Subskill 30: Scale factor distortion: identifying linear scaling misconception on area."""\n    prompt = (',
    '''def gen_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Subskill 30: Scale factor distortion: identifying linear scaling misconception on area."""
    d_spec_30 = {
        "kind": "floor_plan",
        "title": "Hall Model Floor Area (50 cm² at 1 : 100)",
        "rooms": [{"name": "Hall", "area_cm2": 50}],
    }

    prompt = ('''
)

# Define d_spec_31
av_code = av_code.replace(
    '    model_freq_hz = test_freq_hz * scale\n\n    prompt = (',
    '''    model_freq_hz = test_freq_hz * scale

    d_spec_31 = {
        "kind": "line_graph",
        "title": f"Acoustic Frequency Response (1 : {scale})",
        "series": [{"name": "Acoustic Freq", "points": [[0, 1000], [1, model_freq_hz]]}],
        "x_label": "Domain",
        "y_label": "Frequency (Hz)",
    }

    prompt = ('''
)

with open(av_path, "w", encoding="utf-8") as f:
    f.write(av_code)
print("Updated area_volume_scaling_factors.py")

# 2. assembly_instructions_packaging.py
pkg_path = "caps-ai-backend/app/utils/mathematical_literacy/gr12_maps_and_plans_models/assembly_instructions_packaging.py"
with open(pkg_path, "r", encoding="utf-8") as f:
    pkg_code = f.read()

# Define d_spec_37 and wire to gen_subskill_37
pkg_code = pkg_code.replace(
    '    net_h_mm = ext_h_mm - (2 * wall_thickness_mm)\n\n    prompt = (',
    '''    net_h_mm = ext_h_mm - (2 * wall_thickness_mm)

    d_spec_37 = {
        "kind": "packaging_cartons",
        "title": f"Corrugated Box: {ext_l_mm} x {ext_w_mm} x {ext_h_mm} mm",
        "box": {"length": ext_l_mm, "width": ext_w_mm, "height": ext_h_mm, "wall_thickness": wall_thickness_mm},
    }

    prompt = ('''
)

# In gen_subskill_37, add diagram_spec=d_spec_37
pkg_code = pkg_code.replace(
    '    return _build_question_payload(\n        "gr12_models_subskill_37",\n        prompt,\n        correct_ans,\n        opts,\n        explanation,\n        t1,\n        t2,\n        t3,\n        r,\n        difficulty="medium",\n    )',
    '    return _build_question_payload(\n        "gr12_models_subskill_37",\n        prompt,\n        correct_ans,\n        opts,\n        explanation,\n        t1,\n        t2,\n        t3,\n        r,\n        difficulty="medium",\n        diagram_spec=d_spec_37,\n    )'
)

# In gen_subskill_38, remove diagram_spec=d_spec_37
pkg_code = pkg_code.replace(
    '    return _build_question_payload(\n        "gr12_models_subskill_38",\n        prompt,\n        correct_ans,\n        opts,\n        explanation,\n        t1,\n        t2,\n        t3,\n        r,\n        difficulty="easy",\n        diagram_spec=d_spec_37,\n    )',
    '    return _build_question_payload(\n        "gr12_models_subskill_38",\n        prompt,\n        correct_ans,\n        opts,\n        explanation,\n        t1,\n        t2,\n        t3,\n        r,\n        difficulty="easy",\n    )'
)

with open(pkg_path, "w", encoding="utf-8") as f:
    f.write(pkg_code)
print("Updated assembly_instructions_packaging.py")

# 3. contour_topographic_site_models.py
topo_path = "caps-ai-backend/app/utils/mathematical_literacy/gr12_maps_and_plans_models/contour_topographic_site_models.py"
with open(topo_path, "r", encoding="utf-8") as f:
    topo_code = f.read()

topo_code = topo_code.replace(
    '    layer_thickness_mm = interval_mm / vert_scale\n\n    prompt = (',
    '''    layer_thickness_mm = interval_mm / vert_scale

    d_spec_47 = {
        "kind": "elevation_view",
        "title": f"Contour Profile (Interval: {_fmt(contour_interval_m, 1)} m)",
        "layers": [{"thickness_mm": layer_thickness_mm, "scale": f"1:{vert_scale}"}],
    }

    prompt = ('''
)

topo_code = topo_code.replace(
    'def gen_subskill_48(r: random.Random) -> Dict[str, Any]:\n    """Subskill 48: Identifying hill peaks vs valley depressions in stacked contour models."""\n    prompt = (',
    '''def gen_subskill_48(r: random.Random) -> Dict[str, Any]:
    """Subskill 48: Identifying hill peaks vs valley depressions in stacked contour models."""
    d_spec_48 = {
        "kind": "grid_map",
        "title": "Topographic Contour Rings (1 200 m, 1 220 m, 1 240 m)",
        "contours": [1200, 1220, 1240],
    }

    prompt = ('''
)

topo_code = topo_code.replace(
    '    net_surplus_m3 = available_fill_m3 - fill_required_m3\n\n    prompt = (',
    '''    net_surplus_m3 = available_fill_m3 - fill_required_m3

    d_spec_50 = {
        "kind": "bar_graph",
        "title": f"Cut-and-Fill Excavation Volume ({_fmt(cut_vol_m3, 0)} m³)",
        "series": [{"name": "Cut", "value": cut_vol_m3}, {"name": "Fill", "value": fill_required_m3}],
        "categories": ["Excavated", "Required Fill"],
    }

    prompt = ('''
)

topo_code = topo_code.replace(
    '    model_aisle_mm = (aisle_w_m * 1000.0) / scale\n\n    prompt = (',
    '''    model_aisle_mm = (aisle_w_m * 1000.0) / scale

    d_spec_51 = {
        "kind": "floor_plan",
        "title": "Parking Bay Layout (Scale 1 : 200)",
        "rooms": [{"name": "Parking Bay", "length_m": 5.0, "width_m": 2.5}],
    }

    prompt = ('''
)

with open(topo_path, "w", encoding="utf-8") as f:
    f.write(topo_code)
print("Updated contour_topographic_site_models.py")
