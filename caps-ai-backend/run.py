from app import create_app
from app.utils.cache import cache

app = create_app()

# Initialize cache with app
cache.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
