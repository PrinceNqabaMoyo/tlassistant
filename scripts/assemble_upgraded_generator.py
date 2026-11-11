# Python script to assemble the complete upgraded conversions_time_generator.py

with open('scripts/build_full_conversions_file.py', 'r', encoding='utf-8') as f:
    base_code = f.read()

# Add Clusters 2 through 7 and generator registry dispatcher
clusters_code = '''
# ===========================================================================
# CLUSTER 2: METRIC MASS CONVERSIONS (7 Archetypes)
# ===========================================================================

def _gen_conv_mass_g_to_kg(r: random.Random) -> Dict[str, Any]:
    val_g = r.randint(250, 8500)
    ans_kg = val_g / 1000.0
    items = ["bag of brown sugar", "butchery beef mince", "pumpkin", "cabbage", "bag of oranges"]
    item = r.choice(items)
    prompt = f"A grocery store customer places a {item} on the scale, measuring **{val_g} g**.\n\nConvert this mass to kilograms (**kg**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ kg}} = 1\\\\,000\\\\text{{ g}}$\\n"
        f"• Converting from grams (smaller unit) to kilograms (larger unit) requires **division** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Mass in kg}} = \\\\frac{{{val_g}\\\\text{{ g}}}}{{1\\\\,000}} = \\\\mathbf{{{_fmt(ans_kg)}\\\\text{{ kg}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_kg)}\\\\text{{ kg}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_mass_g_to_kg",
        prompt=prompt,
        answer=f"{_fmt(ans_kg)} kg",
        sol=sol,
        rubric=[f"Method: {val_g} ÷ 1000 [1 Mark]", f"Accuracy: {_fmt(ans_kg)} kg [1 Mark]"],
        hints={
            "tier_1": "There are 1 000 grams in 1 kilogram (1 kg = 1 000 g).",
            "tier_2": f"Divide {val_g} by 1 000.",
            "tier_3": f"{val_g} ÷ 1 000 = {_fmt(ans_kg)} kg."
        }
    )

def _gen_conv_mass_kg_to_g(r: random.Random) -> Dict[str, Any]:
    val_kg = round(r.uniform(0.45, 12.5), 2)
    ans_g = round(val_kg * 1000, 1)
    prompt = f"A recipe for feeding a school sports camp requires **{_fmt(val_kg)} kg** of samp and beans.\n\nConvert this mass to grams (**g**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ kg}} = 1\\\\,000\\\\text{{ g}}$\\n"
        f"• Converting from kilograms to grams requires **multiplication** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Mass in g}} = {_fmt(val_kg)}\\\\text{{ kg}} \\\\times 1\\\\,000 = \\\\mathbf{{{_fmt(ans_g)}\\\\text{{ g}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_g)}\\\\text{{ g}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_mass_kg_to_g",
        prompt=prompt,
        answer=f"{_fmt(ans_g)} g",
        sol=sol,
        rubric=[f"Method: {_fmt(val_kg)} × 1000 [1 Mark]", f"Accuracy: {_fmt(ans_g)} g [1 Mark]"],
        hints={
            "tier_1": "1 kilogram = 1 000 grams.",
            "tier_2": f"Multiply {_fmt(val_kg)} by 1 000.",
            "tier_3": f"{_fmt(val_kg)} × 1 000 = {_fmt(ans_g)} g."
        }
    )

def _gen_conv_mass_kg_to_tonne(r: random.Random) -> Dict[str, Any]:
    val_kg = r.randint(1200, 48000)
    ans_t = val_kg / 1000.0
    prompt = f"A commercial delivery truck carrying maize meal is weighed at a weighbridge at **{val_kg} kg**.\n\nConvert this load mass to metric tonnes (**t**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ tonne (t)}} = 1\\\\,000\\\\text{{ kg}}$\\n"
        f"• Converting from kilograms to metric tonnes requires **division** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Mass in tonnes}} = \\\\frac{{{val_kg}\\\\text{{ kg}}}}{{1\\\\,000}} = \\\\mathbf{{{_fmt(ans_t)}\\\\text{{ t}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_t)}\\\\text{{ t}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_mass_kg_to_tonne",
        prompt=prompt,
        answer=f"{_fmt(ans_t)} t",
        sol=sol,
        rubric=[f"Method: {val_kg} ÷ 1000 [1 Mark]", f"Accuracy: {_fmt(ans_t)} t [1 Mark]"],
        hints={
            "tier_1": "1 metric tonne (t) = 1 000 kilograms (kg).",
            "tier_2": f"Divide {val_kg} by 1 000.",
            "tier_3": f"{val_kg} ÷ 1 000 = {_fmt(ans_t)} t."
        }
    )

def _gen_conv_mass_tonne_to_kg(r: random.Random) -> Dict[str, Any]:
    val_t = round(r.uniform(1.5, 32.0), 2)
    ans_kg = round(val_t * 1000, 1)
    prompt = f"A scrap metal dealership purchases an industrial shipment of scrap iron weighing **{_fmt(val_t)} tonnes**.\n\nConvert this mass to kilograms (**kg**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ tonne}} = 1\\\\,000\\\\text{{ kg}}$\\n"
        f"• Converting from tonnes to kilograms requires **multiplication** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Mass in kg}} = {_fmt(val_t)}\\\\text{{ t}} \\\\times 1\\\\,000 = \\\\mathbf{{{_fmt(ans_kg)}\\\\text{{ kg}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_kg)}\\\\text{{ kg}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_mass_tonne_to_kg",
        prompt=prompt,
        answer=f"{_fmt(ans_kg)} kg",
        sol=sol,
        rubric=[f"Method: {_fmt(val_t)} × 1000 [1 Mark]", f"Accuracy: {_fmt(ans_kg)} kg [1 Mark]"],
        hints={
            "tier_1": "1 metric tonne = 1 000 kilograms.",
            "tier_2": f"Multiply {_fmt(val_t)} by 1 000.",
            "tier_3": f"{_fmt(val_t)} × 1 000 = {_fmt(ans_kg)} kg."
        }
    )

def _gen_conv_mass_mg_to_g(r: random.Random) -> Dict[str, Any]:
    val_mg = r.randint(250, 4500)
    ans_g = val_mg / 1000.0
    prompt = f"A medical capsule contains **{val_mg} mg** of active vitamin C supplement.\n\nConvert this mass to grams (**g**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ g}} = 1\\\\,000\\\\text{{ mg}}$\\n"
        f"• Converting from milligrams to grams requires **division** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Mass in g}} = \\\\frac{{{val_mg}\\\\text{{ mg}}}}{{1\\\\,000}} = \\\\mathbf{{{_fmt(ans_g)}\\\\text{{ g}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_g)}\\\\text{{ g}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_mass_mg_to_g",
        prompt=prompt,
        answer=f"{_fmt(ans_g)} g",
        sol=sol,
        rubric=[f"Method: {val_mg} ÷ 1000 [1 Mark]", f"Accuracy: {_fmt(ans_g)} g [1 Mark]"],
        hints={
            "tier_1": "There are 1 000 milligrams in 1 gram (1 g = 1 000 mg).",
            "tier_2": f"Divide {val_mg} by 1 000.",
            "tier_3": f"{val_mg} ÷ 1 000 = {_fmt(ans_g)} g."
        }
    )

def _gen_conv_mass_g_to_mg(r: random.Random) -> Dict[str, Any]:
    val_g = round(r.uniform(0.25, 4.5), 2)
    ans_mg = round(val_g * 1000, 1)
    prompt = f"A pharmacist measures **{_fmt(val_g)} g** of potassium sorbate preservative.\n\nConvert this mass to milligrams (**mg**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ g}} = 1\\\\,000\\\\text{{ mg}}$\\n"
        f"• Converting from grams to milligrams requires **multiplication** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Mass in mg}} = {_fmt(val_g)}\\\\text{{ g}} \\\\times 1\\\\,000 = \\\\mathbf{{{_fmt(ans_mg)}\\\\text{{ mg}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_mg)}\\\\text{{ mg}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_mass_g_to_mg",
        prompt=prompt,
        answer=f"{_fmt(ans_mg)} mg",
        sol=sol,
        rubric=[f"Method: {_fmt(val_g)} × 1000 [1 Mark]", f"Accuracy: {_fmt(ans_mg)} mg [1 Mark]"],
        hints={
            "tier_1": "1 gram = 1 000 milligrams.",
            "tier_2": f"Multiply {_fmt(val_g)} by 1 000.",
            "tier_3": f"{_fmt(val_g)} × 1 000 = {_fmt(ans_mg)} mg."
        }
    )

def _gen_conv_mass_multi_step_tonne_to_g(r: random.Random) -> Dict[str, Any]:
    val_t = round(r.uniform(0.02, 0.45), 3)
    ans_g = round(val_t * 1000000, 1)
    prompt = f"A specialist gold jewelry workshop receives an allocation of **{_fmt(val_t)} tonnes** of copper alloy.\n\nConvert this mass directly to grams (**g**)."
    sol = (
        f"**Step 1: Multi-Step Conversion Breakdown**\\n"
        f"• First convert tonnes to kilograms: $1\\\\text{{ t}} = 1\\\\,000\\\\text{{ kg}}$\\n"
        f"• Then convert kilograms to grams: $1\\\\text{{ kg}} = 1\\\\,000\\\\text{{ g}}$\\n"
        f"• Overall factor: $1\\\\text{{ t}} = 1\\\\,000 \\\\times 1\\\\,000 = 1\\\\,000\\\\,000\\\\text{{ g}}$\\n\\n"
        f"**Step 2: Method & Calculations**\\n"
        f"$$\\\\text{{Mass in kg}} = {_fmt(val_t)} \\\\times 1\\\\,000 = {_fmt(val_t * 1000)}\\\\text{{ kg}}$$\\n"
        f"✓ [1 Mark: Method – converting tonnes to kilograms]\\n"
        f"$$\\\\text{{Mass in g}} = {_fmt(val_t * 1000)} \\\\times 1\\\\,000 = \\\\mathbf{{{_fmt(ans_g)}\\\\text{{ g}}}}$$\\n"
        f"✓ [1 Mark: Method – converting kilograms to grams]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_g)}\\\\text{{ g}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted mass with units]\\n\\n"
        f"**Total Marks: [3 Marks]**"
    )
    return _make_q(
        subskill="conv_mass_multi_step_tonne_to_g",
        prompt=prompt,
        answer=f"{_fmt(ans_g)} g",
        sol=sol,
        rubric=[f"Tonnes to kg: {_fmt(val_t)} × 1000 [1 Mark]", f"Kg to g: × 1000 [1 Mark]", f"Accuracy: {_fmt(ans_g)} g [1 Mark]"],
        marks=3,
        hints={
            "tier_1": "1 tonne = 1 000 kg, and 1 kg = 1 000 g.",
            "tier_2": f"Multiply {_fmt(val_t)} by 1 000 000 (or by 1 000 twice).",
            "tier_3": f"{_fmt(val_t)} × 1 000 000 = {_fmt(ans_g)} g."
        }
    )


# ===========================================================================
# CLUSTER 3: METRIC VOLUME & CAPACITY (7 Archetypes)
# ===========================================================================

def _gen_conv_vol_ml_to_l(r: random.Random) -> Dict[str, Any]:
    val_ml = r.randint(250, 7500)
    ans_l = val_ml / 1000.0
    prompt = f"A cold-pressed fruit juice bottle contains **{val_ml} ml** of guava juice.\n\nConvert this capacity to litres (**l**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ l}} = 1\\\\,000\\\\text{{ ml}}$\\n"
        f"• Converting from millilitres to litres requires **division** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Volume in litres}} = \\\\frac{{{val_ml}\\\\text{{ ml}}}}{{1\\\\,000}} = \\\\mathbf{{{_fmt(ans_l)}\\\\text{{ l}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing capacity by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_l)}\\\\text{{ l}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_vol_ml_to_l",
        prompt=prompt,
        answer=f"{_fmt(ans_l)} l",
        sol=sol,
        rubric=[f"Method: {val_ml} ÷ 1000 [1 Mark]", f"Accuracy: {_fmt(ans_l)} l [1 Mark]"],
        hints={
            "tier_1": "There are 1 000 millilitres in 1 litre (1 l = 1 000 ml).",
            "tier_2": f"Divide {val_ml} by 1 000.",
            "tier_3": f"{val_ml} ÷ 1 000 = {_fmt(ans_l)} l."
        }
    )

def _gen_conv_vol_l_to_ml(r: random.Random) -> Dict[str, Any]:
    val_l = round(r.uniform(0.35, 6.5), 2)
    ans_ml = round(val_l * 1000, 1)
    prompt = f"A motor mechanic fills an engine with **{_fmt(val_l)} l** of synthetic motor oil.\n\nConvert this volume to millilitres (**ml**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ l}} = 1\\\\,000\\\\text{{ ml}}$\\n"
        f"• Converting from litres to millilitres requires **multiplication** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Volume in ml}} = {_fmt(val_l)}\\\\text{{ l}} \\\\times 1\\\\,000 = \\\\mathbf{{{_fmt(ans_ml)}\\\\text{{ ml}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_ml)}\\\\text{{ ml}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted value with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_vol_l_to_ml",
        prompt=prompt,
        answer=f"{_fmt(ans_ml)} ml",
        sol=sol,
        rubric=[f"Method: {_fmt(val_l)} × 1000 [1 Mark]", f"Accuracy: {_fmt(ans_ml)} ml [1 Mark]"],
        hints={
            "tier_1": "1 litre = 1 000 millilitres.",
            "tier_2": f"Multiply {_fmt(val_l)} by 1 000.",
            "tier_3": f"{_fmt(val_l)} × 1 000 = {_fmt(ans_ml)} ml."
        }
    )

def _gen_conv_vol_l_to_kl(r: random.Random) -> Dict[str, Any]:
    val_l = r.randint(2500, 48000)
    ans_kl = val_l / 1000.0
    prompt = f"A municipal water meter reading indicates that a family household consumed **{val_l} l** of water in March.\n\nConvert this consumption to kilolitres (**kl**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ kl}} = 1\\\\,000\\\\text{{ l}}$\\n"
        f"• Converting from litres to kilolitres requires **division** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Volume in kl}} = \\\\frac{{{val_l}\\\\text{{ l}}}}{{1\\\\,000}} = \\\\mathbf{{{_fmt(ans_kl)}\\\\text{{ kl}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_kl)}\\\\text{{ kl}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted consumption with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_vol_l_to_kl",
        prompt=prompt,
        answer=f"{_fmt(ans_kl)} kl",
        sol=sol,
        rubric=[f"Method: {val_l} ÷ 1000 [1 Mark]", f"Accuracy: {_fmt(ans_kl)} kl [1 Mark]"],
        hints={
            "tier_1": "1 kilolitre (kl) = 1 000 litres (l).",
            "tier_2": f"Divide {val_l} by 1 000.",
            "tier_3": f"{val_l} ÷ 1 000 = {_fmt(ans_kl)} kl."
        }
    )

def _gen_conv_vol_kl_to_l(r: random.Random) -> Dict[str, Any]:
    val_kl = round(r.uniform(1.5, 25.0), 2)
    ans_l = round(val_kl * 1000, 1)
    prompt = f"A communal water delivery tanker delivers **{_fmt(val_kl)} kl** of drinking water to a rural clinic.\n\nConvert this water volume to litres (**l**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ kl}} = 1\\\\,000\\\\text{{ l}}$\\n"
        f"• Converting from kilolitres to litres requires **multiplication** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Volume in l}} = {_fmt(val_kl)}\\\\text{{ kl}} \\\\times 1\\\\,000 = \\\\mathbf{{{_fmt(ans_l)}\\\\text{{ l}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_l)}\\\\text{{ l}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted volume with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_vol_kl_to_l",
        prompt=prompt,
        answer=f"{_fmt(ans_l)} l",
        sol=sol,
        rubric=[f"Method: {_fmt(val_kl)} × 1000 [1 Mark]", f"Accuracy: {_fmt(ans_l)} l [1 Mark]"],
        hints={
            "tier_1": "1 kilolitre = 1 000 litres.",
            "tier_2": f"Multiply {_fmt(val_kl)} by 1 000.",
            "tier_3": f"{_fmt(val_kl)} × 1 000 = {_fmt(ans_l)} l."
        }
    )

def _gen_conv_vol_cm3_to_ml(r: random.Random) -> Dict[str, Any]:
    val_cm3 = r.randint(45, 950)
    prompt = f"A rectangular metal container has an internal volume of **{val_cm3} cm³**.\n\nState the liquid capacity of this container in millilitres (**ml**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Fact**\\n"
        f"• Core equivalence rule: $1\\\\text{{ cm}}^3 = 1\\\\text{{ ml}}$\\n"
        f"• Cubic centimetres and millilitres are directly equivalent on a 1-to-1 basis.\\n\\n"
        f"**Step 2: Method & Stating Equivalence**\\n"
        f"$$\\\\text{{Capacity in ml}} = {val_cm3}\\\\text{{ cm}}^3 \\\\times 1 = \\\\mathbf{{{val_cm3}\\\\text{{ ml}}}}$$\\n"
        f"✓ [1 Mark: Method – stating or applying the 1 cm³ = 1 ml equivalence]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {val_cm3}\\\\text{{ ml}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct capacity with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_vol_cm3_to_ml",
        prompt=prompt,
        answer=f"{val_cm3} ml",
        sol=sol,
        rubric=["Method: 1 cm³ = 1 ml [1 Mark]", f"Accuracy: {val_cm3} ml [1 Mark]"],
        hints={
            "tier_1": "1 cubic centimetre (cm³) is exactly equal to 1 millilitre (ml).",
            "tier_2": "Because the ratio is 1:1, the numeric value remains the same.",
            "tier_3": f"{val_cm3} cm³ = {val_cm3} ml."
        }
    )

def _gen_conv_vol_cm3_to_l(r: random.Random) -> Dict[str, Any]:
    val_cm3 = r.randint(1200, 15000)
    ans_l = val_cm3 / 1000.0
    prompt = f"An aquarium has an internal volume of **{val_cm3} cm³**.\n\nConvert this capacity to litres (**l**)."
    sol = (
        f"**Step 1: Thought Process & Two-Stage Conversion**\\n"
        f"• Equivalence: $1\\\\text{{ cm}}^3 = 1\\\\text{{ ml}}$\\n"
        f"• Therefore, ${val_cm3}\\\\text{{ cm}}^3 = {val_cm3}\\\\text{{ ml}}$\\n"
        f"• Standard rule: $1\\\\text{{ l}} = 1\\\\,000\\\\text{{ ml}}$ (divide by 1 000 to convert to litres).\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Volume in litres}} = \\\\frac{{{val_cm3}\\\\text{{ ml}}}}{{1\\\\,000}} = \\\\mathbf{{{_fmt(ans_l)}\\\\text{{ l}}}}$$\\n"
        f"✓ [1 Mark: Method – converting cm³ to ml and dividing by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(ans_l)}\\\\text{{ l}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct capacity with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_vol_cm3_to_l",
        prompt=prompt,
        answer=f"{_fmt(ans_l)} l",
        sol=sol,
        rubric=[f"Method: {val_cm3} ÷ 1000 [1 Mark]", f"Accuracy: {_fmt(ans_l)} l [1 Mark]"],
        hints={
            "tier_1": "1 cm³ = 1 ml, and 1 000 ml = 1 litre.",
            "tier_2": f"Divide {val_cm3} by 1 000.",
            "tier_3": f"{val_cm3} ÷ 1 000 = {_fmt(ans_l)} l."
        }
    )

def _gen_conv_vol_m3_to_l(r: random.Random) -> Dict[str, Any]:
    val_m3 = round(r.uniform(1.2, 8.5), 1)
    ans_l = int(val_m3 * 1000)
    prompt = f"A rainwater harvesting tank has an internal volume of **{_fmt(val_m3)} m³**.\n\nCalculate the total capacity of the tank in litres (**l**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Core equivalence rule: $1\\\\text{{ m}}^3 = 1\\\\,000\\\\text{{ l}}$ (or $1\\\\text{{ kl}}$)\\n"
        f"• Converting from cubic metres to litres requires **multiplication** by $1\\\\,000$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Capacity in litres}} = {_fmt(val_m3)}\\\\text{{ m}}^3 \\\\times 1\\\\,000 = \\\\mathbf{{{ans_l}\\\\text{{ l}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying by 1 000]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {ans_l}\\\\text{{ l}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct capacity with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_vol_m3_to_l",
        prompt=prompt,
        answer=f"{ans_l} l",
        sol=sol,
        rubric=[f"Method: {_fmt(val_m3)} × 1000 [1 Mark]", f"Accuracy: {ans_l} l [1 Mark]"],
        hints={
            "tier_1": "1 cubic metre (m³) holds exactly 1 000 litres.",
            "tier_2": f"Multiply {_fmt(val_m3)} by 1 000.",
            "tier_3": f"{_fmt(val_m3)} × 1 000 = {ans_l} l."
        }
    )


# ===========================================================================
# CLUSTER 4: KITCHEN COOKING & RECIPE CONVERSIONS (6 Archetypes)
# ===========================================================================

def _gen_cook_tsp_to_ml(r: random.Random) -> Dict[str, Any]:
    tsp_count = r.choice([2, 3, 4, 5, 6])
    ans_ml = tsp_count * 5
    prompt = f"A recipe for traditional South African koeksisters calls for **{tsp_count} teaspoons (tsp)** of ground cinnamon.\n\nCalculate the equivalent volume in millilitres (**ml**)."
    sol = (
        f"**Step 1: Thought Process & Standard Kitchen Measure**\\n"
        f"• In South African cooking standards: $1\\\\text{{ teaspoon (tsp)}} = 5\\\\text{{ ml}}$\\n"
        f"• To find the total volume, multiply the number of teaspoons by $5$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Volume in ml}} = {tsp_count}\\\\text{{ tsp}} \\\\times 5\\\\text{{ ml/tsp}} = \\\\mathbf{{{ans_ml}\\\\text{{ ml}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying teaspoons by 5]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {ans_ml}\\\\text{{ ml}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct volume with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="cook_tsp_to_ml",
        prompt=prompt,
        answer=f"{ans_ml} ml",
        sol=sol,
        rubric=[f"Method: {tsp_count} × 5 [1 Mark]", f"Accuracy: {ans_ml} ml [1 Mark]"],
        hints={
            "tier_1": "1 standard teaspoon = 5 ml.",
            "tier_2": f"Multiply {tsp_count} by 5.",
            "tier_3": f"{tsp_count} × 5 = {ans_ml} ml."
        }
    )

def _gen_cook_tbsp_to_ml(r: random.Random) -> Dict[str, Any]:
    tbsp_count = r.choice([2, 3, 4, 5])
    ans_ml = tbsp_count * 15
    prompt = f"A recipe for malva pudding batter requires **{tbsp_count} tablespoons (tbsp)** of smooth apricot jam.\n\nCalculate the total volume of apricot jam in millilitres (**ml**)."
    sol = (
        f"**Step 1: Thought Process & Standard Kitchen Measure**\\n"
        f"• In South African cooking standards: $1\\\\text{{ tablespoon (tbsp)}} = 15\\\\text{{ ml}}$\\n"
        f"• Multiply the number of tablespoons by $15$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Volume in ml}} = {tbsp_count}\\\\text{{ tbsp}} \\\\times 15\\\\text{{ ml/tbsp}} = \\\\mathbf{{{ans_ml}\\\\text{{ ml}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying tablespoons by 15]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {ans_ml}\\\\text{{ ml}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct volume with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="cook_tbsp_to_ml",
        prompt=prompt,
        answer=f"{ans_ml} ml",
        sol=sol,
        rubric=[f"Method: {tbsp_count} × 15 [1 Mark]", f"Accuracy: {ans_ml} ml [1 Mark]"],
        hints={
            "tier_1": "1 standard tablespoon = 15 ml.",
            "tier_2": f"Multiply {tbsp_count} by 15.",
            "tier_3": f"{tbsp_count} × 15 = {ans_ml} ml."
        }
    )

def _gen_cook_tbsp_to_tsp(r: random.Random) -> Dict[str, Any]:
    tbsp_count = r.choice([2, 3, 4])
    ans_tsp = tbsp_count * 3
    prompt = f"A home baker only has a measuring teaspoon available, but the recipe specifies **{tbsp_count} tablespoons (tbsp)** of vanilla essence.\n\nCalculate how many teaspoons (**tsp**) the baker must measure out."
    sol = (
        f"**Step 1: Thought Process & Kitchen Ratio**\\n"
        f"• $1\\\\text{{ tablespoon}} = 15\\\\text{{ ml}}$ and $1\\\\text{{ teaspoon}} = 5\\\\text{{ ml}}$\\n"
        f"• Ratio: $\\\\frac{{15\\\\text{{ ml}}}}{{5\\\\text{{ ml}}}} = 3\\\\text{{ teaspoons per tablespoon}}$\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Teaspoons needed}} = {tbsp_count}\\\\text{{ tbsp}} \\\\times 3 = \\\\mathbf{{{ans_tsp}\\\\text{{ tsp}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying tablespoons by 3]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {ans_tsp}\\\\text{{ tsp}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct number of teaspoons]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="cook_tbsp_to_tsp",
        prompt=prompt,
        answer=f"{ans_tsp} tsp",
        sol=sol,
        rubric=[f"Method: {tbsp_count} × 3 [1 Mark]", f"Accuracy: {ans_tsp} tsp [1 Mark]"],
        hints={
            "tier_1": "1 tablespoon = 15 ml and 1 teaspoon = 5 ml, so 1 tbsp = 3 tsp.",
            "tier_2": f"Multiply {tbsp_count} by 3.",
            "tier_3": f"{tbsp_count} × 3 = {ans_tsp} tsp."
        }
    )

def _gen_cook_cups_to_ml(r: random.Random) -> Dict[str, Any]:
    cups = r.choice([1.5, 2.0, 2.5, 3.0, 3.5])
    ans_ml = int(cups * 250)
    prompt = f"A recipe for vetkoek requires **{_fmt(cups)} cups** of fresh full-cream milk.\n\nCalculate the total volume of milk in millilitres (**ml**)."
    sol = (
        f"**Step 1: Thought Process & Standard Metric Cup**\\n"
        f"• In South Africa, 1 standard metric cup = 250 ml.\\n"
        f"• To find the total millilitres, multiply the number of cups by 250.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Volume in ml}} = {_fmt(cups)}\\\\text{{ cups}} \\\\times 250\\\\text{{ ml/cup}} = \\\\mathbf{{{ans_ml}\\\\text{{ ml}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying cups by 250]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {ans_ml}\\\\text{{ ml}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct volume with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="cook_cups_to_ml",
        prompt=prompt,
        answer=f"{ans_ml} ml",
        sol=sol,
        rubric=[f"Method: {_fmt(cups)} × 250 [1 Mark]", f"Accuracy: {ans_ml} ml [1 Mark]"],
        hints={
            "tier_1": "In South Africa, 1 standard metric cooking cup = 250 ml.",
            "tier_2": f"Multiply {_fmt(cups)} by 250.",
            "tier_3": f"{_fmt(cups)} × 250 = {ans_ml} ml."
        }
    )

def _gen_cook_recipe_scaling(r: random.Random) -> Dict[str, Any]:
    base_servings = 4
    target_servings = r.choice([8, 12, 16])
    scale_factor = target_servings // base_servings
    base_sugar_g = r.choice([150, 200, 250])
    target_sugar_g = base_sugar_g * scale_factor
    prompt = f"A recipe makes **{base_servings} servings** of pudding and requires **{base_sugar_g} g** of castor sugar.\n\nCalculate the mass of sugar (in grams) required to make **{target_servings} servings**."
    sol = (
        f"**Step 1: Thought Process & Scaling Factor**\\n"
        f"• Determine the proportion multiplier between desired and original servings:\\n"
        f"$$\\\\text{{Scale Factor}} = \\\\frac{{{target_servings}\\\\text{{ servings}}}}{{{base_servings}\\\\text{{ servings}}}} = {scale_factor}$$\\n"
        f"✓ [1 Mark: Method – calculating the scale factor of {scale_factor}]\\n\\n"
        f"**Step 2: Method & Scaled Ingredient Mass**\\n"
        f"$$\\\\text{{Sugar required}} = {base_sugar_g}\\\\text{{ g}} \\\\times {scale_factor} = \\\\mathbf{{{target_sugar_g}\\\\text{{ g}}}}$$\\n"
        f"✓ [1 Mark: Accuracy – multiplying base mass by scale factor]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Mass}} = {target_sugar_g}\\\\text{{ g}}$$\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="cook_recipe_scaling",
        prompt=prompt,
        answer=f"{target_sugar_g} g",
        sol=sol,
        rubric=[f"Method: {target_servings} ÷ {base_servings} = {scale_factor} [1 Mark]", f"Accuracy: {base_sugar_g} × {scale_factor} = {target_sugar_g} g [1 Mark]"],
        hints={
            "tier_1": f"Divide target servings ({target_servings}) by base servings ({base_servings}) to find the multiplier.",
            "tier_2": f"Multiply {base_sugar_g} g by {scale_factor}.",
            "tier_3": f"{base_sugar_g} × {scale_factor} = {target_sugar_g} g."
        }
    )

def _gen_cook_dry_cups_to_grams(r: random.Random) -> Dict[str, Any]:
    ingredient, grams_per_cup = r.choice([
        ("cake flour", 120),
        ("white sugar", 200),
        ("brown sugar", 220),
        ("butter", 225),
        ("cocoa powder", 100),
    ])
    cups = r.choice([1.5, 2.0, 2.5, 3.0])
    total_g = int(cups * grams_per_cup)
    prompt = (
        f"Refer to the standard dry ingredient conversion table below:\n\n"
        f"| Ingredient | 1 Cup Equivalent Mass |\n"
        f"| :--- | :--- |\n"
        f"| **{ingredient.title()}** | **{grams_per_cup} g** |\n\n"
        f"Calculate the mass in grams (**g**) of **{_fmt(cups)} cups** of {ingredient}."
    )
    sol = (
        f"**Step 1: Thought Process & Table Reference**\\n"
        f"• From the table, 1 cup of {ingredient} = {grams_per_cup} g.\\n"
        f"• To find the total mass for {_fmt(cups)} cups, multiply the cups by the mass per cup.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Mass}} = {_fmt(cups)}\\\\text{{ cups}} \\\\times {grams_per_cup}\\\\text{{ g/cup}} = \\\\mathbf{{{total_g}\\\\text{{ g}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying cups by {grams_per_cup} g]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {total_g}\\\\text{{ g}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted mass with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="cook_dry_cups_to_grams",
        prompt=prompt,
        answer=f"{total_g} g",
        sol=sol,
        rubric=[f"Method: {_fmt(cups)} × {grams_per_cup} [1 Mark]", f"Accuracy: {total_g} g [1 Mark]"],
        hints={
            "tier_1": f"Each cup of {ingredient} weighs {grams_per_cup} grams according to the table.",
            "tier_2": f"Multiply {_fmt(cups)} by {grams_per_cup}.",
            "tier_3": f"{_fmt(cups)} × {grams_per_cup} = {total_g} g."
        }
    )


# ===========================================================================
# CLUSTER 5: IMPERIAL TO METRIC CONTEXTS (2 Archetypes)
# ===========================================================================

def _gen_conv_imperial_inches_feet_to_cm_m(r: random.Random) -> Dict[str, Any]:
    inches = r.choice([32, 40, 43, 50, 55, 65])
    cm_val = round(inches * 2.54, 1)
    prompt = (
        f"A flat-screen television has a screen diagonal of **{inches} inches**.\n\n"
        f"Given that **1 inch = 2,54 cm**, calculate the screen diagonal in centimetres (**cm**)."
    )
    sol = (
        f"**Step 1: Thought Process & Given Conversion Factor**\\n"
        f"• Imperial conversion factor: $1\\\\text{{ inch}} = 2{{,}}54\\\\text{{ cm}}$\\n"
        f"• Multiply the screen size in inches by $2{{,}}54$ to obtain centimetres.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Diagonal in cm}} = {inches} \\\\times 2{{,}}54 = \\\\mathbf{{{_fmt(cm_val)}\\\\text{{ cm}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying inches by 2,54]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(cm_val)}\\\\text{{ cm}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted length with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_imperial_inches_feet_to_cm_m",
        prompt=prompt,
        answer=f"{_fmt(cm_val)} cm",
        sol=sol,
        rubric=[f"Method: {inches} × 2,54 [1 Mark]", f"Accuracy: {_fmt(cm_val)} cm [1 Mark]"],
        hints={
            "tier_1": "1 inch = 2,54 centimetres.",
            "tier_2": f"Multiply {inches} by 2,54.",
            "tier_3": f"{inches} × 2,54 = {_fmt(cm_val)} cm."
        }
    )

def _gen_conv_imperial_pounds_gallons_to_metric(r: random.Random) -> Dict[str, Any]:
    pounds = r.choice([15, 20, 25, 30, 35, 40])
    kg_val = round(pounds * 0.454, 2)
    prompt = (
        f"An imported gym kettlebell has its mass labeled as **{pounds} pounds (lbs)**.\n\n"
        f"Given that **1 pound = 0,454 kg**, calculate the mass of the kettlebell in kilograms (**kg**)."
    )
    sol = (
        f"**Step 1: Thought Process & Given Conversion Factor**\\n"
        f"• Imperial conversion factor: $1\\\\text{{ lb}} = 0{{,}}454\\\\text{{ kg}}$\\n"
        f"• Multiply the mass in pounds by $0{{,}}454$ to obtain kilograms.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Mass in kg}} = {pounds} \\\\times 0{{,}}454 = \\\\mathbf{{{_fmt(kg_val)}\\\\text{{ kg}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying pounds by 0,454]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(kg_val)}\\\\text{{ kg}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted mass with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="conv_imperial_pounds_gallons_to_metric",
        prompt=prompt,
        answer=f"{_fmt(kg_val)} kg",
        sol=sol,
        rubric=[f"Method: {pounds} × 0,454 [1 Mark]", f"Accuracy: {_fmt(kg_val)} kg [1 Mark]"],
        hints={
            "tier_1": "1 pound (lb) = 0,454 kilograms (kg).",
            "tier_2": f"Multiply {pounds} by 0,454.",
            "tier_3": f"{pounds} × 0,454 = {_fmt(kg_val)} kg."
        }
    )


# ===========================================================================
# CLUSTER 6: TEMPERATURE CONVERSIONS (5 Archetypes - Clean LaTeX, Zero Red Font)
# ===========================================================================

def _gen_temp_celsius_to_fahrenheit(r: random.Random) -> Dict[str, Any]:
    celsius = r.choice([15, 20, 25, 30, 35, 180, 200])
    fahrenheit = round((celsius * 1.8) + 32, 1)
    prompt = (
        f"A weather broadcast indicates an afternoon temperature of **{celsius} °C** in Pretoria.\n\n"
        f"Calculate the equivalent temperature in degrees Fahrenheit (**°F**)."
    )
    sol = (
        f"**Step 1: Thought Process & Formula**\\n"
        f"• Standard temperature conversion rule: multiply Celsius by $1{,}8$, then add $32$.\\n"
        f"• Formula: $\\\\text{{°F}} = (\\\\text{{°C}} \\\\times 1{{,}}8) + 32$\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Temperature in °F}} = ({celsius} \\\\times 1{{,}}8) + 32 = {celsius * 1.8} + 32 = \\\\mathbf{{{_fmt(fahrenheit)}\\\\text{{ °F}}}}$$\\n"
        f"✓ [1 Mark: Method – substituting Celsius into formula and evaluating]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Temperature}} = {_fmt(fahrenheit)}\\\\text{{ °F}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct temperature with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="temp_celsius_to_fahrenheit",
        prompt=prompt,
        answer=f"{_fmt(fahrenheit)} °F",
        sol=sol,
        rubric=[f"Method: ({celsius} × 1,8) + 32 [1 Mark]", f"Accuracy: {_fmt(fahrenheit)} °F [1 Mark]"],
        hints={
            "tier_1": "Formula: °F = (°C × 1,8) + 32.",
            "tier_2": f"Multiply {celsius} by 1,8 first ({celsius * 1.8}), then add 32.",
            "tier_3": f"{celsius * 1.8} + 32 = {_fmt(fahrenheit)} °F."
        }
    )

def _gen_temp_fahrenheit_to_celsius(r: random.Random) -> Dict[str, Any]:
    fahrenheit = r.choice([68, 77, 86, 95, 350, 400])
    celsius = round((fahrenheit - 32) / 1.8, 1)
    prompt = (
        f"An American online recipe instructs you to preheat the oven to **{fahrenheit} °F**.\n\n"
        f"Calculate the required oven temperature in degrees Celsius (**°C**). Round your answer to one decimal place if needed."
    )
    sol = (
        f"**Step 1: Thought Process & Formula**\\n"
        f"• Standard temperature conversion rule: subtract $32$ from Fahrenheit, then divide by $1{,}8$.\\n"
        f"• Formula: $\\\\text{{°C}} = (\\\\text{{°F}} - 32) \\\\div 1{{,}}8$\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Temperature in °C}} = ({fahrenheit} - 32) \\\\div 1{{,}}8 = {fahrenheit - 32} \\\\div 1{{,}}8 = \\\\mathbf{{{_fmt(celsius)}\\\\text{{ °C}}}}$$\\n"
        f"✓ [1 Mark: Method – subtracting 32 and dividing by 1,8]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Temperature}} = {_fmt(celsius)}\\\\text{{ °C}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct temperature with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="temp_fahrenheit_to_celsius",
        prompt=prompt,
        answer=f"{_fmt(celsius)} °C",
        sol=sol,
        rubric=[f"Method: ({fahrenheit} - 32) ÷ 1,8 [1 Mark]", f"Accuracy: {_fmt(celsius)} °C [1 Mark]"],
        hints={
            "tier_1": "Formula: °C = (°F - 32) ÷ 1,8.",
            "tier_2": f"Subtract 32 from {fahrenheit} first ({fahrenheit - 32}), then divide by 1,8.",
            "tier_3": f"{fahrenheit - 32} ÷ 1,8 = {_fmt(celsius)} °C."
        }
    )

def _gen_temp_baking_oven_setting(r: random.Random) -> Dict[str, Any]:
    c_converted = 176.7
    dial_options = ["160 °C", "180 °C", "200 °C", "220 °C"]
    correct_dial = "180 °C"
    prompt = (
        f"A baking recipe specifies an oven setting of **350 °F** for baking rusks.\n\n"
        f"A South African oven only shows dial markings in degrees Celsius at intervals of **160 °C, 180 °C, 200 °C, and 220 °C**.\n\n"
        f"Calculate the equivalent temperature in degrees Celsius and determine which dial setting should be selected."
    )
    sol = (
        f"**Step 1: Convert 350 °F to degrees Celsius**\\n"
        f"$$\\\\text{{°C}} = (350 - 32) \\\\div 1{{,}}8 = 318 \\\\div 1{{,}}8 = 176{{,}}67\\\\text{{ °C}}$$\\n"
        f"✓ [1 Mark: Method – converting 350 °F to approximately 176,7 °C]\\n\\n"
        f"**Step 2: Select the closest available oven dial setting**\\n"
        f"• The available markings are 160 °C, 180 °C, 200 °C, 220 °C.\\n"
        f"• $176{{,}}67\\\\text{{ °C}}$ is closest to **180 °C** (a difference of only 3,3 °C compared to 16,7 °C for 160 °C).\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Selected Dial Setting}} = \\\\mathbf{{180\\\\text{{ °C}}}}$$\\n"
        f"✓ [1 Mark: Accuracy – selecting 180 °C]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="temp_baking_oven_setting",
        prompt=prompt,
        answer=correct_dial,
        sol=sol,
        rubric=["Method: (350 - 32) ÷ 1,8 = 176,7 °C [1 Mark]", "Accuracy: Select 180 °C setting [1 Mark]"],
        hints={
            "tier_1": "Convert 350 °F to °C: (350 - 32) ÷ 1,8 = 176,7 °C.",
            "tier_2": "Compare 176,7 °C to the available settings: 160 °C, 180 °C, 200 °C, 220 °C.",
            "tier_3": "176,7 °C is closest to 180 °C."
        },
        q_type="multiple_choice",
        options=dial_options,
        correct_idx=1,
    )

def _gen_temp_weather_comparison(r: random.Random) -> Dict[str, Any]:
    c_sa = r.randint(28, 38)
    f_us = r.randint(80, 105)
    f_sa = round((c_sa * 1.8) + 32, 1)
    diff = round(abs(f_sa - f_us), 1)
    warmer_city = "Durban" if f_sa > f_us else "Phoenix (USA)"

    prompt = (
        f"On a summer day, Durban records a maximum temperature of **{c_sa} °C**, while Phoenix (USA) records **{f_us} °F**.\n\n"
        f"Determine which city was warmer and by how many degrees Fahrenheit (**°F**)."
    )
    sol = (
        f"**Step 1: Convert Durban's temperature to °F**\\n"
        f"$$\\\\text{{Durban in °F}} = ({c_sa} \\\\times 1{{,}}8) + 32 = {_fmt(f_sa)}\\\\text{{ °F}}$$\\n"
        f"✓ [1 Mark: Method – converting Celsius to Fahrenheit]\\n\\n"
        f"**Step 2: Compare temperatures & determine difference**\\n"
        f"• Durban: {_fmt(f_sa)} °F\\n"
        f"• Phoenix (USA): {f_us} °F\\n"
        f"• Difference: $|{_fmt(f_sa)} - {f_us}| = {_fmt(diff)}\\\\text{{ °F}}$\\n\\n"
        f"**Step 3: Final Conclusion**\\n"
        f"$$\\\\mathbf{{{warmer_city}\\\\text{{ was warmer by }}{_fmt(diff)}\\\\text{{ °F}}}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct city and difference]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    ans_label = f"{warmer_city} was warmer (by {_fmt(diff)} °F)"
    other_city = "Phoenix (USA)" if warmer_city == "Durban" else "Durban"
    options = [
        ans_label,
        f"{other_city} was warmer (by {_fmt(diff)} °F)",
        f"{warmer_city} was warmer (by {_fmt(round(diff + 5, 1))} °F)",
        f"{other_city} was warmer (by {_fmt(round(diff + 5, 1))} °F)",
    ]
    r.shuffle(options)
    return _make_q(
        subskill="temp_weather_comparison",
        prompt=prompt,
        answer=ans_label,
        sol=sol,
        rubric=[f"Method: Durban = ({c_sa} × 1,8) + 32 = {_fmt(f_sa)} °F [1 Mark]", f"Accuracy: {warmer_city} warmer by {_fmt(diff)} °F [1 Mark]"],
        hints={
            "tier_1": f"Convert Durban's {c_sa} °C to °F: ({c_sa} × 1,8) + 32 = {_fmt(f_sa)} °F.",
            "tier_2": f"Compare {_fmt(f_sa)} °F with Phoenix's {f_us} °F.",
            "tier_3": f"{warmer_city} is warmer by {_fmt(diff)} °F."
        },
        q_type="multiple_choice",
        options=options,
        correct_idx=options.index(ans_label),
    )

def _gen_temp_negative_freezing_c_to_f(r: random.Random) -> Dict[str, Any]:
    c_neg = r.choice([-5, -10, -15, -20])
    f_ans = round((c_neg * 1.8) + 32, 1)
    prompt = (
        f"A laboratory freezer storage unit is kept at a freezing temperature of **{c_neg} °C**.\n\n"
        f"Calculate this freezing temperature in degrees Fahrenheit (**°F**)."
    )
    sol = (
        f"**Step 1: Thought Process & Negative Numbers Rule**\\n"
        f"• Formula: $\\\\text{{°F}} = (\\\\text{{°C}} \\\\times 1{{,}}8) + 32$\\n"
        f"• When multiplying a negative number by $1{,}8$, the result is negative.\\n"
        f"• Adding $32$ shifts the temperature into the positive or negative range.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{°F}} = ({c_neg} \\\\times 1{{,}}8) + 32 = {c_neg * 1.8} + 32 = \\\\mathbf{{{_fmt(f_ans)}\\\\text{{ °F}}}}$$\\n"
        f"✓ [1 Mark: Method – correct substitution with negative value]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Temperature}} = {_fmt(f_ans)}\\\\text{{ °F}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct signed temperature with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="temp_negative_freezing_c_to_f",
        prompt=prompt,
        answer=f"{_fmt(f_ans)} °F",
        sol=sol,
        rubric=[f"Method: ({c_neg} × 1,8) + 32 = {c_neg * 1.8} + 32 [1 Mark]", f"Accuracy: {_fmt(f_ans)} °F [1 Mark]"],
        hints={
            "tier_1": "Formula: °F = (°C × 1,8) + 32.",
            "tier_2": f"{c_neg} × 1,8 = {c_neg * 1.8}. Now add 32: {c_neg * 1.8} + 32.",
            "tier_3": f"Final answer: {_fmt(f_ans)} °F."
        }
    )


# ===========================================================================
# CLUSTER 7: TIME CALCULATIONS, TIMETABLES & SPEED (17 Archetypes)
# ===========================================================================

def _gen_time_unit_seconds_minutes(r: random.Random) -> Dict[str, Any]:
    mins = r.choice([3, 4, 5, 6, 8, 12, 15])
    tot_sec = mins * 60
    prompt = f"A track athlete recorded a training split of **{tot_sec} seconds**.\n\nConvert this time to whole minutes (**min**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ minute}} = 60\\\\text{{ seconds}}$\\n"
        f"• Converting from seconds to minutes requires **division** by $60$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Time in minutes}} = \\\\frac{{{tot_sec}\\\\text{{ s}}}}{{60}} = \\\\mathbf{{{mins}\\\\text{{ min}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing seconds by 60]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {mins}\\\\text{{ min}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted time with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_unit_seconds_minutes",
        prompt=prompt,
        answer=f"{mins} min",
        sol=sol,
        rubric=[f"Method: {tot_sec} ÷ 60 [1 Mark]", f"Accuracy: {mins} min [1 Mark]"],
        hints={
            "tier_1": "There are 60 seconds in 1 minute.",
            "tier_2": f"Divide {tot_sec} by 60.",
            "tier_3": f"{tot_sec} ÷ 60 = {mins} min."
        }
    )

def _gen_time_unit_minutes_hours(r: random.Random) -> Dict[str, Any]:
    hrs = r.choice([1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
    tot_min = int(hrs * 60)
    prompt = f"A community meeting in Khayelitsha lasted for **{tot_min} minutes**.\n\nConvert this duration to hours (**h**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ hour}} = 60\\\\text{{ minutes}}$\\n"
        f"• Converting from minutes to hours requires **division** by $60$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Duration in hours}} = \\\\frac{{{tot_min}\\\\text{{ min}}}}{{60}} = \\\\mathbf{{{_fmt(hrs)}\\\\text{{ hours}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing minutes by 60]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {_fmt(hrs)}\\\\text{{ hours}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted duration with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_unit_minutes_hours",
        prompt=prompt,
        answer=f"{_fmt(hrs)} hours",
        sol=sol,
        rubric=[f"Method: {tot_min} ÷ 60 [1 Mark]", f"Accuracy: {_fmt(hrs)} hours [1 Mark]"],
        hints={
            "tier_1": "There are 60 minutes in 1 hour.",
            "tier_2": f"Divide {tot_min} by 60.",
            "tier_3": f"{tot_min} ÷ 60 = {_fmt(hrs)} hours."
        }
    )

def _gen_time_unit_hours_days(r: random.Random) -> Dict[str, Any]:
    days = r.choice([2, 3, 4, 5, 6, 7])
    tot_hours = days * 24
    prompt = f"A hospital nurse worked on a special rotation totaling **{tot_hours} hours**.\n\nConvert this time to full days (**days**)."
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Standard relationship: $1\\\\text{{ day}} = 24\\\\text{{ hours}}$\\n"
        f"• Converting from hours to days requires **division** by $24$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Duration in days}} = \\\\frac{{{tot_hours}\\\\text{{ hours}}}}{{24}} = \\\\mathbf{{{days}\\\\text{{ days}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing hours by 24]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = {days}\\\\text{{ days}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted days with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_unit_hours_days",
        prompt=prompt,
        answer=f"{days} days",
        sol=sol,
        rubric=[f"Method: {tot_hours} ÷ 24 [1 Mark]", f"Accuracy: {days} days [1 Mark]"],
        hints={
            "tier_1": "There are 24 hours in 1 day.",
            "tier_2": f"Divide {tot_hours} by 24.",
            "tier_3": f"{tot_hours} ÷ 24 = {days} days."
        }
    )

def _gen_time_unit_days_weeks_months(r: random.Random) -> Dict[str, Any]:
    weeks = r.choice([3, 4, 5, 6, 8])
    extra_days = r.choice([1, 2, 3, 4, 5])
    tot_days = (weeks * 7) + extra_days
    prompt = f"A construction crew worked on a school hall renovation for **{tot_days} days**.\n\nConvert this time into weeks and days."
    sol = (
        f"**Step 1: Thought Process & Weekly Breakdown**\\n"
        f"• Standard relationship: $1\\\\text{{ week}} = 7\\\\text{{ days}}$\\n"
        f"• Divide total days by $7$ to find completed weeks, with remainder representing remaining days.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Full weeks}} = {tot_days} \\\\div 7 = {weeks}\\\\text{{ remainder }}{extra_days}$$\\n"
        f"✓ [1 Mark: Method – dividing by 7 and determining remainder]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Answer}} = \\\\mathbf{{{weeks}\\\\text{{ weeks and }}{extra_days}\\\\text{{ days}}}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct weeks and days]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    ans = f"{weeks} weeks and {extra_days} days"
    return _make_q(
        subskill="time_unit_days_weeks_months",
        prompt=prompt,
        answer=ans,
        sol=sol,
        rubric=[f"Method: {tot_days} ÷ 7 [1 Mark]", f"Accuracy: {ans} [1 Mark]"],
        hints={
            "tier_1": "There are 7 days in 1 week.",
            "tier_2": f"Divide {tot_days} by 7: {tot_days // 7} full weeks, with remainder {tot_days % 7}.",
            "tier_3": f"{ans}."
        }
    )

def _gen_time_format_12h_to_24h(r: random.Random) -> Dict[str, Any]:
    is_pm = r.choice([True, False])
    h = r.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    m = r.choice([0, 15, 30, 45, 50])
    merid = "p.m." if is_pm else "a.m."
    h24 = h + 12 if is_pm else h
    ans_24 = f"{h24:02d}:{m:02d}"
    prompt = f"A bus ticket displays an afternoon departure time of **{h:02d}:{m:02d} {merid}**.\n\nConvert this time to **24-hour format** (hh:mm)."
    sol = (
        f"**Step 1: Thought Process & 24-Hour Rules**\\n"
        f"• For morning times (a.m.): keep the hour (e.g. 08:30 a.m. becomes 08:30).\\n"
        f"• For afternoon/evening times (p.m.): add $12$ to the hours (e.g. {h:02d} + 12 = {h24:02d}).\\n\\n"
        f"**Step 2: Method & Conversion**\\n"
        f"$$\\\\text{{24-Hour Time}} = ({h} + {12 if is_pm else 0}):{m:02d} = \\\\mathbf{{{ans_24}}}$$\\n"
        f"✓ [1 Mark: Method – applying 24-hour time conversion]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Time}} = {ans_24}$$\\n"
        f"✓ [1 Mark: Accuracy – correct 24-hour notation without a.m./p.m.]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_format_12h_to_24h",
        prompt=prompt,
        answer=ans_24,
        sol=sol,
        rubric=["Method: Add 12 hours for p.m. [1 Mark]", f"Accuracy: {ans_24} [1 Mark]"],
        hints={
            "tier_1": "For p.m. times after midday, add 12 to the hour.",
            "tier_2": f"Add 12 to {h}: {h} + 12 = {h24}.",
            "tier_3": f"{ans_24}."
        }
    )

def _gen_time_format_24h_to_12h(r: random.Random) -> Dict[str, Any]:
    h24 = r.choice([13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
    m = r.choice([0, 10, 20, 35, 45, 55])
    h12 = h24 - 12
    ans_12 = f"{h12:02d}:{m:02d} p.m."
    prompt = f"An electronic train schedule indicates that a train arrives at **{h24:02d}:{m:02d}**.\n\nConvert this time to **12-hour format** (including a.m. or p.m.)."
    sol = (
        f"**Step 1: Thought Process & 12-Hour Conversion**\\n"
        f"• Since {h24:02d} is greater than 12, this is an afternoon/evening time (p.m.).\\n"
        f"• Subtract $12$ from the hour: ${h24} - 12 = {h12}$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{12-Hour Time}} = ({h24} - 12):{m:02d}\\\\text{{ p.m.}} = \\\\mathbf{{{ans_12}}}$$\\n"
        f"✓ [1 Mark: Method – subtracting 12 and identifying p.m.]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Time}} = {ans_12}$$\\n"
        f"✓ [1 Mark: Accuracy – correct 12-hour format with p.m. identifier]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_format_24h_to_12h",
        prompt=prompt,
        answer=ans_12,
        sol=sol,
        rubric=[f"Method: {h24} - 12 = {h12} [1 Mark]", f"Accuracy: {ans_12} [1 Mark]"],
        hints={
            "tier_1": "Since the hour is greater than 12, subtract 12 and append 'p.m.'.",
            "tier_2": f"Subtract 12 from {h24}: {h24} - 12 = {h12}.",
            "tier_3": f"{ans_12}."
        }
    )

def _gen_time_decimal_to_hours_minutes(r: random.Random) -> Dict[str, Any]:
    h = r.choice([2, 3, 4, 5])
    m = r.choice([15, 30, 45, 12, 24, 36])
    dec_part = round(m / 60.0, 2)
    tot_dec = round(h + dec_part, 2)
    actual_m = round(dec_part * 60)
    ans = f"{h} hours and {actual_m} minutes"
    prompt = f"A road trip GPS device calculates an estimated travel time of **{_fmt(tot_dec)} hours**.\n\nConvert this decimal time into **hours and minutes**."
    sol = (
        f"**Step 1: Thought Process & Decimal Separation**\\n"
        f"• The whole number represents completed hours: **{h} hours**.\\n"
        f"• The decimal portion (${_fmt(dec_part)}$) represents a fraction of an hour.\\n"
        f"• Multiply the decimal fraction by $60$ to convert it to minutes.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Minutes}} = {_fmt(dec_part)} \\\\times 60 = \\\\mathbf{{{actual_m}\\\\text{{ minutes}}}}$$\\n"
        f"✓ [1 Mark: Method – multiplying decimal fraction by 60]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Time}} = \\\\mathbf{{{ans}}}$$\\n"
        f"✓ [1 Mark: Accuracy – stating hours and minutes correctly]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_decimal_to_hours_minutes",
        prompt=prompt,
        answer=ans,
        sol=sol,
        rubric=[f"Method: {_fmt(dec_part)} × 60 = {actual_m} min [1 Mark]", f"Accuracy: {ans} [1 Mark]"],
        hints={
            "tier_1": f"The whole number ({h}) is hours. Multiply the decimal part ({_fmt(dec_part)}) by 60.",
            "tier_2": f"{_fmt(dec_part)} × 60 = {actual_m} minutes.",
            "tier_3": f"{ans}."
        }
    )

def _gen_time_elapsed_same_day(r: random.Random) -> Dict[str, Any]:
    dep_h = r.choice([8, 9, 10, 11])
    dep_m = r.choice([15, 20, 30, 45])
    trip_h = r.choice([2, 3, 4])
    trip_m = r.choice([10, 20, 25, 35])
    tot_m = dep_m + trip_m
    arr_h = dep_h + trip_h + (tot_m // 60)
    arr_m = tot_m % 60
    ans = f"{trip_h} hours and {trip_m} minutes"
    prompt = (
        f"A long-distance taxi departs Mthatha at **{dep_h:02d}:{dep_m:02d}** and arrives in East London at **{arr_h:02d}:{arr_m:02d}** on the same day.\n\n"
        f"Calculate the total elapsed travel time (in hours and minutes)."
    )
    sol = (
        f"**Step 1: Thought Process & Time Subtraction**\\n"
        f"• Subtract the departure time from the arrival time: ${arr_h:02d}:{arr_m:02d} - {dep_h:02d}:{dep_m:02d}$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"• Hours: ${arr_h} - {dep_h} = {arr_h - dep_h}\\\\text{{ hours}}$\\n"
        f"• Minutes: ${arr_m} - {dep_m} = {trip_m}\\\\text{{ minutes}}$\\n"
        f"✓ [1 Mark: Method – subtracting departure time from arrival time]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Elapsed Time}} = \\\\mathbf{{{ans}}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct hours and minutes]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_elapsed_same_day",
        prompt=prompt,
        answer=ans,
        sol=sol,
        rubric=[f"Method: {arr_h:02d}:{arr_m:02d} - {dep_h:02d}:{dep_m:02d} [1 Mark]", f"Accuracy: {ans} [1 Mark]"],
        hints={
            "tier_1": f"Subtract departure time ({dep_h:02d}:{dep_m:02d}) from arrival time ({arr_h:02d}:{arr_m:02d}).",
            "tier_2": f"Find hours difference ({trip_h} h) and minutes difference ({trip_m} min).",
            "tier_3": f"{ans}."
        }
    )

def _gen_time_elapsed_crossing_midnight(r: random.Random) -> Dict[str, Any]:
    dep_h = r.choice([21, 22, 23])
    dep_m = r.choice([15, 30, 45])
    mins_to_mid = (24 * 60) - (dep_h * 60 + dep_m)
    arr_h = r.choice([4, 5, 6])
    arr_m = r.choice([10, 20, 30])
    mins_after_mid = (arr_h * 60) + arr_m
    tot_mins = mins_to_mid + mins_after_mid
    ans_h = tot_mins // 60
    ans_m = tot_mins % 60
    ans = f"{ans_h} hours and {ans_m} minutes"
    prompt = (
        f"An overnight intercity bus departs Bloemfontein at **{dep_h:02d}:{dep_m:02d}** and arrives in Durban at **{arr_h:02d}:{arr_m:02d}** the following morning.\n\n"
        f"Calculate the total travel time."
    )
    sol = (
        f"**Step 1: Thought Process & Crossing Midnight Breakdown**\\n"
        f"• Since the journey crosses midnight (24:00), split the calculation into two parts:\\n"
        f"  1. From departure ({dep_h:02d}:{dep_m:02d}) to midnight (24:00):\\n"
        f"     $$24:00 - {dep_h:02d}:{dep_m:02d} = {mins_to_mid // 60}\\\\text{{ hours and }}{mins_to_mid % 60}\\\\text{{ minutes}}$$\\n"
        f"  2. From midnight (00:00) to arrival ({arr_h:02d}:{arr_m:02d}):\\n"
        f"     $${arr_h}\\\\text{{ hours and }}{arr_m}\\\\text{{ minutes}}$$\\n\\n"
        f"**Step 2: Method & Summing Total Time**\\n"
        f"$$\\\\text{{Total Minutes}} = {mins_to_mid} + {mins_after_mid} = {tot_mins}\\\\text{{ minutes}}$$\\n"
        f"$$\\\\text{{Total Time}} = {ans_h}\\\\text{{ hours and }}{ans_m}\\\\text{{ minutes}}$$\\n"
        f"✓ [1 Mark: Method – splitting at midnight and summing periods]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Time}} = \\\\mathbf{{{ans}}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct hours and minutes]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_elapsed_crossing_midnight",
        prompt=prompt,
        answer=ans,
        sol=sol,
        rubric=["Method: Split at midnight (24:00) and add morning duration [1 Mark]", f"Accuracy: {ans} [1 Mark]"],
        hints={
            "tier_1": f"Calculate time from {dep_h:02d}:{dep_m:02d} to midnight (24:00), then add {arr_h:02d}:{arr_m:02d}.",
            "tier_2": f"Time before midnight: {mins_to_mid // 60} h {mins_to_mid % 60} min. Add {arr_h} h {arr_m} min.",
            "tier_3": f"{ans}."
        }
    )

def _gen_time_elapsed_multi_day(r: random.Random) -> Dict[str, Any]:
    dep_time = "14:00"
    arr_time = "18:30"
    total_hours = 52.5  # Friday 14:00 to Sunday 18:30 = 24 + 24 + 4.5 = 52.5 hrs
    ans = "52,5 hours"
    prompt = (
        f"A freight cargo train departs Polokwane on **Friday at {dep_time}** and reaches Cape Town harbor on **Sunday at {arr_time}**.\n\n"
        f"Calculate the total travel duration in **hours**."
    )
    sol = (
        f"**Step 1: Thought Process & Multi-Day Breakdown**\\n"
        f"• Friday 14:00 to Saturday 14:00 = 24 hours (1 full day)\\n"
        f"• Saturday 14:00 to Sunday 14:00 = 24 hours (1 full day)\\n"
        f"• Sunday 14:00 to Sunday 18:30 = 4 hours and 30 minutes = 4,5 hours\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Total Travel Hours}} = 24 + 24 + 4{{,}}5 = \\\\mathbf{{52{{,}}5\\\\text{{ hours}}}}$$\\n"
        f"✓ [1 Mark: Method – counting 24-hr daily cycles and remaining time]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Travel Time}} = 52{{,}}5\\\\text{{ hours}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct total hours]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_elapsed_multi_day",
        prompt=prompt,
        answer=ans,
        sol=sol,
        rubric=["Method: 24 + 24 + 4,5 hours [1 Mark]", f"Accuracy: {ans} [1 Mark]"],
        hints={
            "tier_1": "Count full 24-hour periods from Friday 14:00 to Sunday 14:00 (48 hours).",
            "tier_2": "Add remaining time from Sunday 14:00 to 18:30 (4,5 hours).",
            "tier_3": "48 + 4,5 = 52,5 hours."
        }
    )

def _gen_time_schedule_bus_timetable(r: random.Random) -> Dict[str, Any]:
    duration_mins = 40
    ans = "40 minutes"
    timetable_md = (
        "| Bus Trip | Baragwanath (Dep) | Park Station | Sandton (Arr) |\n"
        "| :---: | :---: | :---: | :---: |\n"
        "| **Bus 1** | 06:15 | 06:55 | 07:35 |\n"
        "| **Bus 2** | 06:45 | 07:25 | 08:05 |"
    )
    prompt = (
        f"Refer to the commuter bus timetable below:\n\n"
        f"{timetable_md}\n\n"
        f"How long (in minutes) does **Bus 1** take to travel from **Baragwanath** to **Park Station**?"
    )
    sol = (
        f"**Step 1: Thought Process & Timetable Lookup**\\n"
        f"• Look up Bus 1 in the table:\\n"
        f"  - Departure from Baragwanath: **06:15**\\n"
        f"  - Arrival at Park Station: **06:55**\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Travel Time}} = 06:55 - 06:15 = 40\\\\text{{ minutes}}$$\\n"
        f"✓ [1 Mark: Method – subtracting departure time from arrival time]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Duration}} = \\\\mathbf{{40\\\\text{{ minutes}}}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct minutes with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_schedule_bus_timetable",
        prompt=prompt,
        answer=ans,
        sol=sol,
        rubric=["Method: 06:55 - 06:15 [1 Mark]", f"Accuracy: {ans} [1 Mark]"],
        hints={
            "tier_1": "Locate Bus 1 departure (06:15) and Park Station arrival (06:55).",
            "tier_2": "Subtract 15 minutes from 55 minutes: 55 - 15 = 40.",
            "tier_3": "40 minutes."
        }
    )

def _gen_time_schedule_train_flight(r: random.Random) -> Dict[str, Any]:
    dep_time = "09:40"
    gate_closes_mins = 30
    ans = "09:10"
    prompt = (
        f"A domestic flight from Johannesburg (OR Tambo) to Cape Town is scheduled to depart at **{dep_time}**.\n\n"
        f"Boarding gates close **{gate_closes_mins} minutes** before departure.\n\n"
        f"Determine the exact time when the boarding gate closes."
    )
    sol = (
        f"**Step 1: Thought Process & Time Subtraction**\\n"
        f"• Departure time: **09:40**\\n"
        f"• The gate closes 30 minutes earlier: subtract 30 minutes from 09:40.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Gate Closing Time}} = 09:40 - 30\\\\text{{ minutes}} = \\\\mathbf{{09:10}}$$\\n"
        f"✓ [1 Mark: Method – subtracting 30 minutes from 09:40]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Time}} = 09:10$$\\n"
        f"✓ [1 Mark: Accuracy – correct clock time in 24-hr format]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_schedule_train_flight",
        prompt=prompt,
        answer=ans,
        sol=sol,
        rubric=["Method: 09:40 - 30 minutes [1 Mark]", f"Accuracy: {ans} [1 Mark]"],
        hints={
            "tier_1": "Subtract 30 minutes from departure time (09:40).",
            "tier_2": "40 minutes - 30 minutes = 10 minutes past 9.",
            "tier_3": "09:10."
        }
    )

def _gen_time_tide_table_reading(r: random.Random) -> Dict[str, Any]:
    ht1_time = "04:18"
    ht1_height = 2.15
    lt1_time = "10:32"
    lt1_height = 0.42
    range_m = round(ht1_height - lt1_height, 2)
    ans = f"{_fmt(range_m)} m"
    tide_table_md = (
        "| Date | High Tide (Time / Height) | Low Tide (Time / Height) |\n"
        "| :---: | :---: | :---: |\n"
        f"| **14 Oct (Durban)** | {ht1_time} ({_fmt(ht1_height)} m) | {lt1_time} ({_fmt(lt1_height)} m) |"
    )
    prompt = (
        f"Refer to the coastal tide chart for Durban beach below:\n\n"
        f"{tide_table_md}\n\n"
        f"Calculate the **tidal range** (the difference in water height between high tide and low tide) in metres (**m**)."
    )
    sol = (
        f"**Step 1: Thought Process & Table Lookup**\\n"
        f"• High tide water height = {_fmt(ht1_height)} m\\n"
        f"• Low tide water height = {_fmt(lt1_height)} m\\n"
        f"• Tidal range = High Tide Height - Low Tide Height\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Tidal Range}} = {_fmt(ht1_height)}\\\\text{{ m}} - {_fmt(lt1_height)}\\\\text{{ m}} = \\\\mathbf{{{_fmt(range_m)}\\\\text{{ m}}}}$$\\n"
        f"✓ [1 Mark: Method – subtracting low tide height from high tide height]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Range}} = {_fmt(range_m)}\\\\text{{ m}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct tidal range with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_tide_table_reading",
        prompt=prompt,
        answer=ans,
        sol=sol,
        rubric=[f"Method: {_fmt(ht1_height)} - {_fmt(lt1_height)} [1 Mark]", f"Accuracy: {ans} [1 Mark]"],
        hints={
            "tier_1": f"Tidal range is High tide ({_fmt(ht1_height)} m) minus Low tide ({_fmt(lt1_height)} m).",
            "tier_2": f"Subtract: {_fmt(ht1_height)} - {_fmt(lt1_height)}.",
            "tier_3": f"{ans}."
        }
    )

def _gen_speed_distance_time_travel_duration(r: random.Random) -> Dict[str, Any]:
    speed = r.choice([80, 100, 120])
    hours = r.choice([2.5, 3.0, 3.5, 4.0])
    distance = int(speed * hours)
    ans = f"{_fmt(hours)} hours"
    prompt = (
        f"A motorist travels a distance of **{distance} km** on the N1 highway at a constant average speed of **{speed} km/h**.\n\n"
        f"Calculate the total travel time in hours."
    )
    sol = (
        f"**Step 1: Thought Process & Formula**\\n"
        f"• Formula: $\\\\text{{Time}} = \\\\frac{{\\\\text{{Distance}}}}{{\\\\text{{Speed}}}}$\\n"
        f"• Divide the total distance ({distance} km) by the average speed ({speed} km/h).\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Time}} = \\\\frac{{{distance}\\\\text{{ km}}}}{{{speed}\\\\text{{ km/h}}}} = \\\\mathbf{{{_fmt(hours)}\\\\text{{ hours}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing distance by speed]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Travel Time}} = {_fmt(hours)}\\\\text{{ hours}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct travel time with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="speed_distance_time_travel_duration",
        prompt=prompt,
        answer=ans,
        sol=sol,
        rubric=[f"Method: {distance} ÷ {speed} [1 Mark]", f"Accuracy: {ans} [1 Mark]"],
        hints={
            "tier_1": "Formula: Time = Distance ÷ Speed.",
            "tier_2": f"Divide {distance} by {speed}: {distance} ÷ {speed}.",
            "tier_3": f"{ans}."
        }
    )

def _gen_speed_unit_conversion_kmh_to_ms(r: random.Random) -> Dict[str, Any]:
    kmh = r.choice([36, 72, 90, 108, 126])
    ans_ms = round(kmh / 3.6, 1)
    ans = f"{_fmt(ans_ms)} m/s"
    prompt = (
        f"A vehicle travels on an urban road at a speed of **{kmh} km/h**.\n\n"
        f"Convert this speed to metres per second (**m/s**)."
    )
    sol = (
        f"**Step 1: Thought Process & Conversion Factor**\\n"
        f"• Derivation: $1\\\\text{{ km/h}} = \\\\frac{{1\\\\,000\\\\text{{ m}}}}{{3\\\\,600\\\\text{{ s}}}} = \\\\frac{{1}}{{3{{,}}6}}\\\\text{{ m/s}}$\\n"
        f"• To convert from km/h to m/s, divide the speed by $3{,}6$.\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Speed in m/s}} = \\\\frac{{{kmh}\\\\text{{ km/h}}}}{{3{{,}}6}} = \\\\mathbf{{{_fmt(ans_ms)}\\\\text{{ m/s}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing speed by 3,6]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Speed}} = {_fmt(ans_ms)}\\\\text{{ m/s}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct converted speed with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="speed_unit_conversion_kmh_to_ms",
        prompt=prompt,
        answer=ans,
        sol=sol,
        rubric=[f"Method: {kmh} ÷ 3,6 [1 Mark]", f"Accuracy: {ans} [1 Mark]"],
        hints={
            "tier_1": "To convert from km/h to m/s, divide by 3,6.",
            "tier_2": f"Divide {kmh} by 3,6: {kmh} ÷ 3,6.",
            "tier_3": f"{ans}."
        }
    )

def _gen_time_international_time_zones(r: random.Random) -> Dict[str, Any]:
    city, offset, desc = r.choice([
        ("London (UK)", -2, "2 hours behind South Africa"),
        ("New York (USA)", -7, "7 hours behind South Africa"),
        ("Sydney (Australia)", 8, "8 hours ahead of South Africa"),
        ("Dubai (UAE)", 2, "2 hours ahead of South Africa"),
    ])
    sa_h = r.choice([14, 15, 16, 17, 18])
    sa_m = 30
    other_h = (sa_h + offset) % 24
    ans = f"{other_h:02d}:{sa_m:02d}"
    prompt = (
        f"South Africa standard time is **UTC+2**.\n\n"
        f"A business executive in Johannesburg schedules a video conference at **{sa_h:02d}:{sa_m:02d}** SAST with colleagues in **{city}**, which is **{desc}**.\n\n"
        f"What local time will it be in {city} when the conference starts?"
    )
    sol = (
        f"**Step 1: Thought Process & Time Zone Offset**\\n"
        f"• South African meeting time: {sa_h:02d}:{sa_m:02d}\\n"
        f"• {city} is {desc} ({offset:+d} hours).\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Local Time}} = {sa_h:02d}:{sa_m:02d} {offset:+d}\\\\text{{ hours}} = \\\\mathbf{{{ans}}}$$\\n"
        f"✓ [1 Mark: Method – applying time zone offset]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Local Time in {city}}} = {ans}$$\\n"
        f"✓ [1 Mark: Accuracy – correct clock time in 24-hr notation]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_international_time_zones",
        prompt=prompt,
        answer=ans,
        sol=sol,
        rubric=[f"Method: {sa_h:02d}:{sa_m:02d} {offset:+d} hours [1 Mark]", f"Accuracy: {ans} [1 Mark]"],
        hints={
            "tier_1": f"{city} is {desc}.",
            "tier_2": f"Add {offset} hours to {sa_h:02d}:{sa_m:02d}.",
            "tier_3": f"{ans}."
        }
    )

def _gen_time_pace_speed_running(r: random.Random) -> Dict[str, Any]:
    km = r.choice([5, 10, 15, 21])
    pace_per_km = r.choice([4.5, 5.0, 5.5, 6.0])
    total_mins = round(km * pace_per_km, 1)
    ans = f"{_fmt(pace_per_km)} min/km"
    prompt = (
        f"A runner completes a **{km} km** community road race in a total time of **{_fmt(total_mins)} minutes**.\n\n"
        f"Calculate the runner's average pace in minutes per kilometre (**min/km**)."
    )
    sol = (
        f"**Step 1: Thought Process & Pace Formula**\\n"
        f"• Pace measures the time taken to cover one kilometre.\\n"
        f"• Formula: $\\\\text{{Pace}} = \\\\frac{{\\\\text{{Total Minutes}}}}{{\\\\text{{Total Kilometres}}}}$\\n\\n"
        f"**Step 2: Method & Calculation**\\n"
        f"$$\\\\text{{Pace}} = \\\\frac{{{_fmt(total_mins)}\\\\text{{ min}}}}{{{km}\\\\text{{ km}}}} = \\\\mathbf{{{_fmt(pace_per_km)}\\\\text{{ min/km}}}}$$\\n"
        f"✓ [1 Mark: Method – dividing total minutes by total kilometres]\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\text{{Final Average Pace}} = {_fmt(pace_per_km)}\\\\text{{ min/km}}$$\\n"
        f"✓ [1 Mark: Accuracy – correct pace with units]\\n\\n"
        f"**Total Marks: [2 Marks]**"
    )
    return _make_q(
        subskill="time_pace_speed_running",
        prompt=prompt,
        answer=ans,
        sol=sol,
        rubric=[f"Method: {_fmt(total_mins)} ÷ {km} [1 Mark]", f"Accuracy: {ans} [1 Mark]"],
        hints={
            "tier_1": "Pace = Total Minutes ÷ Total Kilometres.",
            "tier_2": f"Divide {_fmt(total_mins)} by {km}.",
            "tier_3": f"{ans}."
        }
    )


# ===========================================================================
# DISPATCHER MAP & TOP-LEVEL GENERATE FUNCTION
# ===========================================================================

GEN_MAP = {
    # Cluster 1: Length
    "conv_len_mm_to_cm": _gen_conv_len_mm_to_cm,
    "conv_len_cm_to_mm": _gen_conv_len_cm_to_mm,
    "conv_len_cm_to_m": _gen_conv_len_cm_to_m,
    "conv_len_m_to_cm": _gen_conv_len_m_to_cm,
    "conv_len_mm_to_m": _gen_conv_len_mm_to_m,
    "conv_len_m_to_mm": _gen_conv_len_m_to_mm,
    "conv_len_m_to_km": _gen_conv_len_m_to_km,
    "conv_len_km_to_m": _gen_conv_len_km_to_m,

    # Cluster 2: Mass
    "conv_mass_g_to_kg": _gen_conv_mass_g_to_kg,
    "conv_mass_kg_to_g": _gen_conv_mass_kg_to_g,
    "conv_mass_kg_to_tonne": _gen_conv_mass_kg_to_tonne,
    "conv_mass_tonne_to_kg": _gen_conv_mass_tonne_to_kg,
    "conv_mass_mg_to_g": _gen_conv_mass_mg_to_g,
    "conv_mass_g_to_mg": _gen_conv_mass_g_to_mg,
    "conv_mass_multi_step_tonne_to_g": _gen_conv_mass_multi_step_tonne_to_g,

    # Cluster 3: Volume
    "conv_vol_ml_to_l": _gen_conv_vol_ml_to_l,
    "conv_vol_l_to_ml": _gen_conv_vol_l_to_ml,
    "conv_vol_l_to_kl": _gen_conv_vol_l_to_kl,
    "conv_vol_kl_to_l": _gen_conv_vol_kl_to_l,
    "conv_vol_cm3_to_ml": _gen_conv_vol_cm3_to_ml,
    "conv_vol_cm3_to_l": _gen_conv_vol_cm3_to_l,
    "conv_vol_m3_to_l": _gen_conv_vol_m3_to_l,

    # Cluster 4: Kitchen Cooking
    "cook_tsp_to_ml": _gen_cook_tsp_to_ml,
    "cook_tbsp_to_ml": _gen_cook_tbsp_to_ml,
    "cook_tbsp_to_tsp": _gen_cook_tbsp_to_tsp,
    "cook_cups_to_ml": _gen_cook_cups_to_ml,
    "cook_recipe_scaling": _gen_cook_recipe_scaling,
    "cook_dry_cups_to_grams": _gen_cook_dry_cups_to_grams,

    # Cluster 5: Imperial
    "conv_imperial_inches_feet_to_cm_m": _gen_conv_imperial_inches_feet_to_cm_m,
    "conv_imperial_pounds_gallons_to_metric": _gen_conv_imperial_pounds_gallons_to_metric,

    # Cluster 6: Temperature
    "temp_celsius_to_fahrenheit": _gen_temp_celsius_to_fahrenheit,
    "temp_fahrenheit_to_celsius": _gen_temp_fahrenheit_to_celsius,
    "temp_baking_oven_setting": _gen_temp_baking_oven_setting,
    "temp_weather_comparison": _gen_temp_weather_comparison,
    "temp_negative_freezing_c_to_f": _gen_temp_negative_freezing_c_to_f,

    # Cluster 7: Time & Speed
    "time_unit_seconds_minutes": _gen_time_unit_seconds_minutes,
    "time_unit_minutes_hours": _gen_time_unit_minutes_hours,
    "time_unit_hours_days": _gen_time_unit_hours_days,
    "time_unit_days_weeks_months": _gen_time_unit_days_weeks_months,
    "time_format_12h_to_24h": _gen_time_format_12h_to_24h,
    "time_format_24h_to_12h": _gen_time_format_24h_to_12h,
    "time_decimal_to_hours_minutes": _gen_time_decimal_to_hours_minutes,
    "time_elapsed_same_day": _gen_time_elapsed_same_day,
    "time_elapsed_crossing_midnight": _gen_time_elapsed_crossing_midnight,
    "time_elapsed_multi_day": _gen_time_elapsed_multi_day,
    "time_schedule_bus_timetable": _gen_time_schedule_bus_timetable,
    "time_schedule_train_flight": _gen_time_schedule_train_flight,
    "time_tide_table_reading": _gen_time_tide_table_reading,
    "speed_distance_time_travel_duration": _gen_speed_distance_time_travel_duration,
    "speed_unit_conversion_kmh_to_ms": _gen_speed_unit_conversion_kmh_to_ms,
    "time_international_time_zones": _gen_time_international_time_zones,
    "time_pace_speed_running": _gen_time_pace_speed_running,
}


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    mode: str = "practice",
    seed: Optional[int] = None,
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Generates authentic questions across 52 distinct conversions & time archetypes."""
    actual_seed = seed if seed is not None else random.randint(1, 1_000_000_000)
    r = random.Random(actual_seed)

    questions: List[Dict[str, Any]] = []
    for i in range(count):
        step_seed = actual_seed + (i * 31)
        r_step = random.Random(step_seed)

        chosen = subskill
        if chosen in ("mixed", "auto", "", None) or chosen not in GEN_MAP:
            # Deterministic linear sequence based on seed
            idx = step_seed % len(SUBSKILLS)
            chosen = SUBSKILLS[idx]

        builder = GEN_MAP.get(chosen, _gen_conv_len_mm_to_cm)
        q = builder(r_step)
        q["seed"] = step_seed
        q["difficulty"] = difficulty
        q["mode"] = mode
        questions.append(q)

    return questions
'''

full_file = base_code + clusters_code
target_path = 'caps-ai-backend/app/utils/mathematical_literacy/conversions_time_generator.py'

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(full_file)

print(f"Successfully wrote full generator to {target_path}!")
print(f"Total lines: {len(full_file.splitlines())}")
