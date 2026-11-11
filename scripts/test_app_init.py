import sys
import os

print("Step 1: chdir", flush=True)
os.chdir("caps-ai-backend")
sys.path.insert(0, ".")

print("Step 2: importing create_app", flush=True)
from app import create_app
print("Step 3: calling create_app", flush=True)
app = create_app()
print("Step 4: create_app returned", flush=True)
from app.utils.cache import cache
cache.init_app(app)
print("Step 5: cache init done", flush=True)
