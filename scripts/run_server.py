import sys
import os

# Change working dir to caps-ai-backend
os.chdir("caps-ai-backend")
sys.path.insert(0, ".")

print("Starting backend...")
from app import create_app
from app.utils.cache import cache

app = create_app()
cache.init_app(app)

print("App created and cache initialized. Running app on port 5001...")
app.run(host='0.0.0.0', debug=False, use_reloader=False, port=5001, threaded=True)
