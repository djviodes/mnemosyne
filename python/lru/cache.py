"""
Implements an in-memory cache using least-recently-used (LRU) eviction.
"""


class LRUCache:
    """Creates a Cache instance
    
    Args:
        max_size (int): The maximum number of items the cache can hold. Defaults to 1000.
    """

    def __init__(self, max_size: int = 1000):
        # The internal Map storing key-value pairs and their max size metadata.
        self.cache = {}

        # Maximum capacity of the cache
        if max_size < 1:
            raise ValueError("Max size must be larger than or equal to 1")

        self.max_size = max_size

    def put(self, key: str, value: str):
        """Adds a key-value pair to the cache. If the cache is full, the least recently used (LRU)
        item is evicted.
            
        Args:
            key (str): The key for the pair.
            value (str): The value to store.
        """

        # If the key already exists, delete it first to refresh its insertion order (LRU)
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) >= self.max_size:
            # Evict the oldest (first) item in the Map
            oldest_key = next(iter(self.cache.keys()))
            del self.cache[oldest_key]

        self.cache[key] = value

    def get(self, key: str):
        """Retrieves the value for the given key from the cache, if it exists.
        Refreshes the item's insertion order (LRU)
        
        Args:
            key (str): The key to look up.
        
        Returns:
            The cached value, or none if the key is missing.
        """
        if key in self.cache:
            cached = self.cache[key]

            # Refresh insertion order (LRU): delete and re-insert
            del self.cache[key]
            self.cache[key] = cached

            return cached

        return None

    def has(self, key: str):
        """Checks if a key exists in the cache.
        Does not update the LRU order (view-only check).
            
        Args:
            key (str): The key to check.
        
        Returns:
            (bool): True if the key exists, false otherwise.
        """
        if key in self.cache:
            return True

        return False

    def delete(self, key: str):
        """Removes the key-value pair with the given key from the cache.
            
        Args:
            key (str): The key to remove.
        
        Returns:
            (bool): True if the key was found and removed, false otherwise.
        """
        if key in self.cache:
            del self.cache[key]

            return True
        else:
            return False

    def clear(self):
        """
        Removes all key-value pairs from the cache.
        """
        self.cache.clear()

    def keys(self):
        """Returns an array of all active keys in the cache.
            
        Returns:
            (list): A list of active keys
        """
        active_keys = []

        for key in self.cache.keys():
            active_keys.append(key)

        return active_keys

    def size(self):
        """Returns the number of active key-value pairs currently in the cache.
        
        Returns:
            (int): The count of active items.
        """
        return len(self.cache)
