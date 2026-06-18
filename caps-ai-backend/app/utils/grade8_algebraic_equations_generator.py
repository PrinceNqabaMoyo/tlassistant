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


def _choice(rng: random.Random, xs: List[Any]) -> Any:
    return xs[int(rng.randrange(0, len(xs)))]


def _fmt_int(n: int) -> str:
    return str(int(n))


def _normalize(s: str) -> str:
    return str(s).strip().replace('−', '-').replace(' ', '')


def _solve_linear(a: int, b: int, c: int) -> Optional[int]:
    # Solve a*x + b = c for integer x
    if a == 0:
        return None
    num = c - b
    if num % a != 0:
        return None
    return int(num // a)


def _gen_truth_check(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # "Is the equation true for x = value?" (yes/no)
    a_choices = [1, 2, 3, 4, 5] if difficulty == 'easy' else ([1, 2, 3, 4, 5, 6] if difficulty == 'medium' else [2, 3, 4, 5, 6, 7, 8])
    a = int(_choice(rng, a_choices))

    b = int(_choice(rng, [-10, -7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7, 10]))
    x_val = int(_choice(rng, [-3, -2, -1, 0, 1, 2, 3, 4, 5] if difficulty != 'easy' else [0, 1, 2, 3, 4]))

    lhs = a * x_val + b

    # Decide whether to make it true or false
    make_true = bool(_choice(rng, [True, False]))
    rhs = lhs if make_true else lhs + int(_choice(rng, [-5, -3, -2, -1, 1, 2, 3, 5]))

    eq = f"{a}x" + (f" + {b}" if b > 0 else (f" - {abs(b)}" if b < 0 else ''))
    prompt = f"Is the statement true? {eq} = {rhs} when x = {x_val}. (yes/no)"

    correct = 'yes' if make_true else 'no'
    explanation = f"Substitute x = {x_val}: left side = {a}×{x_val} {('+' if b >= 0 else '-') } {abs(b)} = {lhs}. Compare with {rhs}." if b != 0 else f"Substitute x = {x_val}: left side = {a}×{x_val} = {lhs}. Compare with {rhs}."

    if qtype == 'mcq':
        return _make_mcq(prompt=prompt, options=['yes', 'no'], correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'x': x_val, 'rhs': rhs})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Calculate the left side value when x = {x_val}.",
                'correct_answer': _fmt_int(lhs),
                'explanation': 'Substitute and calculate the left side.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Is {lhs} equal to {rhs}? (yes/no)",
                'correct_answer': correct,
                'explanation': 'An equation is true only if both sides are equal.',
            },
        ]
        steps = [
            'Substitute the given value for x.',
            'Calculate the left-hand side.',
            'Compare left-hand side with the right-hand side.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'x': x_val, 'rhs': rhs})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'x': x_val, 'rhs': rhs})


def _gen_solve_linear_one_step(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Solve ax = c OR x + b = c OR x - b = c
    pattern = _choice(rng, ['ax_equals_c', 'x_plus_b', 'x_minus_b'])

    if pattern == 'ax_equals_c':
        a = int(_choice(rng, [2, 3, 4, 5, 6, 8, 10] if difficulty != 'hard' else [2, 3, 4, 5, 6, 7, 8, 9, 10, 12]))
        x = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6] if difficulty != 'easy' else [1, 2, 3, 4, 5, 6]))
        c = a * x
        eq = f"{a}x = {c}"
        prompt = f"Solve for x: {eq}"
        correct = _fmt_int(x)
        explanation = f"Divide both sides by {a}: x = {c} ÷ {a} = {x}."
        inverse_step = f"Divide both sides by {a}."
    elif pattern == 'x_plus_b':
        b = int(_choice(rng, [2, 3, 4, 5, 7, 8, 10] if difficulty != 'hard' else [1, 2, 3, 4, 5, 7, 8, 10, 12, 15]))
        x = int(_choice(rng, [-10, -7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7, 10]))
        c = x + b
        eq = f"x + {b} = {c}"
        prompt = f"Solve for x: {eq}"
        correct = _fmt_int(x)
        explanation = f"Subtract {b} from both sides: x = {c} − {b} = {x}."
        inverse_step = f"Subtract {b} from both sides."
    else:
        b = int(_choice(rng, [2, 3, 4, 5, 7, 8, 10] if difficulty != 'hard' else [1, 2, 3, 4, 5, 7, 8, 10, 12, 15]))
        x = int(_choice(rng, [-10, -7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7, 10]))
        c = x - b
        eq = f"x - {b} = {c}"
        prompt = f"Solve for x: {eq}"
        correct = _fmt_int(x)
        explanation = f"Add {b} to both sides: x = {c} + {b} = {x}."
        inverse_step = f"Add {b} to both sides."

    if qtype == 'mcq':
        opt1 = correct
        opt2 = _fmt_int(int(correct) + 1)
        opt3 = _fmt_int(int(correct) - 1)
        opt4 = _fmt_int(int(correct) + int(_choice(rng, [2, -2, 3, -3])))
        options = list(dict.fromkeys([opt1, opt2, opt3, opt4]))
        while len(options) < 4:
            options.append(opt1)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=opt1, explanation=explanation, parameters={'pattern': pattern, 'equation': eq})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'What single inverse operation should you do first?',
                'correct_answer': inverse_step,
                'explanation': 'Use the inverse of the operation applied to x.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final value of x:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Identify what is being done to x.',
            'Do the inverse operation on both sides.',
            'Check by substitution.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'pattern': pattern, 'equation': eq})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'pattern': pattern, 'equation': eq})


def _gen_solve_linear_two_step(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Solve ax + b = c with integer solution
    a = int(_choice(rng, [2, 3, 4, 5, 6] if difficulty != 'hard' else [2, 3, 4, 5, 6, 7, 8, 9]))
    b = int(_choice(rng, [-12, -10, -8, -7, -5, -3, -2, 2, 3, 5, 7, 8, 10, 12]))

    x = int(_choice(rng, [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6] if difficulty != 'easy' else [1, 2, 3, 4, 5, 6]))
    c = a * x + b

    eq = f"{a}x" + (f" + {b}" if b > 0 else (f" - {abs(b)}" if b < 0 else '')) + f" = {c}"
    prompt = f"Solve for x: {eq}"
    correct = _fmt_int(x)
    explanation = f"Subtract {b} from both sides, then divide by {a}."

    if qtype == 'mcq':
        opt1 = correct
        opt2 = _fmt_int(x + 1)
        opt3 = _fmt_int(x - 1)
        opt4 = _fmt_int(x + int(_choice(rng, [2, -2, 3, -3])))
        options = list(dict.fromkeys([opt1, opt2, opt3, opt4]))
        while len(options) < 4:
            options.append(opt1)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=opt1, explanation=explanation, parameters={'a': a, 'b': b, 'c': c})

    if qtype == 'scaffold':
        rhs_after = c - b
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"First undo the +/− {abs(b)} term. What is the new right-hand side after moving b?",
                'correct_answer': _fmt_int(rhs_after),
                'explanation': 'Add/subtract the constant term on both sides to isolate the ax term.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Now solve {a}x = {rhs_after}. What is x?",
                'correct_answer': correct,
                'explanation': f"Divide by {a}.",
            },
        ]
        steps = [
            'Move the constant term to the other side (add/subtract).',
            'Divide by the coefficient of x.',
            'Check by substitution.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'a': a, 'b': b, 'c': c})


def generate_grade8_algebraic_equations_question(
    *,
    subskill: str = 'algebraic_equations',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed)

    topic = 'Algebraic equations 1'
    difficulty = (difficulty or 'easy').lower()
    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    qtype = (question_type or 'typed').lower()
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    subskill = (subskill or 'algebraic_equations').lower()

    generators = {
        'truth_check': _gen_truth_check,
        'solve_linear_one_step': _gen_solve_linear_one_step,
        'solve_linear_two_step': _gen_solve_linear_two_step,
    }

    if subskill not in generators:
        order = ['truth_check', 'solve_linear_one_step', 'solve_linear_two_step']
        subskill = order[int(rng.randrange(0, len(order)))]

    gen = generators[subskill]
    q = gen(rng, difficulty, qtype)

    q.update(
        {
            'id': _make_id('g8_algeq'),
            'topic': topic,
            'subskill': subskill,
            'difficulty': difficulty,
        }
    )

    q['_normalized_correct_answer'] = _normalize(q.get('correct_answer', ''))

    _validate_question(q)
    return q
