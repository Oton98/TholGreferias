import threading
import time

class Cache:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls, *args, **kwargs)
                    cls._instance.__initialize()
        return cls._instance

    def __initialize(self):
        self.cache = {}
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            if key in self.cache:
                value, expiry_time = self.cache[key]
                if time.time() < expiry_time:
                    return value
                else:
                    # Remove expired item
                    del self.cache[key]
        return None

    def put(self, key, value, ttl):
        with self.lock:
            expiry_time = time.time() + ttl
            self.cache[key] = (value, expiry_time)

    def __cleanup_expired_items(self):
        with self.lock:
            current_time = time.time()
            keys_to_delete = [key for key, (value, expiry_time) in self.cache.items() if current_time >= expiry_time]
            for key in keys_to_delete:
                del self.cache[key]

    def cleanup(self):
        # This can be called periodically to cleanup expired items
        self.__cleanup_expired_items()