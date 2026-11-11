with open('caps-ai-backend/app/utils/grade8_mathematics/measurement_3d_generator.py', 'r', encoding='utf-8') as f:
    text = f.read()

subskills_def = """
SUBSKILLS = [
    "rectangular_prism_sa_vol",
    "triangular_prism_sa_vol",
    "cube_sa_vol",
    "unit_conversion_capacity",
    "compound_container_problem",
]
"""

cube_fn = """
def generate_cube(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    s = r.randint(4, 15)
    vol = s ** 3
    sa = 6 * (s ** 2)
    prompt = (
        f"A cube-shaped storage box has sides of length \\(s = {s}\\text{{ cm}}\\).\\n\\n"
        f"1. State the formula for the total surface area of a cube.\\n"
        f"2. Calculate the total surface area in \\(\\text{{cm}}^2\\).\\n"
        f"3. State the formula for the volume of a cube.\\n"
        f"4. Calculate the volume of the box in \\(\\text{{cm}}^3\\)."
    )
    sol = (
        f"**Step 1:** Surface area formula: \\(SA = 6s^2\\)\\n\\n"
        f"**Step 2:** \\(SA = 6({s})^2 = 6({s*s}) = {sa}\\text{{ cm}}^2\\)\\n\\n"
        f"**Step 3:** Volume formula: \\(V = s^3\\)\\n\\n"
        f"**Step 4:** \\(V = ({s})^3 = {vol}\\text{{ cm}}^3\\)"
    )
    ans = f"1. SA = 6s^2; 2. SA = {sa} cm^2; 3. V = s^3; 4. V = {vol} cm^3"
    return {
        "id": f"g8_meas_cube_{r.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "cube_sa_vol",
        "learning_objective_id": f"{LO}_cube",
        "prompt": prompt,
        "question": prompt,
        "sample_answer": ans,
        "correct_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "hints": {
            "tier_1": "A cube has 6 identical square faces.",
            "tier_2": "SA = 6s^2 and Volume = s^3.",
            "tier_3": f"SA = {sa} cm^2, V = {vol} cm^3.",
        },
        "misconception_tags": ["cubing_side_instead_of_squaring_in_surface_area"],
    }

def generate_unit_conversion(r: random.Random, mode: str = "compound") -> Dict[str, Any]:
    litres = r.choice([1.5, 2.0, 2.5, 3.5, 5.0, 8.0, 10.0])
    cm3 = int(litres * 1000)
    ml = cm3
    prompt = (
        f"A container holds \\({litres}\\text{{ litres}}\\) of water.\\n\\n"
        f"1. Convert this volume into millilitres (\\(\\text{{ml}}\\)), given that \\(1\\text{{ litre}} = 1\\,000\\text{{ ml}}\\).\\n"
        f"2. State the volume in cubic centimetres (\\(\\text{{cm}}^3\\)), given that \\(1\\text{{ ml}} = 1\\text{{ cm}}^3\\)."
    )
    sol = (
        f"**Step 1:** \\({litres} \\times 1\\,000 = {ml}\\text{{ ml}}\\)\\n\\n"
        f"**Step 2:** Since \\(1\\text{{ ml}} = 1\\text{{ cm}}^3\\), the volume is \\({cm3}\\text{{ cm}}^3\\)."
    )
    ans = f"1. {ml} ml; 2. {cm3} cm^3"
    return {
        "id": f"g8_meas_conv_{r.randint(100000, 999999)}",
        "topic": TOPIC,
        "subskill": "unit_conversion_capacity",
        "learning_objective_id": f"{LO}_conversion",
        "prompt": prompt,
        "question": prompt,
        "sample_answer": ans,
        "correct_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Multiply litres by 1000 to convert to ml.",
            "tier_2": "1 ml equals 1 cm^3.",
            "tier_3": f"Answers: {ans}.",
        },
        "misconception_tags": ["confused_litres_to_cm3_conversion_factor"],
    }
"""

new_generate_fn = """
def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
    subskill: Optional[str] = None,
    **kwargs
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    sub_str = str(subskill or "").lower()
    questions = []

    for _ in range(count):
        if "triangular" in sub_str or "subskill_2" in sub_str:
            q = generate_triangular_prism(r, mode=mode)
            q["subskill"] = "triangular_prism_sa_vol"
        elif "cube" in sub_str or "subskill_3" in sub_str:
            q = generate_cube(r, mode=mode)
        elif "conversion" in sub_str or "capacity" in sub_str or "subskill_4" in sub_str:
            q = generate_unit_conversion(r, mode=mode)
        else:
            q = generate_rectangular_prism(r, mode=mode)
            q["subskill"] = "rectangular_prism_sa_vol"
        if "question" not in q:
            q["question"] = q.get("prompt", "")
        questions.append(q)

    return questions
"""

# Replace old generate function
old_gen = text[text.find("def generate("):]
text = text[:text.find("def generate(")] + subskills_def + cube_fn + new_generate_fn

with open('caps-ai-backend/app/utils/grade8_mathematics/measurement_3d_generator.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Upgraded measurement_3d_generator.py successfully!")
