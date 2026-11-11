"""Subskills 25-32: Area & Volume Scaling Factors (k, k², k³) for Grade 12 Maps & Plans (Models)."""
from __future__ import annotations

import random
from typing import Any, Dict

from .common import (
    SA_NAMES,
    _build_options,
    _build_question_payload,
    _fmt,
)


def gen_subskill_25(r: random.Random) -> Dict[str, Any]:
    """Subskill 25: Area scale factor (k²) calculation between model and real structure."""
    scale = r.choice([20, 25, 50, 100])
    area_factor = scale ** 2

    d_spec_25 = {
        "diagram_role": "context",
        "kind": "mensuration_2d",
        "shape": "square_pavilion",
        "scale": f"1:{scale}",
        "title": f"Pavilion Model (1 : {scale})",
        "area_ratio": f"1:{area_factor}",
    }

    prompt = (
        f"An architectural model of an exhibition pavilion is built to a linear number scale of 1 : {scale}.\n\n"
        f"What is the mathematical AREA scale factor relating the surface area of the model to the actual surface area of the building?"
    )

    correct_ans = f"1 : {_fmt(area_factor, 0)}"
    custom_opts = [
        correct_ans,
        f"1 : {_fmt(scale, 0)}",
        f"1 : {_fmt(scale * 2, 0)}",
        f"1 : {_fmt(scale ** 3, 0)}",
    ]

    t1 = "Remember that area has two dimensions (length × width)."
    t2 = f"When lengths scale by a factor of {scale}, areas scale by {scale}²."
    t3 = f"Area scale factor = ({scale})² = {area_factor}. Therefore the ratio is 1 : {_fmt(area_factor, 0)}."

    explanation = [
        f"Step 1: Identify that area is two-dimensional: Area scale factor = (Linear scale)² [1 Mark: Method].",
        f"Step 2: Calculate ({scale})² = {scale} × {scale} = {area_factor} [1 Mark: Method].",
        f"Step 3: State the area scale ratio: 1 : {_fmt(area_factor, 0)} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_25",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_25,
    )


def gen_subskill_26(r: random.Random) -> Dict[str, Any]:
    """Subskill 26: Real floor area from model plan area (cm² to m²)."""
    scale = r.choice([20, 50, 100])
    # Model area in cm²
    model_area_cm2 = r.choice([120.0, 180.0, 240.0, 300.0])
    # Real area in cm² = model_area_cm2 * (scale^2)
    # 1 m² = 10 000 cm² -> real_area_m2 = (model_area_cm2 * (scale^2)) / 10 000
    real_area_m2 = (model_area_cm2 * (scale ** 2)) / 10000.0

    d_spec_26 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Classroom Floor Plan (1 : {scale})",
        "rooms": [{"name": "Classroom", "area_cm2": model_area_cm2}],
    }

    prompt = (
        f"Refer to the accompanying 2D architectural floor plan (scale ratio 1 : {scale}) shown in the diagram.\n"
        f"The measured floor area of an open-plan classroom is {_fmt(model_area_cm2, 1)} cm².\n\n"
        f"Calculate the ACTUAL real-life floor area of the classroom in square metres (m²)."
    )

    correct_ans = f"{_fmt(real_area_m2, 2)} m²"
    custom_opts = [
        correct_ans,
        f"{_fmt((model_area_cm2 * scale) / 100.0, 2)} m²",
        f"{_fmt(real_area_m2 / 10.0, 2)} m²",
        f"{_fmt(model_area_cm2, 2)} m²",
    ]

    t1 = f"Multiply the plan area by the area scale factor ({scale}²)."
    t2 = f"Convert the resulting area from cm² to m² by dividing by 10 000 (since 1 m² = 10 000 cm²)."
    t3 = f"Area scale factor = {scale}² = {scale**2}. Real area in cm² = {_fmt(model_area_cm2, 1)} × {scale**2} = {_fmt(model_area_cm2 * (scale**2), 0)} cm². In m² = {_fmt(model_area_cm2 * (scale**2), 0)} ÷ 10 000 = {_fmt(real_area_m2, 2)} m²."

    explanation = [
        f"Step 1: Calculate area scale factor: {scale}² = {scale**2} [1 Mark: Method].",
        f"Step 2: Real area in cm² = {_fmt(model_area_cm2, 1)} cm² × {scale**2} = {_fmt(model_area_cm2 * (scale**2), 0)} cm² [1 Mark: Method].",
        f"Step 3: Convert cm² to m²: {_fmt(model_area_cm2 * (scale**2), 0)} ÷ 10 000 = {_fmt(real_area_m2, 2)} m² [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_26",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_26,
    )


def gen_subskill_27(r: random.Random) -> Dict[str, Any]:
    """Subskill 27: Volume scale factor (k³) calculation for solid shapes."""
    scale = r.choice([10, 20, 25, 50])
    vol_factor = scale ** 3

    d_spec_27 = {
        "diagram_role": "context",
        "kind": "mensuration_3d",
        "shape": "cylinder",
        "scale": f"1:{scale}",
        "title": f"Cylinder Purification Model (1 : {scale})",
        "volume_ratio": f"1:{vol_factor}",
    }

    prompt = (
        f"A 3D solid model of a municipal water purification cylinder is constructed at a linear scale of 1 : {scale}.\n\n"
        f"What is the VOLUME scale ratio relating the volume of the model to the actual volume of the full-sized cylinder?"
    )

    correct_ans = f"1 : {_fmt(vol_factor, 0)}"
    custom_opts = [
        correct_ans,
        f"1 : {_fmt(scale ** 2, 0)}",
        f"1 : {_fmt(scale * 3, 0)}",
        f"1 : {_fmt(scale, 0)}",
    ]

    t1 = "Volume has three dimensions (length × width × height)."
    t2 = f"When linear dimensions scale by {scale}, volume scales by {scale}³."
    t3 = f"Volume scale factor = ({scale})³ = {vol_factor}. Therefore the ratio is 1 : {_fmt(vol_factor, 0)}."

    explanation = [
        f"Step 1: Identify that volume is three-dimensional: Volume scale factor = (Linear scale)³ [1 Mark: Method].",
        f"Step 2: Calculate ({scale})³ = {scale} × {scale} × {scale} = {vol_factor} [1 Mark: Method].",
        f"Step 3: State the volume scale ratio: 1 : {_fmt(vol_factor, 0)} [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_27",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_27,
    )


def gen_subskill_28(r: random.Random) -> Dict[str, Any]:
    """Subskill 28: Water tank/reservoir scale model capacity scaling (cm³ to litres / m³)."""
    scale = r.choice([20, 25, 50])
    model_vol_ml = r.choice([250.0, 400.0, 500.0, 800.0])  # in cm³ / mL
    # 1 cm³ = 1 mL
    # Real volume cm³ = model_vol_ml * (scale^3)
    # 1 m³ = 1 000 000 cm³ = 1 000 L
    real_vol_cm3 = model_vol_ml * (scale ** 3)
    real_vol_litres = real_vol_cm3 / 1000.0
    real_vol_m3 = real_vol_cm3 / 1000000.0

    d_spec_28 = {
        "diagram_role": "context",
        "kind": "mensuration_3d",
        "shape": "water_tank",
        "scale": f"1:{scale}",
        "title": f"Rainwater Tank Model ({_fmt(model_vol_ml, 0)} mL)",
    }

    prompt = (
        f"A laboratory scale model of a rainwater harvesting tank is built to a scale of 1 : {scale}.\n"
        f"When filled with water, the model holds exactly {_fmt(model_vol_ml, 0)} mL (or {_fmt(model_vol_ml, 0)} cm³) of water.\n\n"
        f"Calculate the actual storage capacity of the real JoJo tank in LITRES (L).\n"
        f"(Hint: 1 litre = 1 000 cm³)."
    )

    correct_ans = f"{_fmt(real_vol_litres, 0)} L"
    custom_opts = [
        correct_ans,
        f"{_fmt(model_vol_ml * scale, 0)} L",
        f"{_fmt(model_vol_ml * (scale ** 2), 0)} L",
        f"{_fmt(real_vol_litres / 10, 0)} L",
    ]

    t1 = f"Multiply the model volume by the volume scale factor ({scale}³)."
    t2 = "Convert the total volume from cm³ to litres by dividing by 1 000."
    t3 = f"Volume factor = {scale}³ = {scale**3}. Real cm³ = {_fmt(model_vol_ml, 0)} × {scale**3} = {_fmt(real_vol_cm3, 0)} cm³. Litres = {_fmt(real_vol_cm3, 0)} ÷ 1 000 = {_fmt(real_vol_litres, 0)} L."

    explanation = [
        f"Step 1: Calculate volume scale factor: {scale}³ = {scale**3} [1 Mark: Method].",
        f"Step 2: Real volume in cm³ = {_fmt(model_vol_ml, 0)} cm³ × {scale**3} = {_fmt(real_vol_cm3, 0)} cm³ [1 Mark: Method].",
        f"Step 3: Convert cm³ to litres: {_fmt(real_vol_cm3, 0)} ÷ 1 000 = {_fmt(real_vol_litres, 0)} L [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_28",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
        diagram_spec=d_spec_28,
    )


def gen_subskill_29(r: random.Random) -> Dict[str, Any]:
    """Subskill 29: Model weight vs real weight for identical material density."""
    scale = r.choice([10, 20, 25])
    model_mass_g = r.choice([150.0, 250.0, 350.0, 500.0])
    # Real mass = model_mass_g * (scale^3)
    real_mass_g = model_mass_g * (scale ** 3)
    real_mass_kg = real_mass_g / 1000.0

    prompt = (
        f"A prototype scale model of a pre-cast concrete stormwater pipe is cast from concrete at a scale of 1 : {scale}.\n"
        f"The model pipe has a mass of {_fmt(model_mass_g, 0)} grams.\n\n"
        f"Assuming the real full-sized stormwater pipe is cast from the EXACT same density concrete, "
        f"what will be the mass of the real pipe, in kilograms (kg)?"
    )

    correct_ans = f"{_fmt(real_mass_kg, 1)} kg"
    custom_opts = [
        correct_ans,
        f"{_fmt((model_mass_g * scale) / 1000.0, 1)} kg",
        f"{_fmt((model_mass_g * (scale ** 2)) / 1000.0, 1)} kg",
        f"{_fmt(real_mass_kg * 2, 1)} kg",
    ]

    t1 = "Because mass = volume × density and both use identical concrete, mass scales proportionally with volume (k³)."
    t2 = f"Multiply the model mass in grams by {scale}³, then divide by 1 000 to convert to kilograms."
    t3 = f"Real mass (g) = {_fmt(model_mass_g, 0)} × {scale}³ = {_fmt(real_mass_g, 0)} g. In kg = {_fmt(real_mass_g, 0)} ÷ 1 000 = {_fmt(real_mass_kg, 1)} kg."

    explanation = [
        f"Step 1: Identify that mass scales with volume (Linear scale factor)³: {scale}³ = {scale**3} [1 Mark: Method].",
        f"Step 2: Real mass in grams = {_fmt(model_mass_g, 0)} g × {scale**3} = {_fmt(real_mass_g, 0)} g [1 Mark: Method].",
        f"Step 3: Convert grams to kg: {_fmt(real_mass_g, 0)} ÷ 1 000 = {_fmt(real_mass_kg, 1)} kg [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_29",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )


def gen_subskill_30(r: random.Random) -> Dict[str, Any]:
    """Subskill 30: Scale factor distortion: identifying linear scaling misconception on area."""
    scale = r.choice([50, 100, 200])
    model_area_cm2 = r.choice([40.0, 50.0, 60.0, 75.0])
    linear_factor = scale
    area_factor = scale ** 2
    true_area_m2 = (model_area_cm2 * area_factor) / 10000.0
    erroneous_area_m2 = (model_area_cm2 * linear_factor) / 10000.0

    d_spec_30 = {
        "diagram_role": "context",
        "kind": "floor_plan",
        "title": f"Hall Model Floor Area ({_fmt(model_area_cm2, 0)} cm² at 1 : {scale})",
        "rooms": [{"name": "Hall", "area_cm2": model_area_cm2, "scale": f"1:{scale}"}],
        "dimensions": {"model_area_cm2": model_area_cm2, "scale": scale},
    }

    prompt = (
        f"Refer to the accompanying floor plan layout shown in the diagram (scale 1 : {scale}).\n"
        f"A student calculates the real floor area of a hall from the model where the model floor area measures {_fmt(model_area_cm2, 0)} cm².\n"
        f"The student calculates:\n"
        f"  Real Area = {_fmt(model_area_cm2, 0)} cm² × {scale} = {_fmt(model_area_cm2 * scale, 0)} cm² = {_fmt(erroneous_area_m2, 2)} m².\n\n"
        f"What critical mathematical error did the student commit, and what is the true area?"
    )

    correct_ans = f"The student multiplied by the linear factor ({scale}) instead of the area factor ({scale}² = {area_factor:,}); true area is {_fmt(true_area_m2, 1)} m²."
    custom_opts = [
        correct_ans,
        f"The student forgot to convert cm² to m²; true area is {_fmt(erroneous_area_m2, 2)} m².",
        f"The student divided instead of multiplying; true area is {_fmt(model_area_cm2 / scale, 4)} m².",
        f"The student used the wrong scale; true area is {_fmt(true_area_m2 * 2, 1)} m².",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    explanation = (
        f"1. A linear scale of 1 : {scale} means distances scale by {scale}.\n"
        f"2. Area scales by the square of the scale factor: {scale}² = {area_factor:,}.\n"
        f"3. Real area = {_fmt(model_area_cm2, 0)} cm² × {area_factor:,} = {_fmt(model_area_cm2 * area_factor, 0)} cm² = {_fmt(true_area_m2, 1)} m²."
    )
    t1 = f"Identify that area scales by {scale}², not {scale}."
    t2 = f"Multiply {_fmt(model_area_cm2, 0)} cm² by {scale}² = {area_factor:,}."
    t3 = f"Convert cm² to m²: divide by 10 000 to get {_fmt(true_area_m2, 1)} m²."

    return _build_question_payload(
        "gr12_models_subskill_30",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="hard",
        diagram_spec=d_spec_30,
    )


def gen_subskill_31(r: random.Random) -> Dict[str, Any]:
    """Subskill 31: Acoustic scale model frequency/wavelength relationship."""
    scale = r.choice([10, 20, 50])
    test_freq_hz = 1000  # Real sound frequency 1 000 Hz
    # In scale acoustics, to model wavelength (lambda = c/f), wavelength reduces by scale,
    # so testing frequency must be multiplied by scale: f_model = f_real * scale
    model_freq_hz = test_freq_hz * scale

    d_spec_31 = {
        "diagram_role": "context",
        "kind": "line_graph",
        "title": f"Acoustic Frequency Response (1 : {scale})",
        "series": [{"name": "Acoustic Freq", "points": [[0, 1000], [1, model_freq_hz]]}],
        "x_label": "Domain",
        "y_label": "Frequency (Hz)",
    }

    prompt = (
        f"In architectural acoustic testing, an auditor's hall is modeled at a scale of 1 : {scale} to analyze reverberation.\n"
        f"Because acoustic sound waves must be reduced by the scale factor {scale} to match the model's physical dimensions, "
        f"the acoustic testing frequency must be increased proportionally: Frequency_model = Frequency_real × Scale.\n\n"
        f"If the speech frequency to be tested in the real hall is 1 000 Hz, what sound frequency must be broadcast in the 1 : {scale} model?"
    )

    correct_ans = f"{_fmt(model_freq_hz, 0)} Hz"
    custom_opts = [
        correct_ans,
        f"{_fmt(test_freq_hz / scale, 1)} Hz",
        f"{_fmt(test_freq_hz, 0)} Hz",
        f"{_fmt(model_freq_hz * 2, 0)} Hz",
    ]

    t1 = "Apply the formula provided: Frequency_model = Frequency_real × Scale."
    t2 = f"Substitute: 1 000 Hz × {scale}."
    t3 = f"Model frequency = 1 000 × {scale} = {_fmt(model_freq_hz, 0)} Hz."

    explanation = [
        f"Step 1: Identify frequency formula: Frequency_model = Frequency_real × Scale [1 Mark: Method].",
        f"Step 2: Substitute: 1 000 Hz × {scale} [1 Mark: Method].",
        f"Step 3: Scaled test frequency = {_fmt(model_freq_hz, 0)} Hz [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_31",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="easy",
        diagram_spec=d_spec_31,
    )


def gen_subskill_32(r: random.Random) -> Dict[str, Any]:
    """Subskill 32: Wind tunnel model frontal area ratio calculation."""
    scale = r.choice([10, 15, 20])
    real_frontal_area_m2 = r.choice([2.4, 2.8, 3.2, 4.0])
    # Model frontal area in cm² = (real_frontal_area_m2 * 10 000) / (scale^2)
    model_frontal_cm2 = (real_frontal_area_m2 * 10000.0) / (scale ** 2)

    prompt = (
        f"Automotive engineers test an aerodynamic clay model of a minibus taxi in a wind tunnel at a scale of 1 : {scale}.\n"
        f"The full-sized minibus taxi has a frontal cross-sectional area of {_fmt(real_frontal_area_m2, 2)} m².\n\n"
        f"Calculate the frontal cross-sectional area of the scale model in square centimetres (cm²)."
    )

    correct_ans = f"{_fmt(model_frontal_cm2, 1)} cm²"
    custom_opts = [
        correct_ans,
        f"{_fmt((real_frontal_area_m2 * 10000.0) / scale, 1)} cm²",
        f"{_fmt(model_frontal_cm2 * 2, 1)} cm²",
        f"{_fmt(model_frontal_cm2 / 2, 1)} cm²",
    ]

    t1 = "Convert the real frontal area to cm² by multiplying by 10 000."
    t2 = f"Divide by the area scale factor ({scale}²)."
    t3 = f"Real cm² = {_fmt(real_frontal_area_m2, 2)} × 10 000 = {_fmt(real_frontal_area_m2 * 10000, 0)} cm². Model area = {_fmt(real_frontal_area_m2 * 10000, 0)} ÷ {scale**2} = {_fmt(model_frontal_cm2, 1)} cm²."

    explanation = [
        f"Step 1: Convert real area to cm²: {_fmt(real_frontal_area_m2, 2)} m² × 10 000 = {_fmt(real_frontal_area_m2 * 10000, 0)} cm² [1 Mark: Method].",
        f"Step 2: Area scale factor = {scale}² = {scale**2} [1 Mark: Method].",
        f"Step 3: Model frontal area = {_fmt(real_frontal_area_m2 * 10000, 0)} ÷ {scale**2} = {_fmt(model_frontal_cm2, 1)} cm² [1 Mark: Accuracy].",
    ]

    opts, _ = _build_options(correct_ans, r, custom_options=custom_opts)
    return _build_question_payload(
        "gr12_models_subskill_32",
        prompt,
        correct_ans,
        opts,
        explanation,
        t1,
        t2,
        t3,
        r,
        difficulty="medium",
    )
