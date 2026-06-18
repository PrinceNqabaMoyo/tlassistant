import random
import time
from typing import Optional

def _make_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"


def _pick_nonzero_digit(rng: random.Random) -> int:
    return rng.randint(1, 9)


def _generate_place_value_number(rng: random.Random, digits: int) -> int:
    if digits < 2:
        digits = 2
    if digits > 9:
        digits = 9

    first = _pick_nonzero_digit(rng)
    rest = [rng.randint(0, 9) for _ in range(digits - 1)]
    return int(str(first) + ''.join(str(d) for d in rest))


def _format_with_spaces(n: int) -> str:
    return f"{n:,}".replace(',', ' ')


def _expanded_sum_parts(rng: random.Random, digits: int):
    number = _generate_place_value_number(rng, digits)
    parts = []
    place = 1
    n = number
    while n > 0:
        digit = n % 10
        if digit:
            parts.append(digit * place)
        n //= 10
        place *= 10
    parts.reverse()
    return number, parts


def _round_to_base(n: int, base: int) -> int:
    return int(base * round(n / base))


def _number_to_words_upto_999999(n: int) -> str:
    ones = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }
    teens = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }
    tens_words = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    }

    def _two_digits(x: int) -> str:
        if x < 10:
            return ones[x]
        if 10 <= x < 20:
            return teens[x]
        t = x // 10
        u = x % 10
        if u == 0:
            return tens_words[t]
        return f"{tens_words[t]} {ones[u]}"

    def _three_digits(x: int) -> str:
        if x < 100:
            return _two_digits(x)
        h = x // 100
        rest = x % 100
        if rest == 0:
            return f"{ones[h]} hundred"
        return f"{ones[h]} hundred and {_two_digits(rest)}"

    if n < 0:
        return f"minus {_number_to_words_upto_999999(-n)}"
    if n <= 999:
        return _three_digits(n)
    if n <= 999999:
        thousands = n // 1000
        rest = n % 1000
        if rest == 0:
            return f"{_three_digits(thousands)} thousand"
        # Use a space (not 'and') between thousand and the rest; the rest itself may contain 'and'.
        return f"{_three_digits(thousands)} thousand {_three_digits(rest)}"
    return str(n)


def generate_grade7_whole_numbers_question(
    *,
    subskill: str,
    difficulty: str,
    question_type: str,
    seed: Optional[int] = None,
):
    rng = random.Random(seed)

    normalized_subskill = (subskill or '').strip().lower()
    normalized_difficulty = (difficulty or 'easy').strip().lower()
    normalized_qtype = (question_type or 'typed').strip().lower()

    if normalized_difficulty not in {'easy', 'medium', 'hard'}:
        normalized_difficulty = 'easy'

    if normalized_qtype not in {'typed', 'mcq', 'scaffold'}:
        normalized_qtype = 'typed'

    if normalized_subskill not in {
        'rounding',
        'expanded_notation',
        'build_number_from_expanded',
        'compare',
        'place_value',
        'multiples',
        'words_to_number',
        'number_to_words',
        'ordering',
        'doubling_halving',
    } and normalized_qtype == 'scaffold':
        normalized_qtype = 'typed'

    if normalized_subskill in {'', 'whole_numbers'}:
        typed_capable = [
            'build_number_from_expanded',
            'expanded_notation',
            'place_value',
            'compare',
            'rounding',
            'multiples',
            'words_to_number',
            'doubling_halving',
        ]
        mcq_capable = [
            'build_number_from_expanded',
            'place_value',
            'compare',
            'number_to_words',
            'ordering',
        ]

        if normalized_qtype == 'mcq':
            normalized_subskill = rng.choice(mcq_capable)
        else:
            normalized_subskill = rng.choice(typed_capable)

    if normalized_subskill == 'words_to_number':
        digits = {'easy': 3, 'medium': 4, 'hard': 6}[normalized_difficulty]
        n = _generate_place_value_number(rng, digits)
        words = _number_to_words_upto_999999(n)
        question = f"Write this number in digits: {words}."
        explanation = f"The digits form is { _format_with_spaces(n) }."

        if normalized_qtype == 'scaffold':
            str_n = str(n)
            num_digits = len(str_n)
            thousands_part = (n // 1000) * 1000
            checkpoints = [
                {
                    'id': 'c1_digits',
                    'kind': 'mcq',
                    'prompt': 'How many digits will the final number have?'
                    ,
                    'options': [str(max(1, num_digits - 1)), str(num_digits), str(num_digits + 1)],
                    'correct_answer': str(num_digits),
                    'explanation': f"It has {num_digits} digits.",
                },
                {
                    'id': 'c2_thousands',
                    'kind': 'typed',
                    'prompt': 'If there is a “thousand” part, write it as digits (otherwise write 0).',
                    'correct_answer': _format_with_spaces(thousands_part) if n >= 1000 else '0',
                    'explanation': 'This helps you build the number from large place values downwards.',
                },
                {
                    'id': 'c3_final',
                    'kind': 'typed',
                    'prompt': 'Final answer: write the number in digits.',
                    'correct_answer': _format_with_spaces(n),
                    'explanation': explanation,
                },
            ]
            steps = [
                'Read the words and identify the large place values (thousands, hundreds, tens, units).',
                'Build the number from left to right.',
                'Write the final digits clearly (spaces/commas don’t change the value).',
            ]
            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'scaffold',
                'question': question,
                'correct_answer': _format_with_spaces(n),
                'explanation': explanation,
                'steps': steps,
                'checkpoints': checkpoints,
                'parameters': {'number': n, 'words': words, 'digits': digits},
            }

        return {
            'id': _make_id('g7_whole'),
            'topic': 'Whole Numbers',
            'subskill': normalized_subskill,
            'difficulty': normalized_difficulty,
            'question_type': 'typed',
            'question': question,
            'correct_answer': _format_with_spaces(n),
            'explanation': explanation,
            'parameters': {'number': n, 'words': words, 'digits': digits},
        }

    if normalized_subskill == 'number_to_words':
        if normalized_qtype != 'mcq':
            normalized_qtype = 'mcq'
        digits = {'easy': 3, 'medium': 4, 'hard': 6}[normalized_difficulty]
        n = _generate_place_value_number(rng, digits)
        correct_words = _number_to_words_upto_999999(n)
        question = f"Which option shows { _format_with_spaces(n) } in words?"
        # Build distractors by tweaking number slightly
        distractors = set()
        while len(distractors) < 3:
            tweak = rng.choice([-1, 1]) * (10 ** rng.randint(0, min(2, digits - 1)))
            d = max(0, n + tweak)
            if d != n:
                distractors.add(_number_to_words_upto_999999(d))
        options = [correct_words, *sorted(distractors)]
        rng.shuffle(options)
        explanation = f"{ _format_with_spaces(n) } is written as: {correct_words}."

        return {
            'id': _make_id('g7_whole'),
            'topic': 'Whole Numbers',
            'subskill': normalized_subskill,
            'difficulty': normalized_difficulty,
            'question_type': 'mcq',
            'question': question,
            'options': options,
            'correct_answer': correct_words,
            'explanation': explanation,
            'parameters': {'number': n, 'digits': digits},
        }

    if normalized_subskill == 'ordering':
        if normalized_qtype == 'mcq':
            # ok
            pass
        digits = {'easy': 3, 'medium': 4, 'hard': 5}[normalized_difficulty]
        nums = set()
        while len(nums) < 4:
            nums.add(_generate_place_value_number(rng, digits))
        nums = list(nums)
        correct_sorted = sorted(nums)
        correct_list = ', '.join(_format_with_spaces(x) for x in correct_sorted)

        def _make_option(seq):
            return ', '.join(_format_with_spaces(x) for x in seq)

        # Create distractors by shuffling / swapping
        distractors = set()
        while len(distractors) < 3:
            cand = correct_sorted[:]
            rng.shuffle(cand)
            opt = _make_option(cand)
            if opt != correct_list:
                distractors.add(opt)

        options = [correct_list, *sorted(distractors)]
        rng.shuffle(options)
        question = "Which list is ordered from smallest to biggest?"
        explanation = f"Order numbers by comparing from the leftmost digit. Correct order: {correct_list}."

        if normalized_qtype == 'scaffold':
            checkpoints = [
                {
                    'id': 'c1_rule',
                    'kind': 'mcq',
                    'prompt': 'When ordering whole numbers, which digits do you compare first?'
                    ,
                    'options': ['Leftmost digits', 'Rightmost digits', 'Random digits'],
                    'correct_answer': 'Leftmost digits',
                    'explanation': 'Start with the highest place value (leftmost digit).',
                },
                {
                    'id': 'c2_final',
                    'kind': 'mcq',
                    'prompt': f"Choose the correctly ordered list for: { _make_option(nums) }",
                    'options': options,
                    'correct_answer': correct_list,
                    'explanation': explanation,
                },
            ]
            steps = [
                'Look at the number of digits (more digits usually means bigger).',
                'If digits are the same length, compare from the leftmost digit.',
                'Write the order from smallest to biggest.',
            ]
            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'scaffold',
                'question': question,
                'correct_answer': correct_list,
                'explanation': explanation,
                'steps': steps,
                'checkpoints': checkpoints,
                'parameters': {'numbers': nums, 'sorted': correct_sorted},
            }

        return {
            'id': _make_id('g7_whole'),
            'topic': 'Whole Numbers',
            'subskill': normalized_subskill,
            'difficulty': normalized_difficulty,
            'question_type': 'mcq',
            'question': question,
            'options': options,
            'correct_answer': correct_list,
            'explanation': explanation,
            'parameters': {'numbers': nums, 'sorted': correct_sorted},
        }

    if normalized_subskill == 'doubling_halving':
        # Focus on doubling strategy (multiplying by a power of 2)
        multiplier = rng.choice([4, 8, 16]) if normalized_difficulty != 'easy' else rng.choice([4, 8])
        multiplicand = rng.randint(12, 99) if normalized_difficulty != 'easy' else rng.randint(10, 50)
        product = multiplicand * multiplier

        question = f"Use doubling to calculate: {multiplicand} × {multiplier}."
        explanation = f"Doubling repeatedly: {multiplicand} × {multiplier} = { _format_with_spaces(product) }."

        if normalized_qtype == 'scaffold':
            checkpoints = []
            current = multiplicand
            step_mult = 1
            # Build doubling ladder until we reach multiplier
            while step_mult < multiplier:
                step_mult *= 2
                current *= 2
                checkpoints.append(
                    {
                        'id': f"c{len(checkpoints)+1}_double_{step_mult}",
                        'kind': 'typed',
                        'prompt': f"What is {multiplicand} × {step_mult}?",
                        'correct_answer': _format_with_spaces(current),
                        'explanation': 'Double the previous result.',
                    }
                )
            checkpoints.append(
                {
                    'id': 'c_final',
                    'kind': 'typed',
                    'prompt': f"Final answer: {multiplicand} × {multiplier} = ?",
                    'correct_answer': _format_with_spaces(product),
                    'explanation': explanation,
                }
            )
            steps = [
                'Start with the number you are multiplying.',
                'Double step-by-step (×2, ×4, ×8, ×16).',
                'Use the row that matches your multiplier.',
            ]
            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'scaffold',
                'question': question,
                'correct_answer': _format_with_spaces(product),
                'explanation': explanation,
                'steps': steps,
                'checkpoints': checkpoints,
                'parameters': {'multiplicand': multiplicand, 'multiplier': multiplier, 'product': product},
            }

        return {
            'id': _make_id('g7_whole'),
            'topic': 'Whole Numbers',
            'subskill': normalized_subskill,
            'difficulty': normalized_difficulty,
            'question_type': 'typed',
            'question': question,
            'correct_answer': _format_with_spaces(product),
            'explanation': explanation,
            'parameters': {'multiplicand': multiplicand, 'multiplier': multiplier, 'product': product},
        }

    if normalized_subskill == 'build_number_from_expanded':
        digits = {'easy': 4, 'medium': 5, 'hard': 6}[normalized_difficulty]
        number, parts = _expanded_sum_parts(rng, digits)

        question = f"Write this sum as a single number: { ' + '.join(_format_with_spaces(p) for p in parts) }"
        correct_answer = str(number)
        explanation = f"Add the place-value parts to get { _format_with_spaces(number) }."

        if normalized_qtype == 'scaffold':
            num_parts = len(parts)
            first_part = parts[0] if parts else number
            checkpoints = [
                {
                    'id': 'c1_count_parts',
                    'kind': 'mcq',
                    'prompt': 'How many place-value parts are being added? (How many numbers do you see?)',
                    'options': [str(max(1, num_parts - 1)), str(num_parts), str(num_parts + 1)],
                    'correct_answer': str(num_parts),
                    'explanation': f"There are {num_parts} parts in the expanded sum.",
                },
                {
                    'id': 'c2_first_part_value',
                    'kind': 'typed',
                    'prompt': 'What is the value of the first (leftmost) part?',
                    'correct_answer': _format_with_spaces(first_part),
                    'explanation': f"The first part is { _format_with_spaces(first_part) }.",
                },
                {
                    'id': 'c3_final',
                    'kind': 'typed',
                    'prompt': 'Final answer: write the single number.',
                    'correct_answer': _format_with_spaces(number),
                    'explanation': explanation,
                },
            ]

            steps = [
                'Read each place-value part.',
                'Add the parts (you are combining place values).',
                'Write the final number in standard form.',
            ]

            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'scaffold',
                'question': question,
                'correct_answer': _format_with_spaces(number),
                'explanation': explanation,
                'steps': steps,
                'checkpoints': checkpoints,
                'parameters': {'number': number, 'parts': parts, 'digits': digits},
            }

        if normalized_qtype == 'mcq':
            distractors = set()
            while len(distractors) < 3:
                tweak = rng.choice([-1, 1]) * (10 ** rng.randint(0, min(2, digits - 1)))
                d = max(0, number + tweak)
                if d != number:
                    distractors.add(_format_with_spaces(d))
            options = [_format_with_spaces(number), *sorted(distractors)]
            rng.shuffle(options)
            correct_answer = _format_with_spaces(number)
            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'mcq',
                'question': question,
                'options': options,
                'correct_answer': correct_answer,
                'explanation': explanation,
                'parameters': {'number': number, 'parts': parts, 'digits': digits},
            }

        return {
            'id': _make_id('g7_whole'),
            'topic': 'Whole Numbers',
            'subskill': normalized_subskill,
            'difficulty': normalized_difficulty,
            'question_type': 'typed',
            'question': question,
            'correct_answer': _format_with_spaces(number),
            'explanation': explanation,
            'parameters': {'number': number, 'parts': parts, 'digits': digits},
        }

    if normalized_subskill == 'expanded_notation':
        digits = {'easy': 4, 'medium': 5, 'hard': 6}[normalized_difficulty]
        number, parts = _expanded_sum_parts(rng, digits)

        question = f"Write { _format_with_spaces(number) } in expanded notation."
        correct_answer = ' + '.join(_format_with_spaces(p) for p in parts)
        explanation = f"Split the number into place-value parts: {correct_answer}."

        if normalized_qtype == 'scaffold':
            str_num = str(number)
            num_digits = len(str_num)
            first_nonzero_part = parts[0] if parts else number
            checkpoints = [
                {
                    'id': 'c1_digit_count',
                    'kind': 'mcq',
                    'prompt': f"How many digits are in { _format_with_spaces(number) }?",
                    'options': [str(max(2, num_digits - 1)), str(num_digits), str(num_digits + 1)],
                    'correct_answer': str(num_digits),
                    'explanation': f"{ _format_with_spaces(number) } has {num_digits} digits.",
                },
                {
                    'id': 'c2_first_part',
                    'kind': 'typed',
                    'prompt': "What is the value of the leftmost (first) digit?",
                    'correct_answer': _format_with_spaces(first_nonzero_part),
                    'explanation': f"The leftmost digit represents { _format_with_spaces(first_nonzero_part) }.",
                },
                {
                    'id': 'c3_final',
                    'kind': 'typed',
                    'prompt': 'Final answer: write the expanded notation using +.',
                    'correct_answer': correct_answer,
                    'explanation': explanation,
                },
            ]

            steps = [
                'Read the number from left to right.',
                'Identify each digit and its place value.',
                'Write each non-zero digit as a place-value part.',
                'Add the parts using + to form expanded notation.',
            ]

            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'scaffold',
                'question': question,
                'correct_answer': correct_answer,
                'explanation': explanation,
                'steps': steps,
                'checkpoints': checkpoints,
                'parameters': {'number': number, 'parts': parts, 'digits': digits},
            }

        return {
            'id': _make_id('g7_whole'),
            'topic': 'Whole Numbers',
            'subskill': normalized_subskill,
            'difficulty': normalized_difficulty,
            'question_type': 'typed',
            'question': question,
            'correct_answer': correct_answer,
            'explanation': explanation,
            'parameters': {'number': number, 'parts': parts, 'digits': digits},
        }

    if normalized_subskill == 'place_value':
        digits = {'easy': 4, 'medium': 6, 'hard': 8}[normalized_difficulty]
        number = _generate_place_value_number(rng, digits)
        str_num = str(number)
        idx = rng.randrange(0, len(str_num))
        digit = int(str_num[idx])
        place_power = len(str_num) - idx - 1
        place_value = digit * (10 ** place_power)

        question = f"In the number { _format_with_spaces(number) }, what is the value of the digit {digit}?"
        explanation = f"The digit {digit} is in the 10^{place_power} place, so its value is { _format_with_spaces(place_value) }."

        if normalized_qtype == 'scaffold':
            place_names = {
                0: 'units',
                1: 'tens',
                2: 'hundreds',
                3: 'thousands',
                4: 'ten-thousands',
                5: 'hundred-thousands',
                6: 'millions',
                7: 'ten-millions',
                8: 'hundred-millions',
            }
            place_name = place_names.get(place_power, f"10^{place_power} place")
            checkpoints = [
                {
                    'id': 'c1_place_name',
                    'kind': 'mcq',
                    'prompt': f"The digit {digit} is in which place?",
                    'options': [
                        place_names.get(max(0, place_power - 1), 'tens'),
                        place_name,
                        place_names.get(place_power + 1, 'hundreds'),
                    ],
                    'correct_answer': place_name,
                    'explanation': f"It is in the {place_name} place.",
                },
                {
                    'id': 'c2_power_of_ten',
                    'kind': 'typed',
                    'prompt': 'Write the value of that place as a power of 10 (e.g. 1, 10, 100, 1000).',
                    'correct_answer': str(10 ** place_power),
                    'explanation': f"That place is {10 ** place_power}.",
                },
                {
                    'id': 'c3_final',
                    'kind': 'typed',
                    'prompt': 'Final answer: write the value of the digit.',
                    'correct_answer': _format_with_spaces(place_value),
                    'explanation': explanation,
                },
            ]

            steps = [
                'Find where the digit sits in the number (its place).',
                'Convert the place into a power of 10.',
                'Multiply the digit by the place value.',
            ]

            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'scaffold',
                'question': question,
                'correct_answer': _format_with_spaces(place_value),
                'explanation': explanation,
                'steps': steps,
                'checkpoints': checkpoints,
                'parameters': {'number': number, 'digit_index': idx, 'digit': digit, 'place_power': place_power},
            }

        if normalized_qtype == 'mcq':
            distractors = set()
            while len(distractors) < 3:
                wrong_power = rng.choice([p for p in range(0, len(str_num)) if p != place_power])
                distractors.add(_format_with_spaces(digit * (10 ** wrong_power)))
            options = [_format_with_spaces(place_value), *sorted(distractors)]
            rng.shuffle(options)
            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'mcq',
                'question': question,
                'options': options,
                'correct_answer': _format_with_spaces(place_value),
                'explanation': explanation,
                'parameters': {'number': number, 'digit_index': idx, 'digit': digit, 'place_power': place_power},
            }

        return {
            'id': _make_id('g7_whole'),
            'topic': 'Whole Numbers',
            'subskill': normalized_subskill,
            'difficulty': normalized_difficulty,
            'question_type': 'typed',
            'question': question,
            'correct_answer': _format_with_spaces(place_value),
            'explanation': explanation,
            'parameters': {'number': number, 'digit_index': idx, 'digit': digit, 'place_power': place_power},
        }

    if normalized_subskill == 'compare':
        digits = {'easy': 4, 'medium': 6, 'hard': 8}[normalized_difficulty]
        a = _generate_place_value_number(rng, digits)
        b = _generate_place_value_number(rng, digits)
        while b == a:
            b = _generate_place_value_number(rng, digits)

        correct = '<' if a < b else '>'
        question = f"Fill in the correct symbol (< or >): { _format_with_spaces(a) } ? { _format_with_spaces(b) }"
        explanation = f"Compare from the leftmost digit. { _format_with_spaces(a) } {correct} { _format_with_spaces(b) }."

        if normalized_qtype == 'scaffold':
            checkpoints = [
                {
                    'id': 'c1_rule',
                    'kind': 'mcq',
                    'prompt': 'When comparing two whole numbers, where should you start comparing?'
                    ,
                    'options': ['Leftmost digit', 'Rightmost digit', 'Any digit'],
                    'correct_answer': 'Leftmost digit',
                    'explanation': 'Start at the leftmost digit (highest place value) and move right only if they are equal.',
                },
                {
                    'id': 'c2_symbol',
                    'kind': 'mcq',
                    'prompt': f"Which symbol makes this true? { _format_with_spaces(a) } ? { _format_with_spaces(b) }",
                    'options': ['<', '>'],
                    'correct_answer': correct,
                    'explanation': explanation,
                },
                {
                    'id': 'c3_final',
                    'kind': 'typed',
                    'prompt': 'Final answer: type just the correct symbol (< or >).',
                    'correct_answer': correct,
                    'explanation': explanation,
                },
            ]

            steps = [
                'Compare the leftmost digits (highest place value).',
                'If they are the same, move one place to the right and compare again.',
                'Decide whether the first number is smaller (<) or bigger (>).',
            ]

            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'scaffold',
                'question': question,
                'correct_answer': correct,
                'explanation': explanation,
                'steps': steps,
                'checkpoints': checkpoints,
                'parameters': {'a': a, 'b': b},
            }

        if normalized_qtype == 'mcq':
            options = ['<', '>']
            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'mcq',
                'question': question,
                'options': options,
                'correct_answer': correct,
                'explanation': explanation,
                'parameters': {'a': a, 'b': b},
            }

        return {
            'id': _make_id('g7_whole'),
            'topic': 'Whole Numbers',
            'subskill': normalized_subskill,
            'difficulty': normalized_difficulty,
            'question_type': 'typed',
            'question': question,
            'correct_answer': correct,
            'explanation': explanation,
            'parameters': {'a': a, 'b': b},
        }

    if normalized_subskill == 'rounding':
        bases_by_diff = {
            'easy': [10, 100],
            'medium': [5, 10, 100, 1000],
            'hard': [5, 10, 100, 1000, 10000],
        }

        # Scaffold v2 for rounding: keep the bases clean (avoid base=5 here for clearer step-checkpoints).
        if normalized_qtype == 'scaffold':
            bases_by_diff = {
                'easy': [10, 100],
                'medium': [10, 100, 1000],
                'hard': [10, 100, 1000, 10000],
            }

        base = rng.choice(bases_by_diff[normalized_difficulty])
        digits = 4 if base <= 100 else 6
        n = _generate_place_value_number(rng, digits)

        rounded = _round_to_base(n, base)
        question = f"Round { _format_with_spaces(n) } to the nearest { _format_with_spaces(base) }."

        lower = (n // base) * base
        upper = lower + base
        midpoint = lower + (base / 2)
        direction = 'down' if n < midpoint else 'up'

        explanation = f"Find the nearest multiple of {base}. The rounded value is { _format_with_spaces(rounded) }."

        if normalized_qtype == 'scaffold':
            place_names = {
                1: 'units digit',
                10: 'tens digit',
                100: 'hundreds digit',
                1000: 'thousands digit',
                10000: 'ten-thousands digit',
            }
            deciding_place = max(1, base // 10)
            deciding_digit_name = place_names.get(deciding_place, f"{_format_with_spaces(deciding_place)}s digit")

            checkpoints = [
                {
                    'id': 'c1_deciding_digit',
                    'kind': 'mcq',
                    'prompt': f"When rounding to the nearest { _format_with_spaces(base) }, which digit decides whether you round up or down?",
                    'options': [
                        'units digit',
                        'tens digit',
                        'hundreds digit',
                        'thousands digit',
                        'ten-thousands digit',
                    ],
                    'correct_answer': deciding_digit_name,
                    'explanation': f"To round to the nearest { _format_with_spaces(base) }, look at the digit in the {deciding_digit_name}.",
                },
                {
                    'id': 'c2_lower_multiple',
                    'kind': 'typed',
                    'prompt': f"What is the multiple of { _format_with_spaces(base) } just below { _format_with_spaces(n) }?",
                    'correct_answer': _format_with_spaces(lower),
                    'explanation': f"The lower multiple is { _format_with_spaces(lower) }.",
                },
                {
                    'id': 'c3_round_direction',
                    'kind': 'mcq',
                    'prompt': f"Is { _format_with_spaces(n) } closer to { _format_with_spaces(lower) } or { _format_with_spaces(upper) }?",
                    'options': [
                        _format_with_spaces(lower),
                        _format_with_spaces(upper),
                    ],
                    'correct_answer': _format_with_spaces(lower if direction == 'down' else upper),
                    'explanation': f"The midpoint is { _format_with_spaces(int(midpoint)) }. Since the number is {direction}, you round {direction}.",
                },
                {
                    'id': 'c4_final',
                    'kind': 'typed',
                    'prompt': 'Final answer: write the rounded value.',
                    'correct_answer': _format_with_spaces(rounded),
                    'explanation': explanation,
                },
            ]

            steps = [
                'Identify the rounding base (what you are rounding to).',
                'Find the two nearest multiples (one below and one above).',
                'Find the midpoint between those two multiples.',
                'Decide whether the number is closer to the lower or upper multiple.',
                'Write the rounded value.',
            ]

            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'scaffold',
                'question': question,
                'correct_answer': _format_with_spaces(rounded),
                'explanation': explanation,
                'steps': steps,
                'checkpoints': checkpoints,
                'parameters': {'number': n, 'base': base, 'lower': lower, 'upper': upper, 'midpoint': midpoint},
            }

        return {
            'id': _make_id('g7_whole'),
            'topic': 'Whole Numbers',
            'subskill': normalized_subskill,
            'difficulty': normalized_difficulty,
            'question_type': 'typed',
            'question': question,
            'correct_answer': _format_with_spaces(rounded),
            'explanation': explanation,
            'parameters': {'number': n, 'base': base},
        }

    if normalized_subskill == 'multiples':
        base = rng.choice([3, 4, 5, 6, 7, 8, 9])
        limit = {'easy': 60, 'medium': 120, 'hard': 200}[normalized_difficulty]
        target = base * rng.randint(2, limit // base)

        if normalized_qtype == 'scaffold':
            non_multiple = target + rng.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
            if non_multiple % base == 0:
                non_multiple += 1

            checkpoints = [
                {
                    'id': 'c1_is_multiple',
                    'kind': 'mcq',
                    'prompt': f"Is { _format_with_spaces(target) } a multiple of {base}?",
                    'options': ['Yes', 'No'],
                    'correct_answer': 'Yes',
                    'explanation': f"Yes. { _format_with_spaces(target) } = {base} × {target // base}.",
                },
                {
                    'id': 'c2_not_multiple',
                    'kind': 'mcq',
                    'prompt': f"Which number is NOT a multiple of {base}?",
                    'options': [_format_with_spaces(target), _format_with_spaces(non_multiple)],
                    'correct_answer': _format_with_spaces(non_multiple),
                    'explanation': f"{ _format_with_spaces(non_multiple) } is not divisible by {base}.",
                },
                {
                    'id': 'c3_final',
                    'kind': 'typed',
                    'prompt': f"Final answer: write the next multiple of {base} after { _format_with_spaces(target) }.",
                    'correct_answer': _format_with_spaces(target + base),
                    'explanation': f"Add {base} to get the next multiple.",
                },
            ]

            steps = [
                'Multiples are numbers you get when you multiply by a whole number.',
                f"A number is a multiple of {base} if it is divisible by {base}.",
                f"To get the next multiple, add {base}.",
            ]

            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'scaffold',
                'question': f"Work with multiples of {base}.",
                'correct_answer': _format_with_spaces(target + base),
                'explanation': f"The next multiple after { _format_with_spaces(target) } is { _format_with_spaces(target + base) }.",
                'steps': steps,
                'checkpoints': checkpoints,
                'parameters': {'base': base, 'target': target, 'non_multiple': non_multiple, 'limit': limit},
            }

        if normalized_qtype == 'mcq':
            options = [_format_with_spaces(target)]
            while len(options) < 4:
                candidate = rng.randint(10, limit)
                formatted = _format_with_spaces(candidate)
                if formatted not in options:
                    options.append(formatted)
            rng.shuffle(options)
            question = f"Which of these is a multiple of {base}?"
            explanation = f"A multiple of {base} is {base} × whole number. {target} = {base} × {target // base}."
            return {
                'id': _make_id('g7_whole'),
                'topic': 'Whole Numbers',
                'subskill': normalized_subskill,
                'difficulty': normalized_difficulty,
                'question_type': 'mcq',
                'question': question,
                'options': options,
                'correct_answer': _format_with_spaces(target),
                'explanation': explanation,
                'parameters': {'base': base, 'limit': limit, 'target': target},
            }

        question = f"Write the first 6 multiples of {base}."
        multiples = [base * i for i in range(1, 7)]
        correct_answer = ', '.join(_format_with_spaces(m) for m in multiples)
        explanation = f"Multiply {base} by 1, 2, 3, 4, 5, 6."
        return {
            'id': _make_id('g7_whole'),
            'topic': 'Whole Numbers',
            'subskill': normalized_subskill,
            'difficulty': normalized_difficulty,
            'question_type': 'typed',
            'question': question,
            'correct_answer': correct_answer,
            'explanation': explanation,
            'parameters': {'base': base, 'limit': limit},
        }

    raise ValueError(f"Unsupported subskill: {subskill}")
