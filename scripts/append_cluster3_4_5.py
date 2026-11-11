# -*- coding: utf-8 -*-
"""Appends Clusters 3, 4, 5 to conversions_time_generator.py."""

from pathlib import Path

target = Path("caps-ai-backend/app/utils/mathematical_literacy/conversions_time_generator.py")

content = '''
# ==============================================================================
# CLUSTER 3: METRIC VOLUME & LIQUID CAPACITY (7 Archetypes)
# ==============================================================================

def _gen_conv_vol_ml_to_l(r: random.Random) -> Dict[str, Any]:
    val_ml = r.randint(250, 4800)
    ans_l = val_ml / 1000.0
    prompt = f"A bottle of fruit juice contains **{val_ml} ml** of beverage.\\n\\nConvert this liquid volume to litres (**l**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from millilitres (ml) to litres (l) moves from a smaller unit to a larger unit, requiring **division** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ l}} = 1\\\\ 000\\\\text{{ ml}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Volume in litres}} = \\\\frac{{{val_ml}\\\\text{{ ml}}}}{{1\\\\ 000}} = {_fmt(ans_l)}\\\\text{{ l}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ans_l)}\\\\text{{ l}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_vol_ml_to_l",
        prompt=prompt,
        answer=f"{_fmt(ans_l)} l",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 1 000", f"1 Mark: Accuracy – {_fmt(ans_l)} l"],
        hints={
            "tier_1": "There are 1 000 millilitres in 1 litre. Divide by 1 000.",
            "tier_2": f"Divide {val_ml} by 1 000.",
            "tier_3": f"{val_ml} ÷ 1 000 = {_fmt(ans_l)} l."
        },
        r=r
    )

def _gen_conv_vol_l_to_ml(r: random.Random) -> Dict[str, Any]:
    val_l = round(r.uniform(0.75, 5.5), 2)
    ans_ml = int(round(val_l * 1000))
    prompt = f"A car radiator requires **{_fmt(val_l)} l** of coolant mixture.\\n\\nConvert this coolant volume to millilitres (**ml**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from litres (l) to millilitres (ml) moves from a larger unit to a smaller unit, requiring **multiplication** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ l}} = 1\\\\ 000\\\\text{{ ml}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Volume in ml}} = {_fmt(val_l)}\\\\text{{ l}} \\\\times 1\\\\ 000 = {ans_ml}\\\\text{{ ml}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_ml}\\\\text{{ ml}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_vol_l_to_ml",
        prompt=prompt,
        answer=f"{ans_ml} ml",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 1 000", f"1 Mark: Accuracy – {ans_ml} ml"],
        hints={
            "tier_1": "1 litre = 1 000 millilitres. Multiply by 1 000.",
            "tier_2": f"Multiply {_fmt(val_l)} by 1 000.",
            "tier_3": f"{_fmt(val_l)} × 1 000 = {ans_ml} ml."
        },
        r=r
    )

def _gen_conv_vol_l_to_kl(r: random.Random) -> Dict[str, Any]:
    val_l = r.randint(1500, 28000)
    ans_kl = val_l / 1000.0
    prompt = f"A municipal household water meter records a monthly consumption of **{val_l} l**.\\n\\nConvert this water consumption to kilolitres (**kl**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from litres (l) to kilolitres (kl) moves to a larger unit, requiring **division** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ kl}} = 1\\\\ 000\\\\text{{ l}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Consumption in kl}} = \\\\frac{{{val_l}\\\\text{{ l}}}}{{1\\\\ 000}} = {_fmt(ans_kl)}\\\\text{{ kl}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ans_kl)}\\\\text{{ kl}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_vol_l_to_kl",
        prompt=prompt,
        answer=f"{_fmt(ans_kl)} kl",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 1 000", f"1 Mark: Accuracy – {_fmt(ans_kl)} kl"],
        hints={
            "tier_1": "There are 1 000 litres in 1 kilolitre. Divide by 1 000.",
            "tier_2": f"Divide {val_l} by 1 000.",
            "tier_3": f"{val_l} ÷ 1 000 = {_fmt(ans_kl)} kl."
        },
        r=r
    )

def _gen_conv_vol_kl_to_l(r: random.Random) -> Dict[str, Any]:
    val_kl = round(r.uniform(2.5, 24.0), 1)
    ans_l = int(round(val_kl * 1000))
    prompt = f"A farm JoJo water storage tank holds **{_fmt(val_kl)} kl** of rainwater.\\n\\nConvert this stored water capacity to litres (**l**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Converting from kilolitres (kl) to litres (l) moves to a smaller unit, requiring **multiplication** by 1 000.\\n"
        f"• Base relationship: $1\\\\text{{ kl}} = 1\\\\ 000\\\\text{{ l}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Capacity in litres}} = {_fmt(val_kl)}\\\\text{{ kl}} \\\\times 1\\\\ 000 = {ans_l}\\\\text{{ l}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_l}\\\\text{{ l}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_vol_kl_to_l",
        prompt=prompt,
        answer=f"{ans_l} l",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 1 000", f"1 Mark: Accuracy – {ans_l} l"],
        hints={
            "tier_1": "1 kilolitre = 1 000 litres. Multiply by 1 000.",
            "tier_2": f"Multiply {_fmt(val_kl)} by 1 000.",
            "tier_3": f"{_fmt(val_kl)} × 1 000 = {ans_l} l."
        },
        r=r
    )

def _gen_conv_vol_cm3_to_ml(r: random.Random) -> Dict[str, Any]:
    val_cm3 = r.randint(45, 850)
    ans_ml = val_cm3
    prompt = f"A rectangular science beaker displaces **{val_cm3} cm³** of water.\\n\\nConvert this internal volume to millilitres (**ml**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• In the metric system, liquid volume and spatial capacity share a direct 1-to-1 equivalence:\\n"
        f"  $1\\\\text{{ cm}}^3 = 1\\\\text{{ ml}}$\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Volume in ml}} = {val_cm3}\\\\text{{ cm}}^3 \\\\times 1 = {ans_ml}\\\\text{{ ml}}$$\\n"
        f"✓ **[1 Mark: Method – stating the 1-to-1 equivalence $1\\\\text{{ cm}}^3 = 1\\\\text{{ ml}}$]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_ml}\\\\text{{ ml}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_vol_cm3_to_ml",
        prompt=prompt,
        answer=f"{ans_ml} ml",
        sol=sol,
        rubric=["1 Mark: Method – 1 cm³ = 1 ml equivalence", f"1 Mark: Accuracy – {ans_ml} ml"],
        hints={
            "tier_1": "1 cubic centimetre (cm³) is exactly equal to 1 millilitre (ml).",
            "tier_2": f"The value remains unchanged: {val_cm3} cm³ = {ans_ml} ml.",
            "tier_3": f"{val_cm3} ml."
        },
        r=r
    )

def _gen_conv_vol_cm3_to_l(r: random.Random) -> Dict[str, Any]:
    val_cm3 = r.randint(650, 7500)
    ans_l = val_cm3 / 1000.0
    prompt = f"A car engine displacement or battery container has a volume of **{val_cm3} cm³**.\\n\\nConvert this capacity to litres (**l**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Since $1\\\\text{{ cm}}^3 = 1\\\\text{{ ml}}$ and $1\\\\text{{ l}} = 1\\\\ 000\\\\text{{ ml}}$, we have:\\n"
        f"  $1\\\\text{{ l}} = 1\\\\ 000\\\\text{{ cm}}^3$\\n"
        f"• Converting from cubic centimetres to litres requires **division** by 1 000.\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Volume in litres}} = \\\\frac{{{val_cm3}\\\\text{{ cm}}^3}}{{1\\\\ 000}} = {_fmt(ans_l)}\\\\text{{ l}}$$\\n"
        f"✓ **[1 Mark: Method – dividing by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ans_l)}\\\\text{{ l}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_vol_cm3_to_l",
        prompt=prompt,
        answer=f"{_fmt(ans_l)} l",
        sol=sol,
        rubric=["1 Mark: Method – dividing by 1 000", f"1 Mark: Accuracy – {_fmt(ans_l)} l"],
        hints={
            "tier_1": "There are 1 000 cm³ in 1 litre. Divide by 1 000.",
            "tier_2": f"Divide {val_cm3} by 1 000.",
            "tier_3": f"{val_cm3} ÷ 1 000 = {_fmt(ans_l)} l."
        },
        r=r
    )

def _gen_conv_vol_m3_to_l(r: random.Random) -> Dict[str, Any]:
    val_m3 = round(r.uniform(1.5, 35.0), 1)
    ans_l = int(round(val_m3 * 1000))
    prompt = f"A concrete swimming pool or garden pond contains **{_fmt(val_m3)} m³** of water.\\n\\nConvert this water volume to litres (**l**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• 1 cubic metre is equal to 1 000 litres ($1\\\\text{{ m}}^3 = 1\\\\ 000\\\\text{{ l}} = 1\\\\text{{ kl}}$).\\n"
        f"• Converting from cubic metres (m³) to litres (l) requires **multiplication** by 1 000.\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Volume in litres}} = {_fmt(val_m3)}\\\\text{{ m}}^3 \\\\times 1\\\\ 000 = {ans_l}\\\\text{{ l}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 1 000]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_l}\\\\text{{ l}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="conv_vol_m3_to_l",
        prompt=prompt,
        answer=f"{ans_l} l",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 1 000", f"1 Mark: Accuracy – {ans_l} l"],
        hints={
            "tier_1": "1 cubic metre (m³) holds exactly 1 000 litres. Multiply by 1 000.",
            "tier_2": f"Multiply {_fmt(val_m3)} by 1 000.",
            "tier_3": f"{_fmt(val_m3)} × 1 000 = {ans_l} l."
        },
        r=r
    )


# ==============================================================================
# CLUSTER 4: KITCHEN COOKING & RECIPE CONVERSIONS (6 Archetypes)
# ==============================================================================

def _gen_cook_tsp_to_ml(r: random.Random) -> Dict[str, Any]:
    tsp_count = r.randint(2, 8)
    ans_ml = tsp_count * 5
    prompt = f"A traditional recipe for koeksisters calls for **{tsp_count} teaspoons (tsp)** of ground cinnamon.\\n\\nConvert this quantity to millilitres (**ml**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• In South African cooking and Mathematical Literacy, standard metric measuring spoons are used:\\n"
        f"  $1\\\\text{{ teaspoon (tsp)}} = 5\\\\text{{ ml}}$\\n"
        f"• To find total millilitres, multiply the number of teaspoons by 5.\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Volume in ml}} = {tsp_count}\\\\text{{ tsp}} \\\\times 5 = {ans_ml}\\\\text{{ ml}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 5]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_ml}\\\\text{{ ml}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="cook_tsp_to_ml",
        prompt=prompt,
        answer=f"{ans_ml} ml",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 5", f"1 Mark: Accuracy – {ans_ml} ml"],
        hints={
            "tier_1": "Standard South African metric kitchen teaspoon = 5 ml.",
            "tier_2": f"Multiply {tsp_count} by 5.",
            "tier_3": f"{tsp_count} × 5 = {ans_ml} ml."
        },
        r=r
    )

def _gen_cook_tbsp_to_ml(r: random.Random) -> Dict[str, Any]:
    tbsp_count = r.randint(2, 6)
    ans_ml = tbsp_count * 15
    prompt = f"A recipe for malva pudding batter requires **{tbsp_count} tablespoons (tbsp)** of smooth apricot jam.\\n\\nDetermine the total volume of jam in millilitres (**ml**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Standard metric kitchen measuring spoon rule:\\n"
        f"  $1\\\\text{{ tablespoon (tbsp)}} = 15\\\\text{{ ml}}$\\n"
        f"• Multiply the number of tablespoons by 15.\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Volume in ml}} = {tbsp_count}\\\\text{{ tbsp}} \\\\times 15 = {ans_ml}\\\\text{{ ml}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 15]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_ml}\\\\text{{ ml}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value and unit]**"
    )
    return _make_q(
        subskill="cook_tbsp_to_ml",
        prompt=prompt,
        answer=f"{ans_ml} ml",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 15", f"1 Mark: Accuracy – {ans_ml} ml"],
        hints={
            "tier_1": "1 standard metric tablespoon equals 15 millilitres.",
            "tier_2": f"Multiply {tbsp_count} by 15.",
            "tier_3": f"{tbsp_count} × 15 = {ans_ml} ml."
        },
        r=r
    )

def _gen_cook_tbsp_to_tsp(r: random.Random) -> Dict[str, Any]:
    tbsp_count = r.randint(2, 5)
    ans_tsp = tbsp_count * 3
    prompt = f"A baker only has a 5 ml measuring teaspoon available, but the cake recipe specifies **{tbsp_count} tablespoons** of baking powder.\\n\\nHow many teaspoons must the baker measure out?"
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Understand the relationship between tablespoons and teaspoons:\\n"
        f"  $1\\\\text{{ tbsp}} = 15\\\\text{{ ml}}$ and $1\\\\text{{ tsp}} = 5\\\\text{{ ml}}$\\n"
        f"  $$\\\\frac{{15\\\\text{{ ml}}}}{{5\\\\text{{ ml}}}} = 3 \\\\implies 1\\\\text{{ tbsp}} = 3\\\\text{{ tsp}}$$\\n"
        f"• Multiply the required tablespoons by 3.\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Teaspoons}} = {tbsp_count} \\\\times 3 = {ans_tsp}\\\\text{{ tsp}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 3]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_tsp}\\\\text{{ tsp}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct number of teaspoons]**"
    )
    return _make_q(
        subskill="cook_tbsp_to_tsp",
        prompt=prompt,
        answer=f"{ans_tsp} tsp",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 3", f"1 Mark: Accuracy – {ans_tsp} tsp"],
        hints={
            "tier_1": "There are 3 teaspoons in 1 tablespoon (15 ml ÷ 5 ml = 3).",
            "tier_2": f"Multiply {tbsp_count} by 3.",
            "tier_3": f"{tbsp_count} × 3 = {ans_tsp} tsp."
        },
        r=r
    )

def _gen_cook_cups_to_ml(r: random.Random) -> Dict[str, Any]:
    cups = r.choice([1.5, 2.0, 2.5, 3.0, 3.5])
    ans_ml = int(cups * 250)
    prompt = f"A recipe for traditional vetkoek requires **{_fmt(cups)} metric cups** of fresh milk.\\n\\nCalculate the total volume of milk in millilitres (**ml**)."
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• In South African culinary standards, 1 standard metric cup is defined as:\\n"
        f"  $1\\\\text{{ metric cup}} = 250\\\\text{{ ml}}$\\n"
        f"• Multiply the number of metric cups by 250.\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Volume in ml}} = {_fmt(cups)} \\\\times 250 = {ans_ml}\\\\text{{ ml}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 250]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{ans_ml}\\\\text{{ ml}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct volume in ml]**"
    )
    return _make_q(
        subskill="cook_cups_to_ml",
        prompt=prompt,
        answer=f"{ans_ml} ml",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 250", f"1 Mark: Accuracy – {ans_ml} ml"],
        hints={
            "tier_1": "In South Africa, 1 standard metric cooking cup = 250 ml.",
            "tier_2": f"Multiply {_fmt(cups)} by 250.",
            "tier_3": f"{_fmt(cups)} × 250 = {ans_ml} ml."
        },
        r=r
    )

def _gen_cook_recipe_scaling(r: random.Random) -> Dict[str, Any]:
    base_servings = 4
    target_servings = r.choice([8, 12, 16])
    scale_factor = target_servings // base_servings
    base_sugar_g = r.choice([150, 200, 250])
    target_sugar_g = base_sugar_g * scale_factor
    prompt = f"A dessert recipe makes **{base_servings} servings** and requires **{base_sugar_g} g** of sugar.\\n\\nCalculate the mass of sugar (in grams) required to prepare **{target_servings} servings**."
    sol = (
        f"**Step 1: Scaling Multiplier & Thought Process**\\n"
        f"• Find the scale factor by dividing target servings by base recipe servings:\\n"
        f"  $$\\\\text{{Scale Factor}} = \\\\frac{{{target_servings}}}{{{base_servings}}} = {scale_factor}$$\\n"
        f"✓ **[1 Mark: Method – calculating scale factor]**\\n\\n"
        f"**Step 2: Method Setup & Ingredient Calculation**\\n"
        f"$$\\\\text{{Sugar Required}} = {base_sugar_g}\\\\text{{ g}} \\\\times {scale_factor} = {target_sugar_g}\\\\text{{ g}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying base quantity by scale factor]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{target_sugar_g}\\\\text{{ g}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – final mass of sugar in grams]**"
    )
    return _make_q(
        subskill="cook_recipe_scaling",
        prompt=prompt,
        answer=f"{target_sugar_g} g",
        sol=sol,
        rubric=[
            f"1 Mark: Method – {target_servings} ÷ {base_servings} = {scale_factor}",
            f"1 Mark: Method – {base_sugar_g} g × {scale_factor}",
            f"1 Mark: Accuracy – {target_sugar_g} g"
        ],
        hints={
            "tier_1": f"Find how many times larger the batch is: {target_servings} ÷ {base_servings}.",
            "tier_2": f"Multiply {base_sugar_g} g by {scale_factor}.",
            "tier_3": f"{base_sugar_g} × {scale_factor} = {target_sugar_g} g."
        },
        total_marks=3,
        r=r
    )

def _gen_cook_dry_cups_to_grams(r: random.Random) -> Dict[str, Any]:
    ingredient, grams_per_cup = r.choice([
        ("cake flour", 120),
        ("white sugar", 200),
        ("brown sugar", 180),
        ("rolled oats", 90),
        ("cocoa powder", 100),
    ])
    cups = r.choice([1.5, 2.0, 2.5, 3.0])
    total_g = int(cups * grams_per_cup)
    prompt = (
        f"A baking recipe conversion chart specifies:\\n\\n"
        f"| Ingredient | 1 Metric Cup Equivalent Mass |\\n"
        f"| :--- | :--- |\\n"
        f"| **{ingredient.title()}** | **{grams_per_cup} g** |\\n\\n"
        f"Calculate the total mass in grams (**g**) of **{_fmt(cups)} metric cups** of {ingredient}."
    )
    sol = (
        f"**Step 1: Reading Chart & Thought Process**\\n"
        f"• From the table, 1 metric cup of {ingredient} has a mass of {grams_per_cup} g.\\n"
        f"• To find the total mass for {_fmt(cups)} cups, multiply by {grams_per_cup}.\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Total Mass}} = {_fmt(cups)} \\\\times {grams_per_cup}\\\\text{{ g}} = {total_g}\\\\text{{ g}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying {_fmt(cups)} by {grams_per_cup}]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{total_g}\\\\text{{ g}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct mass in grams]**"
    )
    return _make_q(
        subskill="cook_dry_cups_to_grams",
        prompt=prompt,
        answer=f"{total_g} g",
        sol=sol,
        rubric=[f"1 Mark: Method – {_fmt(cups)} × {grams_per_cup} g", f"1 Mark: Accuracy – {total_g} g"],
        hints={
            "tier_1": f"According to the chart, 1 cup of {ingredient} = {grams_per_cup} g.",
            "tier_2": f"Multiply {_fmt(cups)} by {grams_per_cup}.",
            "tier_3": f"{_fmt(cups)} × {grams_per_cup} = {total_g} g."
        },
        r=r
    )


# ==============================================================================
# CLUSTER 5: IMPERIAL TO METRIC CONTEXTS (2 Archetypes)
# ==============================================================================

def _gen_conv_imperial_inches_feet_to_cm_m(r: random.Random) -> Dict[str, Any]:
    inches = r.choice([24, 32, 40, 50, 55, 65])
    ans_cm = round(inches * 2.54, 1)
    prompt = (
        f"A television monitor imported from the United States has a diagonal screen size of **{inches} inches**.\\n\\n"
        f"Given the imperial conversion factor: **1 inch = 2,54 cm**, calculate the screen size in centimetres (**cm**). "
        f"Round your answer to one decimal place."
    )
    sol = (
        f"**Step 1: Conversion Factor & Thought Process**\\n"
        f"• The conversion factor given is $1\\\\text{{ inch}} = 2{,}54\\\\text{{ cm}}$.\\n"
        f"• Multiply the number of inches by 2,54.\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Size in cm}} = {inches} \\\\times 2{,}54 = {_fmt(ans_cm)}\\\\text{{ cm}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 2,54]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ans_cm)}\\\\text{{ cm}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct value to 1 decimal place]**"
    )
    return _make_q(
        subskill="conv_imperial_inches_feet_to_cm_m",
        prompt=prompt,
        answer=f"{_fmt(ans_cm)} cm",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 2,54", f"1 Mark: Accuracy – {_fmt(ans_cm)} cm"],
        hints={
            "tier_1": "1 inch = 2,54 cm.",
            "tier_2": f"Multiply {inches} by 2,54.",
            "tier_3": f"{inches} × 2,54 = {_fmt(ans_cm)} cm."
        },
        r=r
    )

def _gen_conv_imperial_pounds_gallons_to_metric(r: random.Random) -> Dict[str, Any]:
    lbs = r.choice([15, 20, 25, 30, 45, 50])
    ans_kg = round(lbs * 0.454, 2)
    prompt = (
        f"An imported pet food bag displays a gross weight of **{lbs} pounds (lb)**.\\n\\n"
        f"Given that **1 pound (lb) = 0,454 kg**, calculate the mass of the pet food bag in kilograms (**kg**). "
        f"Round your answer to two decimal places."
    )
    sol = (
        f"**Step 1: Conversion Factor & Thought Process**\\n"
        f"• Conversion factor provided: $1\\\\text{{ lb}} = 0{,}454\\\\text{{ kg}}$.\\n"
        f"• Multiply pounds by 0,454 to convert to kilograms.\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$\\\\text{{Mass in kg}} = {lbs} \\\\times 0{,}454 = {_fmt(ans_kg)}\\\\text{{ kg}}$$\\n"
        f"✓ **[1 Mark: Method – multiplying by 0,454]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(ans_kg)}\\\\text{{ kg}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct mass to 2 decimal places]**"
    )
    return _make_q(
        subskill="conv_imperial_pounds_gallons_to_metric",
        prompt=prompt,
        answer=f"{_fmt(ans_kg)} kg",
        sol=sol,
        rubric=["1 Mark: Method – multiplying by 0,454", f"1 Mark: Accuracy – {_fmt(ans_kg)} kg"],
        hints={
            "tier_1": "1 pound (lb) equals 0,454 kg.",
            "tier_2": f"Multiply {lbs} by 0,454.",
            "tier_3": f"{lbs} × 0,454 = {_fmt(ans_kg)} kg."
        },
        r=r
    )
'''

with open(target, "a", encoding="utf-8") as f:
    f.write(content)

print("Clusters 3, 4, 5 appended successfully.")
