from flask import Blueprint, request, jsonify
import json
import re
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
from app.services.adaptive_progression import (
    evaluate_standard_progression,
    evaluate_pro_progression,
    get_progression_recommendation,
)
from app.services.agent_service import get_student_model
from app.utils.grade10_business_studies._bs_curriculum import (
    get_topic_sections,
    get_section_for_topic,
)

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

def _normalize_generated_question(question, topic, index):
    question_type = question.get('question_type') or ('mcq' if question.get('options') else 'typed')

    base_meta = {
        'topic': topic,
        'subject': 'business-studies',
        'grade': 'grade-10',
        'subskill': question.get('subskill', 'concepts'),
        'learning_objective_id': question.get('learning_objective_id') or f"bs10_{topic}",
        'misconception_tags': question.get('misconception_tags', []),
        'diagnostic_tags': question.get('diagnostic_tags', []),
        'minimum_mastery_score': question.get('minimum_mastery_score', 0.6),
        'keywords': question.get('keywords', []),
        'hint_trigger': question.get('hint_trigger', ''),
        'guidelines': question.get('guidelines', []),
        'visual_aid_key': question.get('visual_aid_key', ''),
    }

    if question_type == 'mcq':
        return {
            'id': str(question.get('id') or f'g10_bs_mcq_{index}'),
            'question_type': 'mcq',
            'prompt': question.get('prompt', ''),
            'options': question.get('options', []),
            'correct_index': str(question.get('correct_index', question.get('correct_option_index', 0))),
            'explanation': question.get('explanation', ''),
            'marks': question.get('marks', 1),
            **base_meta,
        }

    if question_type == 'word_bank':
        return {
            'id': str(question.get('id') or f'g10_bs_wb_{index}'),
            'question_type': 'word_bank',
            'prompt': question.get('prompt', ''),
            'word_bank': question.get('word_bank', []),
            'blanks': question.get('blanks', []),
            'correct_map': question.get('correct_map', {}),
            'explanation': question.get('explanation', ''),
            'marks': question.get('marks', 1),
            **base_meta,
        }

    if question_type == 'matching_columns':
        return {
            'id': str(question.get('id') or f'g10_bs_match_{index}'),
            'question_type': 'matching_columns',
            'prompt': question.get('prompt', ''),
            'column_a': question.get('column_a', []),
            'column_b': question.get('column_b', []),
            'correct_pairs': question.get('correct_pairs', {}),
            'explanation': question.get('explanation', ''),
            'marks': question.get('marks', 1),
            **base_meta,
        }

    if question_type == 'crossword':
        return {
            'id': str(question.get('id') or f'g10_bs_cross_{index}'),
            'question_type': 'crossword',
            'prompt': question.get('prompt', ''),
            'words': question.get('words', []),
            'clues': question.get('clues', {}),
            'grid_size': question.get('grid_size', 10),
            'explanation': question.get('explanation', ''),
            'marks': question.get('marks', 1),
            **base_meta,
        }

    if question_type == 'essay':
        return {
            'id': str(question.get('id') or f'g10_bs_essay_{index}'),
            'question_type': 'essay',
            'prompt': question.get('prompt', ''),
            'rubric': question.get('rubric', []),
            'sample_answer': question.get('sample_answer', ''),
            'explanation': question.get('explanation', question.get('sample_answer', '')),
            'marks': question.get('marks', 20),
            'min_words': question.get('min_words', 150),
            'max_words': question.get('max_words', 400),
            **base_meta,
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
        **base_meta,
    }


def _normalize_generator_result(result, topic):
    if isinstance(result, list):
        return [_normalize_generated_question(q, topic, i) for i, q in enumerate(result, start=1)]

    if isinstance(result, dict):
        if result.get('success') is False:
            raise ValueError(result.get('error') or 'Generation failed')

        questions = result.get('questions')
        if isinstance(questions, list):
            return [_normalize_generated_question(q, topic, i) for i, q in enumerate(questions, start=1)]

    raise ValueError('Generator returned an unsupported response shape')


def generate_questions(topic, subskill, difficulty, count=1, config=None):
    """
    Unified function for generating Grade 10 Business Studies questions.

    Supports section-based progression: if `subskill` matches a section key
    from the curriculum `.md` file, the function picks a recommended
    format pool for that section.
    """
    if config is None:
        config = {}

    # Check if subskill is a section key from curriculum .md
    section = get_section_for_topic(topic, subskill)
    if section:
        import random
        # Pick a random format from the section's recommended formats
        pool_key = random.choice(section['formats'])
        subskill = pool_key

    # Try the specific topic generator if it exists
    if topic in GENERATORS:
        generator = GENERATORS[topic]
        result = generator(subskill=subskill, difficulty=difficulty, count=count, **config)
        return _normalize_generator_result(result, topic)

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


@grade10_business_studies_bp.route('/sections', methods=['GET'])
def get_business_studies_sections():
    """
    Return scaffold sections for a given topic, derived from the
    curriculum `.md` file.

    Query params:
        topic  – topic key, e.g. grade10_bs_business_functions
    """
    topic = request.args.get('topic')
    if not topic:
        return jsonify({'error': 'Missing topic query param'}), 400

    try:
        sections = get_topic_sections(topic)
        # Return only the fields the frontend needs for scaffold steps
        steps = [
            {
                'key': sec['key'],
                'title': sec['title'],
                'formats': sec['formats'],
            }
            for sec in sections
        ]
        return jsonify({'topic': topic, 'steps': steps})
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
            student_text = str(user_ans or '').strip().lower()
            marking_points = q.get('marking_points', [])
            expected_points = max(1, len(marking_points)) if marking_points else 1

            if marking_points:
                # Deterministic keyword matching: count how many marking points
                # have at least one keyword present in the student's answer.
                def _has_keyword(point_text: str, answer: str) -> bool:
                    # Extract simple keywords (words > 3 chars) from the point
                    keywords = [w for w in re.findall(r"[a-z]{4,}", point_text.lower())]
                    # Also include any capitalised proper nouns
                    keywords += [w for w in re.findall(r"[A-Z][a-z]{2,}", point_text)]
                    # Deduplicate while preserving order
                    seen = set()
                    unique = []
                    for k in keywords:
                        if k not in seen:
                            seen.add(k)
                            unique.append(k)
                    keywords = unique
                    # A point is considered matched if at least one keyword is present
                    return any(k in answer for k in keywords)

                matched = sum(1 for p in marking_points if _has_keyword(p, student_text))
                score = matched
                feedback = f"You covered {matched}/{expected_points} marking points."
            else:
                # No marking points available: fall back to presence check
                score = expected_points if len(student_text) > 10 else 0
                feedback = 'Answer submitted for review.' if score else 'Please provide a valid answer.'

            results[q_id] = {
                'is_correct': score == expected_points,
                'score': score,
                'max_score': expected_points,
                'feedback': feedback,
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
            
        elif q_type == 'word_bank':
            correct_map = q.get('correct_map', {})
            user_map = user_ans if isinstance(user_ans, dict) else {}
            hit = 0
            total = len(correct_map)
            for blank_id, expected in correct_map.items():
                got = str(user_map.get(blank_id, '')).strip()
                if got.lower() == str(expected).strip().lower():
                    hit += 1
            is_correct = total > 0 and hit == total
            results[q_id] = {
                'is_correct': is_correct,
                'score': hit,
                'max_score': total,
                'feedback': 'Perfect match.' if is_correct else f"You got {hit}/{total} correct.",
            }
            total_score += hit
            max_score += total

        elif q_type == 'matching_columns':
            correct_pairs = q.get('correct_pairs', {})
            user_pairs = user_ans if isinstance(user_ans, dict) else {}
            hit = 0
            total = len(correct_pairs)
            for a_key, expected_b in correct_pairs.items():
                got = str(user_pairs.get(a_key, '')).strip()
                if got.lower() == str(expected_b).strip().lower():
                    hit += 1
            is_correct = total > 0 and hit == total
            results[q_id] = {
                'is_correct': is_correct,
                'score': hit,
                'max_score': total,
                'feedback': 'Perfect match.' if is_correct else f"You got {hit}/{total} correct.",
            }
            total_score += hit
            max_score += total

        elif q_type == 'crossword':
            correct_words = q.get('words', [])
            correct_clues = q.get('clues', {})
            user_words = user_ans if isinstance(user_ans, dict) else {}
            hit = 0
            total = len(correct_words)
            for word in correct_words:
                expected = word.upper().strip()
                got = str(user_words.get(word, '')).upper().strip()
                if got == expected:
                    hit += 1
            is_correct = total > 0 and hit == total
            results[q_id] = {
                'is_correct': is_correct,
                'score': hit,
                'max_score': total,
                'feedback': 'Perfect match.' if is_correct else f"You got {hit}/{total} words correct.",
            }
            total_score += hit
            max_score += total

        elif q_type == 'essay':
            student_text = str(user_ans or '').strip()
            rubric = q.get('rubric', [])
            min_words = q.get('min_words', 150)
            max_words = q.get('max_words', 400)
            word_count = len(student_text.split())

            matched_criteria = 0
            total_criteria = max(1, len(rubric)) if rubric else 1
            rubric_feedback = []

            if rubric:
                for criterion in rubric:
                    desc = str(criterion.get('description', '')).strip().lower()
                    criterion_marks = criterion.get('marks', 1)
                    keywords = [w for w in re.findall(r"[a-z]{4,}", desc)]
                    # Proper nouns too
                    keywords += [w for w in re.findall(r"[A-Z][a-z]{2,}", str(criterion.get('description', '')))]
                    seen = set()
                    unique = []
                    for k in keywords:
                        if k not in seen:
                            seen.add(k)
                            unique.append(k)
                    keywords = unique
                    matched = any(k in student_text.lower() for k in keywords)
                    if matched:
                        matched_criteria += 1
                        rubric_feedback.append(f"✓ {criterion.get('criterion', 'Criterion')}")
                    else:
                        rubric_feedback.append(f"✗ {criterion.get('criterion', 'Criterion')}")

            score = matched_criteria
            max_score_q = total_criteria

            length_note = ""
            if word_count < min_words:
                length_note = f" Your essay is only {word_count} words (min {min_words})."
            elif word_count > max_words:
                length_note = f" Your essay is {word_count} words (max {max_words})."
            else:
                length_note = f" Word count: {word_count} (within range)."

            feedback = (
                f"Rubric: {matched_criteria}/{total_criteria} criteria matched.{length_note}"
                + ("\n" + "\n".join(rubric_feedback) if rubric_feedback else "")
            )

            results[q_id] = {
                'is_correct': score == max_score_q and min_words <= word_count <= max_words,
                'score': score,
                'max_score': max_score_q,
                'feedback': feedback,
                'word_count': word_count,
            }
            total_score += score
            max_score += max_score_q

        else:
            # Fallback
            results[q_id] = {
                'is_correct': False,
                'score': 0,
                'max_score': 1,
                'feedback': f'Unknown question type: {q_type}'
            }
            max_score += 1
            
    # Adaptive progression: record mastery and decide next step
    mode = data.get('mode', 'practice')
    user_id = data.get('user_id')
    tier = data.get('subscription', 'standard')
    topic = data.get('topic', 'unknown')
    subskill = data.get('subskill', 'concepts')

    student_model = get_student_model()
    if tier == 'pro':
        progression = evaluate_pro_progression(
            student_model=student_model,
            user_id=user_id,
            subject='business-studies',
            grade='grade-10',
            topic=topic,
            subskill=subskill,
            score=total_score,
            max_score=max_score,
            mode=mode,
        )
    else:
        progression = evaluate_standard_progression(
            mode=mode,
            score=total_score,
            max_score=max_score,
        )

    recommendations = []
    if student_model and user_id:
        recommendations = get_progression_recommendation(
            student_model=student_model,
            user_id=user_id,
            subject='business-studies',
            grade='grade-10',
            topic=topic,
        )

    return jsonify({
        'results': results,
        'total_score': total_score,
        'max_score': max_score,
        'progression': progression,
        'recommendations': recommendations,
    })
