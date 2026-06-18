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

    # Initialize global AI agent
    from .services.agent_service import initialize_agent
    initialize_agent(firestore_db=firestore_db)

    # Register blueprints
    from .api.math import math_bp
    from .api.accounting import accounting_bp
    # from .api.curriculum import curriculum_bp  # Temporarily disabled due to ChromaDB issues
    from .api.thumbnails import thumbnails_bp
    from .api.payments import payments_bp
    from .api.statistics import stats_bp
    from .api.grade10_business_studies import grade10_business_studies_bp
    from .api.grade11_business_studies import grade11_business_studies_bp
    from .api.grade12_business_studies import grade12_business_studies_bp
    from .api.agent import agent_bp
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
    # app.register_blueprint(curriculum_bp, url_prefix='/api/curriculum')  # Temporarily disabled
    app.register_blueprint(thumbnails_bp, url_prefix='/api/thumbnails')
    app.register_blueprint(payments_bp, url_prefix='/api/payments')
    app.register_blueprint(stats_bp, url_prefix='/api/statistics')
    app.register_blueprint(grade10_business_studies_bp, url_prefix='/api/business-studies/grade10')
    app.register_blueprint(grade11_business_studies_bp, url_prefix='/api/business-studies/grade11')
    app.register_blueprint(grade12_business_studies_bp, url_prefix='/api/business-studies/grade12')
    app.register_blueprint(agent_bp, url_prefix='/api/agent')
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

    return app
