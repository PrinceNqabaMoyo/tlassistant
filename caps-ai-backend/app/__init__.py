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
        difficulty = data.get('difficulty', 'medium')
        mode = data.get('mode', 'compound')
        extra_config = {
            'mode': mode,
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
            return jsonify({
                "success": True,
                "questions": questions,
                "metadata": {
                    "subject": subject,
                    "grade": grade,
                    "topic": topic,
                    "resolved_key": resolve_generator_key(topic, grade=grade, subject=subject),
                    "seed": seed,
                    "total_questions": len(questions),
                }
            })
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400

    @app.route('/api/mark', methods=['POST'])
    def unified_mark():
        import asyncio
        from flask import request, jsonify
        from .services.evaluation_service import grade_submission

        data = request.get_json() or {}
        user_answer = data.get('user_answer')
        question = data.get('question') or {}
        q_id = str(data.get('question_id') or question.get('id') or 'q_active')

        # Ensure question has required fields for evaluation_service
        q_copy = dict(question)
        q_copy['id'] = q_id

        # Normalize question_type and correct keys
        if ('journal' in q_copy or 'table_schema' in q_copy) and not q_copy.get('question_type'):
            q_copy['question_type'] = 'journal'
        elif ('options' in q_copy or 'options_latex' in q_copy) and not q_copy.get('question_type'):
            q_copy['question_type'] = 'mcq'

        if 'correct_index' in q_copy and 'correct_idx' not in q_copy:
            q_copy['correct_idx'] = q_copy['correct_index']

        # If user_answer is wrapped in { cells: ... }
        clean_answer = user_answer
        if isinstance(user_answer, dict) and 'cells' in user_answer and isinstance(user_answer['cells'], dict):
            clean_answer = {**user_answer.get('cells', {}), **{k: v for k, v in user_answer.items() if k != 'cells'}}

        try:
            report = asyncio.run(grade_submission([q_copy], {q_id: clean_answer}))
            res = report.get('results', {}).get(q_id, {})
            score = res.get('score', 0)
            max_score = res.get('max_score', q_copy.get('marks', 1))
            is_correct = res.get('is_correct', False)
            pct = round((score / max_score) * 100) if max_score > 0 else 0
            return jsonify({
                "success": True,
                "score": score,
                "total": max_score,
                "percentage": pct,
                "is_correct": is_correct,
                "feedback": res.get('feedback', report.get('overall_feedback', '')),
                "cell_results": res.get('cell_results', {}),
            })
        except Exception as e:
            return jsonify({
                "success": False,
                "error": str(e),
                "score": 0,
                "total": q_copy.get('marks', 5),
                "percentage": 0,
                "is_correct": False,
                "feedback": f"Marking error: {e}",
            }), 200

    return app
