from pathlib import Path

import firebase_admin
from firebase_admin import auth, credentials, firestore
from flask import current_app


DEFAULT_SERVICE_ACCOUNT_FILE = 'caps-ai-math-assistant-app-firebase-adminsdk-fbsvc-16f0a819d2.json'


def _resolve_credentials_path():
    configured_path = current_app.config.get('FIREBASE_CREDENTIALS_PATH')
    if configured_path:
        path = Path(str(configured_path)).expanduser()
        if path.exists():
            return path
        raise RuntimeError(f'Firebase credentials file not found: {path}')

    fallback_path = Path(current_app.root_path).parent / DEFAULT_SERVICE_ACCOUNT_FILE
    if fallback_path.exists():
        return fallback_path

    return None


def get_firebase_app():
    import json
    import os
    try:
        return firebase_admin.get_app()
    except ValueError:
        # 1. Try JSON string from environment variable (Hugging Face Secrets)
        env_json = os.environ.get('FIREBASE_CREDENTIALS_JSON')
        if env_json:
            try:
                creds_dict = json.loads(env_json)
                return firebase_admin.initialize_app(credentials.Certificate(creds_dict))
            except json.JSONDecodeError as e:
                raise RuntimeError(f"Failed to parse FIREBASE_CREDENTIALS_JSON: {e}")

        # 2. Try file path
        credentials_path = _resolve_credentials_path()
        if credentials_path:
            return firebase_admin.initialize_app(credentials.Certificate(str(credentials_path)))
            
        # 3. Fallback to ADC
        return firebase_admin.initialize_app()


def verify_firebase_id_token(id_token):
    return auth.verify_id_token(id_token, app=get_firebase_app())


def get_firestore_client():
    return firestore.client(app=get_firebase_app())
