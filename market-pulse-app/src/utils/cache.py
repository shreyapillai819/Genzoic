from functools import wraps
from time import time

_cache = {}

def cache(ttl=600):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args):
            key = (func.__name__, args)
            if key in _cache:
                result, expiry = _cache[key]
                if time() < expiry:
                    return result
            result = await func(*args)
            _cache[key] = (result, time() + ttl)
            return result
        return wrapper
    return decorator