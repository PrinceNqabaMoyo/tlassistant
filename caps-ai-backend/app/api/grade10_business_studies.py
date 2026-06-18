from flask import Blueprint, request, jsonify
import json
import os
import re
from langchain_google_genai import ChatGoogleGenerativeAI
from app.utils.grade10_business_studies.term_1 import micro_environment_generator
from app.utils.grade10_business_studies.term_1 import business_functions_generator
from app.utils.grade10_business_studies.term_1 import market_environment_generator
from app.utils.grade10_business_studies.term_1 import macro_environment_generator
from app.utils.grade10_business_studies.term_1 import interrelationship_generator
from app.utils.grade10_business_studies.term_1 import business_sectors_generator
from app.utils.grade10_business_studies.term_2 import socio_economic_issues_generator
from app.utils.grade10_business_studies.term_2 import social_responsibility_generator
from app.utils.grade10_business_studies.term_2 import entrepreneurial_qualities_generator
from app.utils.grade10_business_studies.term_2 import forms_of_ownership_generator
from app.utils.grade10_business_studies.term_2 import concept_of_quality_generator
from app.utils.grade10_business_studies.term_3 import creative_thinking_generator
from app.utils.grade10_business_studies.term_3 import business_opportunities_generator
from app.utils.grade10_business_studies.term_3 import business_location_generator
from app.utils.grade10_business_studies.term_3 import contracts_generator
from app.utils.grade10_business_studies.term_3 import presentation_generator
from app.utils.grade10_business_studies.term_3 import business_plans_generator

grade10_business_studies_bp = Blueprint('grade10_business_studies', __name__)

# Fallback basic generators mapping
GENERATORS = {
    # Term 1
    'grade10_bs_micro_environment': micro_environment_generator.generate,
    'grade10_bs_business_functions': business_functions_generator.generate_business_functions,
    'grade10_bs_market_environment': market_environment_generator.generate_market_environment,
    'grade10_bs_macro_environment': macro_environment_generator.generate_macro_environment,
    'grade10_bs_interrelationship': interrelationship_generator.generate_interrelationship,
    'grade10_bs_business_sectors': business_sectors_generator.generate_business_sectors,
    # Term 2
    'grade10_bs_socio_economic_issues': socio_economic_issues_generator.generate_socio_economic_issues,
    'grade10_bs_social_responsibility': social_responsibility_generator.generate_social_responsibility,
    'grade10_bs_entrepreneurial_qualities': entrepreneurial_qualities_generator.generate_entrepreneurial_qualities,
    'grade10_bs_forms_of_ownership': forms_of_ownership_generator.generate_forms_of_ownership,
    'grade10_bs_concept_of_quality': concept_of_quality_generator.generate_concept_of_quality,
    # Term 3
    'grade10_bs_creative_thinking': creative_thinking_generator.generate_creative_thinking,
    'grade10_bs_business_opportunities': business_opportunities_generator.generate_business_opportunities,
    'grade10_bs_business_location': business_location_generator.generate_business_location,
    'grade10_bs_contracts': contracts_generator.generate_contracts,
    'grade10_bs_presentation': presentation_generator.generate_presentation,
    'grade10_bs_business_plans': business_plans_generator.generate_business_plans,
}

_LLM_GENERATOR_MODULES = (
    business_functions_generator,
    market_environment_generator,
    macro_environment_generator,
    interrelationship_generator,
    business_sectors_generator,
    socio_economic_issues_generator,
    social_responsibility_generator,
    entrepreneurial_qualities_generator,
    forms_of_ownership_generator,
    concept_of_quality_generator,
    creative_thinking_generator,
    business_opportunities_generator,
    business_location_generator,
    contracts_generator,
    presentation_generator,
    business_plans_generator,
)


def _extract_json_payload(raw_text):
    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        list_match = re.search(r'\[.*\]', raw_text, re.DOTALL)
        if list_match:
            return json.loads(list_match.group(0))

        object_match = re.search(r'\{.*\}', raw_text, re.DOTALL)
        if object_match:
            return json.loads(object_match.group(0))

        raise


def _normalize_generated_question(question, index):
    question_type = question.get('question_type') or ('mcq' if question.get('options') else 'typed')

    if question_type == 'mcq':
        return {
            'id': str(question.get('id') or f'g10_bs_mcq_{index}'),
            'question_type': 'mcq',
            'prompt': question.get('prompt', ''),
            'options': question.get('options', []),
            'correct_index': str(question.get('correct_index', question.get('correct_option_index', 0))),
            'explanation': question.get('explanation', ''),
            'marks': question.get('marks', 1),
        }

    marking_points = question.get('marking_points') or question.get('required_points') or []
    if not isinstance(marking_points, list):
        marking_points = []

    sample_answer = question.get('sample_answer') or question.get('explanation') or ''
    marks = question.get('marks', len(marking_points) or 1)

    return {
        'id': str(question.get('id') or f'g10_bs_typed_{index}'),
        'question_type': 'typed',
        'prompt': question.get('prompt', ''),
        'marking_points': marking_points,
        'sample_answer': sample_answer,
        'explanation': question.get('explanation', sample_answer),
        'marks': marks,
    }


def generate_questions_with_llm(system_prompt, prompt, count):
    google_api_key = os.getenv('GOOGLE_API_KEY')
    if not google_api_key:
        raise ValueError('AI service not configured')

    llm = ChatGoogleGenerativeAI(
        model='models/gemini-1.5-flash',
        temperature=0.3,
        convert_system_message_to_human=True,
        google_api_key=google_api_key,
    )

    response = llm.invoke(f"{system_prompt}\n\n{prompt}")
    raw_content = response.content if isinstance(response.content, str) else str(response.content)
    payload = _extract_json_payload(raw_content)

    if isinstance(payload, dict):
        payload = payload.get('questions') or payload.get('assessment') or []

    if not isinstance(payload, list):
        raise ValueError('LLM question generator returned an unsupported response format')

    normalized_questions = [_normalize_generated_question(question, index) for index, question in enumerate(payload[:count], start=1)]
    return normalized_questions


def _ensure_llm_helpers_registered():
    for module in _LLM_GENERATOR_MODULES:
        if not hasattr(module, 'generate_questions_with_llm'):
            module.generate_questions_with_llm = generate_questions_with_llm


def _normalize_generator_result(result):
    if isinstance(result, list):
        return result

    if isinstance(result, dict):
        if result.get('success') is False:
            raise ValueError(result.get('error') or 'Generation failed')

        questions = result.get('questions')
        if isinstance(questions, list):
            return questions

    raise ValueError('Generator returned an unsupported response shape')


def generate_questions(topic, subskill, difficulty, count=1, config=None):
    """
    Unified function for generating Grade 10 Business Studies questions.
    """
    if config is None:
        config = {}

    _ensure_llm_helpers_registered()

    # Try the specific topic generator if it exists
    if topic in GENERATORS:
        generator = GENERATORS[topic]
        result = generator(subskill=subskill, difficulty=difficulty, count=count, **config)
        return _normalize_generator_result(result)

    # Fallback to LLM if no static generator is found (or simply raise an error during static generation)
    raise ValueError(f"No generator found for topic: {topic}")


@grade10_business_studies_bp.route('/generate', methods=['POST'])
def generate_business_studies_endpoint():
    data = request.json
    topic = data.get('topic')
    subskill = data.get('subskill', 'concepts')
    difficulty = data.get('difficulty', 'medium')
    count = data.get('count', 1)

    try:
        if topic == 'practice':
            # Handle mixed practice mode: e.g. 8 structured questions
            return jsonify({'error': 'Practice mode not yet implemented'}), 501

        questions = generate_questions(topic, subskill, difficulty, count=count)
        return jsonify({'questions': questions})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@grade10_business_studies_bp.route('/mark', methods=['POST'])
def mark_business_studies_endpoint():
    """
    Unified endpoint for marking Business Studies questions.
    """
    data = request.json
    questions = data.get('questions', [])
    answers = data.get('answers', {})

    results = {}
    total_score = 0
    max_score = 0

    for q in questions:
        q_id = str(q.get('id', ''))
        q_type = q.get('question_type')
        user_ans = answers.get(q_id)

        # Grading logic mirror of the frontend check
        if q_type == 'mcq':
            correct_idx = str(q.get('correct_index', ''))
            is_correct = str(user_ans) == correct_idx
            score = 1 if is_correct else 0
            results[q_id] = {
                'is_correct': is_correct,
                'score': score,
                'max_score': 1,
                'feedback': 'Correct.' if is_correct else f"Incorrect. The correct answer was: {q.get('options', [])[int(correct_idx)] if correct_idx.isdigit() else ''}"
            }
            total_score += score
            max_score += 1

        elif q_type == 'typed':
            # For typed semantic questions, exact match is rare.
            # In a real system, we'd use LLM grading here.
            # For now, we will mark it as "needs review" or assign partial/full credit if length is sufficient.
            # Let's just assign full marks for providing a substantial answer to simulate completion.
            is_valid = bool(user_ans and len(str(user_ans).strip()) > 5)
            # The actual max score should be derived from the number of expected marking points
            expected_points = len(q.get('marking_points', [])) if 'marking_points' in q else 1
            expected_points = max(1, expected_points)

            score = expected_points if is_valid else 0
            results[q_id] = {
                'is_correct': is_valid,
                'score': score,
                'max_score': expected_points,
                'feedback': 'Answer submitted for review. Check against memo.' if is_valid else 'Please provide a valid answer.'
            }
            total_score += score
            max_score += expected_points
            
        elif q_type == 'table_wordbank':
            correct_map = q.get('correct_map', {})
            selections = user_ans.get('selections', {}) if user_ans and isinstance(user_ans, dict) else {}
            hit = 0
            total = 0
            for row_key, expected_obj in correct_map.items():
                expected = str(expected_obj.get('2'))
                if expected != 'None':
                    total += 1
                    got = str(selections.get(row_key, {}).get('2'))
                    if got == expected:
                        hit += 1
            
            is_correct = (total > 0 and hit == total)
            results[q_id] = {
                'is_correct': is_correct,
                'score': hit,
                'max_score': total,
                'feedback': 'Perfect match.' if is_correct else f"You got {hit}/{total} correct."
            }
            total_score += hit
            max_score += total
            
        else:
            # Fallback
            results[q_id] = {
                'is_correct': False,
                'score': 0,
                'max_score': 1,
                'feedback': f'Unknown question type: {q_type}'
            }
            max_score += 1
            
    return jsonify({
        'results': results,
        'total_score': total_score,
        'max_score': max_score
    })
