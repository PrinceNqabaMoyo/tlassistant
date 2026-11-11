import sys
import os
os.chdir("caps-ai-backend")
sys.path.insert(0, ".")

print("Testing firebase app...", flush=True)
from app.utils.firebase_admin_client import get_firebase_app
app = get_firebase_app()
print(f"Firebase app: {app.name}", flush=True)

print("Testing firestore client...", flush=True)
from firebase_admin import firestore
db = firestore.client(app=app)
print("Firestore client created!", flush=True)
