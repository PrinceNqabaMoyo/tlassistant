import sys

filepath = r'C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade11_accounting\term2\clubs_nonprofit_generator.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_gen = """def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "",
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    questions: List[Dict[str, Any]] = []

    for _ in range(count):
        gen = r.choice(_GENERATORS)
        q = gen(r)
        q["difficulty"] = difficulty
        q["mode"] = mode
        questions.append(q)

    return questions"""

new_gen = """def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "",
) -> List[Dict[str, Any]]:
    r = _rng(seed)
    questions: List[Dict[str, Any]] = []
    
    subskill_norm = str(subskill or "mixed").strip().lower()
    
    pool = _GENERATORS
    if subskill_norm == "receipts_payments_items":
        pool = [_gen_receipts_payments_items]

    for _ in range(count):
        gen = r.choice(pool)
        q = gen(r)
        q["difficulty"] = difficulty
        q["mode"] = mode
        questions.append(q)

    return questions"""

content = content.replace(old_gen, new_gen)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("patched clubs subskill filter")
