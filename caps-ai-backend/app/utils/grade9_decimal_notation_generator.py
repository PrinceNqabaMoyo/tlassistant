import random
import time
from typing import Any, Dict, List, Optional, Tuple


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


def _gcd(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


def _reduce(n: int, d: int) -> Tuple[int, int]:
    if d == 0:
        raise ValueError('Denominator cannot be zero')
    if d < 0:
        n, d = -n, -d
    g = _gcd(n, d)
    return n // g, d // g


def _fmt_frac(n: int, d: int) -> str:
    n, d = _reduce(n, d)
    if d == 1:
        return str(n)
    return f"{n}/{d}"


def _fmt_decimal_comma(s: str) -> str:
    return str(s).replace('.', ',')


def _parse_decimal_to_int_scale(s: str) -> Tuple[int, int]:
    # returns (scaled_int, scale) where value = scaled_int/scale
    s = str(s).strip().replace(' ', '').replace(',', '.')
    sign = -1 if s.startswith('-') else 1
    if s.startswith('-'):
        s = s[1:]

    if '.' not in s:
        return sign * int(s), 1

    a, b = s.split('.', 1)
    b = ''.join([ch for ch in b if ch.isdigit()])
    if b == '':
        return sign * int(a or '0'), 1
    scale = 10 ** len(b)
    scaled = int(a or '0') * scale + int(b)
    return sign * scaled, scale


def _int_scale_to_decimal_string(scaled: int, scale: int) -> str:
    if scale == 1:
        return str(scaled)

    sign = '-' if scaled < 0 else ''
    scaled = abs(scaled)
    s = str(scaled).rjust(len(str(scale)) - 1 + 1, '0')
    k = len(str(scale)) - 1
    whole = s[:-k] or '0'
    frac = s[-k:]
    frac = frac.rstrip('0')
    if frac == '':
        return f"{sign}{whole}"
    return f"{sign}{whole}.{frac}"


def _pick_terminating_fraction(rng: random.Random, difficulty: str) -> Tuple[int, int]:
    if difficulty == 'easy':
        den = rng.choice([2, 4, 5, 8, 10, 20, 25, 50, 100])
    elif difficulty == 'medium':
        den = rng.choice([4, 8, 10, 20, 25, 40, 50, 100, 125, 200])
    else:
        den = rng.choice([8, 16, 20, 25, 40, 50, 80, 125, 200, 250, 500, 1000])

    num = rng.randint(1, den - 1)
    if difficulty != 'easy' and rng.random() < 0.25:
        num = rng.randint(den + 1, den * 2)

    return _reduce(num, den)


def _fraction_to_decimal_string(n: int, d: int) -> str:
    # d must divide 10^k for some k
    dd = d
    k2 = 0
    while dd % 2 == 0:
        dd //= 2
        k2 += 1
    k5 = 0
    while dd % 5 == 0:
        dd //= 5
        k5 += 1

    if dd != 1:
        # non-terminating; fall back to 6dp string
        val = n / d
        s = f"{val:.6f}".rstrip('0').rstrip('.')
        return s

    k = max(k2, k5)
    scale = 10 ** k
    scaled = n * (scale // d)
    return _int_scale_to_decimal_string(scaled, scale)


def _csv_equivalents_table() -> Dict[str, Any]:
    headers = ['Percentage', 'Common fraction', 'Decimal fraction']
    rows = [
        ['2.5%', '', ''],
        ['', '15/250', ''],
        ['', '', '0.009'],
        ['25%', '1/4', '0.25'],
        ['50%', '1/2', '0.5'],
        ['75%', '3/4', '0.75'],
        ['12.5%', '1/8', '0.125'],
    ]
    return {'headers': headers, 'rows': rows}


def _gen_decimal_to_fraction(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    dp = rng.choice([1, 2] if difficulty == 'easy' else ([2, 3] if difficulty == 'hard' else [1, 2, 3]))
    whole = rng.randint(0, 5 if difficulty == 'easy' else 20)
    frac = rng.randint(0, 10 ** dp - 1)
    if frac == 0 and whole == 0:
        frac = 1

    dec = f"{whole}.{str(frac).zfill(dp)}"
    n = whole * (10 ** dp) + frac
    d = 10 ** dp
    n, d = _reduce(n, d)
    correct = _fmt_frac(n, d)

    prompt = f"Write the following decimal fraction as a common fraction in its simplest form: {_fmt_decimal_comma(dec)}"
    explanation = f"Write {_fmt_decimal_comma(dec)} over {10 ** dp} and simplify to {correct}."

    if qtype == 'mcq':
        wrong = [
            _fmt_frac(n, 10 ** dp),
            _fmt_frac(n * 2, d),
            _fmt_frac(n, d * 2),
        ]
        options = list(dict.fromkeys([correct, *wrong]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Count the decimal places.', 'Write the decimal over a power of ten.', 'Simplify the fraction.']
        checkpoints = [
            {
                'id': 'cp_den',
                'prompt': 'What power of ten is the denominator?',
                'kind': 'typed',
                'correct_answer': str(10 ** dp),
                'explanation': f"There are {dp} decimal places, so denominator is {10 ** dp}."
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the simplest fraction.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_fraction_to_decimal(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    n, d = _pick_terminating_fraction(rng, difficulty)
    frac = _fmt_frac(n, d)
    correct = _fraction_to_decimal_string(n, d)

    prompt = f"Write the following common fraction as a decimal fraction: {frac}"
    explanation = f"Convert {frac} to a denominator that is a power of ten (or divide) to get {correct}."

    if qtype == 'mcq':
        scaled, scale = _parse_decimal_to_int_scale(correct)
        wrong = [
            _int_scale_to_decimal_string(scaled + 1, scale),
            _int_scale_to_decimal_string(max(0, scaled - 1), scale),
            _int_scale_to_decimal_string(scaled * 10, scale),
        ]
        options = list(dict.fromkeys([correct, *wrong]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Make the denominator a power of ten (2s and 5s only).', 'Write the decimal.']
        checkpoints = [
            {
                'id': 'cp_term',
                'prompt': 'Is this a terminating decimal? Type: yes',
                'kind': 'typed',
                'correct_answer': 'yes',
                'explanation': 'We use denominators made from 2s and 5s, so the decimal terminates.'
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the decimal fraction.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_percent_to_fraction(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    if difficulty == 'easy':
        p = rng.choice([5, 10, 20, 25, 50, 75])
    elif difficulty == 'medium':
        p = rng.choice([12.5, 70, 30, 15, 40])
    else:
        p = rng.choice([2.5, 12.5, 37.5, 62.5, 87.5])

    # p% = p/100
    scaled, scale = _parse_decimal_to_int_scale(str(p))
    n = scaled
    d = 100 * scale
    n, d = _reduce(n, d)
    correct = _fmt_frac(n, d)

    prompt = f"Write the following percentage as a common fraction in its simplest form: {_fmt_decimal_comma(str(p))}%"
    explanation = f"A percent means 'out of 100': {_fmt_decimal_comma(str(p))}% = {p}/100 = {correct}."

    if qtype == 'mcq':
        wrong = [_fmt_frac(n, d * 2), _fmt_frac(n * 2, d), f"{n}/{100}" ]
        options = list(dict.fromkeys([correct, *wrong]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Write the percent over 100.', 'Simplify the fraction.']
        checkpoints = [
            {
                'id': 'cp_over',
                'prompt': 'A percent is out of what number?',
                'kind': 'typed',
                'correct_answer': '100',
                'explanation': 'Percent means per 100.'
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the simplest fraction.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation)


def _gen_decimal_to_percent(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    dp = rng.choice([1, 2] if difficulty == 'easy' else [2, 3])
    whole = rng.randint(0, 1 if difficulty == 'easy' else 5)
    frac = rng.randint(1, 10 ** dp - 1)
    dec = f"{whole}.{str(frac).zfill(dp)}"

    scaled, scale = _parse_decimal_to_int_scale(dec)
    pct_scaled = scaled * 100
    correct = _int_scale_to_decimal_string(pct_scaled, scale)

    prompt = f"Write the following decimal fraction as a percentage: {_fmt_decimal_comma(dec)}"
    explanation = f"Multiply by 100: {_fmt_decimal_comma(dec)} × 100 = {correct}%."

    if qtype == 'mcq':
        wrong = [
            _int_scale_to_decimal_string(pct_scaled * 10, scale),
            _int_scale_to_decimal_string(max(0, pct_scaled - 1), scale),
            _int_scale_to_decimal_string(pct_scaled, scale * 10),
        ]
        options = list(dict.fromkeys([f"{correct}%", *[f"{w}%" for w in wrong]]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=f"{correct}%", explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Multiply the decimal by 100.', 'Add the percent sign.']
        checkpoints = [
            {
                'id': 'cp_mul',
                'prompt': 'What operation converts a decimal to a percent? Type: multiply by 100',
                'kind': 'typed',
                'correct_answer': 'multiply by 100',
                'explanation': 'Multiply by 100 to get a percentage.'
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the percentage.',
                'kind': 'typed',
                'correct_answer': f"{correct}%",
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=f"{correct}%", explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=f"{correct}%", explanation=explanation)


def _gen_fraction_to_percent(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    n, d = _pick_terminating_fraction(rng, difficulty)
    frac = _fmt_frac(n, d)
    dec = _fraction_to_decimal_string(n, d)
    scaled, scale = _parse_decimal_to_int_scale(dec)
    pct_scaled = scaled * 100
    pct = _int_scale_to_decimal_string(pct_scaled, scale)

    prompt = f"Write the following common fraction as a percentage: {frac}"
    explanation = f"Convert to decimal then ×100: {frac} = {dec}, so {dec} × 100 = {pct}%."

    if qtype == 'mcq':
        wrong = [
            f"{_int_scale_to_decimal_string(pct_scaled + 1, scale)}%",
            f"{_int_scale_to_decimal_string(max(0, pct_scaled - 1), scale)}%",
            f"{_int_scale_to_decimal_string(pct_scaled * 10, scale)}%",
        ]
        options = list(dict.fromkeys([f"{pct}%", *wrong]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=f"{pct}%", explanation=explanation)

    if qtype == 'scaffold':
        steps = ['Convert the fraction to a decimal.', 'Multiply by 100.', 'Add %.']
        checkpoints = [
            {
                'id': 'cp_dec',
                'prompt': 'Write the decimal value (no %).',
                'kind': 'typed',
                'correct_answer': dec,
                'explanation': f"{frac} = {dec}."
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the percentage.',
                'kind': 'typed',
                'correct_answer': f"{pct}%",
                'explanation': explanation
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=f"{pct}%", explanation=explanation)

    return _make_typed(prompt=prompt, correct_answer=f"{pct}%", explanation=explanation)


def _gen_decimal_add_sub(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    dp = rng.choice([1, 2] if difficulty == 'easy' else [2, 3])
    a_scaled = rng.randint(1, 2000)
    b_scaled = rng.randint(1, 2000)
    scale = 10 ** dp
    op = rng.choice(['+', '-'])

    a = _int_scale_to_decimal_string(a_scaled, scale)
    b = _int_scale_to_decimal_string(b_scaled, scale)

    if op == '+':
        res = a_scaled + b_scaled
        prompt = f"Calculate: {_fmt_decimal_comma(a)} + {_fmt_decimal_comma(b)}"
        explanation = "Align decimal places and add." 
    else:
        if difficulty == 'easy' and a_scaled < b_scaled:
            a_scaled, b_scaled = b_scaled, a_scaled
            a = _int_scale_to_decimal_string(a_scaled, scale)
            b = _int_scale_to_decimal_string(b_scaled, scale)
        res = a_scaled - b_scaled
        prompt = f"Calculate: {_fmt_decimal_comma(a)} − {_fmt_decimal_comma(b)}"
        explanation = "Align decimal places and subtract." 

    correct = _int_scale_to_decimal_string(res, scale)

    if qtype == 'mcq':
        options = list(dict.fromkeys([
            correct,
            _int_scale_to_decimal_string(res + 1, scale),
            _int_scale_to_decimal_string(max(0, res - 1), scale),
            _int_scale_to_decimal_string(res, scale * 10),
        ]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=f"{explanation} Answer: {correct}.")

    if qtype == 'scaffold':
        steps = ['Line up decimal points.', 'Add/subtract as whole numbers.', 'Place the decimal point back.']
        checkpoints = [
            {
                'id': 'cp_scale',
                'prompt': 'How many decimal places are used here?',
                'kind': 'typed',
                'correct_answer': str(dp),
                'explanation': f"There are {dp} decimal places."
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the final answer.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': f"{explanation} Answer: {correct}."
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=f"{explanation} Answer: {correct}.")

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=f"{explanation} Answer: {correct}.")


def _gen_decimal_mul(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    dp1 = rng.choice([1] if difficulty == 'easy' else [1, 2])
    dp2 = rng.choice([1] if difficulty == 'easy' else [1, 2])
    a_scaled = rng.randint(1, 400 if difficulty == 'easy' else 2000)
    b_scaled = rng.randint(1, 400 if difficulty == 'easy' else 2000)
    scale1 = 10 ** dp1
    scale2 = 10 ** dp2

    a = _int_scale_to_decimal_string(a_scaled, scale1)
    b = _int_scale_to_decimal_string(b_scaled, scale2)

    res_scaled = a_scaled * b_scaled
    res_scale = scale1 * scale2
    correct = _int_scale_to_decimal_string(res_scaled, res_scale)

    prompt = f"Calculate: {_fmt_decimal_comma(a)} × {_fmt_decimal_comma(b)}"
    explanation = "Multiply as whole numbers, then place the decimal point using total decimal places." 

    if qtype == 'mcq':
        options = list(dict.fromkeys([
            correct,
            _int_scale_to_decimal_string(res_scaled, res_scale * 10),
            _int_scale_to_decimal_string(res_scaled, max(1, res_scale // 10)),
            _int_scale_to_decimal_string(res_scaled + 1, res_scale),
        ]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=f"{explanation} Answer: {correct}.")

    if qtype == 'scaffold':
        steps = ['Count decimal places in each number.', 'Multiply ignoring decimals.', 'Place the decimal using the total decimal places.']
        checkpoints = [
            {
                'id': 'cp_dp',
                'prompt': 'How many decimal places in total?',
                'kind': 'typed',
                'correct_answer': str(dp1 + dp2),
                'explanation': f"Total decimal places = {dp1} + {dp2} = {dp1 + dp2}."
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the final answer.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': f"{explanation} Answer: {correct}."
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=f"{explanation} Answer: {correct}.")

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=f"{explanation} Answer: {correct}.")


def _gen_decimal_div(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # build a division that results in a clean terminating decimal.
    dp = rng.choice([1, 2] if difficulty != 'hard' else [2, 3])
    divisor_dp = rng.choice([1] if difficulty == 'easy' else [1, 2])

    divisor_scaled = rng.choice([2, 3, 4, 5, 6, 7, 8, 9]) * (10 ** max(0, divisor_dp - 1))
    divisor_scale = 10 ** divisor_dp

    # choose integer quotient then compute dividend
    quotient = rng.randint(2, 50 if difficulty != 'hard' else 120)
    dividend_scaled = quotient * divisor_scaled
    dividend_scale = divisor_scale

    dividend = _int_scale_to_decimal_string(dividend_scaled, dividend_scale)
    divisor = _int_scale_to_decimal_string(divisor_scaled, divisor_scale)

    correct = str(quotient)
    prompt = f"Calculate: {_fmt_decimal_comma(dividend)} ÷ {_fmt_decimal_comma(divisor)}"
    explanation = "Multiply numerator and denominator by a power of 10 to make the divisor a whole number, then divide." 

    if qtype == 'mcq':
        options = list(dict.fromkeys([
            correct,
            str(quotient + 1),
            str(max(0, quotient - 1)),
            str(quotient * 10),
        ]))[:4]
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=f"{explanation} Answer: {correct}.")

    if qtype == 'scaffold':
        steps = ['Multiply both numbers by the same power of ten to clear decimals.', 'Divide.']
        checkpoints = [
            {
                'id': 'cp_op',
                'prompt': 'What do we do to clear decimals in division? Type: multiply both by a power of ten',
                'kind': 'typed',
                'correct_answer': 'multiply both by a power of ten',
                'explanation': 'Use equivalent fractions: multiply numerator and denominator by the same power of 10.'
            },
            {
                'id': 'cp_final',
                'prompt': 'Write the final answer.',
                'kind': 'typed',
                'correct_answer': correct,
                'explanation': f"{explanation} Answer: {correct}."
            }
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=f"{explanation} Answer: {correct}.")

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=f"{explanation} Answer: {correct}.")


def generate_grade9_decimal_notation_question(
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
        'decimal_to_fraction': _gen_decimal_to_fraction,
        'fraction_to_decimal': _gen_fraction_to_decimal,
        'percent_to_fraction': _gen_percent_to_fraction,
        'decimal_to_percent': _gen_decimal_to_percent,
        'fraction_to_percent': _gen_fraction_to_percent,
        'decimal_add_sub': _gen_decimal_add_sub,
        'decimal_multiply': _gen_decimal_mul,
        'decimal_divide': _gen_decimal_div,
    }

    if subskill == 'mixed':
        subskill = rng.choice(list(generators.keys()))

    if subskill not in generators:
        subskill = 'decimal_to_fraction'

    q = generators[subskill](rng, difficulty, question_type)

    q_full = {
        'id': _make_id('g9_dec'),
        'topic': 'grade9_decimal_notation',
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    if subskill in {'decimal_to_fraction', 'fraction_to_decimal', 'percent_to_fraction', 'decimal_to_percent', 'fraction_to_percent'}:
        q_full['table'] = _csv_equivalents_table()

    _validate_question(q_full)
    return q_full
