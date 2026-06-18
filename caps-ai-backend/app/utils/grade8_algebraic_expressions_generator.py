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


def _fmt_term(coef: int, var: str) -> str:
    if coef == 0:
        return '0'
    if coef == 1:
        return var
    if coef == -1:
        return f"-{var}"
    return f"{coef}{var}"


def _join_sum(terms: List[str]) -> str:
    # terms are already signed or unsiged; we normalize to a + b - c form
    out: List[str] = []
    for t in terms:
        t = str(t).strip()
        if not t:
            continue
        if not out:
            out.append(t)
        else:
            if t.startswith('-'):
                out.append(f"- {t[1:]}")
            else:
                out.append(f"+ {t}")
    return ' '.join(out) if out else '0'


def _normalize_expr(expr: str) -> str:
    return (
        str(expr)
        .strip()
        .replace('−', '-')
        .replace('×', '*')
        .replace(' ', '')
        .lower()
    )


def _gen_algebraic_language_translate(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Word/flow descriptions -> algebraic expression
    var = 'x'
    mult_choices = [2, 3, 4, 5] if difficulty == 'easy' else ([2, 3, 4, 5, 6] if difficulty == 'medium' else [2, 3, 4, 5, 6, 7, 8])
    add_choices = [1, 2, 3, 4, 5, 6, 7] if difficulty != 'hard' else [2, 3, 4, 5, 6, 7, 8, 9, 10]

    m = int(_choice(rng, mult_choices))
    k = int(_choice(rng, add_choices))

    pattern = _choice(rng, ['multiply_then_add', 'add_then_multiply', 'multiply_then_subtract'])

    if pattern == 'multiply_then_add':
        words = f"Multiply a number by {m} and add {k} to the answer."
        correct = f"{m}{var}+{k}"
        hint_expr = f"({var} × {m}) then +{k}"
        explanation = 'Write multiplication next to the variable (omit ×) and then add the constant.'
    elif pattern == 'multiply_then_subtract':
        words = f"Multiply a number by {m} and subtract {k} from the answer."
        correct = f"{m}{var}-{k}"
        hint_expr = f"({var} × {m}) then -{k}"
        explanation = 'Write multiplication next to the variable (omit ×) and then subtract the constant.'
    else:
        # parentheses introduced
        words = f"Add {k} to a number and then multiply the answer by {m}."
        correct = f"{m}({var}+{k})"
        hint_expr = f"({var} + {k}) then ×{m}"
        explanation = 'When you add first and then multiply, use brackets: m(x + k).'

    prompt = f"Write the algebraic expression (in normal algebraic language) for: {words}"

    if qtype == 'mcq':
        opt1 = correct
        # common distractors
        opt2 = f"{m}{var}+{k}" if correct != f"{m}{var}+{k}" else f"{m}{var}-{k}"
        opt3 = f"{var}{m}+{k}"
        opt4 = f"{m}({var}-{k})" if pattern == 'add_then_multiply' else f"{m}({var}+{k})"
        options = list(dict.fromkeys([opt1, opt2, opt3, opt4]))
        while len(options) < 4:
            options.append(opt1)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=opt1, explanation=explanation, parameters={'m': m, 'k': k, 'pattern': pattern, 'hint': hint_expr})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"What is the variable used for the number?",
                'correct_answer': var,
                'explanation': 'We use x to represent an unknown number.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Write the operation order in words (e.g. 'multiply then add'): {hint_expr}",
                'correct_answer': 'multiply then add' if pattern == 'multiply_then_add' else ('multiply then subtract' if pattern == 'multiply_then_subtract' else 'add then multiply'),
                'explanation': 'Identify the order to decide whether you need brackets.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final expression:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Let the unknown number be x.',
            'Follow the order of operations described in the words/flow.',
            'Use brackets if you add/subtract before multiplying.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'m': m, 'k': k, 'pattern': pattern, 'hint': hint_expr})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'m': m, 'k': k, 'pattern': pattern, 'hint': hint_expr})


def _eval_linear_expr(x: int, coef: int, const: int) -> int:
    return coef * x + const


def _gen_substitution_evaluate(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Evaluate an expression by substitution
    coef_choices = [1, 2, 3, 4, 5, 6] if difficulty != 'hard' else [2, 3, 4, 5, 6, 7, 8, 9]
    const_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] if difficulty == 'easy' else [ -10, -7, -5, -3, -2, 0, 2, 3, 5, 7, 10]

    coef = int(_choice(rng, coef_choices))
    const = int(_choice(rng, const_choices))

    x_choices = [1, 3, 7, 10] if difficulty == 'easy' else ([-3, -2, -1, 0, 1, 2, 3, 4] if difficulty == 'medium' else [-5, -3, -2, -1, 0, 1, 2, 3, 5, 7])
    x_val = int(_choice(rng, x_choices))

    expr = f"{coef}x" if const == 0 else (f"{coef}x+{const}" if const > 0 else f"{coef}x{const}")
    val = _eval_linear_expr(x_val, coef, const)

    prompt = f"Evaluate the expression {expr} for x = {x_val}."
    correct = str(val)
    explanation = f"Substitute x = {x_val}: {expr} = {coef}×{x_val} {('+' if const >= 0 else '-') } {abs(const)} = {val}." if const != 0 else f"Substitute x = {x_val}: {coef}×{x_val} = {val}."

    if qtype == 'mcq':
        opt1 = correct
        opt2 = str(_eval_linear_expr(x_val + 1, coef, const))
        opt3 = str(_eval_linear_expr(x_val, coef + 1, const))
        opt4 = str(val + _choice(rng, [1, -1, 2, -2]))
        options = list(dict.fromkeys([opt1, opt2, opt3, opt4]))
        while len(options) < 4:
            options.append(opt1)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=opt1, explanation=explanation, parameters={'coef': coef, 'const': const, 'x': x_val})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Write the substitution (replace x): {expr} with x = {x_val}.",
                'correct_answer': f"{coef}×{x_val}{'+' + str(const) if const > 0 else (str(const) if const < 0 else '')}".replace('+-', '-'),
                'explanation': 'Replace x with the given value.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final value:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Substitute the given value for x.',
            'Do multiplication first.',
            'Then add/subtract the constant term.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'coef': coef, 'const': const, 'x': x_val})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'coef': coef, 'const': const, 'x': x_val})


def _gen_like_unlike_terms(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Decide whether two terms are like terms
    var_options = ['x', 'y', 'm', 'n'] if difficulty != 'hard' else ['x', 'y', 'm', 'n', 'a', 'b']
    v1 = str(_choice(rng, var_options))
    same = bool(_choice(rng, [True, False]))

    power_choices = [1, 2, 3] if difficulty == 'hard' else [1, 2]
    p1 = int(_choice(rng, power_choices))
    p2 = p1 if same else int(_choice(rng, [p for p in power_choices if p != p1]))

    coef1 = int(_choice(rng, [2, 3, 4, 5, 6, 7, 8, 9]))
    coef2 = int(_choice(rng, [2, 3, 4, 5, 6, 7, 8, 9]))

    def term(var: str, p: int, c: int) -> str:
        if p == 1:
            return _fmt_term(c, var)
        return _fmt_term(c, f"{var}^{p}")

    if same:
        v2 = v1
    else:
        v2 = str(_choice(rng, [v for v in var_options if v != v1]))

    t1 = term(v1, p1, coef1)
    t2 = term(v2, p2, coef2)

    are_like = (v1 == v2) and (p1 == p2)

    prompt = f"Are the terms {t1} and {t2} like terms? (yes/no)"
    correct = 'yes' if are_like else 'no'
    explanation = 'Like terms have the same variable(s) raised to the same power. Coefficients may differ.'

    if qtype == 'mcq':
        options = ['yes', 'no']
        return _make_mcq(prompt=prompt, options=options, correct_answer=correct, explanation=explanation, parameters={'t1': t1, 't2': t2, 'like': are_like})

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Identify the variable and power in the first term {t1} (format: variable^power, e.g. x^2):",
                'correct_answer': f"{v1}^{p1}",
                'explanation': 'Ignore the coefficient, focus on the variable and exponent.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': f"Identify the variable and power in the second term {t2}:",
                'correct_answer': f"{v2}^{p2}",
                'explanation': 'Ignore the coefficient, focus on the variable and exponent.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Are they like terms? (yes/no)',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Ignore the coefficients.',
            'Compare the variables.',
            'Compare the exponents (powers).',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters={'t1': t1, 't2': t2, 'like': are_like})

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters={'t1': t1, 't2': t2, 'like': are_like})


def _gen_simplify_like_terms(rng: random.Random, difficulty: str, qtype: str) -> Dict[str, Any]:
    # Simplify by combining like terms
    var = str(_choice(rng, ['x', 'y', 'm']))
    include_square = difficulty != 'easy' and bool(_choice(rng, [True, False]))

    c1 = int(_choice(rng, [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    c2 = int(_choice(rng, [2, 3, 4, 5, 6, 7, 8])) * int(_choice(rng, [1, -1]))
    const1 = int(_choice(rng, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    const2 = int(_choice(rng, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) * int(_choice(rng, [1, -1]))

    lin = _join_sum([_fmt_term(c1, var), _fmt_term(c2, var), str(const1), str(const2)])

    if include_square:
        s1 = int(_choice(rng, [2, 3, 4, 5, 6]))
        s2 = int(_choice(rng, [2, 3, 4, 5, 6])) * int(_choice(rng, [1, -1]))
        expr = _join_sum([_fmt_term(s1, f"{var}^2"), _fmt_term(s2, f"{var}^2"), lin])
        a = s1 + s2
        b = c1 + c2
        c = const1 + const2
        simplified_terms = []
        if a != 0:
            simplified_terms.append(_fmt_term(a, f"{var}^2"))
        if b != 0:
            simplified_terms.append(_fmt_term(b, var))
        if c != 0:
            simplified_terms.append(str(c))
        simplified = _join_sum(simplified_terms)
        parameters = {'var': var, 'a': a, 'b': b, 'c': c, 'include_square': True}
    else:
        expr = lin
        b = c1 + c2
        c = const1 + const2
        simplified_terms = []
        if b != 0:
            simplified_terms.append(_fmt_term(b, var))
        if c != 0:
            simplified_terms.append(str(c))
        simplified = _join_sum(simplified_terms)
        parameters = {'var': var, 'b': b, 'c': c, 'include_square': False}

    prompt = f"Simplify: {expr}"
    correct = simplified
    explanation = 'Rearrange and combine like terms (same variable and power), and combine constants.'

    if qtype == 'mcq':
        opt1 = correct
        # distractors: wrong coefficient or wrong constant
        opt2 = _join_sum([_fmt_term(parameters.get('b', 0) + 1, var), str(parameters.get('c', 0))])
        opt3 = _join_sum([_fmt_term(parameters.get('b', 0), var), str(parameters.get('c', 0) + 1)])
        opt4 = expr.replace(' + ', ' - ') if ' + ' in expr else expr
        options = list(dict.fromkeys([opt1, opt2, opt3, opt4]))
        while len(options) < 4:
            options.append(opt1)
            options = list(dict.fromkeys(options))
        options = options[:4]
        rng.shuffle(options)
        return _make_mcq(prompt=prompt, options=options, correct_answer=opt1, explanation=explanation, parameters=parameters)

    if qtype == 'scaffold':
        checkpoints = [
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Write the like-term groups you can combine (e.g. x terms, x^2 terms, constants):',
                'correct_answer': 'x terms, constants' if not include_square else 'x^2 terms, x terms, constants',
                'explanation': 'Like terms share the same variable and exponent; constants have no variable.',
            },
            {
                'id': _make_id('cp'),
                'kind': 'typed',
                'prompt': 'Final simplified expression:',
                'correct_answer': correct,
                'explanation': explanation,
            },
        ]
        steps = [
            'Reorder terms so like terms are together.',
            'Add/subtract coefficients of like terms.',
            'Combine constants.',
        ]
        return _make_scaffold(prompt=prompt, steps=steps, checkpoints=checkpoints, final_answer=correct, explanation=explanation, parameters=parameters)

    return _make_typed(prompt=prompt, correct_answer=correct, explanation=explanation, parameters=parameters)


def generate_grade8_algebraic_expressions_question(
    *,
    subskill: str = 'algebraic_expressions',
    difficulty: str = 'easy',
    question_type: str = 'typed',
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    rng = random.Random(seed)

    topic = 'Algebraic expressions 1'
    difficulty = (difficulty or 'easy').lower()
    if difficulty not in {'easy', 'medium', 'hard'}:
        difficulty = 'easy'

    qtype = (question_type or 'typed').lower()
    if qtype not in {'typed', 'mcq', 'scaffold'}:
        qtype = 'typed'

    subskill = (subskill or 'algebraic_expressions').lower()

    generators = {
        'algebraic_language_translate': _gen_algebraic_language_translate,
        'substitution_evaluate': _gen_substitution_evaluate,
        'like_unlike_terms': _gen_like_unlike_terms,
        'simplify_like_terms': _gen_simplify_like_terms,
    }

    if subskill not in generators:
        # default: pick one based on difficulty
        order = ['algebraic_language_translate', 'substitution_evaluate', 'like_unlike_terms', 'simplify_like_terms']
        subskill = order[int(rng.randrange(0, len(order)))]

    gen = generators[subskill]
    q = gen(rng, difficulty, qtype)

    q.update(
        {
            'id': _make_id('g8_algexp'),
            'topic': topic,
            'subskill': subskill,
            'difficulty': difficulty,
        }
    )

    # Lightweight normalization sanity check for generator outputs
    q['_normalized_correct_answer'] = _normalize_expr(q.get('correct_answer', ''))

    _validate_question(q)
    return q
