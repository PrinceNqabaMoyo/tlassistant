"""
Fundile Learning API - Unified FastAPI ASGI Application
Standardizes all endpoints under ASGI concurrency, with non-blocking async workers and security guardrails.
"""

import os
import sys
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Add backend directory to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from app.utils.firebase_admin_client import get_firestore_client
from app.api.grade10_accounting import router as grade10_acct_router
from app.api.session import router as session_router
from app.api.trial import router as trial_router
from app.api.classes import router as classes_router
from app.api.notifications import router as notifications_router
from app.api.olympiad import router as olympiad_router
from app.api.gamification import router as gamification_router
from app.api.generate import router as generate_router

# Initialize FastAPI App
app = FastAPI(
    title="Fundile Learning API",
    description="Adaptive learning backend for South African high school curriculum",
    version="0.4.0",
)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Firebase
firestore_db = None
try:
    firestore_db = get_firestore_client()
    print("[INIT] Firebase Admin SDK / Firestore initialized.")
except Exception as e:
    print(f"[INIT WARNING] Firebase Admin SDK not initialized: {e}")

# Include Native FastAPI Routers
app.include_router(grade10_acct_router, prefix="/api/accounting/grade10", tags=["Accounting Grade 10"])
app.include_router(session_router, prefix="/api/session", tags=["Session Audit"])
app.include_router(trial_router, prefix="/api/trial", tags=["Trial & Subscription"])
app.include_router(classes_router, prefix="/api/classes", tags=["Teacher LMS Cockpit"])
app.include_router(notifications_router, tags=["Notifications"])
app.include_router(olympiad_router, tags=["Olympiad Track"])
app.include_router(gamification_router, tags=["Gamification & Credentials"])
app.include_router(generate_router)

# Health Check & Root Endpoints
@app.get("/")
async def root():
    return {
        "status": "ok",
        "app": "Fundile Learning API",
        "mode": "FastAPI ASGI",
        "version": "0.4.0",
    }

@app.get("/api/health")
async def health():
    return {
        "status": "healthy",
        "firestore_connected": firestore_db is not None,
        "engine": "FastAPI ASGI",
    }

# Try mounting existing Flask WSGI blueprints for seamless backward compatibility
try:
    from starlette.middleware.wsgi import WSGIMiddleware
    from app import create_app
    flask_app = create_app()
    app.mount("/api/v1", WSGIMiddleware(flask_app))
    print("[INIT] Mounted Flask WSGI compatibility layer at /api/v1")
except Exception as e:
    print(f"[INIT NOTE] WSGIMiddleware mounting skipped: {e}")
