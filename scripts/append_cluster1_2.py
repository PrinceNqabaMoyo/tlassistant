# -*- coding: utf-8 -*-
"""Appends Cluster 1 & Cluster 2 to conversions_time_generator.py."""

from pathlib import Path

target = Path("caps-ai-backend/app/utils/mathematical_literacy/conversions_time_generator.py")

content = '''
# ==============================================================================
# CLUSTER 1: METRIC LENGTH CONVERSIONS (8 Archetypes)
# ==============================================================================

def _gen_conv_len_mm_to_cm(r: random.Random) -> Dict[str, Any]:
    val_mm = r.randint(15, 950)
    ans_cm = val_mm / 10.0
    name = r.choice(SA_NAMES)
    items = ["wire segment", "ribbon", "pencil", "tile spacer", "pipe fitting"]
    item = r.choice(items)
    prompt = f"{name} measured the length of a {item} to be **{val_mm} mm**.\\n\\nConvert this measurement to centimetres (**cm**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from a smaller unit (millimetres, mm) to a larger unit (centimetres, cm) requires **division**.\\n"
        f"• Base relationship: $1\\\\text{{ cm}} = 10\\\\text{{ mm}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Length in cm}} = \\\\frac{{{val_mm}\\\\text{{ mm}}}}{{10}} = {_fmt(ans_cm)}\\\\text{{ cm}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 10]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ans_cm)}\\\\text{{ cm}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct numerical value and unit]**"
    )
    return _make_q(
        subskill="conv_len_mm_to_cm",
        prompt=prompt,
        answer=f"{_fmt(ans_cm)} cm",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 10", f"1 Mark: Accuracy – {_fmt(ans_cm)} cm"],
        hints={
            "tier_1": "There are 10 millimetres in 1 centimetre. Converting from smaller to larger unit requires division.",
            "tier_2": f"Divide {val_mm} by 10.",
            "tier_3": f"{val_mm} ÷ 10 = {_fmt(ans_cm)} cm."
        },
        r=r
    )

def _gen_conv_len_cm_to_mm(r: random.Random) -> Dict[str, Any]:
    val_cm = r.randint(5, 120)
    ans_mm = val_cm * 10
    name = r.choice(SA_NAMES)
    prompt = f"{name} is cutting timber for woodwork. A plank measures **{val_cm} cm** in width.\\n\\nConvert this measurement to millimetres (**mm**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from a larger unit (centimetres, cm) to a smaller unit (millimetres, mm) requires **multiplication**.\\n"
        f"• Base relationship: $1\\\\text{{ cm}} = 10\\\\text{{ mm}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Width in mm}} = {val_cm}\\\\text{{ cm}} \\\\times 10 = {ans_mm}\\\\text{{ mm}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 10]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_mm}\\\\text{{ mm}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct numerical value and unit]**"
    )
    return _make_q(
        subskill="conv_len_cm_to_mm",
        prompt=prompt,
        answer=f"{ans_mm} mm",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 10", f"1 Mark: Accuracy – {ans_mm} mm"],
        hints={
            "tier_1": "1 centimetre equals 10 millimetres. Moving to a smaller unit means multiplying.",
            "tier_2": f"Multiply {val_cm} by 10.",
            "tier_3": f"{val_cm} × 10 = {ans_mm} mm."
        },
        r=r
    )

def _gen_conv_len_cm_to_m(r: random.Random) -> Dict[str, Any]:
    val_cm = r.randint(25, 950)
    ans_m = val_cm / 100.0
    name = r.choice(SA_NAMES)
    prompt = f"{name} measured the height of a garden gate to be **{val_cm} cm**.\\n\\nConvert this height to metres (**m**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from centimetres (cm) to metres (m) moves from smaller to larger units, requiring **division**.\\n"
        f"• Base relationship: $1\\\\text{{ m}} = 100\\\\text{{ cm}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Height in m}} = \\\\frac{{{val_cm}\\\\text{{ cm}}}}{{100}} = {_fmt(ans_m)}\\\\text{{ m}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 100]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ans_m)}\\\\text{{ m}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_len_cm_to_m",
        prompt=prompt,
        answer=f"{_fmt(ans_m)} m",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 100", f"1 Mark: Accuracy – {_fmt(ans_m)} m"],
        hints={
            "tier_1": "There are 100 centimetres in 1 metre. Divide by 100.",
            "tier_2": f"Divide {val_cm} by 100.",
            "tier_3": f"{val_cm} ÷ 100 = {_fmt(ans_m)} m."
        },
        r=r
    )

def _gen_conv_len_m_to_cm(r: random.Random) -> Dict[str, Any]:
    val_m = round(r.uniform(1.2, 14.5), 2)
    ans_cm = int(round(val_m * 100))
    prompt = f"A roll of curtain fabric is **{_fmt(val_m)} m** long.\\n\\nConvert the length of the fabric to centimetres (**cm**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from metres (m) to centimetres (cm) moves from larger to smaller units, requiring **multiplication**.\\n"
        f"• Base relationship: $1\\\\text{{ m}} = 100\\\\text{{ cm}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Length in cm}} = {_fmt(val_m)}\\\\text{{ m}} \\\\times 100 = {ans_cm}\\\\text{{ cm}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 100]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_cm}\\\\text{{ cm}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_len_m_to_cm",
        prompt=prompt,
        answer=f"{ans_cm} cm",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 100", f"1 Mark: Accuracy – {ans_cm} cm"],
        hints={
            "tier_1": "1 metre = 100 centimetres. Multiply by 100.",
            "tier_2": f"Multiply {_fmt(val_m)} by 100.",
            "tier_3": f"{_fmt(val_m)} × 100 = {ans_cm} cm."
        },
        r=r
    )

def _gen_conv_len_mm_to_m(r: random.Random) -> Dict[str, Any]:
    val_mm = r.randint(350, 7500)
    ans_m = val_mm / 1000.0
    name = r.choice(SA_NAMES)
    prompt = f"An engineering blueprint indicates that a steel drainage pipe has a length of **{val_mm} mm**.\\n\\nConvert this pipe length to metres (**m**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from millimetres (mm) to metres (m) requires **division** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ m}} = 1\\\\ 000\\\\text{{ mm}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Length in m}} = \\\\frac{{{val_mm}\\\\text{{ mm}}}}{{1\\\\ 000}} = {_fmt(ans_m)}\\\\text{{ m}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ans_m)}\\\\text{{ m}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_len_mm_to_m",
        prompt=prompt,
        answer=f"{_fmt(ans_m)} m",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 1 000", f"1 Mark: Accuracy – {_fmt(ans_m)} m"],
        hints={
            "tier_1": "There are 1 000 millimetres in 1 metre. Divide by 1 000.",
            "tier_2": f"Divide {val_mm} by 1 000.",
            "tier_3": f"{val_mm} ÷ 1 000 = {_fmt(ans_m)} m."
        },
        r=r
    )

def _gen_conv_len_m_to_mm(r: random.Random) -> Dict[str, Any]:
    val_m = round(r.uniform(0.6, 8.5), 2)
    ans_mm = int(round(val_m * 1000))
    prompt = f"A builder marks off a distance of **{_fmt(val_m)} m** on a foundation trench.\\n\\nConvert this distance to millimetres (**mm**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from metres (m) to millimetres (mm) requires **multiplication** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ m}} = 1\\\\ 000\\\\text{{ mm}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Distance in mm}} = {_fmt(val_m)}\\\\text{{ m}} \\\\times 1\\\\ 000 = {ans_mm}\\\\text{{ mm}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_mm}\\\\text{{ mm}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_len_m_to_mm",
        prompt=prompt,
        answer=f"{ans_mm} mm",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 1 000", f"1 Mark: Accuracy – {ans_mm} mm"],
        hints={
            "tier_1": "1 metre = 1 000 millimetres. Multiply by 1 000.",
            "tier_2": f"Multiply {_fmt(val_m)} by 1 000.",
            "tier_3": f"{_fmt(val_m)} × 1 000 = {ans_mm} mm."
        },
        r=r
    )

def _gen_conv_len_m_to_km(r: random.Random) -> Dict[str, Any]:
    val_m = r.randint(450, 18500)
    ans_km = val_m / 1000.0
    prompt = f"A fun run route in Polokwane is measured at **{val_m} m**.\\n\\nConvert this distance to kilometres (**km**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from metres (m) to kilometres (km) moves to a larger unit, requiring **division** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ km}} = 1\\\\ 000\\\\text{{ m}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Distance in km}} = \\\\frac{{{val_m}\\\\text{{ m}}}}{{1\\\\ 000}} = {_fmt(ans_km)}\\\\text{{ km}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ans_km)}\\\\text{{ km}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_len_m_to_km",
        prompt=prompt,
        answer=f"{_fmt(ans_km)} km",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 1 000", f"1 Mark: Accuracy – {_fmt(ans_km)} km"],
        hints={
            "tier_1": "There are 1 000 metres in 1 kilometre. Divide by 1 000.",
            "tier_2": f"Divide {val_m} by 1 000.",
            "tier_3": f"{val_m} ÷ 1 000 = {_fmt(ans_km)} km."
        },
        r=r
    )

def _gen_conv_len_km_to_m(r: random.Random) -> Dict[str, Any]:
    val_km = round(r.uniform(1.5, 42.5), 2)
    ans_m = int(round(val_km * 1000))
    prompt = f"The road distance between two toll gates on the N3 highway is **{_fmt(val_km)} km**.\\n\\nConvert this road distance to metres (**m**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from kilometres (km) to metres (m) moves to a smaller unit, requiring **multiplication** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ km}} = 1\\\\ 000\\\\text{{ m}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Distance in m}} = {_fmt(val_km)}\\\\text{{ km}} \\\\times 1\\\\ 000 = {ans_m}\\\\text{{ m}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_m}\\\\text{{ m}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_len_km_to_m",
        prompt=prompt,
        answer=f"{ans_m} m",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 1 000", f"1 Mark: Accuracy – {ans_m} m"],
        hints={
            "tier_1": "1 kilometre = 1 000 metres. Multiply by 1 000.",
            "tier_2": f"Multiply {_fmt(val_km)} by 1 000.",
            "tier_3": f"{_fmt(val_km)} × 1 000 = {ans_m} m."
        },
        r=r
    )


# ==============================================================================
# CLUSTER 2: METRIC MASS CONVERSIONS (7 Archetypes)
# ==============================================================================

def _gen_conv_mass_g_to_kg(r: random.Random) -> Dict[str, Any]:
    val_g = r.randint(250, 4800)
    ans_kg = val_g / 1000.0
    prompt = f"A packet of biltong weighs **{val_g} g** at a butchery.\\n\\nConvert this mass to kilograms (**kg**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from grams (g) to kilograms (kg) moves to a larger unit, requiring **division** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ kg}} = 1\\\\ 000\\\\text{{ g}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Mass in kg}} = \\\\frac{{{val_g}\\\\text{{ g}}}}{{1\\\\ 000}} = {_fmt(ans_kg)}\\\\text{{ kg}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ans_kg)}\\\\text{{ kg}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_mass_g_to_kg",
        prompt=prompt,
        answer=f"{_fmt(ans_kg)} kg",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 1 000", f"1 Mark: Accuracy – {_fmt(ans_kg)} kg"],
        hints={
            "tier_1": "There are 1 000 grams in 1 kilogram. Divide by 1 000.",
            "tier_2": f"Divide {val_g} by 1 000.",
            "tier_3": f"{val_g} ÷ 1 000 = {_fmt(ans_kg)} kg."
        },
        r=r
    )

def _gen_conv_mass_kg_to_g(r: random.Random) -> Dict[str, Any]:
    val_kg = round(r.uniform(0.75, 12.5), 2)
    ans_g = int(round(val_kg * 1000))
    prompt = f"A baker buys a bag of cake flour weighing **{_fmt(val_kg)} kg**.\\n\\nConvert this mass to grams (**g**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from kilograms (kg) to grams (g) moves to a smaller unit, requiring **multiplication** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ kg}} = 1\\\\ 000\\\\text{{ g}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Mass in g}} = {_fmt(val_kg)}\\\\text{{ kg}} \\\\times 1\\\\ 000 = {ans_g}\\\\text{{ g}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_g}\\\\text{{ g}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_mass_kg_to_g",
        prompt=prompt,
        answer=f"{ans_g} g",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 1 000", f"1 Mark: Accuracy – {ans_g} g"],
        hints={
            "tier_1": "1 kilogram = 1 000 grams. Multiply by 1 000.",
            "tier_2": f"Multiply {_fmt(val_kg)} by 1 000.",
            "tier_3": f"{_fmt(val_kg)} × 1 000 = {ans_g} g."
        },
        r=r
    )

def _gen_conv_mass_kg_to_tonne(r: random.Random) -> Dict[str, Any]:
    val_kg = r.randint(450, 8500)
    ans_t = val_kg / 1000.0
    prompt = f"A delivery truck carries bags of cement with a combined mass of **{val_kg} kg**.\\n\\nConvert this cement payload to tonnes (**t**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from kilograms (kg) to metric tonnes (t) moves to a larger unit, requiring **division** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ tonne}} = 1\\\\ 000\\\\text{{ kg}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Mass in tonnes}} = \\\\frac{{{val_kg}\\\\text{{ kg}}}}{{1\\\\ 000}} = {_fmt(ans_t)}\\\\text{{ t}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ans_t)}\\\\text{{ t}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_mass_kg_to_tonne",
        prompt=prompt,
        answer=f"{_fmt(ans_t)} t",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 1 000", f"1 Mark: Accuracy – {_fmt(ans_t)} t"],
        hints={
            "tier_1": "There are 1 000 kilograms in 1 metric tonne. Divide by 1 000.",
            "tier_2": f"Divide {val_kg} by 1 000.",
            "tier_3": f"{val_kg} ÷ 1 000 = {_fmt(ans_t)} t."
        },
        r=r
    )

def _gen_conv_mass_tonne_to_kg(r: random.Random) -> Dict[str, Any]:
    val_t = round(r.uniform(1.2, 18.5), 2)
    ans_kg = int(round(val_t * 1000))
    prompt = f"A shipping container has a registered freight mass of **{_fmt(val_t)} t**.\\n\\nConvert this freight mass to kilograms (**kg**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from tonnes (t) to kilograms (kg) moves to a smaller unit, requiring **multiplication** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ tonne}} = 1\\\\ 000\\\\text{{ kg}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Mass in kg}} = {_fmt(val_t)}\\\\text{{ t}} \\\\times 1\\\\ 000 = {ans_kg}\\\\text{{ kg}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_kg}\\\\text{{ kg}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_mass_tonne_to_kg",
        prompt=prompt,
        answer=f"{ans_kg} kg",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 1 000", f"1 Mark: Accuracy – {ans_kg} kg"],
        hints={
            "tier_1": "1 metric tonne = 1 000 kilograms. Multiply by 1 000.",
            "tier_2": f"Multiply {_fmt(val_t)} by 1 000.",
            "tier_3": f"{_fmt(val_t)} × 1 000 = {ans_kg} kg."
        },
        r=r
    )

def _gen_conv_mass_mg_to_g(r: random.Random) -> Dict[str, Any]:
    val_mg = r.randint(150, 4500)
    ans_g = val_mg / 1000.0
    prompt = f"A pharmacist measures **{val_mg} mg** of an active ingredient for a cough mixture.\\n\\nConvert this active ingredient to grams (**g**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from milligrams (mg) to grams (g) moves to a larger unit, requiring **division** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ g}} = 1\\\\ 000\\\\text{{ mg}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Mass in g}} = \\\\frac{{{val_mg}\\\\text{{ mg}}}}{{1\\\\ 000}} = {_fmt(ans_g)}\\\\text{{ g}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ans_g)}\\\\text{{ g}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_mass_mg_to_g",
        prompt=prompt,
        answer=f"{_fmt(ans_g)} g",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 1 000", f"1 Mark: Accuracy – {_fmt(ans_g)} g"],
        hints={
            "tier_1": "There are 1 000 milligrams in 1 gram. Divide by 1 000.",
            "tier_2": f"Divide {val_mg} by 1 000.",
            "tier_3": f"{val_mg} ÷ 1 000 = {_fmt(ans_g)} g."
        },
        r=r
    )

def _gen_conv_mass_g_to_mg(r: random.Random) -> Dict[str, Any]:
    val_g = round(r.uniform(0.25, 4.5), 2)
    ans_mg = int(round(val_g * 1000))
    prompt = f"A laboratory technician dispenses **{_fmt(val_g)} g** of a chemical reagent.\\n\\nConvert this reagent mass to milligrams (**mg**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from grams (g) to milligrams (mg) moves to a smaller unit, requiring **multiplication** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ g}} = 1\\\\ 000\\\\text{{ mg}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Mass in mg}} = {_fmt(val_g)}\\\\text{{ g}} \\\\times 1\\\\ 000 = {ans_mg}\\\\text{{ mg}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_mg}\\\\text{{ mg}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_mass_g_to_mg",
        prompt=prompt,
        answer=f"{ans_mg} mg",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 1 000", f"1 Mark: Accuracy – {ans_mg} mg"],
        hints={
            "tier_1": "1 gram = 1 000 milligrams. Multiply by 1 000.",
            "tier_2": f"Multiply {_fmt(val_g)} by 1 000.",
            "tier_3": f"{_fmt(val_g)} × 1 000 = {ans_mg} mg."
        },
        r=r
    )

def _gen_conv_mass_multi_step_tonne_to_g(r: random.Random) -> Dict[str, Any]:
    val_t = round(r.uniform(0.005, 0.085), 3)
    ans_kg = round(val_t * 1000, 2)
    ans_g = int(round(val_t * 1000000))
    prompt = f"A commercial spice packaging facility receives a mini-bulk bag containing **{_fmt(val_t)} t** of ground paprika.\\n\\nCalculate the mass of paprika in grams (**g**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Multi-step conversion from tonnes (t) to grams (g):\\n"
        f"  1. Convert tonnes to kilograms ($1\\\\text{{ t}} = 1\\\\ 000\\\\text{{ kg}}$)\\n"
        f"  2. Convert kilograms to grams ($1\\\\text{{ kg}} = 1\\\\ 000\\\\text{{ g}}$)\\n"
        f"• Combined conversion factor: $1\\\\text{{ t}} = 1\\\\ 000 \\\\times 1\\\\ 000 = 1\\\\ 000\\\\ 000\\\\text{{ g}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Mass in kg}} = {_fmt(val_t)}\\\\text{{ t}} \\\\times 1\\\\ 000 = {_fmt(ans_kg)}\\\\text{{ kg}}$$\\n"
        f"$$\\\\text{{Mass in g}} = {_fmt(ans_kg)}\\\\text{{ kg}} \\\\times 1\\\\ 000 = {ans_g}\\\\text{{ g}}$$\\n"
        f"✓ **[1 Mark: Method – converting tonnes to kilograms]**\\n"
        f"✓ **[1 Mark: Method – converting kilograms to grams]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_g}\\\\text{{ g}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – final mass in grams]**"
    )
    return _make_q(
        subskill="conv_mass_multi_step_tonne_to_g",
        prompt=prompt,
        answer=f"{ans_g} g",
        sol=sol,
        rubric=[
            f"1 Mark: Method – {_fmt(val_t)} t × 1 000 = {_fmt(ans_kg)} kg",
            f"1 Mark: Method – {_fmt(ans_kg)} kg × 1 000",
            f"1 Mark: Accuracy – {ans_g} g"
        ],
        hints={
            "tier_1": "1 tonne = 1 000 kg, and 1 kg = 1 000 g. Therefore, 1 tonne = 1 000 000 g.",
            "tier_2": f"Multiply {_fmt(val_t)} by 1 000 to get kg, then multiply by 1 000 to get grams.",
            "tier_3": f"{_fmt(val_t)} × 1 000 000 = {ans_g} g."
        },
        total_marks=3,
        r=r
    )
'''

with open(target, "a", encoding="utf-8") as f:
    f.write(content)

print("Cluster 1 & 2 appended successfully.")
