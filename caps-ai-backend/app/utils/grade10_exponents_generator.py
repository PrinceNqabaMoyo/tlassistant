import random
import time
from typing import Any, Dict, List, Optional


TOPIC = 'grade10_exponents'


def _make_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"


def _make_typed(*, prompt: str, correct_answer: str, explanation: str, **extra) -> Dict[str, Any]:
    return {
        'question_type': 'typed',
        'question': prompt,
        'correct_answer': str(correct_answer),
        'explanation': explanation,
        **extra,
    }


def _make_mcq(*, prompt: str, options: List[str], correct_answer: str, explanation: str, **extra) -> Dict[str, Any]:
    return {
        'question_type': 'mcq',
        'question': prompt,
        'options': [str(o) for o in options],
        'correct_answer': str(correct_answer),
        'explanation': explanation,
        **extra,
    }


def _make_scaffold(
    *,
    prompt: str,
    steps: List[str],
    checkpoints: List[Dict[str, Any]],
    final_answer: str,
    explanation: str,
    **extra,
) -> Dict[str, Any]:
    return {
        'question_type': 'scaffold',
        'question': prompt,
        'steps': steps,
        'checkpoints': checkpoints,
        'correct_answer': str(final_answer),
        'explanation': explanation,
        **extra,
    }


def _validate_question(q: Dict[str, Any]) -> None:
    required = {'id', 'topic', 'subskill', 'difficulty', 'question_type', 'question', 'correct_answer', 'explanation'}
    missing = [k for k in required if k not in q]
    if missing:
        raise ValueError(f"Missing required keys: {missing}")

    if q['question_type'] not in {'typed', 'mcq', 'scaffold'}:
        raise ValueError('Invalid question_type')

    if q['question_type'] == 'mcq':
        if not isinstance(q.get('options'), list) or len(q.get('options', [])) < 2:
            raise ValueError('MCQ must include options list')
        if str(q['correct_answer']) not in [str(o) for o in q.get('options', [])]:
            raise ValueError('MCQ correct_answer must be one of options')

    if q['question_type'] == 'scaffold':
        if not isinstance(q.get('steps'), list) or len(q.get('steps', [])) < 1:
            raise ValueError('Scaffold must include steps')
        if not isinstance(q.get('checkpoints'), list) or len(q.get('checkpoints', [])) < 1:
            raise ValueError('Scaffold must include checkpoints')


def _unique_options(options: List[str], *, correct: str, rng: random.Random, min_len: int = 4) -> List[str]:
    unique: List[str] = []
    for o in options:
        s = str(o)
        if s not in unique:
            unique.append(s)

    if str(correct) not in unique:
        unique.append(str(correct))

    while len(unique) < min_len:
        unique.append(str(correct))
        unique = list(dict.fromkeys(unique))

    rng.shuffle(unique)
    return unique


def _root_symbol(n: int, radicand: str) -> str:
    if n == 2:
        return f"√{radicand}"
    if n == 3:
        return f"∛{radicand}"
    return f"{n}√{radicand}"


def _format_rational_as_power(base: str, m: int, n: int) -> str:
    # Prefer showing rational exponent with parentheses so renderMathText can show superscript cleanly
    return f"{base}^({m}/{n})"


def _format_rational_as_root(base: str, m: int, n: int) -> str:
    root = _root_symbol(n, base)
    if m == 1:
        return root
    return f"({root})^{m}"


def _gen_product_same_base(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 7, 10])
    m = rng.randint(1, 4 if difficulty == 'easy' else 6)
    n = rng.randint(1, 4 if difficulty == 'easy' else 6)

    prompt = f"Simplify: {base}^{m} × {base}^{n}"
    correct = f"{base}^{m + n}"
    explanation = f"Same base → add exponents: {base}^{m}×{base}^{n}={base}^({m}+{n})={base}^{m + n}."

    if qtype == 'mcq':
        options = _unique_options(
            [correct, f"{base}^{m * n}", f"{base}^{abs(m - n)}", f"{base}^{m + n + 1}"],
            correct=correct,
            rng=rng,
        )
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Check the bases match.', 'Add the exponents.', 'Keep the base.']
        checkpoints = [
            {
                'id': 'cp_add',
                'kind': 'typed',
                'prompt': f"Add exponents: {m} + {n} = ?",
                'correct_answer': str(m + n),
                'explanation': 'Add the exponents.',
            },
            {
                'id': 'cp_final',
                'kind': 'typed',
                'prompt': 'Write the simplified expression.',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_quotient_same_base(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 7, 10])
    m = rng.randint(2, 7 if difficulty == 'easy' else 9)
    n = rng.randint(1, 6 if difficulty == 'easy' else 8)

    if difficulty == 'easy' and m < n:
        m, n = n, m

    prompt = f"Simplify: {base}^{m} ÷ {base}^{n}"
    correct = f"{base}^{m - n}"
    explanation = f"Same base → subtract exponents: {base}^{m}÷{base}^{n}={base}^({m}−{n})={base}^{m - n}."

    if qtype == 'mcq':
        options = _unique_options(
            [correct, f"{base}^{m + n}", f"{base}^{m * n}", f"{base}^{abs(m - n)}"],
            correct=correct,
            rng=rng,
        )
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Check the bases match.', 'Subtract the exponents.', 'Keep the base.']
        checkpoints = [
            {
                'id': 'cp_sub',
                'kind': 'typed',
                'prompt': f"Subtract exponents: {m} − {n} = ?",
                'correct_answer': str(m - n),
                'explanation': 'Subtract the exponents.',
            },
            {
                'id': 'cp_final',
                'kind': 'typed',
                'prompt': 'Write the simplified expression.',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_power_of_power(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 7])
    m = rng.randint(2, 4 if difficulty == 'easy' else 6)
    n = rng.randint(2, 4 if difficulty == 'easy' else 6)

    prompt = f"Simplify: ({base}^{m})^{n}"
    correct = f"{base}^{m * n}"
    explanation = f"Use (a^m)^n = a^(m·n). Here: ({base}^{m})^{n} = {base}^({m}·{n}) = {base}^{m * n}."

    if qtype == 'mcq':
        options = _unique_options([correct, f"{base}^{m + n}", f"{base}^{m - n}", f"{base}^{m * n + 1}"], correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Identify the outer exponent.', 'Multiply exponents.', 'Keep the base.']
        checkpoints = [
            {
                'id': 'cp_mul',
                'kind': 'typed',
                'prompt': f"Multiply exponents: {m} × {n} = ?",
                'correct_answer': str(m * n),
                'explanation': 'Multiply the exponents.',
            },
            {
                'id': 'cp_final',
                'kind': 'typed',
                'prompt': 'Write the simplified expression.',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_negative_exponent(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4, 5, 6, 7, 10])
    n = rng.randint(1, 2 if difficulty == 'easy' else 3)

    prompt = f"Write with positive exponents: {base}^-{n}"
    correct = f"1/{base}^{n}"
    explanation = f"Use a^-n = 1/a^n. So {base}^-{n} = 1/{base}^{n}."

    if qtype == 'mcq':
        options = _unique_options([correct, f"{base}^{n}", f"-1/{base}^{n}", f"1/{base}^{max(1, n - 1)}"], correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Recall the negative exponent law.', 'Rewrite as a reciprocal.', 'Ensure the exponent is positive.']
        checkpoints = [
            {
                'id': 'cp_rule',
                'kind': 'typed',
                'prompt': 'Fill in: a^-n = ____',
                'correct_answer': '1/a^n',
                'explanation': 'A negative exponent means reciprocal.',
            },
            {
                'id': 'cp_final',
                'kind': 'typed',
                'prompt': 'Write the final answer with positive exponents.',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_rational_exponent_convert(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Convert between a^(m/n) and n√(a^m)
    base = rng.choice(['x', 'a', 'm', 'p'])
    n = rng.choice([2, 3, 4]) if difficulty != 'easy' else rng.choice([2, 3])
    m = rng.randint(1, 3 if difficulty == 'easy' else 4)

    power_form = _format_rational_as_power(base, m, n)
    root_form = _format_rational_as_root(base, m, n)

    if rng.random() < 0.5:
        prompt = f"Rewrite using a root: {power_form}"
        correct = root_form
        explanation = (
            f"A rational exponent means a root: {base}^({m}/{n}) = (n√{base})^{m}. "
            f"So {power_form} = {root_form}."
        )
    else:
        prompt = f"Rewrite using a rational exponent: {root_form}"
        correct = power_form
        explanation = (
            f"A root can be written as a rational exponent: (n√{base})^{m} = {base}^({m}/{n}). "
            f"So {root_form} = {power_form}."
        )

    if qtype == 'mcq':
        if correct == root_form:
            options = _unique_options([correct, _format_rational_as_root(base, 1, n), _format_rational_as_root(base, m, 2), power_form], correct=correct, rng=rng)
        else:
            options = _unique_options([correct, _format_rational_as_power(base, 1, n), _format_rational_as_power(base, m, 2), root_form], correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Identify the numerator and denominator of the rational exponent (or index of the root).', 'Convert between power and root forms.', 'Rewrite the expression.']
        checkpoints = [
            {
                'id': 'cp_rule',
                'kind': 'typed',
                'prompt': 'Fill in: a^(m/n) = (n√a)^m',
                'correct_answer': 'a^(m/n) = (n√a)^m',
                'explanation': 'This is the key conversion rule used in Grade 10.',
            },
            {
                'id': 'cp_final',
                'kind': 'typed',
                'prompt': 'Write the converted form.',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_equate_exponents(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Solve  a^x = a^k  => x = k
    base = rng.choice([2, 3, 5])
    k = rng.randint(1, 6 if difficulty == 'easy' else 10)

    prompt = f"Solve for x: {base}^x = {base}^{k}"
    correct = str(k)
    explanation = f"If the bases are the same, the exponents must be equal. So x = {k}."

    if qtype == 'mcq':
        options = _unique_options([correct, str(-k), str(k + 1), str(max(0, k - 1))], correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Check both sides have the same base.', 'Equate exponents.', 'Solve for x.']
        checkpoints = [
            {
                'id': 'cp_bases',
                'kind': 'typed',
                'prompt': 'Are the bases the same? (yes/no)',
                'correct_answer': 'yes',
                'explanation': f"Both sides are powers of {base}.",
            },
            {
                'id': 'cp_eq',
                'kind': 'typed',
                'prompt': 'Write the equation for exponents: x = ___',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


_SUBSKILL_GENERATORS = {
    'laws_product_same_base': _gen_product_same_base,
    'laws_quotient_same_base': _gen_quotient_same_base,
    'laws_power_of_power': _gen_power_of_power,
    'negative_exponents': _gen_negative_exponent,
    'rational_exponents_convert': _gen_rational_exponent_convert,
    'solve_by_equating_exponents': _gen_equate_exponents,
}


def generate_grade10_exponents_question(
    *,
    subskill: Optional[str] = None,
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed)

    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    if question_type not in {'typed', 'mcq', 'scaffold'}:
        question_type = 'typed'

    if not subskill or subskill == 'mixed':
        subskill = rng.choice(list(_SUBSKILL_GENERATORS.keys()))

    gen = _SUBSKILL_GENERATORS.get(subskill)
    if gen is None:
        subskill = 'laws_product_same_base'
        gen = _SUBSKILL_GENERATORS[subskill]

    q = gen(rng, difficulty, question_type)

    q.update(
        {
            'id': _make_id('g10_exp'),
            'topic': TOPIC,
            'subskill': subskill,
            'difficulty': difficulty,
        }
    )

    _validate_question(q)
    return q


def generate_grade10_exponents_questions(
    *,
    count: int = 10,
    subskill: Optional[str] = None,
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    base_seed = seed if seed is not None else random.randint(1, 10**9)

    questions: List[Dict[str, Any]] = []
    for i in range(max(1, int(count))):
        q = generate_grade10_exponents_question(
            subskill=subskill,
            difficulty=difficulty,
            question_type=question_type,
            seed=base_seed + i,
        )
        questions.append(q)

    return questions
