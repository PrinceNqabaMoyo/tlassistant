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


def _pick_int(rng: random.Random, low: int, high: int) -> int:
    return rng.randint(low, high)


def _fmt_int(n: int) -> str:
    return str(n)


def _gen_number_line_fill(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Similar to the doc's missing numbers on a number line.
    step = 1 if difficulty == 'easy' else rng.choice([1, 2, 5])
    start = rng.randint(-10, 0) if difficulty != 'hard' else rng.randint(-30, -5)
    length = 9 if difficulty != 'hard' else 11
    values = [start + step * i for i in range(length)]
    hidden_count = 3 if difficulty == 'easy' else (4 if difficulty == 'medium' else 5)
    hide_idxs = sorted(rng.sample(range(length), hidden_count))
    shown = []
    missing = []
    for i, v in enumerate(values):
        if i in hide_idxs:
            shown.append('□')
            missing.append(v)
        else:
            shown.append(str(v))
    prompt = f"Fill in the missing integers on this number line sequence (step {step}): " + ', '.join(shown)
    correct = ', '.join(str(v) for v in missing)
    explanation = 'Integers increase by the constant step size each tick.'

    if qtype == 'mcq':
        # Make distractors by nudging one value.
        opt1 = correct
        opt2 = ', '.join(str(v + step) for v in missing)
        opt3 = ', '.join(str(v - step) for v in missing)
        opt4 = ', '.join(str(v + rng.choice([-1, 1])) for v in missing)
        options = list(dict.fromkeys([opt1, opt2, opt3, opt4]))
        while len(options) < 4:
            options.append(opt1)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=opt1, explanation=explanation, parameters={'step': step, 'start': start, 'missing': missing})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'step': step, 'start': start, 'missing': missing})


def _gen_compare_integers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    lo = -50 if difficulty == 'hard' else -20
    hi = 50 if difficulty == 'hard' else 20
    a = _pick_int(rng, lo, hi)
    b = _pick_int(rng, lo, hi)
    while b == a:
        b = _pick_int(rng, lo, hi)

    correct = '>' if a > b else '<'
    prompt = f"Insert < or > to make the statement true: {a} ? {b}"
    explanation = 'On the number line, numbers further right are greater.'

    if qtype == 'mcq':
        options = ['<', '>', '=']
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b})


def _gen_add_sub_integers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    lo = -30 if difficulty == 'hard' else -15
    hi = 30 if difficulty == 'hard' else 15
    a = _pick_int(rng, lo, hi)
    b = _pick_int(rng, lo, hi)
    op = rng.choice(['+', '-'])

    if op == '+':
        ans = a + b
        prompt = f"Calculate: {a} + ({b})"
        explanation = 'Add integers (adding a negative moves left, adding a positive moves right).'
    else:
        ans = a - b
        prompt = f"Calculate: {a} − ({b})"
        explanation = 'Subtracting a number is the same as adding its additive inverse.'

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Rewrite using addition only: {a} {op} ({b}) = {a} + ( ? )",
                'correct_answer': str(b if op == '+' else -b),
                'explanation': 'Change subtraction to adding the opposite.'
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final answer:',
                'correct_answer': str(ans),
                'explanation': explanation,
            }
        ]
        steps = [
            'If you see subtraction, rewrite it as adding the opposite.',
            'Combine positives and negatives to get the final integer.'
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=str(ans), explanation=explanation, parameters={'a': a, 'b': b, 'op': op})

    if qtype == 'mcq':
        options = [str(ans), str(ans + 1), str(ans - 1), str(-ans)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=str(ans), explanation=explanation, parameters={'a': a, 'b': b, 'op': op})

    return _make_typed(prompt=prompt, correct_answer=str(ans), explanation=explanation, parameters={'a': a, 'b': b, 'op': op})


def _gen_multiply_divide_integers(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    a_mag = rng.randint(2, 12) if difficulty != 'hard' else rng.randint(5, 20)
    b_mag = rng.randint(2, 12) if difficulty != 'hard' else rng.randint(5, 20)
    a = a_mag * rng.choice([-1, 1])
    b = b_mag * rng.choice([-1, 1])

    op = rng.choice(['×', '÷'])
    if op == '×':
        ans = a * b
        prompt = f"Calculate: ({a}) × ({b})"
        explanation = 'Same signs give positive; different signs give negative.'
    else:
        # Ensure divisible
        ans = a_mag
        prod = ans * b
        a = prod
        ans = int(a / b)
        prompt = f"Calculate: ({a}) ÷ ({b})"
        explanation = 'Division sign rules match multiplication sign rules.'

    if qtype == 'mcq':
        options = [str(ans), str(-ans), str(ans + 1), str(ans - 1)]
        options = list(dict.fromkeys(options))[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=str(ans), explanation=explanation, parameters={'a': a, 'b': b, 'op': op})

    return _make_typed(prompt=prompt, correct_answer=str(ans), explanation=explanation, parameters={'a': a, 'b': b, 'op': op})


def generate_grade8_integers_question(
    *,
    subskill: str = 'integers',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed if seed is not None else time.time_ns())

    topic = 'Integers'
    subskill = str(subskill or 'integers')
    difficulty = str(difficulty or 'easy')
    question_type = str(question_type or 'typed')

    # Map broad/"mixed" to a random supported subskill
    supported = [
        'number_line_fill',
        'compare_integers',
        'add_sub_integers',
        'multiply_divide_integers',
    ]

    if subskill in {'integers', 'mixed'}:
        subskill = rng.choice(supported)

    generators = {
        'number_line_fill': _gen_number_line_fill,
        'compare_integers': _gen_compare_integers,
        'add_sub_integers': _gen_add_sub_integers,
        'multiply_divide_integers': _gen_multiply_divide_integers,
    }

    if subskill not in generators:
        subskill = rng.choice(supported)

    qtype = question_type
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    q = generators[subskill](rng, difficulty, qtype)

    out = {
        'id': _make_id('g8_int'),
        'topic': topic,
        'subskill': subskill,
        'difficulty': difficulty,
        **q,
    }

    _validate_question(out)
    return out
