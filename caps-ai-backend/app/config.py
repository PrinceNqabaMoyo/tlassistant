import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
    FIREBASE_CREDENTIALS_PATH = os.environ.get('FIREBASE_CREDENTIALS_PATH')
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_SECRET_KEY = os.environ.get('SUPABASE_SECRET_KEY')
    SUPABASE_SERVICE_ROLE_KEY = os.environ.get('SUPABASE_SERVICE_ROLE_KEY')
    SUPABASE_POP_BUCKET = os.environ.get('SUPABASE_POP_BUCKET')
    CHROMA_DB_DIR = os.environ.get('CHROMA_DB_DIR', 'chroma_db_langchain')
    FIREBASE_APP_ID = os.environ.get('FIREBASE_APP_ID', 'default-app-id')
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
    
    # Flask settings
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    TESTING = os.environ.get('FLASK_TESTING', 'False').lower() == 'true'
