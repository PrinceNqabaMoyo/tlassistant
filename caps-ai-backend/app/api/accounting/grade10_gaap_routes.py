from flask import jsonify, request

from . import accounting_bp
from ...utils.grade10_accounting.gaap_generator import generate_grade10_gaap_questions


@accounting_bp.route('/grade10/gaap/generate', methods=['POST'])
def generate_grade10_gaap():
    try:
        data = request.get_json() or {}

        subskill = data.get('subskill')
        difficulty = data.get('difficulty', 'easy')
        question_type = data.get('question_type')
        count = data.get('count', 1)
        seed = data.get('seed')

        result = generate_grade10_gaap_questions(
            seed=seed,
            subskill=subskill,
            difficulty=difficulty,
            question_type=question_type,
            count=count,
        )

        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
        }), 500
