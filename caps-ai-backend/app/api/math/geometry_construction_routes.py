from flask import request, jsonify
from . import math_bp
from ...utils.geometry_construction_generator import generate_grade7_geometry_construction_question


@math_bp.route('/grade7/geometry-construction/generate', methods=['POST'])
def generate_grade7_geometry_construction():
    try:
        data = request.get_json() or {}

        subskill = data.get('subskill', 'degree_unit_familiar_angles_table')
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

            question = generate_grade7_geometry_construction_question(
                subskill=subskill,
                difficulty=difficulty,
                question_type=question_type,
                seed=q_seed,
            )
            questions.append(question)

        return jsonify({'success': True, 'questions': questions, 'count': len(questions)})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
