import math
import re
from flask import Blueprint, request, jsonify
from app.utils.grade11_business_studies.term_1 import influences_on_business_environments_generator
from app.utils.grade11_business_studies.term_1 import the_challenges_of_the_business_environments_generator
from app.utils.grade11_business_studies.term_1 import adapting_to_challenges_generator
from app.utils.grade11_business_studies.term_1 import socio_economic_issues_generator
from app.utils.grade11_business_studies.term_1 import business_sectors_generator
from app.utils.grade11_business_studies.term_1 import benefits_of_a_company_generator
from app.utils.grade11_business_studies.term_1 import avenues_of_acquiring_businesses_generator
from app.utils.grade11_business_studies.term_2 import creative_thinking_generator
from app.utils.grade11_business_studies.term_2 import stress_crisis_change_generator
from app.utils.grade11_business_studies.term_2 import marketing_function_generator
from app.utils.grade11_business_studies.term_2 import production_function_generator
from app.utils.grade11_business_studies.term_2 import professionalism_and_ethics_generator
from app.utils.grade11_business_studies.term_3 import entrepreneurial_assessment_generator
from app.utils.grade11_business_studies.term_3 import citizenship_responsibilities_generator
from app.utils.grade11_business_studies.term_3 import business_plan_transformation_generator
from app.utils.grade11_business_studies.term_3 import start_business_venture_generator
from app.utils.grade11_business_studies.term_3 import presentation_of_information_generator


grade11_business_studies_bp = Blueprint('grade11_business_studies', __name__)


GENERATORS = {
    'grade11_bs_influences_on_business_environments': influences_on_business_environments_generator,
    'grade11_bs_challenges_of_the_business_environments': the_challenges_of_the_business_environments_generator,
    'grade11_bs_adapting_to_challenges': adapting_to_challenges_generator,
    'grade11_bs_socio_economic_issues': socio_economic_issues_generator,
    'grade11_bs_business_sectors': business_sectors_generator,
    'grade11_bs_benefits_of_a_company': benefits_of_a_company_generator,
    'grade11_bs_avenues_of_acquiring_businesses': avenues_of_acquiring_businesses_generator,
    'grade11_bs_creative_thinking': creative_thinking_generator,
    'grade11_bs_stress_crisis_change': stress_crisis_change_generator,
    'grade11_bs_marketing_function': marketing_function_generator,
    'grade11_bs_production_function': production_function_generator,
    'grade11_bs_professionalism_and_ethics': professionalism_and_ethics_generator,
    'grade11_bs_entrepreneurial_assessment': entrepreneurial_assessment_generator,
    'grade11_bs_citizenship_responsibilities': citizenship_responsibilities_generator,
    'grade11_bs_business_plan_transformation': business_plan_transformation_generator,
    'grade11_bs_start_business_venture': start_business_venture_generator,
    'grade11_bs_presentation_of_information': presentation_of_information_generator,
}


def generate_questions(topic, subskill, difficulty, count=1, config=None):
    config = config or {}
    if topic not in GENERATORS:
        raise ValueError(f'No generator found for topic: {topic}')
    generator = GENERATORS[topic]
    if hasattr(generator, 'generate'):
        return generator.generate(subskill=subskill, difficulty=difficulty, count=count, **config)
    return generator(subskill=subskill, difficulty=difficulty, count=count, **config)


def _normalize_text(value):
    return re.sub(r'\s+', ' ', str(value or '').lower()).strip()


def _resolve_mastery_threshold(question):
    default_threshold = 1.0 if question.get('question_type') == 'mcq' else 0.6
    raw_threshold = question.get('minimum_mastery_score', default_threshold)
    try:
        threshold = float(raw_threshold)
    except (TypeError, ValueError):
        threshold = default_threshold
    return max(0.0, min(1.0, threshold))


def _score_typed_answer(question, user_answer):
    normalized_answer = _normalize_text(user_answer)
    marking_points = question.get('marking_points', [])
    max_score = int(question.get('marks') or len(marking_points) or 1)
    keywords = question.get('keywords', [])
    mastery_threshold = _resolve_mastery_threshold(question)

    if not normalized_answer:
        return {
            'is_correct': False,
            'is_mastered': False,
            'score': 0,
            'max_score': max_score,
            'mastery_threshold': mastery_threshold,
            'mastery_ratio': 0,
            'keyword_coverage': 0,
            'feedback': 'Please provide a valid answer before marking.'
        }

    keyword_hits = 0
    for keyword in keywords:
        if _normalize_text(keyword) in normalized_answer:
            keyword_hits += 1

    if keywords:
        coverage = keyword_hits / max(1, len(keywords))
    else:
        coverage = 0

    if coverage >= 0.8:
        score = max_score
    elif coverage >= 0.5:
        score = max(1, math.ceil(max_score * 0.67))
    elif coverage > 0 or len(normalized_answer) >= 50:
        score = max(1, math.ceil(max_score * 0.34))
    else:
        score = 0

    mastery_ratio = score / max_score if max_score else 0
    is_mastered = mastery_ratio >= mastery_threshold

    if score == max_score:
        feedback = 'Strong answer. Your response covers most of the expected memo points.'
    elif is_mastered:
        feedback = 'Good answer. You reached the mastery threshold, though you can still strengthen some memo points.'
    elif score > 0:
        feedback = 'Partially correct. Compare your response to the memo to strengthen missing ideas and reach mastery.'
    else:
        feedback = 'Your response needs more of the key ideas from the memo.'

    return {
        'is_correct': is_mastered,
        'is_mastered': is_mastered,
        'score': score,
        'max_score': max_score,
        'mastery_threshold': mastery_threshold,
        'mastery_ratio': mastery_ratio,
        'keyword_coverage': coverage,
        'feedback': feedback
    }


@grade11_business_studies_bp.route('/generate', methods=['POST'])
def generate_business_studies_endpoint():
    data = request.json or {}
    topic = data.get('topic')
    subskill = data.get('subskill', 'concepts')
    difficulty = data.get('difficulty', 'medium')
    count = data.get('count', 1)
    config = data.get('config') or {}

    try:
        questions = generate_questions(topic, subskill, difficulty, count=count, config=config)
        return jsonify({'questions': questions})
    except Exception as exc:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(exc)}), 500


@grade11_business_studies_bp.route('/mark', methods=['POST'])
def mark_business_studies_endpoint():
    data = request.json or {}
    questions = data.get('questions', [])
    answers = data.get('answers', {})

    results = {}
    total_score = 0
    max_score = 0

    for question in questions:
        question_id = str(question.get('id', ''))
        question_type = question.get('question_type')
        user_answer = answers.get(question_id)
        mastery_threshold = _resolve_mastery_threshold(question)

        if question_type == 'mcq':
            correct_index = str(question.get('correct_index', ''))
            is_correct = str(user_answer) == correct_index
            score = 1 if is_correct else 0
            correct_option = ''
            if correct_index.isdigit():
                options = question.get('options', [])
                idx = int(correct_index)
                if 0 <= idx < len(options):
                    correct_option = options[idx]
            result = {
                'is_correct': is_correct,
                'is_mastered': is_correct,
                'score': score,
                'max_score': 1,
                'mastery_threshold': mastery_threshold,
                'mastery_ratio': score,
                'feedback': 'Correct.' if is_correct else f'Incorrect. The correct answer was: {correct_option}'
            }
        elif question_type == 'typed':
            result = _score_typed_answer(question, user_answer)
        else:
            result = {
                'is_correct': False,
                'is_mastered': False,
                'score': 0,
                'max_score': 1,
                'mastery_threshold': mastery_threshold,
                'mastery_ratio': 0,
                'feedback': f'Unknown question type: {question_type}'
            }

        results[question_id] = result
        total_score += result['score']
        max_score += result['max_score']

    return jsonify({
        'results': results,
        'total_score': total_score,
        'max_score': max_score
    })
