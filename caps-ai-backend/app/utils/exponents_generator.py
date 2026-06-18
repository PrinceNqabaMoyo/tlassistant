import random
import math
from typing import Any, Dict, List, Optional


SUPPORTED_SUBSKILLS = {
    'squares_cubes_quickfacts',
    'expanded_to_exponential',
    'exponential_to_expanded_or_value',
    'identify_base_exponent_language',
    'prime_factors_to_exponential',
    'express_as_power_2_3_5_10',
    'roots_square_cube',
    'compare_exponential_root_forms',
    'order_expressions',
    'order_of_operations_with_powers_and_roots',
    'write_expression_in_words',
    'mixed_calculations_worksheet',
    'patterns_last_digit_powers_of_2',
}

SUPPORTED_DIFFICULTIES = {'easy', 'medium', 'hard'}
SUPPORTED_QUESTION_TYPES = {'typed', 'mcq', 'scaffold'}


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed)


def _question_id(rng: random.Random) -> str:
    return f"g7-exp-{rng.randrange(10**11, 10**12)}"


def _format_pow(base: int, exp: int) -> str:
    return f"{base}^{exp}"


def _is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    r = int(math.isqrt(n))
    return r * r == n


def _is_perfect_cube(n: int) -> bool:
    if n < 0:
        return False
    r = round(n ** (1 / 3))
    return r * r * r == n


def _sqrt_symbol(n: int) -> str:
    return f"√{n}"


def _cbrt_symbol(n: int) -> str:
    return f"∛{n}"


def _prime_factorization(n: int) -> Dict[int, int]:
    if n < 2:
        return {}
    factors: Dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def _factorization_to_product_string(factors: Dict[int, int]) -> str:
    parts: List[str] = []
    for p in sorted(factors.keys()):
        parts.extend([str(p)] * int(factors[p]))
    return ' × '.join(parts) if parts else '1'


def _factorization_to_exponential_string(factors: Dict[int, int]) -> str:
    if not factors:
        return '1'
    parts: List[str] = []
    for p in sorted(factors.keys()):
        e = int(factors[p])
        if e == 1:
            parts.append(str(p))
        else:
            parts.append(_format_pow(int(p), e))
    return ' × '.join(parts)


def _op_word(op: str) -> str:
    mapping = {
        '+': 'plus',
        '-': 'minus',
        '*': 'multiplied by',
        '/': 'divided by',
    }
    return mapping.get(op, op)


def _expr_to_words_b(expr: Dict[str, Any]) -> str:
    kind = expr.get('kind')
    if kind == 'int':
        return str(expr['value'])
    if kind == 'pow':
        base = int(expr['base'])
        exp = int(expr['exp'])
        if exp == 2:
            return f"{base} squared"
        if exp == 3:
            return f"{base} cubed"
        return f"{base} to the power {exp}"
    if kind == 'sqrt':
        return f"square root of {int(expr['value'])}"
    if kind == 'cbrt':
        return f"cube root of {int(expr['value'])}"
    if kind == 'binop':
        left = _expr_to_words_b(expr['left'])
        right = _expr_to_words_b(expr['right'])
        return f"{left} {_op_word(expr['op'])} {right}"
    if kind == 'group':
        inner = _expr_to_words_b(expr['value'])
        return f"open bracket {inner} close bracket"
    raise ValueError('Unsupported expression kind for words')


def _pick_base_for_powers(rng: random.Random, difficulty: str) -> int:
    if difficulty == 'easy':
        return rng.randint(2, 12)
    if difficulty == 'medium':
        return rng.randint(2, 20)
    return rng.randint(2, 30)


def _pick_exponent(rng: random.Random, difficulty: str) -> int:
    if difficulty == 'easy':
        return rng.choice([2, 3, 4])
    if difficulty == 'medium':
        return rng.choice([2, 3, 4, 5])
    return rng.choice([2, 3, 4, 5, 6])


def _make_typed(prompt: str, answer: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    return {
        **meta,
        'question_type': 'typed',
        'prompt': prompt,
        'answer': answer,
    }


def _make_mcq(prompt: str, answer: str, options: List[str], meta: Dict[str, Any]) -> Dict[str, Any]:
    unique_options = []
    for opt in options:
        s = str(opt)
        if s not in unique_options:
            unique_options.append(s)
    if answer not in unique_options:
        unique_options.append(answer)
    return {
        **meta,
        'question_type': 'mcq',
        'prompt': prompt,
        'answer': answer,
        'options': unique_options,
    }


def _make_scaffold(prompt: str, answer: str, steps: List[Dict[str, Any]], checkpoints: List[Dict[str, Any]], meta: Dict[str, Any]) -> Dict[str, Any]:
    return {
        **meta,
        'question_type': 'scaffold',
        'prompt': prompt,
        'answer': answer,
        'steps': steps,
        'checkpoints': checkpoints,
    }


def _validate_question(q: Dict[str, Any]) -> None:
    qt = q.get('question_type')
    if qt not in SUPPORTED_QUESTION_TYPES:
        raise ValueError(f"Unsupported question_type: {qt}")
    if not q.get('prompt'):
        raise ValueError('Question missing prompt')
    if 'answer' not in q:
        raise ValueError('Question missing answer')
    if qt == 'mcq':
        if not isinstance(q.get('options'), list) or len(q.get('options')) < 2:
            raise ValueError('MCQ question must include options[]')
    if qt == 'scaffold':
        if not isinstance(q.get('steps'), list) or not isinstance(q.get('checkpoints'), list):
            raise ValueError('Scaffold question must include steps[] and checkpoints[]')


def _gen_squares_cubes_quickfacts(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    use_square = rng.random() < 0.6
    if use_square:
        base = rng.randint(1, 12) if difficulty == 'easy' else rng.randint(1, 20)
        value = base * base
        prompt = f"Calculate: {base}^2"
        answer = str(value)
    else:
        base = rng.randint(1, 10) if difficulty == 'easy' else rng.randint(1, 12)
        value = base * base * base
        prompt = f"Calculate: {base}^3"
        answer = str(value)

    if question_type == 'mcq':
        distractors = {
            str(value + rng.choice([1, 2, 3, 5, 10])),
            str(max(0, value - rng.choice([1, 2, 3, 5, 10]))),
            str((base + 1) * (base + 1) if use_square else (base + 1) ** 3),
        }
        options = list(distractors) + [answer]
        rng.shuffle(options)
        return _make_mcq(prompt, answer, options, meta)

    if question_type == 'scaffold':
        exp = 2 if use_square else 3
        repeated = ' × '.join([str(base)] * exp)
        steps = [
            {'title': 'Meaning of the exponent', 'content': f"{_format_pow(base, exp)} means multiply {base} by itself {exp} times."},
            {'title': 'Write as repeated multiplication', 'content': repeated},
        ]
        checkpoints = [
            {'id': 'c1', 'kind': 'typed', 'prompt': f"Write {_format_pow(base, exp)} as repeated multiplication.", 'answer': repeated},
            {'id': 'c2', 'kind': 'typed', 'prompt': f"Now calculate the value of {_format_pow(base, exp)}.", 'answer': answer},
        ]
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def _gen_expanded_to_exponential(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    base = _pick_base_for_powers(rng, difficulty)
    exp = _pick_exponent(rng, difficulty)
    exp = min(exp, 6)
    product = ' × '.join([str(base)] * exp)
    answer = _format_pow(base, exp)
    prompt = f"Write in exponential form: {product}"

    if question_type == 'mcq':
        options = [
            _format_pow(base, exp),
            _format_pow(exp, base),
            _format_pow(base, max(1, exp - 1)),
            _format_pow(base + 1, exp),
        ]
        rng.shuffle(options)
        return _make_mcq(prompt, answer, options, meta)

    if question_type == 'scaffold':
        steps = [
            {'title': 'Identify the base', 'content': f"The repeated factor is {base}."},
            {'title': 'Count repetitions', 'content': f"{base} is repeated {exp} times."},
        ]
        checkpoints = [
            {'id': 'c1', 'kind': 'typed', 'prompt': 'What is the base?', 'answer': str(base)},
            {'id': 'c2', 'kind': 'typed', 'prompt': 'What is the exponent?', 'answer': str(exp)},
            {'id': 'c3', 'kind': 'typed', 'prompt': 'Write the exponential form.', 'answer': answer},
        ]
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def _gen_exponential_to_expanded_or_value(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    base = _pick_base_for_powers(rng, difficulty)
    exp = _pick_exponent(rng, difficulty)

    if base == 10:
        exp = rng.randint(1, 6)

    ask_expanded = rng.random() < 0.55
    pow_str = _format_pow(base, exp)
    repeated = ' × '.join([str(base)] * exp)
    value = base ** exp

    if ask_expanded:
        prompt = f"Write in expanded form: {pow_str}"
        answer = repeated
    else:
        prompt = f"Calculate: {pow_str}"
        answer = str(value)

    if question_type == 'mcq':
        if ask_expanded:
            options = [
                repeated,
                ' × '.join([str(base)] * max(1, exp - 1)),
                ' × '.join([str(exp)] * base) if base <= 6 else ' × '.join([str(exp)] * 6),
                ' × '.join([str(base + 1)] * exp),
            ]
        else:
            options = [
                str(value),
                str(value + rng.choice([1, 2, 3, 10])),
                str(max(0, value - rng.choice([1, 2, 3, 10]))),
                str((base ** max(1, exp - 1)) * base),
            ]
        rng.shuffle(options)
        return _make_mcq(prompt, answer, options, meta)

    if question_type == 'scaffold':
        steps = [
            {'title': 'Meaning', 'content': f"{pow_str} means multiply {base} by itself {exp} times."},
            {'title': 'Expanded form', 'content': repeated},
        ]
        checkpoints = [
            {'id': 'c1', 'kind': 'typed', 'prompt': f"Write {pow_str} as repeated multiplication.", 'answer': repeated},
        ]
        if not ask_expanded:
            checkpoints.append({'id': 'c2', 'kind': 'typed', 'prompt': f"Now calculate {pow_str}.", 'answer': str(value)})
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def _gen_identify_base_exponent_language(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    base = _pick_base_for_powers(rng, difficulty)
    exp = _pick_exponent(rng, difficulty)

    style = rng.choice(['words_to_exp', 'given_base_exp', 'exp_to_words'])

    if style == 'given_base_exp':
        prompt = f"Write in exponential notation: base {base}, exponent {exp}"
        answer = _format_pow(base, exp)
    elif style == 'exp_to_words':
        pow_str = _format_pow(base, exp)
        prompt = f"Write in words: {pow_str}"
        answer = f"{base} to the power {exp}"
    else:
        prompt = f"Write in exponential notation: {base} to the power {exp}"
        answer = _format_pow(base, exp)

    if question_type == 'mcq':
        if style == 'exp_to_words':
            options = [
                f"{base} to the power {exp}",
                f"{exp} to the power {base}",
                f"{base} times {exp}",
                f"{base} squared" if exp == 2 else f"{base} cubed" if exp == 3 else f"{base} to the power {exp - 1}",
            ]
        else:
            options = [
                _format_pow(base, exp),
                _format_pow(exp, base),
                _format_pow(base, max(1, exp - 1)),
                _format_pow(base + 1, exp),
            ]
        rng.shuffle(options)
        return _make_mcq(prompt, answer, options, meta)

    if question_type == 'scaffold':
        steps = [
            {'title': 'Base and exponent', 'content': f"The base is {base}. The exponent tells how many times the base is used as a factor."},
        ]
        checkpoints = [
            {'id': 'c1', 'kind': 'typed', 'prompt': 'What is the base?', 'answer': str(base)},
            {'id': 'c2', 'kind': 'typed', 'prompt': 'What is the exponent?', 'answer': str(exp)},
        ]
        if style == 'exp_to_words':
            checkpoints.append({'id': 'c3', 'kind': 'typed', 'prompt': f"Write { _format_pow(base, exp) } in words.", 'answer': answer})
        else:
            checkpoints.append({'id': 'c3', 'kind': 'typed', 'prompt': 'Write the exponential notation.', 'answer': answer})
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def _gen_roots_square_cube(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    use_square_root = rng.random() < 0.6
    if use_square_root:
        base = rng.randint(2, 15) if difficulty == 'easy' else rng.randint(2, 30)
        value = base * base
        expr = _sqrt_symbol(value)
        answer = str(base)
        prompt = f"Calculate: {expr}"
    else:
        base = rng.randint(2, 10) if difficulty == 'easy' else rng.randint(2, 12)
        value = base ** 3
        expr = _cbrt_symbol(value)
        answer = str(base)
        prompt = f"Calculate: {expr}"

    if question_type == 'mcq':
        options = [answer, str(base + 1), str(max(1, base - 1)), str(base + 2)]
        rng.shuffle(options)
        return _make_mcq(prompt, answer, options, meta)

    if question_type == 'scaffold':
        if use_square_root:
            steps = [
                {'title': 'Meaning of square root', 'content': f"{expr} asks for the number that squares to {value}."},
                {'title': 'Check', 'content': f"{base} × {base} = {value}"},
            ]
            checkpoints = [
                {'id': 'c1', 'kind': 'typed', 'prompt': f"What number squared equals {value}?", 'answer': answer},
            ]
        else:
            steps = [
                {'title': 'Meaning of cube root', 'content': f"{expr} asks for the number that cubes to {value}."},
                {'title': 'Check', 'content': f"{base} × {base} × {base} = {value}"},
            ]
            checkpoints = [
                {'id': 'c1', 'kind': 'typed', 'prompt': f"What number cubed equals {value}?", 'answer': answer},
            ]
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def _eval_simple(expr: Dict[str, Any]) -> int:
    kind = expr['kind']
    if kind == 'int':
        return int(expr['value'])
    if kind == 'pow':
        return int(expr['base']) ** int(expr['exp'])
    if kind == 'sqrt':
        return int(math.isqrt(int(expr['value'])))
    if kind == 'cbrt':
        v = int(expr['value'])
        r = round(v ** (1 / 3))
        return int(r)
    raise ValueError('Unsupported expr kind')


def _expr_to_str(expr: Dict[str, Any]) -> str:
    kind = expr['kind']
    if kind == 'int':
        return str(expr['value'])
    if kind == 'pow':
        return _format_pow(int(expr['base']), int(expr['exp']))
    if kind == 'sqrt':
        return _sqrt_symbol(int(expr['value']))
    if kind == 'cbrt':
        return _cbrt_symbol(int(expr['value']))
    raise ValueError('Unsupported expr kind')


def _gen_prime_factors_to_exponential(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    if difficulty == 'easy':
        n = rng.choice([35, 70, 81, 125, 100, 140])
    elif difficulty == 'medium':
        n = rng.choice([140, 280, 625, 216, 343, 900])
    else:
        n = rng.choice([280, 784, 2025, 1331, 8000, 1600])

    factors = _prime_factorization(int(n))
    product = _factorization_to_product_string(factors)
    answer = _factorization_to_exponential_string(factors)
    prompt = f"Express {n} as a product using exponential notation (prime factors)."

    if question_type == 'mcq':
        wrong1 = product
        wrong2 = answer.replace('^', '')
        wrong3 = _factorization_to_exponential_string(_prime_factorization(int(n) + rng.choice([1, 2, 3])))
        options = [answer, wrong1, wrong2, wrong3]
        rng.shuffle(options)
        return _make_mcq(prompt, answer, options, meta)

    if question_type == 'scaffold':
        steps = [
            {'title': 'Prime factorization', 'content': f"Break {n} into prime factors."},
            {'title': 'Use exponents', 'content': 'Write repeated primes using exponent notation.'},
        ]
        checkpoints = [
            {'id': 'c1', 'kind': 'typed', 'prompt': f"Write {n} as a product of primes (using ×).", 'answer': product},
            {'id': 'c2', 'kind': 'typed', 'prompt': 'Now rewrite using exponents.', 'answer': answer},
        ]
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def _gen_express_as_power_2_3_5_10(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    base = rng.choice([2, 3, 5, 10])
    if difficulty == 'easy':
        exp = rng.choice([2, 3, 4])
    elif difficulty == 'medium':
        exp = rng.choice([3, 4, 5])
    else:
        exp = rng.choice([4, 5, 6])
    value = base ** exp

    prompt = f"Express {value} as a power of {base}."
    answer = _format_pow(base, exp)

    if question_type == 'mcq':
        options = [
            answer,
            _format_pow(base, max(1, exp - 1)),
            _format_pow(base, exp + 1),
            _format_pow(rng.choice([2, 3, 5, 10]), exp),
        ]
        rng.shuffle(options)
        return _make_mcq(prompt, answer, options, meta)

    if question_type == 'scaffold':
        factors = ' × '.join([str(base)] * exp)
        steps = [
            {'title': 'Repeated multiplication', 'content': factors},
            {'title': 'Convert to power', 'content': f"The base {base} is repeated {exp} times."},
        ]
        checkpoints = [
            {'id': 'c1', 'kind': 'typed', 'prompt': f"Write {value} as repeated multiplication using {base}.", 'answer': factors},
            {'id': 'c2', 'kind': 'typed', 'prompt': f"Write {value} as a power of {base}.", 'answer': answer},
        ]
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def _gen_compare_exponential_root_forms(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    left_kind = rng.choice(['pow', 'sqrt', 'cbrt'])
    right_kind = rng.choice(['pow', 'sqrt', 'cbrt'])

    def make_expr(kind: str) -> Dict[str, Any]:
        if kind == 'pow':
            base = _pick_base_for_powers(rng, 'easy' if difficulty == 'easy' else 'medium')
            exp = rng.choice([2, 3, 4])
            return {'kind': 'pow', 'base': base, 'exp': exp}
        if kind == 'sqrt':
            b = rng.randint(2, 15)
            return {'kind': 'sqrt', 'value': b * b}
        b = rng.randint(2, 10)
        return {'kind': 'cbrt', 'value': b ** 3}

    left = make_expr(left_kind)
    right = make_expr(right_kind)

    left_val = _eval_simple(left)
    right_val = _eval_simple(right)

    if left_val == right_val:
        relation = '='
    elif left_val < right_val:
        relation = '<'
    else:
        relation = '>'

    prompt = f"Fill in the symbol: {_expr_to_str(left)} ? {_expr_to_str(right)}"
    answer = relation

    if question_type == 'mcq':
        return _make_mcq(prompt, answer, ['<', '>', '='], meta)

    if question_type == 'scaffold':
        steps = [
            {'title': 'Evaluate left', 'content': f"{_expr_to_str(left)} = {left_val}"},
            {'title': 'Evaluate right', 'content': f"{_expr_to_str(right)} = {right_val}"},
        ]
        checkpoints = [
            {'id': 'c1', 'kind': 'typed', 'prompt': f"What is {_expr_to_str(left)}?", 'answer': str(left_val)},
            {'id': 'c2', 'kind': 'typed', 'prompt': f"What is {_expr_to_str(right)}?", 'answer': str(right_val)},
            {'id': 'c3', 'kind': 'mcq', 'prompt': 'Which symbol makes it true?', 'answer': relation, 'options': ['<', '>', '=']},
        ]
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def _gen_order_expressions(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    count = 4 if difficulty == 'easy' else 5
    direction = rng.choice(['ascending', 'descending'])

    exprs: List[Dict[str, Any]] = []
    while len(exprs) < count:
        kind = rng.choice(['pow', 'sqrt', 'cbrt', 'int'])
        if kind == 'pow':
            base = rng.randint(2, 9) if difficulty == 'easy' else rng.randint(2, 12)
            exp = rng.choice([2, 3, 4]) if difficulty != 'hard' else rng.choice([2, 3, 4, 5])
            expr = {'kind': 'pow', 'base': base, 'exp': exp}
        elif kind == 'sqrt':
            b = rng.randint(2, 15) if difficulty != 'hard' else rng.randint(2, 25)
            expr = {'kind': 'sqrt', 'value': b * b}
        elif kind == 'cbrt':
            b = rng.randint(2, 10) if difficulty != 'hard' else rng.randint(2, 12)
            expr = {'kind': 'cbrt', 'value': b ** 3}
        else:
            expr = {'kind': 'int', 'value': rng.randint(0, 200)}
        exprs.append(expr)

    decorated = [(e, _eval_simple(e)) for e in exprs]
    ordered = sorted(decorated, key=lambda t: t[1], reverse=(direction == 'descending'))

    items_str = '; '.join([_expr_to_str(e) for e, _ in decorated])
    answer = ', '.join([_expr_to_str(e) for e, _ in ordered])

    prompt = f"Arrange in {direction} order: {items_str}"

    if question_type == 'mcq':
        wrong = ', '.join([_expr_to_str(e) for e, _ in reversed(ordered)])
        options = [answer, wrong]
        rng.shuffle(options)
        return _make_mcq(prompt, answer, options, meta)

    if question_type == 'scaffold':
        steps = [
            {'title': 'Evaluate each item', 'content': 'Compute each power/root to compare their values.'},
            {'title': 'Sort', 'content': f"Put them in {direction} order."},
        ]
        checkpoints = []
        for idx, (e, v) in enumerate(decorated[:min(3, len(decorated))], start=1):
            checkpoints.append({'id': f'c{idx}', 'kind': 'typed', 'prompt': f"What is {_expr_to_str(e)}?", 'answer': str(v)})
        checkpoints.append({'id': f'c{len(checkpoints)+1}', 'kind': 'typed', 'prompt': f"Write the full list in {direction} order (comma-separated).", 'answer': answer})
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def _gen_write_expression_in_words(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    base = rng.randint(2, 9)
    exp = rng.choice([2, 3, 4]) if difficulty != 'hard' else rng.choice([2, 3, 4, 5])
    a = rng.randint(2, 8)
    b = rng.randint(1, 12)
    pattern = rng.choice(['mul_pow_plus', 'sqrt_plus_pow', 'pow_times_pow'])

    if pattern == 'mul_pow_plus':
        expr = {
            'kind': 'binop',
            'op': '+',
            'left': {'kind': 'binop', 'op': '*', 'left': {'kind': 'int', 'value': a}, 'right': {'kind': 'pow', 'base': base, 'exp': exp}},
            'right': {'kind': 'int', 'value': b},
        }
        expr_str = f"{a} × {base}^{exp} + {b}"
    elif pattern == 'sqrt_plus_pow':
        s = rng.randint(5, 15)
        expr = {
            'kind': 'binop',
            'op': '+',
            'left': {'kind': 'sqrt', 'value': s * s},
            'right': {'kind': 'pow', 'base': base, 'exp': 2 if difficulty == 'easy' else exp},
        }
        expr_str = f"√{s*s} + {base}^{(2 if difficulty == 'easy' else exp)}"
    else:
        e2 = rng.choice([2, 3])
        expr = {
            'kind': 'binop',
            'op': '*',
            'left': {'kind': 'pow', 'base': base, 'exp': exp},
            'right': {'kind': 'pow', 'base': a, 'exp': e2},
        }
        expr_str = f"{base}^{exp} × {a}^{e2}"

    answer = _expr_to_words_b(expr)
    prompt = f"Write this numerical expression in words: {expr_str}"

    if question_type == 'mcq':
        options = [
            answer,
            answer.replace('plus', 'minus') if 'plus' in answer else answer + ' plus 1',
            answer.replace('multiplied by', 'plus') if 'multiplied by' in answer else answer,
            answer.replace('square root of', 'cube root of') if 'square root of' in answer else answer,
        ]
        rng.shuffle(options)
        return _make_mcq(prompt, answer, options, meta)

    if question_type == 'scaffold':
        steps = [
            {'title': 'Read the structure', 'content': 'Identify exponents, roots, and operations.'},
            {'title': 'Use operation words', 'content': 'Say “multiplied by”, “plus”, and “square root of”.'},
        ]
        checkpoints = [
            {'id': 'c1', 'kind': 'typed', 'prompt': 'Write the expression in words.', 'answer': answer},
        ]
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def _gen_mixed_calculations_worksheet(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    pattern = rng.choice(['pow_mul_pow', 'sqrt_plus_sqrt', 'nested_brackets', 'compare_powers'])

    if pattern == 'pow_mul_pow':
        a = rng.randint(2, 9)
        b = rng.randint(2, 9)
        ea = rng.choice([2, 3])
        eb = rng.choice([2, 3])
        prompt = f"Calculate: {a}^{ea} × {b}^{eb}"
        answer_val = (a ** ea) * (b ** eb)
        steps = [
            {'title': 'Evaluate powers', 'content': f"{a}^{ea} = {a**ea} and {b}^{eb} = {b**eb}"},
            {'title': 'Multiply', 'content': f"{a**ea} × {b**eb} = {answer_val}"},
        ]
        answer = str(answer_val)
    elif pattern == 'sqrt_plus_sqrt':
        x = rng.randint(5, 15)
        y = rng.randint(5, 15)
        prompt = f"Calculate: √{x*x} + √{y*y}"
        answer_val = x + y
        steps = [
            {'title': 'Evaluate roots', 'content': f"√{x*x} = {x} and √{y*y} = {y}"},
            {'title': 'Add', 'content': f"{x} + {y} = {answer_val}"},
        ]
        answer = str(answer_val)
    elif pattern == 'nested_brackets':
        a = rng.randint(2, 12)
        b = rng.randint(1, 8)
        prompt = f"Calculate: ({a} + {b})^2"
        answer_val = (a + b) ** 2
        steps = [
            {'title': 'Brackets first', 'content': f"{a} + {b} = {a+b}"},
            {'title': 'Square', 'content': f"({a+b})^2 = {answer_val}"},
        ]
        answer = str(answer_val)
    else:
        left_base = rng.randint(2, 6)
        left_exp = rng.choice([2, 3, 4])
        right_base = rng.randint(2, 10)
        right_exp = rng.choice([2, 3])
        left_val = left_base ** left_exp
        right_val = right_base ** right_exp
        relation = '=' if left_val == right_val else '<' if left_val < right_val else '>'
        prompt = f"Fill in the symbol: {left_base}^{left_exp} ? {right_base}^{right_exp}"
        answer = relation
        steps = [
            {'title': 'Evaluate both sides', 'content': f"{left_base}^{left_exp} = {left_val} and {right_base}^{right_exp} = {right_val}"},
        ]

    if question_type == 'mcq':
        if pattern == 'compare_powers':
            return _make_mcq(prompt, answer, ['<', '>', '='], meta)
        options = [
            answer,
            str(int(answer) + rng.choice([1, 2, 3, 5, 10])),
            str(max(0, int(answer) - rng.choice([1, 2, 3, 5, 10]))),
            str(int(answer) + rng.choice([11, 12, 13])),
        ]
        rng.shuffle(options)
        return _make_mcq(prompt, answer, options, meta)

    if question_type == 'scaffold':
        checkpoints: List[Dict[str, Any]] = []
        if pattern == 'compare_powers':
            checkpoints.append({'id': 'c1', 'kind': 'mcq', 'prompt': 'Which symbol makes the statement true?', 'answer': answer, 'options': ['<', '>', '=']})
        else:
            checkpoints.append({'id': 'c1', 'kind': 'typed', 'prompt': 'Calculate the final answer.', 'answer': answer})
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def _gen_order_of_operations_with_powers_and_roots(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    base = rng.randint(2, 9) if difficulty == 'easy' else rng.randint(2, 12)
    exp = rng.choice([2, 3]) if difficulty == 'easy' else rng.choice([2, 3, 4])
    pow_val = base ** exp

    a = rng.randint(2, 12)
    b = rng.randint(1, 20)

    pattern = rng.choice(['mul_add', 'add_mul', 'brackets'])

    if pattern == 'mul_add':
        prompt = f"Calculate: {a} × {base}^{exp} + {b}"
        answer_val = a * pow_val + b
        steps = [
            {'title': 'Exponents first', 'content': f"{base}^{exp} = {pow_val}"},
            {'title': 'Multiply', 'content': f"{a} × {pow_val} = {a * pow_val}"},
            {'title': 'Add', 'content': f"{a * pow_val} + {b} = {answer_val}"},
        ]
    elif pattern == 'add_mul':
        prompt = f"Calculate: {a} + {base}^{exp} × {b}"
        answer_val = a + pow_val * b
        steps = [
            {'title': 'Exponents first', 'content': f"{base}^{exp} = {pow_val}"},
            {'title': 'Multiply', 'content': f"{pow_val} × {b} = {pow_val * b}"},
            {'title': 'Add', 'content': f"{a} + {pow_val * b} = {answer_val}"},
        ]
    else:
        k = rng.randint(1, 8)
        prompt = f"Calculate: ({a} + {k})^{2}"
        answer_val = (a + k) ** 2
        steps = [
            {'title': 'Brackets first', 'content': f"{a} + {k} = {a + k}"},
            {'title': 'Square the result', 'content': f"({a + k})^2 = {answer_val}"},
        ]

    answer = str(answer_val)

    if question_type == 'mcq':
        options = [
            answer,
            str(answer_val + rng.choice([1, 2, 3, 5, 10])),
            str(max(0, answer_val - rng.choice([1, 2, 3, 5, 10]))),
            str(answer_val + rng.choice([11, 12, 13])),
        ]
        rng.shuffle(options)
        return _make_mcq(prompt, answer, options, meta)

    if question_type == 'scaffold':
        checkpoints: List[Dict[str, Any]] = []
        if pattern in ['mul_add', 'add_mul']:
            checkpoints.append({'id': 'c1', 'kind': 'typed', 'prompt': f"Calculate {base}^{exp}.", 'answer': str(pow_val)})
        else:
            checkpoints.append({'id': 'c1', 'kind': 'typed', 'prompt': f"Calculate {a} + {k}.", 'answer': str(a + k)})
        checkpoints.append({'id': 'c2', 'kind': 'typed', 'prompt': 'Calculate the final answer.', 'answer': answer})
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def _gen_patterns_last_digit_powers_of_2(rng: random.Random, difficulty: str, question_type: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    n = rng.randint(5, 20) if difficulty == 'easy' else rng.randint(20, 2000)

    cycle = [2, 4, 8, 6]
    last_digit = cycle[(n - 1) % 4]

    prompt = f"Without calculating the full value, what is the last digit of 2^{n}?"
    answer = str(last_digit)

    if question_type == 'mcq':
        return _make_mcq(prompt, answer, ['2', '4', '6', '8'], meta)

    if question_type == 'scaffold':
        steps = [
            {'title': 'Look at the last digit pattern', 'content': '2^1 ends in 2, 2^2 ends in 4, 2^3 ends in 8, 2^4 ends in 6. Then it repeats.'},
            {'title': 'Use the remainder when dividing by 4', 'content': f"Compute {n} mod 4 to choose the position in the cycle."},
        ]
        checkpoints = [
            {'id': 'c1', 'kind': 'typed', 'prompt': f"What is {n} mod 4?", 'answer': str(n % 4)},
            {'id': 'c2', 'kind': 'typed', 'prompt': 'What is the last digit?', 'answer': answer},
        ]
        return _make_scaffold(prompt, answer, steps, checkpoints, meta)

    return _make_typed(prompt, answer, meta)


def generate_grade7_exponents_question(
    subskill: str = 'squares_cubes_quickfacts',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    if subskill not in SUPPORTED_SUBSKILLS:
        raise ValueError(f"Unsupported subskill: {subskill}")
    if difficulty not in SUPPORTED_DIFFICULTIES:
        raise ValueError(f"Unsupported difficulty: {difficulty}")
    if question_type not in SUPPORTED_QUESTION_TYPES:
        raise ValueError(f"Unsupported question_type: {question_type}")

    rng = _rng(seed)
    meta = {
        'id': _question_id(rng),
        'topic': 'exponents',
        'subskill': subskill,
        'difficulty': difficulty,
    }

    if subskill == 'squares_cubes_quickfacts':
        q = _gen_squares_cubes_quickfacts(rng, difficulty, question_type, meta)
    elif subskill == 'expanded_to_exponential':
        q = _gen_expanded_to_exponential(rng, difficulty, question_type, meta)
    elif subskill == 'exponential_to_expanded_or_value':
        q = _gen_exponential_to_expanded_or_value(rng, difficulty, question_type, meta)
    elif subskill == 'identify_base_exponent_language':
        q = _gen_identify_base_exponent_language(rng, difficulty, question_type, meta)
    elif subskill == 'prime_factors_to_exponential':
        q = _gen_prime_factors_to_exponential(rng, difficulty, question_type, meta)
    elif subskill == 'express_as_power_2_3_5_10':
        q = _gen_express_as_power_2_3_5_10(rng, difficulty, question_type, meta)
    elif subskill == 'roots_square_cube':
        q = _gen_roots_square_cube(rng, difficulty, question_type, meta)
    elif subskill == 'compare_exponential_root_forms':
        q = _gen_compare_exponential_root_forms(rng, difficulty, question_type, meta)
    elif subskill == 'order_expressions':
        q = _gen_order_expressions(rng, difficulty, question_type, meta)
    elif subskill == 'order_of_operations_with_powers_and_roots':
        q = _gen_order_of_operations_with_powers_and_roots(rng, difficulty, question_type, meta)
    elif subskill == 'write_expression_in_words':
        q = _gen_write_expression_in_words(rng, difficulty, question_type, meta)
    elif subskill == 'mixed_calculations_worksheet':
        q = _gen_mixed_calculations_worksheet(rng, difficulty, question_type, meta)
    elif subskill == 'patterns_last_digit_powers_of_2':
        q = _gen_patterns_last_digit_powers_of_2(rng, difficulty, question_type, meta)
    else:
        raise ValueError(f"Unhandled subskill: {subskill}")

    _validate_question(q)
    return q
