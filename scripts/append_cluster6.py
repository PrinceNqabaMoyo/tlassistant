# -*- coding: utf-8 -*-
"""Appends Cluster 6 (Temperature) to conversions_time_generator.py."""

from pathlib import Path

target = Path("caps-ai-backend/app/utils/mathematical_literacy/conversions_time_generator.py")

content = '''
# ==============================================================================
# CLUSTER 6: TEMPERATURE CONVERSIONS (5 Archetypes)
# ==============================================================================

def _gen_temp_celsius_to_fahrenheit(r: random.Random) -> Dict[str, Any]:
    celsius = r.choice([15, 20, 25, 30, 35, 180, 200])
    fahrenheit = round((celsius * 1.8) + 32, 1)
    prompt = (
        f"A weather broadcast indicates an afternoon temperature of **{celsius} °C**.\\n\\n"
        f"Calculate the equivalent temperature in degrees Fahrenheit (**°F**)."
    )
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Target: Convert temperature from Celsius (°C) to Fahrenheit (°F).\\n"
        f"• Standard Formula: $^\\\\circ\\\\text{{F}} = (^\\\\circ\\\\text{{C}} \\\\times 1{{,}}8) + 32$\\n"
        f"• Thought process: First multiply the Celsius temperature by 1,8, then add the 32 offset.\\n\\n"
        f"**Step 2: Method Setup & Substitution**\\n"
        f"$$^\\\\circ\\\\text{{F}} = ({celsius} \\\\times 1{{,}}8) + 32 = {round(celsius * 1.8, 1)} + 32$$\\n"
        f"✓ **[1 Mark: Method – correct formula substitution]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(fahrenheit)}\\\\ ^\\\\circ\\\\text{{F}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct temperature in °F]**"
    )
    return _make_q(
        subskill="temp_celsius_to_fahrenheit",
        prompt=prompt,
        answer=f"{_fmt(fahrenheit)} °F",
        sol=sol,
        rubric=["1 Mark: Method – multiply by 1,8 and add 32", f"1 Mark: Accuracy – {_fmt(fahrenheit)} °F"],
        hints={
            "tier_1": "Standard Temperature Formula: °F = (°C × 1,8) + 32.",
            "tier_2": f"Multiply {celsius} by 1,8, then add 32.",
            "tier_3": f"({celsius} × 1,8) + 32 = {round(celsius * 1.8, 1)} + 32 = {_fmt(fahrenheit)} °F."
        },
        r=r
    )

def _gen_temp_fahrenheit_to_celsius(r: random.Random) -> Dict[str, Any]:
    fahrenheit = r.choice([68, 77, 86, 95, 350, 400])
    celsius = round((fahrenheit - 32) / 1.8, 1)
    prompt = (
        f"An American online recipe instructs you to preheat the oven to **{fahrenheit} °F**.\\n\\n"
        f"Calculate the required oven temperature in degrees Celsius (**°C**). Round to one decimal place."
    )
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Target: Convert temperature from Fahrenheit (°F) to Celsius (°C).\\n"
        f"• Standard Formula: $^\\\\circ\\\\text{{C}} = (^\\\\circ\\\\text{{F}} - 32) \\\\div 1{{,}}8$\\n"
        f"• Thought process: First subtract the 32 offset, then divide by 1,8.\\n\\n"
        f"**Step 2: Method Setup & Substitution**\\n"
        f"$$^\\\\circ\\\\text{{C}} = ({fahrenheit} - 32) \\\\div 1{{,}}8 = {fahrenheit - 32} \\\\div 1{{,}}8$$\\n"
        f"✓ **[1 Mark: Method – subtracting 32 and dividing by 1,8]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(celsius)}\\\\ ^\\\\circ\\\\text{{C}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct temperature in °C]**"
    )
    return _make_q(
        subskill="temp_fahrenheit_to_celsius",
        prompt=prompt,
        answer=f"{_fmt(celsius)} °C",
        sol=sol,
        rubric=["1 Mark: Method – subtract 32 and divide by 1,8", f"1 Mark: Accuracy – {_fmt(celsius)} °C"],
        hints={
            "tier_1": "Standard Temperature Formula: °C = (°F - 32) ÷ 1,8.",
            "tier_2": f"Subtract 32 from {fahrenheit}, then divide by 1,8.",
            "tier_3": f"({fahrenheit} - 32) ÷ 1,8 = {fahrenheit - 32} ÷ 1,8 = {_fmt(celsius)} °C."
        },
        r=r
    )

def _gen_temp_baking_oven_setting(r: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A baking recipe specifies an oven setting of **350 °F** for baking rusks.\\n\\n"
        f"Calculate the equivalent setting in °C and select the most appropriate oven temperature setting on a standard South African electric stove dial:\\n\\n"
        f"A. 140 °C\\n"
        f"B. 160 °C\\n"
        f"C. 180 °C\\n"
        f"D. 220 °C"
    )
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Convert 350 °F to °C using the standard formula:\\n"
        f"  $$^\\\\circ\\\\text{{C}} = (350 - 32) \\\\div 1{{,}}8 = 318 \\\\div 1{{,}}8 = 176{{,}}67\\\\ ^\\\\circ\\\\text{{C}}$$\\n"
        f"✓ **[1 Mark: Method – converting 350 °F to approximately 177 °C]**\\n\\n"
        f"**Step 2: Practical Stove Setting Selection**\\n"
        f"• South African electric stove dials have markings typically in 20 °C intervals (140 °C, 160 °C, 180 °C, 200 °C).\\n"
        f"• 176,67 °C rounds to the nearest dial mark of **180 °C**.\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{180\\\\ ^\\\\circ\\\\text{{C}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – selecting 180 °C]**"
    )
    return _make_q(
        subskill="temp_baking_oven_setting",
        prompt=prompt,
        answer="180 °C",
        sol=sol,
        rubric=["1 Mark: Method – (350 - 32) ÷ 1,8 ≈ 176,7 °C", "1 Mark: Accuracy – selecting 180 °C"],
        hints={
            "tier_1": "Formula: °C = (°F - 32) ÷ 1,8. Then round to the nearest stove dial increment (180 °C).",
            "tier_2": "(350 - 32) ÷ 1,8 = 318 ÷ 1,8 = 176,67 °C.",
            "tier_3": "176,67 °C is closest to 180 °C."
        },
        options=["140 °C", "160 °C", "180 °C", "220 °C"],
        r=r
    )

def _gen_temp_weather_comparison(r: random.Random) -> Dict[str, Any]:
    c_sa = r.randint(28, 38)
    f_us = r.randint(80, 105)
    f_sa = round((c_sa * 1.8) + 32, 1)
    diff = round(abs(f_sa - f_us), 1)

    if f_sa > f_us:
        warmer_city = "Durban"
        colder_city = "Phoenix (USA)"
        diff_text = f"Durban was warmer by {_fmt(diff)} °F"
    elif f_us > f_sa:
        warmer_city = "Phoenix (USA)"
        colder_city = "Durban"
        diff_text = f"Phoenix (USA) was warmer by {_fmt(diff)} °F"
    else:
        warmer_city = "Both"
        colder_city = "Neither"
        diff_text = "Both cities had the same temperature"

    prompt = (
        f"On a summer day, Durban records a maximum temperature of **{c_sa} °C**, while Phoenix (USA) records **{f_us} °F**.\\n\\n"
        f"Determine which city was warmer and by how many degrees Fahrenheit (**°F**)."
    )
    sol = (
        f"**Step 1: Convert Durban's Temperature to °F**\\n"
        f"• Formula: $^\\\\circ\\\\text{{F}} = (^\\\\circ\\\\text{{C}} \\\\times 1{{,}}8) + 32$\\n"
        f"• Calculation: $^\\\\circ\\\\text{{F}} = ({c_sa} \\\\times 1{{,}}8) + 32 = {_fmt(f_sa)}\\\\ ^\\\\circ\\\\text{{F}}$\\n"
        f"✓ **[1 Mark: Method – converting Celsius to Fahrenheit]**\\n\\n"
        f"**Step 2: Comparison & Difference**\\n"
        f"• Durban: {_fmt(f_sa)} °F\\n"
        f"• Phoenix: {f_us} °F\\n"
        f"• Difference: $|{_fmt(f_sa)} - {f_us}| = {_fmt(diff)}\\\\ ^\\\\circ\\\\text{{F}}$\\n"
        f"✓ **[1 Mark: Method – calculating difference]**\\n\\n"
        f"**Step 3: Final Conclusion**\\n"
        f"**{diff_text}**.\\n"
        f"✓ **[1 Mark: Accuracy – correct city and temperature difference]**"
    )

    opt_correct = diff_text
    opt_inverted = f"{colder_city} was warmer by {_fmt(diff)} °F"
    opt_alt_diff = f"{warmer_city} was warmer by {_fmt(round(diff + 4.5, 1))} °F"
    opt_same = f"Both cities recorded the same temperature ({f_us} °F)"
    options = [opt_correct, opt_inverted, opt_alt_diff, opt_same]

    return _make_q(
        subskill="temp_weather_comparison",
        prompt=prompt,
        answer=diff_text,
        sol=sol,
        rubric=[
            f"1 Mark: Method – Durban in °F = ({c_sa} × 1,8) + 32 = {_fmt(f_sa)} °F",
            f"1 Mark: Method – Difference = |{_fmt(f_sa)} - {f_us}| = {_fmt(diff)} °F",
            f"1 Mark: Accuracy – {diff_text}"
        ],
        hints={
            "tier_1": f"Convert Durban's {c_sa} °C to °F using: ({c_sa} × 1,8) + 32.",
            "tier_2": f"Durban = {_fmt(f_sa)} °F. Now compare with Phoenix ({f_us} °F).",
            "tier_3": f"{diff_text}."
        },
        options=options,
        total_marks=3,
        r=r
    )

def _gen_temp_negative_freezing_c_to_f(r: random.Random) -> Dict[str, Any]:
    c_neg = r.choice([-5, -10, -15, -20])
    f_ans = round((c_neg * 1.8) + 32, 1)
    prompt = (
        f"An industrial deep-freeze unit in an abattoir operates at **{c_neg} °C**.\\n\\n"
        f"Calculate this freezing temperature in degrees Fahrenheit (**°F**)."
    )
    sol = (
        f"**Step 1: Conversion Principle & Thought Process**\\n"
        f"• Target: Convert negative Celsius temperature to Fahrenheit.\\n"
        f"• Standard Formula: $^\\\\circ\\\\text{{F}} = (^\\\\circ\\\\text{{C}} \\\\times 1{{,}}8) + 32$\\n"
        f"• Notice: Multiplying a negative number by 1,8 produces a negative result, which is then added to +32.\\n\\n"
        f"**Step 2: Method Setup & Calculation**\\n"
        f"$$^\\\\circ\\\\text{{F}} = ({c_neg} \\\\times 1{{,}}8) + 32 = {round(c_neg * 1.8, 1)} + 32 = {_fmt(f_ans)}\\\\ ^\\\\circ\\\\text{{F}}$$\\n"
        f"✓ **[1 Mark: Method – correct substitution with negative value]**\\n\\n"
        f"**Step 3: Final Answer**\\n"
        f"$$\\\\mathbf{{{_fmt(f_ans)}\\\\ ^\\\\circ\\\\text{{F}}}}$$\\n"
        f"✓ **[1 Mark: Accuracy – correct evaluation of {_fmt(f_ans)} °F]**"
    )
    ans_label = f"{_fmt(f_ans)} °F"
    opt_pos = f"{_fmt(round((abs(c_neg) * 1.8) + 32, 1))} °F"
    opt_sub_err = f"{_fmt(round(f_ans - 9, 1))} °F"
    opt_mult_err = f"{_fmt(round(f_ans + 18, 1))} °F"
    options = [ans_label, opt_pos, opt_sub_err, opt_mult_err]

    return _make_q(
        subskill="temp_negative_freezing_c_to_f",
        prompt=prompt,
        answer=ans_label,
        sol=sol,
        rubric=[f"1 Mark: Method – ({c_neg} × 1,8) + 32", f"1 Mark: Accuracy – {ans_label}"],
        hints={
            "tier_1": "Formula: °F = (°C × 1,8) + 32. Be mindful of the negative sign.",
            "tier_2": f"({c_neg} × 1,8) = {round(c_neg * 1.8, 1)}. Now add 32.",
            "tier_3": f"{round(c_neg * 1.8, 1)} + 32 = {ans_label}."
        },
        options=options,
        r=r
    )
'''

with open(target, "a", encoding="utf-8") as f:
    f.write(content)

print("Cluster 6 appended successfully.")
