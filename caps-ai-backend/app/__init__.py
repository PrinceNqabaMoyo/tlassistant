def create_app():
    try:
        from flask import Flask
        from flask_cors import CORS
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "Missing optional dependency required to run the API server. Install 'flask' (and 'flask-cors') to use create_app()."
        ) from e

    try:
        from .config import Config
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "Missing optional dependency required to run the API server configuration. Install 'python-dotenv' to use create_app()."
        ) from e

    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Initialize Firebase Admin SDK and Firestore
    try:
        from .utils.firebase_admin_client import get_firestore_client
        firestore_db = get_firestore_client()
        print("Firebase Admin SDK / Firestore initialized successfully.")
    except Exception as e:
        print(f"Warning: Firebase Admin SDK initialization failed: {e}")
        firestore_db = None

    # Initialize LLM Rate Limiter with Firestore
    if firestore_db:
        try:
            from .utils.llm_rate_limiter import init_firestore as init_llm_rate_limiter
            init_llm_rate_limiter(firestore_db)
            print("LLM Rate Limiter initialized with Firestore.")
        except Exception as e:
            print(f"Warning: Could not initialize LLM Rate Limiter: {e}")

    # Initialize global AI agent and orchestrator
    from .services.agent_service import initialize_agent
    initialize_agent(firestore_db=firestore_db)
    from .services.orchestrator_service import initialize_orchestrator
    initialize_orchestrator(firestore_db=firestore_db)

    # Register blueprints
    from .api.math import math_bp
    from .api.accounting import accounting_bp
    from .api.curriculum import curriculum_bp
    from .api.thumbnails import thumbnails_bp
    from .api.payments import payments_bp
    from .api.statistics import stats_bp
    from .api.grade10_business_studies import grade10_business_studies_bp
    from .api.grade11_business_studies import grade11_business_studies_bp
    from .api.grade12_business_studies import grade12_business_studies_bp
    from .api.grade10_mathematics import grade10_mathematics_bp
    from .api.agent import agent_bp
    from .api.orchestrator import orchestrator_bp
    from .api.journals import journals_bp
    from .api.evaluation import evaluation_bp
    from .api.teacher import teacher_bp
    from .api.admin import admin_bp
    from .api.school_admin import school_admin_bp
    from .api.grade7_ems import grade7_ems_bp
    from .api.grade8_ems import grade8_ems_bp
    from .api.grade9_ems import grade9_ems_bp

    app.register_blueprint(math_bp, url_prefix='/api/math')
    app.register_blueprint(accounting_bp, url_prefix='/api/accounting')
    app.register_blueprint(curriculum_bp, url_prefix='/api/curriculum')
    app.register_blueprint(thumbnails_bp, url_prefix='/api/thumbnails')
    app.register_blueprint(payments_bp, url_prefix='/api/payments')
    app.register_blueprint(stats_bp, url_prefix='/api/statistics')
    app.register_blueprint(grade10_business_studies_bp, url_prefix='/api/business-studies/grade10')
    app.register_blueprint(grade11_business_studies_bp, url_prefix='/api/business-studies/grade11')
    app.register_blueprint(grade12_business_studies_bp, url_prefix='/api/business-studies/grade12')
    app.register_blueprint(grade10_mathematics_bp, url_prefix='/api/mathematics/grade10')
    app.register_blueprint(agent_bp, url_prefix='/api/agent')
    app.register_blueprint(orchestrator_bp, url_prefix='/api/orchestrator')
    app.register_blueprint(journals_bp, url_prefix='/api/journals')
    app.register_blueprint(evaluation_bp, url_prefix='/api')
    app.register_blueprint(teacher_bp, url_prefix='/api/teacher')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(school_admin_bp, url_prefix='/api/school-admin')
    app.register_blueprint(grade7_ems_bp, url_prefix='/api/grade7/ems')
    app.register_blueprint(grade8_ems_bp, url_prefix='/api/grade8/ems')
    app.register_blueprint(grade9_ems_bp, url_prefix='/api/grade9/ems')

    @app.route('/')
    def health_check():
        return {"status": "ok", "message": "TLAssistant Backend API is running."}

    @app.route('/api/generate', methods=['GET', 'POST'])
    def unified_generate():
        from flask import request, jsonify
        from .services.generator_registry import generate_variant, resolve_generator_key
        if request.method == 'GET':
            data = request.args.to_dict()
        else:
            data = request.get_json() or {}
        subject = data.get('subject', 'Mathematics')
        grade = str(data.get('grade', '10'))
        topic = data.get('topic', 'Algebraic Expressions')
        count = int(data.get('count', 1))
        seed_raw = data.get('seed')
        try:
            seed = int(seed_raw) if seed_raw is not None else None
        except (ValueError, TypeError):
            seed = None
        subskill = data.get('subskill', 'mixed')
        difficulty = data.get('difficulty') or 'auto'
        mode = data.get('mode') or 'auto'
        stage = data.get('stage')
        diag_step_raw = data.get('diagnostic_step')
        try:
            diag_step = int(diag_step_raw) if diag_step_raw is not None else None
        except (ValueError, TypeError):
            diag_step = None
        extra_config = {
            'mode': mode,
            'stage': stage,
            'diagnostic_step': diag_step,
            'exam_type': data.get('exam_type'),
            'paper': data.get('paper', 1),
            'term': data.get('term', 1),
        }
        try:
            questions = generate_variant(
                topic=topic,
                subskill=subskill,
                difficulty=difficulty,
                count=count,
                seed=seed,
                grade=grade,
                subject=subject,
                extra_config=extra_config,
            )
            try:
                from .services.audit_logger import log_question_generation
                log_question_generation(subject, grade, topic, questions, seed=seed)
            except Exception:
                pass
            return jsonify({
                "success": True,
                "questions": questions,
                "metadata": {
                    "subject": subject,
                    "grade": grade,
                    "topic": topic,
                    "resolved_key": resolve_generator_key(topic, grade=grade, subject=subject),
                    "seed": seed,
                    "stage": stage or "practice",
                    "total_questions": len(questions),
                }
            })
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    @app.route('/api/curriculum/archetypes', methods=['GET'])
    def curriculum_archetypes_endpoint():
        from flask import request, jsonify
        from .services.generator_registry import get_curriculum_archetypes_catalog, get_topic_archetypes
        subject = request.args.get('subject')
        grade = request.args.get('grade')
        topic = request.args.get('topic')
        try:
            if topic and subject and grade:
                info = get_topic_archetypes(topic=topic, grade=str(grade), subject=subject)
                return jsonify({"success": True, "topics": [info], "total_topics": 1})
            catalog = get_curriculum_archetypes_catalog(subject=subject, grade=grade)
            total_archetypes = sum(len(item.get("archetypes", [])) for item in catalog)
            return jsonify({
                "success": True,
                "topics": catalog,
                "total_topics": len(catalog),
                "total_archetypes": total_archetypes,
            })
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    @app.route('/api/offline/pack', methods=['POST'])
    def generate_offline_pack_endpoint():
        from flask import request, jsonify
        from .services.offline_pack_service import build_offline_study_pack
        data = request.get_json() or {}
        subject = data.get('subject', 'Mathematics')
        grade = str(data.get('grade', '10'))
        term = int(data.get('term', 1))
        count = int(data.get('count_per_topic', data.get('count', 5)))
        topics = data.get('topics')
        student_id = data.get('student_id')
        try:
            pack = build_offline_study_pack(
                subject=subject,
                grade=grade,
                term=term,
                count_per_topic=count,
                custom_topics=topics,
                student_id=student_id
            )
            return jsonify(pack)
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    @app.route('/api/offline/sync', methods=['POST'])
    def sync_offline_attempts_endpoint():
        import time
        from flask import request, jsonify
        data = request.get_json() or {}
        attempts = data.get('attempts', [])
        return jsonify({
            "success": True,
            "synced_count": len(attempts),
            "received_at": time.time()
        })

    @app.route('/api/mark', methods=['POST'])
    def unified_mark():
        import asyncio
        from flask import request, jsonify
        from .services.evaluation_service import grade_submission

        data = request.get_json() or {}
        user_answer = data.get('user_answer')
        question = data.get('question') or {}
        q_id = str(data.get('question_id') or question.get('id') or 'q_active')

        # Clean answer first so clean_answer is always bound
        clean_answer = user_answer
        if isinstance(user_answer, dict) and 'cells' in user_answer and isinstance(user_answer['cells'], dict):
            clean_answer = {**user_answer.get('cells', {}), **{k: v for k, v in user_answer.items() if k != 'cells'}}

        # Ensure question has required fields for evaluation_service
        q_copy = dict(question)
        q_copy['id'] = q_id

        # Normalize question_type and correct keys
        if ('journal' in q_copy or 'table_schema' in q_copy) and not q_copy.get('question_type'):
            q_copy['question_type'] = 'journal'
        elif ('options' in q_copy or 'options_latex' in q_copy) and not q_copy.get('question_type'):
            q_copy['question_type'] = 'mcq'
        elif ('arithmetic_grid' in q_copy and q_copy.get('arithmetic_grid') or (isinstance(clean_answer, dict) and 'quotient' in clean_answer)) and not q_copy.get('modality'):
            q_copy['modality'] = 'arithmetic_grid'

        if 'correct_index' in q_copy and 'correct_idx' not in q_copy:
            q_copy['correct_idx'] = q_copy['correct_index']

        try:
            report = asyncio.run(grade_submission([q_copy], {q_id: clean_answer}))
            res = report.get('results', {}).get(q_id, {})
            score = res.get('score', 0)
            max_score = res.get('max_score', q_copy.get('marks', 1))
            is_correct = res.get('is_correct', False)
            pct = round((score / max_score) * 100) if max_score > 0 else 0
            eval_res = {
                "success": True,
                "score": score,
                "total": max_score,
                "max_score": max_score,
                "percentage": pct,
                "is_correct": is_correct,
                "feedback": res.get('feedback', report.get('overall_feedback', '')),
                "cell_results": res.get('cell_results', {}),
                "misconception_tag": res.get('misconception_tag'),
            }
            try:
                from .services.audit_logger import log_answer_evaluation
                log_answer_evaluation(q_id, clean_answer, eval_res)
            except Exception:
                pass
            return jsonify(eval_res)
        except Exception as e:
            return jsonify({
                "success": False,
                "error": str(e),
                "score": 0,
                "total": q_copy.get('marks', 5),
                "max_score": q_copy.get('marks', 5),
                "percentage": 0,
                "is_correct": False,
                "feedback": f"Marking error: {e}",
            }), 200

    @app.route('/api/audit/bkt-dossier', methods=['POST'])
    def bkt_dossier_audit_endpoint():
        import asyncio
        from flask import request, jsonify
        from .services.bkt_dossier_service import simulate_persona_topic_dossier

        data = request.get_json() or {}
        grade = str(data.get('grade', '10'))
        subject = data.get('subject', 'Mathematics')
        topic = data.get('topic', 'Algebraic Expressions')
        personas = data.get('personas') or (
            [data['persona']] if data.get('persona') else ['high-performing', 'medium-performing', 'low-performing']
        )
        practice_count = max(50, int(data.get('practice_count', 50)))
        exams_count = max(3, int(data.get('exams_count', 3)))
        questions_per_exam = max(1, int(data.get('questions_per_exam', 5)))

        try:
            async def _run_all():
                results = []
                for p in personas:
                    res = await simulate_persona_topic_dossier(
                        grade=grade,
                        subject=subject,
                        topic=topic,
                        persona=p,
                        practice_count=practice_count,
                        exams_count=exams_count,
                        questions_per_exam=questions_per_exam,
                    )
                    results.append(res)
                return results

            dossiers = asyncio.run(_run_all())
            return jsonify({
                "success": True,
                "grade": grade,
                "subject": subject,
                "topic": topic,
                "dossiers": dossiers,
            })
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    return app

