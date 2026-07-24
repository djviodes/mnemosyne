"""
Implements an in-memory cache using least-recently-used (LRU) eviction.
"""

from python.data_structures.doubly_linked_list import DoublyLinkedList


class LRUCache:
    """Creates a Cache instance
    
    Args:
        max_size (int): The maximum number of items the cache can hold. Defaults to 1000.
    """

    def __init__(self, max_size: int = 1000):
        # The internal Map storing key-value pairs and their max size metadata.
        self.cache = {}

        # The internal Doubly Linked List initialized with no nodes
        self.doubly_linked_list = DoublyLinkedList()

        # Maximum capacity of the cache
        if max_size < 1:
            raise ValueError("Max size must be larger than or equal to 1")

        self.max_size = max_size

    def put(self, key: str, value: str):
        """Adds a key-value pair to the cache. If the cache is full, the least recently used (LRU)
        item is evicted.
            
        Args:
            key (str): The key for the pair.
            value (str): The value to store in the node.
        """
        # If the node already exists, move it to the front to refresh its insertion order (LRU)
        if key in self.cache:
            self.doubly_linked_list.remove_node(target_node=self.cache[key])

            self.cache[key].data = value
            self.doubly_linked_list.move_to_front(target_node=self.cache[key])

            return
        # Evict the oldest (last) item in the Map and Doubly Linked List
        elif len(self.cache) >= self.max_size:
            oldest_node = self.doubly_linked_list.last_node

            self.doubly_linked_list.remove_node(target_node=oldest_node)
            del self.cache[oldest_node.key]

        new_node = self.doubly_linked_list.insert_at_front(key=key, value=value)
        self.cache[key] = new_node

    def get(self, key: str) -> str:
        """Retrieves the node for the given key from the cache, if it exists.
        Refreshes the item's insertion order (LRU)
        
        Args:
            key (str): The key to look up.
        
        Returns:
            The cached node, or none if the key is missing.
        """
        if key in self.cache:
            cached_node = self.cache[key]

            # Refresh insertion order (LRU): delete and re-insert
            self.doubly_linked_list.remove_node(target_node=cached_node)
            del self.cache[key]

            self.cache[key] = cached_node
            self.doubly_linked_list.move_to_front(target_node=cached_node)

            return cached_node.data

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
            self.doubly_linked_list.remove_node(self.cache[key])
            del self.cache[key]

            return True
        else:
            return False

    def clear(self):
        """
        Removes all key-value pairs from the cache.
        """
        self.doubly_linked_list.clear_doubly_linked_list()
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
