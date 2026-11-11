import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.utils.cache import cache

app = create_app()

# Initialize cache with app
cache.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, use_reloader=False, port=5001, threaded=True)
