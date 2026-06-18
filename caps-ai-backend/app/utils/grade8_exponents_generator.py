import random
import time
import math
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
    unique = unique[:max(min_len, len(unique))]
    rng.shuffle(unique)
    return unique


def _pow_int(base: int, exp: int) -> int:
    return int(base ** exp)


def _format_scientific(mantissa: float, exp: int) -> str:
    # Use comma as decimal separator to align with doc examples.
    s = f"{mantissa:.10g}"
    s = s.rstrip('0').rstrip('.') if '.' in s else s
    s = s.replace('.', ',')
    return f"{s} × 10^{exp}"


def _scientific_to_int(mantissa: float, exp: int) -> int:
    return int(round(mantissa * (10 ** exp)))


def _gen_write_exponential_form(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 10]) if difficulty == 'easy' else rng.randint(2, 9)
    exp = rng.choice([2, 3, 4, 5]) if difficulty != 'hard' else rng.randint(4, 8)
    product = ' × '.join([str(base)] * exp)
    prompt = f"Write in exponential form: {product}"
    correct = f"{base}^{exp}"
    explanation = f"There are {exp} factors of {base}, so the exponential form is {base}^{exp}."

    if qtype == 'mcq':
        options = [correct, f"{exp}^{base}", f"{base}^{max(1, exp - 1)}", f"{base + 1}^{exp}"]
        options = _unique_options(options, correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'base': base, 'exp': exp})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'base': base, 'exp': exp})


def _gen_calculate_power(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        base = rng.randint(2, 12)
        exp = rng.choice([2, 3, 4])
    elif difficulty == 'medium':
        base = rng.randint(2, 15)
        exp = rng.choice([2, 3, 4, 5])
    else:
        base = rng.randint(2, 20)
        exp = rng.choice([2, 3, 4, 5, 6])

    value = _pow_int(base, exp)
    prompt = f"Calculate: {base}^{exp}"
    correct = str(value)
    explanation = f"{base}^{exp} means multiply {base} by itself {exp} times."

    if qtype == 'mcq':
        options = [correct, str(value + 1), str(max(0, value - 1)), str(_pow_int(base + 1, exp))]
        options = _unique_options(options, correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'base': base, 'exp': exp})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'base': base, 'exp': exp})


def _gen_square_or_cube_root(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    kind = rng.choice(['sqrt', 'cbrt'])
    if kind == 'sqrt':
        root = rng.randint(2, 15) if difficulty != 'hard' else rng.randint(5, 30)
        n = root * root
        prompt = f"Calculate: √{n}"
        correct = str(root)
        explanation = f"Because {root} × {root} = {n}, √{n} = {root}."
    else:
        root = rng.randint(2, 10) if difficulty != 'hard' else rng.randint(3, 15)
        n = root * root * root
        prompt = f"Calculate: ∛{n}"
        correct = str(root)
        explanation = f"Because {root} × {root} × {root} = {n}, ∛{n} = {root}."

    if qtype == 'mcq':
        options = [correct, str(root + 1), str(max(1, root - 1)), str(root * 2)]
        options = _unique_options(options, correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'kind': kind, 'n': n, 'root': root})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'kind': kind, 'n': n, 'root': root})


def _gen_negative_base_parentheses(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = -rng.randint(2, 6) if difficulty != 'hard' else -rng.randint(2, 10)
    exp = rng.choice([2, 3, 4, 5])

    variant = rng.choice(['minus_outside', 'paren'])
    if variant == 'minus_outside':
        abs_base = abs(base)
        prompt = f"Calculate: -{abs_base}^{exp}"
        correct_val = -_pow_int(abs_base, exp)
        explanation = f"Without brackets, calculate {abs_base}^{exp} first, then apply the negative sign."
        correct = str(correct_val)
    else:
        prompt = f"Calculate: ({base})^{exp}"
        correct_val = _pow_int(base, exp)
        explanation = f"With brackets, the negative base is included: ({base})^{exp} = {correct_val}."
        correct = str(correct_val)

    if qtype == 'mcq':
        options = [correct, str(-correct_val), str(correct_val + 1), str(correct_val - 1)]
        options = _unique_options(options, correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'base': base, 'exp': exp, 'variant': variant})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'base': base, 'exp': exp, 'variant': variant})


def _gen_product_of_powers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.randint(2, 9)
    m = rng.randint(1, 6)
    n = rng.randint(1, 6)
    prompt = f"Simplify: {base}^{m} × {base}^{n}"
    correct = f"{base}^{m + n}"
    explanation = f"Same base → add exponents: {m}+{n}={m+n}."

    if qtype == 'mcq':
        options = [correct, f"{base}^{m * n}", f"{base}^{abs(m - n)}", f"{base}^{m + n + 1}"]
        options = _unique_options(options, correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'base': base, 'm': m, 'n': n})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Add exponents: {m} + {n} = ?",
                'correct_answer': str(m + n),
                'explanation': 'Add the exponents.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Write the simplified power:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Confirm the bases match.', 'Add the exponents.', 'Keep the base.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'base': base, 'm': m, 'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'base': base, 'm': m, 'n': n})


def _gen_quotient_of_powers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.randint(2, 9) if difficulty != 'hard' else rng.randint(2, 15)
    m = rng.randint(3, 10) if difficulty != 'hard' else rng.randint(8, 20)
    n = rng.randint(1, m - 1)
    prompt = f"Simplify: {base}^{m} ÷ {base}^{n}"
    correct = f"{base}^{m - n}"
    explanation = f"Same base → subtract exponents: {m}−{n}={m-n}."

    if qtype == 'mcq':
        options = [correct, f"{base}^{m + n}", f"{base}^{m // max(1, n)}", f"{base}^{n - m}"]
        options = _unique_options(options, correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'base': base, 'm': m, 'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'base': base, 'm': m, 'n': n})


def _gen_power_of_a_power(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.randint(2, 9) if difficulty != 'hard' else rng.randint(2, 12)
    m = rng.randint(2, 6) if difficulty != 'hard' else rng.randint(3, 10)
    n = rng.randint(2, 5) if difficulty != 'hard' else rng.randint(3, 8)
    prompt = f"Simplify: ({base}^{m})^{n}"
    correct = f"{base}^{m * n}"
    explanation = f"Power of a power → multiply exponents: {m}×{n}={m*n}."

    if qtype == 'mcq':
        options = [correct, f"{base}^{m + n}", f"{base}^{m - n}", f"{base}^{m * n + 1}"]
        options = _unique_options(options, correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'base': base, 'm': m, 'n': n})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Multiply exponents: {m} × {n} = ?",
                'correct_answer': str(m * n),
                'explanation': 'Multiply the exponents.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Write the simplified power:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = ['Identify inner and outer exponent.', 'Multiply the exponents.', 'Keep the base.']
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'base': base, 'm': m, 'n': n})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'base': base, 'm': m, 'n': n})


def _gen_power_of_a_product(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a = rng.randint(2, 9)
    b = rng.randint(2, 9)
    exp = rng.randint(2, 5) if difficulty != 'hard' else rng.randint(3, 7)
    prompt = f"Write as a product of powers: ({a}×{b})^{exp}"
    correct = f"{a}^{exp} × {b}^{exp}"
    explanation = f"(a×b)^m = a^m × b^m."

    if qtype == 'mcq':
        options = [correct, f"{a}^{exp} + {b}^{exp}", f"{(a*b)}^{exp}", f"{a}^{exp + 1} × {b}^{exp}"]
        options = _unique_options(options, correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'exp': exp})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'exp': exp})


def _gen_zero_exponent(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    base = rng.randint(2, 15) if difficulty != 'hard' else rng.randint(2, 40)
    prompt = f"Simplify: {base}^0"
    correct = '1'
    explanation = 'Any non-zero number raised to the power 0 equals 1.'

    if qtype == 'mcq':
        options = ['0', '1', str(base), str(-base)]
        options = _unique_options(options, correct=correct, rng=rng)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'base': base})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'base': base})


def _gen_scientific_to_ordinary(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    exp = rng.randint(2, 8) if difficulty != 'hard' else rng.randint(4, 12)
    mantissa = rng.choice([1.24, 2.05, 3.4, 9.2074, 1.04]) if difficulty == 'easy' else round(rng.uniform(1.1, 9.9), 2)
    value = _scientific_to_int(mantissa, exp)
    prompt = f"Write in the ordinary way: {_format_scientific(mantissa, exp)}"
    correct = f"{value:,}".replace(',', ' ')
    explanation = f"Move the decimal point {exp} places to the right."

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'mantissa': mantissa, 'exp': exp, 'value': value})


def _gen_ordinary_to_scientific(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    zeros = rng.randint(3, 8) if difficulty != 'hard' else rng.randint(6, 12)
    lead = rng.randint(12, 987) if difficulty != 'easy' else rng.randint(12, 99)
    n = int(str(lead) + ('0' * zeros))
    s = str(n)
    exp = len(s) - 1
    mantissa = float(s[0] + ('.' + s[1:3] if len(s) >= 3 else ''))
    mantissa = round(mantissa, 2)
    correct = _format_scientific(mantissa, exp)
    prompt = f"Write in scientific notation: {s}"
    explanation = 'Scientific notation is a number between 1 and 10 multiplied by a power of 10.'

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'n': n, 'mantissa': mantissa, 'exp': exp})


def _gen_compare_scientific(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    exp1 = rng.randint(2, 9)
    exp2 = rng.randint(2, 9)
    m1 = round(rng.uniform(1.1, 9.9), 1)
    m2 = round(rng.uniform(1.1, 9.9), 1)
    n1 = m1 * (10 ** exp1)
    n2 = m2 * (10 ** exp2)
    correct = '>' if n1 > n2 else '<'
    left = _format_scientific(m1, exp1)
    right = _format_scientific(m2, exp2)
    prompt = f"Compare using < or > : {left} ? {right}"
    explanation = 'Compare the exponents first; if equal compare mantissas.'

    if qtype == 'mcq':
        options = ['<', '>', '=']
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'m1': m1, 'e1': exp1, 'm2': m2, 'e2': exp2})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'m1': m1, 'e1': exp1, 'm2': m2, 'e2': exp2})


def _gen_rational_square_or_cube(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    kind = rng.choice(['square_fraction', 'cube_fraction', 'square_decimal'])
    if kind == 'square_fraction':
        num = rng.choice([1, 2, 3, 4, 5, 7])
        den = rng.choice([2, 3, 4, 5, 6, 7, 8, 10, 12])
        prompt = f"Calculate: ({num}/{den})^2"
        correct = f"{num * num}/{den * den}"
        explanation = f"Square numerator and denominator: ({num}/{den})^2 = {num}^2/{den}^2."
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'num': num, 'den': den, 'power': 2})

    if kind == 'cube_fraction':
        num = rng.choice([1, 2, 3, 4, 5])
        den = rng.choice([3, 4, 5, 6, 8, 10])
        prompt = f"Calculate: ({num}/{den})^3"
        correct = f"{num ** 3}/{den ** 3}"
        explanation = f"Cube numerator and denominator: ({num}/{den})^3 = {num}^3/{den}^3."
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'num': num, 'den': den, 'power': 3})

    d = rng.choice([0.6, 0.7, 0.8, 0.9]) if difficulty != 'hard' else round(rng.uniform(0.2, 0.9), 1)
    prompt = f"Calculate: ({str(d).replace('.', ',')})^2"
    correct = str(round(d * d, 4)).replace('.', ',').rstrip('0').rstrip(',')
    explanation = 'Square the decimal (or convert to a fraction like 0,6 = 6/10).'
    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'decimal': d, 'power': 2})


def _gen_mixed_operations(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    variant = rng.choice(['cube_root_and_power', 'brackets_square_plus_zero'])
    if variant == 'cube_root_and_power':
        base = rng.randint(2, 5)
        cube = rng.choice([27, 64, 125, 216])
        croot = round(cube ** (1 / 3))
        prompt = f"Simplify: {base}^3 + ∛{cube} × 2"
        value = (base ** 3) + int(croot) * 2
        correct = str(value)
        explanation = 'Calculate the power and root first, then multiply, then add.'
        return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'variant': variant})

    a = rng.randint(2, 6)
    b = rng.randint(2, 6)
    prompt = f"Simplify: 5 × ({a} + {b})^2 + (-1)^0"
    value = 5 * ((a + b) ** 2) + 1
    correct = str(value)
    explanation = 'Compute inside brackets, square, multiply, and remember anything^0 = 1.'
    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'variant': variant})


def generate_grade8_exponents_question(
    *,
    subskill: str = 'exponents',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed if seed is not None else time.time_ns())

    topic = 'Exponents'
    subskill = str(subskill or 'exponents')
    difficulty = str(difficulty or 'easy').strip().lower()
    question_type = str(question_type or 'typed').strip().lower()

    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'
    if question_type not in {'typed', 'mcq', 'scaffold'}:
        question_type = 'typed'

    generators = {
        'write_exponential_form': _gen_write_exponential_form,
        'calculate_power': _gen_calculate_power,
        'square_or_cube_root': _gen_square_or_cube_root,
        'negative_base_parentheses': _gen_negative_base_parentheses,
        'product_of_powers': _gen_product_of_powers,
        'quotient_of_powers': _gen_quotient_of_powers,
        'power_of_a_power': _gen_power_of_a_power,
        'power_of_a_product': _gen_power_of_a_product,
        'zero_exponent': _gen_zero_exponent,
        'scientific_to_ordinary': _gen_scientific_to_ordinary,
        'ordinary_to_scientific': _gen_ordinary_to_scientific,
        'compare_scientific': _gen_compare_scientific,
        'rational_square_or_cube': _gen_rational_square_or_cube,
        'mixed_operations': _gen_mixed_operations,
    }

    supported = list(generators.keys())
    if subskill in {'exponents', 'mixed', ''}:
        subskill = rng.choice(supported)
    if subskill not in generators:
        subskill = rng.choice(supported)

    q = generators[subskill](rng, difficulty, question_type)

    out = {
        'id': _make_id('g8_exp'),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }
    _validate_question(out)
    return out
