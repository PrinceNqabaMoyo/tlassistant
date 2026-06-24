import re
from flask import Blueprint, request, jsonify
from app.services.adaptive_progression import (
    evaluate_standard_progression,
    evaluate_pro_progression,
    get_progression_recommendation,
)
from app.services.agent_service import get_student_model
from app.utils.grade8_ems import (
    term1_gov_and_society,
    term1_accounting_basics,
    term1_source_documents,
    term2_markets_and_production,
    term2_crj,
    term2_accounting_cycle,
    term3_cpj_and_crj,
    term3_ownership,
)
from app.utils.grade8_ems._ems_curriculum import get_g8_topic_sections, get_g8_section_for_topic

grade8_ems_bp = Blueprint('grade8_ems', __name__)

GENERATORS = {
    # Term 1
    'grade8_ems_gov_and_society': term1_gov_and_society.generate,
    'grade8_ems_government': term1_gov_and_society.generate,
    'grade8_ems_national_budget': term1_gov_and_society.generate,
    'grade8_ems_standard_of_living': term1_gov_and_society.generate,
    'grade8_ems_accounting_basics': term1_accounting_basics.generate,
    'grade8_ems_source_documents': term1_source_documents.generate,
    # Term 2
    'grade8_ems_markets_and_production': term2_markets_and_production.generate,
    'grade8_ems_markets': term2_markets_and_production.generate,
    'grade8_ems_factors_of_production': term2_markets_and_production.generate,
    'grade8_ems_crj': term2_crj.generate,
    'grade8_ems_accounting_cycle': term2_accounting_cycle.generate,
    # Term 3
    'grade8_ems_cpj_and_crj': term3_cpj_and_crj.generate,
    'grade8_ems_ownership': term3_ownership.generate,
    'grade8_ems_forms_of_ownership': term3_ownership.generate,
}

def generate_questions(topic, subskill, difficulty, count=1, mode='scaffold', config=None):
    if config is None:
        config = {}

    # Section-based progression: if subskill matches a curriculum section key,
    # pick a recommended format pool for that section.
    section = get_g8_topic_sections(topic)
    if section:
        for sec in section:
            if sec['key'] == subskill and sec.get('formats'):
                import random
                pool_key = random.choice(sec['formats'])
                subskill = pool_key
                break

    # Map new format keys to legacy subskill pools generators understand.
    _FORMAT_TO_SUBSKILL = {
        'mcq': 'concepts',
        'word_bank': 'concepts',
        'matching_columns': 'concepts',
        'crossword': 'concepts',
        'typed': 'application',
        'essay': 'discussion',
    }
    subskill = _FORMAT_TO_SUBSKILL.get(subskill, subskill)
        
    generator_func = GENERATORS.get(topic)
    if not generator_func:
        raise ValueError(f"Unknown topic: {topic}")
        
    return generator_func(subskill=subskill, difficulty=difficulty, count=count, mode=mode, **config)

@grade8_ems_bp.route('/generate', methods=['POST'])
def generate_grade8_ems():
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No JSON payload provided'}), 400

        topic = data.get('topic')
        subskills = data.get('subskills', ['concepts'])
        difficulty = data.get('difficulty', 'medium')
        count = data.get('count', 1)
        mode = data.get('mode', 'scaffold')
        config = data.get('config', {})

        if not topic:
            return jsonify({'success': False, 'error': 'Missing required parameter: topic'}), 400

        all_questions = []
        # Support passing multiple subskills and distributing count among them
        for subskill in subskills:
            try:
                questions = generate_questions(topic, subskill, difficulty, count=count, mode=mode, config=config)
                all_questions.extend(questions)
            except Exception as e:
                # Log the error but continue if possible
                print(f"Error generating subskill {subskill}: {str(e)}")

        if not all_questions:
            return jsonify({'success': False, 'error': 'Failed to generate any questions'}), 500

        return jsonify({
            'success': True,
            'topic': topic,
            'questions': all_questions
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@grade8_ems_bp.route('/sections', methods=['GET'])
def get_grade8_ems_sections():
    """Return scaffold sections for a given topic, derived from the curriculum `.md` file."""
    topic = request.args.get('topic')
    if not topic:
        return jsonify({'error': 'Missing topic query param'}), 400

    try:
        sections = get_g8_topic_sections(topic)
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


@grade8_ems_bp.route('/mark', methods=['POST'])
def mark_grade8_ems():
    """Unified endpoint for marking Grade 8 EMS questions."""
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
                def _has_keyword(point_text: str, answer: str) -> bool:
                    keywords = [w for w in re.findall(r"[a-z]{4,}", point_text.lower())]
                    keywords += [w for w in re.findall(r"[A-Z][a-z]{2,}", point_text)]
                    seen = set()
                    unique = []
                    for k in keywords:
                        if k not in seen:
                            seen.add(k)
                            unique.append(k)
                    keywords = unique
                    return any(k in answer for k in keywords)

                matched = sum(1 for p in marking_points if _has_keyword(p, student_text))
                score = matched
                feedback = f"You covered {matched}/{expected_points} marking points."
            else:
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

        elif q_type == 'journal':
            correct_map = q.get('correct_map', {})
            user_map = user_ans if isinstance(user_ans, dict) else {}
            hit = 0
            total = 0
            for cell_key, expected in correct_map.items():
                total += 1
                got = str(user_map.get(cell_key, '')).strip()
                if got.lower() == str(expected).strip().lower():
                    hit += 1
            is_correct = total > 0 and hit == total
            results[q_id] = {
                'is_correct': is_correct,
                'score': hit,
                'max_score': total,
                'feedback': 'Perfect match.' if is_correct else f"You got {hit}/{total} cells correct.",
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
            min_words = q.get('min_words', 80)
            max_words = q.get('max_words', 250)
            word_count = len(student_text.split())

            matched_criteria = 0
            total_criteria = max(1, len(rubric)) if rubric else 1
            rubric_feedback = []

            if rubric:
                for criterion in rubric:
                    desc = str(criterion.get('description', '')).strip().lower()
                    keywords = [w for w in re.findall(r"[a-z]{4,}", desc)]
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
            results[q_id] = {
                'is_correct': False,
                'score': 0,
                'max_score': 1,
                'feedback': f'Unknown question type: {q_type}'
            }
            max_score += 1

    mode = data.get('mode', 'practice')
    user_id = data.get('user_id')
    tier = data.get('subscription', 'standard')
    topic = data.get('topic', 'unknown')
    subskill = data.get('subskill', 'concepts')

    student_model = get_student_model()
    metadata = {
        "question_results": {qid: res["is_correct"] for qid, res in results.items()},
        "total_score": total_score,
        "max_score": max_score,
    }
    if tier == 'pro':
        progression = evaluate_pro_progression(
            student_model=student_model,
            user_id=user_id,
            subject='ems',
            grade='grade-8',
            topic=topic,
            subskill=subskill,
            score=total_score,
            max_score=max_score,
            mode=mode,
            metadata=metadata,
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
            subject='ems',
            grade='grade-8',
            topic=topic,
        )

    return jsonify({
        'results': results,
        'total_score': total_score,
        'max_score': max_score,
        'progression': progression,
        'recommendations': recommendations,
    })


@grade8_ems_bp.route('/assessment', methods=['POST'])
def generate_assessment_paper():
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No JSON payload provided'}), 400

        term = data.get('term', 'term1')
        target_marks = data.get('target_marks', 50)
        mode = data.get('mode', 'assessment')
        
        from app.utils.grade8_ems.assessment_generator import generate_assessment
        questions = generate_assessment(term=term, target_marks=target_marks, mode=mode)
        
        return jsonify({
            'success': True,
            'term': term,
            'total_marks': sum(int(q.get('marks', 1)) for q in questions),
            'questions': questions
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
