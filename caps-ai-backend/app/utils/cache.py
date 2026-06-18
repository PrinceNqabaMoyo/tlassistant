try:
    import redis
    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False

from functools import wraps
import pickle
import json
from flask import current_app
import time

class Cache:
    def __init__(self, app=None):
        self.app = app
        self.redis_client = None
        self.memory_cache = {}
        self.use_redis = False
        
        if app is not None:
            self.init_app(app)
    
    def init_app(self, app):
        """Initialize cache with Flask app"""
        if not REDIS_AVAILABLE:
            print("Redis not available, using memory cache")
            self.use_redis = False
            return
            
        try:
            redis_url = app.config.get('REDIS_URL', 'redis://localhost:6379/0')
            self.redis_client = redis.from_url(redis_url)
            # Test connection
            self.redis_client.ping()
            self.use_redis = True
            print("Redis cache initialized successfully")
        except Exception as e:
            print(f"Redis not available, using memory cache: {e}")
            self.use_redis = False
    
    def memoize(self, timeout=300):
        """Decorator for caching function results"""
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                # Create cache key
                cache_key = f"{f.__name__}:{hash(str(args) + str(kwargs))}"
                
                # Try to get from cache
                cached_result = self.get(cache_key)
                if cached_result is not None:
                    return cached_result
                
                # Execute function and cache result
                result = f(*args, **kwargs)
                self.set(cache_key, result, timeout)
                
                return result
            return decorated_function
        return decorator
    
    def get(self, key):
        """Get value from cache"""
        if self.use_redis and self.redis_client:
            try:
                cached_data = self.redis_client.get(key)
                if cached_data:
                    return pickle.loads(cached_data)
            except Exception as e:
                print(f"Redis get error: {e}")
        
        # Fallback to memory cache
        if key in self.memory_cache:
            item = self.memory_cache[key]
            if time.time() - item['timestamp'] < item['ttl']:
                return item['value']
            else:
                del self.memory_cache[key]
        
        return None
    
    def set(self, key, value, timeout=300):
        """Set value in cache"""
        if self.use_redis and self.redis_client:
            try:
                self.redis_client.setex(
                    key, 
                    timeout, 
                    pickle.dumps(value)
                )
                return
            except Exception as e:
                print(f"Redis set error: {e}")
        
        # Fallback to memory cache
        self.memory_cache[key] = {
            'value': value,
            'timestamp': time.time(),
            'ttl': timeout
        }
        
        # Clean up old entries
        self._cleanup_memory_cache()
    
    def delete(self, key):
        """Delete value from cache"""
        if self.use_redis and self.redis_client:
            try:
                self.redis_client.delete(key)
            except Exception as e:
                print(f"Redis delete error: {e}")
        
        # Also remove from memory cache
        if key in self.memory_cache:
            del self.memory_cache[key]
    
    def clear(self):
        """Clear all cache"""
        if self.use_redis and self.redis_client:
            try:
                self.redis_client.flushdb()
            except Exception as e:
                print(f"Redis clear error: {e}")
        
        # Clear memory cache
        self.memory_cache.clear()
    
    def _cleanup_memory_cache(self):
        """Remove expired entries from memory cache"""
        current_time = time.time()
        expired_keys = [
            key for key, item in self.memory_cache.items()
            if current_time - item['timestamp'] > item['ttl']
        ]
        
        for key in expired_keys:
            del self.memory_cache[key]

# Create global cache instance
cache = Cache()
