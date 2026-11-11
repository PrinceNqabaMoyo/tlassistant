sample_q = {
    'id': 'test_1',
    'question_text': 'Name three cell organelles and their functions.',
    'expected_answer': 'Nucleus, mitochondria, ribosomes',
}

canonical_prompt = str(
    sample_q.get("prompt")
    or sample_q.get("question")
    or sample_q.get("question_text")
    or sample_q.get("stem")
    or sample_q.get("context")
    or ""
).strip()

normalized = {
    **sample_q,
    "prompt": canonical_prompt,
    "question": canonical_prompt,
}

assert normalized.get("prompt") == 'Name three cell organelles and their functions.'
assert normalized.get("question") == 'Name three cell organelles and their functions.'
print("Prompt normalization logic verified!")
