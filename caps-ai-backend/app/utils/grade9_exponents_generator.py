import random
import time
from typing import Any, Dict, List, Optional


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
        'options': options,
        'correct_answer': str(correct_answer),
        'explanation': explanation,
        **extra,
    }


def _make_scaffold(*, prompt: str, steps: List[str], checkpoints: List[Dict[str, Any]], final_answer: str, explanation: str, **extra) -> Dict[str, Any]:
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


def _pow_int(base: int, exp: int) -> int:
    # exp can be negative, but we'll avoid generating negative exponents for numeric evaluation
    if exp < 0:
        raise ValueError('Negative exponent not supported for integer evaluation')
    return base ** exp


def _csv_exponent_laws_table() -> Dict[str, Any]:
    headers = ['Law', 'Example']
    rows = [
        ['a^m × a^n = a^(m+n)', '3^2 × 3^3 = 3^(2+3) = 3^5'],
        ['a^m ÷ a^n = a^(m−n)', '5^4 ÷ 5^2 = 5^(4−2) = 5^2'],
        ['(a^m)^n = a^(m×n)', '(2^3)^2 = 2^6'],
        ['(a × t)^n = a^n × t^n', '(3 × 4)^2 = 3^2 × 4^2'],
        ['a^0 = 1', '32^0 = 1'],
    ]
    return {'headers': headers, 'rows': rows}


def _gen_write_exponential_form(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.choice([2, 3, 4, 5, 6, 7, 8, 10])
    exp = rng.randint(2, 5 if difficulty == 'easy' else 7)

    # occasionally include a negative base
    if difficulty != 'easy' and rng.random() < 0.35:
        base = -base

    term = f"({base})" if base < 0 else str(base)
    repeated = ' × '.join([term] * exp)
    correct = f"{term}^{exp}" if base < 0 else f"{base}^{exp}"

    prompt = f"Write in exponential notation: {repeated}"
    explanation = f"The base is {term} repeated {exp} times, so the exponential form is {correct}."

    if qtype == 'mcq':
        wrong = [
            f"{term}^{exp - 1}" if exp > 2 else f"{term}^{exp + 1}",
            f"{term}^{exp + 1}",
            f"{base}^{exp}" if base >= 0 else f"{abs(base)}^{exp}",
        ]
        options = list(dict.fromkeys([correct, *wrong]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Identify the repeated factor (base).', 'Count how many times it is repeated (exponent).', 'Write base^exponent.']
        checkpoints = [
            {
                'id': 'cp_base',
                'prompt': 'What is the base?',
                'kind': 'typed',
                'correct_answer': str(base),
                'explanation': f"The repeated factor is {base}."
            },
            {
                'id': 'cp_exp',
                'prompt': 'What is the exponent (how many factors)?',
                'kind': 'typed',
                'correct_answer': str(exp),
                'explanation': f"There are {exp} factors."
            },
            {
                'id': 'cp_form',
                'prompt': 'Write the exponential form.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_order_of_operations(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = rng.randint(2, 9)
    e = rng.randint(2, 3 if difficulty == 'easy' else 4)
    b = rng.randint(1, 15)

    # expression: a^e - b OR b + c×a^e - d
    if rng.random() < 0.5:
        prompt = f"Calculate: {a}^{e} − {b}"
        correct_val = _pow_int(a, e) - b
        explanation = f"Calculate the power first: {a}^{e} = {_pow_int(a, e)}. Then subtract {b}: {_pow_int(a, e)} − {b} = {correct_val}."
    else:
        c = rng.randint(2, 6)
        d = rng.randint(1, 20)
        prompt = f"Calculate: {b} + {c} × {a}^{e} − {d}"
        powv = _pow_int(a, e)
        correct_val = b + c * powv - d
        explanation = f"Order: powers, then ×, then +/−. {a}^{e}={powv}. {c}×{powv}={c*powv}. Then {b}+{c*powv}−{d}={correct_val}."

    correct = str(correct_val)

    if qtype == 'mcq':
        options = list(dict.fromkeys([
            correct,
            str(correct_val + 1),
            str(correct_val - 1),
            str(correct_val + rng.choice([2, 3, 5])),
        ]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Calculate powers first.', 'Do multiplication/division.', 'Finish with addition/subtraction.']
        checkpoints = [
            {
                'id': 'cp_pow',
                'prompt': 'Calculate the power(s) first. What is the value of the power term?',
                'kind': 'typed',
                'correct_answer': str(_pow_int(a, e)),
                'explanation': f"{a}^{e} = {_pow_int(a, e)}."
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the final answer.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_laws_product_quotient(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 7])
    m = rng.randint(1, 5)
    n = rng.randint(1, 5)
    op = rng.choice(['×', '÷'])

    if op == '×':
        prompt = f"Simplify using laws of exponents: {base}^{m} × {base}^{n}"
        correct = f"{base}^{m+n}"
        explanation = f"Same base: add exponents. {base}^{m}×{base}^{n}={base}^({m}+{n})={base}^{m+n}."
    else:
        if difficulty == 'easy' and m < n:
            m, n = n, m
        prompt = f"Simplify using laws of exponents: {base}^{m} ÷ {base}^{n}"
        correct = f"{base}^{m-n}"
        explanation = f"Same base: subtract exponents. {base}^{m}÷{base}^{n}={base}^({m}−{n})={base}^{m-n}."

    if qtype == 'mcq':
        options = list(dict.fromkeys([
            correct,
            f"{base}^{m*n}",
            f"{base}^{m+n+1}",
            f"{base}^{abs(m-n)}",
        ]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, table=_csv_exponent_laws_table())

    if qtype == 'scaffold':
        steps = ['Check the bases are the same.', 'Use the correct law (add exponents for ×, subtract for ÷).', 'Write the simplified expression.']
        checkpoints = [
            {
                'id': 'cp_law',
                'prompt': 'Which operation do we use on the exponents (add or subtract)?',
                'kind': 'typed',
                'correct_answer': 'add' if op == '×' else 'subtract',
                'explanation': 'Multiply: add exponents. Divide: subtract exponents.'
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the simplified expression.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, table=_csv_exponent_laws_table())

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, table=_csv_exponent_laws_table())


def _gen_power_of_a_power(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 7])
    m = rng.randint(2, 4 if difficulty == 'easy' else 6)
    n = rng.randint(2, 3 if difficulty == 'easy' else 4)

    prompt = f"Simplify: ({base}^{m})^{n}"
    correct = f"{base}^{m*n}"
    explanation = f"Power of a power: multiply exponents. ({base}^{m})^{n} = {base}^({m}×{n}) = {base}^{m*n}."

    if qtype == 'mcq':
        options = list(dict.fromkeys([
            correct,
            f"{base}^{m+n}",
            f"{base}^{m-n}",
            f"{base}^{m*n + 1}",
        ]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, table=_csv_exponent_laws_table())

    if qtype == 'scaffold':
        steps = ['Identify the inner exponent and outer exponent.', 'Multiply them.', 'Write the simplified expression.']
        checkpoints = [
            {
                'id': 'cp_mul',
                'prompt': f"Multiply exponents: {m} × {n} = ?",
                'kind': 'typed',
                'correct_answer': str(m * n),
                'explanation': f"{m} × {n} = {m * n}."
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the simplified expression.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, table=_csv_exponent_laws_table())

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, table=_csv_exponent_laws_table())


def _gen_zero_exponent(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 7, 10, 12, 32])
    prompt = f"Evaluate: {base}^0"
    correct = '1'
    explanation = "Any non-zero number to the power of 0 equals 1."

    if qtype == 'mcq':
        options = list(dict.fromkeys(['1', '0', str(base), str(-base)]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, table=_csv_exponent_laws_table())

    if qtype == 'scaffold':
        steps = ['Use the law a^0 = 1 (for a ≠ 0).']
        checkpoints = [
            {
                'id': 'cp_final',
                'prompt': 'Write the value.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, table=_csv_exponent_laws_table())

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, table=_csv_exponent_laws_table())


def _gen_negative_exponent_meaning(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 10])
    exp = rng.randint(2, 4 if difficulty == 'easy' else 6)

    prompt = f"Write with a positive exponent: {base}^-{exp}"
    correct = f"1/{base}^{exp}"
    explanation = f"Negative exponent means reciprocal: {base}^-{exp} = (1/{base})^{exp} = 1/{base}^{exp}."

    if qtype == 'mcq':
        options = list(dict.fromkeys([
            correct,
            f"{base}^{exp}",
            f"1/{base}^-{exp}",
            f"({base})/{exp}",
        ]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Recall: a^-n = 1/a^n.', 'Rewrite using a positive exponent.']
        checkpoints = [
            {
                'id': 'cp_rule',
                'prompt': 'What does a negative exponent mean (reciprocal)? Type: reciprocal',
                'kind': 'typed',
                'correct_answer': 'reciprocal',
                'explanation': 'A negative exponent indicates the reciprocal (multiplicative inverse).'
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the expression with a positive exponent.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def generate_grade9_exponents_question(
    *,
    subskill: str = 'mixed',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    if question_type not in {'typed', 'mcq', 'scaffold'}:
        question_type = 'typed'

    rng = random.Random(seed if seed is not None else int(time.time() * 1000))
    subskill = str(subskill or 'mixed').strip().lower()

    generators = {
        'write_exponential_form': _gen_write_exponential_form,
        'order_of_operations': _gen_order_of_operations,
        'laws_product_quotient': _gen_laws_product_quotient,
        'power_of_a_power': _gen_power_of_a_power,
        'zero_exponent': _gen_zero_exponent,
        'negative_exponent_meaning': _gen_negative_exponent_meaning,
    }

    if subskill == 'mixed':
        keys = list(generators.keys())
        subskill = rng.choice(keys)

    if subskill not in generators:
        subskill = 'write_exponential_form'

    q = generators[subskill](rng, difficulty, question_type)

    q_full = {
        'id': _make_id('g9_exp'),
        'topic': 'grade9_exponents',
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(q_full)
    return q_full
