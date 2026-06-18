from flask import request, jsonify
from . import math_bp
from ...utils.grade11_equations_inequalities_generator import generate_grade11_equations_inequalities_question


@math_bp.route('/grade11/equations-inequalities/generate', methods=['POST'])
def generate_grade11_equations_inequalities():
    try:
        data = request.get_json() or {}

        subskill = data.get('subskill', 'equations_inequalities')
        difficulty = data.get('difficulty', 'easy')
        question_type = data.get('question_type', 'typed')
        count = data.get('count', 1)
        seed = data.get('seed')

        if not isinstance(count, int) or count < 1 or count > 20:
            return jsonify({'success': False, 'error': 'Count must be an integer between 1 and 20'}), 400

        questions = []
        for i in range(count):
            q_seed = None
            if seed is not None:
                try:
                    q_seed = int(seed) + i
                except Exception:
                    q_seed = None

            questions.append(
                generate_grade11_equations_inequalities_question(
                    subskill=subskill,
                    difficulty=difficulty,
                    question_type=question_type,
                    seed=q_seed,
                )
            )

        return jsonify({'success': True, 'questions': questions, 'count': len(questions)})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
